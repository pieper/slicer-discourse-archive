---
topic_id: 9815
title: "Filling Holes In A Skull"
date: 2020-01-14
url: https://discourse.slicer.org/t/9815
---

# Filling Holes in a Skull

**Topic ID**: 9815
**Date**: 2020-01-14
**URL**: https://discourse.slicer.org/t/filling-holes-in-a-skull/9815

---

## Post #1 by @MarcoPinheiro (2020-01-14 20:27 UTC)

<p>Hi, everyone!</p>
<p>I’ve been working on segmenting a skull from a specific file i found on the internet, but i just can’t seem to get a nice result from it.</p>
<p>All my attempts result in a skull with too many holes, and i can’t seem to fix it using the Surface Tool.</p>
<p>Is there another way to “close/fill” it?</p>
<p>Please, i would appreciate some help.</p>
<p>Thx!</p>
<p>Before Surface Tool<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9da9b082d2d76ef2250b30979d94ea8a3ba131a4.jpeg" data-download-href="/uploads/short-url/muKwis47HShtTHbwQyDIVrkjUKo.jpeg?dl=1" title="original" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9da9b082d2d76ef2250b30979d94ea8a3ba131a4_2_690x351.jpeg" alt="original" data-base62-sha1="muKwis47HShtTHbwQyDIVrkjUKo" width="690" height="351" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9da9b082d2d76ef2250b30979d94ea8a3ba131a4_2_690x351.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9da9b082d2d76ef2250b30979d94ea8a3ba131a4_2_1035x526.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9da9b082d2d76ef2250b30979d94ea8a3ba131a4.jpeg 2x" data-dominant-color="BFBFD9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">original</span><span class="informations">1366×696 74.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After Surface Tool<br>
(The best so far, but still too many holes inside the skull)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebe6e8fd2bfa1755c7f9b4db3b327994ff239c3b.jpeg" data-download-href="/uploads/short-url/xESVxXWZOffMY7CNOuFCp5jTl3l.jpeg?dl=1" title="Figura 7.1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ebe6e8fd2bfa1755c7f9b4db3b327994ff239c3b_2_690x340.jpeg" alt="Figura 7.1" data-base62-sha1="xESVxXWZOffMY7CNOuFCp5jTl3l" width="690" height="340" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ebe6e8fd2bfa1755c7f9b4db3b327994ff239c3b_2_690x340.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ebe6e8fd2bfa1755c7f9b4db3b327994ff239c3b_2_1035x510.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebe6e8fd2bfa1755c7f9b4db3b327994ff239c3b.jpeg 2x" data-dominant-color="BCBDD7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Figura 7.1</span><span class="informations">1366×674 76.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Juicy (2020-01-14 22:15 UTC)

<p>Are you segmenting from a CT volume or have you just imported an STL model?</p>
<p>If you are segmenting from a CT volume then in segment editor you can use the smoothing effect with the smoothing method set to “Closing (fill holes)”. Try different sized kernels, the bigger the kernel, the more holes are filled. Just be careful not to have it so high that you fill too many foramen holes/other anatomical holes which are supposed to be there. Depending on how patient you are then you can also manually paint in areas of sketchy bone in the 2D slice windows.</p>
<p>If you are worried about there being lots of holes around the orbital walls and the sinus bones then this is a more difficult problem to solve. These bones are notoriously difficult to segment because they are so thin (down to around 0.5mm thick) their hounsfield units are very susceptible to being under-represented due to partial volume effects.</p>
<p>To get the best results you need a scan which has small voxels i.e. small field of view and small slice thickness. Then you can use the instructions on this post to get a slightly better segmentation: <a href="https://discourse.slicer.org/t/enhancing-orbital-walls-with-unsharp-mask-filtering/8440/3">Enhancing orbital walls with Unsharp mask filtering</a></p>
<p>In the past if I want a skull model with nicely defined orbital walls then I first segment the skull from the main volume. Then I will crop out a volume for each orbit using two ROIs, then perform the unsharp mask image filter on these volumes, segment the orbital bones in separate segments, then combine these segments back into the original segment. This is easier than performing unsharp mask filtering on the whole original volume because the filter does have some negative side effects such as rasing the HU units of the skin etc.</p>

---

## Post #3 by @Juicy (2020-01-14 22:18 UTC)

<p>By the way where did you source the volume from? If it is open to the public then I would be keen to have a copy as it would be good to have a mandibulectomy sample volume.</p>
<p>Cheers,</p>

---

## Post #4 by @MarcoPinheiro (2020-01-14 22:54 UTC)

<p>Hey, Juicy, thanks a lot for the response!</p>
<p>To tell you the truth a lot of what you said is yet a bit unknown to me, so i’ll take some time to fully comprehend and try it.</p>
<p>Regarding the ct scan, i’m positive that i found it on <a href="http://embodi3d.com" rel="nofollow noopener">embodi3d.com</a>, but i just can’t seem to find it again. I’ll try to attach a link here from google drive. CTskull.nrrd<br>
If you manage to succeed with this skull, please share it as well.</p>
<p>Some comments about the quality of this file would be appreciated too. (Like if it’s possible to have a nice final model)</p>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1FwJrFtycnH3krs-QpscaS1S4DcnNmecZ/view?usp=sharing" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1FwJrFtycnH3krs-QpscaS1S4DcnNmecZ/view?usp=sharing" target="_blank" rel="nofollow noopener"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1FwJrFtycnH3krs-QpscaS1S4DcnNmecZ/view?usp=sharing" target="_blank" rel="nofollow noopener">CTskull.nrrd</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Thanks!</p>

---

## Post #5 by @Juicy (2020-01-15 00:44 UTC)

<p>Thanks for the link, That is a strange looking mandibulectomy! The bar looks like it is protruding from the skin!</p>
<p>That volume is not ideal for capturing the small details of the sinus bones so it is no wonder that there are lots of holes in the eye orbits. If you open the volume, then go to the Volumes module, then expand the volume information area you can see the image spacing values in there. The first two values are 0.556mm x 0.556mm which is the size of the voxels in the axial plane. This suggests that this was an axial CT scan with a field of view of about 285mm with a 512 matrix (0.556mm x 512 = 285mm).</p>
<p>The spacing in the z direction (Superior-Inferior) is 2mm which indicates that the slice spacing was 2mm.</p>
<p>If you go down to the display area in the volume module you can untick the interpolation box which allows you to visualise the voxels more easily in the 2D slice views.</p>
<p>Most of the scans I deal with for imaging orbital bones have a field of view of around 200mm so in plane voxel size of around 0.35 - 0.4mm and a slice thickness of 0.5mm - 1mm. This gives much better results that this volume.</p>
<p>You will need more that the fill holes tool to salvage a low resolution volume like this. You may see some improvement with Unsharp mask image filtering as described in the link above. You could also experiment with the shrink wrap segment effect that <a class="mention" href="/u/lassoan">@lassoan</a> mentioned.</p>
<p>Yes it is rather a complicated process. Read as much as you can in the linked topic above and follow some of the links to the masters thesis etc and post any remaining questions that you have on here.</p>

---
