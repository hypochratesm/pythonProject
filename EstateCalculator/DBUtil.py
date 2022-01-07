import pymysql # pymysql

class DBUtil :
    #생성자
    def __init__(self):
        pass

    #sql 실행
    def run(self,sql) : 

        try:

            conn = None
            cur = None
            conn = pymysql.connect(host = '127.0.0.1' , user = 'root' , password='root' , db= 'estate_crawller' , charset= 'utf8')
            cur = conn.cursor() # cursor는 sql 실행
            cur.execute(sql)
            conn.commit()
            conn.close()

        except BaseException as e:
            print(e)
            #conn.rollback()
            conn.close()

if __name__=="__main__":
    sql = "select * from APT_DEAL_LIST"
    DBUtil.run("",sql)

