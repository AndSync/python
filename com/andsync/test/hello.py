# print ('hello');
print(ord('中'));

age=3;
if age<18:
    print('young');
else:
    print('old');

names=['zhangsan','lisi','wangwu'];
for name in names:
    print(name)

sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum=sum+x
print(sum)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)
print(list(range(100)))

n=1
while n<=100:
    n = n + 1;
    if n%2==0:
        continue
    print(n)

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Bob']=90
print(d.get('Bob2'))

s=set([2,3,4,5,])
print(s)
help(abs)
print(hex(100))