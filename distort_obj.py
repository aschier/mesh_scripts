#!/usr/bin/env python
import sys, random

vertices = []
faces = []

with open(sys.argv[1], "r") as file:
    lines = file.read().split("\n")
    outputobj = ""
    for line in lines:
        if line.startswith("v"):
            parts = line.split(" ")
            vertices.append([float(x) for x in parts[1:]])
        if line.startswith("f"):
            parts = line.split(" ")
            faces.append([int(x) for x in parts[1:]])
    for face in faces:
        for idx in face:
            vertex = [x+random.random()/50.0 for x in vertices[idx-1]]
            outputobj += "v " + " ".join([str(x) for x in vertex]) + "\n"
    for i in xrange(len(faces)):
        outputobj += "f {0:d} {1:d} {2:d}".format(3*i+1, 3*i+1+1, 3*i+2+1) + "\n"
    with open(sys.argv[2], "w") as outfile:
        outfile.write(outputobj)
