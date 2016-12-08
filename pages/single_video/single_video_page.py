from pages.base import Page, Component
from video_meta import VideoMeta
from .comment_add.video_comment_form import VideoCommentForm
from .comment_dialog.video_comment_dailog import VideoCommentDialog
from .video_comments import CommentList, Comment
import utils


class SingleVideoPage(Page):

    def __init__(self, driver, path):
        super(SingleVideoPage, self).__init__(driver)
        self.PATH = path
        self.VIDEO_META = VideoMeta(self.driver)
        self.VIDEO_COMMENT_FORM = VideoCommentForm(self.driver)
        self.VIDEO_COMMENTS = CommentList(self.driver)

    def updateElementsBindings(self):
        self.VIDEO_META.updateElementsBindings()
        self.VIDEO_COMMENT_FORM.updateElementsBindings()
        self.VIDEO_COMMENTS.updateElementsBindings()

    def openCommentDialog(self):
        utils.click_directly(self.driver, self.VIDEO_META.EL_COMMENT_DIALOG_OPEN)
        VCD = VideoCommentDialog(self.driver)
        return VCD
