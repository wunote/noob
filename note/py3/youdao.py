import urllib.request
import urllib.parse
import json

while True: 
    content = input('Enter the words needs translated:')
    if not len(content):
        break

    head="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom="

    #创建Form_Data字典，存储上图的Form Data
    Data = {}
    Data['from'] = 'AUTO'
    Data['to'] = 'AUTO'
    Data['i'] = content
    Data['doctype'] = 'json'
    Data['version'] = '2.1'
    Data['keyfrom'] = 'fanyi.web'
    Data['smartresult'] = 'dict'
    Data['client'] = 'fanyideskweb'
    Data["salt"]="502865709143"
    Data["sign"]="e7b725d55dd02ab7b3a17c44170950ad"
    Data['action'] = 'FY_BY_CLICKBUTTON'
    Data['typoResult'] = 'true'
    #使用urlencode方法转换标准格式
    data = urllib.parse.urlencode(Data).encode('utf-8')
    
    req = urllib.request.Request(url,data)
    req.add_header("User-Agent",head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    #使用JSON
    translate_results = json.loads(html)
    #找到翻译结果
    translate_results = translate_results['translateResult'][0][0]['tgt']
    print(translate_results)

