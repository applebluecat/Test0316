#print (33.123)
#print(arr1) #註解
#print('你好, hello, hi', 100+40, 100-40, 100*40, 100/40)
#print('先乘除後加減', 100+40*40/40-1)
#print(12+(6-34)*5-4*(3+24/8))
'''
y=-5.0
print(y, 'y+y+y=' , y+y+y)
y= 'age'
print(y, 'y+y+y=' , y+y+y)
#help("keywords")

name='bee'
print('字串練習name =', name)
#可以單引號,也可以雙引號.
print('age')
print("age")

text="ABCDEF"
print('ABCDEF第一個值=',text[0],';ABCDEF倒數第二個值=',text[-2],
';ABCDEF第一個值(start-end):2開始,不要碰到5=',text[2:5],
';ABCDEF第二個值(start-end):2開始=',text[2:],
';ABCDEF第二個值(start-end):2開始,跳1=',text[2:1:1],
'倒著數',text[15:2:-4]
)

text="鼠牛虎兔龍蛇馬羊猴雞狗豬"
print(text[11:1:-2])
print(text[-1:2:-2])

name=input("what is your name?") #要求使用者輸入名字,存入變數.參考指導語:請問貴姓大名.
print("hello!",name,".")        #跟使用者問好,內容包含使用者名字.
print("hello!"+name+".")

#自我介紹
name=input("please input your name:")
age=input("please input your age:")
print("introduction:I am "+name,",my age is "+age)

print("字串乘數字(重覆)","ABC" *3)
print("字串乘浮點數(error)","ABC"*3.3)


#加法計算機:1.存入變數a, 2.存入變數b, 3.計算相加(a+b).
a=input("please input number a:")#input()只會是字串
b=float(input("please input number b:"))
#print("a+b=",int(a) + float(b))
print("a+b="+str((int(a) + b)))


#乘法計算機:1.讓使手者輸入第一個數字,2.讓使用者輸入第二個數字,3.計算出相乘的積(product)並印出來
a = float(input("please input number a=:"))
b=float(input("please input number b="))
print("a*b result =",str(a*b))


#退休年份計機:1.輸入生日年份, 2.加上65, 存入變數退休年份, 3.告訴使用者哪年可以退休:文字內容:您的退休年份為:退休年份
bbYear= input("please input your bith year:")
retiredYear = int(bbYear)+65
print("your retired year is:"+str(retiredYear))


#自我介紹產生器: 文字,變數的練習
name = input("please input your name:")
pet = input("your pet:")
petName = input("your pet name:")
birthYear=input("your birth year:")
retiredYear = int(birthYear)+65
print("My name is",name,",my pet is",pet,",his name is",petName,".I'll retire in",str(retiredYear))

#list
myList = ["奇異果",10,"蘋果",40,"榴槤",1000]
print("製作一份水果及熱量清單",myList)
print(myList[0])#挑出第0個物件

#查詢票房
ticketList = [180,215,134,209,195,220]
ep = int(input("which ep do you query:"))
print("ep"+str(ep),":",ticketList[ep-1])

#修改清單
myList=[1,2,3,4,5]
myList[2]=30
print(myList)


frutList=["apple","melon"]
frutList=frutList+["mango"]
print(frutList)


#字典:索引是標籤
myCalo = {
    "burger":200, 
    "fries" :100, 
    "tea"   :10,
    "ice"   :50,
} #標籤 冒號 箱子 
print("all",myCalo)
print("burger:",myCalo["burger"])

queryCalo=input("input")
print(queryCalo,myCalo[queryCalo])


#值沒有限制
myDic={
    "m":10,
    999:20,
}
print(myDic["m"])
'''
#1.上網搜尋電影資料, 2.為電影建立一個字典, 3.字典包含5組key-value的組合. 4.value類型為1個數字,1個浮點數,1個字串,1個清單,1個字典.
myMovie={
    "name":"霍爾的移動城堡",
    "year":2004,
    "票房-USD":1.9,
     "roleList":["霍爾","蘇菲","卡西法"],
     "processHistory":{2002:"取材",2003:"製片",2004:"威尼斯影展"}
}
print("電影名稱:",myMovie["name"],"\n",
      "上映:",str(int(myMovie["year"])),"\n",
      "票房:",str(float(myMovie["票房-USD"])),"\n",
      "主要演員",myMovie["roleList"][0],"\n",
      "歷史記錄",myMovie["processHistory"][2002],"\n",
      )
