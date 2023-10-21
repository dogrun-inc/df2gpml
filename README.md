# txt2gpml
Tools to generate readable XML (GPML) for [WikiPathways (https://www.wikipathways.org/)](https://www.wikipathways.org/) from nodes and interactions data described in text format.

## Environment

- Python version must be 3.9 or higher
   - `networkx`, `matplotlib` should be installed using `pip`
- `graphviz` required for `pygraphviz`.

## Input data format

- comma-separated data of pathway, nodes, edges, and anchors for each block.
- If each block is preceded by a comment describing the type, for example, a line beginning with "# nodes", it is treated as a block describing a node up to the following empty line.
- The first line of each block describes the header. The headers are converted to dictionary keys after the file is read.
- IDs must be added for nodes, interactions and anchors. Each ID is a 5- or 8-digit string with the letters a-f as its initials.

```
# pathway
name,organism

# nodes
Label, BiologicalType,ID

# interactions
start_point,end_point,BiologicalType

# anchors
interaction,position,ID
```

### pathway
- name
- organism
- layout(optional)

You can specify the layout of graphviz, such as dot or circo. Default value is circo.

### nodes
- Label
- BiologicalType
- ID

### interactions
- start_point
- end_point
- BiologicalType
- ID

Interactions describe the start node and target node, each with a node ID.
Interactions also describe the relationship between anchors and nodes.
Currently, when an interaction combines an anchor and a node, be sure to specify the anchor at the "end_point".

### anchors
- interaction
- position
- ID

Anchors describe the interaction in which the anchor is placed, its relative position in the interaction, and the ID of the anchor.

## Way to use

```
$ python txt2gpm.py -i input_file -o output_file_name.gpml
```

## To be implemented...

- Layout optimization
- Option to allow select layout program option (dot, circo and so on) 
- GroupRef attribute
- Color attribute
- LineStyle attribute
- DB binding
- Group 






