# Problem with myvmtkmeshDlabeling

**Topic ID**: 22953
**Date**: 2022-04-13
**URL**: https://discourse.slicer.org/t/problem-with-myvmtkmeshdlabeling/22953

---

## Post #1 by @19lollo95 (2022-04-13 22:09 UTC)

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
