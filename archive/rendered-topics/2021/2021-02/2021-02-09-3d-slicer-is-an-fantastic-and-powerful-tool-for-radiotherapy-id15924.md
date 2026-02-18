# 3D slicer is an fantastic and powerful tool for radiotherapy

**Topic ID**: 15924
**Date**: 2021-02-09
**URL**: https://discourse.slicer.org/t/3d-slicer-is-an-fantastic-and-powerful-tool-for-radiotherapy/15924

---

## Post #1 by @hao (2021-02-09 21:10 UTC)

<p>I am new user of 3D slicer. at first I search on internet for a simple  Dicom viewer but when I tried the 3D slicer, I realize that it is far more than an image viewer. I work in a radiotherapy department in which image fusion (MRI PET etc) and segmentation are very important tache. I am interested in AI segmentation but the first need for our physicist, is the fusion problem for adaptive radiotherapy. They give me a very difficult case in which the patient has an ORL cancer with huge pathological lymph nodes. after 3 weeks radio-chemotherapy, there are significant changement of the volume of the lymph nodes and the second CT scan is done to redo the planning. We have not adaptive tool to transform the old segmentation and all of them need to re-contour manually. there ares about 35 segmentation in this example.<br>
yesterday, I have tried this example with the function of segmentation of 3D Slicer. With the help of community, especially Lassoan and Steve Pieper , I have finally obtain the satisfied results. I am very encouraged by this success because I think that I have just used less than 10% of the total functionality of the 3D slicer. the potential capacity of 3D slicer is great.<br>
My future goal is to use the fully function of AIAA segmentation. I have establish a AIAA server as indicated by Nvidia Clara. Several models are already worked with 3D slicer. I hope with the community we can accomplish this object rapidly.</p>
<p>here are the results of the registration of 2 CT scans of the same patient before and during the treatment.</p>
<ol>
<li>the segmentation of the first CT vs the Second CT,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/258df625d82e57e51193605d1968f52d74862cdd.png" data-download-href="/uploads/short-url/5mdOGEYSXYtidOAJ5P2mCSXerH7.png?dl=1" title="Screenshot from 2021-02-09 15-45-05" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/258df625d82e57e51193605d1968f52d74862cdd_2_690x373.png" alt="Screenshot from 2021-02-09 15-45-05" data-base62-sha1="5mdOGEYSXYtidOAJ5P2mCSXerH7" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/258df625d82e57e51193605d1968f52d74862cdd_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/258df625d82e57e51193605d1968f52d74862cdd_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/258df625d82e57e51193605d1968f52d74862cdd_2_1380x746.png 2x" data-dominant-color="616363"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-02-09 15-45-05</span><span class="informations">1876×1015 486 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
<li>the 2 CT scan before registration<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee471e2683fba3784f9188fc60f4a3f9d4ce340a.jpeg" alt="" data-base62-sha1="xZU0rhxobjbxFuCRlSqJNPOkEv8" role="presentation" width="690" height="488"></li>
<li>after Rigid registration (General registration Brain), pay attention to the difference of the lymph node and the external contour of 2 scan.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99ccc42ec6b761daeb7a8c27bdead2aa23e205bc.jpeg" alt="" data-base62-sha1="lWzLildva3BkI3qkeqBXPEW2OFS" role="presentation" width="690" height="498"></li>
<li>After Bspline transform, the 1er CT scan (moving image volume) is well registered elastically to the 2nd CT scan.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69be0b0eeeae7ba47c6150df497f57902a3ea52d.jpeg" alt="" data-base62-sha1="f5riBsC8JuH5xmTPLbKPIqwdNHD" role="presentation" width="690" height="485"></li>
<li>the segmentation before transform.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad7f4527266b5bd4b0928ef8d352ca1eccc8eed0.jpeg" alt="" data-base62-sha1="oKPhcfAGW1JpJCXNU2PA4TtNSU0" role="presentation" width="686" height="499"></li>
<li>the final results of transformed segmentation.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96a2ccea01f030f6fee6299db3c185ec85aec390.jpeg" alt="" data-base62-sha1="luApYiPF6nhaTrIXN4QOxnL96ec" role="presentation" width="690" height="490"></li>
</ol>
<p>Dr QIU Hao<br>
Oncologue radiothérapie<br>
Centre de radiothérapie de Blois<br>
France</p>

---
