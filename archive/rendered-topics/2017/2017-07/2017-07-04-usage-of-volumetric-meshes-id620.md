---
topic_id: 620
title: "Usage Of Volumetric Meshes"
date: 2017-07-04
url: https://discourse.slicer.org/t/620
---

# Usage of volumetric meshes

**Topic ID**: 620
**Date**: 2017-07-04
**URL**: https://discourse.slicer.org/t/usage-of-volumetric-meshes/620

---

## Post #1 by @cosmogit (2017-07-04 11:08 UTC)

<p>Hi everyone,</p>
<p>I am quite new to 3D slicer and haven’t figured out many of the function yet.<br>
I found this blog post on <a href="https://blog.kitware.com/3d-slicer-adds-volumetric-mesh-support/" rel="nofollow noopener">volumetric mesh support</a> and I would like to experiment with its capabilities.</p>
<p>Can someone might give me an explanation on how I get such a volumentric mesh? I always end up with an normal surface mesh.</p>
<p>Thank you,<br>
Julian</p>
<hr>
<p>Slicer version: 4.7.0-2017-06-26 r26137</p>

---

## Post #2 by @fedorov (2017-07-05 16:54 UTC)

<p>There are several extensions that advertise the capability of generating a volume mesh, but I don’t know whether they are functional and/or maintained.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/CleaverExtension" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/CleaverExtension</a><br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/PBNRR" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/PBNRR</a></p>
<p>There are well-established tools outside of Slicer that can be used for volumetric mesh generation, such as TetGen and CGAL:</p>
<p><a href="http://wias-berlin.de/software/tetgen/" class="onebox" target="_blank">http://wias-berlin.de/software/tetgen/</a></p>
<p>Specifically for generating volumetric meshes from image data, you can look at iso2mesh, although it is not self-contained and you will need matlab/octave (I personally do not have any experience with this package):</p>
<p><a href="http://iso2mesh.sourceforge.net/cgi-bin/index.cgi" class="onebox" target="_blank">http://iso2mesh.sourceforge.net/cgi-bin/index.cgi</a></p>
<p>and CGAL (there is a section of the manual of generating meshes from labeled image data, I don’t know if they provide any ready to use command line tools):</p>
<p><a href="http://doc.cgal.org/latest/Mesh_3/index.html" class="onebox" target="_blank">http://doc.cgal.org/latest/Mesh_3/index.html</a></p>

---

## Post #3 by @Michael_Hardisty (2017-08-11 15:22 UTC)

<p>Hi Julian,</p>
<p>I thought I would share my experience that I have had lately with volumetric meshing and include the problems I am having</p>
<p>I tried using cleaver with limited success. I had a lot of trouble with the extension initially.  After I spoke with Andras Lasso I was able to get the meshing working.  The main thing I did to get cleaver to work with my data was to create a label map with a value of 75 on the inside and -75 on the outside.  I used simple filters to do the shifting and scaling.</p>
<p>2 notes on using cleaver:  1) the mesh did not contain tetrahedra as far as I could tell.  Instead it contained 4 triangles representing the faces instead of tetrahedra.  2) the mesh was not aligned in physical space with the volumes.</p>
<p>The method I am currently working with is using vtkDataSetTriangleFilter with something like the following at the python interpreter</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import vtk
&gt;&gt;&gt; dstFilter = vtk.vtkDataSetTriangleFilter()
&gt;&gt;&gt; croppedScan = getNode("croppedScan")
&gt;&gt;&gt; dstFilter.SetInputData(croppedScan.GetImageData())
&gt;&gt;&gt; dstFilter.Update()
&gt;&gt;&gt; mesh = dstFilter.GetOutput()
&gt;&gt;&gt; modelNode = slicer.vtkMRMLModelNode()
&gt;&gt;&gt; modelNode.SetAndObserveMesh(mesh)
&gt;&gt;&gt; slicer.mrmlScene.AddNode(modelNode)
</code></pre>
<p>This creates a solid rectangular prism mesh, where each voxel is split into several tets.  The nodes are labeled with the intensity of the scan.I was able to cut out regions of the mesh based on the intensity at the nodes using vtkThreshold.</p>
<p>I am having trouble labeling the tetrahedra with intensity.  I wrote the following function to label the tetrahedra with intensity.  After this processing step the meshes show up as having zero cells in the Models module.  Further they are not visualized in the 3D scene.  The vtk files written from these models appear to have the cell data.  Does anyone have any thought on how to go about labeling tets in Slicer that allows visualization?  Is there some problem with my approach?</p>
<pre><code class="lang-auto">def sampleNodeScalarOntoCellScalar(mesh):
    """

    :type mesh: vtkUnstructuredGrid
    """
    idList = vtk.vtkIdList()
    cells = mesh.GetCells()
    nCell = cells.GetNumberOfCells()

    scanIntensity = vtk.vtkFloatArray()
    scanIntensity.SetNumberOfComponents(1)
    scanIntensity.SetNumberOfValues(nCell)

    for cellIndex in range(nCell):
        mesh.GetCellPoints(cellIndex, idList)
        scalarArray = mesh.GetPointData().GetArray(0)
        meanScalar = 0
        numPoints = idList.GetNumberOfIds()
        for pointIndex in range(numPoints):
            meanScalar = meanScalar + scalarArray.GetValue(idList.GetId(pointIndex))


        meanScalar = meanScalar / numPoints
        scanIntensity.SetValue(cellIndex, meanScalar)

    mesh.GetCellData().SetScalars(scanIntensity)
    return scanIntensity
