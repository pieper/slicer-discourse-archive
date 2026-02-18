# How to apply a BSpline Transformation Field(produced by a registration) to another volume image(for DeepLearning Data Augmentation)? 

**Topic ID**: 3923
**Date**: 2018-08-28
**URL**: https://discourse.slicer.org/t/how-to-apply-a-bspline-transformation-field-produced-by-a-registration-to-another-volume-image-for-deeplearning-data-augmentation/3923

---

## Post #1 by @Scorbinwen (2018-08-28 13:40 UTC)

<p>Operating system: window10<br>
Slicer version:4.8.1<br>
Expected behavior:<br>
Actual behavior:<br>
I’m now ongoing a project of medical image analysis based on deep learning,but the dataset I can obtain is really limited,so I want augment the dataset by applying non-rigid transformation on the dataset I now have to obtain new volumes with different shape.<br>
I use  registration two volumes to get a transformation grid field,but when I apply this transformation to another volumes,I notice that the volume does not match the field of transformation grid field:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b073d9dc58befce1c36432613d409dae7933029a.png" data-download-href="/uploads/short-url/paYf9HZvQtRVug8epKIS9Y8bgTw.png?dl=1" title="field" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b073d9dc58befce1c36432613d409dae7933029a_2_690x491.png" alt="field" data-base62-sha1="paYf9HZvQtRVug8epKIS9Y8bgTw" width="690" height="491" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b073d9dc58befce1c36432613d409dae7933029a_2_690x491.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b073d9dc58befce1c36432613d409dae7933029a_2_1035x736.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b073d9dc58befce1c36432613d409dae7933029a.png 2x" data-dominant-color="515359"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">field</span><span class="informations">1052×750 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
How can I move the volume to the field of transformation field?<br>
I’ve tried to translate the volume, but it seem strange that the volume looks not translated after I reload the saved the translated volume.</p>

---

## Post #2 by @lassoan (2018-08-28 14:05 UTC)

<p>If you only want to apply non-rigid transformation then you need to align the images first with rigid transformation and harden the transform on the moving volume. If you register these rigidly aligned images using deformable registration, then the resulting transform will only contain the deformable component.</p>

---

## Post #3 by @Scorbinwen (2018-09-01 01:52 UTC)

<p>Thank you so much,I’ve solve this according to your helpful advice:<br>
It didn’t work because I did not resample the rigidly aligned volumes.After I resample the rigidly aligned volumes and then reload the volume,I found that the volume is cropped outside the volume field,and then I solved this problem according to your advice from :<a>https://discourse.slicer.org/t/save-transformed-data/2151/8</a> :<br>
"</p>
<p>For most resample modules you can specify an output geometry (by selecting a reference volume), you just have to set that output geometry to avoid any undesired cropping</p>
<p>."</p>

---

## Post #4 by @Scorbinwen (2018-09-01 02:09 UTC)

<p>I have another question:<br>
I want enlarge the scale  factor of the BSpline Transformation to make the volumes deform larger,I’ve notice there is a option under the “Advance”:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/233870b4c4b6e6d1fdd57c6ac3f7a28faeb04dca.png" data-download-href="/uploads/short-url/51zDjIqFtXcgpNN73ZVVuoq3QLg.png?dl=1" title="field" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/233870b4c4b6e6d1fdd57c6ac3f7a28faeb04dca_2_690x310.png" alt="field" data-base62-sha1="51zDjIqFtXcgpNN73ZVVuoq3QLg" width="690" height="310" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/233870b4c4b6e6d1fdd57c6ac3f7a28faeb04dca_2_690x310.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/233870b4c4b6e6d1fdd57c6ac3f7a28faeb04dca_2_1035x465.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/233870b4c4b6e6d1fdd57c6ac3f7a28faeb04dca_2_1380x620.png 2x" data-dominant-color="898684"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">field</span><span class="informations">1600×721 362 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
but enlarge the scale factor here does not  actually make  the  volumes deform larger.I’ve also save the BSpline transformation after enlarge the scale factor,and then reload the transform,it looks that the transform does not change at all.<br>
What should I do,any hints?<br>
Thank you.</p>

---
