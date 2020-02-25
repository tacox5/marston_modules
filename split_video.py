from moviepy.video.fx.all import crop
from moviepy.editor import *
import sys
import os

def split_video(video):
    """Splits a clip into quadrants
    """
    clip = VideoFileClip(video).subclip(0, 10)
    x_size, y_size = clip.size
    cropped_tl = clip.crop(x1 = 0, y1 = 0, x2 = int(x_size / 2.0), y2 = int(y_size / 2.0))
    cropped_tr = clip.crop(x1 = int(x_size / 2.0), y1 = 0, x2 = x_size, y2 = int(y_size / 2.0))
    cropped_bl = clip.crop(x1 = 0, y1 = int(y_size / 2.0), x2 = int(x_size / 2.0), y2 = y_size)
    cropped_br = clip.crop(x1 = int(x_size / 2.0), y1 = int(y_size / 2.0), x2 = x_size, y2 = y_size)
    clips = [cropped_tl, cropped_tr, cropped_bl, cropped_br]
    names = ['_tl.mp4', '_tr.mp4', '_bl.mp4', '_br.mp4']
    path = os.path.dirname(video)
    video_name = os.path.basename(video)
    for i, c in enumerate(clips):
        c.write_videofile(os.path.join(path, video_name + names[i]), codec = 'mpeg4')

if __name__ == '__main__':
    videos = sys.argv[1:]

    for video in videos:
        if os.path.isfile(video):
            split_video(video)
