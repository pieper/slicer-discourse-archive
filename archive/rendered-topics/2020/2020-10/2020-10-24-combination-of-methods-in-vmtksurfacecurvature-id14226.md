# Combination of methods in vmtkSurfaceCurvature

**Topic ID**: 14226
**Date**: 2020-10-24
**URL**: https://discourse.slicer.org/t/combination-of-methods-in-vmtksurfacecurvature/14226

---

## Post #1 by @Jana_Trdlicova (2020-10-24 19:43 UTC)

<p>Hi everyone,</p>
<p>I have another problem with generating a ‘nice’ mesh of an aneurysm. I use the information about curvature (vmtkSurfaceCurvature) in vmtkMeshGenerator. There are 4 methods for computing the curvature, and I was wondering if I could somehow combine them. For example, I would like to use the gaussian method in one part of the mesh, and the mean method everywhere else. Is this possible?</p>
<p>If not, are there other possibilities of setting the TargetEdgeLengthArrayName, apart from ‘Curvature’ and ‘DistanceToCenterlines’?</p>
<p>Thank you in advance,<br>
Jana</p>

---

## Post #2 by @lantiga (2020-10-26 15:03 UTC)

<p>Hi Jana,<br>
what <code>vmtkMeshGenerator</code> requires for sizing is just a scalar field. Any <code>PointData</code> array associated on the <code>vtkPolyData</code> will work.<br>
So you can create a new array, assign the Gaussian curvature to one portion (according to some geometric criteria - e.g. the points within a sphere) and use mean curvature everywhere else. If you provide the array with a name, <code>GetPointData()-&gt;AddArray(the_array)</code> and save it, you can then specify that name as <code>TargetEdgeLengthArrayName</code> to the script.<br>
Hope this helps</p>
<p>Luca</p>

---

## Post #3 by @Jana_Trdlicova (2020-10-30 08:34 UTC)

<p>Hi Luca,</p>
<p>thank you very much for your response. Finally, I figured out how to implement it and it works well. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Now, the only problem is that I would like to smooth the new curvature in order to reduce the sharp edge between the two methods. Could you, please, give me some advice?</p>
<p>Thank you,<br>
Jana</p>

---
