import requests
import base64


def get_code(img):
    with open(img, 'rb') as f:  # 转为二进制格式
        base64_data = base64.b64encode(f.read())  # 使用base64进行加密
        base64_data = str(base64_data, encoding='utf-8')  # 二进制转为str
    body = {'image': 'data:image/png;base64,' + base64_data,
            'image_url': '',
            'type': 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic',
            'detect_direction': 'false'}
    s = requests.post('https://ai.baidu.com/aidemo', data=body)
    result = s.json()['data']['words_result'][0]['words']
    # return s.json()['data']['words_result'][0]['words']
    if len(result) == 4:
        return result
    elif len(result) > 4:
        return result.replace(' ', '')

    """
    from PublicMethods.GetVerificationCode import get_code

    print(get_code('/home/bugpz/图片/yzm/cYMi.png'))
    """