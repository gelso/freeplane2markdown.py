# -*- coding: utf-8 -*-
"""
Created on Sun May 15 11:23:51 2016

@author: Andrea Caprera


This simple script converts the structure of a freeplane .mm tree into a
markdown structure: different "level" branches in a mindmap are read, and then translated into a
"markdown-style" text, having corresponding levels as headers with the correct number of #.
Leaves are copied, then, as simple text.

This allows to quickly convert the structure of a mind map, used to organize ideas for an article or
a document (along with the chapter/paragraph/text levels), into a skeleton of a markdown document,
ready for further management or for format conversion.

"""


from xml.etree import ElementTree as ET
import sys

input_file = sys.argv[1]

def recursively_parse(elem, level):
    level +=1 # level is a local variable which value follows recursions

    for sub in elem:
#        if "LOCALIZED_TEXT" in sub.attrib:
#            recursively_parse(sub, level)
        
        if sub.tag == 'node': # I'm interested only in elements named 'node'
            
            # check if this node is a leaf (a simple text) or a branch with chilfren branches (a header)
            
            if not list(sub): # it is empty, so sub is a leaf:
                print(sub.attrib["TEXT"].encode("utf-8") + "\n")
            else: # sub is a header:
                if "TEXT" in sub.attrib:
                    print(level * "#" + " " + sub.attrib["TEXT"].encode("utf-8") + "\n")
            recursively_parse(sub, level)



# getting the first elem in the tree (the root)
elem = ET.parse(input_file).getroot()

# go!
recursively_parse(elem, level=0)
