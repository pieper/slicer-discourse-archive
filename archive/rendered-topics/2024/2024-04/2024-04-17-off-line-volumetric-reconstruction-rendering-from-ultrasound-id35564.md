# Off line volumetric reconstruction/rendering from ultrasound images

**Topic ID**: 35564
**Date**: 2024-04-17
**URL**: https://discourse.slicer.org/t/off-line-volumetric-reconstruction-rendering-from-ultrasound-images/35564

---

## Post #1 by @Caterina (2024-04-17 16:48 UTC)

<p>Dear support,<br>
is it possible to perform offline 3d reconstruction of rendering from ultrasound images?<br>
Thanks</p>

---

## Post #2 by @Nethrav22 (2024-04-18 01:46 UTC)

<p>You can use the Slicer IGT volume reconstruction module with recorded sequence data to perform offline reconstruction.</p>

---

## Post #3 by @Caterina (2024-05-12 20:14 UTC)

<p>I installed SlicerIGT, SlicerAIGT and SlicerIGSIO. These modules resulted installed but they are not present in module finder. In addition, I’m having trouble segmenting a region from ultrasound images GE Vivid E95 in 3D Slicer. I have already read the previous post: <a href="https://discourse.slicer.org/t/issue-with-3d-tee-from-ge-vivid-e95-in-3d-slicer/13642" class="inline-onebox">Issue With 3D TEE from GE Vivid E95 in 3D Slicer</a>. More specifically, considering only the scalar volume file (see screen)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be2f5523e2ea8b4a36d4b5ce6036254968e1e240.png" data-download-href="/uploads/short-url/r8s7ZKD9zPEJOtVS0XAaFWhLQR2.png?dl=1" title="Screenshot 2024-05-12 alle 21.56.16" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be2f5523e2ea8b4a36d4b5ce6036254968e1e240_2_690x89.png" alt="Screenshot 2024-05-12 alle 21.56.16" data-base62-sha1="r8s7ZKD9zPEJOtVS0XAaFWhLQR2" width="690" height="89" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be2f5523e2ea8b4a36d4b5ce6036254968e1e240_2_690x89.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be2f5523e2ea8b4a36d4b5ce6036254968e1e240_2_1035x133.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be2f5523e2ea8b4a36d4b5ce6036254968e1e240_2_1380x178.png 2x" data-dominant-color="E2E2E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-05-12 alle 21.56.16</span><span class="informations">1640×212 15.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>, I cropped the interested region but it is static. If I considered the crop volume sequence module, the input volume sequence, does not recognize the source file as a sequence. The volume rendering option provides this view (see attach<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/043de12803e8dd761f7845e822098a99262589f3.jpeg" data-download-href="/uploads/short-url/Bwu8HCKsSEK27kxuq0fSVyxQFZ.jpeg?dl=1" title="Screenshot 2024-05-12 alle 22.03.55" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/043de12803e8dd761f7845e822098a99262589f3_2_690x368.jpeg" alt="Screenshot 2024-05-12 alle 22.03.55" data-base62-sha1="Bwu8HCKsSEK27kxuq0fSVyxQFZ" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/043de12803e8dd761f7845e822098a99262589f3_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/043de12803e8dd761f7845e822098a99262589f3_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/043de12803e8dd761f7845e822098a99262589f3_2_1380x736.jpeg 2x" data-dominant-color="666179"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-05-12 alle 22.03.55</span><span class="informations">1920×1025 84.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>).<br>
The segmentation performed using threshold method is not good (<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be3dede178724107d9b9f4568b0987a5592bf6b5.png" data-download-href="/uploads/short-url/r8XoVN1IsZUAIgDhML0PZgHo6Rn.png?dl=1" title="Screenshot 2024-05-12 alle 22.06.17" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be3dede178724107d9b9f4568b0987a5592bf6b5_2_690x410.png" alt="Screenshot 2024-05-12 alle 22.06.17" data-base62-sha1="r8XoVN1IsZUAIgDhML0PZgHo6Rn" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be3dede178724107d9b9f4568b0987a5592bf6b5_2_690x410.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be3dede178724107d9b9f4568b0987a5592bf6b5_2_1035x615.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be3dede178724107d9b9f4568b0987a5592bf6b5_2_1380x820.png 2x" data-dominant-color="5D5F70"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-05-12 alle 22.06.17</span><span class="informations">1736×1034 79.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>.<br>
Any suggestion on how to perform a good and time-varying segmentation as the original file?<br>
Thanks</p>

---

## Post #4 by @pieper (2024-05-12 21:56 UTC)

<aside class="quote no-group" data-username="Caterina" data-post="3" data-topic="35564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/439d5e/48.png" class="avatar"> Caterina:</div>
<blockquote>
<p>volume rendering option provides this view</p>
</blockquote>
</aside>
<p>That appears to be a sequence of frames from a cine recording of a rendering made on some other system, not a volumetric dataset.  You’ll need to see if you’ve got an actual volume in your study.</p>

---

## Post #5 by @Caterina (2024-05-15 10:18 UTC)

<p>Dear <a class="mention" href="/u/pieper">@pieper</a>, thanks a lot.<br>
If Slicer produces a volume rendering, the imported file contains information about volume.<br>
Is it correct?</p>

---

## Post #6 by @pieper (2024-05-15 11:44 UTC)

<p>I’m not sure I follow your question exactly, but generally speaking the data acquisition should include a volume, since it appears from your screenshot that the system made a volume rendering and saved out a movie.  If you can load the volume data you should be able to make a similar image in slicer but live, so you can adjust the parameters, like rotation and thresholding.</p>

---
