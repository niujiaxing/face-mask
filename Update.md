# 文件更新

## [Readme]
### 项目介绍

- 利用TensorFlow的相应模型


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

在os.systerm（）中输入

```python
python tensorflow_infer.py  --img-path /path/to/your/img
```


如果您要在视频上跑，只需要：

```python
python tensorflow_infer.py --img-mode 0 --video-path /path/to/video  
```



如果要打开本地摄像头, video_path填写0就可以了，如下

```python
python tensorflow_infer.py --img-mode 0 --video-path 0
```



---
##存在问题汇总以及需求

### 需求

- 搭建网站，在网站中使用模型
- 调用api增加一些有意思的ai小工具，比如图像检测，或者语音对话之类的
- 制作视频展示和ppt

### 目前存在问题

- [ ] 存在多个模型，搞清楚那些文件是必须的，清理多余文件
- [ ] 解决播放视频没有声音的bug
- [x] 检测到未戴口罩，增加语音提示（视频）
- [ ] 增加人群密集度检测，大于一个阈值则提醒（3人）
- [ ] 模型精度偏低，需要训练（额外）





