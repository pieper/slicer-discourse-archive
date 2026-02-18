# Display and interact with a vtkMRMLAnnotationROINode() in the view

**Topic ID**: 17056
**Date**: 2021-04-13
**URL**: https://discourse.slicer.org/t/display-and-interact-with-a-vtkmrmlannotationroinode-in-the-view/17056

---

## Post #1 by @ond12 (2021-04-13 09:42 UTC)

<p>Hi Slicer Community,</p>
<p>I apologize in advance if the answer to my question is out there. I’ve seen related threads, but I haven’t  manage to get my solution to work.</p>
<p>I’m using slicer 4.11<br>
I would like to create a vtkMRMLAnnotationROINode() and set it’s position size in the slice view as in the cropvolume module.</p>
<p>I’ve tried this script but the node it’s not showing in the 2D slice view but only in the 3D view</p>
<pre><code>roi=slicer.vtkMRMLAnnotationROINode()
slicer.mrmlScene.AddNode(roi)
roi.Initialize(slicer.mrmlScene)
roi.SetDisplayVisibility(1)
roi.SetInteractiveMode(1)
</code></pre>
<p>If you have a solution please?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2021-04-14 04:54 UTC)

<p>We are working on the Markups module to replace the old Annotation module. I would recommend to use Markups ROI. You can create it like this:</p>
<pre><code class="lang-python">roiNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsROINode')
roiNode.SetCenter([20,30,40])
roiNode.SetSize([33,23,45])
</code></pre>

---

## Post #3 by @ond12 (2021-04-14 07:23 UTC)

<p>Thanks you,  unfortunately i’m using 4.11 of Slicer it seems the ‘vtkMRMLMarkupsROINode’ was not fully implemented yet.</p>
<p>Also i manage to emulate the good behavior i wanted by a trick: (after my image is loaded )</p>
<pre><code>  cropVolumeWidget = slicer.modules.cropvolume.widgetRepresentation()
  cropVolumeWidget.setMRMLScene(slicer.mrmlScene)
  cropVolumeWidget.enter()
  inp = cropVolumeWidget.findChild(slicer.qMRMLNodeComboBox,"InputROIComboBox")
  inp.addNode()
</code></pre>
<p>This create the Roi node and showing it.<br>
I would like to do the same but the good way. Do you have any idea how can i emulate the crop module by scripting :  step 1 set a define input and output , step 2 create and edit by hand the roi node  ?</p>
<p>Thanks</p>

---
