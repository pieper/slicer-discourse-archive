# Linear transform problem. Rotation slider makes my images goes away.

**Topic ID**: 39921
**Date**: 2024-10-29
**URL**: https://discourse.slicer.org/t/linear-transform-problem-rotation-slider-makes-my-images-goes-away/39921

---

## Post #1 by @Dimitar_Velev (2024-10-29 14:33 UTC)

<p>Tried but cant solve the problem. Want to reposition up down position in linear transform, but when i push the slider images goes away, not rotating. Can you help me? I use newest version of 3d slicer.</p>

---

## Post #2 by @cpinter (2024-10-29 14:49 UTC)

<p>Can you please send a video of what you do? Also if you can describe what you want to achieve in more detail. Where does the data come from, what you want to do with it exactly, to what purpose, etc. Thanks!</p>

---

## Post #3 by @mau_igna_06 (2024-10-29 15:30 UTC)

<p>I think this could happen if the center of the image is very far from zero</p>
<p>HIH</p>

---

## Post #4 by @lassoan (2024-10-29 16:16 UTC)

<p>In recent Slicer Preview Releases you can conveniently set the center of transform:</p>
<ul>
<li>Enable “Interaction” in the right-click menu of the visibility column of the image in Data module:</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43c156ffa7e5d1c28ee9f9ba0b178a1922c89211.jpeg" data-download-href="/uploads/short-url/9FodAEKOgeKf2tRGGym0DPq5jJ7.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43c156ffa7e5d1c28ee9f9ba0b178a1922c89211_2_690x342.jpeg" alt="image" data-base62-sha1="9FodAEKOgeKf2tRGGym0DPq5jJ7" width="690" height="342" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43c156ffa7e5d1c28ee9f9ba0b178a1922c89211_2_690x342.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43c156ffa7e5d1c28ee9f9ba0b178a1922c89211_2_1035x513.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43c156ffa7e5d1c28ee9f9ba0b178a1922c89211_2_1380x684.jpeg 2x" data-dominant-color="3B3B3B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1917×952 241 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>Move the center of rotation by Alt+Left-click-and-drag in viewers, or by right-clicking on the current center and reset the center of the transformation to the image center you want to rotate around:</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48c1847873cc765d77e3c1fb9788b8a44a8a5daf.jpeg" data-download-href="/uploads/short-url/anCZcvqabTK93cwhoMuWaUeaE8f.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48c1847873cc765d77e3c1fb9788b8a44a8a5daf_2_622x500.jpeg" alt="image" data-base62-sha1="anCZcvqabTK93cwhoMuWaUeaE8f" width="622" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48c1847873cc765d77e3c1fb9788b8a44a8a5daf_2_622x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48c1847873cc765d77e3c1fb9788b8a44a8a5daf_2_933x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48c1847873cc765d77e3c1fb9788b8a44a8a5daf_2_1244x1000.jpeg 2x" data-dominant-color="524F5C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1323×1063 201 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Dimitar_Velev (2024-10-30 05:09 UTC)

<p>The problem began, when i downloaded data from patient CT scan, and tried to open in 3d slicer. The liver was in the left side and upside down. Tried to use linear transform and reformat, useless. Realised that the center of rotation is far, but not able to change it. Then i tried to load images not from"Add data", but from “Add DICOM data” and the problem was fixed. I still wonder … Thank You for advices, it will be usefull in future <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---
