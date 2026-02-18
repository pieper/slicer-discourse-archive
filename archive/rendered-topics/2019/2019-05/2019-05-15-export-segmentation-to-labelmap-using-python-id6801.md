# Export segmentation to labelmap using python

**Topic ID**: 6801
**Date**: 2019-05-15
**URL**: https://discourse.slicer.org/t/export-segmentation-to-labelmap-using-python/6801

---

## Post #1 by @Dmitriy_Desser (2019-05-15 12:47 UTC)

<p>Hi guys,</p>
<p>I am trying to save some clicks and time by wrting a python script for saving my segmentations to files (labelmaps (nii.gz))<br>
I simply do not undestand how to provide the reference image to the function:</p>
<pre><code>slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode()
</code></pre>
<p>so my code is:</p>
<pre><code>seg = slicer.util.getNode(‘Segmentation_2’)
lmVN = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLLabelMapVolumeNode’)
slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode(seg, lmVN)
saveNode(lmVN, file_name)
</code></pre>
<p>if I give the reference image as additional argument, I get following error:</p>
<pre><code>Traceback (most recent call last):

File “”, line 1, in

TypeError: ExportAllSegmentsToLabelmapNode() takes exactly 2 arguments (3 given)
</code></pre>
<p>Can anybody help?</p>
<p>Thank you very much!</p>
<p>Cheers,</p>
<p>Dima</p>

---

## Post #2 by @lassoan (2019-05-15 13:34 UTC)

<p>See code snippet that does what you need in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_labelmap_node_from_segmentation_node" rel="nofollow noopener">script repository</a>, and a complete working example <a href="https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37" rel="nofollow noopener">here</a>.</p>

---

## Post #3 by @Dmitriy_Desser (2019-05-15 14:23 UTC)

<p>thank you very much for your reply!</p>
<p>After running this Slicer crashes down:</p>
<pre><code>#load volume
masterVolumeNode = slicer.util.loadVolume('c:/Users/desserdmi/Desktop/data.nii.gz', returnNode=True)

#make vtk object of mastervolume
masterVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkmasterVolumeNode")

#  --- Doing some   manual segmentation ----

#make segmentationNode
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")

#set references to masterVolumeNode
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)

#make labelvolumenode
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')

#export Segmentation to labelmapNode
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, masterVolumeNode)

#save labelmap to disk
slicer.util.saveNode(labelmapVolumeNode,"c:/Users/desserdmi/Desktop/data.nii.gz")
</code></pre>
<p>I am still doing something wrong… Do you maybe have any idea of what the reason could be?</p>

---

## Post #4 by @cpinter (2019-05-15 15:05 UTC)

<p>The original error was caused because that function is static, and the way you called it, it passes the object instance (self) as well.</p>
<p>To the code you recently pasted:</p>
<aside class="quote no-group quote-modified" data-username="Dmitriy_Desser" data-post="3" data-topic="6801">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dmitriy_desser/48/3523_2.png" class="avatar"> Dmitriy_Desser:</div>
<blockquote>
<p>masterVolumeNode = slicer.mrmlScene.AddNewNodeByClass(“vtkmasterVolumeNode”)</p>
</blockquote>
</aside>
<p>You don’t need this for sure. By the way there is no such class as vtkmasterVolumeNode. So this will return None and the variable won’t contain the loaded nifti file any more.</p>

---

## Post #5 by @Dmitriy_Desser (2019-05-15 15:49 UTC)

<p>Thank you very much for your reply!</p>
<p>the reason, why I have tried this is the error message I get:</p>
<pre><code>Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
TypeError: SetReferenceImageGeometryParameterFromVolumeNode argument 1: method requires a VTK object
</code></pre>
<p>Anyway, is there no simple solution for this issue in 3dSlicer? I mean a simple save segmentation as function like in ITK-SNAP?</p>
<p>I have an amount of data with long names (BIDS) and trying to do some automatisation for segmentation like: load data -&gt; segment it manually -&gt; save segmentation to binary label maps</p>

---

## Post #6 by @cpinter (2019-05-15 16:07 UTC)

<p>In general, my advice is that try running the lines within the python interactor one by one, checking the content of variables. The error messages are usually pretty straightforward. For example if the message is that it should be a VTK object and it’s not, then you need to find out what it is instead.</p>
<aside class="quote no-group" data-username="Dmitriy_Desser" data-post="5" data-topic="6801">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dmitriy_desser/48/3523_2.png" class="avatar"> Dmitriy_Desser:</div>
<blockquote>
<p>is there no simple solution for this issue in 3dSlicer? I mean a simple save segmentation as function like in ITK-SNAP?</p>
</blockquote>
</aside>
<p>Of course there is:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4bf9067c39c60535ca7db2aeded3573f1c1b3b85.png" alt="image" data-base62-sha1="aQ5lmDBDaswDzkvzeRcDAXHneWF" width="516" height="161"><br>
(this is in the Segmentations module)</p>
<p>Pleae check the source code for that if you want to automate it. Also the script repository (see <a class="mention" href="/u/lassoan">@lassoan</a>’s answer above) contains lots of examples you can directly use. In addition, this forum has topics for mostly every issue you may encounter, so please don’t hesitate to search it. The documentation may also help: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations" class="inline-onebox">Documentation/Nightly/Modules/Segmentations - Slicer Wiki</a></p>

