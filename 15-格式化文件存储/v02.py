import xml.etree.ElementTree

root = xml.etree.ElementTree.parse("student.xml")
print("利用getiterator访问：")
nodes = root.getiterator()
for node in nodes:
    print("{0}--{1}".format(node.tag, node.text))



print("利用find和findall方法：")
ele_teacher = root.find("Teacher")
print(type(ele_teacher))
print("{0}--{1}".format(ele_teacher.tag, ele_teacher.text))


ele_stus = root.findall("Student")
print(type(ele_stus))
for ele in ele_stus:
    print("{0}--{1}".format(ele.tag, ele.text))
    for sub in ele.getiterator():
        if sub.tag =="Name":
            if "Other" in sub.attrib.keys():
                print(sub.attrib['Other'])