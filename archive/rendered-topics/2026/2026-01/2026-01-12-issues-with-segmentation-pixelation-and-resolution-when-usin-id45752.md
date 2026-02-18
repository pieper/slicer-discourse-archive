# Issues with segmentation pixelation and resolution when using separate Axial/Coronal DICOMs.

**Topic ID**: 45752
**Date**: 2026-01-12
**URL**: https://discourse.slicer.org/t/issues-with-segmentation-pixelation-and-resolution-when-using-separate-axial-coronal-dicoms/45752

---

## Post #1 by @teakpAUM (2026-01-12 16:36 UTC)

<p>I’m working on a project to segment structures within the orbit. I’m using fat suppressed T1 weighted images from a database. The MRI DICOM files are downloaded individually e.g. one will be coronal one will be axial. But they’ll both be from the same patient. So they’re the same scan but different protocols. I’m importing the axial and coronal scan from the same patient into one file. Then I’m opening the folder on 3D slicer which has both the scans in. I ran into an issue that when viewing the scans e.g. I’m looking at the coronal scan 3D slicer then renders the other planes in awful quality so I cant segment using them.</p>
<p>When I try to segment in only one of the files e.g. the coronal file and then look at the axial file the segmentations roughly overlap but become extremely pixelated and blocky. When I try to change the segmentation on that scan (the axial) it only does large wide pixels. I would’ve expected if I segmented on the coronal scan for the axial to match roughly and then I can fill in the blanks using that axial scan. But the way its so pixelated I cant work on it at all.</p>
<p>Based on the practice scans, all three planes were clear and visible such that I could segment freely - my segmentation on one plane would show up correctly on the other planes and this would generate a correct 3d image in the fourth window. Is there any way to achieve this with the scans I’m downloading? Maybe so that the separated clear planes in each scan could be merged so I can view and segment on them at the same time.</p>

---

## Post #2 by @lassoan (2026-01-12 17:40 UTC)

<p>This is a very common limitation of clinical images that are acquired for slice-by-slice reading by humans, and not for 3D processing. You can find how to deal with such images for example here:</p>
<aside class="quote quote-modified" data-post="2" data-topic="2941">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941/2">Combining volumes - what am I missing?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    In general, these multiple low-resolution acquisitions are not well suited for any 3D processing, so the best would be to acquire proper 3D volume, with as isotropic spacing (cubic voxel shape) as possible. 
You may try to find toolkits that can create an isotropic super-resolution image from multiple low-resolution sweeps, but this is a difficult image reconstruction problem, so there are no standard solutions. Have a look at this post <a href="https://discourse.slicer.org/t/import-volume-by-projections/2871/6">Import volume by projections</a> for info on a toolkit that mig…
  </blockquote>
</aside>


---

## Post #3 by @teakpAUM (2026-01-13 09:43 UTC)

<p>Hi thank you for the reply! So from my understanding we either need to acquire isovoxel scans or try to use NiftyMIC to see if it could work is that correct?</p>
<p>is it possible to segment individual planes e.g if I segmented using the Coronal plane scan then segmented the Axial plane scan (both high quality) from the same patient. Would that be accurate or could you combine the volumes of those?</p>
<p>Or could it even be an option to just use one plane to segment and compare that to other scans only segmented using one plane?</p>
<p>My aim is to segment normal structures within the orbit and also segment lesions within the orbit. We ideally want to create parameters of the normal structure volumes out of our data.</p>

---

## Post #4 by @lassoan (2026-01-13 13:11 UTC)

<p>As it is described in the post I linked, you can resample any of the input volumes to be isotropic using the Crop Volume module. Then the segmentation you create for it will be isotropic, too. You can represent structures with finer details in this segmentation than in any of the input 3D volumes. The difficulty is that after you segmented a structure based on one of the 3D volumes, how you correct it based on another 3D volume.</p>
<p>That’s why 3D reconstruction using niftymic or other reconstruction techniques; or acquiring isotropic volume may work better.</p>

---

## Post #5 by @teakpAUM (2026-02-03 15:55 UTC)

<p>Hi,</p>
<p>I’m not quite proficient with 3Dslicer. I’ve tried playing around with the crop volume module but with no luck on how to do what you mentioned before. Is there a guide / tutorial anywhere explaining how to achieve this using the crop volume function?</p>
<p>I also looked at NiftyMIC and the main problem is that I am using fat suppressed T1 scans which mainly are only coronal or axial, there is no sagital version. Would that still be able to generate a 3D version of it? I also noticed it’s for fetal MRIs, would the algorithm be suitable for adults?</p>
<p>I have access to Mprage MRIs which are typically 3D but are not fat suppressed which creates the issue of not being able to segment the recti muscles properly</p>

---

## Post #6 by @Deep_Learning (2026-02-04 09:43 UTC)

<div class="youtube-onebox lazy-video-container" data-video-id="o44Oxk_DcSM" data-video-title="Cropping a Volume   [3D Slicer Workflow]" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=o44Oxk_DcSM" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/o44Oxk_DcSM/maxresdefault.jpg" title="Cropping a Volume   [3D Slicer Workflow]" width="690" height="388">
  </a>
</div>


---

## Post #7 by @teakpAUM (2026-02-17 21:56 UTC)

<p>Hi guys, Thanks for the help! I managed to acquire 3D scans (I believe isovoxel?) however when I try to segment its very pixely / block like. Any ideas what cause be causing this? Im just using the segment editor function with the sphere brush. I just need the pixels slightly smaller to be able to segment it more accurately to get the structure better (quite a small structure) / or even a smooth brush?</p>
<p>PixelSpacing : 0.9375, 0.9375</p>
<p>Slice thickness: 0.89999997615814</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/587a6f340e31bf9874fdafcca7f5ff4e1b4e4b88.png" data-download-href="/uploads/short-url/cCIkzGZzNEux60lLrYU3EzKmRuw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/587a6f340e31bf9874fdafcca7f5ff4e1b4e4b88.png" alt="image" data-base62-sha1="cCIkzGZzNEux60lLrYU3EzKmRuw" width="106" height="148"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">106×148 5.34 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2b4a2f16188dba20cd367c3bdceac901fa25b36.png" data-download-href="/uploads/short-url/ndmmrZiNgjPfjMDMKWzOkpVMxUO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2b4a2f16188dba20cd367c3bdceac901fa25b36.png" alt="image" data-base62-sha1="ndmmrZiNgjPfjMDMKWzOkpVMxUO" width="136" height="166"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">136×166 7.14 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @teakpAUM (2026-02-18 10:09 UTC)

<p>For context these are medial recti muscles.</p>

---
