# Exporting Volume Model and HU for FEA (issue with vtk export)

**Topic ID**: 28865
**Date**: 2023-04-12
**URL**: https://discourse.slicer.org/t/exporting-volume-model-and-hu-for-fea-issue-with-vtk-export/28865

---

## Post #1 by @evaherbst (2023-04-12 13:28 UTC)

<p>Hi all,</p>
<p>I want to export a volumetric model along with HU values for FEA analysis.</p>
<p>Based on several very helpful forum posts, I was able to create a volumetric mesh (single material) with the SegmentMesher module. I then used Probe Volume with Model to get a map of the densities across the model.</p>
<p>I have 2 questions.</p>
<p><strong>1) export of volumetric mesh (single material)</strong><br>
Unfortunately my FEA program of choice (Artisynth) is unable to read the vtk FE mesh file. I get an error that it is of type “Polydata” and unable to read that (vtk ascii should be supported).</p>
<p>To double check that it isn’t an error with the FE program, I also tried using meshio in the Slicer Python console to try to read the vtk mesh and convert to .inp (which Artisynth can also read):</p>
<p><em>import meshio</em><br>
<em>mesh = meshio.read(“T:/Slicer_Tests/Material Mapping/Test_single_material_skull.vtk”)</em><br>
<em>meshio.write(“T:/Slicer_Tests/Material Mapping/test2.inp”, mesh)</em></p>
<p>However, when trying to read the .vtk file, I also get the error:<br>
<em>Only VTK ‘UNSTRUCTURED_GRID’, ‘STRUCTURED_POINTS’, ‘STRUCTURED_GRID’, ‘RECTILINEAR_GRID’ supported (not POLYDATA).</em></p>
<p>And when I open the .vtk file itself it says “DATASET POLYDATA”.</p>
<p>My question is whether this is a bug in the .vtk export (I did select “unstructured grid”, not “polydata”).</p>
<p>I also get the error <em>vtkMRMLModelDisplayNode (00000218420FB2D0): Can not use color node scalar range since model display node does not have a color node.</em> during the export, and it looks like in the type of export, it quickly flashes to “polydata” instead of “unstructured grid” before the pop up window closes.</p>
<p><strong>2) mapping material properties</strong><br>
Related to question 1, when I export the output from Probe Volume with Model, I get a polydata .vtk file. Looking at the file it is unclear to me how it is structured, e.g. where the coordinates are and where the HU values are.</p>
<p>Thank you very much!<br>
Eva</p>

---

## Post #2 by @evaherbst (2023-04-19 11:28 UTC)

<p>Hello again,</p>
<p>I managed to fix the vtk export problem by using File&gt;Save Data instead of right clicking in the hierarchy and exporting the data. This enabled me to save as vtk unstructured binary, which can be read by meshio to create an .inp file. My FE software should also be able to read vtk unstructured ascii but I was not able to export as ascii.</p>
<p>To export a list of density values, I used Probe Volume with Model on the tetra mesh and the following code.</p>
<blockquote>
<p>import numpy as np</p>
<p>modelNode = getNode(‘Probe_volume_with_model’)<br>
coords = slicer.util.arrayFromModelPoints(modelNode)<br>
densities = slicer.util.arrayFromModelPointData(modelNode, ‘NRRDImage’)</p>
</blockquote>
<p>However, the node coords calculated in this way have an error. For some reason the x and y coords here are the wrong sign (negative compared to positive values listed in the .inp file coordinates).</p>
<p>So my questions are:<br>
<strong>1)</strong> Why am I getting the wrong sign for these coordinates? I think the meshio .inp coordinates are the correct ones, since I can import this file into my FE program and the orientation is the same as in the original slicer Model.</p>
<p><strong>2)</strong> Are the coordinates and densities listed in the node order? Such that the first coordinate and density printed out is node 1 and so on? In other words, if I want to export node IDs with corresponding densities, can I simply add an array of 1 - n+1, where n is the number of nodes, and concatenate it to the densities? Or is there a function to query node numbers?</p>
<p>I.e.</p>
<blockquote>
<p>length = len(densities)<br>
IDs = np.zeros(1,length+1)<br>
print(len(list_array))</p>
<p>//need to reshape density array to be 2D instead of 1D<br>
IDs_2d = IDs[:, None]</p>
<p>//need to reshape density array to be 2D instead of 1D<br>
densities_2d = densities[:, None]</p>
<p>output = np.concatenate((IDs_2d.astype(int),densities_2d),axis=1)</p>
</blockquote>
<p><strong>3)</strong> When I check the segment statistics, the mean and max density values are a bit different from the densities I calculate from the volumetric mesh. I assume this is just because the volumetric mesh has larger sized elements and so some voxel values are averaged to get the values at those tet mesh nodes. Is that correct?</p>
<p>Thank you very much,<br>
Eva</p>

---

## Post #3 by @pieper (2023-04-19 14:09 UTC)

<p>Most likely issue 1 is due to LPS/RAS management.  We try to be very explicit and consistent about this in Slicer but you need to take care when working with other tools.  See <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#models">this</a> and <a href="https://www.slicer.org/wiki/Coordinate_systems">this for background</a>.</p>
<p>I’m not sure I follow your second question, but the <code>densities</code> will be in the same order as <code>coords</code>.  If these are one-to-one with your finite element nodes, then yes that mapping would make sense.</p>
<p>For question 3, it makes sense they would differ.  The results of Probe Volume with Model will be point samples while the Segment Statistics will include all the voxels in the volume in that segment so it could include some extremes and a different mean than the mesh points.</p>

---

## Post #4 by @evaherbst (2023-04-19 15:08 UTC)

<p>Thank you Steve!</p>
<ol>
<li>
<p>Oh, that makes a lot of sense, thanks! That link is very useful. I guess generating the input file is LPS since it was initially exported as VTK unstructured, and the coords I printed out from the scene are in RAS.</p>
</li>
<li>
<p>Great, that’s what I was thinking too - using the coords to double check the order is what I think it is.</p>
</li>
<li>
<p>Ok, perfect, just wanted to confirm.</p>
</li>
</ol>
<p>Thanks so much!<br>
Eva</p>

---
