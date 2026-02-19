---
topic_id: 22098
title: "How To Programmatically Create The Master Volume For A Segme"
date: 2022-02-22
url: https://discourse.slicer.org/t/22098
---

# How to programmatically create the Master Volume for a segmentation node with multiple segments

**Topic ID**: 22098
**Date**: 2022-02-22
**URL**: https://discourse.slicer.org/t/how-to-programmatically-create-the-master-volume-for-a-segmentation-node-with-multiple-segments/22098

---

## Post #1 by @PhilipDavis (2022-02-22 01:04 UTC)

<p>Hi there,<br>
I’m new to 3D Slicer and now I’m developing a Python scripting module.</p>
<p>Currently, I want to implement a procedure in python code of my module for calculating the volume value of the <strong>overlapping/Intersection</strong> part of two segments.<br>
As shown in the figure below, at the beginning I have two segmentation nodes, I set their color to red and green respectively:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fe2dc1e75c31bf339f1060ef9815df592370788.png" data-download-href="/uploads/short-url/6PCu8tzCuepN2yNb3GGiyGAYmPS.png?dl=1" title="Figure1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fe2dc1e75c31bf339f1060ef9815df592370788_2_517x198.png" alt="Figure1" data-base62-sha1="6PCu8tzCuepN2yNb3GGiyGAYmPS" width="517" height="198" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fe2dc1e75c31bf339f1060ef9815df592370788_2_517x198.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fe2dc1e75c31bf339f1060ef9815df592370788_2_775x297.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fe2dc1e75c31bf339f1060ef9815df592370788_2_1034x396.png 2x" data-dominant-color="838484"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Figure1</span><span class="informations">1267×488 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e89561f83b673965e4a07e8f83c9ec367ddd6fa2.png" data-download-href="/uploads/short-url/xbwP5NI2czWpYxzUsY40NwaKmwq.png?dl=1" title="Figure2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e89561f83b673965e4a07e8f83c9ec367ddd6fa2_2_517x204.png" alt="Figure2" data-base62-sha1="xbwP5NI2czWpYxzUsY40NwaKmwq" width="517" height="204" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e89561f83b673965e4a07e8f83c9ec367ddd6fa2_2_517x204.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e89561f83b673965e4a07e8f83c9ec367ddd6fa2_2_775x306.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e89561f83b673965e4a07e8f83c9ec367ddd6fa2_2_1034x408.png 2x" data-dominant-color="838383"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Figure2</span><span class="informations">1238×491 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And according to this post:<a href="https://discourse.slicer.org/t/calculating-shared-volume-between-two-models/10144/8">Calculating shared volume between two models</a>, here are the steps I followed to get the Intersection of two segments:</p>
<ol>
<li>
<p>Go to the ‘Segmentation’ module and use ‘Export/Import Models and Labelmaps’ to export the two segments to the ‘Models’ module to create two corresponding models:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2af7c857fad252dce42f97c5ca820950c757498.png" alt="Figure3" data-base62-sha1="ndbklhm3oAZgdDnghBpsX0JwRKg" width="480" height="258"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2116929c5e7df785b8c0048b4c2a4ee48cdef8b.png" alt="Figure4" data-base62-sha1="tYlzpSjyqiLlOAO8VHJQVqg2lCj" width="475" height="256"></p>
</li>
<li>
<p>Go to the ‘segmentation’ module and create a new segmentation node, I named it ‘<strong>NEW Segmentation</strong>’, and import both of models get from the previous step into this new segmentation node using the ‘Export/Import Models and Labelmaps’:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4ce18231599cdb27c8e7f08c99efad048ce96903.png" alt="Figure5" data-base62-sha1="aY7r8eSUTTmPR8q6IB8V49KQixt" width="462" height="293"></p>
</li>
<li>
<p>Go to the ‘<strong>Segmentation Editor</strong>’ module, switch the Segmentation node to ‘<strong>NEW Segmentation</strong>’, and now I notice that all effects are greyed out:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/4320ffd723b625b344ee3ef79370dfa3824069fd.png" alt="Figure6" data-base62-sha1="9zQGRA1b4TXK8Iq16c5nH74cle5" width="466" height="348"></p>
</li>
</ol>
<p>According to the example given by <a class="mention" href="/u/mikebind">@mikebind</a> in this post: <a href="https://discourse.slicer.org/t/how-to-programmatically-use-logical-operator-add-function-from-segment-editor/16581/2">How to programmatically use logical operator add function</a>, I found that in order to use the logical operator effect, which in my case is the ‘INTERSECT’ opreation, a master volume must be selected first, although I know I can create this Master Volume by clicking on the small “Specify geometry button” and selecting the ‘NEW Segmentation’ in the drop down box(the lowest option), but how to create the Master Volume for the ‘NEW Segmentation’ programmatically using python?</p>
<p>Thank you very much in advance!</p>

---

## Post #2 by @rbumm (2022-02-22 08:47 UTC)

<pre><code class="lang-auto">seg = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
</code></pre>
<p>adds an empty segmentation node to your scene.</p>

---

## Post #4 by @PhilipDavis (2022-02-22 17:47 UTC)

<p>Hello Rudolf,<br>
Thank you for your reply!</p>
<p>I’ve tried the code you provided. However, If I’m correct, this is actually the same as clicking the ‘Create new segmentation’ in the ‘Segmentations’ module, and this is how the ‘NEW segmentation’ I mentioned above with two segments was created:</p>
<blockquote>
<ol start="2">
<li>Go to the ‘segmentations’ module and create a new segmentation node, I named it ‘ <strong>NEW Segmentation</strong> ’, and import both of models get from the previous step into this new segmentation node using the ‘Export/Import Models and Labelmaps’</li>
</ol>
</blockquote>
<p>So, how to create the <strong>Master Volume</strong> for the ‘NEW Segmentation’ programmatically using python? Because after I create this Master Volume for the ‘NEW Segmentation’, I can execute code similar to the following to use logical operator effects and the ‘INTERSECT’ operation:</p>
<blockquote>
<p>segmentationNode = getNode(‘NEW Segmentation’)<br>
<strong>masterVolume = segmentationNode.GetNodeReference(slicer.vtkMRMLSegmentationNode().GetReferenceImageGeometryReferenceRole())</strong><br>
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()<br>
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)<br>
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSegmentEditorNode”)<br>
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)<br>
segmentEditorWidget.setSegmentationNode(segmentationNode)<br>
segmentEditorWidget.setMasterVolumeNode(masterVolume)<br>
tgt = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(‘RED’)<br>
src = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(‘GREEN’)<br>
segmentEditorNode.SetSelectedSegmentID(tgt)<br>
segmentEditorWidget.setActiveEffectByName(“Logical operators”)<br>
effect = segmentEditorWidget.activeEffect()<br>
effect.setParameter(“Operation”,“INTERSECT”)<br>
effect.setParameter(“ModifierSegmentID”,src)<br>
effect.self().onApply()</p>
</blockquote>

---

## Post #5 by @rbumm (2022-02-22 18:11 UTC)

<p>You can either get the volume node from an MRML node like</p>
<pre><code class="lang-auto">volumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")
</code></pre>
<p>or create a new one like</p>
<pre><code class="lang-auto">volumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
</code></pre>
<p>Check out the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a> for more examples.</p>

---

## Post #6 by @PhilipDavis (2022-02-22 19:21 UTC)

<p>Thank you so much, it’s working now <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @Aboma_Negasa_Guracho (2022-02-25 10:19 UTC)

<p>Thank you so much, it’s working now!</p>

---
