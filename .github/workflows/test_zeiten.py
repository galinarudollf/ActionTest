import sys
from datetime import datetime, timedelta
def foo1(zeit_str):
    d1=datetime.strptime(zeit_str,"%Y-%m-%d")
#    print(d1)
    d2=datetime.now()
#    print(d2)
#    print((d2-d1).seconds)
# longer than a week?
    if (d2-d1).seconds > 7*24*60*60: 
        return '1'
    else: 
        return '0'

def foo2(zeit_str):
    epoch = datetime.utcfromtimestamp(0)
    today=(datetime.now()-epoch).total_seconds()
#    print(today)
    d=datetime.strptime(zeit_str,"%Y-%m-%d")+timedelta(days=7)
#    print(d)
    firstcommit=(d-epoch).total_seconds()
#    print(firstcommit)
    tomorrow=(datetime.now()+timedelta(days=1)-epoch).total_seconds()
#    print(tomorrow)

    if today < firstcommit and firstcommit <= tomorrow: 
        return '1'
    else: 
        return '0'

zeit_str1=sys.argv[1]
print(foo2(zeit_str1))
