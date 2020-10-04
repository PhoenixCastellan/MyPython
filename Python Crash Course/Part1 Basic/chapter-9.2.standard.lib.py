from collections import OrderedDict

favorite_fruits = OrderedDict()
favorite_fruits['lvrihui'] = "boluo"
favorite_fruits["lvhongfang"] = "xiangjiao"
favorite_fruits["lvshuen"] = "putao"
favorite_fruits["lvshuai"] = "putao"

for key, value in favorite_fruits.items():
    print(key.title() + "'s favorite fruit is " + value)
