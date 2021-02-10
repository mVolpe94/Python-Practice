import time

multiples_list=[3,5,10,6]
fizzbuzz_list = ['fizz', 'buzz']


def fizzbuzz(i, multiples_list):
    output = ""
    for index in range(len(multiples_list)):
        if i % multiples_list[index] == 0:
            if (index + 1) % 2 == 0:
                char = fizzbuzz_list[1]
            else:
                char = fizzbuzz_list[0]
            output = output + char
    if output == "":
        return str(i)
    else: 
        return output
        
if __name__ == "__main__":
    for i in range(100):
        i += 1
        print(fizzbuzz(i, multiples_list))
    time.sleep(10)