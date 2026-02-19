---
topic_id: 9156
title: "Problems With Conversion Dicom Files To Nrrd With Dti"
date: 2019-11-15
url: https://discourse.slicer.org/t/9156
---

# Problems with conversion DICOM files to NRRD with DTI

**Topic ID**: 9156
**Date**: 2019-11-15
**URL**: https://discourse.slicer.org/t/problems-with-conversion-dicom-files-to-nrrd-with-dti/9156

---

## Post #1 by @Santiago_Cutiller (2019-11-15 13:59 UTC)

<p>Hello, A few month ago I started to use 3D Slicer to create tractographys. Usually I use DWIconvert and then Difussion Brain Masking and Difussion Tensor Estimation. I’m trying to do the same but the next error comes up when I use Difussion Brain Masking: “Diffusion Brain Masking standard error:<br>
C:/Users/Usuario/AppData/Roaming/NA-MIC/Extensions-28257/SlicerDMRI/lib/Slicer-4.10/cli-modules/DiffusionWeightedVolumeMasking.exe: Error parsing Diffusion information, no B0 images”.<br>
After I use Difussion Tensor Estimator a black image appears.<br>
in the volume tool the number of the scale is 17.</p>
<p>I hope you can give me an answer to my problem<br>
sincerely Santiago</p>

---

## Post #2 by @zhangfanmark (2019-11-15 14:33 UTC)

<p>Hi Santiago,</p>
<p>As the error message says, there may be no baseline image in your data. You may want to look into that.</p>
<p>Also, when you look at the converted DWI data, does it look good to you?</p>
<p>Regards,<br>
Fan</p>

---

## Post #3 by @Santiago_Cutiller (2019-11-16 02:33 UTC)

<p>Hi, Thanks for answer!</p>
<p>The conversion from dcm to DWI its allright, I can also see the image corresponding to b0</p>
<p>I’ll explain the steps I followed.<br>
This is the list of dcm files:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0453b4f69a46bf17a1ede2c2d315acb61a2c1f7.png" data-download-href="/uploads/short-url/yhwV6HIq47DJiUBWUvfHU220oxV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0453b4f69a46bf17a1ede2c2d315acb61a2c1f7_2_690x390.png" alt="image" data-base62-sha1="yhwV6HIq47DJiUBWUvfHU220oxV" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0453b4f69a46bf17a1ede2c2d315acb61a2c1f7_2_690x390.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0453b4f69a46bf17a1ede2c2d315acb61a2c1f7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0453b4f69a46bf17a1ede2c2d315acb61a2c1f7.png 2x" data-dominant-color="E3E5E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">904×512 329 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then I use DWIconvert<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/339ca731f4042a9247275cf07bdede51208202d9.png" data-download-href="/uploads/short-url/7mzYGdsSk9pLMbCq0JEWQ257cMN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/339ca731f4042a9247275cf07bdede51208202d9_2_690x388.png" alt="image" data-base62-sha1="7mzYGdsSk9pLMbCq0JEWQ257cMN" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/339ca731f4042a9247275cf07bdede51208202d9_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/339ca731f4042a9247275cf07bdede51208202d9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/339ca731f4042a9247275cf07bdede51208202d9.png 2x" data-dominant-color="B6B6BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">965×544 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The result is accurate and I can select the DWI component in the volume module<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa84959c032e2a36d8975ee0bcf45d6e6044315f.png" data-download-href="/uploads/short-url/zKbqyMMJCO8RGPSytVsY37u6f2n.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa84959c032e2a36d8975ee0bcf45d6e6044315f_2_690x388.png" alt="image" data-base62-sha1="zKbqyMMJCO8RGPSytVsY37u6f2n" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa84959c032e2a36d8975ee0bcf45d6e6044315f_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa84959c032e2a36d8975ee0bcf45d6e6044315f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa84959c032e2a36d8975ee0bcf45d6e6044315f.png 2x" data-dominant-color="A4A5B3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">962×542 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/303ac4a42d72eaa0d09487b98602fae80358bbe0.png" data-download-href="/uploads/short-url/6SEPnB6TcPKoIVStIN83E2R6Rji.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/303ac4a42d72eaa0d09487b98602fae80358bbe0_2_690x388.png" alt="image" data-base62-sha1="6SEPnB6TcPKoIVStIN83E2R6Rji" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/303ac4a42d72eaa0d09487b98602fae80358bbe0_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/303ac4a42d72eaa0d09487b98602fae80358bbe0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/303ac4a42d72eaa0d09487b98602fae80358bbe0.png 2x" data-dominant-color="9F9FAC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">962×542 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
BUT… When I want to create the mask this mistake comes out:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df3aef9969e7105209ac42a6449c1099f99293ab.png" data-download-href="/uploads/short-url/vQMKdXGcKXlFjSEY5MzTZtOzyZR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df3aef9969e7105209ac42a6449c1099f99293ab_2_690x388.png" alt="image" data-base62-sha1="vQMKdXGcKXlFjSEY5MzTZtOzyZR" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df3aef9969e7105209ac42a6449c1099f99293ab_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df3aef9969e7105209ac42a6449c1099f99293ab.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df3aef9969e7105209ac42a6449c1099f99293ab.png 2x" data-dominant-color="CACBD3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">962×542 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried to convert dcm to nrrd with MRIcon but the same mistakes comes out again</p>
<p>I expect your answer!</p>
<p>Regards</p>
<p>Santiago.</p>

