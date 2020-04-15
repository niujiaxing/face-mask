[![构建状态](/badges/test/build.svg)](/p/test/ci/job)

[TOC]

# 体验示例项目

这个示例代码可以帮你快速了解一个简单的 Python Flask 网页应用。并已经配置好自动打包镜像过程。

文件解释
-----------

样例包括:

* README.md - 本文件
* Jenkinsfile - 用以自动构建和测试的脚本
* Dockerfile - 用以自动构建 Docker 镜像的脚本
* requirements.txt - 依赖包文件
* app.py - 主 Flask 服务器端源代码

快速开始
---------------

如下这些引导，假定你想在自己的电脑上开发本项目。

1. 安装依赖

        $ pip install -r requirements.txt


2. 启动服务器

        $ python app.py

3. 打开 http://0.0.0.0:5000/ .
