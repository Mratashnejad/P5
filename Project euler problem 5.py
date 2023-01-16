# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# 2520 کوچکترین عددی است که می توان بر هر یک از اعداد از 1 تا 10 بدون هیچ باقیمانده ای تقسیم کرد.

# کوچکترین عدد مثبتی که به طور مساوی بر همه اعداد 1 تا 20 بخش پذیر است کدام است؟



def get_divs(n):
    dives = [x for x in range(1,20) if n % x == 0]
    print (dives)
    return dives

get_divs(999999999999999999)
