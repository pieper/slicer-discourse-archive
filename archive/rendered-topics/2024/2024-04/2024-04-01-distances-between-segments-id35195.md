---
topic_id: 35195
title: "Distances Between Segments"
date: 2024-04-01
url: https://discourse.slicer.org/t/35195
---

# Distances between segments

**Topic ID**: 35195
**Date**: 2024-04-01
**URL**: https://discourse.slicer.org/t/distances-between-segments/35195

---

## Post #1 by @ILB (2024-04-01 07:16 UTC)

<p>Hi!</p>
<p>Is there any software or stl viewer I can use that gives measurements between segments? For example, if I segment the liver and the aorta, is there a way to click between to points (one in the liver and the other in the aorta), and know the distance between both of them?<br>
It would be very useful.<br>
Thanks in advance!<br>
Best</p>

---

## Post #2 by @rfenioux (2024-04-02 07:36 UTC)

<p>Hi,</p>
<p>Yes you can easily achieve that using a Line Markup (available in the Markups Module or the Markups toolbar). You can place the points in the 2D view or directly on the surface of the segments in the 3D view.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de200a06c65cf4c9c13bf663a240d8d3b4ea5bb1.jpeg" data-download-href="/uploads/short-url/vH0DNZ9DsLLBfEZvFZnfoNeKhUd.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de200a06c65cf4c9c13bf663a240d8d3b4ea5bb1_2_675x500.jpeg" alt="image" data-base62-sha1="vH0DNZ9DsLLBfEZvFZnfoNeKhUd" width="675" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de200a06c65cf4c9c13bf663a240d8d3b4ea5bb1_2_675x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de200a06c65cf4c9c13bf663a240d8d3b4ea5bb1_2_1012x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de200a06c65cf4c9c13bf663a240d8d3b4ea5bb1.jpeg 2x" data-dominant-color="87868B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1243×920 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @ILB (2024-04-02 08:09 UTC)

<p>Thank you! That was exactly what I was looking for!</p>
<p>Also, by any chance do you know if there is a way to get the surface of contact between two elements, for example between a tumor and the adjacent organ?</p>
<p>Thanks again!</p>
<p>Best wishes</p>

---

## Post #4 by @qiqi5210 (2024-04-02 12:47 UTC)

<p>This could perhaps be achieved by obtaining the two adjacent segment arrays that need to be compared. Iterate through the points in one array that have a value of 1 and check if the voxel coordinates around them in the second array are also 1. If they are, then they are adjacent voxels. However, this method can be cumbersome, and there might be a better approach to implement it.</p>

---

## Post #5 by @ILB (2024-04-02 13:12 UTC)

<p>Thank you! But would this method return the value of the area (mm^2) in common between the two segments?</p>

---

## Post #6 by @qiqi5210 (2024-04-02 13:27 UTC)

<p>This method allows you to obtain a new segment, which represents the region adjacent to the previous two segments. You can then use other methods to obtain its surface area.</p>

---

## Post #7 by @rfenioux (2024-04-02 14:03 UTC)

<p>A manual method for obtaining the (approximate) area of a portion of a segment would be to use a closed curve markup. You could then obtain the area enclosed by the curve in the Measurements panel. However this will only work if the surface is almost flat.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/410ada2dea28c2b4eb7836903bd81c7d7b4db652.jpeg" data-download-href="/uploads/short-url/9hohL61dUaifrzApeQG1pZJfC14.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/410ada2dea28c2b4eb7836903bd81c7d7b4db652_2_675x500.jpeg" alt="image" data-base62-sha1="9hohL61dUaifrzApeQG1pZJfC14" width="675" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/410ada2dea28c2b4eb7836903bd81c7d7b4db652_2_675x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/410ada2dea28c2b4eb7836903bd81c7d7b4db652_2_1012x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/410ada2dea28c2b4eb7836903bd81c7d7b4db652.jpeg 2x" data-dominant-color="ABB2BA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1242×920 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Another method would be to extract the common surface using VTK. For this you can write a custom scripted module where you retrieve the meshes of the two segments, extract the common surface and measure the area using VTK filters.</p>

---

## Post #8 by @rfenioux (2024-04-02 14:54 UTC)

<p>Contrary to what I said above, there is a way to get the exact value of the area enclosed by a curve markups.</p>
<p>For this you can follow these steps :</p>
<ul>
<li>Export your segment to a model as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-model-surface-mesh-file" rel="noopener nofollow ugc">here</a></li>
<li>Create your closed curve around the area of interest</li>
<li>Go to the Dynamic Modeler Module and use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dynamicmodeler.html#curve-cut" rel="noopener nofollow ugc">Curve cut</a> tool, set your model and your curve as inputs. This will create an inside and an outside cutout models as output.</li>
<li>Go to the Models Module, select your “inside” model and read the surface area in the “information” panel.</li>
</ul>

---

## Post #9 by @ILB (2024-04-03 06:47 UTC)

<p>Thank you so much! That was really helpful!</p>

---
