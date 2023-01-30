phone_1 = "motorola"
phone_2 = "samsung"
phone_3 = "nokia"
phone_4 = "sony"
phone_5 = "google"


print("is phone equal to 'motorola', i predict True")
print(phone_1 == "motorola")

print("is phone equal to 'i phone', i predict False")
print(phone_1 == "i phone")


print("is phone equal to 'samsung', i predict True")
print(phone_2.lower() == "samsung")

print("is phone equal to 'facebook', i predict False")
print(phone_2.lower() == "facebook")


print("is phone equal to 'nokia', i predict True")
print("nokia" in phone_3)
print("is phone equal to 'ericson', i predict False")
print("ericson" in phone_3)

print("is phone equal to 'sony', i predict True")
print(7>6 and 5>=5)

print("is phone equal to 'huawei', i predict False")
print(4<3 or 4<=3)


print("is phone equal to 'google', i predict True")
print("blue" not in phone_5 )

print("is phone equal to 'blu', i predict False")
print("google" not in phone_5)