# TotalSegmentator for MRI dataset

**Topic ID**: 35080
**Date**: 2024-03-26
**URL**: https://discourse.slicer.org/t/totalsegmentator-for-mri-dataset/35080

---

## Post #1 by @muratmaga (2024-03-26 01:26 UTC)

<p>Is there an full body (or lower limb) muscle segmentation model from MRI images? As I understand totalsegmentator is specifically for CT.</p>

---

## Post #2 by @lassoan (2024-03-26 02:38 UTC)

<p>There are a couple of pre-trained MRI segmentation models for MONAI Auto3DSeg (brain, prostate, etc) and you can probably find some spine segmentation models, but I don’t remember seeing any for lower lung muscles. However, it is almost sure your can train Auto3DSeg or nnUNet model for this quite easily, by manually segment cases (perhaps a few dozen is enough to get started)</p>

---

## Post #3 by @pieper (2024-03-26 16:09 UTC)

<p>We have a project underway to try training an MR segmenter based on TotalSegmentator using the SynthSeg approach (not muscles yet though).  The preprint paper actually just went up on arxiv:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://arxiv.org/abs/2403.15609">
  <header class="source">
      <img src="https://arxiv.org/static/browse/0.3.4/images/icons/favicon-32x32.png" class="site-icon" width="32" height="32">

      <a href="https://arxiv.org/abs/2403.15609" target="_blank" rel="noopener">arXiv.org</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/402;"><img src="https://static.arxiv.org/icons/twitter/arxiv-logo-twitter-square.png" class="thumbnail" width="500" height="500"></div>

<h3><a href="https://arxiv.org/abs/2403.15609" target="_blank" rel="noopener">Towards Automatic Abdominal MRI Organ Segmentation: Leveraging Synthesized...</a></h3>

  <p>Deep learning has shown great promise in the ability to automatically annotate organs in magnetic resonance imaging (MRI) scans, for example, of the brain. However, despite advancements in the field, the ability to accurately segment abdominal organs...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Would be great to generalize to other segmentation tasks.</p>

---

## Post #4 by @lassoan (2024-03-29 00:53 UTC)

<p>This looks interesting <a class="mention" href="/u/pieper">@pieper</a>. Is the trained model available publicly?</p>

---

## Post #5 by @pieper (2024-03-29 12:18 UTC)

<p>Not currently, but I’ll check.</p>

---

## Post #6 by @fedorov (2024-03-29 12:29 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="35080" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This looks interesting <a class="mention" href="/u/pieper">@pieper</a>. Is the trained model available publicly?</p>
</blockquote>
</aside>
<p>Andras, <a class="mention" href="/u/deepakrishnaswamy">@DeepaKrishnaswamy</a> and <a class="mention" href="/u/cosmin_ciausu">@Cosmin_Ciausu</a> are working on this. We absolutely will make everything publicly available, but there are some experiments and refinements that we want to do first. It’s great to see the interest. This most definitely adds a lot to the motivation to continue this work!</p>

---

## Post #7 by @DeepaKrishnaswamy (2024-04-16 14:18 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Thank you for your interest! As <a class="mention" href="/u/fedorov">@fedorov</a> said, we are in the process of doing a few more experiments. We are definitely planning on making the model, and the code, publicly available, and will get back to you when we are at that stage.</p>
<p>Deepa and Cosmin</p>

---

## Post #8 by @jamesobutler (2024-05-31 03:08 UTC)

<p>Following up here, TotalSegmentator v2.2 now has support for MR tasks. SlicerTotalSegmentator will have to be updated to specify to use this new version.</p>
<p>From <a href="https://github.com/wasserth/TotalSegmentator?tab=readme-ov-file#totalsegmentator" class="inline-onebox" rel="noopener nofollow ugc">GitHub - wasserth/TotalSegmentator: Tool for robust segmentation of &gt;100 important anatomical structures in CT and MR images</a> :</p>
<blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0b13f1802895a7f1e8b40a68c79fddf41626442.png" data-download-href="/uploads/short-url/pd5MA745uOhoGOfkrZG3q3DXNWW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0b13f1802895a7f1e8b40a68c79fddf41626442_2_690x393.png" alt="image" data-base62-sha1="pd5MA745uOhoGOfkrZG3q3DXNWW" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0b13f1802895a7f1e8b40a68c79fddf41626442_2_690x393.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0b13f1802895a7f1e8b40a68c79fddf41626442_2_1035x589.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0b13f1802895a7f1e8b40a68c79fddf41626442_2_1380x786.png 2x" data-dominant-color="1D1711"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3068×1750 496 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</blockquote>

---

## Post #9 by @mangotee (2024-05-31 07:55 UTC)

<p>There is also <a href="https://github.com/hhaentze/MRSegmentator" rel="noopener nofollow ugc">MRSegmentator</a>, also based on nnUnet., and trained on 1400+ MRI images from UKBB.</p>

---