---

## Post #4 by @zhangfanmark (2019-11-16 14:36 UTC)

<p>Hi!</p>
<p>Yes, I agree that the data looks good. One thing we can check is to look at the actual b values in your data.</p>
<p>In conversion options, please chose DicomToFSL to output nifti format of the DWI data. In the output bval file, you will see the actual b values. Please check if there are b=0 inside.</p>
<p>Regards,<br>
Fan</p>

---

## Post #5 by @Santiago_Cutiller (2019-11-23 15:15 UTC)

<p>Hi!<br>
I could not get the bval file with 3D slicer but I used MRIcron to create the NIfTI file and then I opened it up with DTI studio and got the next info…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84e9f551ade4964a93e37f1e400ddb020719d8e9.jpeg" data-download-href="/uploads/short-url/iXOhk0bjve4XAWPr24X7lZHRClj.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/84e9f551ade4964a93e37f1e400ddb020719d8e9_2_690x396.jpeg" alt="image" data-base62-sha1="iXOhk0bjve4XAWPr24X7lZHRClj" width="690" height="396" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/84e9f551ade4964a93e37f1e400ddb020719d8e9_2_690x396.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84e9f551ade4964a93e37f1e400ddb020719d8e9.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84e9f551ade4964a93e37f1e400ddb020719d8e9.jpeg 2x" data-dominant-color="EFEFF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">970×557 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43dd8ee81f5c7b99cc5b703234c71d9774b865bb.png" data-download-href="/uploads/short-url/9GmFXLijbmQMkz3O3GXSW6m3DgT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43dd8ee81f5c7b99cc5b703234c71d9774b865bb_2_631x500.png" alt="image" data-base62-sha1="9GmFXLijbmQMkz3O3GXSW6m3DgT" width="631" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43dd8ee81f5c7b99cc5b703234c71d9774b865bb_2_631x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43dd8ee81f5c7b99cc5b703234c71d9774b865bb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43dd8ee81f5c7b99cc5b703234c71d9774b865bb.png 2x" data-dominant-color="EDEEEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">705×558 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/998f27fdb4fc3c9350a1cb0e3be5f04164d71da2.png" data-download-href="/uploads/short-url/lUrLlSa0SDoGPxLNMrZTru5vC0O.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/998f27fdb4fc3c9350a1cb0e3be5f04164d71da2_2_690x367.png" alt="image" data-base62-sha1="lUrLlSa0SDoGPxLNMrZTru5vC0O" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/998f27fdb4fc3c9350a1cb0e3be5f04164d71da2_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/998f27fdb4fc3c9350a1cb0e3be5f04164d71da2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/998f27fdb4fc3c9350a1cb0e3be5f04164d71da2.png 2x" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">965×514 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I guess there is missed info in this files. Is there a way to get it back?</p>

---

## Post #6 by @zhangfanmark (2019-11-24 15:07 UTC)

<p>Yes, looks there is something wrong with the gradient table for this dataset. I am not aware if there is good way to recover. If you can another dataset scanned using the save acquisition parameters on your site. You can use the gradient table from that dataset.</p>
<p>Regards<br>
Fan</p>

---
