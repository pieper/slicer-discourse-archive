---
topic_id: 19926
title: "Cardiac Mri Loading Erros"
date: 2021-09-30
url: https://discourse.slicer.org/t/19926
---

# Cardiac MRI loading erros

**Topic ID**: 19926
**Date**: 2021-09-30
**URL**: https://discourse.slicer.org/t/cardiac-mri-loading-erros/19926

---

## Post #1 by @xiaolin (2021-09-30 09:36 UTC)

<p>Operating system: Win 10<br>
Slicer version:4.13</p>
<p>Hi everyone,<br>
I am trying to load cardiac MRI (sheep) to slicer, but when I finished the loading, it always showed as the figure. The MRI is a DICOM file with a time frame that was used to analyze the pulmonary valve function with Q-Flow. I want to use the MRI to analyze ventricular function and motion during the cardiac cycle.Does anybody know how to load the MRI coreectly in 3 axises?<br>
Thank you in adavance.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb677c919794567d7d7b9e3cd4632c0a99bb93c9.png" data-download-href="/uploads/short-url/qJR0n0hDe0QH4raJmSCsvkUm7j3.png?dl=1" title="3D Slicer 4.13.0-2021-08-13 30.09.2021 11_11_55" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb677c919794567d7d7b9e3cd4632c0a99bb93c9_2_690x365.png" alt="3D Slicer 4.13.0-2021-08-13 30.09.2021 11_11_55" data-base62-sha1="qJR0n0hDe0QH4raJmSCsvkUm7j3" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb677c919794567d7d7b9e3cd4632c0a99bb93c9_2_690x365.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb677c919794567d7d7b9e3cd4632c0a99bb93c9_2_1035x547.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb677c919794567d7d7b9e3cd4632c0a99bb93c9_2_1380x730.png 2x" data-dominant-color="F2F5F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D Slicer 4.13.0-2021-08-13 30.09.2021 11_11_55</span><span class="informations">1920×1017 83.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/479615df9e57b8b597f484fabae7f16035edd8de.png" data-download-href="/uploads/short-url/adhskDs7iayixCPOnhpK2WkcxtQ.png?dl=1" title="3D Slicer 4.13.0-2021-08-13 30.09.2021 11_24_09" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/479615df9e57b8b597f484fabae7f16035edd8de_2_690x365.png" alt="3D Slicer 4.13.0-2021-08-13 30.09.2021 11_24_09" data-base62-sha1="adhskDs7iayixCPOnhpK2WkcxtQ" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/479615df9e57b8b597f484fabae7f16035edd8de_2_690x365.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/479615df9e57b8b597f484fabae7f16035edd8de_2_1035x547.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/479615df9e57b8b597f484fabae7f16035edd8de_2_1380x730.png 2x" data-dominant-color="8F8F95"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D Slicer 4.13.0-2021-08-13 30.09.2021 11_24_09</span><span class="informations">1920×1017 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-09-30 13:30 UTC)

<p>Have you acquired rotational cone-MRI like this?</p>
<div class="youtube-onebox lazy-video-container" data-video-id="hIxr9OKBvQ8" data-video-title="Reconstruct 3D or 4D cardiac volumes from sparse 2D frame set" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=hIxr9OKBvQ8" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/hIxr9OKBvQ8/maxresdefault.jpg" title="Reconstruct 3D or 4D cardiac volumes from sparse 2D frame set" width="" height="">
  </a>
</div>

<p>If yes, then you are in luck, because SlicerHeart extension can reconstruct such volumes. See details <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/Reconstruct4DCineMRI.md#reconstruct-4d-cine-mri">here</a>.</p>

---

## Post #3 by @xiaolin (2021-10-01 07:50 UTC)

<p>Thanks for your prompt response.<br>
I have never try to rotate the Cine-MRI. How can I get the rotational MRI after loading?<br>
Much appreciate your help.</p>

---

## Post #4 by @lassoan (2021-10-01 17:45 UTC)

