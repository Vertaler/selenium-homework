from pages.base import Component
import utils


class AttachPhotoDialog(Component):

    # without smiles yet
    X_FIRST_ALBUM = "//ul[contains(@class, 'photo-sc_grid')]/li[1]//a[1]"
    X_FIRST_PHOTO = "//ul[contains(@class, 'photo-sc_grid')]/li[1]//img[1]"
    X_ADD_BUTTON = "//input[@name='button_attach']"

    def __init__(self, driver):
        super(AttachPhotoDialog, self).__init__(driver)
        self.updateElementsBindings()

    def updateElementsBindings(self):
        self.EL_FIRST_ALBUM = utils.wait_xpath(self.driver, self.X_FIRST_ALBUM)
        self.EL_FIRST_PHOTO = utils.wait_xpath(self.driver, self.X_FIRST_PHOTO)
        self.EL_ADD_BUTTON = utils.wait_xpath(self.driver, self.X_ADD_BUTTON)

    def selectFirstPhoto(self):
        self.EL_FIRST_ALBUM.click()
        self.updateElementsBindings()
        self.EL_FIRST_PHOTO.click()
        self.EL_ADD_BUTTON.click()
