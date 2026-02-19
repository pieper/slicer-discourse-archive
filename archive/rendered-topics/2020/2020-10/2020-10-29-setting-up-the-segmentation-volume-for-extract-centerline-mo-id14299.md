---
topic_id: 14299
title: "Setting Up The Segmentation Volume For Extract Centerline Mo"
date: 2020-10-29
url: https://discourse.slicer.org/t/14299
---

# Setting up the segmentation volume for extract centerline module

**Topic ID**: 14299
**Date**: 2020-10-29
**URL**: https://discourse.slicer.org/t/setting-up-the-segmentation-volume-for-extract-centerline-module/14299

---

## Post #1 by @Deepa (2020-10-29 04:09 UTC)

<p>Hello Everyone,</p>
<p>I have a segmentation volume shown in the image below, created after processing an image stack by pixel classification. I want to use this volume for creating a network model in the <code>extract centerline </code> module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d355f9582636d0958e4cd07e33f9eef78fa3f1a.jpeg" data-download-href="/uploads/short-url/fA6oz1nHA6x623nilUBKM3pDDXY.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6d355f9582636d0958e4cd07e33f9eef78fa3f1a_2_345x205.jpeg" alt="image" data-base62-sha1="fA6oz1nHA6x623nilUBKM3pDDXY" width="345" height="205" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6d355f9582636d0958e4cd07e33f9eef78fa3f1a_2_345x205.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6d355f9582636d0958e4cd07e33f9eef78fa3f1a_2_517x307.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6d355f9582636d0958e4cd07e33f9eef78fa3f1a_2_690x410.jpeg 2x" data-dominant-color="657978"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1126×670 214 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>However, the presence of tiny sharp endpoints (circled black) creates an issue while trying to use <code>Autodetect</code> for detecting endpoints post which the network model can be created.</p>
<p>I would like to know if it is possible to use any of the options available in the segment editor to remove these sharp surfaces after reconstruction of the 3D volume.</p>

---

## Post #2 by @lassoan (2020-10-30 04:49 UTC)

<p>You can use Smoothing effect in Segment editor. You can also try preprocessing your input image before segmentation using filters in Simple Filters module. It may also improve your segmentation quality if you resample the image before segmentation to have isotropic voxels, using Crop volume module (as some of the structures look suspiciously flat).</p>

---

## Post #3 by @Deepa (2020-10-30 07:36 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Firstly, thank you very much for always taking the time to guide me throughout this journey.</p>
<p>Í’m afraid I don’t know which filter has to be chosen In the <code>Simple Filters</code> module from the many options that are listed.</p>
<p>I am sharing the stack (<a href="https://drive.google.com/file/d/18zvU6FHjcvpCfKD93fcwu3KEiaKe_Rtr/view?usp=sharing" rel="noopener nofollow ugc">here</a>) that I wish to preprocess for your kind reference.</p>
<p>Could you please suggest which filter would be appropriate? I’m looking for an option similar to imopen in MATLAB (erosion followed by dilation) to remove these small objects in the borders of an image. I’ll be really happy to know if there are other suggestions.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="14299">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It may also improve your segmentation quality if you resample the image before segmentation to have isotropic voxels, using Crop volume module (as some of the structures look suspiciously flat).</p>
</blockquote>
</aside>
<p>Sure, I’ll try this too.</p>

---

## Post #4 by @lassoan (2020-10-30 13:46 UTC)

<aside class="quote no-group" data-username="Deepa" data-post="3" data-topic="14299">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>imopen in MATLAB (erosion followed by dilation)</p>
</blockquote>
</aside>
<p>This exact algorithm is available in Segment Editor, Smoothing effect, opening method.</p>
<aside class="quote no-group" data-username="Deepa" data-post="3" data-topic="14299">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>Í’m afraid I don’t know which filter has to be chosen In the <code>Simple Filters</code> module from the many options that are listed.</p>
</blockquote>
</aside>
<p>ITK filters are documented in the <a href="https://itk.org/ItkSoftwareGuide.pdf">ITK software guide</a>. Search for “smoothing”.</p>

---

## Post #5 by @Deepa (2020-10-30 16:27 UTC)

<p>Thank you, I tried to use Smoothing → Opening for the default kernel size, and it results in the following segment unfortunately</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/567765d2137990fa1eea0cd797af9802d89da01d.jpeg" data-download-href="/uploads/short-url/ckURZQXZQgZ27JSgPdfz12CXyzj.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/567765d2137990fa1eea0cd797af9802d89da01d_2_306x250.jpeg" alt="image" data-base62-sha1="ckURZQXZQgZ27JSgPdfz12CXyzj" width="306" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/567765d2137990fa1eea0cd797af9802d89da01d_2_306x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/567765d2137990fa1eea0cd797af9802d89da01d_2_459x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/567765d2137990fa1eea0cd797af9802d89da01d_2_612x500.jpeg 2x" data-dominant-color="738691"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">792×646 256 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I’d a chance to look at the smoothing filters chapter of the documentation. Unfortunately, I still do not completely understand how those operations differ from the smoothing option available in segment editor &gt; smoothing .</p>

---

## Post #6 by @lassoan (2020-10-30 19:34 UTC)

<p>Probably the segmentation’s resolution is just not fine enough to remove such small noise from it. You can try oversampling the segmentation or apply more surface smoothing. You can probably also find out from vessel network extraction results which endpoints correspond to very short branches, remove those endpoints, and rerun the network extraction.</p>

---

## Post #7 by @Deepa (2020-11-01 07:02 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="14299">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It may also improve your segmentation quality if you resample the image before segmentation to have isotropic voxels, using Crop volume module (as some of the structures look suspiciously flat).</p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a><br>
For what has been suggested, I’m trying to set up the crop volume parameters.</p>
<p>I’ve selected nearest neighbor as the interpolator and I am not sure how the Spacing scale has to be adjusted. I think the spatial resolution of the original volume has to be increased. To increase the resolution , I tried a spacing scale of 0.5. I would like to confirm on this.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c393dd3490a203c285c1344dba32ec32af1d1cb.jpeg" data-download-href="/uploads/short-url/k0tu5c1NHUpkvQpW0Ti8dZ1ACj9.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c393dd3490a203c285c1344dba32ec32af1d1cb_2_560x500.jpeg" alt="image" data-base62-sha1="k0tu5c1NHUpkvQpW0Ti8dZ1ACj9" width="560" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c393dd3490a203c285c1344dba32ec32af1d1cb_2_560x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c393dd3490a203c285c1344dba32ec32af1d1cb.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c393dd3490a203c285c1344dba32ec32af1d1cb.jpeg 2x" data-dominant-color="EAEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">758×676 74 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2020-11-01 20:06 UTC)

<p>The simplest way to resample (and also at the same time crop the volume to the minimum necessary size, to avoid blowing up your memory usage) is to use Crop volume module.</p>

---
