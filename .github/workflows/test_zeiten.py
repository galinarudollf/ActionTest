import sys
from datetime import datetime
def foo(zeit_str):
    d1=datetime.strptime(zeit_str1,"%Y-%m-%d")
#    print(d1)
    d2=datetime.now()
#    print(d2)
    print((d2-d1).seconds)
# longer than a week?
    if (d2-d1).seconds > 7*24*60*60: 
        return 1
    else: 
        return 0

zeit_str1=sys.argv[1]
print(foo(zeit_str1))
