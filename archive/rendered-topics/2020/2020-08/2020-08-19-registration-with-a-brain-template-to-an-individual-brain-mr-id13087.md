# Registration with a Brain template to an individual brain MRI

**Topic ID**: 13087
**Date**: 2020-08-19
**URL**: https://discourse.slicer.org/t/registration-with-a-brain-template-to-an-individual-brain-mri/13087

---

## Post #1 by @Christiane (2020-08-19 13:32 UTC)

<p>Hi all,</p>
<p>I try to register a population brain template to a subject anatomical MRI, so that in the end all anatomical MRI’s fit to the brain template.<br>
In the beginning I used the “Transforms”, so that my template and the MRI overlap (see attached picture). After that I used the “Landmarks” tool and then went over to the “resample image (brains)” and tried to do an affine registration- but the result is not perfect. The MRI brain size doesn’t fit perfectly to the template size after registration. What have I done wrong? Other Tools like “general registration (brains)” never worked with my data- there is always an error or just nonsense results…</p>
<p>This is the screenshot after I orientated template and MRi new:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/794ebe115296f66d1e29921cdd15e106d7aaaefd.jpeg" data-download-href="/uploads/short-url/hj8tGHcepSTSjsHcAQABulFg4qN.jpeg?dl=1" title="Balu" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/794ebe115296f66d1e29921cdd15e106d7aaaefd_2_690x471.jpeg" alt="Balu" data-base62-sha1="hj8tGHcepSTSjsHcAQABulFg4qN" width="690" height="471" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/794ebe115296f66d1e29921cdd15e106d7aaaefd_2_690x471.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/794ebe115296f66d1e29921cdd15e106d7aaaefd_2_1035x706.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/794ebe115296f66d1e29921cdd15e106d7aaaefd.jpeg 2x" data-dominant-color="35353E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Balu</span><span class="informations">1305×892 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This is the result after registration with landmarks:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/785bc09d53517cbcbbb58f710219e68694dc1d73.jpeg" data-download-href="/uploads/short-url/haJSfKCCPmcSLq99GC1CvXVbVJh.jpeg?dl=1" title="Balu landmark" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/785bc09d53517cbcbbb58f710219e68694dc1d73_2_690x469.jpeg" alt="Balu landmark" data-base62-sha1="haJSfKCCPmcSLq99GC1CvXVbVJh" width="690" height="469" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/785bc09d53517cbcbbb58f710219e68694dc1d73_2_690x469.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/785bc09d53517cbcbbb58f710219e68694dc1d73_2_1035x703.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/785bc09d53517cbcbbb58f710219e68694dc1d73.jpeg 2x" data-dominant-color="5C5C68"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Balu landmark</span><span class="informations">1312×893 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I hope someone recorgnize what I’m doing wrong.<br>
Best regards<br>
Christiane</p>

---

## Post #2 by @lassoan (2020-08-19 13:36 UTC)

<p>You can use SlicerElastix extension instead of BRAINS. Elastix worjs very well with the default parameter set, yiu just need to make sure the images are cropped to approximately the same anatomical region and aligned with no more than 10-20mm and 5-10 degrees of initial misalignment.</p>
<p>To register images manually, you may also try SlicerIGT extension’s Fiducial Registration Wizard module with warping transform.</p>

---

## Post #3 by @Christiane (2020-08-20 12:45 UTC)

<p>I have downloaded the SlicerIGT but i cannot find a tool called Fiducial Registration Wizard ?! I just have the tool Fiducial Model Registration and Model registration? Is this the same to fiducial rregistration wizard? And do you have a tutorial how to use this tool?<br>
Because also with Elastix the registration fails - is there a possibility to show me a propably misalignment from my images?</p>
<p>Thank you so much. Best regards,<br>
Christiane</p>

---

## Post #4 by @lassoan (2020-08-20 13:50 UTC)

<p>Could you please try if Fiducial Registration Wizard shows up if you use latest Slicer Preview Release? After you click “Install” in the extension manager, wait for the “Restart” button to become active and click that (do not press close and restart manually).</p>

---

## Post #5 by @Christiane (2020-08-20 14:07 UTC)

<p>Thanks =) now I have the Fiducial Registration Wizard! Hope it works =)</p>
<p>Best regards,<br>
Christiane</p>

---
