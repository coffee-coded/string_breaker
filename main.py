s = input().split()
n = int(input())
ans = []
tmp = ""
for i in s:
    if len(i) <= n and tmp == "":
        tmp = i
    elif len(tmp) + len(" ") + len(i) <= n:
        tmp += " " + i
    elif len(tmp) == 0:
        ans = None
        break
    else:
        ans.append(tmp)
        tmp = ""
        if len(i) < n:
            tmp = i
if len(tmp) > 0:
    ans.append(tmp)
if ans:
    print(ans)
else:
    print("null")
