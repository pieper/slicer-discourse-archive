---
topic_id: 15374
title: "Interactive Lobe Segmentation On Chest Imaging Platform"
date: 2021-01-06
url: https://discourse.slicer.org/t/15374
---

# Interactive lobe segmentation on Chest Imaging Platform

**Topic ID**: 15374
**Date**: 2021-01-06
**URL**: https://discourse.slicer.org/t/interactive-lobe-segmentation-on-chest-imaging-platform/15374

---

## Post #1 by @JMC (2021-01-06 10:34 UTC)

<p>Hello everyone,<br>
I have created a lung lobe segmentation using Interactive lobe segmentation on Chest Imaging Platform but I don’t know how to calculate the volume of each lung and each lobe. Is there a way to get the volumes of each lobe and lung from the segmentation created with Interactive lobe segmentation?<br>
Thanks a lot</p>

---

## Post #2 by @lassoan (2021-01-06 15:40 UTC)

<p>You can right-click on the lobe segmentation result labelmap to convert it to segmentation then use Segment Statistics module to get volumes.</p>

---

## Post #3 by @JMC (2021-01-06 19:52 UTC)

<p>Thank you very much Andras,<br>
I have tried but have not succeeded. I can’t select the lobe segmentation result labelmap to convert it to segmentation on my MAC. I must be doing something wrong<br>
Also I would like to create a 3D model from this segmentation, is it possible?<br>
I will keep trying!!!</p>

---

## Post #4 by @lassoan (2021-01-06 20:18 UTC)

<p>I’m not sure what node type is the result of lobe segmentation. Could you upload an example somewhere (save the entire scene as a .mrb file) and post the link here so that I can have a look?</p>
<aside class="quote no-group" data-username="JMC" data-post="3" data-topic="15374">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jmc/48/9439_2.png" class="avatar"> JMC:</div>
<blockquote>
<p>Also I would like to create a 3D model from this segmentation, is it possible?</p>
</blockquote>
</aside>
<p>Yes, once you have your lobes in a segmentation node, you can create a 3D model by a single click.</p>

---

## Post #5 by @JMC (2021-01-07 14:25 UTC)

<p><a href="https://drive.google.com/drive/folders/1Eux1f8_2tuaKIjoojblDmBDio-ZjK5gl?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1Eux1f8_2tuaKIjoojblDmBDio-ZjK5gl?usp=sharing</a></p>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1MIgr7anCLpOO8oDah0Hu-dD_rK1KvGbs/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1MIgr7anCLpOO8oDah0Hu-dD_rK1KvGbs/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1MIgr7anCLpOO8oDah0Hu-dD_rK1KvGbs/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">2021-01-07-Scene.mrb</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>This the link of my lobe segmentation.<br>
Thank you very much Andras,<br>
Sorry for the inconvenience.<br>
I am a radiologist and I am starting to use 3DSlicer for 3D printing. Everything that can be done with 3D Slicer is impressive, although it takes a bit of learning to use it.<br>
Thanks a lot</p>

---

## Post #6 by @lassoan (2021-01-07 17:12 UTC)

<p>Everything works as expected. Right-click on the labelmap and choose to convert to segmentation node:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2ab8ef3a0cd312045797049d39622cf227547431.png" data-download-href="/uploads/short-url/65WgZsIowoPWXXutg1bQ973Q9pf.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ab8ef3a0cd312045797049d39622cf227547431_2_385x500.png" alt="image" data-base62-sha1="65WgZsIowoPWXXutg1bQ973Q9pf" width="385" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ab8ef3a0cd312045797049d39622cf227547431_2_385x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ab8ef3a0cd312045797049d39622cf227547431_2_577x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ab8ef3a0cd312045797049d39622cf227547431_2_770x1000.png 2x" data-dominant-color="3E3E3B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">963×1248 92.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Click Closed surface → Create in Segmentations module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ef9701732e6bc3535fca4460d5ec5ec11709f10.png" data-download-href="/uploads/short-url/fPIWgVlUBqfHG0BqZHnaS44xkeA.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ef9701732e6bc3535fca4460d5ec5ec11709f10_2_423x500.png" alt="image" data-base62-sha1="fPIWgVlUBqfHG0BqZHnaS44xkeA" width="423" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ef9701732e6bc3535fca4460d5ec5ec11709f10_2_423x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ef9701732e6bc3535fca4460d5ec5ec11709f10_2_634x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ef9701732e6bc3535fca4460d5ec5ec11709f10_2_846x1000.png 2x" data-dominant-color="40403F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">913×1079 58.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can adjust opacity to see inside the segmentation:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c897482c8a3656e3cd775a52c1448be684748c78.jpeg" data-download-href="/uploads/short-url/sCvC4IbuQpr4WY8RCoXeT78qECk.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c897482c8a3656e3cd775a52c1448be684748c78_2_592x500.jpeg" alt="image" data-base62-sha1="sCvC4IbuQpr4WY8RCoXeT78qECk" width="592" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c897482c8a3656e3cd775a52c1448be684748c78_2_592x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c897482c8a3656e3cd775a52c1448be684748c78_2_888x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c897482c8a3656e3cd775a52c1448be684748c78_2_1184x1000.jpeg 2x" data-dominant-color="656468"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1324×1118 283 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @JMC (2021-01-07 17:50 UTC)

<p>Thank you very much Andras,<br>
What a great help !!<br>
If instead of using “unnamed Series_partialLungLabelMap-segmentation” we use “unnamed Series_interactiveLobeSegmentation” we create the anatomy of the pulmonary lobes perfectly.<br>
Simply wonderful.<br>
Thank you so much for everything</p>

---

## Post #8 by @Tibor_Krajc (2021-02-28 18:55 UTC)

<p>Hi András,<br>
I have been looking for the Segment Statistics module but it is not offered by my Extensions Manager. No trace of it in the list of all installed modules either. Using Slicer 4.10.2 r28257. Could you please point me in the right direction?<br>
Kôszônom szépen!</p>

---

## Post #9 by @lassoan (2021-02-28 19:47 UTC)

<p>The module might have been added after Slicer-4.10. It is available in current Slicer releases.</p>

---
