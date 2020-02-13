import sys, random
if not len(sys.argv) == 3:
    print("randomize the vertex order of faces in an OFF mesh to randomize the normals.")
    print("Syntax: %s input.off output.off"%sys.argv[0])
    sys.exit()
with open(sys.argv[1], "r") as inputfile, open(sys.argv[2], "w") as outputfile:
    for line in inputfile.read().replace("\r\n", "\n").split("\n"):
        if line.startswith("3 "):
            parts = line.split(" ")
            vertices = parts[1:]
            random.shuffle(vertices)
            outputfile.write(" ".join([parts[0]] + vertices)+"\n")
        else:
            outputfile.write(line + "\n")


