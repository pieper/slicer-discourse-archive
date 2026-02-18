# How to convert model to markups?

**Topic ID**: 3665
**Date**: 2018-08-05
**URL**: https://discourse.slicer.org/t/how-to-convert-model-to-markups/3665

---

## Post #1 by @Saha_Saha (2018-08-05 15:55 UTC)

<p>Operating system: window 10<br>
Slicer version: 4.9.0<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I have dicom data (CT scan) set of spin. Where I need to get point cloud on the surface of vertebra. So I need markups from a model on the surface of vertebra. Please guide me how can I that.</p>

---

## Post #2 by @Andinet_Enquobahrie (2018-08-05 17:23 UTC)

<p>Not sure if I understand your question.</p>
<p>If you want to create markups from surface models, you can use the Markups module.<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Markups" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Markups</a></p>

---

## Post #3 by @lassoan (2018-08-05 21:27 UTC)

<p>Indeed, from the short description that was provided we can only guess what you would like to do. Please clarify. For example, what do you mean by “DICOM data set of spin”?</p>

---

## Post #4 by @Saha_Saha (2018-08-06 00:37 UTC)

<p>Dear all,</p>
<p>Thank you very much for the reply.</p>
<p>My task is to find optimal path inside the bone channel for placing pedicle screw in vertebra. So I am trying to get point cloud on vertebra so that I can calculate the width automatically and define the optimal path.</p>
<p>I am attaching some pictures for your consideration.<br>
I placed the markups on the surface of the vertebra manually. But I want to place this markups automatically.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79ddd79fb028f22c45682fb6a571c3d302b435b9.png" alt="Master%20Scene%20View" data-base62-sha1="ho54gxgDkVHZr4fMCrNS8wuj0mt" width="584" height="476"></p>

---

## Post #5 by @Saha_Saha (2018-08-06 00:51 UTC)

<p>Dear Andras Lasso,</p>
<p>I have DICOM data set of spin attached below. I used DICOM data set as input in 3D Slicer. Therefore, I chose the model from volume module in slicer. Then I cropped and segmented to get one vertebra.(Described my problem in previous reply)</p>
<p>Thank you very much for you support.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee049613ab5a16eaeac587e93f314dec3314d2f0.png" data-download-href="/uploads/short-url/xXBsLmRv4oL0ChQrrCNXU0h1VmM.png?dl=1" title="Master%20Scene%20View" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee049613ab5a16eaeac587e93f314dec3314d2f0_2_462x500.png" alt="Master%20Scene%20View" data-base62-sha1="xXBsLmRv4oL0ChQrrCNXU0h1VmM" width="462" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee049613ab5a16eaeac587e93f314dec3314d2f0_2_462x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee049613ab5a16eaeac587e93f314dec3314d2f0_2_693x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee049613ab5a16eaeac587e93f314dec3314d2f0_2_924x1000.png 2x" data-dominant-color="9C9ED2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Master%20Scene%20View</span><span class="informations">1122×1214 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2018-08-06 09:12 UTC)

<p>A single approximate entry point should be enough to initialize an automatic trajectory finding algorithm. You can get approximate direction from the image’s standard anatomical orientation.</p>
<p>By specifying two points, you can specify the trajectory completely, which you can use as is, or as an initial guess. A Slicer extension is already available for this:</p>
<div class="lazyYT" data-youtube-id="XN3Tp8jaYdQ" data-youtube-title="3D Slicer - Pedicle Screw Surgical Simulator" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>More information: <a href="https://discourse.slicer.org/t/how-to-install-pedicle-screws-simulator-extension/1073/8">How to install pedicle screws simulator extension?</a></p>

---

## Post #7 by @Saha_Saha (2018-08-07 21:54 UTC)

<p>Thank you very much.</p>
<p>I downloaded from “<a href="https://github.com/smclach/PedicleScrewSimulator" rel="nofollow noopener">https://github.com/smclach/PedicleScrewSimulator</a>”. But It is not working like the video. I think, it has been changed. Some of the function are different. Moreover, screw placement are not working. However, I need to find optimal path through bone channel numerically. So that I can show the evidence that it is the optimal path. Could you please suggest me how can I do?</p>

---

## Post #8 by @lassoan (2018-08-08 07:00 UTC)

<p>I’ve fixed the issues in my fork: <a href="https://github.com/lassoan/PedicleScrewSimulator">https://github.com/lassoan/PedicleScrewSimulator</a></p>
<p>Compute optimal position from a reasonable initial guess should not be a difficult task. If you need hints about how to do it then let us know.</p>

---

## Post #9 by @Saha_Saha (2018-08-08 20:09 UTC)

<p>Please give me the hinds, how can I do it. Moreover, still I am getting error for Load screw and insert screw option. Please find attached picture for your reference. Please give me instruction also for this module, how can I load and insert screw.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eafafedf7bca634b2608f04f3bf41758c9895398.png" data-download-href="/uploads/short-url/xwJtZeLWHVgns9OiKvxIvN67qTm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eafafedf7bca634b2608f04f3bf41758c9895398_2_690x460.png" alt="image" data-base62-sha1="xwJtZeLWHVgns9OiKvxIvN67qTm" width="690" height="460" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eafafedf7bca634b2608f04f3bf41758c9895398_2_690x460.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eafafedf7bca634b2608f04f3bf41758c9895398_2_1035x690.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eafafedf7bca634b2608f04f3bf41758c9895398_2_1380x920.png 2x" data-dominant-color="D7D4DF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1504 627 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @ungi (2018-08-09 23:17 UTC)

<p>Going back to your original question. You don’t just need to convert bone surface points to markups, but you need specific surface points along the pedicle walls as markups. It will be hard to select the right points automatically, so you may need some points selected by the user to initialize your search. Some time ago I planned a few pedicle screw position with Slicer, and I could do it by selecting only 4 points (2 on medial, 2 on lateral side of the pedicle) and registering those with 4 points selected on the screw model. I just used fiducial registration: <a href="http://perk.cs.queensu.ca/contents/ultrasound-snapshots-percutaneous-pedicle-screw-placement-navigation-feasibility-study" rel="nofollow noopener">http://perk.cs.queensu.ca/contents/ultrasound-snapshots-percutaneous-pedicle-screw-placement-navigation-feasibility-study</a></p>
<p>Regardless how automatic your pedicle screw planning gets, the simulator module in Andras’ fork is a great tool to evaluate the result. Maybe combine that quality score in the search algorithm later.</p>

---

## Post #11 by @Saha_Saha (2018-08-13 01:34 UTC)

<p>Thank you for the reply.</p>
<p>How did you get automatic optimal path using 4 points given by user? Could you please explain little more details? I would like to mention you that I have only CT Image available.</p>

---

## Post #12 by @ungi (2018-08-13 04:10 UTC)

<p>It is in the paper I linked. Select a CT slice where the screw long axis would be. Select four points on the pedicle (top left, top right, bottom left, bottom right) cross section. And register matching points pre-defined in the middle of the screw. I just used fiducial (landmark) registration.</p>

---
