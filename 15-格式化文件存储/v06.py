import xml.etree.ElementTree as et

#在内存中创建一个空的文档


etree = et.ElementTree()

e = et.Element('Student')

etree._setroot(e)

e_name = et.SubElement(e, 'Name')
e_name.text = "hahahah"


etree.write('v06.xml')
