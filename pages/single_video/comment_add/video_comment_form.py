from pages.base import Component
import utils
from attach_photo_dialog import AttachPhotoDialog
from attach_video_dialog import AttachVideoDialog
from selenium.webdriver.common.action_chains import ActionChains


class VideoCommentForm(Component):

    # without smiles yet
    X_INPUT_FIELD = "(//body//*[contains(@class,'comments_form')]//*[contains(@class, 'js-comments_add')])[8]"
    X_ADD_COMMENT_BUTTON = "//*[contains(@id,'hook_NewDiscussion')]/div[2]/div[2]/div/div/div/div[3]/div/form/div[3]/button[1]"
    X_ATTACH = "//*[contains(@id,'hook_NewDiscussion')]/div[2]/div[2]/div/div/div/div[3]/div/form/div[1]/div[1]/span[3]"
    X_ATTACH_VIDEO = "(//*[contains(@id,'hook_NewDiscussion')]//*[contains(@class, 'sc-menu ')]//li[1]//span)[2]"
    X_ATTACH_PHOTO = "(//*[contains(@id,'hook_NewDiscussion')]//*[contains(@class, 'sc-menu ')]//li[2]//span)[2]"
    X_ATTACH_PHOTO_FROM_PC = "(//*[contains(@id,'hook_NewDiscussion')]//*[contains(@class, 'sc-menu ')]//li[2]//span)[2]"

    def __init__(self, driver):
        super(VideoCommentForm, self).__init__(driver)
        self.updateElementsBindings()

    def updateElementsBindings(self):
        self.EL_INPUT_FIELD = utils.wait_xpath(self.driver, self.X_INPUT_FIELD)
        self.EL_ADD_COMMENT_BUTTON = utils.wait_xpath(self.driver, self.X_ADD_COMMENT_BUTTON)
        self.EL_ATTACH = utils.wait_xpath(self.driver, self.X_ATTACH)
        self.EL_ATTACH_VIDEO = utils.wait_xpath(self.driver, self.X_ATTACH_VIDEO)
        self.EL_ATTACH_PHOTO = utils.wait_xpath(self.driver, self.X_ATTACH_PHOTO)
        self.EL_ATTACH_PHOTO_FROM_PC = utils.wait_xpath(self.driver, self.X_ATTACH_PHOTO_FROM_PC)

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
