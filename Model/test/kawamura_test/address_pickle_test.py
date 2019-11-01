# -*- coding: utf-8 -*-
from collections import defaultdict
import os
import pickle

#空の辞書を宣言
address_datas = defaultdict(list)


#住所入力
title = input("タイトルは？")
address = input("住所は？")
latiude = input("緯度は？")
longitude = input("経度は？")
postal_code_frist3 = input("郵便番号上3桁は？")

#ファイルの読み込み

with open('address_data_test_pickle2',mode="rb") as read:
    address_datas = pickle.load(read)

add_data = {"title": title, "address" : address, "latiude": latiude, "longitude": longitude}

#address_datas[postal_code_frist3]["title"] = title
#address_datas[postal_code_frist3]["address"] = address
#address_datas[postal_code_frist3]["latiude"] = latiude
#address_datas[postal_code_frist3]["longitude"] = longitude

address_datas[postal_code_frist3].append(add_data)

#address_datas = address_data_update()

#データ追加処理
#def address_data_update():
#    for mykey in address_datas.keys():
#        if mykey == postal_code_frist3:
#            number = number + len(address_datas[postal_code_frist3])
#            address_datas[postal_code_frist3]["title" + str(number)] = title
#            address_datas[postal_code_frist3]["address" + str(number)] = address
#            address_datas[postal_code_frist3]["latiude" + str(number)] = latiude
#            address_datas[postal_code_frist3]["longitude" + str(number)] = longitude
#    return address_datas


#ファイルの書き込み
with open('address_data_test_pickle2',mode="wb") as update:
    pickle.dump(address_datas,update)

print(address_datas)
