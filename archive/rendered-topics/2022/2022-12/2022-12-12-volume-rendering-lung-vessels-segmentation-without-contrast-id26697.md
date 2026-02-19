---
topic_id: 26697
title: "Volume Rendering Lung Vessels Segmentation Without Contrast"
date: 2022-12-12
url: https://discourse.slicer.org/t/26697
---

# Volume Rendering - Lung Vessels segmentation without contrast

**Topic ID**: 26697
**Date**: 2022-12-12
**URL**: https://discourse.slicer.org/t/volume-rendering-lung-vessels-segmentation-without-contrast/26697

---

## Post #1 by @Eserval (2022-12-12 18:58 UTC)

<p>Hello everyone!</p>
<p>I’m working on my doctorate involving quality in lung resections. For that, I’m segmenting some Lung CT without IV contrast. Sometimes I use volume rendering to help the segmentation process (an excellent suggestion from <a class="mention" href="/u/rbumm">@rbumm</a> ). I usually create a new volume with the lung using the Slipt Volume after the Lung CT Segmenter. However, the external space always makes visualization difficult. Is there a way to make this adjustment?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d7160ecc729d6333a3d1a8cd02343f9f9ae375f.jpeg" data-download-href="/uploads/short-url/1UV7q1BRTNAa8kptR9aSc4W5PLV.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d7160ecc729d6333a3d1a8cd02343f9f9ae375f_2_690x421.jpeg" alt="image" data-base62-sha1="1UV7q1BRTNAa8kptR9aSc4W5PLV" width="690" height="421" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d7160ecc729d6333a3d1a8cd02343f9f9ae375f_2_690x421.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d7160ecc729d6333a3d1a8cd02343f9f9ae375f_2_1035x631.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d7160ecc729d6333a3d1a8cd02343f9f9ae375f.jpeg 2x" data-dominant-color="4D4B4A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1347×823 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @mau_igna_06 (2022-12-12 19:33 UTC)

<p>If the grey box it’s what bothers you I think you can get rid of it by using a fill value of -1024</p>
<p>Hope it helps</p>

---

## Post #3 by @muratmaga (2022-12-12 19:52 UTC)

<aside class="quote no-group" data-username="Eserval" data-post="1" data-topic="26697">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eserval/48/14650_2.png" class="avatar"> Eserval:</div>
<blockquote>
<p>I usually create a new volume with the lung using the Slipt Volume after the Lung CT Segmenter. However, the external space always makes visualization difficult. Is there a way to make this adjustment?</p>
</blockquote>
</aside>
<p>When using either Split Volume or Mask Volume, you need to set the background value to the background value of your datasets. By default it is 0, but for signed datasets this can be a negative value like -1024 (or lower, depends on the data type and reconstruction settings) as <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> mentioned.</p>

---

## Post #4 by @Eserval (2022-12-12 21:12 UTC)

<p>Thanks a lot! That works!  I set the background value to -3024.<br>
Best regards !</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bae9deccd6953acae9611242e3701f75e462e67.jpeg" data-download-href="/uploads/short-url/3WT0pErsbSF1nr1lJIrFnXmcUM7.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bae9deccd6953acae9611242e3701f75e462e67_2_432x500.jpeg" alt="image" data-base62-sha1="3WT0pErsbSF1nr1lJIrFnXmcUM7" width="432" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bae9deccd6953acae9611242e3701f75e462e67_2_432x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bae9deccd6953acae9611242e3701f75e462e67.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bae9deccd6953acae9611242e3701f75e462e67.jpeg 2x" data-dominant-color="DCD8D3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">542×627 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9ac7368510b3a808c12fefab6638f29c4b50e85c.jpeg" data-download-href="/uploads/short-url/m5eldFcTA25sTVZXVsr1ithnr9a.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9ac7368510b3a808c12fefab6638f29c4b50e85c_2_690x388.jpeg" alt="image" data-base62-sha1="m5eldFcTA25sTVZXVsr1ithnr9a" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9ac7368510b3a808c12fefab6638f29c4b50e85c_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9ac7368510b3a808c12fefab6638f29c4b50e85c_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9ac7368510b3a808c12fefab6638f29c4b50e85c_2_1380x776.jpeg 2x" data-dominant-color="A29A99"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1505×848 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @rbumm (2022-12-13 18:41 UTC)

<p>Very nice, <a class="mention" href="/u/eserval">@Eserval</a>. Any new tricks on this one? How do you split the volume so cleanly?</p>

---

## Post #6 by @Eserval (2022-12-13 22:18 UTC)

<p>Thanks <a class="mention" href="/u/rbumm">@rbumm</a>!</p>
<p>1- I use de Lung CT segmenter<br>
2- A litte manual work pinting the mediastinal part of hilar structures in the lung mask to include it.<br>
3- Sometimes litte island from chest wall are included in the mask, so I create a new mask copied from lung mask and aply a little Shrink with the Margin tool.<br>
4- I use the  split volume to create the new volume from the new created mask. To set the background value I used the Local Treshold to find the correct value.</p>

---
