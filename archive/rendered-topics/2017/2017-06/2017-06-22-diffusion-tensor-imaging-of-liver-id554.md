# Diffusion tensor imaging of liver

**Topic ID**: 554
**Date**: 2017-06-22
**URL**: https://discourse.slicer.org/t/diffusion-tensor-imaging-of-liver/554

---

## Post #1 by @Egor (2017-06-22 11:54 UTC)

<p>Hi all</p>
<p>Is it possible to calculate FA of the liver by 3D slicer?<br>
i’m trying to do that by instructions (DiffusionMRIanalysisTutorial_Slicer4.5_SoniaPujol) Unsuccessfully</p>
<p>Thank you!</p>

---

## Post #2 by @ihnorton (2017-06-22 14:33 UTC)

<p>Speaking generally, yes: aside from brain, I’ve used Slicer tools for spine and abdominal diffusion, as have other people. Provided your scan is a compatible diffusion-weighted image and has sufficient gradient information in the header (Siemens, GE, and Philips are well-supported; others mixed), then it should be possible.</p>
<p>Can you please give more information about what you tried and what the problem was? Some module names have changed a little bit since that tutorial was written, but they should still be close enough to follow the tutorial (look under the <code>Modules-&gt;Diffusion</code> menu to find all the necessary modules).</p>
<p>Note that it is now necessary to install the SlicerDMRI extension separately, and we recommend using the Nightly slicer build rather than 4.6. See below for installation instructions, as well as links to other tutorials:</p>
<p><a href="http://dmri.slicer.org/download/" class="onebox" target="_blank">http://dmri.slicer.org/download/</a></p>

---

## Post #3 by @Egor (2017-06-23 05:30 UTC)

<p>I tried using 3dSlicer 4.5.0.-1 for head imaging and everything was OK. When I try to do the same for the abdomen (liver) there is an error on stage "Diffusion weighted volume masking - complete with errors’'.<br>
Siemens 3T<br>
b-value 50, 400, 800, 1500<br>
6 directions<br>
1 number of signal averages<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f32066e976c967a665fc03de72756a27521b9b42.png" data-download-href="/uploads/short-url/yGNrFvTNbkRspUHU6ImlxctXXFM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f32066e976c967a665fc03de72756a27521b9b42_2_572x500.png" alt="image" data-base62-sha1="yGNrFvTNbkRspUHU6ImlxctXXFM" width="572" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f32066e976c967a665fc03de72756a27521b9b42_2_572x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f32066e976c967a665fc03de72756a27521b9b42.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f32066e976c967a665fc03de72756a27521b9b42.png 2x" data-dominant-color="353535"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">660×576 234 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Thank you!</p>

---

## Post #4 by @Egor (2017-06-23 11:18 UTC)

<p>upd<br>
I managed to calculate FA by using Slicer 4.7.0-2017-06-22 with the SlicerDMRI extension. But only the kidneys, spleen, pancreas and a small part of the liver. How can I fix it? I’m interested in the liver.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e48587c0093ab4c7b6299c52559e94a55a2e45c0.png" data-download-href="/uploads/short-url/wBAWVVRNHkiL3tOlUagL5YPvgxa.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e48587c0093ab4c7b6299c52559e94a55a2e45c0_2_690x387.png" alt="image" data-base62-sha1="wBAWVVRNHkiL3tOlUagL5YPvgxa" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e48587c0093ab4c7b6299c52559e94a55a2e45c0_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e48587c0093ab4c7b6299c52559e94a55a2e45c0_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e48587c0093ab4c7b6299c52559e94a55a2e45c0.png 2x" data-dominant-color="81878D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @ihnorton (2017-06-23 13:01 UTC)

<p>Masking is not required to calculate or measure FA.  The mask probably excludes some areas because the intensity or connectedness is below the threshold. To calculate an FA volume:</p>
<p>Step 1: use Diffusion Tensor Estimation module to calculate a Diffusion Tensor volume from a Diffusion Weighted Volume.<br>
Step 2: use Diffusion Tensor Scalar Maps module with the DTI volume above to generate a Fractional Anisotropy map. Then you can draw ROIs and measure anywhere in the volume using the Segment Editor and Label Statistics tools.</p>

---