</code></pre>
<p>Thanks for the help!</p>
<p>Michael</p>

---

## Post #4 by @lassoan (2017-08-12 14:30 UTC)

<aside class="quote no-group" data-username="Michael_Hardisty" data-post="3" data-topic="620">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michael_hardisty/48/1593_2.png" class="avatar"> Michael_Hardisty:</div>
<blockquote>
<p>the mesh did not contain tetrahedra as far as I could tell.  Instead it contained 4 triangles representing the faces instead of tetrahedra.</p>
</blockquote>
</aside>
<p>Have you tried the new Cleaver library? Does it still write volumetric meshes like this?</p>
<aside class="quote no-group" data-username="Michael_Hardisty" data-post="3" data-topic="620">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michael_hardisty/48/1593_2.png" class="avatar"> Michael_Hardisty:</div>
<blockquote>
<p>the mesh was not aligned in physical space with the volumes</p>
</blockquote>
</aside>
<p>This is a bug in the CLI modules in the Cleaver extension. We did not see this before, because Slicer could not load volumetric meshes. It should be very easy to fix, but I would do it only after upgrading Cleaver extension to use latest Cleaver library.</p>
<aside class="quote no-group" data-username="Michael_Hardisty" data-post="3" data-topic="620">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michael_hardisty/48/1593_2.png" class="avatar"> Michael_Hardisty:</div>
<blockquote>
<p>I am having trouble labeling the tetrahedra with intensity</p>
</blockquote>
</aside>
<p>To see if it is an error in how you are setting scalar data or how Slicer displays it, you can compute some scalars and verify visualization in Paraview, then save to file, load the file into Slicer, and see if it is displayed correctly. If you want to color by cells instead of by points then set cell array instead of point array (there was a small bug that prevented cell scalar display in Slicer, I’ll commit a fix for that later today).</p>

---

## Post #5 by @lassoan (2017-10-30 19:02 UTC)

<p><a class="mention" href="/u/michael_hardisty">@Michael_Hardisty</a> I’ve added Segment Mesher extension that can generate volumetric meshes using Cleaver2 or Tetgen. See a bit more details in this topic: <a href="https://discourse.slicer.org/t/convert-3d-slicer-into-3d-solid-body/1307/8?u=lassoan">Convert 3D slicer into 3D solid body</a></p>

---

## Post #6 by @Michael_Hardisty (2017-10-31 16:15 UTC)

<p>Thanks for follow up.  This enhancement should be helpful to our group.</p>

---

## Post #7 by @Saima (2018-08-14 09:40 UTC)

<p>Dear Michael,<br>
Can you please post the screen shots of how you successfully got the tetrahedral mesh for geometry of interest.</p>
<p>Does it produces cube always even if the segmented label is provided and you want tetrahedral mesh for only that portion of image?</p>
<p>Regards,<br>
Saima</p>

---

## Post #8 by @Michael_Hardisty (2018-08-16 12:35 UTC)

<p>Hi Saima,</p>
<p>I looked back at my notes and I don’t have any screenshots.  We’ve moved in a different direction on this project.  The vtk based method is essentially possible with code snippet in the thread. Are you referring to one of the other methods I had tried?  Which method are you referring to?  I am happy to help and can reproduce what I had done but want to make sure that I understand which method you are trying to use.</p>
<p>Michael</p>

---

## Post #9 by @Saima (2018-08-17 04:37 UTC)

<p>Dear Michael,<br>
Thank you for your reply.</p>
<p>The problem is to get the volumetric mesh of brain from the cubic mesh generated through using segment mesher. The brain is inside the cube.</p>
<p>How do I achieve this?</p>
<p>How did you use the threshold to cut the unwanted regions of mesh based on intensity values?<br>
how to get the intensity values?</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---
