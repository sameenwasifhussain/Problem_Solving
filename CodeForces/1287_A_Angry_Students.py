test_cases = int(input())

for i in range(0,test_cases):
    num_of_students = int(input())
    student_string = input()
    result = 0
    while 'AP' in student_string:
        result+=1
        print("While:  ",student_string)
        for j in range(0 , num_of_students - 1):
            if student_string[j] == 'A' and student_string[j+1] == 'P':
                print("Before: ",student_string)
                student_string = student_string[:j+1] + 'A' + student_string[j+2:]
                print("After : ",student_string)
    print(result)