# Spilling out of the segmentation

**Topic ID**: 3858
**Date**: 2018-08-21
**URL**: https://discourse.slicer.org/t/spilling-out-of-the-segmentation/3858

---

## Post #1 by @alewandow (2018-08-21 14:20 UTC)

<p>I’m following the video tutorial on editor/segment editor to get proper segmantation, but it does not work properly with my CT data.</p>
<p>In my real CT dicom files (even with CONTRAST and after I digged through the MultipleVolumeExplore <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fd51bb4d366cb9007a6baf97881bf8b1875cde4.jpeg" data-download-href="/uploads/short-url/2g3K9cww5bL2VKyQDOdVaKxbPxy.jpeg?dl=1" title="cyst" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fd51bb4d366cb9007a6baf97881bf8b1875cde4_2_690x387.jpeg" alt="cyst" data-base62-sha1="2g3K9cww5bL2VKyQDOdVaKxbPxy" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fd51bb4d366cb9007a6baf97881bf8b1875cde4_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fd51bb4d366cb9007a6baf97881bf8b1875cde4_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fd51bb4d366cb9007a6baf97881bf8b1875cde4_2_1380x774.jpeg 2x" data-dominant-color="989795"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">cyst</span><span class="informations">2953×1660 587 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>, the marked segment “pours” over the whole image height, when I use grow from seed, so even spleen cyst- closed rounded structure is covered by the artefacts. I expected that after picking some area of distinct density in the spleen cyst or in the liver, the segments will expand through the slices but only within those structures.<br>
Maybe this is because the content of spleen cyst or liver are not enough homogenously distinct from the surrounding structured. But how to decrease the sensitivity to increase specificity ?</p>
<p>This is the same in 4.8 and 4.9 last version.</p>

---

## Post #2 by @alewandow (2018-08-21 14:23 UTC)

<p>ps. This is another picture. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d8a32c765e633bc96eb0cac94a041fc48e40d5c.jpeg" data-download-href="/uploads/short-url/6uRzDsgnQvTdTaSNL8tncpwAdg8.jpeg?dl=1" title="cyst2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d8a32c765e633bc96eb0cac94a041fc48e40d5c_2_690x387.jpeg" alt="cyst2" data-base62-sha1="6uRzDsgnQvTdTaSNL8tncpwAdg8" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d8a32c765e633bc96eb0cac94a041fc48e40d5c_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d8a32c765e633bc96eb0cac94a041fc48e40d5c_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d8a32c765e633bc96eb0cac94a041fc48e40d5c_2_1380x774.jpeg 2x" data-dominant-color="979694"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">cyst2</span><span class="informations">1654×930 299 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @alewandow (2018-08-21 14:27 UTC)

<p>This is pthe picture where the segmentation was made by grow from seed in case of liver, and fill between slices for spleen.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e7b42790568964dd94860ffb1970fda12993afc.jpeg" data-download-href="/uploads/short-url/fLmBt7NMluoz9JRhrf3c4jHzMFm.jpeg?dl=1" title="cyst3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e7b42790568964dd94860ffb1970fda12993afc_2_690x369.jpeg" alt="cyst3" data-base62-sha1="fLmBt7NMluoz9JRhrf3c4jHzMFm" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e7b42790568964dd94860ffb1970fda12993afc_2_690x369.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e7b42790568964dd94860ffb1970fda12993afc_2_1035x553.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e7b42790568964dd94860ffb1970fda12993afc_2_1380x738.jpeg 2x" data-dominant-color="959599"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">cyst3</span><span class="informations">1654×886 277 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @alewandow (2018-08-21 14:29 UTC)

<p>ps2. and another strange thing, probably with memory.</p>
<p>Picture attached:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2ea4934fe2e5c93b0cb50fbb20c1f1fca88f9c6.png" data-download-href="/uploads/short-url/rOiAfk8m2WH1XV0fi7qeABl1GD4.png?dl=1" title="SceneView_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2ea4934fe2e5c93b0cb50fbb20c1f1fca88f9c6_2_581x500.png" alt="SceneView_1" data-base62-sha1="rOiAfk8m2WH1XV0fi7qeABl1GD4" width="581" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2ea4934fe2e5c93b0cb50fbb20c1f1fca88f9c6_2_581x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2ea4934fe2e5c93b0cb50fbb20c1f1fca88f9c6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2ea4934fe2e5c93b0cb50fbb20c1f1fca88f9c6.png 2x" data-dominant-color="585565"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SceneView_1</span><span class="informations">716×616 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @cpinter (2018-08-21 14:46 UTC)

<p>Based on the screenshots you give the Grow from seeds algorithm way too little seed. You need to keep refining the seed segments, both background and foreground, so that it gives you a better result. You can do this by drawing green where it should definitely be green not yellow, and vice versa. Only click Apply when the result is satisfactory.</p>
<p>I cannot make out much from the last screenshot, as I don’t know what am I supposed to see in the 2D viewers.</p>

---

## Post #6 by @pieper (2018-08-21 14:59 UTC)

<p>Also if you want just spleen and liver, then you also need to define a background class for everything else.  E.g. paint in rad in the lungs, kidneys, air table, etc.  Let us know if you get it working or have more questions.</p>

---

## Post #7 by @lassoan (2018-08-21 17:01 UTC)

<p>The main issue is what <a class="mention" href="/u/pieper">@pieper</a> described above (you need to add a third segment for “other”, as it is shown in almost all <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">segmentation tutorials</a>).</p>
<p>I’ve also noticed that you have a huge volume and you segment only a small fraction of it, which unnecessarily increases computation time and memory usage. Moreover, slice spacing seems to be larger than in-slice spacing. You can fix both these issues by cropping the input volume to the minimum necessary size (to only contain the object of interests and a small margin) and resample to have isotropic voxel spacing - using “Crop volume” module.</p>

---

## Post #8 by @alewandow (2018-08-22 08:00 UTC)

<p>Thanks a lot. I will try to follow your all suggestions.</p>

---

## Post #9 by @alewandow (2018-08-24 11:04 UTC)

<p>Hello !</p>
<p>I’m trying to make segmentation on another CT example. When using Editor and PaintEffect on the white colored bones and spine, after FastMarching Effect the selected area are completly reversed to selected. Why ?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c07d199b4ccb608ac1c2c288bf8337775caa658d.jpeg" data-download-href="/uploads/short-url/rsPHooJD6ub8sYl0N051oKjGZJj.jpeg?dl=1" title="CDL" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c07d199b4ccb608ac1c2c288bf8337775caa658d_2_690x387.jpeg" alt="CDL" data-base62-sha1="rsPHooJD6ub8sYl0N051oKjGZJj" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c07d199b4ccb608ac1c2c288bf8337775caa658d_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c07d199b4ccb608ac1c2c288bf8337775caa658d_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c07d199b4ccb608ac1c2c288bf8337775caa658d.jpeg 2x" data-dominant-color="ACA89E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CDL</span><span class="informations">1366×768 316 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/108e79fecf34805a22a5ee28b5a1fc21bbb9b57a.jpeg" data-download-href="/uploads/short-url/2msTqYMvGZ5LSMbvlZdmacVS1n4.jpeg?dl=1" title="segmenation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/108e79fecf34805a22a5ee28b5a1fc21bbb9b57a_2_690x366.jpeg" alt="segmenation" data-base62-sha1="2msTqYMvGZ5LSMbvlZdmacVS1n4" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/108e79fecf34805a22a5ee28b5a1fc21bbb9b57a_2_690x366.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/108e79fecf34805a22a5ee28b5a1fc21bbb9b57a_2_1035x549.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/108e79fecf34805a22a5ee28b5a1fc21bbb9b57a.jpeg 2x" data-dominant-color="A3A2A6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segmenation</span><span class="informations">1366×725 240 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Pictures attached.</p>
<p>Tkanks.<br>
Andrzej</p>

---

## Post #10 by @alewandow (2018-08-24 11:14 UTC)

<p>ps. Error report. Maybe it is usefull for you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5fcf38b406f601514d9b90c76d2465c493c6527c.jpeg" data-download-href="/uploads/short-url/dFzkrnjyZ4AnMy2uKL3UfXDPekQ.jpeg?dl=1" title="error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5fcf38b406f601514d9b90c76d2465c493c6527c_2_690x387.jpeg" alt="error" data-base62-sha1="dFzkrnjyZ4AnMy2uKL3UfXDPekQ" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5fcf38b406f601514d9b90c76d2465c493c6527c_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5fcf38b406f601514d9b90c76d2465c493c6527c_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5fcf38b406f601514d9b90c76d2465c493c6527c.jpeg 2x" data-dominant-color="BBB8B7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error</span><span class="informations">1366×768 274 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @pieper (2018-08-24 12:08 UTC)

<aside class="quote no-group" data-username="alewandow" data-post="10" data-topic="3858">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/3bc359/48.png" class="avatar"> alewandow:</div>
<blockquote>
<p>Error report. Maybe it is usefull for you.</p>
</blockquote>
</aside>
<p>Yes, that helps - whenever it says “bad allocation” it means you ran out of memory.  If possible, you can use a bigger computer or you can crop the images.</p>
<p>Also we suggest using the Segment Editor from the latest nightly build rather than the older Editor module which isn’t maintained.</p>

---

## Post #12 by @alewandow (2018-08-24 12:20 UTC)

<p>I sent two posts above that, which you had read. Can you see those too ?</p>

---