<p>How the slice plane moves during the acquisition? Rotates, translates, …, or just stands still?</p>
<p>If the slices don’t move, for example you only have a single slice, or 3 orthogonal slices, then you cannot reconstruct a 3D volume from them. You can still display each slice by drag-and-dropping each from the Data module into a slice view.</p>

---

## Post #5 by @xiaolin (2021-10-04 08:12 UTC)

<p>Hi Prof. Andras Lasso,</p>
<p>After loading the Cine-MRI, I can only play the frame in the sequence browser to get the beating heart (2D)“B”, the slicer can only move in the “A and C”. How can i get the rotational cone-MRI?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f16f0210b4a42adac71fa188dd52f4ccc8a06f8.jpeg" data-download-href="/uploads/short-url/907dXedpBQGT02gv3nSbyiiTZEI.jpeg?dl=1" title="fd4341d45fadd856602b4c5def44bd25bb6d069c_2_1380x730" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f16f0210b4a42adac71fa188dd52f4ccc8a06f8_2_690x365.jpeg" alt="fd4341d45fadd856602b4c5def44bd25bb6d069c_2_1380x730" data-base62-sha1="907dXedpBQGT02gv3nSbyiiTZEI" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f16f0210b4a42adac71fa188dd52f4ccc8a06f8_2_690x365.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f16f0210b4a42adac71fa188dd52f4ccc8a06f8_2_1035x547.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f16f0210b4a42adac71fa188dd52f4ccc8a06f8_2_1380x730.jpeg 2x" data-dominant-color="8D8C93"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fd4341d45fadd856602b4c5def44bd25bb6d069c_2_1380x730</span><span class="informations">1380×730 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks for your help.</p>

---

## Post #6 by @lassoan (2021-10-04 11:54 UTC)

<aside class="quote no-group" data-username="xiaolin" data-post="5" data-topic="19926">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/x/c4cdca/48.png" class="avatar"> xiaolin:</div>
<blockquote>
<p>How can i get the rotational cone-MRI?</p>
</blockquote>
</aside>
<p>Slicer can replay whatever you have acquired and can reconstruct a 3D volume if the slices move in space in a translational or rotational sweep during the acquisition. If the slice position and orientation do not change during the acquisition then it is not possible to reconstruct a 3D volume.</p>

---

## Post #7 by @lassoan (2021-10-07 04:38 UTC)

<p>I’ve checked the sample images that were shared in <a href="https://discourse.slicer.org/t/blood-flow-simulation-from-cardiac-cine-mri/20036/3">this post</a>.</p>
<p>You can load them by enabling “Advanced” mode and selecting the “… Volume Sequence…” loadables:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72054273e557919da24158cf2a9bf605f4495886.png" data-download-href="/uploads/short-url/ggFHpGJW1iY9ZIeGNRxaIotfrYW.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72054273e557919da24158cf2a9bf605f4495886_2_690x418.png" alt="image" data-base62-sha1="ggFHpGJW1iY9ZIeGNRxaIotfrYW" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72054273e557919da24158cf2a9bf605f4495886_2_690x418.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72054273e557919da24158cf2a9bf605f4495886_2_1035x627.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72054273e557919da24158cf2a9bf605f4495886_2_1380x836.png 2x" data-dominant-color="393F45"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2238×1358 428 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Most of the datasets are 4D data sets (3D+t), although most of them just 3-5 slice thick slab (except series 601, which is a bit thicker, as it contains 18 slices). There are also a few flow data sets, which contain 3 sub-sequences (PCA, FFE, and VELOCITY MAP).</p>
<p>I’ve submitted a <a href="https://github.com/fedorov/MultiVolumeImporter/pull/49">pull request</a> to the multi-volume importer module, which will change the default behavior so that you will not need to use the advanced mode to load your sequences as thick slabs. It will probably take just a few days to get integrated into the Slicer Preview Release.</p>

---
