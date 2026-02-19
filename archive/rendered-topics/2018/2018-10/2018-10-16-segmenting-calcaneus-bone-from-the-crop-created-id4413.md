---
topic_id: 4413
title: "Segmenting Calcaneus Bone From The Crop Created"
date: 2018-10-16
url: https://discourse.slicer.org/t/4413
---

# Segmenting Calcaneus bone from the crop created

**Topic ID**: 4413
**Date**: 2018-10-16
**URL**: https://discourse.slicer.org/t/segmenting-calcaneus-bone-from-the-crop-created/4413

---

## Post #1 by @SRIKESH (2018-10-16 13:13 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.8.1</p>
<p>Hello everyone,<br>
I am trying to segment the calcaneus bone from the ankle for my project work. I have tried to crop it down as much as possible. Now there are few other bones adjacent to the calcaneus which I don’t want.<br>
<a href="/404" data-orig-href="upload://iKmwfEMWNlbz6UnIeceChlG6ftP.jpeg">Calcaneus|660x499</a> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/642db421dafa8972e89575c8d7e8f560a103d836.jpeg" data-download-href="/uploads/short-url/eidFkAgF4zvW4dfhgdRpE2YmcrI.jpeg?dl=1" title="Calcaneus1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/642db421dafa8972e89575c8d7e8f560a103d836_2_655x500.jpeg" alt="Calcaneus1" data-base62-sha1="eidFkAgF4zvW4dfhgdRpE2YmcrI" width="655" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/642db421dafa8972e89575c8d7e8f560a103d836_2_655x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/642db421dafa8972e89575c8d7e8f560a103d836.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/642db421dafa8972e89575c8d7e8f560a103d836.jpeg 2x" data-dominant-color="686A61"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Calcaneus1</span><span class="informations">802×612 56.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I tried to segment using “Paint” in segment editor but I am not able to clearly distinguish the boundary of Calcaneus bone.</p>
<p>Can anyone suggest me how to go about it? Any help would be much appreciated.<br>
Thanks in advance !!</p>
<p>P.S: Also can anyone suggest me where can I get CT scans of Calcaneus fracture</p>

---

## Post #2 by @lassoan (2018-10-16 13:52 UTC)

<p>You can often separate bones by painting a different segment inside each bone (and one segment in the background - air and soft tissues) and then use “Grow from seeds” effect to create a complete segmentation. Similarly to how it is done to segment different heart ventricles as shown in <a href="https://youtu.be/BJoIexIvtGo">this video tutorial</a>.</p>
<p>Another approach is to use scissors tool to reassign part of a segment to a different segment, as shown in <a href="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/">this tutorial</a>.</p>
<aside class="quote no-group" data-username="SRIKESH" data-post="1" data-topic="4413">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/53a042/48.png" class="avatar"> SRIKESH:</div>
<blockquote>
<p>P.S: Also can anyone suggest me where can I get CT scans of Calcaneus fracture</p>
</blockquote>
</aside>
<p>Your clinical collaborator should be able to provide you images. Clinical collaborator is not just needed for images but also for ensuring that you focus on the right problem and come up with solutions that are applicable in clinical practice.</p>

---

## Post #3 by @SRIKESH (2018-10-17 08:51 UTC)

<p>Thanks for the reply.<br>
I have tried segmentation with “Grow from seeds”. I am attaching a pic below. As you can see, the calcaneus is segmented but its not in the exact shape. My project is to model a calcaneus bone,design it for 3D printing for implementation in surgeries. So I need an exact shape for this.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73762ee63e8db5dcae1527a6b2a563f676e73480.jpeg" data-download-href="/uploads/short-url/gtq79KVZnPSWaKC6WZd0g9GQhqg.jpeg?dl=1" title="Calcaneus2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/73762ee63e8db5dcae1527a6b2a563f676e73480_2_659x500.jpeg" alt="Calcaneus2" data-base62-sha1="gtq79KVZnPSWaKC6WZd0g9GQhqg" width="659" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/73762ee63e8db5dcae1527a6b2a563f676e73480_2_659x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73762ee63e8db5dcae1527a6b2a563f676e73480.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73762ee63e8db5dcae1527a6b2a563f676e73480.jpeg 2x" data-dominant-color="5C6365"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Calcaneus2</span><span class="informations">806×611 45 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>So can you suggest me what needs to be done. I am looking for something like this</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b5f71a69adf35f04750e3fa8552c326a9a6a872.jpeg" alt="Capture" data-base62-sha1="1CBJS8PI6af653aQgwK7PgxdQnE" width="230" height="206"></p>
<p>Thanks !!</p>

---

## Post #4 by @pieper (2018-10-17 11:55 UTC)

<p>It looks like you are very close on the segmentation.  The key point about grow from seeds is that you can apply it and then undo a few steps and try again with different input.  Here you have a little oversegmentation and a little undersegmentation, so you need to go back and add a few more positive and negative strokes of input as ‘hints’ for the GrowCut algorithm (google growcut for lots of tutorials and examples).</p>
<p>Regarding the result, do you need those dimples?  That would be a distinct step once the basic segmentation is right.</p>

---

## Post #5 by @SRIKESH (2018-10-17 12:15 UTC)

<p>Thanks for the suggestion… I will go through the algorithm and get back to you.<br>
As for the result, no I don’t need the dimples on the surface…that’s a later step. I was just referring to the shape of bone.</p>

---

## Post #6 by @lassoan (2018-10-17 12:35 UTC)

<p>Yes, it is expected that initial seeds will not result in perfect segmentation. You need to paint further strokes using Paint effect in places where you would like to change segmentation result. Segmentation result is updated automatically in a few seconds.</p>
<p>This is all explained in details in the cardiac CT segmentation tutorial that I referred to above.</p>

---
