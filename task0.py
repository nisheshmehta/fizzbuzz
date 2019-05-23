# this is final quiz
# this is secound commit



def fizzbuzzz(max_num=101):
    for i in range(max_num):
        value = ""
        if i % 3 == 0: value += "Fizz"
        if i % 5 == 0: value += "Buzz"
        yield value if value else i

for number, burp in enumerate(fizzbuzzz()):
    print "%s: %s" % (number, burp)

#https://github.com/nisheshmehta/fizzbuzz.git
