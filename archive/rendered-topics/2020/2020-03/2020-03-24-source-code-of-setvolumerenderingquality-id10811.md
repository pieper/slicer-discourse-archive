---
topic_id: 10811
title: "Source Code Of Setvolumerenderingquality"
date: 2020-03-24
url: https://discourse.slicer.org/t/10811
---

# Source code of SetVolumeRenderingQuality

**Topic ID**: 10811
**Date**: 2020-03-24
**URL**: https://discourse.slicer.org/t/source-code-of-setvolumerenderingquality/10811

---

## Post #1 by @joechenrh (2020-03-24 08:42 UTC)

<p>Hello,<br>
I want to know the implemention of <code>SetVolumeRenderingQuality</code> which control the quality of volume rendering, I search the whole project but I canot find it. Could you help me? Thanks!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39cfb1887974611dd05124a806306df029658337.jpeg" data-download-href="/uploads/short-url/8fqcdvBci4fRLhZpJBMrKksS4vl.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/39cfb1887974611dd05124a806306df029658337_2_690x27.jpeg" alt="1" data-base62-sha1="8fqcdvBci4fRLhZpJBMrKksS4vl" width="690" height="27" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/39cfb1887974611dd05124a806306df029658337_2_690x27.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/39cfb1887974611dd05124a806306df029658337_2_1035x40.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/39cfb1887974611dd05124a806306df029658337_2_1380x54.jpeg 2x" data-dominant-color="DADACB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1392×55 32.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27b36b3121df420c4455a734d1263b6ab2856907.png" data-download-href="/uploads/short-url/5Fd1uWwcTqizqYbuloGmM6NkhRZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27b36b3121df420c4455a734d1263b6ab2856907.png" alt="image" data-base62-sha1="5Fd1uWwcTqizqYbuloGmM6NkhRZ" width="690" height="210" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">843×257 3.37 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @joechenrh (2020-03-24 10:26 UTC)

<p>Ok, I found the implemention in <code>vtkMRMLVolumeRenderingDisplayableManager.cxx</code></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6df2415f4c8700f834e80d6e87be70cb18972d01.jpeg" alt="33" data-base62-sha1="fGD4Ar2RvqGt4wGGVmRbWEtnZF7" width="612" height="261"></p>

---
