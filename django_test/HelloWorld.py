# coding=utf-8
msg = "HelloWorld!"
print msg

# べき乗は「A ** B」
print 3 ** 4

# 割り算：どちらかが少数であれば、結果は少数
print 4 / 2.0

# 割り算：両方整数なら、結果は整数（小数部切り捨て）
print 10 / 3

# 割り算：少数を使用して、結果の少数部切り捨て
print 10 // 3.0

# エスケープ
print "タブです\t改行です\nダブルクォーテーションです\""

# ["""]で囲むことによって、改行しつつ文章を書くことができる！
print """
改行をしつつ
文章を
かけるよ！
"""

# 日本語を書くときは、先頭に「u」をつけると安心(uはunicodeのu!!)
# 文字列を数える時など、日本語に合わせてカウントしてくれるよ！
print u"日本語"

# 文字列の連結「+」
print "Hello" + "World"

# 文字列の繰り返し「*」
print u"無駄！" * 10

# 文字列の長さ「len」
print len("何文字かな？")
# uをつけると日本語安心
print len(u"何文字かな？")

# 文字列の操作
s = "abcdefghi"


# 文字列の切り出し [] [start:end] ※endは含まない
print s[1]
print s[1:5]
print s[1:]
print s[:3]
print s[1:-1]

# 文字列検索 find  ※値が見つからないときは、「-1」が返る
print s.find("def")
print s.find("cx")

# 文字列と数値の変換
# 文字列⇒数値 int / float
print 5 + int("5")

# 数値⇒文字列
age = 23
print "i am " + str(24) + " years old."

# リスト 型は自由
a = [1, 2, "a", 5.5]
b = list([3, 5])

print a
print b

# リストの長さを調べる
print len(a)

print a + b
print a * 5
print a[2]

a[2] = "b"
print a

# 2から4を変える
a[2:4] = ["b", "c"]
print a

# sort / reverse
c = [1, 5, 2, 10]
c.sort()
print c

c.reverse()
print c

# in 含まれているか確認
print 5 in c
print 3 in c

# range 配列を作ってくれる
# 0 から 10 未満
d = range(10)
print d
# 3 から 10 未満
e = range(3, 10)
print e
# 2 飛びで 3 から 10 未満
f = range(3, 10, 2)
print f

# リストと文字列の相互変換
# split / join
g = "2012/10/12"
h = g.split("/")
print h

gg = ["a", "b", "c"]
hh = "-".join(gg)
print hh

# タプル ⇒ 変更不可能なリスト
i = (1, 5, 8)
print i

#  len []
print i[0]

# タプルとリストの相互変換
j = list(i)
print j

k = tuple(j)
print k

# セット ⇒ 集合型のデータ(重複不可)
l = set(["taro", "yamada", "suzuki", "taro"])
print l
m = set(["taro", "yamada", "sasai"])
# - ⇒l にあって m にないもの
print l - m
# | ⇒l と m にあるもの
print l | m
# & ⇒l と m 両方にあるもの
print l & m
# ^ ⇒l と m どちらか片方にしかないもの
print l ^ m

# 辞書型 （Hash）
# key value がセットになっている
n = {"tajima": 200, "fuji": 300, "dotinstall": 500}
print n["tajima"]
n["fuji"] = 5000
print n

# in ⇒key の存在チェック
print "tajima" in n
print "wada" in n

# keys, values, items
print n.keys()    # key のみをリストに
print n.values()  # value のみをリストに
print n.items()   # タプルにする

# print の使い方
m = 10
o = "taguchi"
p = {"taguchi": 100, "fkoji": 200}
# 整数値：%d  小数点：%f  文字列：%s
print "my age is %d" % m
# 桁数の指定
print "my age is %5d" % m
# 桁数が満たない場合は「0」で埋める
print "my age is %05d" % m

print "my name is %s" % o
# 複数
print "%s is %d years old" % (o, m)
# リスト
print "%(taguchi)d" % p

# if文の使用
# >= <= > < == !=
score = 70
if score >= 80:     # :で真のとき
    print "pass!"   # ブロックをインデントで示す！
