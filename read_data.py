import xml.etree.ElementTree as ET
import pandas as pd
import glob

files=glob.glob(r'D:\project\capstone\ddi_dataset\DDICorpus\DDI2011\DDI2011\train\*_ddi.xml')
dataset=[]
for file in files:
    xml_file_path = file#r'D:\project\capstone\ddi_dataset\DDICorpus\DDI2011\DDI2011\train\Abarelix_ddi.xml'

    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    print(root.tag,root.attrib)
    drug1=root.attrib['origId']
    drug1_id=root.attrib['id']
    for child in root:
        print(child.tag,child.attrib,'\n')
        # drug_id=child.attrib['id']
        sentence=child.attrib['text']
        # orig_id=child.attrib['orig_id']
        if child:
            print('Child')
            print('\n')
            for sub_child in child:
                try:
                    drug2_id=sub_child.attrib['origId']
                except KeyError:
                    drug2_id=None
                try:
                    drug2=sub_child.attrib['text']
                except:
                    drug2=None
                print(sub_child.tag,sub_child.attrib)
                # if sub_child:
                dataset.append({'drug1':drug1,'drug1_id':drug1_id,'sentence':sentence,'drug2':drug2,'drug2_id':drug2})
                    # print('Sub-Child')
        else:
            dataset.append({'drug1':drug1,'drug1_id':drug1_id,'sentence':sentence,'drug2':None,'drug2_id':None})
            print('No Child')
        print('#'*20)
        # for sub_child in child:
            # print(sub_child.tag,sub_child.attrib)

print(dataset)
# print(root.findall('.//document'))
# Now you can iterate through the XML tree to access the data

for document in root.findall('./document'):
    document_id = document.get('id')
    print(f"Document ID: {document_id}")

    # Iterate through sentences
    for sentence in document.findall('.//sentence'):
        sentence_id = sentence.get('id')
        print(f"\tSentence ID: {sentence_id}")

        # Iterate through entities in the sentence
        for entity in sentence.findall('.//entity'):
            entity_id = entity.get('id')
            entity_type = entity.get('type')
            entity_text = entity.text
            print(f"\t\tEntity ID: {entity_id}, Type: {entity_type}, Text: {entity_text}")

        # Iterate through pair elements in the sentence
        for pair in sentence.findall('.//pair'):
            pair_id = pair.get('id')
            e1 = pair.get('e1')
            e2 = pair.get('e2')
            ddi = pair.get('ddi')
            print(f"\t\tPair ID: {pair_id}, E1: {e1}, E2: {e2}, DDI: {ddi}")
