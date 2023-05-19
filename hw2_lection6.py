n = int(input())
f = open("mails.txt", 'w', encoding='utf8')

for i in range(n):
    name = input()
    with open('mails.txt', 'a') as f:
        f.write(f'\n Спасибо, {name}! Твой подарок ждет тебя под елкой! ')

f = open('mails.txt', 'r')
for line in f:
    print(line, )


