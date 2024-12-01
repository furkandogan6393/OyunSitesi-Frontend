import datetime

brithay = datetime.datetime(2000, 5, 12, 15, 20, 6)
result = datetime.datetime.timestamp(brithay)
result = datetime.datetime.fromtimestamp(result)
result = datetime.datetime.fromtimestamp(0)

print(result)
print(brithay)
