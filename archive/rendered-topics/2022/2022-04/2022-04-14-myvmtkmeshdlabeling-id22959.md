---
topic_id: 22959
title: "Myvmtkmeshdlabeling"
date: 2022-04-14
url: https://discourse.slicer.org/t/22959
---

# myvmtkmeshDlabeling

**Topic ID**: 22959
**Date**: 2022-04-14
**URL**: https://discourse.slicer.org/t/myvmtkmeshdlabeling/22959

---

## Post #1 by @19lollo95 (2022-04-14 09:58 UTC)

<p>I’m working with macOS operating system on mac with M1 processor.<br>
I’m having problems in order to obtain a meshDxx.vtu (starting from 2 files meshR.vtu and Dxx.mhd) which associates the values of the tensor built in Dxx.mhd to the meshR.<br>
Following a guide given to me, I ran the following command:<br>
<code>vmtk myvmtkmeshDlabeling -ifile meshR.vtu -diffusionmapfile Dxx.mhd -diffusionarray "Dxx_labels" -ofile meshDxx.vtu</code></p>
<p>I get the following output:</p>
<pre><code class="lang-auto">Executing myvmtkmeshDlabeling -ifile meshR.vtu -diffusionmapfile Dxx.mhd -diffusionarray Dxx_labels -ofile meshDxx.vtu

Automatic piping myvmtkmeshDlabeling
Parsing options myvmtkmeshDlabeling
    MeshInInputFileName = meshR.vtu
    DiffusionMapInputFileName = Dxx.mhd
    DiffusionArrayName = Dxx_labels
    MeshOutOutputFileName = meshDxx.vtu
Explicit piping myvmtkmeshDlabeling
Input myvmtkmeshDlabeling members:
    Id = 0
    Disabled = 0
    MeshIn = None
    MeshInInputFileName = meshR.vtu
    DiffusionMap = None
    DiffusionMapInputFileName = Dxx.mhd
    DiffusionArrayName = Dxx_labels
    Correction = 0
    Radius = 9
    OnlyNegatives = 0
    MeshOutOutputFileName = meshDxx.vtu
Reading VTK XML mesh file.
Spacing 0.449219 0.449219 0.900000
Origin -105.647736 -123.984390 -68.281136
Dimensions 448 512 176
Executing myvmtkmeshDlabeling ...
Creating points location array
Assigning diffusion values to tethraedrical mesh

</code></pre>
<p>It seems to be processing but I believe there is some problem as it doesn’t seem to have an end and I cannot obtain this file. How can I solve this problem?</p>

---

## Post #2 by @ramtingh (2022-04-14 15:21 UTC)

<p><code>myvmtkmeshDlabeling</code> isn’t a script shipped with vmtk, so not quite sure what you are attempting to do or what the problem could be.</p>

---

## Post #3 by @19lollo95 (2022-04-14 17:51 UTC)

<p>I know that it is a vmtk command which takes in input a refined mesh (meshR.vtu), a component of the DTI and the name of the array to be associated with the mesh cells, and returns a new mesh that has, associated in each cell, the value of the chosen component of the diffusion tensor.In the guide I am using it is indicated that it is an alternative vmtk command to the python script label_D.py</p>

---
