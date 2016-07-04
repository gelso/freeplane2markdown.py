This simple script converts a mind map realized in 
[Freeplane](httd://www.freeplane.org) to the simplest 
markdown structure, containing nested sections.
These sections reflect tree levels in the mind map, carrying the right number of 
"#" in their headers or titles (all but the last, leaf level text).



Use:


$ python freeplane2markdown.py input.mm | pandoc -o output.odt

note: prior to run the script, please convert all the mind map content 
to plain text:

1) unfold all the map nodes
2) select all using CTRL-A
3) convert all the selection to text using SHIFT+ALT+P

python freeplane2markdown.py input.mm | pandoc -o output.odt

note: convert all nodes into the mind map to plain text format:
1) unfold all the map nodes
2) select all with CTRL-A
3) press shift+alt+p (i.e., convert to text)



