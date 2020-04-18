import pyttsx3

def notice(is_unwear):
    '''
    @author:niu
    @语音提示戴口罩
    由于需要等待语音提示完成，采用多线程
    :return:
    '''
    if is_unwear != '0':
        engine = pyttsx3.init()
        # 设置要播报的Unicode字符串
        engine.say("请佩戴口罩")

        # 等待语音播报完毕
        engine.runAndWait()


if __name__ == '__main__':
    notice(str(1))