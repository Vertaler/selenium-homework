from pages.base import Component
import utils
from attach_photo_dialog import AttachPhotoDialog
from attach_video_dialog import AttachVideoDialog


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
        self.EL_ATTACH_PHOTO = utils.wait_xpath(self.driver, self.X_ATTACH_PHOTO)
        self.EL_ATTACH_PHOTO_FROM_PC = utils.wait_xpath(self.driver, self.X_ATTACH_PHOTO_FROM_PC)

    def attachPhoto(self):
        APD = AttachPhotoDialog(self.driver)
        APD.selectFirstPhoto()

    def attachVideo(self):
        AVD = AttachVideoDialog(self.driver)
        AVD.selectFirstVideo()

    def setCommentText(self, text):
        self.EL_INPUT_FIELD.sendKeys(text)

    def submit(self):
        self.EL_ADD_COMMENT_BUTTON.click()
