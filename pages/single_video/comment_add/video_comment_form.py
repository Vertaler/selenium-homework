from pages.base import Component
import utils


class VideoCommentForm(Component):

    # without smiles yet
    X_INPUT_FIELD = "//*[contains(@class, 'js-comments_add')]"
    X_ADD_COMMENT_BUTTON = "//*[contains(@class, 'comments_add-controls_save')]"
    X_ATTACH_VIDEO = "//*[contains(@class, 'sc-menu ')]//li[1]//a"
    X_ATTACH_PHOTO = "//*[contains(@class, 'sc-menu ')]//li[2]//a"
    X_ATTACH_PHOTO_FROM_PC = "//*[contains(@class, 'sc-menu ')]//li[3]//a"

    def __init__(self, driver):
        super(VideoCommentForm, self).__init__(driver)
        self.updateElementsBindings()

    def updateElementsBindings(self):
        self.EL_INPUT_FIELD = utils.wait_xpath(self.driver, self.X_INPUT_FIELD)
        self.EL_ADD_COMMENT_BUTTON = utils.wait_xpath(self.driver, self.X_ADD_COMMENT_BUTTON)
        self.EL_ATTACH_VIDEO = utils.wait_xpath(self.driver, self.X_ATTACH_VIDEO)
        self.EL_ATTACH_PHOTO = utils.wait_xpath(self.driver, self.X_SHARE_DIALOG_OPEN)
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