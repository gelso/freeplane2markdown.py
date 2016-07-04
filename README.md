This freeplane2markdown.py script converts a mind map realized in 
[Freeplane](httd://www.freeplane.org) to the simplest 
markdown structure, containing nested sections.
These sections reflect tree levels in the mind map, carrying the *right number of 
"#" in their headers or titles* (all but the last, leaf level text).



Use:

`$ python freeplane2markdown.py input.mm`

or, if you want

`$ python freeplane2markdown.py input.mm | pandoc -o output.odt`

note: prior to run the script, please convert all the mind map content 
to plain text:

- unfold all the map nodes

- select all using CTRL-A

- convert all the selection to text using SHIFT+ALT+P




