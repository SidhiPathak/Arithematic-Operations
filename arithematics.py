from multiprocessing import Process

def addition(numbers):
    result = 0
    for number in numbers:
        result+=int(number)
    print(f"sum of {number_list} is: ",result)
    return result

def subtraction(numbers):
    result = int(numbers[0])
    for i in range(len(numbers)):
        if i<(len(numbers)-1):
            result=result-int(numbers[i+1])
    print(f"Subration of {number_list} is: ",result)
    return result

def multiplication(numbers):
    result = int(numbers[0])
    for i in range(len(numbers)):
        if i<(len(numbers)-1):
            result=result*int(numbers[i+1])
    print(f"Multiplication of {number_list} is: ",result)
    return result

def division(numbers):
    result = float(numbers[0])
    for i in range(len(numbers)):
        if i<(len(numbers)-1):
            result=result/float(numbers[i+1])
    print(f"Division of {number_list} is: ",result)
    return result

print("Enter the number of digits you want to perform arithematic operations: ")
n = input()
number_list = []
i=0
while i<int(n):
    print(f"Enter {i} number: ")
    number = input()
    number_list.append(number)
    i+=1

p1 = Process(target=addition, args=(number_list,))
p2 = Process(target=subtraction, args=(number_list,))
p3 = Process(target=multiplication, args=(number_list,))
p4 = Process(target=division, args=(number_list,))

p1.start()
p2.start()
p3.start()
p4.start()

p1.join()
p2.join()
p3.join()
p4.join()

print("Process Successful!")