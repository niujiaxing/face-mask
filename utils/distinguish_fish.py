
import requests
import base64
import json
'''
easydl图像分类
'''

# client_id 为官网获取的AK， client_secret 为官网获取的SK
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=nXScD8LH6EIZfsRsSb28jk8e&client_secret=Zppi5rYVNFs8GypMUzNZiBksWwPounoX'
# response = requests.get(host)
# print(response)
# if response:
#     dicts = dict()
#     dicts = response.json()
#     for key,value in dicts.items():
#         print(key,value)
'''
refresh_token 25.ea3122e787b392905571365a298255cf.315360000.1902801465.282335-19409691
expires_in 2592000
session_key 9mzdDAYpOgOWk/LrTU0xEG0d10dRcxRRzY76S8dbQExoEgYFSr82LTsgXROOP61NE0ahTJYlYbWtwsvFiDx7dIXsV7//Gw==
access_token 24.7370302fe5870a0a2b252979f4fd358a.2592000.1590033465.282335-19409691
scope ai_custom_facemask_det ai_custom_detection_fish public brain_all_scope easydl_mgr easydl_retail_mgr ai_custom_retail_image_stitch ai_custom_test_oversea easydl_pro_mgr wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test权限 vis-classify_flower lpq_开放 cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify smartapp_opensource_openapi smartapp_opensource_recapi qatest_scope1 fake_face_detect_开放Scope vis-ocr_虚拟人物助理 idl-video_虚拟人物助理
session_secret e357751e289acb9de83e1e54abb09d8e
'''

def get_fish(filename):

    '''

    :param filename: input the filename you want to distinguish
    :return: fishname+predict_number
    '''
    AccessToken = '24.7370302fe5870a0a2b252979f4fd358a.2592000.1590033465.282335-19409691'#这里填写自己的access_token
    # filename = 'D:\python_work\project\\newpro\Face_Mask2.0\img\shark.jpg'#填写图片路径
    url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/classification/detection_fish' + '?access_token='+ AccessToken
    # 请求头
    headers = {'Content-Type' : 'application/json'}

    #打开图片文件
    str_res = ""
    with open(filename , 'rb') as file:
        pic = base64.b64encode(file.read()).decode()
    data = {'image':pic,"top_num": 5}
    request = requests.post(url,headers= headers, data=json.dumps(data))
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
    img = 'D:\python_work\project\\newpro\Face_Mask2.0\img\goldfish.jpg'
    result = get_fish(img)

    ###终端返回
    #goldfish 0.6889322996139526
