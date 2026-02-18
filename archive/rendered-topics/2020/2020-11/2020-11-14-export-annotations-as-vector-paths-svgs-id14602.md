# Export annotations as vector paths / svgs

**Topic ID**: 14602
**Date**: 2020-11-14
**URL**: https://discourse.slicer.org/t/export-annotations-as-vector-paths-svgs/14602

---

## Post #1 by @noisyneuron (2020-11-14 18:25 UTC)

<p>Hi, I was wondering if it would be possible to export the annotated areas on an image as vector paths / svgs?</p>

---

## Post #2 by @noisyneuron (2020-11-14 23:56 UTC)

<p>to be more specific, I’m referring to the segments… I’d like to get the outline of the drawn segment as a vector instead of dealing with everything in raster form</p>

---

## Post #3 by @noisyneuron (2020-11-17 00:11 UTC)

<p>Operating system: OS X</p>
<p>Slicer version: 4.11.0</p>
<p>I building a website in which I render segmentations I generated in 3D slicer, and want to manipulate them with html/css (for eg. change the color of a specific segment).<br>
Is there any export format in 3D slicer that would allow me to convert segmentations (or label maps) into vector paths that I can save in an svg file? Or any other structured data format that specifies the points (x,y) that make up the outline for an individual segment?</p>

---

## Post #4 by @lassoan (2020-11-17 00:20 UTC)

<p>There should be no reason to develop such things from scratch, but instead you can use a DICOM web viewer for this (and extend/customize/improve it as needed). You can push a DICOM segmentation object from Slicer directly to a DICOMweb server and use OHIF viewer to view the images and segmentations. You can also launch a locally installed Slicer from the web viewer, create segmentation, and upload the result back to the server. You can use a very lightweight DICOM server, such as <a href="https://github.com/dcmjs-org/dicomweb-server">https://github.com/dcmjs-org/dicomweb-server</a>, or for demo/test purposes the <a href="https://kheops.online/">Kheops demo server</a>.</p>
<p>I’ll create a demo video of this tomorrow, it works very nicely.</p>

---

## Post #5 by @noisyneuron (2020-11-17 00:33 UTC)

<p>Thanks for the quick response. Looking into the links you shared. If I did want to do this anyway though, is there a way I might be able to export the coordinates of the paths in any structured data format?</p>

---

## Post #6 by @lassoan (2020-11-17 02:35 UTC)

<p>In all modern segmentation software, 3D image segmentations are natively stored in binary labelmaps. Conversion of arbitrary labelmaps to smooth curves is inherently very fragile and may result in very large point sets and loss of details. If you really must reimplement a segmentation viewer then I would recommend to use the native binary labelmap representation (render it as an additional image layer). OHIF viewer is free, open-source, restriction-free software, so you can copy-paste its segmentation renderer into your code (of course I would not recommend doing it, but it is still less waste of time than redeveloping from scratch).</p>
<p>If you are just interested to see how you can generate smooth parallel contours from segmentations then you choose to visualize a segmentation’s closed surface representation in slice views (Segmentations module / Display / Advanced / Representation in 2D views -&gt; Closed surface). See implementation <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/MRMLDM/vtkMRMLSegmentationsDisplayableManager2D.cxx">here</a>, using vtkPlaneCutter and vtkContourTriangulator. You can play with it and see what kind of quality problems and performance issues you will run into if you decided to store segmentations as parallel contours. Another issue that we learnt from legacy DICOM RT structure set representations, is that it is practically impossible to reliably reconstruct a 3D surface from parallel contours. So, you would go to lots of unnecessary trouble if you decided to use parallel contours for representing segmentations.</p>

---
