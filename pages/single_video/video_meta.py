from pages.base import Component
import utils


class VideoMeta(Component):

    X_VIDEO_TITLE = "//*[contains(@class, 'vp-layer-info')]/div[contains(@class,'textWrap')]"
    X_COMMENT_DIALOG_OPEN = "//div[contains(@class, 'vp-layer-info')]//*[contains(@data-module,'CommentWidgets')]"
    X_COMMENT_NUM = "{}/*[contains(@class,'widget_count')]".format(X_COMMENT_DIALOG_OPEN)
    X_SHARE_DIALOG_OPEN = "//*[contains(@class, 'vp-layer-info')]//*[contains(@data-type,'RESHARE')]"
    X_SHARE_NUM = "{}/*[contains(@class,'widget_count')]".format(X_SHARE_DIALOG_OPEN)
    X_CLASS_BUTTON = "//*[contains(@class, 'vp-layer-info')]//*[contains(@data-type,'MOVIE')]"
    X_CLASS_NUM = "/*[contains(@class,'widget_count')"
    X_DATE = "//*[contains(@class, 'vp-layer-info_cnt')]//*[contains(@class,'vp-layer-info_date')]"
    X_VIEWS = "//*[contains(@class, 'vp-layer-info_cnt')]//*[contains(@class,'vp-layer-info_views')]"
    X_AUTHOR_CHANNEL_LINK = "//*[contains(@class,'ucard_info')]//*[contains(@class,'js-video-album-link')]"
    X_AUTHOR_NAME = "//*[contains(@class,'ucard_info')]//*[contains(@href,'profile')]"
    X_SUBSCRIBERS_NUM = "//*[contains(@class, 'vp-layer-channel_ac_count')]"
    X_SUBSCRIBE_BUTTON = "//*[@class = 'vp-layer-channel_ac']//button"
    X_DESCRIPTION = "//*[@class = 'vp-layer-description']//*[contains(@class, 'textWrap')]/span"
    X_EXPAND_DESCRIPTION = "//*[contains(@class, 'js-vp-layer-description_more')]"
    X_CLOSE_VIDEO = "//*[contains(@class,'media-layer_close_ico')]"
    X_MINIMIZE_VIDEO = "//*[contains(@class,'media-layer_turn_ico')]"

    def __init__(self, driver):
        super(VideoMeta, self).__init__(driver)
        self.updateElementsBindings()

    def updateElementsBindings(self):
        self.EL_VIDEO_TITLE = utils.wait_xpath(self.driver, self.X_VIDEO_TITLE)
        self.EL_COMMENT_DIALOG_OPEN = utils.wait_xpath(self.driver, self.X_COMMENT_DIALOG_OPEN)
        self.EL_COMMENT_NUM = utils.wait_xpath(self.driver, self.X_COMMENT_NUM)
        self.EL_SHARE_DIALOG_OPEN = utils.wait_xpath(self.driver, self.X_SHARE_DIALOG_OPEN)
        self.EL_SHARE_NUM = utils.wait_xpath(self.driver, self.X_SHARE_NUM)
        self.EL_CLASS_BUTTON = utils.wait_xpath(self.driver, self.X_CLASS_BUTTON)
        self.EL_CLASS_NUM = utils.wait_xpath(self.driver, self.X_CLASS_NUM)
        self.EL_DATE = utils.wait_xpath(self.driver, self.X_DATE)
        self.EL_VIEWS = utils.wait_xpath(self.driver, self.X_VIEWS)
        self.EL_AUTHOR_CHANNEL_LINK = utils.wait_xpath(self.driver, self.X_AUTHOR_CHANNEL_LINK)
        self.EL_AUTHOR_NAME = utils.wait_xpath(self.driver, self.X_AUTHOR_NAME)
        self.EL_SUBSCRIBERS_NUM = utils.wait_xpath(self.driver, self.X_SUBSCRIBERS_NUM)
        self.EL_SUBSCRIBE_BUTTON = utils.wait_xpath(self.driver, self.X_SUBSCRIBE_BUTTON)
        self.EL_DESCRIPTION = utils.wait_xpath(self.driver, self.X_DESCRIPTION)
        self.EL_EXPAND_DESCRIPTION = utils.wait_xpath(self.driver, self.X_EXPAND_DESCRIPTION)
        self.EL_CLOSE_VIDEO = utils.wait_xpath(self.driver, self.X_CLOSE_VIDEO)
        self.EL_MINIMIZE_VIDEO = utils.wait_xpath(self.driver, self.X_MINIMIZE_VIDEO)