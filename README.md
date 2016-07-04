This simple script converts a mind map realized in 
[Freeplane](httd://www.freeplane.org) to the simplest 
markdown structure, i.e., containing nested level sections.
Section derives from tree levels in the mind map, and their 
levels are indicated by the number of "#" in their headers, or titles.
Leaves in the map are reported as simple texts, without any #.



Use:

python freeplane2markdown.py input.mm | pandoc -o output.odt

note: convert all nodes into the mind map to plain text format:
1) unfold all the map nodes
2) select all with CTRL-A
3) press shift+alt+p (i.e., convert to text)


