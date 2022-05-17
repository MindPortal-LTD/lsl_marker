"""visualising trials"""

import sys
import cv2
import time
import numpy as np

class TrialVisual(object):
    # Default setting
    color = dict(G=(20, 140, 0), B=(210, 0, 0), R=(0, 50, 200),
        Y=(0, 215, 235), K=(0, 0, 0), W=(255, 255, 255), w=(200, 200, 200))

    def __init__(self, screen_pos=None, screen_size=None):
        """
        Input:
            pc_feedback: show feedback on the pc screen?
            screen_pos: screen position in (x,y)
            screen_size: screen size in (x,y)
        """
        # screen size and message setting
        if screen_size is None:
            screen_width = 1024
            screen_height = 768
        else:
            screen_width, screen_height = screen_size

        if screen_pos is None:
            screen_x, screen_y = (0, 0)
        else:
            screen_x, screen_y = screen_pos

        cv2.namedWindow("img", cv2.WINDOW_AUTOSIZE)
        cv2.moveWindow("img", screen_x, screen_y)
        cv2.setWindowProperty("img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        self.img = 200 * np.ones((screen_height, screen_width, 3), np.uint8)
        self.set_cue_color(boxcol='B', crosscol='W', bgcol='w')
        self.width = self.img.shape[1]
        self.height = self.img.shape[0]
        self.cx = int(self.width / 2)
        self.cy = int(self.height / 2)
        self.cue_size = 20
        self.cross_size = 20
        self.cross_width = 3

    def finish(self):
        cv2.destroyAllWindows()

    def set_cue_color(self, boxcol='B', crosscol='W', bgcol='w'):
        self.boxcol = self.color[boxcol]
        self.crosscol = self.color[crosscol]
        self.bgcol = self.color[bgcol]

    def draw_cue(self):
        # gray background
        cv2.rectangle(self.img, (0, 0), (self.width, self.height), self.bgcol, -1)
        # square indicating trial ongoing
        cv2.rectangle(self.img, (self.cx-self.cue_size, self.cy-self.cue_size), 
            (self.cx+self.cue_size, self.cy+self.cue_size), self.boxcol, -1)

    def draw_iti(self):
        # gray background
        cv2.rectangle(self.img, (0, 0), (self.width, self.height), self.bgcol, -1)
        # equal indicating trial rest
        cv2.rectangle(self.img, (self.cx-self.cross_size, self.cy-self.cross_width), 
            (self.cx+self.cross_size, self.cy+self.cross_width), self.crosscol, -1)
        cv2.rectangle(self.img, (self.cx-self.cross_size, self.cy+self.cross_size-self.cross_width), 
            (self.cx+self.cross_size, self.cy+self.cross_size+self.cross_width), self.crosscol, -1)

    def update(self):
        cv2.imshow("img", self.img)
        cv2.waitKey(1)


