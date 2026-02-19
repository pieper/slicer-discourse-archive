---
topic_id: 719
title: "Dwi To Dti Estimation Problem"
date: 2017-07-20
url: https://discourse.slicer.org/t/719
---

# DWI to DTI Estimation Problem

**Topic ID**: 719
**Date**: 2017-07-20
**URL**: https://discourse.slicer.org/t/dwi-to-dti-estimation-problem/719

---

## Post #1 by @AsliBeriL (2017-07-20 01:25 UTC)

<p>Operating system: Win 10 Pro<br>
Slicer version: 4.5.0-1</p>
<p>Hello everyone,</p>
<p>I want DWI images convert to DTI and tractography. First step, i created .nrrd file, baseline and mask. Later, DWI to DTI estimation module is working but i can’t see DTI images. The screen is seeming black blank. How can I fix the problem?</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2017-07-20 01:26 UTC)

<p>To get started, download the latest <strong>nightly</strong> version of Slicer and install the SlicerDMRI extension.</p>

---

## Post #3 by @AsliBeriL (2017-07-20 02:10 UTC)

<p>Thank you for quick response. I setup 4.7.0-2017-07-18 version and installed DMRI extension. I got error message:</p>
<p>Diffusion Brain Masking standard error:</p>
<p>C:/Users/mehme/AppData/Roaming/NA-MIC/Extensions-26156/SlicerDMRI/lib/Slicer-4.7/cli-modules/DiffusionWeightedVolumeMasking.exe: Error parsing Diffusion information, no B0 images</p>

---

## Post #4 by @ihnorton (2017-07-20 13:53 UTC)

