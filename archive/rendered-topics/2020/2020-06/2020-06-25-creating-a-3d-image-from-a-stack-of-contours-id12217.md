---
topic_id: 12217
title: "Creating A 3D Image From A Stack Of Contours"
date: 2020-06-25
url: https://discourse.slicer.org/t/12217
---

# Creating a 3D image from a stack of contours

**Topic ID**: 12217
**Date**: 2020-06-25
**URL**: https://discourse.slicer.org/t/creating-a-3d-image-from-a-stack-of-contours/12217

---

## Post #1 by @loubna (2020-06-25 15:41 UTC)

<p>I’m trying to create a 3D labelMa from a stack of 2D contours in SlicerRT. . My idea is to binarize the contours, and to run a marching cubes on the resulting binary volume. Before do that. I have Added some treatments which I have inspired from SlicerRT before convert set of contours to binary image (like sort contours based on z value, remove keyholes from contours and Set all of the lines to be oriented in the clockwise direction)</p>
<p>I convert the set of planar contours based on the Following example:</p>
<p><a href="https://vtk.org/Wiki/VTK/Examples/Cxx/PolyData/PolyDataToImageData" class="onebox" target="_blank" rel="noopener nofollow ugc">https://vtk.org/Wiki/VTK/Examples/Cxx/PolyData/PolyDataToImageData</a></p>
<p>the imagedata is well reconstructed but it seems like there are two missing slices (it contains holes) "see attached figure</p>
<p>con you tell me where is the problem please?</p>
<p>here is a sample code of extrusion filter that i have employed:</p>
<p>// sweep polygonal data (this is the important thing with contours!)<br>
vtkSmartPointer extruder =<br>
vtkSmartPointer::New();<br>
extruder-&gt;SetInputData(linePolyData);<br>
extruder-&gt;SetScaleFactor(1.);<br>
extruder-&gt;SetExtrusionTypeToNormalExtrusion();<br>
extruder-&gt;SetVector(0, 0, lineSpacing);  //lineSpacing is the space between contours<br>
extruder-&gt;CappingOn();<br>
extruder-&gt;Update();</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64f65b221b1b3376242392d4496bfa0f86747412.jpeg" alt="image" data-base62-sha1="ep9yRxZjIPsgnNVgbGLnGRQcwCu" width="531" height="497"></p>
<p>thank’s in advance</p>

---

## Post #2 by @cpinter (2020-06-25 16:50 UTC)

<p>Implementing such conversions in a way that it is robust and generic is extremely hard, and we spent years on doing that. Now it is part of the Segmentations infrastructure, and all you need to do is add your polydata to a segment taht you put in a segmentation node, and then you can have it converted in the Segmentations module (with SlicerRT installed). Is there a specific reason to reimplement this conversion from scratch?</p>

---

## Post #3 by @loubna (2020-06-25 17:01 UTC)

<p>Thank you very much for reply. But I do not understand how can I add polydata to a segment and how can I get vtkImage data ? To my knowleadge, vtk image data is computed from reconstructed surface in slicerRT.</p>
<p>I would reimplement that in order to be able to Apply marching cube and other methods then compare them. I know that is more easier if i reconstruct surface from imagedata in slicer (using fro example flying edges or vtkDiscreteMarchingcubes) however I must reipmlement it in slicerRT (from contours ) using the basic marching cube for other purposes of education.</p>
<p>Polydata in my case are the planar contours (3D points)</p>

---

## Post #4 by @loubna (2020-06-25 17:18 UTC)

<p>I have another question. If I keep the shown model, how can deduce the corresponding point position of polydata on vtkImageData without rounding the point coordinates.</p>
<p>Thank you very much in advance</p>

---
