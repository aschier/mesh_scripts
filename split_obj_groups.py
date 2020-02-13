import sys
import os.path
import random

# Quick & dirty script to split an obj file with groups into multiple files.
# Make sure the groups have filename compatible names, and if your file
# does not look like the example below, use a proper tool.

# The script assumes, that the faces reference texture indices and normal indices and that there are the same number of
# vertex normals / vertex texture coordinates as the number of vertices. Otherwise it will not work.

# working example:
# g somegroup
# v 1 1 1
# v 2 2 2
# v 3 3 3
# vn 1 1 1
# vn 2 2 2
# vn 3 3 3
# vt 1 1 1
# vt 2 2 2
# vt 3 3 3
# f 1/1/1 2/2/2 3/3/3

lines = open(sys.argv[1], "r").read().replace("\r", "").split("\n")

objname = "" # name of the group / file to write
obj = "" # data for the new file
offset = 0 # vertex index offset
new_offset = 0 # vertex index offset in the next group
for line in lines:
    if line.startswith("v "):
		# update the new offset
        new_offset += 1
    if line.startswith("g "):
        offset = new_offset
        if objname:
            filename = objname
            while os.path.exists(filename + ".obj"):
                print ("duplicate filename:" + filename)
                filename = objname + "_" + "".join([random.choice("abcdefghijklmnopqrstuvwxyz") for i in range(8)])
                print("new filename: " + filename)
            with open(filename + ".obj", "w") as file:
                file.write(obj)
            obj = ""
        objname = line[2:]
    elif line.startswith("f "):
        parts = line.split(" ")
		# decrement the vertex/vertex normal/vertex uv indices by the current offset
        parts[1:] = map(lambda x: "/".join(map(lambda y: str(int(y)-offset),x.split("/"))), parts[1:])
        obj += " ".join(parts) + "\n"
    else:
        obj += line + "\n"
# write the last object, which is not followed by a new group
with open(objname+".obj", "w") as file:
    file.write(obj)
