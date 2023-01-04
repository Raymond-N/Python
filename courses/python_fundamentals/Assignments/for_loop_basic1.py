# 1. Basic - Print all integers from 0 to 150.

for int in range(151):
    print(int)

# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for mult in range(5,1001):
    if mult % 5 == 0:
        print(mult)

# 3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for num in range(1,101):
    if num % 10 == 0:
        num = "Coding Dojo"
    elif num % 5 == 0:
        num = "Coding"
    print(num)

# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

sum = 0

for odd_int in range(500000):
    if odd_int % 2 == 1:
        sum = sum + odd_int

print(sum)

# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for pos_num in range(2018,0,-4):
    print(pos_num)

# 6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

low_num = 2
high_num = 2578
mult = 4

for flex_count in range(low_num,high_num):
    if flex_count % mult == 0:
        print(flex_count)