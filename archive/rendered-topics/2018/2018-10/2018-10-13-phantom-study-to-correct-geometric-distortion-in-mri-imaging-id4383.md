# Phantom study to correct geometric distortion in MRI imaging (Moving image) based on CT imaging (Fixed image)

**Topic ID**: 4383
**Date**: 2018-10-13
**URL**: https://discourse.slicer.org/t/phantom-study-to-correct-geometric-distortion-in-mri-imaging-moving-image-based-on-ct-imaging-fixed-image/4383

---

## Post #1 by @shahrokh (2018-10-13 10:28 UTC)

<p>Dears 3DSlicer developers:<br>
Andras Lasso, Csaba Pinter, Andrey Fedorov, Steve Pieper and Thomas Vaughan</p>
<p>Firstly, I Should thank you for all tips and guidances in 3DSlicer and python programming.</p>
<p>In the beginning, I will explain our project and then the steps done briefly.</p>
<p>We defined the project to correct geometric distortion in MRI imaging based on CT imaging. As you definitely know, this problem is occurred in MRI imaging due to the non-uniformity of static and gradient magnetic fields.<br>
To correct this distortion, a phantom was designed and fabricated. This phantom consists of 305 plastic pipes containing water and five perspex sheets drilled to fix these pipes. Except for one of the pipes that was inserted obliquely, the other pipes were aligned in parallel.<br>
The following figures represent 3D views of it.</p>
<p>In CT imaging:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/645c87ba3a539e43fae6a282fefd6d20c5d10201.jpeg" data-download-href="/uploads/short-url/ejPZvrWHqopJOwFVORtkGSXubdL.jpeg?dl=1" title="ScreenshotCT" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/645c87ba3a539e43fae6a282fefd6d20c5d10201_2_643x500.jpeg" alt="ScreenshotCT" data-base62-sha1="ejPZvrWHqopJOwFVORtkGSXubdL" width="643" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/645c87ba3a539e43fae6a282fefd6d20c5d10201_2_643x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/645c87ba3a539e43fae6a282fefd6d20c5d10201.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/645c87ba3a539e43fae6a282fefd6d20c5d10201.jpeg 2x" data-dominant-color="7C7892"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScreenshotCT</span><span class="informations">953×741 361 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In MRI imaging:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a60d61ae0ddeeeda7b5b8f7a3dfcb9c48da6b67.jpeg" data-download-href="/uploads/short-url/jK9mqUAiIIVF6iPN5l50684oB3p.jpeg?dl=1" title="ScreenshotMR" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a60d61ae0ddeeeda7b5b8f7a3dfcb9c48da6b67_2_643x500.jpeg" alt="ScreenshotMR" data-base62-sha1="jK9mqUAiIIVF6iPN5l50684oB3p" width="643" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a60d61ae0ddeeeda7b5b8f7a3dfcb9c48da6b67_2_643x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a60d61ae0ddeeeda7b5b8f7a3dfcb9c48da6b67.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a60d61ae0ddeeeda7b5b8f7a3dfcb9c48da6b67.jpeg 2x" data-dominant-color="7F7F9F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScreenshotMR</span><span class="informations">953×741 293 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Since the geometric distortion is not uniform in the entire FOV of MR, It turns out that the best transformation matrix is found by B-Spline transform to correct this type of distortion. I think that this B-spline transform should be calculated in the entire FOV of MRI. The geometric distortion in MRI imaging can be corrected by using this transform matrix.</p>
<p><strong>Overview of the steps in calculating B-Spline matrix:</strong></p>
<ol>
<li>
<p>Equalize “Image Dimensions”, “Image Spacing” and “Image Origin” between CT and MRI images</p>
</li>
<li>
<p>Segment the phantom pipes in two CT and MR imaging</p>
</li>
<li>
<p>Extract the centerlines of the phantom pipes in two CT and MR imaging using vmtk.</p>
</li>
</ol>
<p>The following figure shows the centerlines of CT and MR images along with axial plane, respectively.</p>
<p>Centerlines CT:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed9085d69e2e243aaeff38baa9edf09a0b6e02fd.png" data-download-href="/uploads/short-url/xTANy33EG34tcum9AK0oRS1ELgh.png?dl=1" title="ScreenshotCenterlinesCT" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed9085d69e2e243aaeff38baa9edf09a0b6e02fd_2_690x355.png" alt="ScreenshotCenterlinesCT" data-base62-sha1="xTANy33EG34tcum9AK0oRS1ELgh" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed9085d69e2e243aaeff38baa9edf09a0b6e02fd_2_690x355.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed9085d69e2e243aaeff38baa9edf09a0b6e02fd_2_1035x532.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed9085d69e2e243aaeff38baa9edf09a0b6e02fd_2_1380x710.png 2x" data-dominant-color="75789B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScreenshotCenterlinesCT</span><span class="informations">1440×741 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Centerlines MR:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af6762ff4a7fdd91a39980ccc3f962337ca1d4fb.png" data-download-href="/uploads/short-url/p1H3RAGFsY5uaZzWfALrHv4SPWP.png?dl=1" title="ScreenshotCenterlinesMR" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af6762ff4a7fdd91a39980ccc3f962337ca1d4fb_2_690x355.png" alt="ScreenshotCenterlinesMR" data-base62-sha1="p1H3RAGFsY5uaZzWfALrHv4SPWP" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af6762ff4a7fdd91a39980ccc3f962337ca1d4fb_2_690x355.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af6762ff4a7fdd91a39980ccc3f962337ca1d4fb_2_1035x532.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af6762ff4a7fdd91a39980ccc3f962337ca1d4fb_2_1380x710.png 2x" data-dominant-color="6A6F8F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScreenshotCenterlinesMR</span><span class="informations">1440×741 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="4">
<li>Calculate the collision points between CT and MR centerlines with axial plans apart at intervals 100 mm.</li>
</ol>
<p>Schematic design the centerlines CT and four axial plans<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bcad954b07b5ab0e3731926ea493ca7c110e657b.png" data-download-href="/uploads/short-url/qV7Fd2Pa902bAZ5ynDjdwVReXKH.png?dl=1" title="ScreenshotCenterlinesCT_4AxialPlans" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bcad954b07b5ab0e3731926ea493ca7c110e657b.png" alt="ScreenshotCenterlinesCT_4AxialPlans" data-base62-sha1="qV7Fd2Pa902bAZ5ynDjdwVReXKH" width="690" height="355" data-dominant-color="8A8DA3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScreenshotCenterlinesCT_4AxialPlans</span><span class="informations">1440×741 40.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Schematic design the centerlines MR and four axial plans<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f9906bc927334cd3200f15efcabed4b32e10681.png" data-download-href="/uploads/short-url/dDHdsnwUETbxWaTLmgfBiU3QF9v.png?dl=1" title="ScreenshotCenterlinesMR_4AxialPlans" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f9906bc927334cd3200f15efcabed4b32e10681_2_690x355.png" alt="ScreenshotCenterlinesMR_4AxialPlans" data-base62-sha1="dDHdsnwUETbxWaTLmgfBiU3QF9v" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f9906bc927334cd3200f15efcabed4b32e10681_2_690x355.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f9906bc927334cd3200f15efcabed4b32e10681_2_1035x532.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f9906bc927334cd3200f15efcabed4b32e10681_2_1380x710.png 2x" data-dominant-color="8289AD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScreenshotCenterlinesMR_4AxialPlans</span><span class="informations">1440×741 44.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Schematic design the collision points centerlines CT and four axial plans<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb883a1a829572237090edd83181e9799fcbe6ef.png" data-download-href="/uploads/short-url/xBC4mWR0PgWOpfTSyKGddpanWuX.png?dl=1" title="ScreenshotPointsCT_4AxialPlans" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb883a1a829572237090edd83181e9799fcbe6ef_2_690x355.png" alt="ScreenshotPointsCT_4AxialPlans" data-base62-sha1="xBC4mWR0PgWOpfTSyKGddpanWuX" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb883a1a829572237090edd83181e9799fcbe6ef_2_690x355.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb883a1a829572237090edd83181e9799fcbe6ef_2_1035x532.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb883a1a829572237090edd83181e9799fcbe6ef_2_1380x710.png 2x" data-dominant-color="8382AD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScreenshotPointsCT_4AxialPlans</span><span class="informations">1440×741 56.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Schematic design the collision points centerlines MR and four axial plans<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2265b2959e0d465c7b1724a30fd1abd881763d1.png" data-download-href="/uploads/short-url/ppZan7mEdWZZvGp7Cgh3VSWffe9.png?dl=1" title="ScreenshotPointsMR_4AxialPlans" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2265b2959e0d465c7b1724a30fd1abd881763d1_2_690x355.png" alt="ScreenshotPointsMR_4AxialPlans" data-base62-sha1="ppZan7mEdWZZvGp7Cgh3VSWffe9" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2265b2959e0d465c7b1724a30fd1abd881763d1_2_690x355.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2265b2959e0d465c7b1724a30fd1abd881763d1_2_1035x532.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2265b2959e0d465c7b1724a30fd1abd881763d1_2_1380x710.png 2x" data-dominant-color="8183A9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScreenshotPointsMR_4AxialPlans</span><span class="informations">1440×741 59.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="5">
<li>
<p>Convert these collision points to markups with the names C and M for CT and MR centerlines.<br>
The number of corresponding markups is equal to 1101 in CT and MR.</p>
</li>
<li>
<p>Calculate the B-Spline transform matrix based on the alignment of C and M Markups using “Scattered Transform” module.</p>
</li>
</ol>
<p>The following figure shows screenshot the module of “Scattered Transform”.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/9300d74b58d503b3e0d9f32a059eb828fd415b16.png" data-download-href="/uploads/short-url/kYrZnt2BKTB1YQ2GVllj0xE5K6O.png?dl=1" title="ScreenshotScattereTransorm" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/9300d74b58d503b3e0d9f32a059eb828fd415b16_2_690x431.png" alt="ScreenshotScattereTransorm" data-base62-sha1="kYrZnt2BKTB1YQ2GVllj0xE5K6O" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/9300d74b58d503b3e0d9f32a059eb828fd415b16_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/9300d74b58d503b3e0d9f32a059eb828fd415b16_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/9300d74b58d503b3e0d9f32a059eb828fd415b16_2_1380x862.png 2x" data-dominant-color="81827E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScreenshotScattereTransorm</span><span class="informations">1440×900 224 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As you see, I set “Initial landmarks” to C (CT markups) and “Displaced landmarks” to M (MR markups). Is it true with considering CT as Fixed Image and MR as Moving Image?</p>
<p>I have some questions as following:</p>
<ol>
<li>
<p>Do you think I’ve done the right steps?</p>
</li>
<li>
<p>To increase the accuracy in the calculation of B-Spline transform, should I increase “B-Spline Grid Spacing” in the section of “Advanced parameters” in the module of “Scattered Transform”?</p>
</li>
<li>
<p>How can I apply this B-Spline Transform to MR images for registration CT and MR?</p>
</li>
</ol>
<p>Please guide me,<br>
Thanks a lot.<br>
Shahrokh</p>

