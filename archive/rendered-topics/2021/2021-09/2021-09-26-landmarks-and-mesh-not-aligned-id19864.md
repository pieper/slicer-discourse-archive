---
topic_id: 19864
title: "Landmarks And Mesh Not Aligned"
date: 2021-09-26
url: https://discourse.slicer.org/t/19864
---

# Landmarks and mesh not aligned

**Topic ID**: 19864
**Date**: 2021-09-26
**URL**: https://discourse.slicer.org/t/landmarks-and-mesh-not-aligned/19864

---

## Post #1 by @lv_xiao (2021-09-26 11:29 UTC)

<p>Hi everyone, I created a symmetric 3D human facial mesh in R (exported as .ply using vcgPlyWrite function in Rvcg) and also digitised 5 midfacial landmarks along the facial axis of symmetry (exported as fcsv using write.fcsv in Morpho). In R, plotting reveals that the 5 landmarks are exactly along facial midline. However, when I load the .ply and .fcsv into Slicer3d, the landmarks no longer lie along facial midline.</p>
<p>This is the face and landmarks in R:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6208923304bff619d4a697d07e2d9523e122a72.jpeg" data-download-href="/uploads/short-url/wPNwAqfUm0dMmeYUWrRrcRbHrbA.jpeg?dl=1" title="4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6208923304bff619d4a697d07e2d9523e122a72_2_403x500.jpeg" alt="4" data-base62-sha1="wPNwAqfUm0dMmeYUWrRrcRbHrbA" width="403" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6208923304bff619d4a697d07e2d9523e122a72_2_403x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6208923304bff619d4a697d07e2d9523e122a72_2_604x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6208923304bff619d4a697d07e2d9523e122a72_2_806x1000.jpeg 2x" data-dominant-color="BABABA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4</span><span class="informations">1438×1780 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This is the face and landmarks in Slicer3d:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c878206a0ee27554f90198483485a560e33caea.jpeg" data-download-href="/uploads/short-url/k3baymjh829xcM8MAWCtelhJTFo.jpeg?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c878206a0ee27554f90198483485a560e33caea_2_471x500.jpeg" alt="3" data-base62-sha1="k3baymjh829xcM8MAWCtelhJTFo" width="471" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c878206a0ee27554f90198483485a560e33caea_2_471x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c878206a0ee27554f90198483485a560e33caea_2_706x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c878206a0ee27554f90198483485a560e33caea_2_942x1000.jpeg 2x" data-dominant-color="C7EDEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1574×1668 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Similarly, I noted that although the Sample Data Gorilla_template_LM1.fcsv lie on 3D mesh of Gor_template_low_res.ply, when I import both files into R and plot, the landmarks no longer lie on the surface of the mesh.</p>
<p>This is the R code to load and plot the Gorilla data:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c29a9c97bb31fc13bc389d7b10906483f8ef075.jpeg" data-download-href="/uploads/short-url/418DciItlv3iqsMEQaUS4KcxcSV.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c29a9c97bb31fc13bc389d7b10906483f8ef075_2_690x254.jpeg" alt="2" data-base62-sha1="418DciItlv3iqsMEQaUS4KcxcSV" width="690" height="254" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c29a9c97bb31fc13bc389d7b10906483f8ef075_2_690x254.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c29a9c97bb31fc13bc389d7b10906483f8ef075_2_1035x381.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c29a9c97bb31fc13bc389d7b10906483f8ef075_2_1380x508.jpeg 2x" data-dominant-color="F8F8FC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">2082×769 200 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This is a screeshot of the plot generated:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/475db7b464be22137cc4d4707d707572c3dca366.jpeg" data-download-href="/uploads/short-url/abkGK9wiCMOR8MWUAmj4CrExum2.jpeg?dl=1" title="Snipaste_2021-09-26_18-46-51" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/475db7b464be22137cc4d4707d707572c3dca366_2_344x500.jpeg" alt="Snipaste_2021-09-26_18-46-51" data-base62-sha1="abkGK9wiCMOR8MWUAmj4CrExum2" width="344" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/475db7b464be22137cc4d4707d707572c3dca366_2_344x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/475db7b464be22137cc4d4707d707572c3dca366_2_516x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/475db7b464be22137cc4d4707d707572c3dca366_2_688x1000.jpeg 2x" data-dominant-color="EFEFEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snipaste_2021-09-26_18-46-51</span><span class="informations">1082×1572 54.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I want to know why the landmarks that are correctly positioned in R appear incorrectly positioned in Slicer3d and vice versa. What should be done to have the facial landmarks lie along facial midline and on the facial surface in Slicer3d?</p>

