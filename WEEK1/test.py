# '''Item クラス'''
# class Item:
    
#     '''初期化メソッド'''
#     def __init__(self, name, price):
#         self.__data = {"name":name, "price":price} #辞書型のオブジェクト
    
#     '''辞書の"name"キーの値は参照と変更が可能にします。'''
#     @property
#     def name(self):
#         return self.__data["name"]
    
#     @property
#     def price(self):
#         return self.__data["price"]

#     @price.setter
#     def price(self, value):
#         self.__data["price"] = value
    
#     '''辞書の"price"キーはgetterメソッドしか書かないのでリードオンリーになります。'''
    

#     '''Itemクラスのインスタンスを作ります。'''
# watch = Item("Rolex", 100000)

# '''インスタンス変数の name は、getterとsetterの両方のプロパティが用意されているので、読み取りも変更も可能です。'''
# watch.price = "Omega" #nameの値を変更します。
# print(watch.name) #確認しましょう。

# def a():
#     def b():
#         return 'bです。'
#     return b

# print(a()())  # b関数オブジェクトを出力
# # <function a.<locals>.b at 0x107de8158>

# def a(func):  # 関数を引数に取る関数
#     return func

# def b(name):
#     return 'hello! ' + name

# print(a(b)("fa"))  # a関数の実行結果を出力
# # <function b at 0x103a05488>  # b関数が出力される

# # デコレータとなる関数
# def a(func):
#     def b():
#         print('スタート')
#         func()  # func()=c関数の実行　→ 'c関数を実行しています。'
#         print('おわり')
#     return b

# # デコレートされる関数
# @a
# def c():
#     print('c関数を実行しています。')

# c()  # b関数の実行（func=c）
# # スタート
# # c関数を実行しています。
# # おわり

# def adult(func):
#     def checker(name, age):
#         if age >= 20:
#             print(f'{name}は大人なので処理を実行します。')
#             func(name, age)  # func(≒drink関数)を実行
#             print('処理が完了しました。')
#         else:
#             print(f'{name}は未成年なので処理は実行できません。')
#     return checker

# @adult
# def drink(name, age):
#     """飲酒する"""
#     print(f'{name}({age})「ゴクゴク、ぷはーっ！」')

# # drink関数を実行する。（ageの値によっては実行されない）
# drink('Jobs', 21)
# # Jobsは大人なので処理を実行します。
# # Jobs(21)「ゴクゴク、ぷはーっ！」
# # 処理が完了しました。

# drink('Rola', 12)
# # Rolaは未成年なので処理は実行できません。





# The parent class
# class Shape:
#     def __init__(self, w, l):
#         self.width = w
#         self.len = l
#     def print_size(self):
#         print(f"It is {self.width} cm wide, {self.len} cm long.")

# # The child class
# class Square(Shape):

#     def print_size(self):
#         print(self.width*self.len)

# # Check
# square = Square(10, 10)
# square.print_size()
# shape = Shape(10, 10)
# shape.print_size()



# a = 10 / 0
# print("{0}".format(a))

# try:
#     a = 10 / 0
#     print("{0}".format(a))
# except ZeroDivisionError:
#     print("ZeroDivisionError!!")

# try:
#     a = 10 / 0
#     print("{0}".format(a))
# except ValueError:
#     print("ZeroDivisionError!!")



