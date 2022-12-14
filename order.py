"""
O(n): Big O
・プログラムの計算にかかる時間を表している
・データ量が増えていくとどれくらい時間がかかるかを表す
・この式を見ることで、どんな風に処理が書かれているかがなんとなくわかる
"""

# O(log(n))
def func2(n):
    if n <= 1:
        return
    else:
        print(n)
        return func2(n/2)

# O(n)
def func3(numbers):
    for num in numbers:
        print(num)

# O(n * log(n))
def func4(n):
    for i in range(int(n)):
        print(i, end=' ')
    print()

    if n <= 1:
        return
    func4(n/2)

# O(n**2)
def func5(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(numbers[i], numbers[j])
        print()



# func2(10)
# func3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# func4(10)
func5([1, 2, 3, 4, 5])