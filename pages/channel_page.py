# -*- coding: utf-8 -*-
from urlparse import urlsplit

import utils
from video_page import VideoPage
from .base import Page, Component


# CLEAR_FIELD =Keys.BACKSPACE * 100

class ChannelPage(Page):
    DELETE_BUTTON_CLASS = 'vl_ic_delete'
    DELETE_VIDEO_SUBMIT_XPATH = '//input[@value="Удалить"]'
    CHANNEL_NAME_CLASS = 'mml_ucard_n_g'
    EDIT_BUTTON_CLASS = 'vl_ic_edit'
    ADD_VIDEO_CLASS = 'vl_ic_add-video'
    CONFIRM_DELETE_XPATH = '//input[@value="Удалить"]'
    VIDEOS_LINKS_XPATH = '//div[@class="vid-card js-sortable"]/child::a'  # TODO Исправить
    DELETE_FIRST_VIDEO_XPATH = '//a[@class="vid-card_ac_i ic vl_ic_delete"]'
    #TODO Упростить
    CHANGE_VIDEO_XPATH_TEMPLATE = '//div[@class="vid-card js-sortable"]/child::a[@title="{}"]/following-sibling::' \
                                  'div[@class="vid-card_ac"]/descendant::a[@class="vid-card_ac_i ic vl_ic_{}"]'
    DELETE_VIDEO_XPATH_TEMPLATE = CHANGE_VIDEO_XPATH_TEMPLATE.format('{}','delete')
    EDIT_VIDEO_XPATH_TEMPLATE = CHANGE_VIDEO_XPATH_TEMPLATE.format('{}','edit')
    EDIT_FIRST_VIDEO_XPATH = '//a[@class="vid-card_ac_i ic vl_ic_edit"]'
    VIDEO_LINK_CLASS = 'vid-card_img__link'
    VIDEO_LINK_XPATH = '//a[@title="{}"]'

    def __init__(self, driver, path):
        super(ChannelPage, self).__init__(driver)
        self.PATH = path

    def delete_channel(self):
        utils.wait_class(self.driver, self.DELETE_BUTTON_CLASS).click()
        confirm_delete = utils.wait_xpath(self.driver, self.CONFIRM_DELETE_XPATH)
        confirm_delete.click()
        utils.wait_change_url(self.driver)

    def channel_name(self):
        name_elem = utils.wait_name(self.driver, self.CHANNEL_NAME_CLASS)
        return name_elem.text

    def click_edit(self):
        utils.wait_class(self.driver, self.EDIT_BUTTON_CLASS).click()
        return ChangeChannelDialog(self.driver)

    def click_add_video(self):
        utils.wait_class(self.driver, self.ADD_VIDEO_CLASS).click()
        return AddVideoDialog(self.driver)

    def add_video_by_url(self, url):
        add_video_dialog = self.click_add_video()
        add_video_dialog.choose_add_from_internet()
        add_video_dialog.set_url(url)
        return add_video_dialog.submit()

    def edit_channel(self, new_name):
        old_name = self.channel_name()
        change_channel_dialog = self.click_edit()
        change_channel_dialog.set_channel_name(new_name)
        page = change_channel_dialog.submit()
        self.wait_change(old_name)
        return page

    def delete_video_by_name(self, name):  # TODO
        delete_button = utils.wait_xpath(self.driver, self.DELETE_VIDEO_XPATH_TEMPLATE.format(name))
        self.driver.execute_script('arguments[0].click();', delete_button)
        utils.wait_xpath(self.driver, self.DELETE_VIDEO_SUBMIT_XPATH).click()
        self.wait_clickable()
        return self

    def delete_video(self):
        delete_button = utils.wait_xpath(self.driver, self.DELETE_FIRST_VIDEO_XPATH)
        self.driver.execute_script('arguments[0].click();', delete_button)
        utils.wait_xpath(self.driver, self.DELETE_VIDEO_SUBMIT_XPATH).click()
        self.wait_clickable()
        return self

    def click_edit_video(self, name):
        edit_button = utils.wait_xpath(self.driver, self.EDIT_VIDEO_XPATH_TEMPLATE.format(name))
        self.driver.execute_script('arguments[0].click();', edit_button)
        return EditVideoDialog(self.driver)

    def edit_video(self,name ,title=None, description=None, tags=None):
        edit_video_dialog = self.click_edit_video(name)
        if title is not None:
            edit_video_dialog.set_title(title)
        if description is not None:
            edit_video_dialog.set_description(description)
        if tags is not None:
            edit_video_dialog.set_tags(tags)
        page = edit_video_dialog.submit()
        self.wait_clickable()
        return page

    def wait_change(self, old_name):
        utils.wait(self.driver, lambda d: self.channel_name() != old_name)

    def get_videos_elements(self):
        return utils.wait_many_xpath(self.driver, self.VIDEOS_LINKS_XPATH)

    def get_videos_titles(self):
        return [v.get_attribute('title') for v in self.get_videos_elements()]

    def get_videos_links(self):
        return [v.get_attribute('href') for v in self.get_videos_elements()]

    # def open_video(self):
    #    link = utils.wait_class(self.driver, self.VIDEO_LINK_CLASS)
    #
    #    return VideoPage('')

    # def  open_video_by_name(self, name):
    #    link = utils.wait_class(self.driver, self.VIDEO_LINK_XPATH.format(name))



    def open_video_by_link(self, link):
        return VideoPage(link)

    def wait_clickable(self):
        # condition = (By.CLASS_NAME, self.EDIT_BUTTON_CLASS)
        # utils.wait(self.driver, EC.element_to_be_selected(condition) )
        self.open()  # TODO Сделать по-нормальному


