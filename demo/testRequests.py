import requests

def login():
    session = requests.session()

    url = 'https://authapi.xincheng.com:8090/mobilelogin/index'

    params = {
        'userid': 'lvrihui',
        'password':
        'Taco53TfQ2iDfvIUrKHroIRFNBt2/SP5TYYxCzgJ4wE+dElEIvQzGn4nVO9hQOl2qGDhC5T6D3/jEZvyJ/wQKq6uBnbTECGoB\
            mvTpwAWGHmLe1HMvlyQmEK2WlgJBSCrKlZyJXZAhlDcxnOvcZmqdQsToiVdzRCRaNUwFEg4/zK1ljgxHPDFq3eIOOmbU+KrpPQURrYrqtRc\
            ddpTGCh50EfuWDREDHP9dC0j2J8VcOHRYnP04ysNuK5WpIfWAhhqXWGc0gJJBhSQCpo7ZFB3/Z7NS90/PXfpCYbj6Qd8Vaf0zju2U5Riuj1A2nwEJDWLrSTvHMHHf4arkOWBSKnxSw==',
        'systemCode': 'A09'
    }
    try:
        r = session.post(url=url, data=params)
        return requests.utils.dict_from_cookiejar(r.cookies)
        
    except expression as err:
        print('获取cookie失败：\n{0}'.format(err))


def get_data():
    cookie = login()
    print(cookie)
    res = requests.get(
            url="http://crm.xincheng.com/Kfxt/rcfw/RcRwcl_Edit.aspx",
            params={
                'mode':
                '2',
                'oid':
                'd93aef5b-08fe-ea11-80c3-90e2babd62d1&funcid=01020302&ReceiveGUID=504788b7-07fe-ea11-80c3-90e2babd62d1'
            },
            cookies= cookie)
    print(res.text)

get_data()


'''
    if r.status_code == 200:
        r = session.get(
            url="http://crm.xincheng.com/Kfxt/rcfw/RcRwcl_Edit.aspx",
            params={
                'mode':
                '2',
                'oid':
                'd93aef5b-08fe-ea11-80c3-90e2babd62d1&funcid=01020302&ReceiveGUID=504788b7-07fe-ea11-80c3-90e2babd62d1'
            },
            cookies= session.cookies)
        print(r.status_code)
        print(r.text)
'''