#test more_thread
import threading
from utils import notice
global score
import cv2
import time
import argparse

import numpy as np
from PIL import Image
from keras.models import model_from_json
from utils.anchor_generator import generate_anchors
from utils.anchor_decode import decode_bbox
from utils.nms import single_class_non_max_suppression
from load_model.tensorflow_loader import load_tf_model, tf_inference
from utils.notice import notice
sess, graph = load_tf_model('models/face_mask_detection.pb')
# anchor configuration
feature_map_sizes = [[33, 33], [17, 17], [9, 9], [5, 5], [3, 3]]
anchor_sizes = [[0.04, 0.056], [0.08, 0.11], [0.16, 0.22], [0.32, 0.45], [0.64, 0.72]]
anchor_ratios = [[1, 0.62, 0.42]] * 5
threadLock = threading.Lock()
threads = []

# generate anchors
anchors = generate_anchors(feature_map_sizes, anchor_sizes, anchor_ratios)

# for inference , the batch size is 1, the model output shape is [1, N, 4],
# so we expand dim for anchors to [1, anchor_num, 4]
anchors_exp = np.expand_dims(anchors, axis=0)
id2class = {0: 'Mask', 1: 'NoMask'}

def inference(image,
              conf_thresh=0.5,
              iou_thresh=0.4,
              target_shape=(160, 160),
              draw_result=True,
              show_result=True
              ):
    '''
    Main function of detection inference
    :param image: 3D numpy array of image
    :param conf_thresh: the min threshold of classification probabity.
    :param iou_thresh: the IOU threshold of NMS
    :param target_shape: the model input size.
    :param draw_result: whether to daw bounding box to the image.
    :param show_result: whether to display the image.
    :return:
    '''
    # image = np.copy(image)
    output_info = []
    height, width, _ = image.shape
    image_resized = cv2.resize(image, target_shape)
    image_np = image_resized / 255.0  # 归一化到0~1
    image_exp = np.expand_dims(image_np, axis=0)
    y_bboxes_output, y_cls_output = tf_inference(sess, graph, image_exp)

    # remove the batch dimension, for batch is always 1 for inference.
    y_bboxes = decode_bbox(anchors_exp, y_bboxes_output)[0]
    y_cls = y_cls_output[0]
    # To speed up, do single class NMS, not multiple classes NMS.
    bbox_max_scores = np.max(y_cls, axis=1)
    bbox_max_score_classes = np.argmax(y_cls, axis=1)

    # keep_idx is the alive bounding box after nms.
    #this has a bbbbbbbbbbbbbuuuuuuuuuuuugggggggggggggggg
    keep_idxs = single_class_non_max_suppression(y_bboxes,
                                                 bbox_max_scores,
                                                 conf_thresh=conf_thresh,
                                                 iou_thresh=iou_thresh,
                                                 )
    # times = 0
    for idx in keep_idxs:
        # times += 1
        conf = float(bbox_max_scores[idx])

        class_id = bbox_max_score_classes[idx]
        #在class_id中标注识别结果，若为1则表示未佩戴口罩
        bbox = y_bboxes[idx]
        # clip the coordinate, avoid the value exceed the image boundary.
        xmin = max(0, int(bbox[0] * width))
        ymin = max(0, int(bbox[1] * height))
        xmax = min(int(bbox[2] * width), width)
        ymax = min(int(bbox[3] * height), height)

        if draw_result:
            if class_id == 0:
                color = (0, 255, 0)
            else:
                color = (255, 0, 0)


            cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color, 2)
            cv2.putText(image, "%s: %.2f" % (id2class[class_id], conf), (xmin + 2, ymin - 2),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color)
        output_info.append([class_id, conf, xmin, ymin, xmax, ymax])

    if show_result:
        Image.fromarray(image).show()
    return output_info
    # return class_id


def run_on_video(video_path, output_video_name, conf_thresh):
    cap = cv2.VideoCapture(video_path)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # writer = cv2.VideoWriter(output_video_name, fourcc, int(fps), (int(width), int(height)))
    total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    if not cap.isOpened():
        raise ValueError("Video open failed.")
        return
    status = True
    idx = 0
    while status:
        start_stamp = time.time()
        status, img_raw = cap.read()
        img_raw = cv2.cvtColor(img_raw, cv2.COLOR_BGR2RGB)
        read_frame_stamp = time.time()
        if (status):
            answer = inference(img_raw,
                      conf_thresh,
                      iou_thresh=0.5,
                      target_shape=(260, 260),
                      draw_result=True,
                      show_result=False)
            # define the content add in the picture
            text = ''
            color = (255, 0, 0)
            if answer != []:
                ans = answer[0]
                # get the number of people in the picture
                peopleNumber = len(answer)
                if peopleNumber >= 3:
                    # red color alert people number
                    color = (255, 0, 0)
                else:
                    # safe color show people number
                    color = (0, 255, 0)
                text = '' + str(peopleNumber)
            # modify the show_pic
            img_raw_text = cv2.putText(img_raw, text, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2.0, color, 3)
            cv2.imshow('image', img_raw_text[:, :, ::-1])
            cv2.waitKey(1)
            inference_stamp = time.time()
            # writer.write(img_raw)
            write_frame_stamp = time.time()
            idx += 1
            if idx % 40 == 0 :
                if ans[0] != 0:
                    print(ans,idx,"开始语音播报",peopleNumber)
                    t = MyThread(1, "thread:1", 1)
                    t.start()
            #检测到键盘输入q则退出
            if cv2.waitKey(100) & 0xff == ord('q'):
                break
    # writer.release()
    cap.release()
    cv2.destroyAllWindows()

class MyThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        # print(f"开启线程{self.name}")
        threadLock.acquire()
        print("正在加载语音")
        notice('1')
        print("语音加载完成")
        threadLock.release()



def main(img_mode,img_path,video_path):

    # parser = argparse.ArgumentParser(description="Face Mask Detection")
    # img-mode, type=int,set 1 to run on image, 0 to run on video.
    # img-path', type=str, help='path to your image
    # video-path', type=str|int, path to your video, `0` means to use camera.


    if img_mode:
        if not img_path:
            print("请输入图片的url:")
            img_path = input()

        def exp_imgcvt(img):
            "' :exception'"
            try:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                return img
            except Exception:
                print("请输入正确的图片path")
                imgPath = input()
                img = cv2.imread(imgPath)
                exp_imgcvt(img)
        imgPath = img_path
        img = cv2.imread(imgPath)
        # exception
        img = exp_imgcvt(img)
        inference(img, show_result=True, target_shape=(260, 260))
    else:
        def exp_viocvt(video_path):
            "' :exception'"
            try:
                run_on_video(video_path, '', conf_thresh=0.5)
            except Exception:
                print("请输入正确的视频path")
                video_path = input()
                exp_viocvt(video_path)
        exp_viocvt(video_path)




####################
##############
if __name__ == '__main__':
    # img-mode, type=int,set 1 to run on image, 0 to run on video.
    # img-path', type=str, help='path to your image
    # video-path', type=str|int, path to your video, `0` means to use camera.
    main(1,'img/demo2.jpg',0)
    # main(img_mode=0, img_path=None,video_path=0)
    # main(img_mode=0, img_path=None, video_path='img/video.mp4')