---

## Post #7 by @lassoan (2019-05-15 17:15 UTC)

<p>We are of course aware that some simple segmentation software (that cannot work with arbitrary number of master volumes with varying geometry, overlapping segments, etc.) can save everything in a simple 3D labelmap. However, since Slicer is much more flexible, we need to use a more general file format by default to be able to save all segmentation data without losing information.</p>
<p>If you only use a single master volume and segments don’t overlap then you can export the segmentation into a simple 3D labelmap:</p>
<ul>
<li>Using the application GUI by a few clicks either as Csaba showed above, or even simpler, just by right-clicking on the segmentation node in Data module and selecting “Export visible segments to binary labelmap”</li>
<li>Using two lines of Python code <code>AddNewNodeByClass</code> followed by <code>ExportVisibleSegmentsToLabelmapNode</code> (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_labelmap_node_from_segmentation_node" rel="nofollow noopener">here</a>).</li>
</ul>
<p>I’ve added a complete example that exports your segmentation to a simple 3D labelmap if you hit Ctrl+Shift+S - see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_labelmap_node_from_segmentation_node" rel="nofollow noopener">here</a>. You can add the code snippet to you <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_systematically_execute_custom_python_code_at_startup_.3F" rel="nofollow noopener">.slicerrc</a> file to make this feature permanently available.</p>

---

## Post #8 by @Dmitriy_Desser (2019-05-16 11:31 UTC)

<p>Thank you so much guys!</p>
<p>editing .slicerrc works perfectly!</p>
<p>This is what I was looking for!</p>
<p>Cheers,</p>
<p>Dima</p>

---

## Post #9 by @Jithendra (2020-07-30 16:12 UTC)

<p>Hi Guys,</p>
<p>I am trying to automate storing the segmentation Node using 3D Slicer extension.</p>
<p>self.currentSelector = slicer.qMRMLNodeComboBox()<br>
self.currentSelector.nodeTypes = [“vtkMRMLScalarVolumeNode”]<br>
…<br>
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(actual_segmentation_node, labelmapVolumeNode,actual_master_node)</p>
<p>Error details<br>
ExportVisibleSegmentsToLabelmapNode argument 1: method requires a VTK object</p>
<p>The problem I am facing is I am unable to get reference to the actual Node name referred by slicer.qMRMLNodeComboBox().</p>
<p>The alternative as given in the website reference is getNode(“name”) or GetFirstNodeByClass(“vtkMRMLSegmentationNode”).This requires either it should be first in the list or know the node name earlier.</p>
<p>I want to get all the names of Segmentation Node which is currently selected by the qMRMLNodeComboBox().</p>
<p>Please share the reference if you have any.</p>
<p>Thank you very much!</p>

---

## Post #10 by @lassoan (2020-07-30 16:27 UTC)

<aside class="quote no-group" data-username="Jithendra" data-post="9" data-topic="6801">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jithendra/48/7658_2.png" class="avatar"> Jithendra:</div>
<blockquote>
<p>The problem I am facing is I am unable to get reference to the actual Node name referred by slicer.qMRMLNodeComboBox()</p>
</blockquote>
</aside>
<p>You can get the node selected in <code>qMRMLNodeComboBox</code> by calling <code>currentNode()</code> method. See more examples and background information in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">Slicer programming tutorials</a>.</p>

---

## Post #11 by @Jithendra (2020-07-30 16:52 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a>. This solves my problem.<br>
I was able to get the name using slicer.util.getNode(“currentNodeId value”).GetName()</p>

---

## Post #12 by @lassoan (2020-07-30 17:46 UTC)

<p>Thanks for sharing the solution that worked for you. <code>slicer.util.getNode</code> is intended for quick testing and troubleshooting (as it accepts both name and node ID). For a more robust solution to get name of a selected volume, I would recommend to use <code>slicer.mrmlScene.GetNodeByID(myNode.GetID()).GetName()</code> or simply <code>myNodeComboBox.currentNode().GetName()</code>.</p>

---

## Post #13 by @lassoan (2023-01-16 21:53 UTC)

<p>2 posts were split to a new topic: <a href="/t/different-segmentation-export-function-produce-different-results/27279">Different segmentation export function produce different results</a></p>

---
