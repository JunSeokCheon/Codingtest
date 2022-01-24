n = int(input())
N_list = []
dic = {}

for i in range(n):
    N_list.append(input())

for i in N_list:
  if i not in dic:
    dic[i] = 1
  else:
    dic[i] += 1


sorted_dic = dict(sorted(dic.items(), key=lambda x: x[0]))
result_dic = sorted(sorted_dic.items(), key=lambda x: x[1], reverse=True)[:1]
print(result_dic[0][0])