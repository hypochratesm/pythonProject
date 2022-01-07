from DBUtil import DBUtil 
import Const

class EstateDao :
    pass
    def __init__(self) :
        pass

    def AccessDB(self,result) :

        for item in result :
            pass
            try:
                sql = "insert into APT_DEAL_LIST(DEAL_AMOUNT,BUILD_YEAR,DEAL_YEAR,DONG,APARTMENT_NAME,DEAL_MONTH,DEAL_DAY,AREA_EXCL,JIBUN,REGIONAL_CODE,FLOR,REQ_GBN,CONTRACT_MONTH) values ({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12})".format(item['거래금액'] , "'"+item['건축년도']+ "'","'"+item['년']+ "'","'"+item['법정동']+ "'","'"+ item['아파트'] + "'","'"+item['월']+ "'","'"+item['일']+ "'",item['전용면적'],"'"+item['지번']+ "'","'"+item['지역코드']+ "'","'"+item['층']+ "'","'" + "A" + "'","'" + "202201" + "'")
                dao =DBUtil();
                dao.run(sql);
            except SyntaxError as e:
                print(e)
            
