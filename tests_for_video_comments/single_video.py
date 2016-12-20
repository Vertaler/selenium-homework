import seismograph
from base_case import BaseCase
from pages.single_video_page.single_video_page import SingleVideoPage

suite = seismograph.Suite(__name__, require=['selenium'])


@suite.register
class Test1Case(BaseCase):

    def setup(self):
        super(Test1Case, self).setup()
        self.video_page = SingleVideoPage(self.browser)
        self.video_page.open(id=206458458600)

    def test1(self):
        #self.video_page.description_item.do_expand()
        #self.video_page.description_item.check_expanded()
        #cmnts = self.video_page.info_item.el_comments_link.get_comments_count()
        #self.video_page.info_item.el_klasses_btn.switch_klass()
        #kls = self.video_page.info_item.el_klasses_btn.get_klasses_count()
        for i in range(0, 1):
            self.video_page.send_comment(
                with_video=False,
                with_photo=False,
                with_pc_photo=True,
                photo_path="/root/testsTP/seleniumMy/selenium-homework/unnamed.png",
                text="comment_with_photo{}".format(i)
            )
        pass