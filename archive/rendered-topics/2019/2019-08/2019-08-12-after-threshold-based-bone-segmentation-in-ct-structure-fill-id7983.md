# After threshold-based bone segmentation in CT structure filled with holes

**Topic ID**: 7983
**Date**: 2019-08-12
**URL**: https://discourse.slicer.org/t/after-threshold-based-bone-segmentation-in-ct-structure-filled-with-holes/7983

---

## Post #1 by @chad (2019-08-12 06:55 UTC)

<p>Hi all,</p>
<p>I am segmenting the geometries of flatfoot skeleton from a CT scan using Threshold effect.<br>
What is the better way to fill the holes inside the segmented flatfoot skeleton (see picture below)?<br>
Thanks!<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/456ffdf7ffb030340856baf19762069e3b5161b2.png" data-download-href="/uploads/short-url/9UgT0ZqExHuL1N02LN5GqQI2LSO.png?dl=1" title="68319312_1649184915215972_1185341717348352000_n" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/456ffdf7ffb030340856baf19762069e3b5161b2_2_690x431.png" alt="68319312_1649184915215972_1185341717348352000_n" data-base62-sha1="9UgT0ZqExHuL1N02LN5GqQI2LSO" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/456ffdf7ffb030340856baf19762069e3b5161b2_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/456ffdf7ffb030340856baf19762069e3b5161b2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/456ffdf7ffb030340856baf19762069e3b5161b2.png 2x" data-dominant-color="938AB8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">68319312_1649184915215972_1185341717348352000_n</span><span class="informations">872×545 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2019-08-13 03:28 UTC)

<p>You can try dilate and erode same amount (e.g., dilate 5mm and shrink 5mm) each of the segments one by one. This will take care most of the holes inside segments. But for the ones on the surface, you may have to play with your threshold.</p>

---

## Post #3 by @lassoan (2019-08-15 15:25 UTC)

<p>There is an excellent extension (that will be available in Slicer within days) to fill holes in cancellous bone: <a href="https://github.com/sebastianandress/Slicer-SegmentEditorSRSFilter" rel="nofollow noopener">https://github.com/sebastianandress/Slicer-SegmentEditorSRSFilter</a>.</p>
<p>You may also try the approach described in the <a href="https://lassoan.github.io/SlicerSegmentationRecipes/SkinSurface/" rel="nofollow noopener">Skin surface extraction segmentation recipe</a>.</p>

---

## Post #5 by @chad (2019-09-05 03:58 UTC)

<p>Hi thank you for the response!</p>

---

## Post #6 by @chad (2019-09-05 08:33 UTC)

<p>Hello! My computer system is Windows. Can I use the above method to install the extension ?<br>
Thank you!</p>

---

## Post #7 by @lassoan (2019-09-05 12:45 UTC)

<p>The extension has not been added to the index yet due to summer holidays. You can monitor the status of the extension <a href="https://github.com/Slicer/ExtensionsIndex/pull/1655" rel="nofollow noopener">here</a>. If you prefer not to wait then you can download the <a href="https://github.com/sebastianandress/Slicer-SegmentEditorSRSFilter" rel="nofollow noopener">extension</a> and manually install it (by adding the module to additional module paths in Slicer application settings).</p>

---

## Post #8 by @chad (2019-09-06 06:00 UTC)

<p>Hello professor!I added the module to additional module paths in Slicer application settings,but it didn’t work.I’m not sure if my steps are correct.Is there a more detailed installation method?I will be very grateful.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9d23aec0ed5a753aa7ad4c6e95654a159de335f.png" data-download-href="/uploads/short-url/zE1iZ05WPt71Kc95HQqPGzgwxlB.png?dl=1" title="%E8%A8%BB%E8%A7%A3%202019-09-06%20135418" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9d23aec0ed5a753aa7ad4c6e95654a159de335f.png" alt="%E8%A8%BB%E8%A7%A3%202019-09-06%20135418" data-base62-sha1="zE1iZ05WPt71Kc95HQqPGzgwxlB" width="520" height="500" data-dominant-color="F1F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">%E8%A8%BB%E8%A7%A3%202019-09-06%20135418</span><span class="informations">676×649 35.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
