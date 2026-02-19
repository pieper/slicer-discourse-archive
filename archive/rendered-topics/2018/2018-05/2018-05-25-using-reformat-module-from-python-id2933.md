---
topic_id: 2933
title: "Using Reformat Module From Python"
date: 2018-05-25
url: https://discourse.slicer.org/t/2933
---

# Using Reformat module from Python

**Topic ID**: 2933
**Date**: 2018-05-25
**URL**: https://discourse.slicer.org/t/using-reformat-module-from-python/2933

---

## Post #1 by @mschumaker (2018-05-25 21:07 UTC)

<p>I’m trying to use the Reformat module from a Python scripted module. I’m having trouble using the setSliceNormal and setWorldPosition methods. Looking at qSlicerReformatModuleWidget, both setSliceNormal and setWorldPosition have slots that take double*, and setSliceNormal has a public method that takes three arguments: setSliceNormal (double x, double y, double z). I tried to use it both ways, but I keep getting ValueError. Sample code:</p>
<pre><code>reformatWidget = slicer.modules.reformat.widgetRepresentation()
slice = slicer.app.layoutManager().sliceWidget('Red')
sliceNode = slice.mrmlSliceNode()
reformatWidget.setEditedNode(sliceNode,"","")
reformatWidget.setSliceNormal(1.0,0,0)
</code></pre>
<p>The result is: “ValueError: Called setSliceNormal(double normal) -&gt; void with wrong number of arguments: (1.0, 0.0, 0.0)”.<br>
I also tried a list, tuple, and a ctypes double array.<br>
Is there a way I can accomplish this with the Reformat module? Is there Python compatibility code that’s missing from this module?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2018-05-25 21:27 UTC)

<p>Is there a reason why you not simply modify the slice node?</p>

---

## Post #3 by @mschumaker (2018-05-25 21:51 UTC)

<p>I used (1,0,0) in the example, but I would like to be able to set a normal vector that’s off of the principal axes. Also a centre point of the rotation that’s not the centre of the image. I didn’t see a straightforward way to do that from vtkMRMLSliceNode.</p>

---

## Post #4 by @mschumaker (2018-05-25 22:09 UTC)

<p>In Github, I received a suggestion from <a class="mention" href="/u/jcfr">@jcfr</a> for how to improve the Python compatibility of the Reformat module by adding:</p>
<pre><code>Q_PROPERTY(QVector3D worldPosition READ worldPosition WRITE setWorldPosition)

[...]

QVector3D worldPosition() const;
void setWorldPosition(const QVector3D&amp; position); 
</code></pre>
<p>I’m not sure how the Q_PROPERTY macro works, but I’m willing to give this a try.</p>

---

## Post #5 by @lassoan (2018-05-25 22:42 UTC)

<p>Slice position and orientation are specified by SliceToRAS matrix. You can get it using GetSliceToRAS method and update it. You can also use SetSliceToRASByNTP to set slice orientation by slice normal and X axis and position.</p>

---

## Post #6 by @mschumaker (2018-05-28 14:26 UTC)

<p>Thank you, that’s exactly the method I was hoping to find. I missed it when I was looking at the API docs. Looking at the documentation for it, and at the code, I’m still unclear what the final parameter, “Orientation”, should be set to. In the switch statement in the code, it refers to the cases 0,1,2 as para-Axial, para-Sagittal, and para-Coronal, respectively. Does that mean that if the view I want is close to axial, I should set Orientation to 0?</p>

---

## Post #7 by @lassoan (2018-05-28 14:51 UTC)

<p>SetSliceToRASByNTP’s orientation parameter can be used to generate orthogonal views corresponding to an axial view. It just saves you from figuring out how to change the normal vector for orthogonal views.</p>

---

## Post #8 by @mschumaker (2018-05-28 14:59 UTC)

<p>Ok. My concern is that I don’t see a way that it will set the elements of the SliceToRAS matrix if I don’t supply an Orientation value of 0, 1, or 2. I couldn’t tell if that meant I was limited to the standard orthogonal views.</p>

---

## Post #9 by @lassoan (2018-05-28 15:00 UTC)

<p>N specifies the slice normal direction if you set orientation to Axial.</p>

---

## Post #10 by @mschumaker (2018-05-28 16:19 UTC)

<p>Ok, thanks. I wanted to make sure I was interpreting it correctly.</p>

---
