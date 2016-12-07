from pages.base import Component
import utils


class AttachPhotoDialog(Component):

    # without smiles yet
    X_FIRST_ALBUM = "//ul[contains(@class, 'photo-sc_grid')]/li[1]//a[1]"
    X_FIRST_PHOTO = "//ul[contains(@class, 'photo-sc_grid')]/li[1]//img[1]"
    X_ADD_BUTTON = "//input[contains(@id,'hook_FormButton_button_attach')]"

    def __init__(self, driver):
        super(AttachPhotoDialog, self).__init__(driver)
        self.updateElementsAlbumBindings()

    def updateElementsAlbumBindings(self):
        self.EL_FIRST_ALBUM = utils.wait_xpath(self.driver, self.X_FIRST_ALBUM)
        self.EL_ADD_BUTTON = utils.wait_xpath(self.driver, self.X_ADD_BUTTON)

    def updateElementsChoosePhotoBindings(self):
        self.EL_FIRST_PHOTO = utils.wait_xpath(self.driver, self.X_FIRST_PHOTO)
        self.EL_ADD_BUTTON = utils.wait_xpath(self.driver, self.X_ADD_BUTTON)

    def selectFirstPhoto(self):
        self.EL_FIRST_ALBUM.click()
        self.updateElementsChoosePhotoBindings()
        self.EL_FIRST_PHOTO.click()
        self.EL_ADD_BUTTON.click()
