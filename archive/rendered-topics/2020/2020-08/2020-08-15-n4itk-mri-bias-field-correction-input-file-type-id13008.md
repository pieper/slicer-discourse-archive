# N4ITK MRI Bias Field Correction input file type?

**Topic ID**: 13008
**Date**: 2020-08-15
**URL**: https://discourse.slicer.org/t/n4itk-mri-bias-field-correction-input-file-type/13008

---

## Post #1 by @sgonzalez122 (2020-08-15 02:08 UTC)

<p>Operating system: macOS Catalina<br>
Slicer version: none<br>
Expected behavior: Output a volume in Nifti format<br>
Actual behavior: none</p>
<p>Hi there, I am new to 3D slicer and was wondering if it’s N4ITK Bias Field Correction module accepted Nifti image files as input. More specifically I plan to run this module on a T1 weighted MPRAGE brain volume in Nifti file format. I was wondering if the module with accept this format and also output a corrected volume in Nifti as well. Additionally, I was wondering if the Bias Field Image output is also output as a volume and what file type is output when using this option.</p>
<p>Thank you for your help,<br>
Stephen</p>

---

## Post #2 by @lassoan (2020-08-15 02:09 UTC)

<p>Yes, Slicer can read MRI from a Nifti file, apply bias correction, and save result as Nifti file.</p>

---

## Post #3 by @sgonzalez122 (2020-08-16 20:12 UTC)

<p>Thank you so much <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
I was able to run it successfully, via command line, generate the bias field, and view it in FSL. It looks wonderful.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/0704bf956c8bb1157c9ee0cda5e4006dde531f04.png" data-download-href="/uploads/short-url/105vY6KfWhvBAebmCcdzk7tgOKE.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0704bf956c8bb1157c9ee0cda5e4006dde531f04_2_690x385.png" alt="1" data-base62-sha1="105vY6KfWhvBAebmCcdzk7tgOKE" width="690" height="385" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0704bf956c8bb1157c9ee0cda5e4006dde531f04_2_690x385.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0704bf956c8bb1157c9ee0cda5e4006dde531f04_2_1035x577.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0704bf956c8bb1157c9ee0cda5e4006dde531f04_2_1380x770.png 2x" data-dominant-color="575857"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">4599×2568 1.32 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4ba98aac6e20498b67bf0e0b2b4654ac02cfbe0.png" data-download-href="/uploads/short-url/ulT0hCshPn79FSQiyjN5Wv2Gq6k.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d4ba98aac6e20498b67bf0e0b2b4654ac02cfbe0_2_690x387.png" alt="2" data-base62-sha1="ulT0hCshPn79FSQiyjN5Wv2Gq6k" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d4ba98aac6e20498b67bf0e0b2b4654ac02cfbe0_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d4ba98aac6e20498b67bf0e0b2b4654ac02cfbe0_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d4ba98aac6e20498b67bf0e0b2b4654ac02cfbe0_2_1380x774.png 2x" data-dominant-color="636464"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">4591×2575 1.36 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc62a25ce873ffbd9febd3e30ce093f7e22dbc93.png" data-download-href="/uploads/short-url/A0HE0YRFYEqMpYuNvxZCLJRKGNd.png?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc62a25ce873ffbd9febd3e30ce093f7e22dbc93_2_690x388.png" alt="3" data-base62-sha1="A0HE0YRFYEqMpYuNvxZCLJRKGNd" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc62a25ce873ffbd9febd3e30ce093f7e22dbc93_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc62a25ce873ffbd9febd3e30ce093f7e22dbc93_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc62a25ce873ffbd9febd3e30ce093f7e22dbc93_2_1380x776.png 2x" data-dominant-color="717B60"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">4588×2585 1.59 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2020-08-16 21:21 UTC)

<p>Great! Check out Slicer’s visualization and processing capabilities, too. We also have a FreeSurfer extension that can import data sets. There are tons of tools that fsleyes does not have - from virtual reality tractography to real-time surgical navigation with BrainLab/StealthStation/custom tracker, advanced image segmentation and surface editing, cutting, etc.</p>

---
