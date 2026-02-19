---
topic_id: 14828
title: "Planar Contour To Binary Labelmap Or Model"
date: 2020-12-01
url: https://discourse.slicer.org/t/14828
---

# Planar contour to binary labelmap or model

**Topic ID**: 14828
**Date**: 2020-12-01
**URL**: https://discourse.slicer.org/t/planar-contour-to-binary-labelmap-or-model/14828

---

## Post #1 by @Aaron (2020-12-01 15:54 UTC)

<p>Hi,</p>
<p>I have planar contours that turn into this when I select “Export visible segments to models”:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93f5ace8e6a85e4d3c8e2b55560c66dbfc9ad886.png" alt="image" data-base62-sha1="l6UxOgw5iwtiyM3GyAcEzrKQ8Em" width="258" height="195"><br>
i.e. the contours are not connected.<br>
I think this is because the distance between planes is too large as a result of having transformed all contour points with an affine transformation earlier in the process.<br>
Is there any way to enforce the contours to be connected to get a single closed surface?</p>
<p>Many thanks!</p>

---

## Post #2 by @Sunderlandkyl (2020-12-01 20:50 UTC)

<p>What version of Slicer is this?<br>
Can you send me a message with the saved scene?</p>

---

## Post #3 by @Aaron (2020-12-02 11:23 UTC)

<p>Hi, thank you for looking at this.</p>
<p>The slicer version is: 4.11.20200930 r29402 / 002be18</p>
<p>Here a link to the <a href="https://drive.google.com/file/d/1G122xf0k4r9ZEMvcTDVlXP9jTrQkgYCt/view?usp=sharing" rel="noopener nofollow ugc">scene</a>.</p>
<p>The scene contains the unregistered planar contour (SegmentationFromContourPoints_refgeomT1) and the model created from it, which works fine.<br>
It also contains the planar contour from the registered contour points (SegmentationFromContourPoints_refgeomT2) and the model created from it, which leads to the separated planes model shown in the first post.</p>
<p>The registration had almost no visual effect on the planar contours, i.e. the registered planes are barely distinguishable from the unregistered ones by looking at the 3D view. However when creating the models, it works in the unregistered case, but not in the registered one.</p>
<p>Thanks!</p>

---

## Post #4 by @Aaron (2020-12-03 10:45 UTC)

<p>Hi,</p>
<p>I could narrow down the issue a little bit by modifying the contour point coordinates. Scaling all contour point coordinates (x,y,z) with any number between 0.1 and 10 did not lead to a closed surface. However, scaling only the z-coordinate of all contour points by 0.9 resulted in a closed surface. So the problem doesn’t seem to be related only to the absolute distance between the contour planes.</p>
<p>Another modification of contour points that led to a closed surface was to set all z-values of a plane to a constant value (I chose the z-value of the first contour point of each plane). Is it a requirement for all z-values of a contour line to be the same for the conversion to a model to work?</p>
<p>I also noticed that when the conversion to a model results in several planes (as shown in the first post) the conversion to a binary labelmap does not work either, resulting in a map without any foreground pixels.</p>

---

## Post #5 by @Aaron (2020-12-08 10:51 UTC)

<p>Sorry, I am still struggling to understand why the conversion to a model doesn’t work in the second case. If anyone could explain to me what I’m doing wrong, that would be great.</p>

---

## Post #6 by @Sunderlandkyl (2020-12-08 21:34 UTC)

<p>I don’t think you’re doing anything wrong, there is an issue with the conversion algorithm. I will take a look tomorrow and see if I can fix the problem.</p>

---

## Post #7 by @lassoan (2020-12-09 03:59 UTC)

<aside class="quote no-group" data-username="Aaron" data-post="4" data-topic="14828">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/e19adc/48.png" class="avatar"> Aaron:</div>
<blockquote>
<p>Is it a requirement for all z-values of a contour line to be the same for the conversion to a model to work?</p>
</blockquote>
</aside>
<p>Planar contour representation (as the name suggests) assumes that each contour are exactly planar. If this assumption is violated then anything can happen (I don’t remember if we check or enforce this and what problems can it cause exactly).</p>
<p>If you want to apply transform to a segmentation then change its master representation to closed surface or binary labelmap.</p>

