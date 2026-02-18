# vtkMRMLAnnotationROINode

**Topic ID**: 11405
**Date**: 2020-05-04
**URL**: https://discourse.slicer.org/t/vtkmrmlannotationroinode/11405

---

## Post #1 by @rohan_n (2020-05-04 18:23 UTC)

<p>I’m looking at this link because my Python scripted module will have 2 or 3 vtkMRMLAnnotationROINode objects open at the same time and I would like them to be distinguishable from each other by line color and/or text label that is visible in the slicer window.<br>
<a href="https://apidocs.slicer.org/master/classvtkMRMLAnnotationROINode.html#afaa9522ed4bc6fa5f3234f3787e1c517" class="onebox" target="_blank" rel="nofollow noopener">https://apidocs.slicer.org/master/classvtkMRMLAnnotationROINode.html#afaa9522ed4bc6fa5f3234f3787e1c517</a></p>
<p><strong>What is the correct form of the input for SetLineColor?</strong> I tried<br>
r=slicer.vtkMRMLAnnotationROINode()<br>
r.SetLineColor([255,0,0]) and my module just crashed.</p>
<p><strong>Which function of vtkMRMLAnnotationROINode object would allow me to add a label for the ROI that can be seen in the slicer window, and what should its input look like?</strong><br>
SetLabelText didn’t appear to do anything.</p>
<p>Thanks,<br>
Rohan</p>

---

## Post #2 by @jamesobutler (2020-05-04 19:28 UTC)

<p>Review this other forum post - <a href="https://discourse.slicer.org/t/is-possible-to-change-the-color-of-the-roi-bounding-box-from-white-to-something-else/10034/" class="inline-onebox">Is possible to change the color of the ROI bounding box from white to something else</a>.</p>
<p>Setting ROI color isn’t a supported thing and fixes to annotation ROI won’t be fixed, but instead ROI objects will be moved into the new Markups module framework.</p>

---
