# Differentiating between 2 vtkMRMLAnnotationROINodes

**Topic ID**: 12727
**Date**: 2020-07-25
**URL**: https://discourse.slicer.org/t/differentiating-between-2-vtkmrmlannotationroinodes/12727

---

## Post #1 by @rohan_n (2020-07-25 00:02 UTC)

<p>Hello,<br>
Let’s say I’ve done the following:</p>
<p>a = slicer.vtkMRMLAnnotationROINode()<br>
slicer.mrmlScene.AddNode(a)</p>
<p>b = slicer.vtkMRMLAnnotationROINode()<br>
slicer.mrmlScene.AddNode(b)</p>
<p>And the user is looking at an image in the red and yellow slices with these 2 ROI’s in the scene. What is a good way to modify how each vtkMRMLAnnotationROINode looks in the scene so that it is obvious to the user which one is a and which one is b?</p>
<p>I thought that doing</p>
<p>a.SetLabelText(“ROI1”)</p>
<p>would make the label ROI1 hover over the vtkMRMLAnnotationROINode a in the scene, but that doesn’t appear to be the case. I also tried</p>
<p>a.SetLineColor([255,0,0])</p>
<p>but I don’t see any change in what the vtkMRMLAnnotationROINode a looks like in the scene.</p>
<p>Thanks,<br>
Rohan Nadkarni</p>

---

## Post #2 by @lassoan (2020-07-25 00:33 UTC)

<p>vtkMRMLAnnotationROI does not have labels and cannot be recolored. It will not be improved any further but we will add markups ROI node instead (probably within a couple of months), which will have all these and many more features. You can track the status of this effort <a href="https://github.com/Slicer/Slicer/issues/5061">here</a>.</p>

---
