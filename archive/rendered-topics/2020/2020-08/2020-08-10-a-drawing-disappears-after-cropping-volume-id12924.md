# A drawing disappears after Cropping Volume

**Topic ID**: 12924
**Date**: 2020-08-10
**URL**: https://discourse.slicer.org/t/a-drawing-disappears-after-cropping-volume/12924

---

## Post #1 by @whirl (2020-08-10 12:52 UTC)

<p>Hello,<br>
I try to segment femoral cartilage. To do so, firstly I crop volume containing the area and then try to segment the cartilage using “Draw”. The problem is that I’m unable to do it - it disappears. A painting option works - it marks the area.<br>
Could you help me?</p>

---

## Post #2 by @lassoan (2020-08-10 13:25 UTC)

<p>This could happen when the slice view is positioned right at the boundary between two slices. This is not likely to happen if you use latest Slicer Preview Release. If you the issue is not resolved then let us know and we can give further advice.</p>

---

## Post #3 by @lassoan (2021-05-20 12:18 UTC)

<p>2 posts were split to a new topic: <a href="/t/cannot-paint-segments-on-video/17710">Cannot paint segments on video</a></p>

---

## Post #4 by @caesarsalad (2021-05-21 04:44 UTC)

<p>Hello,</p>
<p>As a follow up is it possible to save the 2D annotations into a .json file? I wish to use the annotations to train a model.</p>
<p>Thanks as always <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #5 by @lassoan (2021-05-21 04:48 UTC)

<p>You can get voxels of a segment as a numpy array by calling <code>slicer.util.arrayFromSegment</code> (see an example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-centroid-of-a-segment-in-world-ras-coordinates">here</a>) and save it in any file format you like.</p>

---

## Post #6 by @caesarsalad (2021-05-21 05:47 UTC)

<p>I’ve looked over the code but can’t quite understand.<br>
I used the segmentation editor tool to draw annotations free handedly, and it seems like 3d slicer saves them in .nrrd by default. Does the call also work for shapes that are not a fixed polygon?</p>

---

## Post #7 by @caesarsalad (2021-05-21 07:12 UTC)

<p>Also quite relatively new to programming in Python, I would appreciate it if you could guide me through how to save the freehand annotations (2D) into a json file format. I appreciate your time sir.</p>

---

## Post #8 by @caesarsalad (2021-05-21 08:26 UTC)

<p>For clarity, I wish to obtain the coordinates of the annotated region that I drew free-hand. Would such a thing be possible?</p>

---

## Post #9 by @lassoan (2021-05-21 12:33 UTC)

<aside class="quote no-group" data-username="caesarsalad" data-post="7" data-topic="12924">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/ecae2f/48.png" class="avatar"> caesarsalad:</div>
<blockquote>
<p>Also quite relatively new to programming in Python, I would appreciate it if you could guide me through how to save the freehand annotations (2D) into a json file format.</p>
</blockquote>
</aside>
<p>JSON just specifies low-level syntax for data storage but it does not tell what you store and exactly how. You need to choose a commonly used file format for storing the segmentation result.</p>
<aside class="quote no-group" data-username="caesarsalad" data-post="8" data-topic="12924">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/ecae2f/48.png" class="avatar"> caesarsalad:</div>
<blockquote>
<p>For clarity, I wish to obtain the coordinates of the annotated region that I drew free-hand.</p>
</blockquote>
</aside>
<p>This does not sound right. It is not likely that you need a polygonal representation as input for CNN. If you mean that you would like to encode the segmentation by storing coordinate of each pixel that would be very wasteful and I don’t think it is commonly used for CNN input.</p>
<p>I would recommend to check out <a href="https://monai.io/">MONAI</a> tutorials for learning how to train models for medical image segmentation. Since you work with RGB camera images, you can use computer vision deep learning tutorials, too.</p>

---
