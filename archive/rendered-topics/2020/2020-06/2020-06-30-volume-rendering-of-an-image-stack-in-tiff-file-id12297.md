---
topic_id: 12297
title: "Volume Rendering Of An Image Stack In Tiff File"
date: 2020-06-30
url: https://discourse.slicer.org/t/12297
---

# Volume rendering of an image stack in tiff file

**Topic ID**: 12297
**Date**: 2020-06-30
**URL**: https://discourse.slicer.org/t/volume-rendering-of-an-image-stack-in-tiff-file/12297

---

## Post #1 by @Deepa (2020-06-30 13:13 UTC)

<p>Hello Everyone,<br>
I have loaded data from a tif file (please check the snapshot for reference)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7093eee9817969247b9d589150547e914950734.jpeg" data-download-href="/uploads/short-url/uGisQocko7Te9OLSZRPk4OZquoI.jpeg?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d7093eee9817969247b9d589150547e914950734_2_345x142.jpeg" alt="Untitled" data-base62-sha1="uGisQocko7Te9OLSZRPk4OZquoI" width="345" height="142" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d7093eee9817969247b9d589150547e914950734_2_345x142.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d7093eee9817969247b9d589150547e914950734_2_517x213.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d7093eee9817969247b9d589150547e914950734_2_690x284.jpeg 2x" data-dominant-color="BDBDC3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1893×781 282 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I have enabled depth peeling, clicked <code>Fit to volume</code>, varied <code>shift</code> and tried different presets. But I am not able to visualize the 3D volume in <code>Volume rendering</code> module.</p>
<p>Could someone offer advice on the other options that I could try for visualizing the volume?</p>

---

## Post #2 by @pieper (2020-06-30 15:19 UTC)

<p>You probably need to use this: <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/VectorToScalarVolume">https://www.slicer.org/wiki/Documentation/4.10/Modules/VectorToScalarVolume</a></p>

---

## Post #3 by @Deepa (2020-06-30 18:04 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a></p>
<p>I tried with VectorToScalarVolume module, after loading the <a href="https://drive.google.com/file/d/1fIH3nQYKyoAaeB1rE3yTFoQdXDf0z6RR/view?usp=sharing" rel="nofollow noopener">input tiff file</a> as <code>Volume</code>.</p>
<p>But I am not able to select the loaded volume as <code>Input Vector Volume</code> in the <code>Conversion settings</code> tab of VectortoScalarVolume module. I think it’s already a scalar volume. Could you please check the input?</p>

---

## Post #4 by @muratmaga (2020-06-30 18:18 UTC)

<aside class="quote no-group" data-username="Deepa" data-post="3" data-topic="12297">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>But I am not able to select the loaded volume as <code>Input Vector Volume</code> in the <code>Conversion settings</code> tab of VectortoScalarVolume module. I think it’s already a scalar volume. Could you please check the input?</p>
</blockquote>
</aside>
<p>I believe TIFF stacks are imported as scalar volume (unlike JPG, BMP and PNG). So I don’t think VectorToScalar will help you there.</p>
<p>What rendering mode are you using? Does switching to CPU rendering help?</p>

---

## Post #5 by @lassoan (2020-06-30 18:27 UTC)

<p>I’ve checked the data set and it is a single-component image (so Vector to scalar conversion is not necessary), but the image is quite unusual, as it has a very uneven intensity distribution (meaningful values are between 60000-65000) and background is bright.</p>
<p>To visualize this volume with volume rendering, I would first normalize the intensity range to let’s say 0-5000 using Simple Filters module RescaleIntensityImageFilter:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b9d8d9223fbb93dc059ff383a6df1ce49010ffe.png" alt="image" data-base62-sha1="aMVmH6L6xoDih20sdrhAqmXRk7Q" width="583" height="447"></p>
<p>Then choose a volume rendering preset where bright voxels are transparent, such as CT-Air preset, and adjust the Shift slider until you see what you need:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f63c9a8ce95ce7461086eaab4427c45402a384c.jpeg" data-download-href="/uploads/short-url/bkjvTkOIbr1EkZv2pKS8ccrHPnm.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f63c9a8ce95ce7461086eaab4427c45402a384c_2_690x360.jpeg" alt="image" data-base62-sha1="bkjvTkOIbr1EkZv2pKS8ccrHPnm" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f63c9a8ce95ce7461086eaab4427c45402a384c_2_690x360.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f63c9a8ce95ce7461086eaab4427c45402a384c_2_1035x540.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f63c9a8ce95ce7461086eaab4427c45402a384c_2_1380x720.jpeg 2x" data-dominant-color="A1A7B0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1002 620 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @Deepa (2020-07-01 03:06 UTC)

<p>Thanks a lot. This helped, but I also had to switch to CPU rendering as suggested by <a class="mention" href="/u/muratmaga">@muratmaga</a>.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/muratmaga">@muratmaga</a><br>
I’ve to find the diameters and lengths of the vessels in this volume element.  I would like to request for advice on how to proceed with this volume, since the z-spacing is 1mm I am not sure if this will work.</p>

---

## Post #7 by @muratmaga (2020-07-01 03:27 UTC)

<p>Now that you know VOlume rendering works on this dataset, you can try to experiment with GPU rendering. What kind of GPU do you have on this computer, and are drivers up to date?</p>

---

## Post #8 by @Deepa (2020-07-01 05:40 UTC)

<p>The following is the GPU info of the server. I’m not sure if the drivers are up to date.</p>
<p>±----------------------------------------------------------------------------+<br>
| NVIDIA-SMI 410.48                 Driver Version: 410.48                    |<br>
|-------------------------------±---------------------±---------------------+<br>
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |<br>
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |<br>
|===============================+======================+======================|<br>
|   0  GeForce GTX 108…  Off  | 00000000:0A:00.0 Off |                  N/A |<br>
| 42%   72C    P2   140W / 250W |    303MiB / 11176MiB |     69%      Default |<br>
±------------------------------±---------------------±---------------------+</p>

---

## Post #9 by @muratmaga (2020-07-01 05:52 UTC)

<p>That GPU should be more than enough to handle that dataset. Are you running this on linux? Might be an issue with the openGL</p>

---

## Post #10 by @Deepa (2020-07-01 07:06 UTC)

<p>Yes, I am running this on linux.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="9" data-topic="12297">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Might be an issue with the openGL</p>
</blockquote>
</aside>
<p>Thanks for pointing this out. I will continue using CPU rendering since I don’t have root access o fix these at this point in time <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=12" title=":confused:" class="emoji" alt=":confused:" loading="lazy" width="20" height="20"></p>

---
