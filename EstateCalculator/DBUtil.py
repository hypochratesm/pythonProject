import pymysql # pymysql
import pandas as pd
class DBUtil :
    #생성자
    def __init__(self):
        pass

    #sql 실행
    def run(self,sql,params) : 

        try:

            conn = None
            cur = None
            conn = pymysql.connect(host = '127.0.0.1' , user = 'root' , password='root' , db= 'pythonDB' , charset= 'utf8')
            cur = conn.cursor() # cursor는 sql 실행
            cur.execute(sql ,params)
            conn.commit()
            conn.close()

        except BaseException as e:
            print(e)
            #conn.rollback()
            conn.close()

if __name__=="__main__":
    
    df_sheet_index = pd.read_excel('C:/Users/qraft/Documents/메타 코드(값) 리스트_20170927.xlsx' , sheet_name='BANK LIST')

    for idx in range(len(df_sheet_index)):
        
        tList = tuple(df_sheet_index.values[idx])
        print(tList)    
        sql = "INSERT INTO pythondb.cmn_dm_info_detail(CMN_KEY, CMN_SRNO, CMN_VAL,CMN_VAL_NM , CMN_DES, USE_YN,VAL_STDT,VAL_ENDT, RG_ID, CG_ID) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        params= (tList[0] ,tList[4], tList[2], tList[3],  tList[5] , 'Y' ,'2022-01-11' , '9999-12-31', 'robo','robo')
        DBUtil.run("", sql, params)

