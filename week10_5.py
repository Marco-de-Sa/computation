nums = [i+1 for i in range(10)]
ops = [nums[i]*3-1 for i in range(len(nums))]
oddn = [i+1 for i in range(10) if (i+1) % 2 != 0]
evenn = [i+1 for i in range(10) if (i+1) % 2 == 0]
print(f"{nums}\n{ops}\n{oddn}\n{evenn}")