---
topic_id: 6626
title: "Resetting Of Splitted Segments In Virtual Reality"
date: 2019-04-27
url: https://discourse.slicer.org/t/6626
---

# Resetting of splitted segments in virtual reality

**Topic ID**: 6626
**Date**: 2019-04-27
**URL**: https://discourse.slicer.org/t/resetting-of-splitted-segments-in-virtual-reality/6626

---

## Post #1 by @sarvpriya1985 (2019-04-27 18:35 UTC)

<p>Operating system:windows 10<br>
Slicer version:4.10<br>
Expected behavior:<br>
Actual behavior:<br>
Hi,<br>
I installed the stable version 4.10 and is working fine with virtual reality. My question is:<br>
This is the base image that i converted to models-<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6db3065bcf39de6c5cd4870b14ddc75d4c341b9a.jpeg" data-download-href="/uploads/short-url/fErBoNI0i60FNZjcDZD9bxHh3Gq.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6db3065bcf39de6c5cd4870b14ddc75d4c341b9a_2_690x461.jpeg" alt="PNG" data-base62-sha1="fErBoNI0i60FNZjcDZD9bxHh3Gq" width="690" height="461" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6db3065bcf39de6c5cd4870b14ddc75d4c341b9a_2_690x461.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6db3065bcf39de6c5cd4870b14ddc75d4c341b9a_2_1035x691.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6db3065bcf39de6c5cd4870b14ddc75d4c341b9a_2_1380x922.jpeg 2x" data-dominant-color="A8ABBC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1576×1053 340 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> .</p>
<p>After converting into models, i splitted all segments in virtual reality. My question is there a way to reset all segments to their original position after moving them apart.<br>
I can manually move them, but I am not sure if I can put them back at their original position.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05b791730b22b6deb07be0becded34d171545bf1.jpeg" data-download-href="/uploads/short-url/OzGbarC3BW6eoPlwlJdHNPU9pL.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05b791730b22b6deb07be0becded34d171545bf1_2_690x414.jpeg" alt="Capture" data-base62-sha1="OzGbarC3BW6eoPlwlJdHNPU9pL" width="690" height="414" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05b791730b22b6deb07be0becded34d171545bf1_2_690x414.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05b791730b22b6deb07be0becded34d171545bf1_2_1035x621.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05b791730b22b6deb07be0becded34d171545bf1_2_1380x828.jpeg 2x" data-dominant-color="ABABCD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1828×1099 300 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks,<br>
Sarv</p>

---

## Post #2 by @cpinter (2019-04-29 00:07 UTC)

<p>When you move objects in virtual reality, then a transform node is added to each of those objects and that transform is modified when moving the controller.</p>
<p>You can unset transforms in the Data module by double-clicking the transform icon and then choose None. The transform icons are the little rotated grid squares on the right side of the color.</p>
<p>If you don’t want to keep any of those transforms and do it in one step, then you can just select all of those transforms in the Data module (will be on the bottom called …VR_Interaction_Transform), right-click, then Delete.</p>

---

## Post #3 by @sarvpriya1985 (2019-04-30 12:20 UTC)

<p>Thanks a lot for the tip!</p>
<p>Sarv</p>

---
