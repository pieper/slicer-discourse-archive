# Segmentation of multi volume sequence

**Topic ID**: 5187
**Date**: 2018-12-25
**URL**: https://discourse.slicer.org/t/segmentation-of-multi-volume-sequence/5187

---

## Post #1 by @Melanie (2018-12-25 06:52 UTC)

<p>Hi , I am trying to segment bone from 4D Ct - multivolume sequence. Because of the  displacement of bone from frame 1 to2 and thereafter , I cannot do one frame and do a registration. Looks like I have to manuallu segment each bone for each time point.<br>
My question is<br>
, how can I do that- when I segment on one frame- it automatically edits my other frames , where the bone is in a different position and the spatial dimensions are different. Can I segment each bone manually and save them while keeping there spatial dimensions, please.</p>

---

## Post #2 by @lassoan (2018-12-27 06:01 UTC)

<p>To allow segmenting each time point of the image, you need to create a segmentation sequence:</p>
<ul>
<li>Create a new Segmentation node (e.g., by segmenting image at one timepoint)</li>
<li>Go to Sequence browser module</li>
<li>Click the green “+” button next to “Create new sequence”. This creates a new sequence that will store the segmentation for each timepoint.</li>
<li>Choose your segmentation node in the “Proxy node” column in the table (last row). This indicates that this sequence will store states of the chosen segmentation node.</li>
<li>Check “Save changes” checkbox to allow modifying the sequence by editing the segmentation node.</li>
</ul>

---

## Post #3 by @Melanie (2018-12-27 06:15 UTC)

<p>Thank you very much Prof Lasso <a class="mention" href="/u/lassoan">@lassoan</a><br>
If I may ask, how would I mask other bones when doing a rigid registration of a single bone.</p>
<p>Following are my screenshots<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35be9ebf04c7324aac022043274cc6686eb937fd.png" alt="image" data-base62-sha1="7FrHS5u0cnI00b6nE9aVh7A5vat" width="350" height="230"><br>
Each tiny bone moves about 30-40 degree angle from the starting frame to the end in my volume sequence. I currently crop each bone using crop volume sequence but cropping does not completely eliminate the effect of other bones., especially when show significant displacement from frame 1 to say 20. I have to include a large area as my ROI when cropping.</p>
<p>Can I do some sort  of masking of other bones.</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2018-12-27 06:24 UTC)

<p>When bones are so close to each other then the mask would be about the bone itself.</p>
<p>Since you can segment these bones without too much difficulty using Grow from seeds effect with the <a href="https://discourse.slicer.org/t/new-segment-editor-feature-masking-in-grow-from-seeds-effect/4978">new masking feature</a>, a good approach could be to use “Segment registration” extension to register segments one by one.</p>

---

## Post #5 by @lassoan (2023-02-07 17:44 UTC)

<p>A post was split to a new topic: <a href="/t/edit-segmentation-sequence/27682">Edit segmentation sequence</a></p>

---