---

## Post #2 by @Fluvio_Lobo (2021-09-26 12:34 UTC)

<p><a class="mention" href="/u/lv_xiao">@lv_xiao</a>,</p>
<p>I am not sure what exactly causes this issue, but it looks like the fiducials/markers are maintaining a relative position/orientation with respect with each other, just not the model… perhaps the model and the fiducials/markers don’t share the same origin?</p>
<p>If I were you, I would start by placing some fiducials on the model using slicer, perhaps on the symmetric face model since there are only 4-5. Then, I would export those landmarks as a .fcsv file and compare the data in the file to the one you generated using R.</p>
<p>Let me know if this helps,</p>

---

## Post #3 by @lv_xiao (2021-09-26 14:23 UTC)

<aside class="quote no-group" data-username="Fluvio_Lobo" data-post="2" data-topic="19864">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/fluvio_lobo/48/81262_2.png" class="avatar"> Fluvio_Lobo:</div>
<blockquote>
<p>would start by placing some fiducials on the model using slicer</p>
</blockquote>
</aside>
<p>Thank you for the reply. I agree that probably the issue is due to different origin. I followed your suggestion to place several fiducials in slicer, exported the landmarks, and plotted in R. The points lie perfect well on facial surface as I have done in R.</p>
<p>However, I really need to import some externally digitized landmarks into slicer. Therefore, I wish to figure out how these externally digitized landamrks, when loaded into slicer, could still be correctly positioned.</p>
<p>I have uploaded my facial .ply and .fscv file into <a href="https://github.com/Patricklv/Landmarks-in-Slicer3d-not-correctly-aligned" rel="noopener nofollow ugc">GitHub</a> so that my issue might be better helped.</p>

---

## Post #4 by @muratmaga (2021-09-26 15:10 UTC)

<aside class="quote no-group" data-username="lv_xiao" data-post="1" data-topic="19864">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lv_xiao/48/8224_2.png" class="avatar"> lv_xiao:</div>
<blockquote>
<p>I want to know why the landmarks that are correctly positioned in R appear incorrectly positioned in Slicer3d and vice versa. What should be done to have the facial landmarks lie along facial midline and on the facial surface in Slicer3d?</p>
</blockquote>
</aside>
<p>I can’t comment on why your external landmarks showing up displaced in Slicer, as <a class="mention" href="/u/fluvio_lobo">@Fluvio_Lobo</a> commented there might be other things going on and you will need to troubleshoot it yourself.</p>
<p>As for the gorilla LMs being different in R, I assume that’s because the model was in LPS and R is reading it as if it is RAS.  If you negate the first two coordinates of LMs in R, they should line up.</p>
<p>You can try the SlicerMorphR package and see if the read/write markups function (along with options to specify coordinate system) helps you. See at <a href="https://github.com/SlicerMorph/SlicerMorphR" class="inline-onebox">GitHub - SlicerMorph/SlicerMorphR: R convenience functions for importing SlicerMorph dataset</a></p>

---

## Post #5 by @lv_xiao (2021-09-26 15:51 UTC)

<p>Thank you so much for the explanation. Errors for both data are due to the issue of LPS/RAS. Solved.</p>

---