class ChangeChannelDialog(Component):
    CHANNEL_NAME_XPATH = '//input[@name="st.vv_albumName"]'
    CHANNEL_SUBMIT_XPATH = '//input[@value="Сохранить"]'

    def set_channel_name(self, name):
        name_elem = utils.wait_xpath(self.driver, self.CHANNEL_NAME_XPATH)
        # name_elem.clear()
        utils.replace_text(name_elem, name)

    def submit(self):
        utils.wait_xpath(self.driver, self.CHANNEL_SUBMIT_XPATH).click()
        path = urlsplit(self.driver.current_url).path
        page = ChannelPage(self.driver, path)
        return page


class AddVideoDialog(Component):
    FROM_INTERNET_XPATH = '//span[@data-target="video_uploader_link"]'
    VIDEO_URL_XPATH = '//input[@name="st.vv_ugLink"]'
    ADD_VIDEO_XPATH = '//div[@class="form-actions video_uploader_actions"]/child::button[text()="Добавить"]'

    def choose_add_from_internet(self):
        utils.wait_xpath(self.driver, self.FROM_INTERNET_XPATH).click()

    def set_url(self, url):
        utils.wait_xpath(self.driver, self.VIDEO_URL_XPATH).send_keys(url)

    def submit(self):
        utils.wait_xpath(self.driver, self.ADD_VIDEO_XPATH).click()
        path = urlsplit(self.driver.current_url).path
        page = ChannelPage(self.driver, path)
        return page


class EditVideoDialog(Component):
    EDIT_SUBMIT_XPATH = '//input[@value="Сохранить"]'
    MOVIE_TITLE_NAME = 'st.vv_movieTitle'
    MOVIE_DESCRIPTION_NAME = 'st.vv_movieDescription'
    TAG_INPUT_CLASS = 'tag_it'

    def set_title(self, title):
        title_input = utils.wait_name(self.driver, self.MOVIE_TITLE_NAME)
        utils.replace_text(title_input, title)

    def set_tags(self, tags):
        tags_input = utils.wait_class(self.driver, self.TAG_INPUT_CLASS)
        utils.replace_text(tags_input, tags)

    def set_description(self, description):
        description_input = utils.wait_name(self.driver, self.MOVIE_DESCRIPTION_NAME)
        utils.replace_text(description_input, description)

    def submit(self):
        utils.wait_xpath(self.driver, self.EDIT_SUBMIT_XPATH).click()
        path = urlsplit(self.driver.current_url).path
        page = ChannelPage(self.driver, path)
        return page