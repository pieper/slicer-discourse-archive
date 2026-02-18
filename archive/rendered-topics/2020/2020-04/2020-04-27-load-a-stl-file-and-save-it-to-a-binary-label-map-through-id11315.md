# Load a .stl file and save it to a binary label map through

**Topic ID**: 11315
**Date**: 2020-04-27
**URL**: https://discourse.slicer.org/t/load-a-stl-file-and-save-it-to-a-binary-label-map-through/11315

---

## Post #1 by @Xabierenko (2020-04-27 14:22 UTC)

<p>Good afternoon,<br>
I’m trying to save a big bunch of .stl files to .nrrd binary label maps through python. I’m using the code below:</p>
<pre><code>volume = slicer.util.loadVolume('C:\\Users\mreib\OneDrive - upf.edu\Burdeos\images\Bordeaux_Case1\image.mha', returnNode=True)
segmentation = slicer.util.loadSegmentation('C:\Users\mreib\OneDrive - upf.edu\Burdeos\Observer_1\case1_1.stl', returnNode=True)

labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')

ids = vtk.vtkStringArray()
seg = getNode('case1_1')
seg.GetDisplayNode().GetVisibleSegmentIDs(ids)

slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(seg, ids, 
labelmapVolumeNode, volume)
</code></pre>
<p>I keep getting the following error.</p>
<pre><code>Traceback (most recent call last):
File "&lt;console&gt;", line 1, in &lt;module&gt;
TypeError: no overloads of ExportSegmentsToLabelmapNode() take 2 arguments
</code></pre>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2020-04-27 16:23 UTC)

<p>Type <code>help(slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode)</code> in the Python console or read the <a href="http://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html">API documentation</a> to get information on what parameters are needed.</p>
<p>You may also find the numerous <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_labelmap_node_from_segmentation_node">segmentation examples in script repository</a> useful.</p>

---

## Post #3 by @Xabierenko (2020-04-27 17:57 UTC)

<p>I have managed to solve it, but thank you very much anyways! Now I have a problem running the script from the python interactor. I suppose it isn’t as simple as using ‘python Myscript.py’.</p>

---

## Post #4 by @lassoan (2020-04-27 20:58 UTC)

<p>It is almost as simple. You can use <code>PythonSlicer Myscript.py</code> (there are a couple of variants - see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Launching_Slicer">here</a>).</p>

---

## Post #5 by @Xabierenko (2020-04-27 21:00 UTC)

<p>Thanks for your help! I’m sorry for asking such simple questions.</p>

---

## Post #6 by @lassoan (2021-03-29 00:34 UTC)

<p>2 posts were split to a new topic: <a href="/t/combine-stls-and-export-as-nrrd/16812">Combine STLs and export as NRRD</a></p>

---
