from django.db import models
from mongoengine import *

# Create your models here.

# 指明要连接的数据库
connect('Complaint',host = '127.0.0.1',port = 27017)

class invitation(Document):
    # 定义数据库中的所有字段
    number = StringField()
    title = StringField()
    content = StringField()
    url = StringField()

    # 指明连接的数据表名
    meta = {'collection':'invitation'}

# 测试是否连接成功
# for i in invitation.objects[:10]:
#     print(i.title)