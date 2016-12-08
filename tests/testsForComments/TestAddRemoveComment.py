#!/usr/bin/env python

import unittest
from base_case import BaseCase
from pages.single_video.single_video_page import SingleVideoPage


class TestAddRemoveComment(BaseCase):

    VIDEO_PATH = "video/205055857128"
    COMMENT_TEXT = "lalala123"

    def testAddRemove(self):
        self.SVP = SingleVideoPage(self.driver, self.VIDEO_PATH)
        self.SVP.open()
        self.SVP.updateElementsBindings()
        self.SVP.VIDEO_COMMENT_FORM.setCommentText(self.COMMENT_TEXT)
        self.SVP.VIDEO_COMMENT_FORM.submit()
        lastCmnt = self.SVP.VIDEO_COMMENTS.getLastComment()
        lastCmntText = lastCmnt.getText()
        self.assertTrue(lastCmntText.contains(self.COMMENT_TEXT))
        lastCmnt.removeComment()
        self.assertTrue(lastCmnt.checkIfRemovedComment())


if __name__ == '__main__':
    unittest.main(verbosity=2)