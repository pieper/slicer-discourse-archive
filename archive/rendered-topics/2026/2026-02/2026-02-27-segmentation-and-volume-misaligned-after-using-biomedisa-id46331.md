---
topic_id: 46331
title: "Segmentation and Volume Misaligned After Using Biomedisa"
date: 2026-02-27
url: https://discourse.slicer.org/t/46331
last_bumped: 2026-03-06T10:34:38.829Z
---

# Segmentation and Volume Misaligned After Using Biomedisa

**Topic ID**: 46331
**Date**: 2026-02-27
**URL**: https://discourse.slicer.org/t/segmentation-and-volume-misaligned-after-using-biomedisa/46331

---

## Post #1 by @FabricioFO (2026-02-27 14:38 UTC)

<p>The problem is the following: I segment nasal turbinates in rodents and use Biomedisa. When I take my CT scans, I need to orient them in 3D Slicer, so I create a Transform and adjust the orientation. After that, I generate the slices that will be used by Biomedisa.</p>
<p>After this step, I upload them to Biomedisa, retrieve the file it generates, and load it into 3D Slicer. I click on the option in Data, “convert labelmap to segmentation node.” Then, I use ImageStack from SlicerMorph to upload the CT scans.</p>
<p>I then take the Transform I created earlier with the slices and, in another scene, apply it to the segmentation that came from Biomedisa and to the volume I uploaded—but they end up completely separated.</p>
<p>What am I doing wrong?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eedfb247effd055f202d9bd103db2f9174270f96.jpeg" data-download-href="/uploads/short-url/y5aU81ZqbycDkEldmwrvvQllpfE.jpeg?dl=1" title="alinhamento" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eedfb247effd055f202d9bd103db2f9174270f96_2_690x387.jpeg" alt="alinhamento" data-base62-sha1="y5aU81ZqbycDkEldmwrvvQllpfE" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eedfb247effd055f202d9bd103db2f9174270f96_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eedfb247effd055f202d9bd103db2f9174270f96_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eedfb247effd055f202d9bd103db2f9174270f96_2_1380x774.jpeg 2x" data-dominant-color="87888C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">alinhamento</span><span class="informations">1919×1079 345 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c58a82921312fdad35f4a024eba43388379f9046.png" data-download-href="/uploads/short-url/sbwOIFQ5Om9ENJ68Tkr8uAzzILs.png?dl=1" title="forum" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c58a82921312fdad35f4a024eba43388379f9046_2_690x387.png" alt="forum" data-base62-sha1="sbwOIFQ5Om9ENJ68Tkr8uAzzILs" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c58a82921312fdad35f4a024eba43388379f9046_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c58a82921312fdad35f4a024eba43388379f9046_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c58a82921312fdad35f4a024eba43388379f9046_2_1380x774.png 2x" data-dominant-color="7E7E83"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">forum</span><span class="informations">1919×1079 329 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @mikebind (2026-02-27 22:03 UTC)

<p>Have you tried using the Biomedisa extension? This would keep everything in Slicer.  I’m guessing that perhaps your issue is related to rearranging image axes in the export-import process.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="VJXDxwp6eHY" data-video-title="Tutorial: How to use Biomedisa’s Smart Interpolation in 3D Slicer" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=VJXDxwp6eHY" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://i.ytimg.com/vi/VJXDxwp6eHY/hqdefault.jpg" title="Tutorial: How to use Biomedisa’s Smart Interpolation in 3D Slicer" width="480" height="360">
  </a>
</div>


---

## Post #3 by @MrMarkus (2026-03-05 08:09 UTC)

<p>Hi,</p>
<p>take a look at this information:</p>
<aside class="quote quote-modified" data-post="1" data-topic="10446">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/model-files-are-now-saved-in-lps-coordinate-system/10446">Model files are now saved in LPS coordinate system</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #000000;" data-drop-close="true" class="badge-category --style-square " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
    </div>
  </div>
  <blockquote>
    While Slicer uses RAS coordinate system internally, images, transforms, and markups files are stored in LPS coordinate system, because DICOM and all medical image computing software (maybe except a few very old ones) uses LPS coordinate system in files. 
However, Slicer has been still using its internal RAS coordinate system in mesh files (STL, VTK, VTP, OBJ, PLY), which <a href="https://issues.slicer.org/view.php?id=4445" rel="noopener nofollow ugc">caused issues when interfacing with third-party software</a>. 
Starting from tomorrow (Slicer-4.11.0-2020-02-26, revision 28794), …
  </blockquote>
</aside>

<p>Maybe that´s also the case in your situation?</p>
<p>Best,<br>
Markus</p>

---

## Post #4 by @drnoorfatima (2026-03-06 10:34 UTC)

<p>This is a classic RAS/LPS coordinate mismatch.</p>
<p>Looking at your screenshots, the segmentation labels are spatially correct relative to each other but displaced and rotated relative to the scan volume. That is the exact signature of an axis flip happening during export or import, not a segmentation error.</p>
<p>A few things to check in order:</p>
<ol>
<li>What format did you export and reimport the segmentation through? STL, OBJ, and PLY historically had this issue in Slicer versions before 4.11 revision 28794</li>
<li>If you are on a current Slicer version, check whether your transform matrix has any negative diagonal values, which would indicate an axis inversion is baked into the transform</li>
<li>The transform matrix visible in your screenshot shows 0.99, -0.99 values which suggests a near-180 degree rotation is already applied, worth checking if that is intentional or a symptom</li>
</ol>
<p>The fix depends on exactly where in your pipeline the flip is introduced. It is a quick solve once you identify the step.</p>

---
