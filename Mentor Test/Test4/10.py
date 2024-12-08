# 10. Sum Fractions Using GCD and LCM
# Task:
# Write a function that sums two fractions and returns the result in its simplest form. The
# fractions will be given as two tuples, where each tuple consists of two integers: the
# numerator and the denominator. To simplify the result, you need to compute the Least
# Common Multiple (LCM) and Greatest Common Divisor (GCD) of the denominators.
# Then, simplify the result by dividing both the numerator and denominator by their GCD.
# Test Cases:
# ● Input: frac1 = (1, 2), frac2 = (1, 3)
# Output: (5, 6)
# Explanation: The LCM of 2 and 3 is 6. The sum is (1 * 3) / 6 + (1 * 2) / 6
# = 3/6 + 2/6 = 5/6.
# ● Input: frac1 = (1, 4), frac2 = (1, 4)
# Output: (1, 2)
# Explanation: The LCM of 4 and 4 is 4. The sum is (1/4 + 1/4) = 2/4 = 1/2.
# ● Input: frac1 = (2, 5), frac2 = (1, 5)
# Output: (3, 5)
# Explanation: The LCM of 5 and 5 is 5. The sum is (2/5 + 1/5) = 3/5.
# ● Input: frac1 = (3, 4), frac2 = (5, 6)
# Output: (19, 12)
# Explanation: The LCM of 4 and 6 is 12. The sum is (3 * 3) / 12 + (5 * 2) /
# 12 = 9/12 + 10/12 = 19/12.
# ● Input: frac1 = (5, 12), frac2 = (7, 15)
# Output: (139, 60)
# Explanation: The LCM of 12 and 15 is 60. The sum is (5 * 5) / 60 + (7 * 4)
# / 60 = 25/60 + 28/60 = 53/60.
# To calculate the Greatest Common Divisor (GCD) of two numbers in Python, you can use
# the Euclidean algorithm, which is an efficient way to find the GCD. Here's an explanation of
# how to build the GCD function and how the algorithm works:
# Understanding the Euclidean Algorithm
# The Euclidean algorithm finds the GCD of two integers a and b by repeatedly applying the
# following steps:
# 1. Divide aby band calculate the remainder (a % b).
# 2. Replace a with b and b with the remainder from the previous step.
# 3. Repeat the process until the remainder becomes 0. The GCD will be the last
# non-zero value of b.
# Steps to Build GCD Function in Python
# 1. Initial Check: If b becomes 0, then a is the GCD.
# 2. Iterate: Continue the division and remainder operation until the remainder becomes
# 0.
# Understanding and Building LCM (Least Common Multiple) in Python
# The Least Common Multiple (LCM) of two integers is the smallest positive integer that is
# divisible by both numbers. The relationship between the LCM and GCD of two numbers can
# be used to efficiently compute the LCM.
# LCM(a, b) = |a * b| / GCD(a, b)
import math


#--------------------------------------------------#
#             ა რ  მ უ შ ა ო ბ ს                   |
#--------------------------------------------------#

# #ვქმნი ფუნქციაც რათა დავითვალო უმცირესი საერთო ჯერადი
def lcm(x,y):
    max_val = max(x,y)
    while True:
        if max_val % x == 0 and max_val % y == 0:
            return max_val
        max_val += 1

#ვეძებ უდიდეს საერთო გამყოფს
def gcd(x, y):
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x

def fraction(frac1, frac2):
    # ამომაქვს რიცხვები გადმოცემული tuple არგუმენტიდან და ვუტოლებ a / b ცვლადებს
    a,b = frac1
    # ამომაქვს რიცხვები გადმოცემული tuple არგუმენტიდან და ვუტოლებ c / d ცვლადებს
    c,d = frac2

    # ვეძებ უმცირეს საერთო მნიშვნელს
    common_denominator = lcm(b,d)


    new1 = a * (common_denominator // b) # ვამრავლებ მრიცხველს რადგან შეიცვალა მნიშვნელი... როგორ ავხსნა ეს არვიცი ;დდდდდ
    new2 = a * (common_denominator // b) # ვამრავლებ მრიცხველს რადგან შეიცვალა მნიშვნელი... როგორ ავხსნა ეს არვიცი ;დდდდდ

    # ვუმატებ ერთამენთს მრიცხველებს
    sum = new1 + new2

    #ვამარტივებ წილადს
    gcd_res = gcd(sum, common_denominator)
    simple1 = sum // gcd_res
    simple2 = common_denominator // gcd_res


    return (simple1, simple2)

print(fraction((1,2), (1,3)))
print(fraction((1,4), (1,4)))
print(fraction((2,5), (1,5)))
print(fraction((3,4), (5,6)))
print(fraction((5,12), (7,12)))





def fractions(frac1, frac2):
    # ამომაქვს რიცხვები გადმოცემული tuple არგუმენტიდან და ვუტოლებ a / b ცვლადებს
    a,b = frac1
    # ამომაქვს რიცხვები გადმოცემული tuple არგუმენტიდან და ვუტოლებ c / d ცვლადებს
    c,d = frac2

    # ვეძებ უმცირეს საერთო მნიშვნელს
    lcd = math.lcm(b,d)

    new1 = a * (lcd // b) # ვამრავლებ მრიცხველს რადგან შეიცვალა მნიშვნელი... როგორ ავხსნა ეს არვიცი ;დდდდდ
    new2 = c * (lcd // d) # ვამრავლებ მრიცხველს რადგან შეიცვალა მნიშვნელი... როგორ ავხსნა ეს არვიცი ;დდდდდ

    # ვუმატებ ერთამენთს მრიცხველებს
    sum = new1 + new2

    #ვამარტივებ წილადს
    gcd_res = math.gcd(sum, lcd)
    simple1 = sum // gcd_res
    simple2 = lcd // gcd_res

    return (simple1, simple2)


print(fractions((1,2), (1,3)))
print(fractions((1,4), (1,4)))
print(fractions((2,5), (1,5)))
print(fractions((3,4), (5,6)))
print(fractions((5,12), (7,15)))