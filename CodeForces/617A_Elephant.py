dis_remaining = int(input())

num_of_steps = int(0)

for i in reversed(range(1,6)):
    num_of_steps += dis_remaining // i
    dis_remaining = dis_remaining % i

print(num_of_steps)