---

## Post #2 by @lassoan (2018-10-13 17:45 UTC)

<aside class="quote no-group" data-username="shahrokh" data-post="1" data-topic="4383">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>Do you think I’ve done the right steps?</p>
</blockquote>
</aside>
<p>“Equalize “Image Dimensions”, “Image Spacing” and “Image Origin” between CT and MRI images” =&gt; This should not be necessary</p>
<p>“Segment the phantom pipes in two CT and MR imaging” =&gt; You don’t need to segment anything. Instead, you can add landmarks at the intersection of planes and tubes. You cannot easily use tube points between planes, because you don’t know how much they are shifted along the tube’s centerline (physical planes do not appear as planar structures in the MRI). If planes are not visible on the MRI at all then you can change your phantom to contain a grid of tubes (don’t make all the tubes parallel). You may use all the tube curve points for validation</p>
<p>Scattered transform module is probably a good choice. The other option would be to compute thin-plate-spline transform using SlicerIGT extension’s Fiducial Registration Wizard module, but in case of hundreds of input points, this transform may be slow to compute.</p>
<aside class="quote no-group" data-username="shahrokh" data-post="1" data-topic="4383">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>How can I apply this B-Spline Transform to MR images for registration CT and MR?</p>
</blockquote>
</aside>
<p>You can apply transforms to any nodes using Transforms module.</p>

