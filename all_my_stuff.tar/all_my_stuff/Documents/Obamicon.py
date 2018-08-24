from PIL import Image
#DARK_BLUE=(0,51,76)
#RED=(217,26,33)
#LIGHT_BLUE=(112,150,158)
#YELLOW=(252,227,166)
DARK_RED=(128,16,16)
RED=(195,28,28)
LIGHT_RED=(235,65,65)
REALLY_LIGHT_RED=(250,145,145)
im= Image.open("woman_portrait.jpg")
def get_pixel_data():
	pixel_list=list(im.getdata())
#return pixel_list
#print(pixel_list)
	num_pixels=len(pixel_list)-1
	for i in range(0,len(pixel_list)):
		intensity=pixel_list[i][0]+pixel_list[i][1]+pixel_list[i][2]
		if intensity<182:
			#im.putpixel((0,51,76))
			pixel_list[i]=DARK_RED
		elif intensity<364 and intensity>182:
			pixel_list[i]=RED
			#im.putpixel((217,26,33))
		elif intensity<546 and intensity>364:
			pixel_list[i]=LIGHT_RED
			#im.putpixel((112,150,158))
		else:
			pixel_list[i]=REALLY_LIGHT_RED
			#im.putpixel((252,227,166))
	im.putdata(pixel_list)
	im.save("edited_portrait.jpg")
	
	
	
get_pixel_data()
im=Image.open("edited_portrait.jpg")
im.show("edited_portrait.jpg")