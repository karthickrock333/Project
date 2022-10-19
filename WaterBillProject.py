c=int(input("corporation water: "))
b=int(input("Bore-well water: "))
print(f"Water ratio is {c}:{b}")
bhk=int(input("BHK 2 or 3 : "))
guest=0
if bhk==2:
    Bhk2_Water=900
    while bhk > 0:
        G = int(input("Guest: "))
        guest += G
        if G == 0:
         water = ((3 + guest) * 10 * 30)
         tank_water=abs(water - Bhk2_Water)
         M = Bhk2_Water*(c/(c+b))
         N = abs(900-M)
         Normal_Water_price = ((M * 1) + (N * 1.5))
         break

elif bhk==3:
    Bhk3_Water=1500
    while bhk > 0:
        G = int(input("Guest: "))
        guest += G
        if G == 0:
         water = ((5 + guest) * 10 * 30)
         tank_water = abs(water - Bhk3_Water)
         M = Bhk3_Water*(c/(c+b))
         N = Bhk3_Water*(b/(c+b))
         Normal_Water_price=int((M*1)+(N*1.5))
         break
else:
    print("This is Wrong option,Try Again.")

if tank_water==0:
    print(f"The Amount of Water {water} Cost of Water {int(Normal_Water_price)}")

elif tank_water in range(0,500):
    price_water=int(abs((tank_water*2)+Normal_Water_price))
    print(f"1The Amount of Water {water} Cost of Water {price_water}")

elif tank_water in range(501,1501):
    actual_amount=abs(500-tank_water)
    price_water=int(abs((500*2)+(actual_amount*3)+Normal_Water_price))
    print(f"The Amount of Water {water} Cost of Water {price_water}")

elif tank_water in range(1501,3001):
    actual_amount=abs(1500-tank_water)
    price_water=int(abs((500*2)+(1000*3)+(actual_amount*5)+Normal_Water_price))
    print(f"The Amount of Water {water} Cost of Water {price_water}")

elif tank_water>3000:
    actual_amount=abs(3000-tank_water)
    price_water=int(abs((500*2)+(1000*3)+(1500*5)+(actual_amount*8)+Normal_Water_price))
    print(f"The Amount of Water {water} Cost of Water {price_water}")