## Post #6 by @fedorov (2017-06-24 01:18 UTC)

<p>You can also use the DWModeling module from the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerProstate">SlicerProstate extension</a> to calculate ADC in the liver. There is extensive literature on the utility of ADC in quantifying liver disease, e.g., see <a href="https://scholar.google.com/scholar?hl=en&amp;q=liver+adc+mri">https://scholar.google.com/scholar?hl=en&amp;q=liver+adc+mri</a>.</p>

---

## Post #7 by @Egor (2017-06-26 13:24 UTC)

<p>Thank you!<br>
Is there any difference how to measure FA from DTI volume? I calculate it by drawing ROIs. Should I use the Segment Editor or Label Statistics tools?</p>

---

## Post #8 by @Egor (2017-06-26 13:30 UTC)

<p>Hi<br>
Is there any guide for DWModeling? There is always an error.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/c99e41d5f42b95e18f28adb16e9b05a74724a740.jpg" data-download-href="/uploads/short-url/sLB2ekhHeB8Wtor2zxHPHtKWAkE.jpg?dl=1" title="image.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/c99e41d5f42b95e18f28adb16e9b05a74724a740_2_690x387.jpg" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/c99e41d5f42b95e18f28adb16e9b05a74724a740_2_690x387.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/c99e41d5f42b95e18f28adb16e9b05a74724a740_2_1035x580.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c99e41d5f42b95e18f28adb16e9b05a74724a740.jpeg 2x" data-dominant-color="7E8083"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">1366×768 237 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @fedorov (2017-06-26 13:44 UTC)

<p>It’s a shame, but there is no guide… It’s been on my list for a very long time.</p>
<p>What is the error?</p>
<p>Did you specify output volume nodes?</p>

---

## Post #10 by @Egor (2017-06-26 14:02 UTC)

<p>I think it is an application error.<br>
What should I choose in “Output common to all models” to get ADC maps?</p>

---

## Post #11 by @fedorov (2017-06-26 15:26 UTC)

