# Creating Histograms From Segments 

**Topic ID**: 22297
**Date**: 2022-03-03
**URL**: https://discourse.slicer.org/t/creating-histograms-from-segments/22297

---

## Post #1 by @benwilk (2022-03-03 21:54 UTC)

<p>I’ve been trying to follow the code found <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region" rel="noopener nofollow ugc">here</a> to create a histogram from my existing MR and existing segmentation. I read on another post that I need to change the volume node and segmentation node so I have the code below, after multiple errors:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; volumeNode = getNode("Volume1")

&gt;&gt;&gt; segmentationNode = getNode("Segmentation")

&gt;&gt;&gt; segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(volumeNode)

&gt;&gt;&gt; segmentID = "Segment_1"

&gt;&gt;&gt; import numpy as np

&gt;&gt;&gt; volumeArray = slicer.util.arrayFromVolume(volumeNode)

&gt;&gt;&gt; segmentArray = arrayFromSegment(segmentationNode, segmentID)

&gt;&gt;&gt; segmentVoxels = volumeArray[segmentArray != 0]

Traceback (most recent call last):

File "&lt;console&gt;", line 1, in &lt;module&gt;

IndexError: boolean index did not match indexed array along dimension 0; dimension is 112 but corresponding boolean dimension is 61

If anyone could tell me what I'm missing that would be fantastic! Unfortunately, I have no experience with python... 

Thanks!
Ben</code></pre>

---

## Post #2 by @mikebind (2022-03-04 19:27 UTC)

<p>You need to use</p>
<pre><code class="lang-auto">segmentArray = slicer.util.arrayFromSegmentBinaryLabelmap(segmentationNode, segmentID, volumeNode)
</code></pre>
<p>Using this version ensures that the <code>segmentArray</code> is the same size as the <code>volumeArray</code> of <code>volumeNode</code>. The error you ran into is because the <code>segmentArray</code> is a different size than the <code>volumeArray</code>, so you can’t use it to properly index into <code>volumeArray</code> because it is not clear what the corresponding locations are.</p>

---

## Post #3 by @benwilk (2022-03-07 15:15 UTC)

<p>Thank you for your reply! When I try that, I get the following error:<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
AttributeError: ‘module’ object has no attribute ‘arrayFromSegmentBinaryLabelmap’</p>

---

## Post #4 by @mikebind (2022-03-07 16:18 UTC)

<p>What version of Slicer are you using?  If you upgrade to a recent preview release, that function will be present.  It was also used in the example you were following (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region" class="inline-onebox">Script repository — 3D Slicer documentation</a>).  I would guess that you are using an older version of Slicer where the <code>arrayFromSegmentBinaryLabelmap</code> function had not been added yet.</p>

---

## Post #5 by @SHADI (2023-05-20 19:51 UTC)

<p>Hi 3Dslicer community, I am trying to create a histogram from an existing segment by 3dslicer 5.2.2 and this code did not work. Your helps will be greatly appreciated.</p>

---
