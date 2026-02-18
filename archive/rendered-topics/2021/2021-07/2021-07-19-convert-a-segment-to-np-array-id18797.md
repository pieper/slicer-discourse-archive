# Convert a segment to np array

**Topic ID**: 18797
**Date**: 2021-07-19
**URL**: https://discourse.slicer.org/t/convert-a-segment-to-np-array/18797

---

## Post #1 by @Guillaume (2021-07-19 11:55 UTC)

<p>Hello, I am doing an extension with Slicer 14.11 on windows in Python. So, I try to import the segmentation directly with. It gets stuck at the time of import (for the selection everything works) and convertion.</p>
<p>I used this helper: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#read-and-write-a-segment-as-a-numpy-array" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a><br>
With :</p>
<pre><code class="lang-auto">volumeNode = slicer.util.getNode('MRHead')
segmentationNode = slicer.util.getNode('Segmentation')
segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName('Segment_1')

segmentArray = slicer.util.arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId, volumeNode)
</code></pre>
<p>But slicer told me :</p>
<pre><code class="lang-auto">slicer.util.MRMLNodeNotFoundException: could not find nodes in the scene by name or id 'MRHead'
</code></pre>
<p>So I changed by:</p>
<pre><code class="lang-auto">volumeNode = slicer.mrmlScene.GetNodeByID('MRHead')
segmentationNode = slicer.mrmlScene.GetNodeByID('Segementation')
segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName('Segment_1')

mask = slicer.util.arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId, volumeNode)
</code></pre>
<p>But:</p>
<pre><code class="lang-auto">AttributeError: 'NoneType' object has no attribute 'GetSegmentation'
</code></pre>
<p>Thanks for your help ! Many topics have already helped me a lot.</p>

---

## Post #2 by @riep (2021-07-19 13:12 UTC)

<p>Hi Guillaume,<br>
You have to first import the volume “MRHead” using the “sample data” module and do a segmentation with the segmentation module, before calling slicer.util.getNode functions.<br>
Pierre</p>

---

## Post #3 by @Guillaume (2021-07-19 14:26 UTC)

<p>Hi Pierre,<br>
Thank you for your answer.</p>
<p>“GetNode” is not for picking up a module? If so, why is there a need for SampleData?</p>

---

## Post #4 by @lassoan (2021-07-19 15:20 UTC)

<p>You need to replace <code>MRHead</code> with the actual name of your volume.</p>

---

## Post #5 by @Guillaume (2021-07-19 15:45 UTC)

<p>Oh okay, I didn’t understand it like that ! Thank’s a lot !</p>
<p>But I do that:</p>
<pre><code class="lang-auto">volumeNode = slicer.mrmlScene.GetNodeByID('IMG_001')
segmentationNode = slicer.mrmlScene.GetNodeByID('MASK_001')
segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName('Segment_1')
</code></pre>
<p>And Slicer told me:</p>
<pre><code class="lang-auto">AttributeError: 'NoneType' object has no attribute 'GetSegmentation'
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/faa806f33b52ec4d153dbbd4b658854807ff8da2.png" data-download-href="/uploads/short-url/zLpmzFDV0zRdO2NHBDJgURKEkCu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/faa806f33b52ec4d153dbbd4b658854807ff8da2.png" alt="image" data-base62-sha1="zLpmzFDV0zRdO2NHBDJgURKEkCu" width="517" height="500" data-dominant-color="F7F9FB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">555×536 8.11 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2021-07-19 16:02 UTC)

<p><code>GetNodeByID</code> gets a node by node ID, not by node name. Node name is displayed for users and it is not required to be unique. You can get the first node in the scene by the specified name by using <code>GetFirstNodeByName</code> method, but for interactive use in the Python console, I would recommend to use <code>getNode</code> method because it can take either node name or ID as input and throws an exception if the node is not found (instead of just returning None, so that you only find out that you did not get the node when you try to access its methods). This is all described in detail <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-mrml-node-from-the-scene">here</a>.</p>

---

## Post #7 by @Guillaume (2021-07-19 16:26 UTC)

<p>Okay, thank you. It works ! But…</p>
<pre><code class="lang-auto">TypeError: arrayFromSegmentBinaryLabelmap() takes 2 positional arguments but 3 were given
</code></pre>
<p><img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=9" title=":sob:" class="emoji only-emoji" alt=":sob:"></p>
<p>It work without “volumeNode”… Is it ok ?</p>

---

## Post #8 by @lassoan (2021-07-19 16:42 UTC)

<p>List of input arguments to this helper function has changed a few times over the last 1-2 years, so I don’t know what arguments are needed in the Slicer version that you use. You can run<code>help(object.methodname)</code> to display the method’s documentation.</p>

---

## Post #9 by @Guillaume (2021-07-20 06:58 UTC)

<p>Okay, thank you for your help !</p>
<p>And here is the help:</p>
<pre><code class="lang-auto">arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId)
</code></pre>

---

## Post #11 by @lassoan (2021-07-20 11:53 UTC)

<p>I would recommend to use the latest Slicer Preview Release, because there <code>arrayFromSegmentBinaryLabelmap</code> returns an array that has the same geometry as the first selected master volume, while earlier the array was cropped to the minimum required size, which was a bit more complicated than the use.</p>
<p>“Latest” documentation at the link <a href="https://slicer.readthedocs.io/en/latest/">https://slicer.readthedocs.io/en/latest/</a> is for the latest Slicer Preview Release. Therefore, all the examples in the script repository page work in the latest Slicer Preview Release. You can find documentation for the current stable release (4.11) at <a href="https://slicer.readthedocs.io/en/v4.11/">https://slicer.readthedocs.io/en/v4.11/</a>.</p>

---
