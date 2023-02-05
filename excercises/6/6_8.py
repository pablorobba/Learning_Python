pedrito = {
    "name": "pedro",
    "kind": "parrot",
    "owner":"claudio",
}
marimar = {
    "name": "marimar",
    "kind": "cat",
    "owner":"claudio",
}
china = {
    "name": "china",
    "kind": "cat",
    "owner": "pablo",
}

pets =[pedrito,marimar,china]

for pet in pets:
    print("\nThe pet name is " + pet["name"].title())
    print("\nThe pet kind is " + pet["kind"].title())
    print("\nThe pet owner is " + pet["owner"].title())