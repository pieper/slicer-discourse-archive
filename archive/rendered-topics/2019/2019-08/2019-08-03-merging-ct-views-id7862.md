# Merging CT-views 

**Topic ID**: 7862
**Date**: 2019-08-03
**URL**: https://discourse.slicer.org/t/merging-ct-views/7862

---

## Post #1 by @HFNGL (2019-08-03 12:18 UTC)

<p>I just got three different files for one CT-scan. Each one contains a different view so there is one file containing the sagittal view in high res, one for axial and one for coronal.<br>
I want slicer to use all of these files when doing segmentations but it always uses only one file creating lower-res versions of the other views out of the file. I assume I’d get better segmentations when using the high-res versions of all views.<br>
Is there a way to create a new file containing all views out of these different files?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04ffcb9c66098dfa563b196ea8cf99a7ff7cc54d.png" data-download-href="/uploads/short-url/IdWPA6s5WbJ1jr07W28wvx0Azj.png?dl=1" title="42" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04ffcb9c66098dfa563b196ea8cf99a7ff7cc54d_2_690x70.png" alt="42" data-base62-sha1="IdWPA6s5WbJ1jr07W28wvx0Azj" width="690" height="70" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04ffcb9c66098dfa563b196ea8cf99a7ff7cc54d_2_690x70.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04ffcb9c66098dfa563b196ea8cf99a7ff7cc54d_2_1035x105.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04ffcb9c66098dfa563b196ea8cf99a7ff7cc54d_2_1380x140.png 2x" data-dominant-color="ECECF3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">42</span><span class="informations">2140×218 29.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47a1d08349d6c90aaa223896f9764e438602db7f.jpeg" data-download-href="/uploads/short-url/adGAm1TnlzcVjsGsWHw6stP5S11.jpeg?dl=1" title="10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47a1d08349d6c90aaa223896f9764e438602db7f_2_502x500.jpeg" alt="10" data-base62-sha1="adGAm1TnlzcVjsGsWHw6stP5S11" width="502" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47a1d08349d6c90aaa223896f9764e438602db7f_2_502x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47a1d08349d6c90aaa223896f9764e438602db7f_2_753x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47a1d08349d6c90aaa223896f9764e438602db7f_2_1004x1000.jpeg 2x" data-dominant-color="60606C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">10</span><span class="informations">1640×1632 500 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2019-08-05 19:54 UTC)

<p>Hi Philip -</p>
<p>This question comes up from time to time - for example the post linked below, or <a href="https://discourse.slicer.org/search?q=sagittal%20coronal">search for sagittal and coronal in the archives of posts</a>.</p>
<p>If you have any control over the scan protocol you can get a higher resolution reconstruction from the scanner, but there’s no good way to combine them after the fact.</p>
<aside class="quote quote-modified" data-post="1" data-topic="2941">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/f19dbf/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941">Combining volumes - what am I missing?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Operating system: Mac - High Sierra 
Slicer version: 4.8.1 
Expected behavior: One perfect, high resolution volume 
Actual behavior: Three volumes, each one being high resolution in only one plane (sagittal, coronal, transverse) 
I have been using 3D Slicer for many months and I’m slowly learning the ropes. I am using it to produce anatomical boney models, and have probably created between 10-15 models. 
After loading CT scans from their DICOM folder I always get several volumes, often with the …
  </blockquote>
</aside>


---
