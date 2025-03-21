info = {
"id": "0001",
"type": "donut",
"name": "Cake",
"image":
{
"url": "images/0001.jpg",
"width": 200,
"height": 200
},
"thumbnail":
{
"url": "images/thumbnails/0001.jpg",
"width": 32,
"height": 32
}
}

# hard and stupid way

# print("ID: ",info["id"])
# print("TYPE: ", info["type"])
# print("NAME: ", info["name"])
# print("IMAGE URL :", info["image"]["url"])
# print("IMAGE WIDTH :", info["image"]["width"])
# print("IMAGE HEIGHT :", info["image"]["height"])
# print("THUMBNAIL URL :", info["thumbnail"]["url"])


# better way
for key, value in info.items():
    if isinstance(value,str):
        print(key.ljust(20), ":", value)
    elif isinstance(value,dict):
        for skey,svalue in value.items():
            fkey = key + "." + skey
            print(fkey.ljust(20),":", svalue)