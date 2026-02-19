---
topic_id: 36022
title: "How To Segment A Skull And Visualize The Skull Sutures"
date: 2024-05-09
url: https://discourse.slicer.org/t/36022
---

# How to segment a skull and visualize the skull sutures

**Topic ID**: 36022
**Date**: 2024-05-09
**URL**: https://discourse.slicer.org/t/how-to-segment-a-skull-and-visualize-the-skull-sutures/36022

---

## Post #1 by @paleomariomm (2024-05-09 12:10 UTC)

<p>Hi everyone. Let’s use this freely-downloadable baboon skull from MorphoSource as an example.</p>
<p><a href="https://www.morphosource.org/concern/media/000059584?locale=en" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.morphosource.org/concern/media/000059584?locale=en</a></p>
<p>If I render the volume, I can see skull sutures very clearly:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13c4b53c4603c2eba45cfe3c4fa06afee4130780.jpeg" data-download-href="/uploads/short-url/2OSw2v5nMlNzCSsJvakPrnhRLkA.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13c4b53c4603c2eba45cfe3c4fa06afee4130780_2_690x485.jpeg" alt="image" data-base62-sha1="2OSw2v5nMlNzCSsJvakPrnhRLkA" width="690" height="485" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13c4b53c4603c2eba45cfe3c4fa06afee4130780_2_690x485.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13c4b53c4603c2eba45cfe3c4fa06afee4130780_2_1035x727.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13c4b53c4603c2eba45cfe3c4fa06afee4130780.jpeg 2x" data-dominant-color="7B7C93"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1339×943 55.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c796ff0524481201e7c77eef8c20cdf0467f7512.jpeg" data-download-href="/uploads/short-url/stEwvTtokpsfjZs125rTvZCMpd8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c796ff0524481201e7c77eef8c20cdf0467f7512_2_690x494.jpeg" alt="image" data-base62-sha1="stEwvTtokpsfjZs125rTvZCMpd8" width="690" height="494" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c796ff0524481201e7c77eef8c20cdf0467f7512_2_690x494.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c796ff0524481201e7c77eef8c20cdf0467f7512_2_1035x741.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c796ff0524481201e7c77eef8c20cdf0467f7512_2_1380x988.jpeg 2x" data-dominant-color="8485A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1683×1205 79.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, when I create a segmentation with the threshold option, all of the sutures are lost.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/666d66176e12fa8c5d13230014ba06e0e6795577.jpeg" data-download-href="/uploads/short-url/eC75rAIgJS5bdrcY6wjZDPz2BVl.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/666d66176e12fa8c5d13230014ba06e0e6795577_2_662x500.jpeg" alt="image" data-base62-sha1="eC75rAIgJS5bdrcY6wjZDPz2BVl" width="662" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/666d66176e12fa8c5d13230014ba06e0e6795577_2_662x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/666d66176e12fa8c5d13230014ba06e0e6795577_2_993x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/666d66176e12fa8c5d13230014ba06e0e6795577_2_1324x1000.jpeg 2x" data-dominant-color="A4A57F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1578×1191 68.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b170faba130ec47f0556a0173dc46e7fae4d853f.jpeg" data-download-href="/uploads/short-url/pjIzjeTRo4hrV1lSqNmBRfLcvhR.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b170faba130ec47f0556a0173dc46e7fae4d853f_2_621x500.jpeg" alt="image" data-base62-sha1="pjIzjeTRo4hrV1lSqNmBRfLcvhR" width="621" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b170faba130ec47f0556a0173dc46e7fae4d853f_2_621x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b170faba130ec47f0556a0173dc46e7fae4d853f_2_931x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b170faba130ec47f0556a0173dc46e7fae4d853f_2_1242x1000.jpeg 2x" data-dominant-color="9C9D99"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1577×1269 89.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have been playing around changing parameters of the Threshold option with no success. I tried also other segmentation options unsuccessfully.</p>
<p>Does anybody know how we can create a segmentation of the full skull keeping reliably the sutures of the skull? Which are the correct parameters?</p>
<p>Be aware that we need to create a segmentation in order to export the resulting segment to PLY file to run in a later step MALPACA  from SlicerMorph.</p>
<p>Any help with the optimal parameters is very welcome!</p>
<p>Thanks</p>

