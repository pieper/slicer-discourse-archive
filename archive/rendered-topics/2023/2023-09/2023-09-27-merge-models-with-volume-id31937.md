# Merge Models with Volume

**Topic ID**: 31937
**Date**: 2023-09-27
**URL**: https://discourse.slicer.org/t/merge-models-with-volume/31937

---

## Post #1 by @Bahram_Zargar (2023-09-27 15:56 UTC)

<p>3d Slicer version 5.2.2<br>
OS: Linux Redhat 8<br>
Hello 3D slicer experts,<br>
I do have an MRI volume, with 6 models in my 3D Slicer, and can export each of them separately as DICOM file. However what I want to do is to merge all those modes with the MRI volume, have one final file, with all the models on the source MRI volume then export the as DICOM file. would you please let me know how can I merge models with an MRI volume?<br>
Thank you in advance.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f965ab5ce9d1c4fa16736baceee46202bf369fa.jpeg" data-download-href="/uploads/short-url/94wddZRYownrwXASsEmo4TbTVoK.jpeg?dl=1" title="3d-slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f965ab5ce9d1c4fa16736baceee46202bf369fa_2_690x353.jpeg" alt="3d-slicer" data-base62-sha1="94wddZRYownrwXASsEmo4TbTVoK" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f965ab5ce9d1c4fa16736baceee46202bf369fa_2_690x353.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f965ab5ce9d1c4fa16736baceee46202bf369fa_2_1035x529.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f965ab5ce9d1c4fa16736baceee46202bf369fa_2_1380x706.jpeg 2x" data-dominant-color="7D7E85"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d-slicer</span><span class="informations">1575×806 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2023-09-27 16:24 UTC)

<p>This should work: Import the models in a new segmentation node and use Mask volume effect in Segment Editor.</p>

---

## Post #3 by @Bahram_Zargar (2023-09-27 17:14 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="31937">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Import the models in a new segmentation node</p>
</blockquote>
</aside>
<p>Thanks a lot, it worked. I am wondering how can I use Mask volume effect in Segment Editor and fill inside the volume with colors, rather than filling it in with black or white.</p>

---

## Post #5 by @lassoan (2023-09-28 02:51 UTC)

<p>If you want a colored overlay then you can export the segmentation as DICOM Segmentation Object, using QuantitativeReporting extension. You can then view the segmentation as a color overlay in any DICOM viewer that supports standard segmentation objects.</p>

---
