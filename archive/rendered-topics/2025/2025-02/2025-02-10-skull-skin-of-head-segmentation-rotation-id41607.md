---
topic_id: 41607
title: "Skull Skin Of Head Segmentation Rotation"
date: 2025-02-10
url: https://discourse.slicer.org/t/41607
---

# Skull / Skin of head segmentation rotation

**Topic ID**: 41607
**Date**: 2025-02-10
**URL**: https://discourse.slicer.org/t/skull-skin-of-head-segmentation-rotation/41607

---

## Post #1 by @mxtt (2025-02-10 16:58 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b4edd78c022b5a7efc32fd1a0f561fedc99af4e.png" data-download-href="/uploads/short-url/8sF8ApAwUbSKmbAFaW7SX64AI6a.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b4edd78c022b5a7efc32fd1a0f561fedc99af4e_2_569x500.png" alt="image" data-base62-sha1="8sF8ApAwUbSKmbAFaW7SX64AI6a" width="569" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b4edd78c022b5a7efc32fd1a0f561fedc99af4e_2_569x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b4edd78c022b5a7efc32fd1a0f561fedc99af4e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b4edd78c022b5a7efc32fd1a0f561fedc99af4e.png 2x" data-dominant-color="8989B8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">707×621 37.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So I have this segmentation of the skin of a head, I also have the skull (not displayed here). Does anyone have an intelligent way to rotate it so that is is positioned correctly - by correctly I essentially mean rotated so that the eyes fall on an equal, horizontal plane. You can see in the image the head is rotated slightly in the CT and I essentially want it straightened.</p>
<p>Thank you!!</p>

---

## Post #2 by @cpinter (2025-02-11 10:03 UTC)

<p>Just to confirm, because you posted in the development category (but I don’t find any clue about this in your text), do you want to do this automatically using Python code?</p>

---

## Post #3 by @mxtt (2025-02-11 16:59 UTC)

<p>Yes I would like to do this automatically through python development. I am writing a script and would like this feature implemented so that it auto rotates the head to the so that it lines up with the orthogonal planes.</p>
<p>I was hoping someone might have a good way to do this as I couldn’t find much.</p>

---

## Post #4 by @cpinter (2025-02-12 13:35 UTC)

<p>The only thing that occurs to me is to try to run TotalSegmentator (or other model that works for the head), get the eyeball centers and do a rotation around the AP axis.</p>

---

## Post #5 by @mxtt (2025-02-12 16:30 UTC)

<p>If I use a semi-automated approach where I place at least 2 fiducials on the corner of the eye and the nasion, do you think this would be sufficient?</p>
<p>Also how might I do the rotation through python?</p>
<p>Thank you for all the input!</p>

---

## Post #6 by @cpinter (2025-02-13 09:10 UTC)

<aside class="quote no-group" data-username="mxtt" data-post="5" data-topic="41607">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/87869e/48.png" class="avatar"> mxtt:</div>
<blockquote>
<p>If I use a semi-automated approach where I place at least 2 fiducials on the corner of the eye and the nasion, do you think this would be sufficient?</p>
</blockquote>
</aside>
<p>Absolutely.</p>
<aside class="quote no-group" data-username="mxtt" data-post="5" data-topic="41607">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/87869e/48.png" class="avatar"> mxtt:</div>
<blockquote>
<p>Also how might I do the rotation through python?</p>
</blockquote>
</aside>
<p>You can fit a plane on the points, calculate its normal, construct a transformation matrix so that the plane normal is the new IS axis, then set the transform node containing this matrix to the volume as parent.</p>

---
