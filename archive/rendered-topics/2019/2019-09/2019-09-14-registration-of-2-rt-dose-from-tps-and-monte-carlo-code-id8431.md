---
topic_id: 8431
title: "Registration Of 2 Rt Dose From Tps And Monte Carlo Code"
date: 2019-09-14
url: https://discourse.slicer.org/t/8431
---

# Registration of 2 RT Dose from TPS and Monte Carlo code

**Topic ID**: 8431
**Date**: 2019-09-14
**URL**: https://discourse.slicer.org/t/registration-of-2-rt-dose-from-tps-and-monte-carlo-code/8431

---

## Post #1 by @aseman (2019-09-14 20:11 UTC)

<p>Slicer version:4.10.1<br>
Hi 3D Slicer experts and all<br>
I want to compare two RT Dose which are obtained  the first from Treatment Planning System(TPS) and the second from Monte Carlo code (Primo software) , by using the Dose Comparison module in 3D Slicer.the Primo software inputs are CT image, RT Structure, RT Plan and its output is RT Dose. this output is a text file and we converted it to a Dose volume by using the command in the following figure. as shown in figure b ,when the primo RT Dose is imported to slicer, the size of cube in 3D view is changed and these RT Doses(from TPS and Primo) don’t match together.<br>
1- how can I register these RT Doses together automatically ?<br>
2-Although the CT image and RT Dose which are  exported from TPS have different dimensions(CT Dimensions:512,512,89 and rt dose:62,46,88), what is the basis of 3D slicer to match them together? in the other words,is there a specific reference to match them together? and if yes, what is this reference?<br>
thanks a lot<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d94bfa3ccc3535e0d2f885591c9526c963ed42ec.png" data-download-href="/uploads/short-url/v0iojgF6caJo5lVMy1BGxP8o90E.png?dl=1" title="picture%20ommand" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d94bfa3ccc3535e0d2f885591c9526c963ed42ec_2_465x375.png" alt="picture%20ommand" data-base62-sha1="v0iojgF6caJo5lVMy1BGxP8o90E" width="465" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d94bfa3ccc3535e0d2f885591c9526c963ed42ec_2_465x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d94bfa3ccc3535e0d2f885591c9526c963ed42ec_2_697x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d94bfa3ccc3535e0d2f885591c9526c963ed42ec.png 2x" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">picture%20ommand</span><span class="informations">767×618 91.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/029dd901e97d47775644c235681f4fa96c033d33.png" alt="TPS%20RT%20Dose" data-base62-sha1="n98O1PsDUCHcFdVuoIYrv7zUtl" width="323" height="241"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa44c918b0fc5cce37fb64960c9066c4df491a4e.png" alt="primo%20RT%20Dose" data-base62-sha1="oigxCBxQwQEH3bgcdYbMZca9Oea" width="258" height="203"></p>

---

## Post #2 by @lassoan (2019-09-14 22:01 UTC)

<aside class="quote no-group" data-username="aseman" data-post="1" data-topic="8431">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/c0e974/48.png" class="avatar"> aseman:</div>
<blockquote>
<p>how can I register these RT Doses together automatically ?</p>
</blockquote>
</aside>
<p>You don’t need to register the dose volumes, just read image origin, spacing, and axis directions from the computed dose file and set it in the volume node.</p>
<aside class="quote no-group" data-username="aseman" data-post="1" data-topic="8431">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/c0e974/48.png" class="avatar"> aseman:</div>
<blockquote>
<p>Although the CT image and RT Dose which are exported from TPS have different dimensions(CT Dimensions:512,512,89 and rt dose:62,46,88), what is the basis of 3D slicer to match them together? in the other words,is there a specific reference to match them together? and if yes, what is this reference?</p>
</blockquote>
</aside>
<p>Evaluated dose volume is resampled to the reference dose volume’s grid.</p>

---

## Post #3 by @aseman (2019-09-27 17:51 UTC)

<p>Hi 3D Slicer exerts and all<br>
Thank you  very much for your guidance. I could match these RT Doses, by using the volumes and Transforms modules. But the max values for the Primo dose is acquired 293! in volumes module( TPS RT Dose is the reference volume) ; while these values was 2, before matching two RT Dose. why this value is changed and How can I  convert it into 2?<br>
Thanks a lot</p>

