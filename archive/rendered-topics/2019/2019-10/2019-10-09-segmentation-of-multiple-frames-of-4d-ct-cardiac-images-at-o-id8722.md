---
topic_id: 8722
title: "Segmentation Of Multiple Frames Of 4D Ct Cardiac Images At O"
date: 2019-10-09
url: https://discourse.slicer.org/t/8722
---

# Segmentation of multiple frames of 4D CT Cardiac Images at once

**Topic ID**: 8722
**Date**: 2019-10-09
**URL**: https://discourse.slicer.org/t/segmentation-of-multiple-frames-of-4d-ct-cardiac-images-at-once/8722

---

## Post #1 by @faisal03 (2019-10-09 15:24 UTC)

<p>Hello!<br>
I have dicom CT cardiac data and I have used a MATLAB script which separates it into 20 time frames (labeled dt1, dt2, dt3, etc.). This is for each patient.</p>
<p>How do I segment out the heart in all the time frames at one go instead of loading each time frame and segmenting it out separately 20 times?? The difference between the images in each time frame is not that much different.</p>
<p>I do believe this is possible using the Sequence extension but I do not know how to!</p>

---

## Post #2 by @lassoan (2019-10-09 22:09 UTC)

<p>There should be no need to split the original DICOM series in Matlab. Install sequences module, import the DICOM files into the DICOM database using DICOM module, then load it as a volume sequence (if it is loaded by default as a MultiVolume then go to menu: Edit / Application settings / DICOM / Preferred multi-volume import format -&gt; volume sequence).</p>
<p>You can segment the CT at one timepoint and warp the segmentation to all other timepoints using Sequence Registration module as described in this topic: <a href="https://discourse.slicer.org/t/load-multiple-cardiac-phases-for-segmentation-virtual-reality/5214" class="inline-onebox">Load multiple cardiac phases for segmentation/virtual reality</a></p>

---

## Post #3 by @faisal03 (2019-10-10 15:44 UTC)

<p>Hi ! Thank you for the reply but for some reason I am unable to do the sequence browser selection. When I choose my segmentation node after creating a new sequence, the master node is also changed to that node itself. Also, master has renaming automatically checked which always points to the current time frame in squared brackets.</p>
<p>How to actually choose the segmentation node and the master and then go with registration? Also during the registration what should be chosen as ‘Input volume sequence’, ‘Output volume sequence’ and ‘Output transform sequence’?? Please do let me know. Thank you.</p>

---

## Post #4 by @lassoan (2019-10-13 12:10 UTC)

<p>In Sequence browser module, you need to select the browser node of the already loaded image sequence. This browser node already contains a synchronized node, which is the master node. You need to add a new sequence to this and choose the segmentation node as proxy node.</p>

---

## Post #5 by @faisal03 (2019-10-15 10:31 UTC)

<p>I cannot see the the name of the segmentation node in the list. All I see is ‘Segmentation’. Do I have to select that as proxy node for the new sequence??</p>
<p>Also, I do not know what to choose as the ‘Input volume sequence’, ‘Output volume sequence’ and ‘Output transform sequence’ in the Sequence registration???</p>

---

## Post #6 by @lassoan (2019-10-16 04:21 UTC)

<aside class="quote no-group" data-username="faisal03" data-post="5" data-topic="8722">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/faisal03/48/4903_2.png" class="avatar"> faisal03:</div>
<blockquote>
<p>I cannot see the the name of the segmentation node in the list. All I see is ‘Segmentation’. Do I have to select that as proxy node for the new sequence??</p>
</blockquote>
</aside>
<p>Yes.</p>
<aside class="quote no-group" data-username="faisal03" data-post="5" data-topic="8722">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/faisal03/48/4903_2.png" class="avatar"> faisal03:</div>
<blockquote>
<p>Also, I do not know what to choose as the ‘Input volume sequence’, ‘Output volume sequence’ and ‘Output transform sequence’ in the Sequence registration???</p>
</blockquote>
</aside>
<ul>
<li>Input volume sequence: the 4D CT you loaded from DICOM</li>
<li>Output volume sequence: optional. If you choose to create a new sequence for output volume sequence and select it in the node selector then you’ll get the transformed input volume sequence in this node.</li>
<li>Output transform sequence: create a new sequence and select it. This transform sequence will contain the transforms that warp the selected input frame to all other frames.</li>
</ul>

---
