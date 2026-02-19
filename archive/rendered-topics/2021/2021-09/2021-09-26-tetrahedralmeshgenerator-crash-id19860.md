---
topic_id: 19860
title: "Tetrahedralmeshgenerator Crash"
date: 2021-09-26
url: https://discourse.slicer.org/t/19860
---

# TetrahedralMeshGenerator crash

**Topic ID**: 19860
**Date**: 2021-09-26
**URL**: https://discourse.slicer.org/t/tetrahedralmeshgenerator-crash/19860

---

## Post #1 by @Saima (2021-09-26 04:33 UTC)

<p>Hi Andras,<br>
Its strange, it didnt run at all and the slicer crashes. ’</p>
<p>Here is what it says:</p>
<p>Switch to module:  “Welcome”<br>
Switch to module:  “TetrahedralMeshGenerator”<br>
QXcbConnection: XCB error: 3 (BadWindow), sequence: 3142, resource id: 39972228, major code: 40 (TranslateCoords), minor code: 0<br>
Processing started<br>
error: [/home/saima/Downloads/Slicer-4.11.20200930-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.</p>
<p>regards,<br>
Saima Safdar</p>

---

## Post #2 by @lassoan (2021-09-26 04:47 UTC)

<p>Probably the issue is that you’ve put some executable or Python files or shared libraries in one of your module folders. Slicer will attempt to use them as Slicer modules: run them with a special argument list (to make the module provide basic information about itself), which makes those executables or Slicer to crash.</p>
<p>The solution is to keep only Slicer module files in those folders that you added to your “Additional module paths” (in menu: Edit / Application settings / Modules).</p>

---

## Post #3 by @Saima (2021-09-26 04:48 UTC)

<p>Hi Andras,<br>
I used the built version of slicer and it is running fine. I do not understand what the problem is with the other downloaded slicer versions. but the one which I build is working fine.</p>
<p>witch to module:  “Welcome”<br>
Switch to module:  “TetrahedralMeshGenerator”<br>
Processing started<br>
Info    : Reading ‘/home/saima/Documents/Model_1_Segment_1.stl’…<br>
Info    : 488726 facets in solid 0 3D Slicer output. SPACE=LPS<br>
Info    : Done reading ‘/home/saima/Documents/Model_1_Segment_1.stl’<br>
Info    : Classifying surfaces (angle: 40)…<br>
Info    : Splitting triangulations to make them parametrizable:<br>
Info    :  - Level 0 partition with 488726 triangles split in 2 parts because too many triangles (488726 vs. 250000)<br>
Info    :  - Level 1 partition with 244362 triangles split in 2 parts because parametrized triangles are too small (2.76429e-09)<br>
Info    :  - Level 2 partition with 122360 triangles split in 2 parts because parametrized triangles are too small (3.03033e-09)<br>
Info    :  - Level 3 partition with 61020 triangles split in 2 parts because parametrized triangles are too small (8.86267e-09)<br>
Info    : Found 5 model surfaces<br>
Info    : Found 9 model curves<br>
Info    : Done classifying surfaces (Wall 30.1653s, CPU 32.3311s)<br>
Info    : Creating geometry of discrete curves…<br>
Info    : Done creating geometry of discrete curves (Wall 0.0113672s, CPU 0.011578s)<br>
Info    : Creating geometry of discrete surfaces…<br>
Info    : Done creating geometry of discrete surfaces (Wall 10.898s, CPU 12.2354s)<br>
Info    : Meshing 1D…<br>
Info    : [  0%] Meshing curve 11 (Discrete curve)<br>
Info    : [ 20%] Meshing curve 12 (Discrete curve)<br>
Info    : [ 30%] Meshing curve 13 (Discrete curve)<br>
Info    : [ 40%] Meshing curve 14 (Discrete curve)<br>
Info    : [ 50%] Meshing curve 15 (Discrete curve)<br>
Info    : [ 60%] Meshing curve 16 (Discrete curve)<br>
Info    : [ 70%] Meshing curve 17 (Discrete curve)<br>
Info    : [ 80%] Meshing curve 18 (Discrete curve)<br>
Info    : [ 90%] Meshing curve 19 (Discrete curve)<br>
Info    : Done meshing 1D (Wall 0.133766s, CPU 0.133808s)<br>
Info    : Meshing 2D…<br>
Info    : [  0%] Meshing surface 2 (Discrete surface, Frontal-Delaunay)<br>
Info    : [ 20%] Meshing surface 3 (Discrete surface, Frontal-Delaunay)<br>
Info    : [ 40%] Meshing surface 4 (Discrete surface, Frontal-Delaunay)<br>
Info    : [ 60%] Meshing surface 5 (Discrete surface, Frontal-Delaunay)<br>
Info    : [ 80%] Meshing surface 6 (Discrete surface, Frontal-Delaunay)<br>
Info    : Done meshing 2D (Wall 31.7743s, CPU 31.3752s)<br>
Info    : 8067 nodes 16395 elements<br>
Info    : Writing ‘/home/saima/Slicer-4.11.0-2020-02-25-linux-amd64/TetrahedralMeshGenerator/TetrahedralMeshGenerator/brainmask_auto.msh’…<br>
2<br>
Info    : Done writing ‘/home/saima/Slicer-4.11.0-2020-02-25-linux-amd64/TetrahedralMeshGenerator/TetrahedralMeshGenerator/brainmask_auto.msh’<br>
ReadDataInternal ((unknown)): File /home/saima/Slicer-4.11.0-2020-02-25-linux-amd64/TetrahedralMeshGenerator/TetrahedralMeshGenerator/vMesh.vtk does not contain coordinate system information. Assuming LPS.</p>
<p>“Model” Reader has successfully read the file “/home/saima/Slicer-4.11.0-2020-02-25-linux-amd64/TetrahedralMeshGenerator/TetrahedralMeshGenerator/vMesh.vtk” “[0.04s]”<br>
Failed to compute results: Could not deduce file format from extension ‘’.<br>
Traceback (most recent call last):<br>
File “/home/saima/Slicer-4.11.0-2020-02-25-linux-amd64/TetrahedralMeshGenerator/TetrahedralMeshGenerator/TetrahedralMeshGenerator.py”, line 158, in onApplyButton<br>
self.logic.run(self.ui.inputFile.currentPath, self.ui.outputSelector.currentNode(),self.ui.outputFile.currentPath, self.ui.meshType.value)<br>
File “/home/saima/Slicer-4.11.0-2020-02-25-linux-amd64/TetrahedralMeshGenerator/TetrahedralMeshGenerator/TetrahedralMeshGenerator.py”, line 287, in run<br>
meshio.write(outputModelFile,mesh)<br>
File “/home/saima/Slicer-SuperBuild-Debug/python-install/lib/python3.6/site-packages/meshio/_helpers.py”, line 120, in write<br>
file_format = _filetype_from_path(path)<br>
File “/home/saima/Slicer-SuperBuild-Debug/python-install/lib/python3.6/site-packages/meshio/_helpers.py”, line 34, in _filetype_from_path<br>
raise ReadError(f"Could not deduce file format from extension ‘{ext}’.")<br>
meshio._exceptions.ReadError: Could not deduce file format from extension ‘’.</p>

---

## Post #4 by @Saima (2021-09-26 04:49 UTC)

<p>Hi Andras,<br>
I will try this and let you know.</p>
<p>regards,<br>
Saima Safdar</p>

---