---

## Post #2 by @muratmaga (2024-05-09 13:17 UTC)

<aside class="quote no-group" data-username="paleomariomm" data-post="1" data-topic="36022">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/paleomariomm/48/68475_2.png" class="avatar"> paleomariomm:</div>
<blockquote>
<p>However, when I create a segmentation with the threshold option, all of the sutures are lost.</p>
</blockquote>
</aside>
<p>What are your steps? That models look quite smoothened that might cause loss of small details like that. Try reducing the amount of smoothing or decimation.</p>
<p>I should warn you that trying to preserve cranial suture patterns patterns will not increase the accuracy of a ALPACA/MALPACA in a meaningful way compared to this model.</p>

---

## Post #3 by @paleomariomm (2024-05-09 13:36 UTC)

<p>Hi Murat, I basically use the Threshold option in the segmentation editor moving the slider.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea25b01c38e3a77b8753acbae158cb468a9ba26c.jpeg" data-download-href="/uploads/short-url/xpmtosh3BqXwHBGo1CYXL0eaUA4.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea25b01c38e3a77b8753acbae158cb468a9ba26c_2_690x292.jpeg" alt="image" data-base62-sha1="xpmtosh3BqXwHBGo1CYXL0eaUA4" width="690" height="292" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea25b01c38e3a77b8753acbae158cb468a9ba26c_2_690x292.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea25b01c38e3a77b8753acbae158cb468a9ba26c_2_1035x438.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea25b01c38e3a77b8753acbae158cb468a9ba26c_2_1380x584.jpeg 2x" data-dominant-color="7B7B8E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×815 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Concerning your last comment, I fully understand, but in order to find out some landmarks (like bregma), sutures are really important.</p>

---

## Post #4 by @muratmaga (2024-05-09 13:47 UTC)

<aside class="quote no-group" data-username="paleomariomm" data-post="3" data-topic="36022">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/paleomariomm/48/68475_2.png" class="avatar"> paleomariomm:</div>
<blockquote>
<p>Concerning your last comment, I fully understand, but in order to find out some landmarks (like bregma), sutures are really important.</p>
</blockquote>
</aside>
<p>For that you can display both the volume rendered image along with the model you derived, which will give you what you want.</p>

---

## Post #5 by @paleomariomm (2024-05-09 13:52 UTC)

<p>Exactly, this is linked with the other question I posted (<a href="https://discourse.slicer.org/t/aligning-a-surface-model-and-volume-rendering-of-the-same-skull/36024" class="inline-onebox">Aligning a surface model and volume rendering of the same skull</a>).</p>
<p>However I was wondering if by changing the segmentation parameters we could be able to visualize sutures… In this way we can save an step.</p>
<p>Thanks</p>

---

## Post #6 by @tsehrhardt (2024-05-12 12:49 UTC)

