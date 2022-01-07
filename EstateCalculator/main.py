#모듈호출
import sys
#import Const 
from HttpUtil import httpUtil
from DTO.EstateDTO import EstateDTO
from EstateDao import EstateDao

def main():

    http= httpUtil()

    #부동산 api 실행결과
    result = http.run_http()
    dao = EstateDao(); 
    dao.AccessDB(result)
if __name__=="__main__":
    main()


















