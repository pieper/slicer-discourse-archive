# Diffusion brain masking

**Topic ID**: 7811
**Date**: 2019-07-30
**URL**: https://discourse.slicer.org/t/diffusion-brain-masking/7811

---

## Post #1 by @Lungimiro (2019-07-30 12:44 UTC)

<p>Operating system: MacOS Mojave 10.14<br>
Slicer version: 4.10.2<br>
MR: Philips</p>
<p>Hello!!<br>
I wanna create a diffusion brain mask but I have the following problem:</p>
<p>"Diffusion Brain Masking standard error:</p>
<p>ERROR: In /Volumes/Dashboards/Stable/Slicer-4102-build/VTK/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx, line 709<br>
vtkCompositeDataPipeline (0x7f886719a800): Input port 0 of algorithm vtkImageWeightedSum(0x7f8867199d20) has 0 connections but is not optional.</p>
<p>/Applications/Slicer.app/Contents/Extensions-28257/SlicerDMRI/lib/Slicer-4.10/cli-modules/DiffusionWeightedVolumeMasking: Error parsing Diffusion information, no B0 images"</p>
<p>I have DWI images in DICOM. In the converter (diffusion - import and export - diffusion weighted DICOM import (DWI convert) transformed the images into “nrrd”.</p>
<p>I can not change the “DWI Component” parameter (module Volumes, field Scalar Display). Besides the value of “DWI Component” is 0. How can I make 10?</p>
<p>Thank you so much!</p>

---

## Post #2 by @ljod (2019-07-30 14:13 UTC)

<p>Hi this sounds like it is not actually DWI data. Please check your original DICOM data and acquisition. It may be a trace image with one component instead of the required components (usually 20 or more) needed for diffusion tensor analyses.</p>

---

## Post #3 by @Lungimiro (2019-08-07 11:44 UTC)

<p>HI!<br>
I’m sure that:<br>
my format data is dicom classic;<br>
my data represents DWI data;<br>
data was been acquired considering 2 b-values and 15 gradient directions.<br>
Besides I have exported my file from workstation!</p>
<p>I send you dicom data and the screenshots of my file!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2550fec60869da9e679db5564e648a9a3dea5c8.png" data-download-href="/uploads/short-url/wie9v4KerJU3X5IQQcpQW8nRQUw.png?dl=1" title="05" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2550fec60869da9e679db5564e648a9a3dea5c8_2_690x449.png" alt="05" data-base62-sha1="wie9v4KerJU3X5IQQcpQW8nRQUw" width="690" height="449" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2550fec60869da9e679db5564e648a9a3dea5c8_2_690x449.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2550fec60869da9e679db5564e648a9a3dea5c8.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2550fec60869da9e679db5564e648a9a3dea5c8.png 2x" data-dominant-color="242527"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">05</span><span class="informations">1010×658 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Lungimiro (2019-08-07 11:44 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddc71abbec0119f5a92e8ab9b82db03cbb43093f.png" data-download-href="/uploads/short-url/vDW6dkJgivZ9DbMgpo9jZdtUlA3.png?dl=1" title="14" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddc71abbec0119f5a92e8ab9b82db03cbb43093f.png" alt="14" data-base62-sha1="vDW6dkJgivZ9DbMgpo9jZdtUlA3" width="547" height="499" data-dominant-color="E8E8E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">14</span><span class="informations">814×744 27.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Lungimiro (2019-08-07 11:45 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0aed8c732043d0d8d575fb5b58ff02c51a82cece.png" data-download-href="/uploads/short-url/1yFIEPOirAcdASNbBPCA1yceZau.png?dl=1" title="22" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0aed8c732043d0d8d575fb5b58ff02c51a82cece.png" alt="22" data-base62-sha1="1yFIEPOirAcdASNbBPCA1yceZau" width="426" height="500" data-dominant-color="EEEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">22</span><span class="informations">636×745 26.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @Lungimiro (2019-08-07 11:45 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/427604ec994ea3e79301fda5f75b248121f8ddad.png" data-download-href="/uploads/short-url/9tWmOXkht9N9ins1UN9SVfgeuhD.png?dl=1" title="54" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/427604ec994ea3e79301fda5f75b248121f8ddad.png" alt="54" data-base62-sha1="9tWmOXkht9N9ins1UN9SVfgeuhD" width="211" height="500" data-dominant-color="EBEBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">54</span><span class="informations">317×749 11.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @Lungimiro (2019-08-07 11:46 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f26a60abaa51d3b2d1f6a9b59d0bcdbf402c864.png" data-download-href="/uploads/short-url/90ESRuKGFBQaHPCEiDaC2Jw6Psw.png?dl=1" title="43" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f26a60abaa51d3b2d1f6a9b59d0bcdbf402c864.png" alt="43" data-base62-sha1="90ESRuKGFBQaHPCEiDaC2Jw6Psw" width="690" height="484" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">43</span><span class="informations">1066×748 25.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @Lungimiro (2019-08-07 11:48 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/cac883d4aec9ad3b6d433018be64dac2665a0b17.png" data-download-href="/uploads/short-url/sVU37Aa0jQ911ASh1FK121tIiiz.png?dl=1" title="03" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/cac883d4aec9ad3b6d433018be64dac2665a0b17.png" alt="03" data-base62-sha1="sVU37Aa0jQ911ASh1FK121tIiiz" width="270" height="500" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">03</span><span class="informations">404×746 12.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @ljod (2019-08-07 12:47 UTC)

<p>In that case please use Slicer 4.10 and make sure you load data with either the DWIConvert or DCM2nii module. Then look in the Volumes module of Slicer and check that you can see all the expected components (b0 and gradient images). Then please send an explanation of exactly what steps you took, including module names, and the result.</p>

---

## Post #10 by @Lungimiro (2019-08-08 08:06 UTC)

<p>My 3dslicer version is 4.10.2. I send you my steps now. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08d9638bf683e5c7ce899fdd72d335f47742e26e.jpeg" data-download-href="/uploads/short-url/1ghzxwdSOsrm9mLKsdYQiZrQ4CW.jpeg?dl=1" title="28" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/08d9638bf683e5c7ce899fdd72d335f47742e26e_2_690x429.jpeg" alt="28" data-base62-sha1="1ghzxwdSOsrm9mLKsdYQiZrQ4CW" width="690" height="429" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/08d9638bf683e5c7ce899fdd72d335f47742e26e_2_690x429.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/08d9638bf683e5c7ce899fdd72d335f47742e26e_2_1035x643.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/08d9638bf683e5c7ce899fdd72d335f47742e26e_2_1380x858.jpeg 2x" data-dominant-color="999A9A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">28</span><span class="informations">1440×896 209 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24afebd0ef8be592a682585bb5e4118dffee7071.jpeg" data-download-href="/uploads/short-url/5ey65M1K8HVPQvcoKH5ZFpS1vkB.jpeg?dl=1" title="06" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24afebd0ef8be592a682585bb5e4118dffee7071_2_690x406.jpeg" alt="06" data-base62-sha1="5ey65M1K8HVPQvcoKH5ZFpS1vkB" width="690" height="406" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24afebd0ef8be592a682585bb5e4118dffee7071_2_690x406.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24afebd0ef8be592a682585bb5e4118dffee7071_2_1035x609.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24afebd0ef8be592a682585bb5e4118dffee7071_2_1380x812.jpeg 2x" data-dominant-color="A9AAAB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">06</span><span class="informations">1389×818 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95ae7151051c00963537499c968c5f389dea8507.jpeg" data-download-href="/uploads/short-url/lm8SQV50sv1qFkNdqsThlF6bkRV.jpeg?dl=1" title="51" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95ae7151051c00963537499c968c5f389dea8507_2_690x431.jpeg" alt="51" data-base62-sha1="lm8SQV50sv1qFkNdqsThlF6bkRV" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95ae7151051c00963537499c968c5f389dea8507_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95ae7151051c00963537499c968c5f389dea8507_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95ae7151051c00963537499c968c5f389dea8507_2_1380x862.jpeg 2x" data-dominant-color="ADACAC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">51</span><span class="informations">1440×900 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @Lungimiro (2019-08-08 08:06 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2e48c6adc0d5646ea232c45105140c9973152a8.jpeg" data-download-href="/uploads/short-url/u5DVLunfqhdFK4bAE1P5Qj0qbK8.jpeg?dl=1" title="07" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d2e48c6adc0d5646ea232c45105140c9973152a8_2_690x431.jpeg" alt="07" data-base62-sha1="u5DVLunfqhdFK4bAE1P5Qj0qbK8" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d2e48c6adc0d5646ea232c45105140c9973152a8_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d2e48c6adc0d5646ea232c45105140c9973152a8_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d2e48c6adc0d5646ea232c45105140c9973152a8_2_1380x862.jpeg 2x" data-dominant-color="AFAEAE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">07</span><span class="informations">1440×900 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @ljod (2019-08-08 23:38 UTC)

<p>Are you able to share the nrrd data via Dropbox or similar? The error means it is not finding any baseline (b-value near 0) images in the dataset. Every DWI acquisition should have one or more of these.</p>

---

## Post #13 by @Lungimiro (2019-08-12 07:38 UTC)

<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="16" height="16">
      <a href="https://www.dropbox.com/sh/vpbofbds1y0lvqk/AADzMg7PJ7-7aShUAIlpyh-Ha?dl=0" target="_blank" rel="nofollow noopener">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://www.dropbox.com/sh/vpbofbds1y0lvqk/AADzMg7PJ7-7aShUAIlpyh-Ha?dl=0" target="_blank" rel="nofollow noopener">Diffusion pugliese</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #14 by @zhangfanmark (2019-08-14 13:54 UTC)

<p><a class="mention" href="/u/lungimiro">@Lungimiro</a><br>
The issue is that the DICOM files cannot be successfully converted to NRRD.</p>
<p>The NRRD file you uploaded has only two diffusion weighted images (both are b=0). I also tried by myself using both DWIConvert and Dcm2niix (a new module that was recently added in SlicerDMRI to convert DICOM). They gave the similar output, that only two DW images can be identified.</p>
<p>Looking into the log file from Dcm2niix, it says “Error: Conversion aborted due to corrupt file: /Users/fan/Desktop/Diffusionpugliese/FILEDICOM/XX_0050”</p>
<p>I am not entirely sure why this happened, but it seems there is something unusual in the input data, if you could try to export it again, or try on data from a different subject.</p>
<p><a class="mention" href="/u/ljod">@ljod</a></p>
<p>Regards,<br>
Fan</p>

---

## Post #15 by @Nicholas.jacobson (2020-08-20 22:28 UTC)

<p>Hi all,<br>
I too am getting an issue with the Brain Masking with an error stating there is no b0.</p>
<p>C:/Users/18166/AppData/Roaming/NA-MIC/Extensions-28257/SlicerDMRI/lib/Slicer-4.10/cli-modules/DiffusionWeightedVolumeMasking.exe: Error parsing Diffusion information, no B0 images</p>
<p>The files I have contain 34 directions. There is a multivolume and a DTI volume file as well. None of which are behaving. This is my first attempt with unique de-identified information. Any advice would be welcome.</p>

---

## Post #16 by @aysegul_sayin (2022-05-07 13:50 UTC)

<p>Hello, I keep getting this error. I’m trying different dwi files but I get the same error every time. Is there a complete solution for this error? Can you suggest me a sample file where this error is not received?</p>

---

## Post #17 by @Mulik_Tv (2022-12-26 12:14 UTC)

<p>I have  same problem with diffusion weight masking I’m using 5.3.3 virsion</p>
<ol>
<li>I convert dicom to nrrd using dicom converter<br>
2 . Then used diffusion brain masking<br>
Out put and  basline  can I edit but input  I’m not able to change<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f09a752e0e560a725ca6ee469aa6c011c25e8c0.jpeg" data-download-href="/uploads/short-url/4qzu1OQJJk9siVDq0pAMYSsYGgo.jpeg?dl=1" title="IMG_20221207_150630" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f09a752e0e560a725ca6ee469aa6c011c25e8c0_2_225x500.jpeg" alt="IMG_20221207_150630" data-base62-sha1="4qzu1OQJJk9siVDq0pAMYSsYGgo" width="225" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f09a752e0e560a725ca6ee469aa6c011c25e8c0_2_225x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f09a752e0e560a725ca6ee469aa6c011c25e8c0_2_337x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f09a752e0e560a725ca6ee469aa6c011c25e8c0_2_450x1000.jpeg 2x" data-dominant-color="A58F7E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20221207_150630</span><span class="informations">1800×4000 772 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
</li>
</ol>

---

## Post #18 by @pieper (2022-12-26 16:20 UTC)

<p>that image indicates that the images were not converted into a valid diffusion weighted volume.</p>

---

## Post #19 by @tfxue (2022-12-29 06:33 UTC)

<p>Hi,</p>
<p>I am able to load the DWI volume and the brain mask into this module (Diffusion Tensor Estimation). I am using 5.0.3 on Mac.</p>
<ol>
<li>Can you have a look at your DWI using “Volume” module. Are all scans from different gradient directions correctly loaded? As <a class="mention" href="/u/pieper">@pieper</a> said, the convert from DICOM to nrrd might not be correct.</li>
<li>You should load the brain mask as “labelmap volume” in order to be used in that module.</li>
</ol>
<p>Hope it helps.</p>

---

## Post #20 by @Mulik_Tv (2023-01-07 17:22 UTC)

<p>Hi,<br>
Can Hi get your email so that can communicate properly.<br>
So I fix this problem</p>

---

## Post #21 by @Mulik_Tv (2023-01-07 17:24 UTC)

<p>So how can I fix this problem</p>

---

## Post #22 by @Mulik_Tv (2023-01-16 08:29 UTC)

<p><span class="mention">@Tengfei</span> Xue I’ve 1st uploaded the series of dicom in the 3d slicer 5.3.0 a in windows and then converted into NRRD format but the images as <a class="mention" href="/u/pieper">@pieper</a> said, might be image are not converting into NRRD format so how can I come over this and this happens to every neuroimage</p>

---