---

## Post #4 by @cpinter (2019-09-27 18:06 UTC)

<p>In DICOM the dose values are stored as integer and there is a scaling factor in the header that needs to be applied (done <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Logic/vtkSlicerDicomRtImportExportModuleLogic.cxx#L484-L501" rel="nofollow noopener">here</a> when loading RTDOSE). Maybe there’s something similar with your Primo volumes?</p>

---

## Post #5 by @gcsharp (2019-09-27 18:44 UTC)

<p>aseman, can you state your question more clearly?  Are you saying that the maximum value changed when you used the transform module?  Please describe what you did in a step-by-step manner.</p>

---

## Post #6 by @aseman (2019-09-29 11:30 UTC)

<p>Hi<br>
Sorry for the delay in responding. As I said before, the Primo output ia a text file that we converted to nrrd format by using the above commands. Then , with the sample filters module(Add image filter) , we combined three of these outputs, and after that averaged them by using Shift Scale image filter. then we set the values of image spacing and image origin for primo dose with the TPS Dose , by using the Volumes module. As shown in figure C , initially the min and max values for this volume are 0 and 2.95 (and not 2), respectively. After that we used the Transforms module to change the axis directions in this module.  the following steps were performed respectively:<br>
1: Active Transform : Create new transform<br>
2- Transform matrix: editing the matrix to  [-1 0 0 ; 0 -1 0 ; 0 0 1]  instead of [1 0 0 ; 0 1 0 ; 0 0 1]<br>
3-the primo dose was selected in Transformed node<br>
4-Reference volume: TPS Dose<br>
5- output volume: create new volume<br>
6- Apply<br>
as shows the figure D , the max and min values after transformation are 293 and -317! can you help me about this problem?<br>
Thanks a lot<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5d93aa0d8c9f89de194640704528febe8e52a65.png" alt="before" data-base62-sha1="uvN6Xp0VSpd0qvcV23ft0VhuZRr" width="469" height="285"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4f65e9c3d24c3f2b81edc8af3a8e24e7ea594ed.png" alt="after" data-base62-sha1="pORMV7wiA6TTjnNTLD6ALEUpFZb" width="474" height="252"></p>

---

## Post #7 by @cpinter (2019-09-29 14:57 UTC)

<p>The volumes in C and D are apparently not the untransformed and transformed versions of the same volume, because basic volume information are different. Just look at number of scalars, scalar type, file name… Other volume information are not included in the screenshot, so it doesn’t show if it’s the same node or not. You must have done something between the C and D states that are more than simple geometric alignment.</p>

---

## Post #8 by @gcsharp (2019-09-29 17:16 UTC)

<p>Somehow you seem to have cropped the image.  Look at your “Image Dimensions”.</p>

---

## Post #9 by @aseman (2019-12-02 16:35 UTC)

<p>Hi 3D Slicer experts and all<br>
I’m sorry for my very long delay in replying. As said to me in the first guidance, my goal was to set the Image Spacing, origin and axis directions between the Primo and TPS RT Dose. As mentioned above, I used Volumes and Transforms modules. After Transformation, in addition to the Spacing, Origin and axis directions, the image Dimensions of Primo dose changed to the TPS RT Dose dimensions(figure E)), that resulted in the unacceptable max and min values for Primo dose. ( in Transforms module, the TPS RT Dose was selected as Reference volume). How can I set these parameters without changing in the max and min values of Primo Dose?<br>
Thanks a lot</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54614d484b8340fe8e783e3c8f27a821815f820f.png" alt="RT%20DOSE%20TPS" data-base62-sha1="c2szHxE1MVCkBEvDtYyWOR1BE2H" width="436" height="327"></p>

---

## Post #10 by @lassoan (2019-12-23 04:56 UTC)

<p>If you don’t want voxel values to be changed at all then you can resample using “Resample Scalar/Vector/DWI volume” module with nearest neighbor (nn) interpolation mode.</p>

---
