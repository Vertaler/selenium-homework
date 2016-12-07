from pages.base import Component
import utils


class VideoCommentDialog(Component):

    X_INPUT_FIELD = "//*[@id='ok-e-d']"
    X_ADD_COMMENT_BUTTON = "//*[@id='ok-e-d_button']"
    X_CLOSE_ICON = "//*[@class='mdialog_disc_controls_close']"

    def __init__(self, driver):
        super(VideoCommentDialog, self).__init__(driver)
        self.updateElementsBindings()

    def updateElementsBindings(self):
        self.EL_INPUT_FIELD = utils.wait_xpath(self.driver, self.X_INPUT_FIELD)
        self.EL_ADD_COMMENT_BUTTON = utils.wait_xpath(self.driver, self.X_ADD_COMMENT_BUTTON)
        self.EL_CLOSE_ICON = utils.wait_xpath(self.driver, self.X_CLOSE_ICON)

    def attachPhoto(self):
        utils.click_directly(self.driver, self.EL_ATTACH)
        utils.click_directly(self.driver, self.EL_ATTACH_PHOTO)
        APD = AttachPhotoDialog(self.driver)
        APD.selectFirstPhoto()

    def attachVideo(self):
        utils.click_directly(self.driver, self.EL_ATTACH)
        utils.click_directly(self.driver, self.EL_ATTACH_VIDEO)
        AVD = AttachVideoDialog(self.driver)
        AVD.selectFirstVideo()

    def setCommentText(self, text):
        #ActionChains(self.driver).move_to_element(self.EL_INPUT_FIELD).send_keys(text)
        self.driver.execute_script("arguments[0].innerHTML = '{}'".format(text), self.EL_INPUT_FIELD)
        pass

    def submit(self):
        utils.click_directly(self.driver, self.EL_ADD_COMMENT_BUTTON)
