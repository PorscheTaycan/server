import pymysql
import pandas as pd

con = pymysql.connect(host="192.168.31.87", user='root', password='0000', db='team4', charset='utf-8')
#역할 connection 객체 생성
cur = con.cursor() # 커서 객체 생성 C# cmd와 같은 역할

sql = "SELECT ~~~~~~~ FROM ~~~~~~~~"

values=[("1", "name", "id", "~~~"), ("2", "name2", "id2","~~~")]
sql2 = "INSERT INTO (A, B, C, D, E, F) VALUES('11', 'name', '3', '4', '5', '6')"
sql3 = "INSERT INTO (A, B, C, D, E, F) VALUES(%s, %s, %s, %s, %s, $%S)"

cur.executemany(sql3, values) # 변수 values값을 통한 sql 실행


cur.execute(sql) # sql 문법을 실행한다. execute


############################################  데이터 가져오기
data = cur.fetchall() # 모든 데이터 가져오는 함수
# fetchone : 데이터 한 행 가져오기

print(data)

res_df = pd.read_sql(sql, con)

print(res_df)
print(res_df.keys())
print(res_df.tail(1))

con.close()