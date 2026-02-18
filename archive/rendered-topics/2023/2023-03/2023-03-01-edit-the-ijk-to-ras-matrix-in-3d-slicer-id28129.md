# Edit the IJK to RAS Matrix in 3D Slicer

**Topic ID**: 28129
**Date**: 2023-03-01
**URL**: https://discourse.slicer.org/t/edit-the-ijk-to-ras-matrix-in-3d-slicer/28129

---

## Post #1 by @elrond11 (2023-03-01 22:28 UTC)

<p>I am working on registering two nrrd files. I have noticed that one of the images appears flipped in the x and y direction resulting in inaccurate registration results. The two volumes have different IJK to RAS Matrix. One of the images has a diagonal of 1,1,1, and the other has a diagonal of -1,-1,1. I was initially applying a linear transformation but that appears to transform all 3 views of the image rather then just the x and y.</p>

---

## Post #2 by @JourneyDentalLab (2023-10-12 14:29 UTC)

<p>Having the same challenge.  Did you ever find a solution?</p>

---

## Post #3 by @pieper (2023-10-12 14:32 UTC)

<p>See the information here: <a href="https://www.slicer.org/wiki/Coordinate_systems" class="inline-onebox">Coordinate systems - Slicer Wiki</a></p>

---

## Post #4 by @elrond11 (2023-10-12 14:47 UTC)

<p>I ended up reorientating the images in Python by flipping them around the access so they can match up and then loaded them into Slicer. Not the most elegant solution. It was hard too try and register the moving image to the fixed image when the orientation was so different.</p>

---
