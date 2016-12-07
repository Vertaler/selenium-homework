from pages.base import Page, Component
from video_meta import VideoMeta
from .comment_add.video_comment_form import VideoCommentForm
import utils


class SingleVideoPage(Page):

    def __init__(self, driver, path):
        super(SingleVideoPage, self).__init__(driver)
        self.PATH = path

    def bind(self):
        self.VIDEO_META = VideoMeta(self.driver)
        self.VIDEO_COMMENT_FORM = VideoCommentForm(self.driver)



class VideoComment(Component):

    def __init__(self, driver):
        super(VideoComment, self).__init__(driver)
        self.selector = None


if __name__ == '__main__':
    pass