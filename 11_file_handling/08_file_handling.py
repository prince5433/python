# try:
#     file = open("order.txt", "w")
#     file.write("masala chai 2 cups")
# finally:
#     file.close()

with open("order.txt", "w") as file:
    file.write("ginger tea 4 cups")
    #with k fayda ye hai ki file automatically close ho jayegi chahe error aaye ya na aaye  