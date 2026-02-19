---
topic_id: 3476
title: "Pig Spinal Vertebrae Segmentation"
date: 2018-07-12
url: https://discourse.slicer.org/t/3476
---

# Pig Spinal Vertebrae Segmentation

**Topic ID**: 3476
**Date**: 2018-07-12
**URL**: https://discourse.slicer.org/t/pig-spinal-vertebrae-segmentation/3476

---

## Post #1 by @Hikmat (2018-07-12 20:10 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.8.1</p>
<p>Hi,</p>
<p>I am attempting to segment the spinal vertebrae of a pig from CT images.</p>
<p>The objective is to generate a surface model from the bone segmentation. The user will then perform a registration between the model and the pig (matching points on the model to the respective points on the pig’s spine) so that a surgical navigation system is in place.</p>
<p>The region of interest is the spinous process (the pointy tip of the vertebra; enclosed in red) since this is the site on the pig’s spine where the stylus tool can easily access during navigation.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/9958c273eb512578fb7a28ffae99af1e79183da7.png" alt="image" data-base62-sha1="lSzdBM5kmVUaH7NF8BErM3nqOxx" width="199" height="166"></p>
<p>The CT slice in use is shown below as well as a closeup of the vertebrae. The bone can clearly be seen in white and the vertebra is well-defined.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bde06ba36c0bcf65f4de8143db669483d48ccba.jpeg" data-download-href="/uploads/short-url/foeMglEuDgce2GvEkMBrlaJbQ3U.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bde06ba36c0bcf65f4de8143db669483d48ccba_2_690x387.jpg" alt="image" data-base62-sha1="foeMglEuDgce2GvEkMBrlaJbQ3U" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bde06ba36c0bcf65f4de8143db669483d48ccba_2_690x387.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bde06ba36c0bcf65f4de8143db669483d48ccba.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bde06ba36c0bcf65f4de8143db669483d48ccba.jpeg 2x" data-dominant-color="747474"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">783×440 67.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, the brightness/contrast does not seem to be consistent throughout the slice. For instance, the spinous process - the most important region - is not being processed as bone (it is a shade of gray rather than white) and this is causing issues in segmentation since the entire vertebra needs to be segmented.</p>
<p>This is evident when I try to perform a bone segmentation using Threshold in which the bone structure of interest (the vertebra) is not being entirely segmented (the spinous process is left out). Further peculiarities include the bone structure not of interest (the ribs) getting segmented perfectly in addition to artifact in the lower region being included.</p>
<p>Threshold results:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96661e1dadf28da091f1c8ad286be7c14b811d82.jpeg" data-download-href="/uploads/short-url/lsupcYPZ3FevzNnfZYew4I8wKUW.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/96661e1dadf28da091f1c8ad286be7c14b811d82_2_690x309.jpg" alt="image" data-base62-sha1="lsupcYPZ3FevzNnfZYew4I8wKUW" width="690" height="309" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/96661e1dadf28da091f1c8ad286be7c14b811d82_2_690x309.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96661e1dadf28da091f1c8ad286be7c14b811d82.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96661e1dadf28da091f1c8ad286be7c14b811d82.jpeg 2x" data-dominant-color="84827C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">810×363 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Closeup of vertebra for the above cases:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57c937c1d1a619065d48ad2cad05460837109df0.jpeg" data-download-href="/uploads/short-url/cwAE7nfGxX5buXKfzHvmkAoa40M.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57c937c1d1a619065d48ad2cad05460837109df0_2_690x366.jpg" alt="image" data-base62-sha1="cwAE7nfGxX5buXKfzHvmkAoa40M" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57c937c1d1a619065d48ad2cad05460837109df0_2_690x366.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57c937c1d1a619065d48ad2cad05460837109df0.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57c937c1d1a619065d48ad2cad05460837109df0.jpeg 2x" data-dominant-color="A09B90"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">811×431 94.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am hoping that better segmentation techniques / tools exist that can solve this unique problem.<br>
I know of threshold separating filters such as Otsu but I am not getting much success with these tools.</p>
<p>Any insight into this matter will be greatly appreciated.</p>
<p>Thanks,<br>
Hikmat</p>

---

## Post #2 by @lassoan (2018-07-13 01:06 UTC)

<blockquote>
<p>The objective is to generate a surface model from the bone segmentation</p>
</blockquote>
<p>It would be useful to know the end goal, as requirements for the generated surface are very different for each clinical application. If you need to generate bone surface models for 3D printing then you want  to minimize internal holes, while if you need surface for ultrasound or surface-scan based registration then you want to have good-quality posterior bone surfaces; if work on artificial disk planning then accurate separation of vertebrae is very important, etc. The choice of method also depends on accuracy requirements and available time for performing the segmentation.</p>
<p>Anyway, these tutorials and tips should help in finding a good workflow for your segmentation:</p>
<ul>
<li><a href="https://discourse.slicer.org/t/fill-holes-after-threshold-based-bone-segmentation-in-ct/2478/2" class="inline-onebox">Fill holes after threshold-based bone segmentation in CT - #2 by lassoan</a></li>
<li><a href="https://discourse.slicer.org/t/bone-segmentation-to-create-3d-printable-stl/960" class="inline-onebox">Bone segmentation to create 3D-printable STL</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation" class="inline-onebox">Documentation/Nightly/Training - Slicer Wiki</a></li>
</ul>
<p>If you figure out a good workflow or cannot figure out an acceptable solution then let us know.</p>

---
