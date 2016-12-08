from pages.base import Component
import utils
from pages.single_video.comment_add.video_comment_form import VideoCommentForm


class CommentList(Component):

    X_COMMENTS = "((//*[@class='comments_lst'])[8])//*[@class='comments_current show-on-hover']"

    def __init__(self, driver):
        super(CommentList, self).__init__(driver)
        self.updateElementsBindings()

    def updateElementsBindings(self):
        try:
            self.EL_COMMENTS = utils.wait_many_xpath(self.driver, self.X_COMMENTS)
        except:
            return []

    def getComments(self):
        result = []
        for el_cmnt in self.EL_COMMENTS:
            cmnt = Comment(self.driver, el_cmnt)
            result.append(cmnt)
        return result

    def getLastComment(self):
        el_last = self.EL_COMMENTS[-1]
        cmnt = Comment(self.driver, el_last)
        return cmnt


class Comment(Component):

    X_REMOVE = ".//*[contains(@class, 'comments_remove')]"
    X_EDIT = ".//*[contains(@class, 'comments_edit')]"
    X_AUTHOR = ".//*[contains(@class, 'comments_author')]/a"
    X_TEXT = ".//*[contains(@class, 'comments_text')]"
    X_CLASS = ".//*[@class = 'klass_w']//span[contains(@class, 'tico')]"
    X_REPLY = ".//*[@class = 'reply_w']//span[contains(@class, 'tico')]"
    X_DELETE_STUB = ".//*[contains(@class, 'delete-stub_info')]"
    X_RESTORE = ".//*[contains(@class, 'delete-stub_ac')]/a"

    def __init__(self, driver, el_cmnt):
        super(Comment, self).__init__(driver)
        self.EL_CMNT = el_cmnt
        self.updateElementsBindings()

    def updateElementsBindings(self):
        self.EL_REMOVE = self.safeBindElem(self.X_REMOVE)
        self.EL_EDIT = self.safeBindElem(self.X_EDIT)
        self.EL_AUTHOR = self.safeBindElem(self.X_AUTHOR)
        self.EL_TEXT = self.safeBindElem(self.X_TEXT)
        self.EL_CLASS = self.safeBindElem(self.X_CLASS)
        self.EL_REPLY = self.safeBindElem(self.X_REPLY)
        self.EL_DELETE_STUB = self.safeBindElem(self.X_DELETE_STUB)
        self.EL_RESTORE = self.safeBindElem(self.X_RESTORE)

    def safeBindElem(self, x_path):
        try:
            return self.EL_CMNT.find_element_by_xpath(x_path)
        except:
            return None

    def editComment(self, text):
        if self.EL_EDIT is None:
            return
        utils.click_directly(self.driver, self.EL_EDIT)
        VCF = VideoCommentForm(self.driver)
        VCF.setCommentText(text)
        VCF.submit()

    def replyComment(self, text):
        if self.EL_REPLY is None:
            return
        utils.click_directly(self.driver, self.EL_REPLY)
        VCF = VideoCommentForm(self.driver)
        VCF.setCommentText(text)
        VCF.submit()

    def removeComment(self):
        if self.EL_REMOVE is None:
            return
        utils.click_directly(self.driver, self.EL_REMOVE)

    def checkIfRemovedComment(self):
        self.updateElementsBindings()
        if self.EL_DELETE_STUB is None:
            return False
        else:
            return True

    def restoreComment(self):
        if self.EL_RESTORE is None:
            return
        utils.click_directly(self.driver, self.EL_RESTORE)

    def checkIfRestoredComment(self):
        return (not self.checkIfRemovedComment())

    def voteComment(self):
        if self.EL_CLASS is None:
            return
        utils.click_directly(self.driver, self.EL_CLASS)

    def getText(self):
        if self.EL_REMOVE is None:
            return None
        return self.EL_TEXT.text
