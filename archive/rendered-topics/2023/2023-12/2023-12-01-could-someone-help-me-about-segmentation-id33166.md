---
topic_id: 33166
title: "Could Someone Help Me About Segmentation"
date: 2023-12-01
url: https://discourse.slicer.org/t/33166
---

# Could someone help me about segmentation?

**Topic ID**: 33166
**Date**: 2023-12-01
**URL**: https://discourse.slicer.org/t/could-someone-help-me-about-segmentation/33166

---

## Post #1 by @S_Esmaeili (2023-12-01 18:17 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b150bb7e896019a5cdb91567c1b83966e89dfbc0.jpeg" data-download-href="/uploads/short-url/piBtNzrrgscZnJP42YH0pyMMY1i.jpeg?dl=1" title="slicer1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b150bb7e896019a5cdb91567c1b83966e89dfbc0.jpeg" alt="slicer1" data-base62-sha1="piBtNzrrgscZnJP42YH0pyMMY1i" width="690" height="424" data-dominant-color="5F6368"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer1</span><span class="informations">869×534 47.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03f14f6966491df60b0a0abb821c96718078b0f0.jpeg" data-download-href="/uploads/short-url/ySr6lsiktEoD2YIz2VtaGRWcTK.jpeg?dl=1" title="slicer2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03f14f6966491df60b0a0abb821c96718078b0f0.jpeg" alt="slicer2" data-base62-sha1="ySr6lsiktEoD2YIz2VtaGRWcTK" width="690" height="381" data-dominant-color="686B6D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer2</span><span class="informations">891×493 41.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>i defined my segmentation over the first image and want to use it for other images too. but when i load new images the segment boxes of the pervious image appear in the new image.</p>

---

## Post #2 by @muratmaga (2023-12-01 18:19 UTC)

<p>Please read these tutorials to make yourself familiar with the UI and controls. You can turn off/on any segmentation visibility using Data module.<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">Image Segmentation — 3D Slicer documentation</a></p>
<p>and<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html">Segmentations — 3D Slicer documentation</a></p>

---

## Post #3 by @S_Esmaeili (2023-12-01 19:58 UTC)

<p>Thanks, i have tried to follow the steps in segmentation instructions but my problem is not solved.</p>

---

## Post #4 by @muratmaga (2023-12-01 19:59 UTC)

<p>You need to turnoff the previous segmentation.</p>

---

## Post #5 by @mikebind (2023-12-01 20:36 UTC)

<p>It looks like you may be working with data in a Sequence (judging by the Sequence Browser toolbar in your screenshots).  This can be confusing until you understand how the Sequence system is set up and the relationships between Sequences, Sequence Browsers, and Proxy Nodes work.  I am guessing that you may want to perform a segmentation on each frame of a sequence of images; if so, it might be helpful to follow the sequence of steps here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/sequences.html#create-a-segmentation-node-sequence">https://slicer.readthedocs.io/en/latest/user_guide/modules/sequences.html#create-a-segmentation-node-sequence</a></p>
<p>The very brief overview is that Sequences are ordered sets of similar data objects (such as a temporal sequence of image volumes).  A Sequence Browser can be linked to a Sequence to allow you to select which of the sequence’s data objects is the “current” one and should be displayed.  The current data object is copied into a designated node which is already in the MRML Scene; this node is the Proxy Node for that Sequence and Sequence Browser combination. As long as two Sequences have the same number of objects and are indexed in the same way, they can both be linked to the same Sequence Browser, and you can browse through both of them simultaneously (e.g. a sequence of image volumes and a sequence of segmentations of those image volumes). One important thing to note is that you generally need to make sure that the “Save Changes” checkbox in the Sequences module is checked for each sequence where you may want to make any alterations (such as a segementation); If you don’t have this checked, then you can still make changes to the proxy node, but when you browse away, those changes are discarded, and when you come back to that frame, it will be unchanged.</p>

---

## Post #6 by @S_Esmaeili (2023-12-07 20:21 UTC)

<p>for turning off previous segmentations i should use the eye icon on the right side of segments?<br>
i am working on a large dataset and because of that hiding segments every time will be time consuming.</p>

---

## Post #7 by @S_Esmaeili (2023-12-07 20:49 UTC)

<p>thanks for your complete explanation of sequence, but my images are bitewings collected in last 3 years and they are not live stream.</p>

---

## Post #8 by @muratmaga (2023-12-07 21:05 UTC)

<aside class="quote no-group" data-username="S_Esmaeili" data-post="6" data-topic="33166">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/s_esmaeili/48/66722_2.png" class="avatar"> S_Esmaeili:</div>
<blockquote>
<p>for turning off previous segmentations i should use the eye icon on the right side of segments?</p>
</blockquote>
</aside>
<p>To turn off the visibility of a segmentation object entirely, you can use the visibility icon in the Data module. Turning visibility on/off is a very fast operation, shouldn’t take long.</p>
<p>Individual segment visibility can be controlled inside the Segment Editor easily. Again it should be fast. The only time it might be slow if you have the 3D visibility also turned on. If that’s the case, try the new surface nets based 3D reconstruction introduced in stable 5.6. It is very fast, particularly if you also choose to do the smoothing with it. See this <a href="https://discourse.slicer.org/t/new-surface-model-generation-method-surfacenets/32430/2">New surface model generation method: SurfaceNets - Support - 3D Slicer Community</a></p>

---
