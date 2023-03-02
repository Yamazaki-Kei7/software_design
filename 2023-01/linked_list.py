class Node:
    def __init__(self, value=""):
        self.nex = None
        self.pre = None
        self.value = value

# 双方向連結リストの初期化
nil = Node()
nil.nex = nil
nil.pre = nil

# ノードnilの直後にノードvを挿入する
def insert(v, nil):
    v.nex = nil.nex
    (nil.nex).pre = v
    nil.nex = v
    v.pre = nil

# ノードvを削除する
def erase(v):
   (v.pre).nex = v.nex
   v.nex.pre = v.pre

# 連結リストの中身を順に出力する
def printList():
    values = []
    print("nil:", nil.value)
    cur = nil.nex
    while cur != nil:
        values.append(cur.value)
        cur = cur.nex
    print(values)

# 連結リストを作る
sato = Node("sato")
suzuki = Node("suzuki")
takahashi = Node("takahashi")
ito = Node("ito")
watanabe = Node("watanabe")
yamamoto = Node("yamamoto")
nodes = [yamamoto, watanabe, ito, takahashi, suzuki, sato]
for node in nodes:
    insert(node, nil)
print("Before: ")
printList()

# 「渡辺」ノードを削除する
erase(watanabe)
print("After: ")
printList()
