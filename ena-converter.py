#!/usr/bin/python

import sys, getopt
import xmlschema
import xml.etree.ElementTree as et 
import json
import pandas as pd
import subprocess
import numpy as np

# new function (rewritten)
# print("Started Reading JSON file")


def append_table_protocol(element, json_rows):

    for parameter in element:

        p=parameter.get('parameterName') if parameter.get('parameterName') is not None else None
#         print(p)
        term_name = p.get('annotationValue') if p.get('annotationValue') is not None else None
        print('name is: '+ term_name )
        term_source = p.get('termSource') if p.get('termSource')  is not None else None
        print( term_source)
        term_accession = p.get('termAccession') if p.get('termAccession')  is not None else None
        print( term_accession)                          
        index_value= p.get('comments')[0].get("value")
        json_rows.append( [file_id,
                           arc_id, 
                           subsection_id,
                           input_id, 
                           input_name,

                           output_id, 
                           output_name,
                           derived_from,
                           term_type,
                           term_name, 
                           term_source, 
                           term_accession, 
                           index_value, 
                           value])
#         print('index value is: '+ term_value)
        


def append_table_assays(element, json_rows, option= 1):
    
    for parameter in element:

        c= parameter.get("category")
        p=c.get('parameterName') if c.get('parameterName') is not None else None
#         print(p)
        value = parameter.get('value') if parameter.get('value') is not None else None
        term_name = p.get('annotationValue') if p.get('annotationValue') is not None else None
#         print('name is: '+ term_name )
        term_source = p.get('termSource') if (p.get('termSource') ) is not None else None
#         print( term_source)
        term_accession = p.get('termAccession') if (p.get('termAccession') ) is not None else None
#         print( term_accession)
        term_type = "parameter"
        index_value= p.get('comments')[0].get("value")
        
        json_rows.append( [file_id, 
                           arc_id, 
                           subsection_id,
                           input_id, 
                           input_name,

                           output_id, 
                           output_name,
                           derived_from,
                           term_type,
                           term_name, 
                           term_source, 
                           term_accession, 
                           index_value, 
                           value])
#         print('index value is: '+ term_value)
        
def append_c_input(element, json_rows):
    
    for parameter in element:

        b = parameter.get("category")
        factor = b.get("characteristicType") if b.get("characteristicType") is not None else None
#         print(p)
        value = parameter.get('value') if parameter.get('value') is not None else None
        term_name = factor.get('annotationValue') if factor.get('annotationValue') is not None else None
#         print('name is: '+ term_name )
        term_source = factor.get('termSource') if (factor.get('termSource') ) is not None else None
#         print( term_source)
        term_accession = factor.get('termAccession') if (factor.get('termAccession') ) is not None else None
#         print( term_accession)
        term_type = "parameter"
        index_value= factor.get('comments')[0].get("value")
        json_rows.append( [file_id, 
                           arc_id, 
                           subsection_id,
                           input_id, 
                           input_name,

                           output_id, 
                           output_name,
                           derived_from,
                           term_type,
                           term_name, 
                           term_source, 
                           term_accession, 
                           index_value, 
                           value])
#         print('index value is: '+ term_value)

def append_input(element, json_rows):
    
    for parameter in element:

        b = parameter.get("category")
        factor = b.get("factorType") if b.get("factorType") is not None else None
#         print(p)

        value = parameter.get('value') if parameter.get('value') is not None else None
        term_name = factor.get('annotationValue') if factor.get('annotationValue') is not None else None
#         print('name is: '+ term_name )
        term_source = factor.get('termSource') if (factor.get('termSource') ) is not None else None
#         print( term_source)
        term_accession = factor.get('termAccession') if (factor.get('termAccession') ) is not None else None
#         print( term_accession)
        term_type = "factor"
        index_value= factor.get('comments')[0].get("value")
        json_rows.append( [file_id, 
                           arc_id, 
                           subsection_id,
                           input_id, 
                           input_name,

                           output_id, 
                           output_name,
                           derived_from,
                           term_type,
                           term_name, 
                           term_source, 
                           term_accession, 
                           index_value, 
                           value])
#         print('index value is: '+ term_value)