## Post #10 by @fedorov (2024-05-31 08:20 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="8" data-topic="35080">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Following up here, TotalSegmentator v2.2 now has support for MR tasks.</p>
</blockquote>
</aside>
<p>If anyone experimented with this model, I would be very interested to hear about your experience!</p>

---

## Post #11 by @lassoan (2024-05-31 16:41 UTC)

<p>We have been discussing this with <a class="mention" href="/u/wasserth">@wasserth</a>. I expect that MRI segmentation will be available in Slicer TotalSegmentator extension from tomorrow. I’ll post updates here.</p>

---

## Post #12 by @lassoan (2024-05-31 17:46 UTC)

<p>TotalSegmentator extension is updated now to use the latest models, including the new <code>total_mr</code>. The update is available from tomorrow for both the latest Slicer Stable Release (Slicer-5.6) and latest Slicer Preview Release (Slicer-5.7 downloaded 2024-06-01 or later).</p>
<p>Example result for an abdominal MRI (source image: Imaging Data Commons / CMC-CRC-MSB-01262 / MRI Abdomen / 31 AX T1 3D FS  3MIN POST_W):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56a51a5624e21ea34a8bcc2a8df287a74f2f98a5.jpeg" data-download-href="/uploads/short-url/cmuNd8Jdzgt1MEXS7jNyRS2QPMV.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56a51a5624e21ea34a8bcc2a8df287a74f2f98a5_2_690x362.jpeg" alt="image" data-base62-sha1="cmuNd8Jdzgt1MEXS7jNyRS2QPMV" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56a51a5624e21ea34a8bcc2a8df287a74f2f98a5_2_690x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56a51a5624e21ea34a8bcc2a8df287a74f2f98a5_2_1035x543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56a51a5624e21ea34a8bcc2a8df287a74f2f98a5_2_1380x724.jpeg 2x" data-dominant-color="4C484E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1010 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Slice sweep:</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27ed29654785281ac0677f300a8e220321b42307.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/5813feea954b0f51dfe1ec6132745a9ef7581a8e.jpeg">
  </div><p></p>
<p>3D Rotation:</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/652237d91d65266c29f6ed651aacb1980953ee35.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/5330161e85a8b1fd74788189e0d0d2e621f9effe.jpeg">
  </div><p></p>

---

## Post #13 by @ffournier13 (2024-06-03 08:47 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a><br>
This is looking very nice !<br>
I tried on my MRI data set but even without the fast setting checked, the segmentation is not as good as yours.<br>
Is there a preferred protocol or parameter for the segmentations to work better? I am working with T2 HASTE, with 4mm slices on the transverse plane, but this could change. Do you have any recommendations?</p>
<p>Here is an example of segmentation I did just now with the new total_mr (we can see, for example, that the stomach is not well segmented):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/9004cc030009d69024a6d72ad06ad9b660834848.jpeg" data-download-href="/uploads/short-url/ky323eFdbpsDIfekEnkwuxHBpJm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9004cc030009d69024a6d72ad06ad9b660834848_2_661x500.jpeg" alt="image" data-base62-sha1="ky323eFdbpsDIfekEnkwuxHBpJm" width="661" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9004cc030009d69024a6d72ad06ad9b660834848_2_661x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/9004cc030009d69024a6d72ad06ad9b660834848.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/9004cc030009d69024a6d72ad06ad9b660834848.jpeg 2x" data-dominant-color="625955"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">850×642 86.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85347645f0c95f12a320562d7ead2309ca0a366f.jpeg" data-download-href="/uploads/short-url/j0nTYJv30XXxASsORinwE6hkn1B.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85347645f0c95f12a320562d7ead2309ca0a366f_2_510x500.jpeg" alt="image" data-base62-sha1="j0nTYJv30XXxASsORinwE6hkn1B" width="510" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85347645f0c95f12a320562d7ead2309ca0a366f_2_510x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85347645f0c95f12a320562d7ead2309ca0a366f.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85347645f0c95f12a320562d7ead2309ca0a366f.jpeg 2x" data-dominant-color="9485A9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">702×688 78 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you in advance for your answer!</p>
<p>François</p>

---

## Post #14 by @lassoan (2024-06-03 12:32 UTC)

<p>4mm slice thickness is very large. Each voxel is a long stick, it is very difficult to create accurate segmentation at such crude resolution.</p>
<p>You may try resampling the image to have isotropic spacing using Crop volume module to see if it improves the results. Let us know is it helped.</p>

---

## Post #15 by @ffournier13 (2024-06-05 07:08 UTC)

<p>Thank you for your answer <a class="mention" href="/u/lassoan">@lassoan</a>.<br>
I’ll try it and get back to you.<br>
What slice thickness did you use to get the result you showed in the above video ? Maybe you could share details aboute sequences that would work with this new version of total segmentator ?<br>
Reducing slice thickness will induce other anatomical errors. I think, as MRI sequences are already taking 1min30s, with longer MRI movements will change the gastrointestinal anatomy during the acquisition …</p>

---

