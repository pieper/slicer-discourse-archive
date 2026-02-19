---
topic_id: 11054
title: "Extract Points From Vtkimagedata"
date: 2020-04-09
url: https://discourse.slicer.org/t/11054
---

# Extract points from vtkImageData

**Topic ID**: 11054
**Date**: 2020-04-09
**URL**: https://discourse.slicer.org/t/extract-points-from-vtkimagedata/11054

---

## Post #1 by @loubna (2020-04-09 10:58 UTC)

<p>Hi,</p>
<p>My question is how can I extract points from vtkImageData. For example, considering 3D image(labelMap), if in  <code>voxels</code>  there are 3 voxel values, I would get the coordinates of those voxels.</p>
<p>vtkImageData-&gt;getPoint() return the point coordiantes in physical space. However I want the point coordinates in ijk space then convert them to RAS space.</p>
<p>Thank’s in advance</p>

---

## Post #2 by @Sam_Horvath (2020-04-09 14:11 UTC)

<p>To get the coordinates in index space [ijk], You would use<br>
<code>vtkImageData-&gt;TransformPhysicalPointToContinuousIndex(point[3], index[3])</code></p>
<p>See: <a href="https://vtk.org/doc/nightly/html/classvtkImageData.html#aa37a2184cb38394a8828d4998f0628fc" rel="nofollow noopener">https://vtk.org/doc/nightly/html/classvtkImageData.html#aa37a2184cb38394a8828d4998f0628fc</a></p>

---

## Post #3 by @loubna (2020-04-09 14:58 UTC)

<p>Thank’s for the response. What about  if I takes I,J,K voxel coordinates directly? where</p>
<p>vtkImageData-- &gt;GetExtent(Kmin,Kmax,Jmin,Jmax,IMin,Imax)</p>
<p>i in range (kmin, kmax)<br>
j in range (jMin,Jmax)<br>
k in range (iMin,Imax)</p>

---

## Post #4 by @Sam_Horvath (2020-04-09 15:25 UTC)

<p>That would also work.</p>

---

## Post #5 by @lassoan (2020-04-09 17:12 UTC)

<p>There are also a few complete examples in script repository, for example:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_value_of_a_volume_at_specific_voxel_coordinates" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_value_of_a_volume_at_specific_voxel_coordinates</a></p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates</a></p>

---

## Post #6 by @loubna (2020-04-10 17:51 UTC)

<p>Thank’s for your responses.</p>
<p>I will try to clarify more my issue.</p>
<p>I have a label Map (vtkImage Data) on which I have applied “vtkImageLabelOutlines” filter  to keep only labelMap boundries.</p>
<p>What I want is to recover the 3D points  corresponding to labelMap boundries labelMapBoundry) and store them  in vtkPoints array</p>
<p>I am trying athe following test, but I don’t know if it can resolve the issue:</p>
<p>vtkVariant variant = labelMapBoundry-&gt;GetPointData()-&gt;GetScalars()-&gt;GetVariantValue(labelMapBoundry-&gt;computePointId(ijk_coords);</p>
<p>if(variant==1)<br>
then store (i,j,k).</p>

---

## Post #7 by @lassoan (2020-04-10 23:47 UTC)

<aside class="quote no-group" data-username="loubna" data-post="6" data-topic="11054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/cab0a1/48.png" class="avatar"> loubna:</div>
<blockquote>
<p>vtkVariant variant = labelMapBoundry-&gt;GetPointData()-&gt;GetScalars()-&gt;GetVariantValue(labelMapBoundry-&gt;computePointId(ijk_coords);</p>
</blockquote>
</aside>
<p>I don’t understand this. You can convert between voxel and physical coordinates as described in the script repository examples I linked above.</p>

---
