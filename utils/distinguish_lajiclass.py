
import requests
import base64
import json
'''
easydl图像分类
'''

# client_id 为官网获取的AK， client_secret 为官网获取的SK
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=q6F6BlnKTisGCFcrvaGS9Kkt&client_secret=r6oDz0Ojdae7MK9jre4qCQ8vQ1djae8r'
# response = requests.get(host)
# print(response)
# if response:
#     dicts = dict()
#     dicts = response.json()
#     for key,value in dicts.items():
#         print(key,value)
'''
refresh_token 25.015e886ec109686864e2f739e38b6dc2.315360000.1902890115.282335-19547903
expires_in 2592000
session_key 9mzdWrlwVfoGAyCpcCaKpYXWswOc0gYTAn+2Y0ukXiyinX1pGSIUIzXG05+zhbmYUalqFG6YbZyaCDAsVunF14G5Xtx46A==
access_token 24.aeebbb75095c7af0b14b49ff10a267c7.2592000.1590122115.282335-19547903
scope public vis-classify_dishes vis-classify_car brain_all_scope vis-classify_animal vis-classify_plant brain_object_detect brain_realtime_logo brain_dish_detect brain_car_detect brain_animal_classify brain_plant_classify brain_ingredient brain_advanced_general_classify brain_custom_dish brain_poi_recognize brain_vehicle_detect brain_redwine brain_currency brain_vehicle_damage wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test权限 vis-classify_flower lpq_开放 cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify smartapp_opensource_openapi smartapp_opensource_recapi qatest_scope1 fake_face_detect_开放Scope vis-ocr_虚拟人物助理 idl-video_虚拟人物助理
session_secret cfde9f1e7d6e9717db31e1d7b776f26c
'''

def get_laji(filename):

    '''

    :param filename: input the filename you want to distinguish
    :return: lajiname+predict_number
    '''
    AccessToken = '24.aeebbb75095c7af0b14b49ff10a267c7.2592000.1590122115.282335-19547903'#这里填写自己的access_token
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
    #goldfish 0.6889322996139526
