import datetime

today                       = datetime.datetime.now()
yesterday                   = today - datetime.timedelta(days=30)
yesterday_unix_timestamp    = int(yesterday.timestamp()) * 1000

print(today)
print(yesterday)
print(yesterday_unix_timestamp)