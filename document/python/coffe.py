#_*_ coding: utf-8-*-
# coffe.py
coffe = 10
while True:
 money = int(input("돈을 넣어주세요:"))
 if money == 300:
   print("커피를 드립니다");
   coffe = coffe-1;
 elif money > 300:
   print("거스름돈 %d를 주고 커피를 줍니다."% (money - 300))
   coffe = coffe -1
 else :
   print('돈을 다시 돌려주고 커피를 주지 않습니다.')
   print("남은 커피의 양은 %d개 입니다. "% coffe);
 if not coffe :
   print ("커피가 다 떨어졌습니다.판매를 중지합니다.");
   break;