def append_output(element, json_rows):
    
    for parameter in element:
        
        b = parameter.get("category")
        factor = b.get("factorType") if b.get("factorType") is not None else None
#         print(p)

        value = parameter.get('value') if parameter.get('value') is not None else None
        term_name = factor.get('annotationValue') if factor.get('annotationValue') is not None else None
#         print('name is: '+ term_name )
        term_source = factor.get('termSource') if (factor.get('termSource') ) is not None else None
#         print( term_source)
        term_accession = factor.get('termAccession') if (factor.get('termAccession') ) is not None else None
#         print( term_accession)
        term_type = 'factor'
        index_value= factor.get('comments')[0].get("value")
        json_rows.append( [file_id, 
                           arc_id, 
                           subsection_id,
                           input_id, 
                           input_name,

                           output_id, 
                           output_name,
                           derived_from,
                           term_type,
                           term_name, 
                           term_source, 
                           term_accession, 
                           index_value, 
                           value])
#         print('index value is: '+ term_value)
#         print('index value is: '+ term_value)
# todo factorValues, derived from

def init_none():
    global input_id 
    global input_name 
    global output_id
    global output_name 
    global derived_from 
    global value 
    global index_value
    global term_type
    global term_name
    global term_source 
    global term_accession 
    input_id = None
    input_name = None
    output_id = None
    output_name = None
    derived_from = None
    value = None
    index_value = None
    term_type = None
    term_name = None
    term_source = None
    term_accession = None
    
def write_smaple_xml(xml_input):
    input_ = xml_input[xml_input["subsection_id"].str.match(r'1SPL01_plants_')==True ]
    sample= input_
    input_list = sample[sample["input_name"].notna()]
    output_list = sample[sample["output_name"].notna()]

    a = et.Element('SAMPLE_SET')
    for index1,input_name in enumerate(input_list["input_name"].unique()):
        one_sample = sample[sample['input_name'] == input_name]
        for index2, tags in enumerate(one_sample):
            b = et.SubElement(a, 'SAMPLE')

            b.attrib = {'alias': input_name , 'center_name':''}
            c = et.SubElement(b, 'TITLE')
            c.text = one_sample[one_sample['term_name']== 'Organism']['value'].to_string(header=False, index=False)

            d = et.SubElement(b, 'SAMPLE_NAME')
            #d.text = input_name

            e = et.SubElement(d, 'TAXON_ID')
            e.text = '110664'
            f = et.SubElement(d, 'SCIENTIFIC_NAME')
            f.text = c.text = one_sample[one_sample['term_name']== 'Organism']['value'].to_string(header=False, index=False)

            g = et.SubElement(d, 'COMMON_NAME')
            g.text = input_name

            h = et.SubElement(b, 'SAMPLE_ATTRIBUTES')
            for index3, row in one_sample.iterrows():
                m = et.SubElement(h,'SAMPLE_ATTRIBUTE' )
                j = et.SubElement(m, 'TAG')
                j.text = str(row['term_name'])

                k = et.SubElement(m, 'VALUE')
                k.text = str(row['value']) 


    tree = et.ElementTree(a)
    et.indent(tree, space=" \n", level=0)
    et.dump(a)
    tree.write("SAMPLE.xml", encoding="utf-8")
        

        
        

    
    
    


# new function

def convert_json(arc_json_file, mapping_file):
    with open(arc_json_file, "r") as read_file:
