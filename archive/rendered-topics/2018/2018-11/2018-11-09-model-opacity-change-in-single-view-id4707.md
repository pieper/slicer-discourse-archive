# Model opacity change in single view

**Topic ID**: 4707
**Date**: 2018-11-09
**URL**: https://discourse.slicer.org/t/model-opacity-change-in-single-view/4707

---

## Post #1 by @priya.vada4 (2018-11-09 21:46 UTC)

<p>Hi</p>
<p>When the Slicer display is setup in the Triple 3D view, is it possible to change the opacity of a model only in 1 view while the model opacity remains the same in the other two views. I know it is possible to change whether the model is visible or not (using vtkMRMLViewNodes) but I wasn’t sure if you could change only the opacity of the model in a single view.</p>
<p>Thanks<br>
Priya</p>

---

## Post #2 by @lassoan (2018-11-10 05:37 UTC)

<p>On the user interface, only the first display node is shown. However, you can add any number of display nodes using the Python console. Turn off visibility for one view on the GUI (e.g., View3) and add a new display node with the desired view ID and display properties:</p>
<pre><code class="lang-auto">modelDisplayNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelDisplayNode")
modelDisplayNode.SetViewNodeIDs([slicer.mrmlScene.GetFirstNodeByName("View3").GetID()])
modelDisplayNode.SetOpacity(0.5)
modelNode.AddAndObserveDisplayNodeID(modelDisplayNode.GetID())
</code></pre>

---

## Post #3 by @priya.vada4 (2018-11-12 20:08 UTC)

<p>Thanks Andras. With slight modifications, your suggestions worked well.</p>
<p>Thanks<br>
Priya</p>

---

## Post #4 by @talmazov (2020-07-30 21:55 UTC)

<p>Hey,<br>
I am trying to change the opacity of a 3D model within vtkMRMLModelDisplayNode (the 3D object viewer) View1</p>
<blockquote>
<p>modelDisplayNode=slicer_model.GetDisplayNode() <span class="hashtag-raw">#vtkMRMLModelDisplayNode</span><br>
modelDisplayNode.SetViewNodeIDs([slicer.mrmlScene.GetFirstNodeByName(“View1”).GetID()])<br>
modelDisplayNode.SetOpacity(float(mat_color.find(‘a’).text))<br>
slicer_model.AddAndObserveDisplayNodeID(modelDisplayNode.GetID())</p>
</blockquote>
<p>however i don’t see change in the opacity, rather the color changes. in fact if i set SetOpacity(0) that is when the true color appears.</p>
<p>im basically trying to set this value for the model<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc623d8a47e87ec7f808b8520917feffe369a4a1.png" alt="image" data-base62-sha1="vrBwoKbzPeOQ2YwmoFPHIdyBLFv" width="551" height="424"></p>

---

## Post #5 by @lassoan (2020-07-30 22:14 UTC)

<p>If you need to display the same model differently in each view then you need to create a separate display node for each. Note that the models module GUI always shows/modifies the first display node only.</p>

---
