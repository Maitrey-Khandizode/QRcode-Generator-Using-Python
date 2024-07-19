import qrcode as qr

img = qr.make("https://www.youtube.com/channel/UCEkRcBCiNobjyV7EUsxG-ZA/videos?app=desktop") 
img.save("SKN_INFOTECH Youtube Qrcode.png")
