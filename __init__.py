#
#
# from PIL import Image
# import sys
# import os
#
# path = sys.argv[1]
# images = os.listdir(path)
# # size = 128,128
# for im in images:
#   image_path = path + os.sep + im
#   #print("image path: " + image_path)
#   try:
#     new_image = Image.open(image_path)
#     print(new_image.size)
#     print(new_image.format)
#     filename = image_path.split(os.sep)[-1].split(".")[0]
#   #  print("filename: " + filename )
#   #   new_image.rotate(270).show()
#     newfilename = "/Users/zhangmengfeifei/Desktop/Personal/" + filename
#     m = new_image.convert("RGB").resize((50, 100))
#     m.save(newfilename,"JPEG")
#     # print(new_image.size)
#     # print(new_image.format)
#     # print("newfilename: " + newfilename)
#     # new_image.save((newfilename), "JPEG")
# #    break
#   except:
#     continue
# print("Finished!")

a = ''
print(type(a))