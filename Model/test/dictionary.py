# -*- coding: utf-8 -*-

from collections import defaultdict

addressData = defaultdict(dict)



# TODO: 仮データを適当に作成する
code1 = "650"
address1 = "toukyou"
name1 = "tokyo"
# latitude1 = ..........
# ..........

code2 = "651"
address2 = "oosaka"
name2 = "osaka"

code3 = "650"
address3 = "koube"
name3 = "kobe"

code4 = "652"
address4 = "kyouto"
name4 = "kyoto"

code5 = "651"
address5 = "hirosima"
name5 = "hiroshima"


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
test_code1 = "650"
test_code2 = "652"
print(addressData[test_code1])
print(addressData[test_code2])

# 特定のcodeのaddressを取得してみる
test_code3 = "651"
test_code4 = "652"
print(addressData[test_code3]["address"])
print(addressData[test_code4]["address"])



