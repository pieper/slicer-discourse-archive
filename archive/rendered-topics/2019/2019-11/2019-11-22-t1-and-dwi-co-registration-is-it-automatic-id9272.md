# T1 and DWI co-registration - is it automatic

**Topic ID**: 9272
**Date**: 2019-11-22
**URL**: https://discourse.slicer.org/t/t1-and-dwi-co-registration-is-it-automatic/9272

---

## Post #1 by @LearningSlicerYay (2019-11-22 16:31 UTC)

<p>Operating system: Win 7 Pro<br>
Slicer version: 4.10.1<br>
Expected behavior: N/A<br>
Actual behavior: N/A</p>
<p>Hello everyone,<br>
New to Slicer - primarily interested in using it for DTI for now.<br>
I have downloaded dMRI and am going through the tutorials with no issues. However, I would like to draw the ROIs for tractography using T1 from the same scan.</p>
<p>I have tried following the <a href="http://dmri.slicer.org/tutorials/Slicer-4.8/DiffusionMRIAnalysis.pdf" rel="nofollow noopener">tutorial by Sonia Pujol</a>. At the step where I draw the ROIs, I diverage a bit and load the T1 sequence. It was taken during the same scan as my DWI dataset, and looks like it is coregistered with no issues when I scroll through it.</p>
<p>My question is, is it actually coregistered or should I proceed by coregistering my T1 to DWI first, then generating my DTI maps and load the coregistered T1 to draw my ROIs?</p>
<p>Many thanks,</p>

---

## Post #2 by @pieper (2019-11-22 19:04 UTC)

<p>Yes, it should be corregistered and work fine.  You can easily test by drawing segments in the corpus and confirm that you can generate tracts.</p>

---

## Post #3 by @LearningSlicerYay (2019-11-26 20:39 UTC)

<p>Thanks Pieper.<br>
When I load the T1c, it does look coregistered. However, after I load the T1c my labels seem to span over multiple slices even when I only draw it on one slice. I am not sure why this is happening or how to fix it.</p>
<p>Do you have any suggestions?</p>
<p>Thank you</p>

---

## Post #4 by @pieper (2019-11-26 22:32 UTC)

<p>The T1 and the DTI probably have different spacings.  When you are creating a segmentation, select the T1 as the master volume and the segmentation will use that spacing.  You can switch to the DTI later when defining segments.</p>

---

## Post #5 by @LearningSlicerYay (2020-02-25 20:03 UTC)

<p>Sorry to push an old post, but I was wondering if you knew what method is being used to coregister the T1 to DWI <a class="mention" href="/u/pieper">@pieper</a> ?</p>

---

## Post #6 by @zhangfanmark (2020-02-25 20:23 UTC)

<p>Hi,</p>
<p>Usually, we do this registration using the b0 that is extracted from DWI. The computed transformation matrix is then applied to either T1 or the whole DWI volume to make them in the same space.</p>
<p>To do this, you can use the Diffusion Brain Masking module to generate the b0 (baseline) image. Then, registration can be done using the General Registration (BRAINS) module. Using the T1 as fixed image and the b0 as the moving image. In this case, you can get a b0 to T1 transformation matrix. Then you can use the Transforms module to apply the transformation matrix to either the T1 or the DWI.<br>
Here is the tutorial about the General Registration and Transforms modules. <a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Registration" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/Training#Registration</a></p>
<p>Regards,<br>
Fan</p>

---

## Post #7 by @LearningSlicerYay (2020-02-25 22:10 UTC)

<p>Hi <a class="mention" href="/u/zhangfanmark">@zhangfanmark</a><br>
Thanks for your help.<br>
I tried doing this and was able to generate a transformation matrix based on the baseline as moving image and T1 as fixed image, as you suggested. Then, I used the Transforms module and tried to apply this to the entire DWI set, but the transformed volume is just colours (screenshot attached).  Do you know why this might be?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32f72bd4f267868b7468fcb44168ea01eab76714.png" data-download-href="/uploads/short-url/7gRqZJxVmErrwjLgXal3ElXhoDW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32f72bd4f267868b7468fcb44168ea01eab76714_2_490x500.png" alt="image" data-base62-sha1="7gRqZJxVmErrwjLgXal3ElXhoDW" width="490" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32f72bd4f267868b7468fcb44168ea01eab76714_2_490x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32f72bd4f267868b7468fcb44168ea01eab76714_2_735x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32f72bd4f267868b7468fcb44168ea01eab76714_2_980x1000.png 2x" data-dominant-color="D7D8D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1094×1116 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
