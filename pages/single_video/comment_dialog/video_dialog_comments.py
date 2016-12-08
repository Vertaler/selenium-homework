from pages.base import Component
import utils


class CommentListDialog(Component):

    X_COMMENTS = "//*[@class='disc-comments-w']/*[contains(@id,'d-id-cmnt-')]"

    def __init__(self, driver):
        super(CommentListDialog, self).__init__(driver)
        self.updateElementsBindings()

    def updateElementsBindings(self):
        try:
            self.EL_COMMENTS = utils.wait_many_xpath(self.driver, self.X_COMMENTS)
        except:
            return []

    def getComments(self):
        result = []
        for el_cmnt in self.EL_COMMENTS:
            cmnt = CommentDialog(self.driver, el_cmnt)
            result.append(cmnt)
        return result

    def getLastComment(self):
        el_last = self.EL_COMMENTS[-1]
        cmnt = CommentDialog(self.driver, el_last)
        return cmnt


class CommentDialog(Component):

    X_AUTHOR = ".//span[contains(@class, 'd_comment_owner')]"
    X_TEXT = ".//div[contains(@class, 'd_comment_text textWrap')]"

    def __init__(self, driver, el_cmnt):
        super(CommentDialog, self).__init__(driver)
        self.EL_CMNT = el_cmnt
        self.updateElementsBindings()

    def updateElementsBindings(self):
        self.EL_AUTHOR = self.safeBindElem(self.X_AUTHOR)
        self.EL_TEXT = self.safeBindElem(self.X_TEXT)

    def safeBindElem(self, x_path):
        try:
            return self.EL_CMNT.find_element_by_xpath(x_path)
        except:
            return None
