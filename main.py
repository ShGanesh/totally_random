import time
from datetime import datetime

def rand():
	lst = time.strftime("%Y %I %W %y %m %j %S %M").split(" ")
	lst = list(map(int, lst))
	lst = [i for i in lst if i != 0]
	ans = 1
	for i in lst[:-3]:
		ans *= i
	ans += lst[-2]**2 - lst[-1]**3 + int(datetime.now().strftime("%f"))
	st = int("".join(list(set(list(str(ans))))))

	return st



if __name__ == "__main__":
    print(rand())