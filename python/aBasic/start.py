
def even_filter(a):
    list1 = []
    for i in a:
        if i%2 == 0:
            list1.append(i)
    return list1

print(even_filter([1, 2, 4, 5, 8, 9, 10]))

def is_prime_number(a):
    for i in range(2,a):
        if a%i == 0:
            return '소수가 아닙니다'
        return '소수 입니다'
    
print(is_prime_number(60))
print(is_prime_number(61))
print(is_prime_number(63))
print(is_prime_number(67))
print("-"*50)
def count_vowel(a):
    b = 0
    for n in a:
        if n== 'a' or n=='e' or n=='i'  or n== 'o'  or n== 'u':
            b += 1
    return b
print(count_vowel("pythonian"))


for i in range(2,10):
    print("{}단 입니다".format(i), end=" ")
    for j in range(1,10):
        print(i*j, end=" ")
    print('')