<p>What are your B-values? The default maximum B-value is 100 in order to be considered a B0, but that can be changed under the <code>Mask Settings</code>:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/c4fab6fece259cda8a015c125d64ace0730c1c9e.png" data-download-href="/uploads/short-url/s6yJLOiKAhQEMDaJFSn4Ev252z4.png?dl=1" title="image.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/c4fab6fece259cda8a015c125d64ace0730c1c9e_2_690x72.png" width="690" height="72" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/c4fab6fece259cda8a015c125d64ace0730c1c9e_2_690x72.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4fab6fece259cda8a015c125d64ace0730c1c9e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4fab6fece259cda8a015c125d64ace0730c1c9e.png 2x" data-dominant-color="F3F3F3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">732×77 5.17 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @AsliBeriL (2017-07-22 13:05 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="4" data-topic="719">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>What are your B-values? The default maximum B-value is 100 in order to be considered a B0, but that can be changed under the Mask Settings:</p>
</blockquote>
</aside>
<p>My B-values are automatic 100 in mask settings. As if i change baseline B-value threshold parameter, i got error message. How i can learn B-values? I want my DWI images analyses for tractography so 3D slicer 4.5 and 4.7 nightly version but i got error message or i seen black screen. I tried diffusion MRI tutorial data so i could. But my datas (20 different patients on DWI images) are failed. How can i fix it? I’ve been struggling for 2 weeks.</p>

---

## Post #6 by @AsliBeriL (2017-07-22 13:18 UTC)

<p>I think my b-values are 1000.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/813cc09ce8f4a935b151728b45d75ae58f8d7f1b.png" data-download-href="/uploads/short-url/irhKOzDTguHPGS01s1bSuTa5Xth.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/813cc09ce8f4a935b151728b45d75ae58f8d7f1b_2_690x388.png" alt="image" data-base62-sha1="irhKOzDTguHPGS01s1bSuTa5Xth" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/813cc09ce8f4a935b151728b45d75ae58f8d7f1b_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/813cc09ce8f4a935b151728b45d75ae58f8d7f1b_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/813cc09ce8f4a935b151728b45d75ae58f8d7f1b_2_1380x776.png 2x" data-dominant-color="090A0A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1600×900 33.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @ljod (2017-07-22 13:51 UTC)

<p>It is not clear if your dataset has multiple diffusion weighted images or just one image. Please check if your data is in fact a DWI image that is compatible with DTI analysis. In the Volumes module, you should be able to see multiple components in your DWI (multiple diffusion-weighted images from the application of multiple diffusion-sensitizing gradients). Look at Volumes-&gt;Volume Information-&gt;Number of Scalars. This must be 7 or higher for DTI analysis. Then you can go to Display-&gt;Scalar Display to visualize each DWI component.</p>

---

## Post #8 by @AsliBeriL (2017-07-22 14:20 UTC)

<p>Thank you for your quick response Lauren. My number of scalars are empty? So i can’t move scalar display bar.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/6096424f4995d735c8f354035290d131b87be05e.png" data-download-href="/uploads/short-url/dMrLt5XiJpmAhmOg45F5wfYEmRg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/6096424f4995d735c8f354035290d131b87be05e_2_690x388.png" alt="image" data-base62-sha1="dMrLt5XiJpmAhmOg45F5wfYEmRg" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/6096424f4995d735c8f354035290d131b87be05e_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/6096424f4995d735c8f354035290d131b87be05e_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/6096424f4995d735c8f354035290d131b87be05e_2_1380x776.png 2x" data-dominant-color="7E7E85"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1600×900 208 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e36d53875ac50169785d4010825f989b319d40c3.png" data-download-href="/uploads/short-url/wrUCcXFGs5WJyWyYxyUSZ2D9OAr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e36d53875ac50169785d4010825f989b319d40c3_2_690x388.png" alt="image" data-base62-sha1="wrUCcXFGs5WJyWyYxyUSZ2D9OAr" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e36d53875ac50169785d4010825f989b319d40c3_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e36d53875ac50169785d4010825f989b319d40c3_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e36d53875ac50169785d4010825f989b319d40c3_2_1380x776.png 2x" data-dominant-color="7D7D83"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1600×900 226 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @AsliBeriL (2017-07-22 14:23 UTC)

<p>My data images are multiple DWI.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89d2a2b0a6a96f37f04be702a291b769e41d16a8.png" data-download-href="/uploads/short-url/jFeHgU5B3RVvRyGkxvBOmYXFDvy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89d2a2b0a6a96f37f04be702a291b769e41d16a8_2_690x388.png" alt="image" data-base62-sha1="jFeHgU5B3RVvRyGkxvBOmYXFDvy" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89d2a2b0a6a96f37f04be702a291b769e41d16a8_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89d2a2b0a6a96f37f04be702a291b769e41d16a8_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89d2a2b0a6a96f37f04be702a291b769e41d16a8_2_1380x776.png 2x" data-dominant-color="EFF0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1600×900 97.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @ihnorton (2017-07-22 15:38 UTC)

<p>Each of those individual files is relatively small and may only be a single slice each. So this might be the slices for only a single volume. Note that there are other kinds of diffusion scans (or scalar output from the scanner such as ADC maps) which are not compatible with DTI analysis. You could share some (<strong>!anonymized!</strong>) headers to get feedback, see instructions here:</p>
<aside class="quote quote-modified" data-post="9" data-topic="716">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/problem-with-sagittal-and-coronal-view-from-ccta-dicom-files/716/9">Problem with sagittal and coronal view from CCTA DICOM files</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    To make it easier to share the metadata with us for analysis, I’ve added the option to copy the metadata to clipboard. Could you please download the latest nightly version of Slicer now (if you downloaded Slicer yesterday or before then it is too old, it does not contain this feature yet), and then: 

Open DICOM browser
Select the image that you want to load
Check Advanced checkbox
Click Examine button
Click Metadata button
Click Copy Metadata button
Paste the copied text to any text editor
Remo…
  </blockquote>
</aside>

<p>But probably the best option is to contact whoever is responsible for scanning these images to verify the scanning protocol.</p>

---

## Post #11 by @AsliBeriL (2017-07-22 17:07 UTC)

<p>My metadatas:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/064bed934f0ec1bbe1af1979737fd125bbd2db8c.jpg" data-download-href="/uploads/short-url/THxthehRYS2PPD4APK0dm9Qp2Y.jpg?dl=1" title="Adsız.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/064bed934f0ec1bbe1af1979737fd125bbd2db8c_2_690x388.jpg" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/064bed934f0ec1bbe1af1979737fd125bbd2db8c_2_690x388.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/064bed934f0ec1bbe1af1979737fd125bbd2db8c_2_1035x582.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/064bed934f0ec1bbe1af1979737fd125bbd2db8c_2_1380x776.jpg 2x" data-dominant-color="EFEFEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Adsız.jpg</span><span class="informations">1600×900 239 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/9c27fbbbc602b788043df8a39fc102b737a4feaa.jpg" data-download-href="/uploads/short-url/mhq9fRuXNHBsMXNtoNYHd4fc7Ee.jpg?dl=1" title="Adsız1.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9c27fbbbc602b788043df8a39fc102b737a4feaa_2_690x388.jpg" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9c27fbbbc602b788043df8a39fc102b737a4feaa_2_690x388.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9c27fbbbc602b788043df8a39fc102b737a4feaa_2_1035x582.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9c27fbbbc602b788043df8a39fc102b737a4feaa_2_1380x776.jpg 2x" data-dominant-color="EFEFEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Adsız1.jpg</span><span class="informations">1600×900 248 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/b9c467ae81fade22a70f44df0367a572c938fd18.jpg" data-download-href="/uploads/short-url/qvn7VkOym7mtuwtniJkUod4ewPe.jpg?dl=1" title="Adsız2.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/b9c467ae81fade22a70f44df0367a572c938fd18_2_690x388.jpg" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/b9c467ae81fade22a70f44df0367a572c938fd18_2_690x388.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/b9c467ae81fade22a70f44df0367a572c938fd18_2_1035x582.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/b9c467ae81fade22a70f44df0367a572c938fd18_2_1380x776.jpg 2x" data-dominant-color="EFEFEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Adsız2.jpg</span><span class="informations">1600×900 246 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In addition, when i’m tried, not only 20 patients but also 2 different instution’s patients so 2 different MRI machines but i can’t tractography.</p>
<p>Thank you for your interest Mr. Norton.</p>

---

## Post #12 by @ljod (2017-07-22 18:34 UTC)

<p>These tags look like a trace weighted or ADC map. It appears to not be a DWI from a DTI protocol. I recommend investigating if other images were saved on the scanner and finding out what the acquisition was.</p>

---

## Post #13 by @AsliBeriL (2017-07-22 18:51 UTC)

<aside class="quote no-group" data-username="ljod" data-post="12" data-topic="719" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ljod/48/652_2.png" class="avatar"> ljod:</div>
<blockquote>
<p>These tags look like a trace weighted or ADC map. It appears to not be a DWI from a DTI protocol. I recommend investigating if other images were saved on the scanner and finding out what the acquisition was.</p>
</blockquote>
</aside>
<p>What do you mean other images? If you have dwi images that work for you, can you send me the meta data? According to these parameters, we make our next MRI protocol at least.</p>
<p>Thanks Mrs. Lauren.</p>

---

## Post #14 by @ihnorton (2017-07-22 20:00 UTC)

<p>This is a trace image:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/9b91075b53df033a9aab7d9009dd772dc7eb4c53.jpg" data-download-href="/uploads/short-url/mccJig0iJj2eqEdK591Bqg7Y2YP.jpg?dl=1" title="image.jpg"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9b91075b53df033a9aab7d9009dd772dc7eb4c53_2_690x53.jpg" width="690" height="53" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9b91075b53df033a9aab7d9009dd772dc7eb4c53_2_690x53.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b91075b53df033a9aab7d9009dd772dc7eb4c53.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b91075b53df033a9aab7d9009dd772dc7eb4c53.jpeg 2x" data-dominant-color="DEDEDD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">700×54 20 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>It looks like you are using the Siemens product sequence, which should work fine, but you need the original DWI images (these derived maps are automatically computed by the scanner by default, but it can be turned off in the protocol card). The raw DWI will have lower series number and the ImageType tag should look like:</p>
<pre><code class="lang-auto">(0008,0008) CS [ORIGINAL\PRIMARY\DIFFUSION\NONE\ND\MOSAIC] #  42, 6 ImageType
</code></pre>
<p>(it might not say MOSAIC at the end, but it needs to say <code>ORIGINAL\PRIMARY</code>)</p>

---

## Post #15 by @lassoan (2017-07-22 20:00 UTC)

<p><a class="mention" href="/u/ihnorton">@ihnorton</a> I’ve improved the metadata dialog to be able to filter for specific tags and export all of them in all of the selected patient, study, or series. It is implemented in CTK and waiting for the pull request to be merged (<a href="https://github.com/commontk/CTK/pull/728">https://github.com/commontk/CTK/pull/728</a>), but it should get into the nightly Slicer version within a few days. That should help figuring out what kind of data the user has much more quickly.</p>

---

## Post #16 by @AsliBeriL (2017-07-22 20:28 UTC)

<p>Thank you very much <a class="mention" href="/u/ihnorton">@ihnorton</a> and <a class="mention" href="/u/lassoan">@lassoan</a> <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
Yes, MRI machine is Siemens’s product. I have also another image series of other institute. ImageType tag is yours said <a class="mention" href="/u/ihnorton">@ihnorton</a>. But i trying again and again, still i can not tractography. Look at this please.<br>
So how can i turned off in the protocol card or whom should i say this situation? Briefly, what can i do?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/108ae41f133b024ad0347d0018c526e54a39a289.jpg" data-download-href="/uploads/short-url/2mldadjNu2bR0XCFoggMJXBESrT.jpg?dl=1" title="Adsız3.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/108ae41f133b024ad0347d0018c526e54a39a289_2_690x388.jpg" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/108ae41f133b024ad0347d0018c526e54a39a289_2_690x388.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/108ae41f133b024ad0347d0018c526e54a39a289_2_1035x582.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/108ae41f133b024ad0347d0018c526e54a39a289_2_1380x776.jpg 2x" data-dominant-color="EFEFEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Adsız3.jpg</span><span class="informations">1600×900 244 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #17 by @ljod (2017-07-23 16:08 UTC)

<p>Hello this is still not a diffusion volume. It does not say diffusion in the ImageType.</p>
<p>In addition to trace and other derived images, the original diffusion DWI should have also been saved on the scanner. It is necessary to talk to the MRI technician, MRI physicist, or look in the image archives to find this image.</p>

---

## Post #18 by @AsliBeriL (2017-07-23 20:52 UTC)

<p>OK. Thank you very much for all and advance. In addition I really appreciate for this software <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Best regards,</p>
<p>A. BeriL</p>

---

## Post #19 by @Cincy (2020-04-21 14:37 UTC)

<p>hello,maybe I need your help .I met the same problem.I created .nrrd file, baseline and mask. DWI to DTI estimation module was working and it did not prompt errors but I did not see DTI  image(it is black), and  I want to know if you solve the problem by  finding  the original diffusion DWI .Thank you！</p>

---

## Post #20 by @Nicholas.jacobson (2020-08-21 18:12 UTC)

<p>Hello, I am working on a new DWI set, de-identified, from a phillips machine. I’m getting 34 directions, a multi volume and a DWI volume showing up in the DICOM viewer. However, in the brain mask step I am getting an error for no b0. How do I work with this error? Happy to share the files as I am somewhat new to this process and could use the guidance.</p>
<p>nick</p>

---
