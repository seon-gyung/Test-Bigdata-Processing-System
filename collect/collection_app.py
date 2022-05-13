# collection 안에 있는 모든 함수를 다 쓰겠다
from collection import *

datas = []
for i in range(1, 21):
    naver_data = naver_craw(i)
    datas.append(naver_data)

mongo_save(mongo, datas, "greendb", "naverss")  # List안에 dict을 넣어야 함
