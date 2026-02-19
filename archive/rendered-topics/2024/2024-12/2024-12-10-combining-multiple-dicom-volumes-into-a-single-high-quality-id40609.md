---
topic_id: 40609
title: "Combining Multiple Dicom Volumes Into A Single High Quality"
date: 2024-12-10
url: https://discourse.slicer.org/t/40609
---

# Combining Multiple DICOM Volumes into a Single High-Quality Volume for Segmentation

**Topic ID**: 40609
**Date**: 2024-12-10
**URL**: https://discourse.slicer.org/t/combining-multiple-dicom-volumes-into-a-single-high-quality-volume-for-segmentation/40609

---

## Post #1 by @Mateo23 (2024-12-10 15:47 UTC)

<p>Hello everyone,</p>
<p>I am working on a DICOM dataset with three volumes (axial, sagittal, and coronal) of a brain MRI study. Each volume is clear and high-quality for its respective orientation (e.g., axial cuts in the axial volume), but the other orientations appear very pixelated.</p>
<p>My goal is to create a single merged volume that combines the high-quality slices from each orientation (axial, sagittal, and coronal) into one coherent dataset that I can use for segmentation and further analysis.</p>
<p>I have attempted the following:</p>
<ol>
<li><strong>Volume Registration:</strong> Using the General Registration (BRAINS) module, I aligned the volumes. However, the output remains pixelated in non-primary orientations.</li>
<li><strong>Resampling:</strong> Adjusting B-Spline grid size, percentage of samples, and interpolation mode. The results are still not satisfactory.</li>
<li><strong>Merging Volumes:</strong> I looked for ways to combine the clear slices from each volume into a single node but couldn’t find an effective solution.</li>
</ol>
<p>Here are my questions:</p>
<ol>
<li>Is there a recommended method to merge slices from different volumes while retaining their original quality?</li>
<li>Are there specific settings I should tweak in the registration or resampling process to improve the results?</li>
<li>Should I use a different approach entirely to achieve my goal?</li>
</ol>
<p>Thank you for your guidance!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b0c5ee9c681b87db0d69c7e130cf27f14ea7b6c.jpeg" data-download-href="/uploads/short-url/8qmFQBGWhZnEPVFtcX2cFBwUZvm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b0c5ee9c681b87db0d69c7e130cf27f14ea7b6c_2_662x500.jpeg" alt="image" data-base62-sha1="8qmFQBGWhZnEPVFtcX2cFBwUZvm" width="662" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b0c5ee9c681b87db0d69c7e130cf27f14ea7b6c_2_662x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b0c5ee9c681b87db0d69c7e130cf27f14ea7b6c_2_993x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b0c5ee9c681b87db0d69c7e130cf27f14ea7b6c.jpeg 2x" data-dominant-color="3E3D43"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1275×962 208 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62aa114b6f1039cbdc1c9bf2569920f15eb20646.jpeg" data-download-href="/uploads/short-url/e4P9VFOiDLHu4UZyXv9VkvPQ4RM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62aa114b6f1039cbdc1c9bf2569920f15eb20646_2_646x500.jpeg" alt="image" data-base62-sha1="e4P9VFOiDLHu4UZyXv9VkvPQ4RM" width="646" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62aa114b6f1039cbdc1c9bf2569920f15eb20646_2_646x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62aa114b6f1039cbdc1c9bf2569920f15eb20646_2_969x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62aa114b6f1039cbdc1c9bf2569920f15eb20646.jpeg 2x" data-dominant-color="3C3B41"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1277×988 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/733b42e1dacb470a7f367d547c3c0683dd13cf94.jpeg" data-download-href="/uploads/short-url/grnSiqQbi3XreRYd705s5G3cnL6.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/733b42e1dacb470a7f367d547c3c0683dd13cf94_2_643x500.jpeg" alt="image" data-base62-sha1="grnSiqQbi3XreRYd705s5G3cnL6" width="643" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/733b42e1dacb470a7f367d547c3c0683dd13cf94_2_643x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/733b42e1dacb470a7f367d547c3c0683dd13cf94_2_964x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/733b42e1dacb470a7f367d547c3c0683dd13cf94.jpeg 2x" data-dominant-color="45454B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1275×990 228 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-12-10 21:11 UTC)

<p>Short answer is that it’s not really doable to combine the multiple series into one higher res volume.  But if your goal is to segment the tumor you should look into the <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/releases/tag/ModelsTestResults#:~:text=Brain%20Tumor%20Segmentation%20(BRATS)%20GLI%20(v1.0.0)">BraTS models in Auto3DSeg</a>.</p>
<p>More info on combining series:</p>
<aside class="quote" data-post="1" data-topic="27089">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/audrina_fernandez/48/17933_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/merge-3-mri-volumes-with-different-orientations-into-one/27089">Merge 3 MRI volumes with different orientations into one</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi, 
I’m working on MRI to segment cheek fat volume and often I have one serie of few images for axial axe, one serie for coronal axe, one serie for sagittal axe (for one patient, one IRM). To get a better volume segmentation I would like to stitch these series. Stitch volume module can help me to match differents axes or it is for differents series of the same axe? 
Sorry for my English <img width="20" height="20" src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title="slight_smile" alt="slight_smile" class="emoji">
  </blockquote>
</aside>


---
