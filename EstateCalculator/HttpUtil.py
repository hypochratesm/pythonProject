#http 유틸
import json
import urllib.request
import xml.dom.minidom
import requests ,bs4
import pandas as pd
import Const
class httpUtil() :
    pass
    def __init__(self):
        self.result = []
    def run_http(self):

        params = {'serviceKey' : Const.DECODING_KEY, 'LAWD_CD' : Const.LAWD_CD, 'DEAL_YMD' : Const.DEAL_YMD }

        url = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade"

        #request 보내기
        response = requests.get(url, params=params)
        xmlobj = bs4.BeautifulSoup(response.content , 'lxml-xml')

        rows = xmlobj.findAll('item')

        columns =rows[0].find_all()

        result = []
        rowList = []
        #nameList = []
        #columnList = []
        rowsLen = len(rows)
        
        dic = {}
        for i in range(0 , rowsLen):
            columns = rows[i].find_all()

            columnsLen = len(columns)
            for j  in range(0,columnsLen):
                eachColumn =columns[j].text.strip().replace("," , "")
                dic[columns[j].name] = eachColumn
            result.append(dic)
            dic = {}

        print(result)
        return result