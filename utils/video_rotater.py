import cv2
import os

class VideoRotator:
    def __init__(self, video_path):
        self.video_path = video_path

    def rotate(self, save_path):
        vcap = cv2.VideoCapture(self.video_path)
        width = int(vcap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(vcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        size = (height, width)
        frame_rate = int(vcap.get(cv2.CAP_PROP_FPS))
        out = cv2.VideoWriter(os.path.join(save_path,'rotated.avi'), cv2.VideoWriter_fourcc('I', '4', '2', '0'), frame_rate, size)
        success, img = vcap.read()
        while success:
            rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
            out.write(rotated)
            success, img = vcap.read()
        out.release()

if __name__ == '__main__':
    vr = VideoRotator(video_path='./videos/data-long.mp4')
    vr.rotate(save_path='./videos/')
