# 项目介绍
## [Readme]
### 项目介绍

- 我们使用TensorFlow运行我们的检测模型。
- 对图片，视频和摄像头中出现的人脸进行识别并检测是否佩戴口罩。
- 如果没有佩戴口罩，系统有提示音提示“请佩戴口罩”，直到您佩戴口罩为止。
- 同时视频左上角会显示出当前视频中的人数，超过三人时系统判断有人群聚集风险，人数显示变为红色进行提示。


- 数据集来自于[WIDER Face](http://shuoyang1213.me/WIDERFACE/)和[MAFA](http://www.escience.cn/people/geshiming/mafa.html)数据集, 我们重新修改了标注并进行了校验

### 模型介绍

我们在本项目中使用了SSD类型的架构，为了让模型可以实时的跑在浏览器以及终端设备上，**我们将模型设计的非常小，只有101.5万个参数**。

本模型输入大小为260x260，主干网络只有8个卷积层，加上定位和分类层，一共只有24层（每层的通道数目基本都是32\64\128），所以模型特别小，只有101.5万参数。模型对于普通人脸基本都能检测出来，但是对于小人脸，检测效果肯定不如大模型。

模型在五个卷积层上接出来了定位分类层，其大小和anchor设置信息如下表.

| 卷积层 | 特征图大小 | anchor大小 | anchor宽高比（aspect ratio） |
| ------ | ---------- | ---------- | ---------------------------- |
| 第一层 | 33x33      | 0.04,0.056 | 1,0.62,0.42                  |
| 第二层 | 17x17      | 0.08,0.11  | 1,0.62,0.42                  |
| 第三层 | 9x9        | 0.16,0.22  | 1,0.62,0.42                  |
| 第四层 | 5x5        | 0.32,0.45  | 1,0.62,0.42                  |
| 第五层 | 3x3        | 0.64,0.72  | 1,0.62,0.42                  |

---
### 模型结构图

![](D:\python_work\project\newpro\Face_Mask2.0\img\face_mask_detection.hdf5.png)

---



修改异常
---

 - 将tenforflow该为tensorflow
- 增加了图片path为空的异常处理
- 增加了找不到图片的异常处理
- 增加了佩戴口罩语音播报功能

---
运行方法（配置TensorFlow环境）
---
打开main_tensorflow.py

如果您要运行图片：

```
#     # img-mode, type=int,set 1 to run on image, 0 to run on video.
#     # img-path', type=str, help='path to your image
#     # video-path', type=str|int, path to your video, `0` means to use camera.
```

在main（）中输入

```python
main(img_mode=1, img_path=your_path,video_path=0) your_path中填写你的图片地址
```


如果您要在视频上跑，只需要：

```python
main(img_mode=0, img_path=None, video_path=your_path)  your_path中填写你的视频地址
```



如果要在本地摄像头运行, video_path填写0就可以了，如下

```python
main(img_mode=0, img_path=None,video_path=0)
```
---

**如果你想体验浏览器功能，运行app.py
访问127.0.0.1:5000**


---
##项目功能实现

### 介绍

- 我们使用flask搭建了一个网站，您可以运行app.py体验在网站中对图片进行口罩检测。
- 为了丰富网站内容，我们在网站中调用我们的模型api增加了一些有意思的ai小工具，鱼类识别和垃圾分类，你可以打开我们进行体验。
- 我们也用心制作了精美的ppt和视频对我们的项目进行了一个介绍，如果您对我们的项目还有什么问题可以观看我们的视频和ppt，绝对值得一看！

---
### 小结

- 希望疫情早日消除，守得云开见月明。
- 如果有任何关于项目的问题，欢迎联系我们。
- 谢谢您的观看。





