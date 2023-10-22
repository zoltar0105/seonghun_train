# drinks = {"커피":500,"콜라":1200,"주스":1400}
# print(drinks["커피"])

def beverage():
    bvg_name = input("음료수를 고르세요  :  커피-500원 | 콜라- 1200원 |  주스 1400원    :")
    if bvg_name == "커피":
        print("커피를 선택했습니다. 잠시만 기다리세요")
        return 1
    elif bvg_name =="콜라":
        print("콜라를 선택했습니다. 잠시만 기다리세요")
        return 2
    elif bvg_name =="주스":
        print("주스를 선택했습니다. 잠시만 기다리세요")
        return 3
    else:
        print("상품을 잘못 선택하셨습니다. 음료수를 다시 고르세요")
        beverage() 
        
    
def cash():
    coin = int(input("현금을 얼마 넣으시겠습니까??"))
    return coin

def calculate(bvg,money):
    if bvg==1:
        if money>500:
            return ["커피",money-500]
            # print("커피가 나왔습니다  거스름돈" ,money-drinks["커피"],"원을 받으세요")
        else:
            # print("돈이 부족합니다. 돈을 더 넣으세요")
            return 00
    if bvg==2:
        if money>1200:
            return ["콜라",money-1200]
            # print("콜라가 나왔습니다  거스름돈" ,money-drinks["콜라"],"원을 받으세요")
        else:
            # print("돈이 부족합니다. 돈을 더 넣으세요")
            return 00
    if bvg==3:
        if money>1400:
            return ["주스",money-1400]
            # print("주스가 나왔습니다  거스름돈" ,money-drinks["주스"],"원을 받으세요")
        else:
            # print("돈이 부족합니다. 돈을 더 넣으세요")
            return 00
        
bvg = beverage()
money = cash()
result=calculate(bvg,money)


if result==00:
    print("돈이 부족합니다 돈을 더 넣으세요")
else:
    print(str(result[0])+"와 거스름돈"+str(result[1])+"을 받으세요")


                
    
        