---

## Post #3 by @shahrokh (2018-10-14 09:10 UTC)

<p>Dear Andras,</p>
<p>Thanks a lot for your guidance.</p>
<p>As guide me in previous my questions, I can calculate the coordinates of intersections between CT/MR centerlines and the models of axial planes using numpy and vtkPolyData. Excuse me, I checked the correctness of the coordinates of intersections with the positions of axial planes. It looks like the coordinates are true.</p>
<p>At now, my problem is to set parameters in the panel of “Scattered Transform” module, although I studied the given description in ScatteredTransform in SlicerWiki but I did not notice much of it, unfortunately.</p>
<p>In summary, please consider two sets of fiducials with the names of C and M which are related to CT and MR images, respectively (1101 points for each ones of C and M fiducials). At now, I want to have the best spatial resolution in the calculation of B-Spline transform.</p>
<p>Please consider the following volume information (CT images):<br>
Image Dimension: 512x512x173<br>
Image spacing: 0.977x0.977x3.000 mm<br>
Image Origin: (249.512)x(249.512)x(-258.000) mm</p>
<p><strong>My question</strong> : What values should I set for the following parameters?<br>
B-Spline Grid Spacing ?<br>
Minimum domain coordinates ?<br>
Maximum domain coordinates ?<br>
Tolerance ?<br>
Minimum grid spacing ?<br>
Maximum number of levels ?</p>
<p>In other words, can the dimensions of B-Spline transform be equal to the matrix size of MR images?<br>
Or<br>
Can I have a displacement vector computed from scattered transform module per voxel of MR image?</p>
<p>Please guide me,<br>
Shahrokh</p>

---

## Post #4 by @shahrokh (2018-10-15 13:17 UTC)

<p>Excuse me, I hope you will be able to help me.</p>

---

## Post #5 by @lassoan (2018-10-16 14:41 UTC)

<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ScatteredTransform">ScatteredTransform module documentation</a> describes meaning of all parameters. If you have any doubts, read the referenced paper (Joldes et al. 2012) and/or read on B-spline transforms in general.</p>

---