<p>For some reason, Grayscale Model Maker can show the sutures better–I have not found an equivalent tool in Segment Editor, but sometimes Grow from Seeds can provide more detail than thresholding. Here I put in a threshold of 300 and this is the model.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73a4d6510c29d94b4b5c33cd6b7c21ebb08917b2.jpeg" data-download-href="/uploads/short-url/gv24pnxTFKGFDJpvMt7vkBWvXy2.jpeg?dl=1" title="2024-05-12_8-41-27" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73a4d6510c29d94b4b5c33cd6b7c21ebb08917b2_2_690x377.jpeg" alt="2024-05-12_8-41-27" data-base62-sha1="gv24pnxTFKGFDJpvMt7vkBWvXy2" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73a4d6510c29d94b4b5c33cd6b7c21ebb08917b2_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73a4d6510c29d94b4b5c33cd6b7c21ebb08917b2_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73a4d6510c29d94b4b5c33cd6b7c21ebb08917b2_2_1380x754.jpeg 2x" data-dominant-color="9B9B9C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2024-05-12_8-41-27</span><span class="informations">1920×1050 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>From there, you can adjust color and surface features (roughness, metallic) in Models and also adjust lighting in Lights to enhance the visibility of sutures as well.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d00ee6716997806157211d9890c3a1a9749cc14.jpeg" data-download-href="/uploads/short-url/fyi2rOQSbV777AylS2Z17Xey1yA.jpeg?dl=1" title="2024-05-12_8-29-56" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d00ee6716997806157211d9890c3a1a9749cc14_2_690x377.jpeg" alt="2024-05-12_8-29-56" data-base62-sha1="fyi2rOQSbV777AylS2Z17Xey1yA" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d00ee6716997806157211d9890c3a1a9749cc14_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d00ee6716997806157211d9890c3a1a9749cc14_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d00ee6716997806157211d9890c3a1a9749cc14_2_1380x754.jpeg 2x" data-dominant-color="BBBDCF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2024-05-12_8-29-56</span><span class="informations">1920×1050 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/1908f2bad2e61c88f33d7129a8667563136d4b6a.jpeg" data-download-href="/uploads/short-url/3zt6HAehaEotKpDl4NOVT03tQtc.jpeg?dl=1" title="2024-05-12_8-31-44" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/1908f2bad2e61c88f33d7129a8667563136d4b6a_2_690x377.jpeg" alt="2024-05-12_8-31-44" data-base62-sha1="3zt6HAehaEotKpDl4NOVT03tQtc" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/1908f2bad2e61c88f33d7129a8667563136d4b6a_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/1908f2bad2e61c88f33d7129a8667563136d4b6a_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/1908f2bad2e61c88f33d7129a8667563136d4b6a_2_1380x754.jpeg 2x" data-dominant-color="C3C4D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2024-05-12_8-31-44</span><span class="informations">1920×1050 94.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can also toggle the visibility of the Grayscale Model Maker model in your slices.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8be89820fee8d43b3c9671c25956f4140aa15613.jpeg" data-download-href="/uploads/short-url/jXGHm2wUx1KUXwQQvj9tSKXux6r.jpeg?dl=1" title="2024-05-12_8-35-17" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8be89820fee8d43b3c9671c25956f4140aa15613_2_690x377.jpeg" alt="2024-05-12_8-35-17" data-base62-sha1="jXGHm2wUx1KUXwQQvj9tSKXux6r" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8be89820fee8d43b3c9671c25956f4140aa15613_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8be89820fee8d43b3c9671c25956f4140aa15613_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8be89820fee8d43b3c9671c25956f4140aa15613_2_1380x754.jpeg 2x" data-dominant-color="898D96"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2024-05-12_8-35-17</span><span class="informations">1920×1050 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The easiest thing would be to overlay the volume rendering, but if you need a surface model and you don’t need to edit individual bones, etc. the Grayscale Model Maker might work for you.</p>

---

## Post #7 by @pieper (2024-05-12 13:44 UTC)

<p>Thanks for pointing this out <a class="mention" href="/u/tsehrhardt">@tsehrhardt</a> - you are right, if somone needs a surface model with fine details, the Grayscale Model Maker can be better since it works by fitting a surface to the original continuous-tone input data, more like what you see in volume rendering, whereas labelmap-based segmentations first discretize the voxels and then reconstruct the surface.</p>
<p>If you need to subdivide the bone, you could use the Mask Volume with segments and then use Grayscale Model Maker.</p>

---

## Post #8 by @muratmaga (2024-05-12 18:05 UTC)

<p>This is probably the only time GrayScale Model Maker can work this effectively, because there is simply nothing to clean up at the segmentation step and a single threshold does the job. For scans with tissue or with other contents, a single threshold to model almost never works, and you have to rely on other tools in the segment editor to get a clean model.</p>

---

## Post #9 by @pieper (2024-05-12 18:07 UTC)

<p>Supersampling the segmentation is another effective way to preserve details if you have enough memory.</p>

---
