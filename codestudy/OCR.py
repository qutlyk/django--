#作者       84202   
#创建时间   2018/9/2  23:24   当前系统时间
#文件       OCR
# IDE       PyCharm

   #数字验证码识别


from PIL import Image
from PIL import ImageEnhance
import pytesseract
im=Image.open("C:\\Users\\84202\\Desktop\\1.jpg")
im=im.convert('L')
im.show()
im=ImageEnhance.Contrast(im)
im=im.enhance(3)
im.show()
print(pytesseract.image_to_string(im))