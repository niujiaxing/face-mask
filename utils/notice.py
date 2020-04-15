import pyttsx3


# 模块初始化
def notice():
    '''
    @author:niu
    @语音提示戴口罩
    :return:
    '''
    engine = pyttsx3.init()

    print('准备开始语音播报...')

    # 设置要播报的Unicode字符串
    engine.say("请佩戴口罩")

    # 等待语音播报完毕
    engine.runAndWait()

if __name__ == '__main__':
    notice()