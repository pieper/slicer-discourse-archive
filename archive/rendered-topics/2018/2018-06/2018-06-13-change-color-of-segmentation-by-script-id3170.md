# Change Color of Segmentation by Script

**Topic ID**: 3170
**Date**: 2018-06-13
**URL**: https://discourse.slicer.org/t/change-color-of-segmentation-by-script/3170

---

## Post #1 by @trnhx001 (2018-06-13 15:09 UTC)

<p>Operating system: Window 7<br>
Slicer version: 4.8.1</p>
<p>Hi,</p>
<p>I am trying to write a program to load two segmentation of Carotid done by two different people on the same volume, then I want to save images of all slices from axial view to a folder.</p>
<p>I could do most of the thing except changing the color of the segmentations. The reason is that I want to compare between two segmentations. It is hard to compare them when they are in the same color.</p>
<p>Is there anyway to write a script to change the color of the finished segmentation? I tried the below code, but it seems like it does not work this way:</p>
<p>segmentationNode = getNode(‘Segmentation’)<br>
segmentationNode.SetColor(1,1,0)</p>
<p>or</p>
<p>segmentationDisplayNode = segmentationNode.GetDisplayNode()<br>
segmentationDisplayNode.SetColor(1,1,0)</p>
<p>Thank you for all of your help.</p>

---

## Post #2 by @lassoan (2018-06-13 19:28 UTC)

<p>You need to set color for individual segments. For example, set first segment color to red:</p>
<pre><code>segmentation = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLSegmentationNode').GetSegmentation()
segmentation.GetNthSegment(0).SetColor(1,0,0)</code></pre>

---

## Post #3 by @Saima (2021-09-13 23:00 UTC)

<p>Hi Andras,<br>
I am setting color like this<br>
scalpSeg =  segmentationNode.GetSegmentation().GetSegment(scalpSelector)<br>
scalpSeg.SetColor(255,192,203)<br>
but its not working even if I change the color values. Not giving any error. code is working but cant visualize in the segment editor window</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #4 by @jamesobutler (2021-09-13 23:52 UTC)

<p>I believe setting segment color takes values from 0 to 1 where 255 is equivalent to 1. So setting to 255,192,203 is actually setting it to 1,1,1.</p>

---

## Post #5 by @Saima (2021-09-14 03:49 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="4" data-topic="3170">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>0 to 1</p>
</blockquote>
</aside>
<p>Hi,<br>
If I have red =255<br>
green = 192<br>
and yellow = 203</p>
<p>so what will be the values in o to 1 range.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #6 by @mau_igna_06 (2021-09-14 21:29 UTC)

<p>You have to divide each of the colors by 255</p>

---
