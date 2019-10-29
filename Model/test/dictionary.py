# -*- coding: utf-8 -*-

from collections import defaultdict

addressData = defaultdict(dict)

# TODO: 仮データを適当に作成する
code1 = "111"
address1 = "ああああああああああああああああああああああ"
name1 = "name1"
# latitude1 = ..........
# ..........

code2 = "222"
address2 = "いいいいいいいいいいいいいい"
name2 = "name2"

code3 = "333"
address3 = "うううううううううううううううううううううううううううう"
name3 = "name3"

code4 = "111"
address4 = "aaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccccccccccc"
name4 = "name4"

code5 = "111"
address5 = "ddddddddddddd"
name5 = "name5"


addressData[code1]["address"] = address1
addressData[code1]["name"] = name1
# ...

addressData[code2]["address"] = address2
addressData[code2]["name"] = name2
# ...

addressData[code3]["address"] = address3
addressData[code3]["name"] = name3
# ...

addressData[code4]["address"] = address4
addressData[code4]["name"] = name4
# ...

addressData[code5]["address"] = address5
addressData[code5]["name"] = name5
# ...

# まずそのままprintしてみる
print(addressData)

# 各codeで検索してみる
test_code1 = "222"
test_code2 = "123"
print(addressData[test_code1])
print(addressData[test_code2])

# 特定のcodeのaddressを取得してみる
test_code3 = "111"
test_code4 = "123"
print(addressData[test_code3]["address"])
print(addressData[test_code4]["address"])



