---
topic_id: 22873
title: "I Want To Obtain The X Y Coordinates Of The Regions I Have S"
date: 2022-04-08
url: https://discourse.slicer.org/t/22873
---

# I want to obtain the x, y coordinates of the regions I have segmented

**Topic ID**: 22873
**Date**: 2022-04-08
**URL**: https://discourse.slicer.org/t/i-want-to-obtain-the-x-y-coordinates-of-the-regions-i-have-segmented/22873

---

## Post #1 by @aysegul_sayin (2022-04-08 13:19 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/049f59e064f528df429d4f08d32364fad07f6f1a.png" data-download-href="/uploads/short-url/ETjInvh5d2E4ckXhhZeoCYKfyi.png?dl=1" title="Screenshot_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/049f59e064f528df429d4f08d32364fad07f6f1a_2_690x351.png" alt="Screenshot_1" data-base62-sha1="ETjInvh5d2E4ckXhhZeoCYKfyi" width="690" height="351" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/049f59e064f528df429d4f08d32364fad07f6f1a_2_690x351.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/049f59e064f528df429d4f08d32364fad07f6f1a_2_1035x526.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/049f59e064f528df429d4f08d32364fad07f6f1a.png 2x" data-dominant-color="CECDCB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_1</span><span class="informations">1311×667 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I want to obtain the x, y coordinates of the regions I have segmented and the information on which section they are in. In what format should I save the segmentation and how can I get this coordinate information?</p>

---

## Post #2 by @lassoan (2022-04-09 10:32 UTC)

<p>Storing a segmentation as a list of coordinates is an extremely inefficient representation. How would you use these coordinates?</p>

---

## Post #3 by @DIV (2022-04-10 22:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="22873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Storing a segmentation as a list of coordinates is an extremely inefficient representation.</p>
</blockquote>
</aside>
<p>True, but it would be easier to understand if inspecting ‘manually’, and also easier to write code to process.<br>
—DIV</p>

---

## Post #4 by @lassoan (2022-04-11 01:26 UTC)

<p>Indices are rarely useful for manual inspection, as even small structures consists of thousands of voxels (e.g., a tiny 10x10x10 structure = 1000 voxels), which is just too tedious to review manually. Image processing algorithms don’t operate on voxel indices representation, so I don’t see how it could help with any processing (unless you want to process your images with text processing algorithms?).</p>
<p>I did not want to tell <a class="mention" href="/u/aysegul_sayin">@aysegul_sayin</a> to just go and use <code>numpy.where</code> to get those indices, because most likely that would have lead to a dead end or suboptimal solution. Instead, I tried to understand what her overall goal was and find the best way to achieve that.</p>

---

## Post #5 by @aysegul_sayin (2022-04-11 08:19 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/701df2d6b7a16f4c5a440c8764b5e5e152500def.png" alt="image" data-base62-sha1="fZPDKWRjVEfSBQAR4nZfiYmheKX" width="690" height="139"></p>
<p>Hello, first of all thank you for your replies.<br>
Actually, my goal is to reach the coordinate information of a segmented structure, for example a tumor. I’ve read and tried before on the forum that we can do this with the following code block. (I’m a bit of a newbie at Slicer so sorry if I said anything wrong). The values I got as numpy format from here were the values corresponding to the field that says Red.What do the values in the place called Red mean here? However, what I want is the x,y,z, coordinate information in my own MR image.</p>

---

## Post #6 by @lassoan (2022-04-11 15:17 UTC)

<p>You can get voxels of a segmentation as a numpy array as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#read-and-write-a-segment-as-a-numpy-array">examples in the script repository</a>.</p>
<p>“Red” means that the mouse pointer is over the “Red” view. You can ignore this information. Content displayed in the Data Probe is documented <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#data-probe">here</a>.</p>
<aside class="quote no-group" data-username="aysegul_sayin" data-post="5" data-topic="22873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aysegul_sayin/48/14944_2.png" class="avatar"> aysegul_sayin:</div>
<blockquote>
<p>my goal is to reach the coordinate information of a segmented structure, for example a tumor</p>
</blockquote>
</aside>
<p>What exactly do you need? Anatomical coordinates of the segmented tumor’s center?</p>

---