---

## Post #8 by @Aaron (2020-12-09 10:44 UTC)

<p>Thank you, that clarifies things for me.</p>
<p>I am wondering, though, why this is a requirement? The transformed contours are still planar in the sense that all contour points of a contour line are exactly in one plane and all planes are parallel to each other. This is, because the transformation is affine. However, the contour planes are not parallel to the planes of the reference geometry.</p>
<p>Regarding the checks and enforcement, I don’t think there are any, because I used the same pipeline (transform + conversion to binary label map) on more than 200 cases and it seemed to have worked great in all but 2.</p>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="14828">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you want to apply transform to a segmentation then change its master representation to closed surface or binary labelmap.</p>
</blockquote>
</aside>
<p>Is there anything I can do if my starting point are the registered contours? For some cases I don’t have access to the not transformed contours?</p>

---

## Post #9 by @cpinter (2020-12-09 11:12 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="14828">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I don’t remember if we check or enforce this and what problems can it cause exactly</p>
</blockquote>
</aside>
<p>I looked at the code and it seems that only consistent spacing is checked, <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/ConversionRules/vtkPlanarContourToClosedSurfaceConversionRule.cxx#L1244">but not enforced</a>. I did not find any trace for requiring all planes to be parallel in the closed surface conversion, <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/ConversionRules/vtkPlanarContourToRibbonModelConversionRule.cxx#L351">only in the ribbon one</a>.</p>

---

## Post #10 by @Aaron (2020-12-09 11:49 UTC)

<p>Thanks for checking the code.</p>
<p>After the affine transform the spacing should still be consistent and all planes should still be parallel to each other. So these checks/warnings shouldn’t be triggered in this case (and I didn’t notice any warnings during conversion). Did I understand correctly that for this case a check for parallelism between the contour line planes and the reference geometry z-planes would be required?</p>

---

## Post #11 by @cpinter (2020-12-09 11:52 UTC)

<p>The reference volume does not take part in the planar contours to closed surface conversion, so there are no such requirements there.</p>

---

## Post #12 by @Aaron (2020-12-09 11:55 UTC)

<p>In this case, why does applying an affine transform to all contour points cause a problem?</p>

---

## Post #13 by @cpinter (2020-12-09 13:30 UTC)

<p>I’m not sure, but I think if you attach a full log from a session when the conversion fails, then <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> who is most familiar with this particular converter could hopefully figure out the root cause of the problem.</p>

---

## Post #14 by @Aaron (2020-12-09 13:52 UTC)

<p>Ok, thank you very much.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>: Thanks for looking at this. The conversion failure can be reproduced from the <a href="https://drive.google.com/file/d/1G122xf0k4r9ZEMvcTDVlXP9jTrQkgYCt/view?usp=sharing" rel="noopener nofollow ugc">scene</a> I linked. I right-click on the segmentation of the SegmentationFromContourPoints_refgeomT2 node and select “Export visible segments to models”. This leads to the failed model from the first post. Is this sufficient? If not, I’ll send the session log.</p>

---

## Post #15 by @Sunderlandkyl (2020-12-09 21:33 UTC)

<p>Contour planes are transformed so that their normals align with the z-axis before triangulation, but there was a problem with the normal calculation.</p>
<p>I’ve pushed a fix: <a href="https://github.com/SlicerRt/SlicerRT/commit/4abe727357899cc8f854a524307b9238e939ff9e" rel="noopener nofollow ugc">https://github.com/SlicerRt/SlicerRT/commit/4abe727357899cc8f854a524307b9238e939ff9e</a></p>
<p>It should be included in the build tomorrow.</p>

---

## Post #16 by @Aaron (2020-12-10 09:06 UTC)

<p>Thanks a lot for fixing this!</p>

---