else:
    print "not pass..."

# 一行で
print "pass!" if score >= 80 else "not pass..."

# 条件を続けるとき
if score >= 80:
    print "OK!"
elif score >= 60:  # elseif は elif
    print "so so"
    print u"インデントがそろっていればOK！"
else:
    print "oh..."

if 40 < score < 60:
    print "..."

# 繰り返し処理
sum1 = 0
for q in [1, 7, 3, 4, 5]:
    sum1 += q
print sum1

# for 文の else
# 繰り返し処理の最後の一回のみ。
sum2 = 0
for q in [1, 3, 5, 2, 3]:
    sum2 += q
else:
    print sum2     # 上と同じ処理

# 単純な繰り返しはレンジを使う
# continue スキップする処理を決める
for s in range(10):
    if s == 3:
        continue
    print s
else:
    print "end"


# break 繰り返し処理自体を止める（※elseも実行されない）
for r in range(10):
    if r == 3:
        break
    print r
else:
    print "end"

# 辞書型のデータをfor文で使う
t = {"yamaguchi": 300, "dotinstall": 200, "fkoji": 400}

# key と value 両方を使用
for k, v in t.iteritems():
    print "key: %s value: %d" % (k, v)

# key のみを使用
for k in t.iterkeys():
    print k

# value のみを使用
for v in t.itervalues():
    print v

# 繰り返し（while 文）
# continue / break も使用できる
n = 0
while n < 10:
    if n == 3:
        n += 1
        continue
    if n == 6:
        break
    print n
    n += 1
else:
    print "while end"

# 関数(def)
def Kansu1():
    print "Kansu"   # インデントをつけた部分が中身


print u"関数呼び出し。呼ばれるのはここ。↓"
Kansu1()

# 関数(引数有り)
def Hello(people):
    print "Hello %s" % people


print u"関数呼び出し"
Hello("Taro")
Hello("Jargon")

# 関数（引数複数）
def Hello2(name, num):
    print "My name is %s . %d years old." % (name, num)


Hello2("Tom", 2)
Hello2("Stave", 3)

# 引数に初期値を入れることもできる。(呼び出し時に引数が設定されていればそれを反映)
# return を使用して値を返すこともできる。
# pass : 関数の中に処理がないことを明示。(※中身は後で書こう、とかそういうこと)
def hello(name, num=3):  # numに初期値を代入
    return "hello! %s !" % name * num


s = hello(num=2, name="Tom")     # 引数の順番がばらばらでもいけたりする。
print s
s = hello("Sum")                 # num を入力していないため、初期値の3が入力される。


def hello2():
    pass        # 後で処理を書くよ。ここでは宣言だけ。っていうのを明記

# 関数のスコープ
# 関数内の変数は関数内でのみ使用することができる
name1 = "globals"


def locals():
    name1 = "locals"
    print name1


print name1
locals()

# 関数とリスト
# リストの値を入れて順に処理してくれる
def double(x):
    return x + x


print map(double, [1, 2, 5])

# 無名関数 lambda 引数:return値
# 一回のみ使用の、名前を付けるほどでもない関数
print map(lambda x: x + x, [1, 2, 5])

# オブジェクト（変数と関数をまとめたもの）
# クラス：オブジェクトの設計図
# インスタンス：クラスを実体化したもの

class Person(object):
    def __init__(self, name):    # self は決まり文句として絶対書く
        self.name = name

    def greet(self):
        print "my name is %s" % self.name


bob = Person("Bob")
tom = Person("Tom")
print bob.name
bob.greet()
tom.greet()

# クラスは継承することができる
class SuperPerson(Person):  # 継承したいものを引数にする。複数ある時はカンマで区切る
    def shout(self):
        print "%s is SUPER!" % self.name

tom = SuperPerson("Tom")
tom.shout()

# モジュール
import math
import random
from datetime import date   # datetime というモジュールの中から date に関するもののみを使用

print math.pi            # 円周率
print math.ceil(5.2)     # 繰り上げ
print random.random()

print date.today()






































