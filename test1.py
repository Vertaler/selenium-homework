#!/usr/bin/env python

import unittest
from base_case import BaseCase
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pages.single_video.single_video_page import SingleVideoPage


class Test1(BaseCase):

    def testTitle(self):
        self.SVP = SingleVideoPage(self.driver, 'video/205055857128')
        self.SVP.open()
        self.SVP.bind()
        tmp = self.SVP.VIDEO_META.EL_DATE.text
        self.SVP.VIDEO_COMMENT_FORM.attachPhoto()
        self.SVP.VIDEO_COMMENT_FORM.attachVideo()
        self.SVP.VIDEO_COMMENT_FORM.setCommentText("75942375924375")
        self.SVP.VIDEO_COMMENT_FORM.submit()
        tmp += "123"


if __name__ == '__main__':
    #pprint(vars(DesiredCapabilities))
    unittest.main(verbosity=2)