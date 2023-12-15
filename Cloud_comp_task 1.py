#- Find the value of x, such that:
import time

#𝑥 = 𝑎 + 𝑏
#𝑎 𝑎𝑛𝑑 𝑏 𝑎𝑟𝑒 𝑎𝑛𝑦 𝑝𝑜𝑠𝑖𝑡𝑖𝑣𝑒 𝑖𝑛𝑡𝑒𝑔𝑒𝑟 𝑛𝑢𝑚𝑏𝑒𝑟𝑠 𝑙𝑒𝑠𝑠 𝑡ℎ𝑎𝑛 10.
#Task 1
for a in range(1, 10):
    print(str(a) + "a")
    for b in range(1, 10):
        print(str(b) + "b")

        if a + b == 10:
            print(str(a) +" and "+ str(b)  +" is equal 10")
