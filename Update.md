# 文件更新

## [updates]
### 第一次更改内容
---
njx
---

 - 将tenforflow该为tensorflow
- 增加了图片path为空的异常处理
- 增加了找不到图片的异常处理

---
为了统一，配置TensorFlow环境即可
---
打开main_tensorflow.py

如果您要运行图片：

在os.systerm（）中输入
python tensorflow_infer.py  --img-path /path/to/your/img
如果您要在视频上跑，只需要：

python tensorflow.py --img-mode 0 --video-path /path/to/video  
### 如果要打开本地摄像头, video_path填写0就可以了，如下
python tensorflow.py --img-mode 0 --video-path 0
---

---
##存在问题汇总以及需求
- [ ] 存在多个模型，搞清楚那些文件是必须的，清理多余文件
- [ ] 播放视频没有声音
- [ ] 检测到未戴口罩，增加语音提示（视频）
- [ ] 增加人群密集度检测，大于一个阈值则提醒（3人）
- [ ] 模型精度偏低，需要训练（额外）