<aside class="quote no-group" data-username="Egor" data-post="10" data-topic="554">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/6de8d8/48.png" class="avatar"> Egor:</div>
<blockquote>
<p>What should I choose in “Output common to all models” to get ADC maps?</p>
</blockquote>
</aside>
<p>This depends on whether you need any of the outputs listed in that section. None of them is required. You can keep them all non-initialized.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de7c59d483bfb8f9b3fa6a8254d73b257098d8af.png" data-base62-sha1="vKcpYGibR6NliDqdy3ReTalFGaj" width="274" height="184"></p>
<p>If you need any of those outputs, just create a new empty node from the node selector.</p>
<p>The model-specific outputs should be initialized depending on what model you selected. From your screenshot, you chose bi-exponential model, so you can initialize the maps produced by that model:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62c37c9ccc7b9664b16a108c7785d4b265ec9350.png" data-base62-sha1="e5HCttEHXMuDJgswjarNmcMtiTu" width="270" height="133"></p>
<p>Also note that if you don’t specify anything in the “Input mask” selector, the module will be fitting the model to every pixel in the image, which is usually not what you want and may take significant time. To limit the region of where the model should be fit, you can first create a mask. Go to “MultiVolume Explorer” module, extract single frame from the multivolume:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb04dded23dac729c392db1d47e0c79655a91695.png" data-download-href="/uploads/short-url/zOCgSYKkGftKPzH7cOqD9Ron8Y5.png?dl=1" title="image.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/fb04dded23dac729c392db1d47e0c79655a91695_2_690x262.png" data-base62-sha1="zOCgSYKkGftKPzH7cOqD9Ron8Y5" width="690" height="262" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/fb04dded23dac729c392db1d47e0c79655a91695_2_690x262.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb04dded23dac729c392db1d47e0c79655a91695.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb04dded23dac729c392db1d47e0c79655a91695.png 2x" data-dominant-color="E2E2E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">739×281 55.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Next you can make a label for that single frame using legacy Editor module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ef8325b6f29915ba5a493f69ef5d0fc79586396.png" data-download-href="/uploads/short-url/8Z3ms9flaq9YZOY4Nz3fQY9VpL8.png?dl=1" title="image.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/3ef8325b6f29915ba5a493f69ef5d0fc79586396_2_690x499.png" data-base62-sha1="8Z3ms9flaq9YZOY4Nz3fQY9VpL8" width="690" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/3ef8325b6f29915ba5a493f69ef5d0fc79586396_2_690x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ef8325b6f29915ba5a493f69ef5d0fc79586396.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ef8325b6f29915ba5a493f69ef5d0fc79586396.png 2x" data-dominant-color="BCBBBA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">920×666 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After that you can specify the mask in DWModeling, and create new nodes for each of the maps matching the model you selected:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f468f290b7b8c7b3c487e554e747f1b1a2e2f3b.png" data-download-href="/uploads/short-url/mJ15AR5haDsLYC9RwJ75o6dd9AT.png?dl=1" title="image.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9f468f290b7b8c7b3c487e554e747f1b1a2e2f3b_2_372x500.png" data-base62-sha1="mJ15AR5haDsLYC9RwJ75o6dd9AT" width="372" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9f468f290b7b8c7b3c487e554e747f1b1a2e2f3b_2_372x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9f468f290b7b8c7b3c487e554e747f1b1a2e2f3b_2_558x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f468f290b7b8c7b3c487e554e747f1b1a2e2f3b.png 2x" data-dominant-color="ECEBEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">657×881 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If that process finishes without errors, you should see the maps initialized:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b0f637a549270cff5035b00957af19577cbd7e7.png" data-base62-sha1="1zQdLCMYa30F55G6opq5P5XgMqb" width="402" height="430"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28aabdfb774bc5db24004f6d15e519ec79a87717.png" data-base62-sha1="5NKUybzSxRgjhKXjdNWUVkg6FAH" width="401" height="404"></p>
<p>If you are getting an error, please let us know what is in the error log:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae2310c846f940a4ad22ac4dc9f1d04fa8c61b93.png" data-download-href="/uploads/short-url/oQucRuNNggOSnrpw3I6WWO0oek3.png?dl=1" title="image.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ae2310c846f940a4ad22ac4dc9f1d04fa8c61b93_2_690x87.png" data-base62-sha1="oQucRuNNggOSnrpw3I6WWO0oek3" width="690" height="87" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ae2310c846f940a4ad22ac4dc9f1d04fa8c61b93_2_690x87.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae2310c846f940a4ad22ac4dc9f1d04fa8c61b93.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae2310c846f940a4ad22ac4dc9f1d04fa8c61b93.png 2x" data-dominant-color="E3E8ED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">886×112 11.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @Egor (2017-06-27 05:41 UTC)

<p>The error log is empty.<br>
I tried to choose and not to choose the outputs. unsuccessfuly<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/fa68b95d8b1e779805d8bccd5fa8e5b2cdaec60f.jpg" data-download-href="/uploads/short-url/zJdJKAzyHJiqItIDCvF1MPxpda7.jpg?dl=1" title="image.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/fa68b95d8b1e779805d8bccd5fa8e5b2cdaec60f_2_690x387.jpg" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/fa68b95d8b1e779805d8bccd5fa8e5b2cdaec60f_2_690x387.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/fa68b95d8b1e779805d8bccd5fa8e5b2cdaec60f_2_1035x580.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa68b95d8b1e779805d8bccd5fa8e5b2cdaec60f.jpeg 2x" data-dominant-color="909497"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">1366×768 278 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #13 by @fedorov (2017-06-27 11:06 UTC)

<p><a class="mention" href="/u/egor">@Egor</a> sorry for the trouble - any chance you can share the de-identified dataset so I can investigate what is going on?</p>

---

## Post #14 by @Egor (2017-06-27 11:40 UTC)

<p>Of course. This is my abdomen (without breathhold) so I don’t mind)<br>
Generally I’m going to calculate ADC and FA of fetal lung. So now I’m testing the possibility of measuring these indices on the liver.</p>

---

## Post #15 by @fedorov (2017-06-30 16:28 UTC)

<p>After following up with <a class="mention" href="/u/egor">@Egor</a> by email, it appears that the DWI data had multiple directions. DWModeling expects trace DW images as input. In fact, I should have noticed this earlier, since in one of the screenshot it is clear that the multivolume was parsed by AcquisitionTime, not b-value. Such data is not suitable for DWModeling analysis.</p>

---