## Post #16 by @wasserth (2024-06-12 07:30 UTC)

<p>Thanks Andras for updating the TotalSegmentator Slicer Extension to the newest TotalSegmentator version!<br>
The problem with many MR images is the much bigger slice thickness compared to CT. This lower data quality results in lower accuracy compared to TotalSegmentator CT. In our training dataset we have many low resolution MR datasets. For these images it is also difficult to create good ground truth annotations. The alternative would be to train only on nice high quality MR images. Then the segmentation accuracy would be better on high res MR images, but the model would not work as robustly on any MR sequence. We decided to prioritise robustness. For many applications this level of accuracy is still fine. For some applications you need higher accuracy. Then some refinement of the initial segmentation is needed.</p>

---

## Post #17 by @mwirtz (2024-06-17 08:22 UTC)

<p>On the official download page, I still only find the latest stable release (revision 32448) built on 2024-04-05 without the new <code>total_mr</code> segmentation. Am I overseeing something or was there an issue updating the latest release?</p>
<p>Thanks in advance!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75e51bc7ec01019947b6d267b030166ff713fdf9.png" data-download-href="/uploads/short-url/gOWJ3KlgiX1vr5BmpazX54RWfZT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75e51bc7ec01019947b6d267b030166ff713fdf9_2_690x284.png" alt="image" data-base62-sha1="gOWJ3KlgiX1vr5BmpazX54RWfZT" width="690" height="284" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75e51bc7ec01019947b6d267b030166ff713fdf9_2_690x284.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75e51bc7ec01019947b6d267b030166ff713fdf9_2_1035x426.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75e51bc7ec01019947b6d267b030166ff713fdf9.png 2x" data-dominant-color="F3F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1077×444 25.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #18 by @fedorov (2024-06-17 19:30 UTC)

<p><a class="mention" href="/u/mwirtz">@mwirtz</a> this functionality is available in a Slicer extension. The version you see on the download page is the version of the Slicer application. Individual extensions may have more recent builds.</p>

---

## Post #19 by @mwirtz (2024-06-19 07:09 UTC)

<p>Thanks <a class="mention" href="/u/fedorov">@fedorov</a>, yes I tried to install the extension in the latest Stable release and <code>total_mr</code> was not appearing. I assumed it might still have something to do with the built version being older than the extension update.</p>

---

## Post #20 by @muratmaga (2024-06-19 15:40 UTC)

<p><a class="mention" href="/u/mwirtz">@mwirtz</a></p>
<p>You are not doing anything wrong. I assume you are trying windows.</p>
<p>There is an ongoing issue about extensions on windows build. Total segmentator is one of those affected (no windows build per Cdash. <a href="https://slicer.cdash.org/index.php?project=SlicerStable" class="inline-onebox">CDash</a>)</p>
<p>Devs are aware of the issue and looking into it, but I do not know when it is going to resolved.</p>
<p>Linux and and Mac seems unaffected from this. If you have access to those you can on those OS.</p>

---

## Post #21 by @lassoan (2024-06-23 22:38 UTC)

<p>Extension builds for Slicer Stable Release are restored now.</p>

---

## Post #22 by @Hasanb (2024-07-24 12:23 UTC)

<p>Dear lassoan,<br>
I am new at this community, sorry if this question is answered another place. I wonder whether there is a way to use total_MR to segment the spinal canal and not only the structures around it? I am working on a project to segment and measure the volume of the spinal canal.<br>
Bests!</p>

---

## Post #23 by @Spiros_Karkavitsas (2024-08-05 18:35 UTC)

<p>Hello from my side too!<br>
I just found out about the existence of TotalSegmentator for MR specifically and it seems amazing and very promising!<br>
I worked in the past with MONAI Label and I was quite satisfied with the results.</p>
<p>Was there any air segmentation in your training dataset?<br>
I am wondering since the MR slices I am working on is 10 mm slice thickness so I guess the accuracy would be low, correct?</p>

---

## Post #24 by @lassoan (2024-08-19 13:38 UTC)

<aside class="quote no-group" data-username="Spiros_Karkavitsas" data-post="23" data-topic="35080">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/spiros_karkavitsas/48/18224_2.png" class="avatar"> Spiros_Karkavitsas:</div>
<blockquote>
<p>Was there any air segmentation in your training dataset?</p>
</blockquote>
</aside>
<p>MR task of TotalSegmentator currently does not include airways, but if you exclude all known segmented regions then you may be able to segment the air using Threshold or with “Grow from seeds” effect.</p>
<aside class="quote no-group" data-username="Spiros_Karkavitsas" data-post="23" data-topic="35080">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/spiros_karkavitsas/48/18224_2.png" class="avatar"> Spiros_Karkavitsas:</div>
<blockquote>
<p>I am wondering since the MR slices I am working on is 10 mm slice thickness so I guess the accuracy would be low, correct?</p>
</blockquote>
</aside>
<p>Yes, 10mm distance between slices is so huge that it is not really usable for 3D analysis.</p>

---
