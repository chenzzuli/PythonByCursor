"""
Python 循环语句示例
包含 for 和 while 循环的常用用法
"""

# ==================== for 循环示例 ====================

# 1. 基本数字循环
print("\n1. 基本数字循环:")
for i in range(5):  # 0到4
    print(f"数字: {i}")

# 2. 指定范围的循环
print("\n2. 指定范围的循环:")
for i in range(2, 6):  # 2到5
    print(f"范围数字: {i}")

# 3. 带步长的循环
print("\n3. 带步长的循环:")
for i in range(0, 10, 2):  # 0,2,4,6,8
    print(f"步长为2: {i}")

# 4. 遍历字符串
print("\n4. 遍历字符串:")
for char in "Python":
    print(f"字符: {char}")

# 5. 遍历列表
print("\n5. 遍历列表:")
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"水果: {fruit}")

# 6. 使用 enumerate 获取索引和值
print("\n6. 使用 enumerate:")
for index, fruit in enumerate(fruits):
    print(f"索引 {index}: {fruit}")

# 7. 遍历字典
print("\n7. 遍历字典:")
person = {"name": "张三", "age": 25, "city": "北京"}
for key, value in person.items():
    print(f"{key}: {value}")

# 8. 嵌套循环
print("\n8. 嵌套循环:")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# 9. 列表推导式
print("\n9. 列表推导式:")
squares = [x**2 for x in range(5)]
print(f"平方数列表: {squares}")

# ==================== while 循环示例 ====================

# 1. 基本 while 循环
print("\n1. 基本 while 循环:")
count = 0
while count < 5:
    print(f"计数: {count}")
    count += 1

# 2. 带条件的 while 循环
print("\n2. 带条件的 while 循环:")
number = 10
while number > 0:
    print(f"数字: {number}")
    number -= 2

# 3. 使用 break 退出循环
print("\n3. 使用 break 退出循环:")
count = 0
while True:
    if count == 3:
        break
    print(f"break 示例: {count}")
    count += 1

# 4. 使用 continue 跳过当前迭代
print("\n4. 使用 continue 跳过当前迭代:")
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(f"continue 示例: {count}")

# 5. while-else 语句
print("\n5. while-else 语句:")
count = 0
while count < 3:
    print(f"while-else 示例: {count}")
    count += 1
else:
    print("循环正常结束")

# 6. 用户输入循环
print("\n6. 用户输入循环示例 (已注释):")
"""
while True:
    user_input = input("请输入 'quit' 退出: ")
    if user_input.lower() == 'quit':
        break
    print(f"你输入了: {user_input}")
"""

# 7. 计数器循环
print("\n7. 计数器循环:")
total = 0
count = 1
while count <= 5:
    total += count
    count += 1
print(f"1到5的和: {total}")

# 8. 条件组合的 while 循环
print("\n8. 条件组合的 while 循环:")
x = 0
y = 10
while x < 5 and y > 5:
    print(f"x={x}, y={y}")
    x += 1
    y -= 1

# 9. 无限循环与条件退出
print("\n9. 无限循环与条件退出:")
"""
while True:
    response = input("继续吗？(y/n): ")
    if response.lower() != 'y':
        break
    print("继续执行...")
"""

# ==================== 实际应用示例 ====================

# 1. 计算阶乘
print("\n1. 计算阶乘:")


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(f"5的阶乘: {factorial(5)}")

# 2. 斐波那契数列
print("\n2. 斐波那契数列:")


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b


print("斐波那契数列前10项:")
fibonacci(10)

# 3. 查找最大最小值
print("\n\n3. 查找最大最小值:")
numbers = [23, 45, 67, 12, 89, 34]
max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(f"最大值: {max_num}")
print(f"最小值: {min_num}")

# 4. 密码验证示例
print("\n4. 密码验证示例 (已注释):")
"""
max_attempts = 3
attempts = 0
correct_password = "1234"

while attempts < max_attempts:
    password = input("请输入密码: ")
    if password == correct_password:
        print("密码正确！")
        break
    attempts += 1
    print(f"密码错误！还剩 {max_attempts - attempts} 次机会")
else:
    print("尝试次数已用完！")
""" 