#     print("Converting JSON encoded data into Python dictionary")
        arc_json = json.load(read_file)
    
    

    

    global file_id
    global arc_id
    global subsection_id
    global input_id 
    global input_name 
    global output_id
    global output_name 
    global derived_from 
    global value 
    global index_value
    global term_type
    global term_name
    global term_source 
    global term_accessio
    json_table= []
    json_cols = ["file_id", 
                 "arc_id" , 
                 "subsection_id", 
                 "input_id", 
                 "input_name", 

                 "output_id", 
                 "output_name",
                 "derived_from",
                 "term_type",
                 "term_name", 
                 "term_source", 
                 "term_accession", 
                 "index_value", 
                 "value", ]
    json_rows = []
    init_none()
    file_id = arc_json.get("identifier")
    section = "studies"
    studies = arc_json.get("studies")
	
    arc_id = studies[0].get("identifier")
    processSequences = arc_json.get("studies")[0].get('assays')[0].get("processSequence")

    for process_seq in processSequences:

        subsection_id = process_seq.get("name")
        print(subsection_id)

        parameter_values = process_seq.get("parameterValues")
        append_table_assays(parameter_values, json_rows)
        init_none() 
        input_section = process_seq.get("inputs")
        if input_section != None:
    #     print(input_section)
            for i,input_ in enumerate(input_section):
                input_name = input_.get("name")
                input_id = i

                derived_from = input_.get("derivesFrom")[0].get("name") if input_.get("derivesFrom") is not None else None
                print(input_name + " derivesFrom is ", derived_from)
                characteristics = input_.get("characteristics") 
                if characteristics != None:
                    append_c_input(characteristics,json_rows)
                factorvalues = input_.get("factorValues") 
                if factorvalues != None:
                        append_input(factorvalues,json_rows)



            
        output_section = process_seq.get("outputs")

    #     print(output_section)
        for i, output_ in enumerate(output_section):
            output_name = output_.get("name")
            output_id = i
            derived_from = output_.get("derivesFrom")[0].get("name") if output_.get("derivesFrom") is not None else None
            print(output_name + " and derived from is ", derived_from)

            term_type = output_.get('type') if output_.get('type') is not None else None

            factorvalues = output_.get("factorValues") 
            if factorvalues != None:
                append_output(factorvalues,json_rows)
            else:
                json_rows.append( [file_id, 
                               arc_id, 
                               subsection_id,
                               input_id, 
                               input_name,

                               output_id, 
                               output_name,
                               derived_from,
                                   term_type,
                               term_name, 
                               term_source, 
                               term_accession, 
                               index_value, 
                               value])



    json_table = pd.DataFrame(json_rows, columns= json_cols)
    mapping = pd.read_excel(mapping_file)
    term_id = mapping.iloc[:,2]
    mapping.iloc[:,3] = term_id.map( lambda x: "http://purl.obolibrary.org/obo/{}".format( str(x).replace(":", "_") )  )

    
    json_table["ena_id"] = json_table["term_name"]
    a = json_table.loc[:, "ena_id"]
    # a = json_table.loc[:, "term_accession"]
    term_mapping = mapping.iloc[:,3]
    for i, term in enumerate(term_mapping):
         cond = json_table["term_accession"] == term
    #     print(term)
    #     print(filter_)
         a.mask(cond , mapping.loc[:, "Field Name"][i], inplace= True)
    json_table.to_csv('json_table_new.csv')
    
    
    a = et.Element('PROJECT_SET')
    for i,project in enumerate(arc_json.get("studies")):
        b = et.SubElement(a, 'PROJECT')

        b.attrib = {'alias': project.get('identifier')}
        c = et.SubElement(b, 'TITLE')
        c.text = project.get('title')
        d = et.SubElement(b, 'DESCRIPTION')
        d.text = str(arc_json.get("publications"))
        f = et.SubElement(b, "SUBMISSION_PROJECT")
        g = et.SubElement(f, "SEQUENCING_PROJECT")
    tree = et.ElementTree(a)
    et.indent(tree, space=" \n", level=0)

    tree.write("STUDY.xml", encoding="utf-8")

    # sample xml
    xml_input = pd.read_csv("json_table_new.csv")
    write_smaple_xml(xml_input)
        
            

        
        

    
    



def main(argv):
    arc_json_file = 'inv.json'
    mapping_file = 'mapping_ERC000037.xlsx'
    try:
        opts, args = getopt.getopt(argv,"ha:m:",["afile=","mfile="])
    except getopt.GetoptError:
        print('ena-c.py -a <arc_json_file> -m <mapping_file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('ena-c.py -a <arc_json_file> -m <mapping_file>')
            sys.exit()
        elif opt in ("-a", "--afile"):
            arc_json_file = arg
        elif opt in ("-m", "--mfile"):
            mapping_file = arg
    print('arc_json file is ', arc_json_file)
    print('mapping file is ', mapping_file)
    convert_json(arc_json_file, mapping_file)

    
    
if __name__ == "__main__":
   main(sys.argv[1:])