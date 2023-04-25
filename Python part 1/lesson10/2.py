"""a, b = int(input()), int(input())
if b == 0:
    raise ZeroDivisionError"""

'''
try:
    val = int(input())
    tmp = 10 / val
    print(tmp)
except ZeroDivisionError as div_exc:
    print("ZeroDivisionError:", div_exc)
except:
    print("Unknown error!")
else:
    print("result=", tmp)
finally:
    print("Finally code")'''

try:
    try:
        try:
            print("1"+1)
        except Exception as exc:
            print("Exceprion level 3", exc)
            raise
    except Exception as exc:
        print("Exception level 2:", exc)
        raise Exception("New message!")
except Exception as exc:
    print("Exception level 1", exc)

