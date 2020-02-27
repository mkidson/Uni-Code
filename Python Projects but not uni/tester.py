

# def twist(input):
#     max=len(input)
#     for i in range(max):
#         print(input)
#         input= input[-1]+input[0:max-1]

# print(twist("Neo"))


word = 'hello'
count = 0

for i in word:
        for c in word:
                if c != i:
                        count += 1

print(count)