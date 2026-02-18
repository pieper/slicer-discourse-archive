# Can you make a difference overlay of two scalar overlays?

**Topic ID**: 2867
**Date**: 2018-05-22
**URL**: https://discourse.slicer.org/t/can-you-make-a-difference-overlay-of-two-scalar-overlays/2867

---

## Post #1 by @srb_4 (2018-05-22 04:38 UTC)

<p>If I have two scalar overlays for the same model, is there a way to create a new overlay that gives me the difference between overlay 1 and overlay 2?</p>
<p>Operating system: Windows 10<br>
Slicer version: 4.8.1</p>

---

## Post #2 by @lassoan (2018-05-22 04:50 UTC)

<p>If by “scalar overlay” you mean scalar data associated with points or cells of a mesh of model node, then it is really easy to do using numpy, since you can get the values as an array, and do any operation, and then create a new array or update an existing one with the result. For example, you can store difference of two arrays in one of the arrays like this:</p>
<pre><code>a1 = slicer.util.arrayFromModelPointData(modelNode, 'SomeArray')
a2 = slicer.util.arrayFromModelPointData(modelNode, 'SomeOtherArray')
a1[:] = a1-a2
slicer.util.arrayFromModelPointsModified(modelNode)
</code></pre>
<p>In Slicer-4.8.1, some of these convenience methods may not have been added yet, so you can either use a recent nightly, or add these methods to your code (see for example here: <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L773-L783">https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L773-L783</a>).</p>

---

## Post #3 by @srb_4 (2018-05-22 05:04 UTC)

<p>Thank you!</p>
<p>I had been given two different FreeSurfer thickness maps from two populations and wanted to show the difference between the two. I loaded them in as scalar volumes and then subtracted the volumes and reloaded them as scalar overlays to visualize on the surface model. Would that do the same thing?</p>

---

## Post #4 by @Nicole_Aucoin (2018-05-22 15:00 UTC)

<p>Slicer can read FreeSurfer geometry and thickness scalar overlay maps and create MRML model nodes. The model node has a function called <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLModelNode.cxx#L508" rel="nofollow noopener">Composite Scalars</a> that can combine two scalar overlays that are associated with a single model to show the differences between one designated as background and one as foreground.</p>
<p>Nicole</p>

---

## Post #5 by @srb_4 (2018-05-22 16:51 UTC)

<p>That looks like it would be perfect! Can you give me any information on how to implement this? I apologize for my lack of familiarity.</p>

---

## Post #6 by @Nicole_Aucoin (2018-05-22 17:28 UTC)

<p>It’s not exposed via the GUI, you’ll have to do some coding to call it. Assuming you’ve loaded a left hemisphere model and two thickness maps as scalar overlays (in my case thickness and area) you can do the following in the python console:</p>
<blockquote>
<p>lh = slicer.util.getNode(‘lh’)<br>
lh.CompositeScalars(‘surf/lh.thickness’, ‘surf/lh.area’, 0.0, 1.0, 0, 1, 0)</p>
</blockquote>
<p>It creates a new scalar overlay called [name1]+[name2] and sets it active. You’ll need to adjust the numerical parameters to get the compositing you want.<br>
You can see the scalar range of the overlays in the Models module, Display, Scalars section.</p>
<p>Nicole</p>

---

## Post #7 by @srb_4 (2018-05-22 17:58 UTC)

<p>That’s great! Thank you so much!</p>
<p>I notice that it only displays positive numbers. Is this just giving me the absolute difference? Is there any way to specify that I want the foreground subtracted from the background?</p>

---

## Post #8 by @Nicole_Aucoin (2018-05-22 19:14 UTC)

<p>The compositing of the scalars doesn’t do addition or subtraction, it’s a logical operation showing either the one overlay or the other depending on a comparison of values (this was a specific function I included years ago for FreeSurfer overlay display for a project). Check the code comments in the link above for implementation details. If you need mathematical operations, Andras’s method will be necessary.</p>
<p>Nicole</p>

---
