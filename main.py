from xml.etree import ElementTree

root = ElementTree.Element("student")

first_name = ElementTree.SubElement(root, "firstName")
first_name.text = "Greg"

second_name = ElementTree.SubElement(root, "secondName")
second_name.text = "Dean"

scores = ElementTree.SubElement(root, "scores")

module1 = ElementTree.SubElement(scores, "module1")
module1.text = "100"

module2 = ElementTree.SubElement(scores, "module2")
module2.text = "90"

module3 = ElementTree.SubElement(scores, "module3")
module3.text = "80"

tree = ElementTree.ElementTree(root)
tree.write("1.xml")


"""
print(root)
print(root.tag, root.attrib)
print(root[0][0].text)


for element in root.iter("Scores"):
    print(element)



for element in root.iter("Scores"):
    score_sum=0
    for chilld in element:
        score_sum += float(chilld.text)
    print(score_sum)


tree.write("example_copy.xml")

greg = root[0]
module1=next(greg.iter("module1"))
print(module1, module1.text)
module1.text = str(int(module1.text) + 30)
tree.write("example_copy.xml")


greg = root[0]
certificate = greg[2]
certificate.set("type", "with destinction")
tree.write("example_copy.xml")


greg = root[0]
description = ElementTree.Element("description")
description.text = "Showed exellent skills during the cource"
greg.append(description)
tree.write("example_copy.xml")

greg = root[0]
description = greg.find("description")
greg.remove(description)
tree.write("example_copy.xml")





"""