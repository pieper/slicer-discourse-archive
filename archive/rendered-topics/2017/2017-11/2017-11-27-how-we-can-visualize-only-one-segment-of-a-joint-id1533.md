---
topic_id: 1533
title: "How We Can Visualize Only One Segment Of A Joint"
date: 2017-11-27
url: https://discourse.slicer.org/t/1533
---

# how we can visualize only one segment of a joint

**Topic ID**: 1533
**Date**: 2017-11-27
**URL**: https://discourse.slicer.org/t/how-we-can-visualize-only-one-segment-of-a-joint/1533

---

## Post #1 by @shrimanti (2017-11-27 18:32 UTC)

<p>I have DICOM image of the knee joint and it has Femur, Patella, Tibia, Fibula. But if I want to show only one part say Patella in the 3D view of Slicer, how can I do that?</p>

---

## Post #2 by @lassoan (2017-11-28 03:23 UTC)

<p>You need to segment your volume. You can use Segment editor to do it manually/semi-automatically. Create separate segment for each part that you want to show/hide separately.</p>
<p>You can also find an example of a knee segmentation in the DataStore module (Atlas collection category / SPL Knee atlas):</p>
<p><a href="http://www.spl.harvard.edu/publications/item/view/1953" class="onebox" target="_blank">http://www.spl.harvard.edu/publications/item/view/1953</a></p>

---

## Post #3 by @shrimanti (2017-11-29 18:14 UTC)

<p>Thank you so much for your reply.<br>
We can segment each part separately but can we delete one part from the 3D view?</p>

---

## Post #4 by @lassoan (2017-11-29 18:37 UTC)

<p>You can show/hide individual segments in a selected view by adjusting options in Segmentations module / Display / Advanced section.</p>

---

## Post #5 by @shrimanti (2017-11-29 23:51 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f3c8703964ef178cb3ee4cfdf1ac56112e172eb.jpeg" data-download-href="/uploads/short-url/fS2G4qX1gNxpR8a2PM0l4QVVls7.JPG?dl=1" title="final1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6f3c8703964ef178cb3ee4cfdf1ac56112e172eb_2_452x500.JPG" alt="final1" data-base62-sha1="fS2G4qX1gNxpR8a2PM0l4QVVls7" width="452" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6f3c8703964ef178cb3ee4cfdf1ac56112e172eb_2_452x500.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6f3c8703964ef178cb3ee4cfdf1ac56112e172eb_2_678x750.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f3c8703964ef178cb3ee4cfdf1ac56112e172eb.jpeg 2x" data-dominant-color="73728A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">final1</span><span class="informations">794×878 64.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>So, I have segmented each part but I am not able to delete one or two particular bones.</p>

---

## Post #6 by @lassoan (2017-11-30 02:21 UTC)

<p>Did you use Segment Editor module or Editor module?<br>
Would you like to permanently delete a segment or just show/hide a segment?</p>

---

## Post #7 by @shrimanti (2017-11-30 02:58 UTC)

<p>I used the Editor module, not the Segment Editor.<br>
I want to hide/show one segment from the 3D view. I couldn’t figure out how to show/hide that in Segmentation module. I don’t think there is any tutorial for that.<br>
Could you please guide me through the steps if possible?<br>
Thank you.</p>

---

## Post #8 by @lassoan (2017-11-30 03:48 UTC)

<aside class="quote no-group" data-username="shrimanti" data-post="7" data-topic="1533">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/8491ac/48.png" class="avatar"> shrimanti:</div>
<blockquote>
<p>I used the Editor module, not the Segment Editor.</p>
</blockquote>
</aside>
<p>That’s the problem. The legacy Editor module is kept in Slicer for backward compatibility only. Use Segment Editor instead. You can import the labelmap created in the Editor module into a segmentation by using Segmentations module Import section.</p>

---
