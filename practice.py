from unicodedata import name
import xml.etree.ElementTree as ET
mytree = ET.parse('sample.xml')

myroot = mytree.getroot()

# print(mytree)
# print(myroot)

for x in myroot.findall('book'):
    name = x.find('title').text
    genre = x.find('genre').text
    price = x.find('price').text

    print(name,'-', genre,'-', price)