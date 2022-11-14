temp={'월':25.5,'화':28.3,'수':33.2,'목':32.1,'금':17.3,'토':35.3,'일':33.3}
list_temp=[]
list_temp2=[]
for key in temp.keys():
    if temp[key]>=30:
        list_temp.append(key)
for i in range(0,len(list_temp)):
    list_temp2.append(list_temp[i])
print(f"기온이 30˚ 이상인 요일 : {', '.join(list_temp2)}")