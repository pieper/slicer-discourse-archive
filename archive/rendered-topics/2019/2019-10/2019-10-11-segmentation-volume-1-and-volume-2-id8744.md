# Segmentation: Volume (1) and Volume (2)

**Topic ID**: 8744
**Date**: 2019-10-11
**URL**: https://discourse.slicer.org/t/segmentation-volume-1-and-volume-2/8744

---

## Post #1 by @dszimatore (2019-10-11 11:24 UTC)

<p>Hi everybody! Why after segmentation of a tumor I obtain two measures Volume (1) and Volume (2)? Their value is quite similar. What’s the difference between these measures?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42e7aa184dc0903a4ce95678c2ebe81a00475f57.jpeg" data-download-href="/uploads/short-url/9xRQOlVQoiMhDuVRLb7QTacHVv9.jpeg?dl=1" title="misure" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42e7aa184dc0903a4ce95678c2ebe81a00475f57_2_690x484.jpeg" alt="misure" data-base62-sha1="9xRQOlVQoiMhDuVRLb7QTacHVv9" width="690" height="484" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42e7aa184dc0903a4ce95678c2ebe81a00475f57_2_690x484.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42e7aa184dc0903a4ce95678c2ebe81a00475f57_2_1035x726.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42e7aa184dc0903a4ce95678c2ebe81a00475f57.jpeg 2x" data-dominant-color="979796"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">misure</span><span class="informations">1278×898 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2019-10-11 15:01 UTC)

<p>For some reason we don’t have a documentation page on the wiki for Segment Statistics (or at least the link from the help is broken).  But the help does list that some properties are calculated on the labelmap and some are calculated with the surface model, so you can choose which you think better matches the reality of the structure being measured.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d986a728736d7eed42f03f34fee3c5f4d5cae5c.png" data-download-href="/uploads/short-url/hV4esjGW4nQWDpA02kTaiH5Lj0o.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d986a728736d7eed42f03f34fee3c5f4d5cae5c.png" alt="image" data-base62-sha1="hV4esjGW4nQWDpA02kTaiH5Lj0o" width="609" height="499" data-dominant-color="E1E1E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1022×838 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @dszimatore (2019-10-13 06:46 UTC)

<p>Thank you very much for your answer. I basically do the calculation with the command “label statistics” rather than “segment statistics”. I Think theoretically that calculating on the labelmap should be more similar to what I have segmented but basically I<br>
do not know with precision the difference between calculation on labelmap and on surface model.</p>
<p>Thank you!</p>
<p><a href="http://www.avg.com/email-signature?utm_medium=email&amp;utm_source=link&amp;utm_campaign=sig-email&amp;utm_content=webmail" rel="nofollow noopener"><img alt width="46" height="29" src="https://ipmcdn.avast.com/images/icons/icon-envelope-tick-green-avg-v1.png"></a><br>
Mail priva di virus. <a href="http://www.avg.com/email-signature?utm_medium=email&amp;utm_source=link&amp;utm_campaign=sig-email&amp;utm_content=webmail" rel="nofollow noopener"><br>
www.avg.com</a></p>

---

## Post #4 by @lassoan (2019-10-13 11:08 UTC)

<p>Segment statistics module computes statistics from all available representations. If you have binary labelmap representation in the segmentation node then you’ll get labelmap-based values, too.</p>

---
