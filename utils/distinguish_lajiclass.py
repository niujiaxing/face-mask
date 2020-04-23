
import requests
import base64
import json
'''
easydl图像分类
'''

# client_id 为官网获取的AK， client_secret 为官网获取的SK
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=eflAg7N58a5UGceWaMIcAibV&client_secret=GedGnDklAl2s11qk21a2XR2C0vbkcgLA'
# response = requests.get(host)
# print(response)
# if response:
#     dicts = dict()
#     dicts = response.json()
#     for key,value in dicts.items():
#         print(key,value)
'''
refresh_token 25.aa13bcf313305c7e85d6307355d06718.315360000.1903011136.282335-19574586
expires_in 2592000
session_key 9mzdX7nqlzo6moMEZWqRfvc+OGH1jh9vxc6aNF3zYKhmocmd2CFE9sHTOkGcA89L2NToyJrTf+AS6OkgKzTW95oMwaim6g==
access_token 24.dc92e08e0d628b5f901b83cd19a91acb.2592000.1590243136.282335-19574586
scope ai_custom_laji_class public brain_all_scope easydl_mgr easydl_retail_mgr ai_custom_retail_image_stitch ai_custom_test_oversea easydl_pro_mgr wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test权限 vis-classify_flower lpq_开放 cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify smartapp_opensource_openapi smartapp_opensource_recapi qatest_scope1 fake_face_detect_开放Scope vis-ocr_虚拟人物助理 idl-video_虚拟人物助理
session_secret 5245e4a51b4ec9623c2cf7dfebb724b2
'''

def get_laji(filename):

    '''

    :param filename: input the filename you want to distinguish
    :return: lajiname+predict_number
    '''
    AccessToken = '24.dc92e08e0d628b5f901b83cd19a91acb.2592000.1590243136.282335-19574586'#这里填写自己的access_token
    url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/classification/laji_class' + '?access_token='+ AccessToken
    # 请求头
    headers = {'Content-Type' : 'application/json'}

    #打开图片文件
    print(filename)
    str_res = ""
    with open(filename , 'rb') as file:
        pic = base64.b64encode(file.read()).decode()
        print(pic)
    data = {'image':pic,"top_num": 5}
    request = requests.post(url,headers= headers, data=json.dumps(data))
    print(request)
    dict_res = json.loads(request.content)
    print(dict_res)
    for key,result in dict_res.items():
        if key != "log_id":
            res = result[0]
            for value in res.values():
                str_res = str_res + str(value) +" "

            print(str_res)
    return str_res

if __name__ == '__main__':
    img = 'D:\python_work\project\\newpro\Face_Mask2.0\img\\apple.jpg'
    result = get_laji(img)

    ###终端返回
    #chuyulaji 0.9976663589477539
