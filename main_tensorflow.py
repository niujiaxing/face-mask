import os
from tensorflow_infer_niu import main
if __name__ == "__main__":
    # img-mode, type=int,set 1 to run on image, 0 to run on video.
    # img-path', type=str, help='path to your image
    # video-path', type=str|int, path to your video, `0` means to use camera.
    # main(1, 'img/demo2.jpg', 0)
    main(img_mode=0, img_path=None,video_path=0)
    # main(img_mode=0, img_path=None, video_path='img/video.mp4')

