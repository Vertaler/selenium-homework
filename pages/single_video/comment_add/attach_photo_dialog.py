from pages.base import Component
import utils


class AttcahVideoDialog(Component):

    # without smiles yet
    X_FIRST_VIDEO = "//*[@id='av-page-myVideo-1']"

    def __init__(self, driver):
        super(AttcahVideoDialog, self).__init__(driver)
        self.updateElementsBindings()

    def updateElementsBindings(self):
        self.EL_FIRST_VIDEO = utils.wait_xpath(self.driver, self.X_FIRST_VIDEO)

    def selectFirstVideo(self):
        self.EL_FIRST_VIDEO.click()
