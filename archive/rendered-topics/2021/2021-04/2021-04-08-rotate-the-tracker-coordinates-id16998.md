---
topic_id: 16998
title: "Rotate The Tracker Coordinates"
date: 2021-04-08
url: https://discourse.slicer.org/t/16998
---

# Rotate the tracker coordinates

**Topic ID**: 16998
**Date**: 2021-04-08
**URL**: https://discourse.slicer.org/t/rotate-the-tracker-coordinates/16998

---

## Post #1 by @WangZhen1175701153 (2021-04-08 12:20 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/666cc31336a21dc94f8749f6360c686bc94e904a.png" alt="image" data-base62-sha1="eC5IRdteomdgH4dMda8EphwJZzA" width="509" height="296">   My tracker doesn’t align with the needle model. How do I rotate the coordinates that the physics tracker passed in?</p>

---

## Post #2 by @Sunderlandkyl (2021-04-08 14:20 UTC)

<p>Have you completed a pivot calibration?<br>
You can find a SlicerIGT tutorial (U-11) here: <a href="http://www.slicerigt.org/wp/user-tutorial/" class="inline-onebox" rel="noopener nofollow ugc">User tutorial | SlicerIGT</a></p>

---

## Post #3 by @WangZhen1175701153 (2021-04-09 01:23 UTC)

<p>Yes. I did pivot calibration as shown in Example 1.<br>
And now, “ProBetoTracker” is my tracker and “StylustoreReference” is the corrected coordinate transform. You can see them in the picture. At this point, my tracker is pinned vertically and the pointer is displayed horizontally. So what do I have to do to get the pointer to be vertical?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/9756f4700182cbaded51f95fe0efa5af9a310c48.png" data-download-href="/uploads/short-url/lAOoFzeO2Xwf2I6PwGwl0QJJ0AE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/9756f4700182cbaded51f95fe0efa5af9a310c48_2_690x270.png" alt="image" data-base62-sha1="lAOoFzeO2Xwf2I6PwGwl0QJJ0AE" width="690" height="270" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/9756f4700182cbaded51f95fe0efa5af9a310c48_2_690x270.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/9756f4700182cbaded51f95fe0efa5af9a310c48_2_1035x405.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/9756f4700182cbaded51f95fe0efa5af9a310c48_2_1380x540.png 2x" data-dominant-color="BCBEE1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1798×706 45.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @wujie (2021-04-09 03:04 UTC)

<p>change the transform</p>

---

## Post #5 by @WangZhen1175701153 (2021-04-09 03:09 UTC)

<p>I tried, but it didn’t work. <img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=9" title=":rofl:" class="emoji" alt=":rofl:"> Maybe I modified the Transform the wrong way.</p>

---

## Post #6 by @WangZhen1175701153 (2021-04-09 07:14 UTC)

<p>I got it. I modified the rotation of the StylusToReference transform. <img src="https://emoji.discourse-cdn.com/twitter/grin.png?v=9" title=":grin:" class="emoji" alt=":grin:"></p>

---

## Post #7 by @ungi (2021-04-09 17:41 UTC)

<p>The cleanest solution is to define a ReferenceToRas transform node as well, and make that as the parent of StylusToReference in the transform hierarchy. Slicer uses the RAS coordinate system for display, but your Reference optical marker is rarely in the same orientation. ReferenceToRAS gives you a chance to rotate the Reference coordinate system to an anatomical one.</p>

---

## Post #8 by @WangZhen1175701153 (2021-04-10 02:02 UTC)

<p>Yes. You’re right. But I changed the rotation Angle of StyleStoreReference, which has the same effect as what you said. <img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=9" title=":rofl:" class="emoji" alt=":rofl:"> <img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=9" title=":rofl:" class="emoji" alt=":rofl:"> <img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=9" title=":rofl:" class="emoji" alt=":rofl:">  I don’t know if this will affect the result of pivot calibration.</p>

---

## Post #9 by @wujie (2021-04-28 04:39 UTC)

<p>Could I add your contact information?My qq is 774829849.Please contact me.I want to ask some question for you.</p>

---
