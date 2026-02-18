# FEM Mesh Analysis & Visualization in Model Module

**Topic ID**: 9376
**Date**: 2019-12-04
**URL**: https://discourse.slicer.org/t/fem-mesh-analysis-visualization-in-model-module/9376

---

## Post #1 by @lausiv (2019-12-04 06:16 UTC)

<p>FEM Mesh Analysis &amp; Visualization in Model Module (refers below picture :-))</p>
<p>in other words, for example.</p>
<p>each mesh, i want to calculate mesh volume and display different color corresponding  to the volume.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da43a2964e54a932fd331f5142f507d97cd60d3b.png" data-download-href="/uploads/short-url/v8QZL1vPppDclVfyt0yb0vAKQRB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da43a2964e54a932fd331f5142f507d97cd60d3b_2_690x314.png" alt="image" data-base62-sha1="v8QZL1vPppDclVfyt0yb0vAKQRB" width="690" height="314" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da43a2964e54a932fd331f5142f507d97cd60d3b_2_690x314.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da43a2964e54a932fd331f5142f507d97cd60d3b_2_1035x471.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da43a2964e54a932fd331f5142f507d97cd60d3b_2_1380x628.png 2x" data-dominant-color="928269"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1760×801 232 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-12-04 07:36 UTC)

<p>Does “Information” section shows the correct volume?<br>
You can color each mesh using a solid color (Display/Visibility/Color) or you can use scalars to color different parts of a model with different colors.</p>

---

## Post #3 by @lausiv (2019-12-04 13:09 UTC)

<p>Does “Information” section shows the correct volume?<br>
==&gt; yes^^</p>
<p>You can color each mesh using a solid color (Display/Visibility/Color)<br>
==&gt;   all of the mesh was drawn by same color ^^;<br>
i want to color each mesh with different color.<br>
each mesh, i want to calculate mesh volume and display different color corresponding to each mesh(not all of the mesh)</p>
<pre><code>    i think that Threshold in Scalars section can be used to calcuate color(0~255)
    i am now finding the source code related to this issue.
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89599dfc41d27d876d990e5ac2ff3142ad59862d.png" data-download-href="/uploads/short-url/jB3pRYCaEfNxS2X8dxxB1dVrRLv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89599dfc41d27d876d990e5ac2ff3142ad59862d_2_552x500.png" alt="image" data-base62-sha1="jB3pRYCaEfNxS2X8dxxB1dVrRLv" width="552" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89599dfc41d27d876d990e5ac2ff3142ad59862d_2_552x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89599dfc41d27d876d990e5ac2ff3142ad59862d_2_828x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89599dfc41d27d876d990e5ac2ff3142ad59862d_2_1104x1000.png 2x" data-dominant-color="AD7667"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1441×1303 511 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lausiv (2019-12-04 13:18 UTC)

<p>I found source code inqMRMLModelDisplayNodeWidget.cxx.<br>
in this source code. i can calcuate and set the color on each mesh from the input of Value in Model Display Widget UI ex. Threshold(Scalors section)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b250956e38e15aee1c2597051bb5f1edcb330b3.png" data-download-href="/uploads/short-url/8rdwiVBDoNf4YBeCn0vmOncUUKf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b250956e38e15aee1c2597051bb5f1edcb330b3.png" alt="image" data-base62-sha1="8rdwiVBDoNf4YBeCn0vmOncUUKf" width="689" height="402" data-dominant-color="1D2E3C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1223×714 57.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2019-12-04 15:57 UTC)

<p>You can assign a color to each mesh cell or point by assigning a scalar array to them and then configuring coloring in Models module’s Scalars section.</p>

---

## Post #6 by @lausiv (2019-12-04 16:27 UTC)

<p>Scalar Array? for example?<br>
It means only editing Scalar  Section in Model module can differentiate color each mesh or point?</p>

---

## Post #7 by @lassoan (2019-12-04 16:54 UTC)

<p>Normally you assign scalar values to points or cells of your mesh when generate the mesh (e.g., you can have a scalar attribute to specify material or a physical quantity).</p>
<p>How did you generate the mesh?</p>

---

## Post #8 by @lausiv (2019-12-05 00:47 UTC)

<p>How did you generate the mesh?<br>
<strong>==&gt;Tetzen(Segment Mesher) on segmented surface of Brain Volume^^. I described in detail. plz refer below texts</strong></p>
<p>Normally you assign scalar values to points or cells of your mesh when generate the mesh (e.g., you can have a scalar attribute to specify material or a physical quantity).<br>
<strong>==&gt; i am now reading manual_tezen.pdf <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> Would u plz introduce using Scalar Array by example code?</strong> . My Mesh Analysis is related with Laplacian Equation, so i want to calculate laplacian function on each mesh cell(or point)</p>
<blockquote>
<p><em>You can assign a color to each mesh cell or point by assigning a scalar array to them and then configuring coloring in Models module’s Scalars section.</em><br>
<em>==&gt; I found it Scalars section, Active Scalar</em><br>
<em><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23669f0672726c63cdcbf5a19626ed9e021d60a2.png" alt="image" data-base62-sha1="53azJvJvmbYR9NHJy9rX1Mud1e2" width="588" height="218"></em></p>
</blockquote>
<p>===========================================================</p>
<p>Finite Element Mesh Generation &amp; Visualization for Brain Volume Analysis</p>
<p>Input :  Brain MR Volume</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c98af6ca8fcfb69e54f6529699b9af3190ca326f.jpeg" data-download-href="/uploads/short-url/sKVHraRefXLNpOpz65FGVljfyiP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c98af6ca8fcfb69e54f6529699b9af3190ca326f_2_567x500.jpeg" alt="image" data-base62-sha1="sKVHraRefXLNpOpz65FGVljfyiP" width="567" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c98af6ca8fcfb69e54f6529699b9af3190ca326f_2_567x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c98af6ca8fcfb69e54f6529699b9af3190ca326f_2_850x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c98af6ca8fcfb69e54f6529699b9af3190ca326f.jpeg 2x" data-dominant-color="779BA5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1052×927 276 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Output : FE Mesh Generation</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c1c384d8600a964e14f4c5af9baea15d71e3130.png" data-download-href="/uploads/short-url/8zL6LAxCIaORf6KZ1UGuaDzoi3u.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c1c384d8600a964e14f4c5af9baea15d71e3130_2_525x500.png" alt="image" data-base62-sha1="8zL6LAxCIaORf6KZ1UGuaDzoi3u" width="525" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c1c384d8600a964e14f4c5af9baea15d71e3130_2_525x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c1c384d8600a964e14f4c5af9baea15d71e3130_2_787x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c1c384d8600a964e14f4c5af9baea15d71e3130_2_1050x1000.png 2x" data-dominant-color="694A59"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1052×1001 593 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Workflow :<br>
1.DICOM Import<br>
2.Segment Editor<br>
<strong>3.Segment Mesher</strong><br>
4.Models</p>
<p>After 1.DICOM Import</p>
<p>2.Segment Editor → Choose Interested RT Structure(Surface Segment)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a06ba8814940d43188db5d32d7a6711c4b373fc2.png" data-download-href="/uploads/short-url/mT93dHdhyaiX6yOqpYpYNa02Ads.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a06ba8814940d43188db5d32d7a6711c4b373fc2_2_384x499.png" alt="image" data-base62-sha1="mT93dHdhyaiX6yOqpYpYNa02Ads" width="384" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a06ba8814940d43188db5d32d7a6711c4b373fc2_2_384x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a06ba8814940d43188db5d32d7a6711c4b373fc2_2_576x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a06ba8814940d43188db5d32d7a6711c4b373fc2.png 2x" data-dominant-color="EBEEF3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">594×773 34.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b45604d7e6ed5d08436eb5c872fb78a57777ef1.png" alt="image" data-base62-sha1="6aNatGWndpkad2aEDwYMf4uOkBr" width="281" height="288"></p>
<p><strong>3.Segment Mesher → Meshing method(TetGen) → Apply</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfe3bf409846499156810f946d5d51b4e08de96e.png" data-download-href="/uploads/short-url/tF4MuY7eqiHQMhJ8AKoNy2YtwKO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfe3bf409846499156810f946d5d51b4e08de96e.png" alt="image" data-base62-sha1="tF4MuY7eqiHQMhJ8AKoNy2YtwKO" width="384" height="499" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">594×773 24.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>4.Models</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c6c5a3d3fb0676e5a67e9b019d25823504c3f87.png" data-download-href="/uploads/short-url/dbC4qB7wDnv6bpptuaIQNZ74e9N.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c6c5a3d3fb0676e5a67e9b019d25823504c3f87_2_417x500.png" alt="image" data-base62-sha1="dbC4qB7wDnv6bpptuaIQNZ74e9N" width="417" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c6c5a3d3fb0676e5a67e9b019d25823504c3f87_2_417x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c6c5a3d3fb0676e5a67e9b019d25823504c3f87.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c6c5a3d3fb0676e5a67e9b019d25823504c3f87.png 2x" data-dominant-color="F3F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">601×720 29.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2019-12-05 02:03 UTC)

<p>You need to use Cleaver to generate multi-material meshes.</p>
<p>Tetgen could probably generate multi-material meshes too, but since it seemed quite complicated to set it up, and Tetgen had some stability issues, and comes with restrictive (GPL-type or commercial) license, we did not spend much time with improving Tetgen support. Cleaver works nicely, supports multiple materials, and freely usable, with non-restrictive license.</p>

---

## Post #10 by @lausiv (2019-12-05 03:26 UTC)

<p>Thank you so much, i am now reading cleaver mesh rendering process</p>

---

## Post #11 by @lausiv (2019-12-06 12:43 UTC)

<p>Normally you assign scalar values to points or cells of your mesh when generate the mesh</p>
<p>(e.g., you can have a scalar attribute to specify material or a physical quantity).<br>
==&gt; How can i set a scalar attribute… would introduce sample code(or workflow). i want to set individual color on each mesh(or point) by scalar array eg. laplacian equation y=ax+b )</p>
<p>(i didn’t find the corresponding source code or document )</p>

---

## Post #12 by @lassoan (2019-12-06 15:08 UTC)

<p>You can use <a href="https://vtk.org/doc/nightly/html/classvtkArrayCalculator.html">vtkArrayCalculator</a> or add a point or cell array and set its values from Python. See how you can get read/write access to point coordinates and point arrays <a href="https://github.com/Slicer/Slicer/blob/805f36a35fe6e301c8f908dfffe70bf615c31232/Base/Python/slicer/util.py#L976-L1007">here</a>.</p>

---

## Post #13 by @lausiv (2019-12-07 05:23 UTC)

<p>I will do it. and Let it share in this page^^</p>

---

## Post #14 by @lausiv (2019-12-08 14:43 UTC)

<p>I have found python script code written by you(Andras Lasso).<br>
But. It has some problem.<br>
I am now checkout latest slicer version .</p>
<p>Would u introduce modification point for all of the mesh, not some mesh?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18727d0700a7007ae79336eec289da69885c9346.png" data-download-href="/uploads/short-url/3ugKtce8j2fQbrGtB624rm6oO3A.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18727d0700a7007ae79336eec289da69885c9346.png" alt="image" data-base62-sha1="3ugKtce8j2fQbrGtB624rm6oO3A" width="543" height="500" data-dominant-color="F9F6FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1301×1197 45 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/504f6c098c3e00cbfee8f89fa0bab4225552a3d9.png" data-download-href="/uploads/short-url/bssmebQLsLWra8k8HeAMtolZVSV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/504f6c098c3e00cbfee8f89fa0bab4225552a3d9.png" alt="image" data-base62-sha1="bssmebQLsLWra8k8HeAMtolZVSV" width="543" height="500" data-dominant-color="F1F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1301×1197 38.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f8261af1125092ef1047c68237ecc5db9a2f6f2.png" data-download-href="/uploads/short-url/93Pq9HNdMNkBlUBaAnO0NE5q0pA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f8261af1125092ef1047c68237ecc5db9a2f6f2.png" alt="image" data-base62-sha1="93Pq9HNdMNkBlUBaAnO0NE5q0pA" width="593" height="499" data-dominant-color="9F9D6E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">672×566 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @lausiv (2019-12-08 14:46 UTC)

<p>i have found error message when i use Cleaver instead of Tetzen at preview release. it</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6f862a3fc2579a4266949d453d50190ee53003a.png" data-download-href="/uploads/short-url/nP5qeGVA23Uu2XAQra7zPvssCXo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6f862a3fc2579a4266949d453d50190ee53003a_2_690x370.png" alt="image" data-base62-sha1="nP5qeGVA23Uu2XAQra7zPvssCXo" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6f862a3fc2579a4266949d453d50190ee53003a_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6f862a3fc2579a4266949d453d50190ee53003a_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6f862a3fc2579a4266949d453d50190ee53003a_2_1380x740.png 2x" data-dominant-color="A0B0AB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1626×873 220 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48ec31dbfc23705d54e5197acf2aa2d3fedb19be.png" data-download-href="/uploads/short-url/ap6qdjood0ax0lDZTjNUHEX1CvY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48ec31dbfc23705d54e5197acf2aa2d3fedb19be_2_690x136.png" alt="image" data-base62-sha1="ap6qdjood0ax0lDZTjNUHEX1CvY" width="690" height="136" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48ec31dbfc23705d54e5197acf2aa2d3fedb19be_2_690x136.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48ec31dbfc23705d54e5197acf2aa2d3fedb19be_2_1035x204.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48ec31dbfc23705d54e5197acf2aa2d3fedb19be_2_1380x272.png 2x" data-dominant-color="FCF6F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2194×434 33.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/4068c069dc61637d1be67c0d6c361c9c580fe5c3.png" data-download-href="/uploads/short-url/9bMZdBkghyo8iNbfq2WP9WJR5cv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4068c069dc61637d1be67c0d6c361c9c580fe5c3_2_502x500.png" alt="image" data-base62-sha1="9bMZdBkghyo8iNbfq2WP9WJR5cv" width="502" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4068c069dc61637d1be67c0d6c361c9c580fe5c3_2_502x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4068c069dc61637d1be67c0d6c361c9c580fe5c3_2_753x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4068c069dc61637d1be67c0d6c361c9c580fe5c3_2_1004x1000.png 2x" data-dominant-color="1D2A39"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1509×1502 276 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #16 by @lassoan (2019-12-09 05:26 UTC)

<p>I’ve tried this on latest preview release and worked well. Please first follow steps described in the <a href="https://github.com/lassoan/SlicerSegmentMesher#tutorial">tutorial</a> and let us know if you run into any problems. If everything works well with the tutorial data set then you try with your data set and let us know how it worked.</p>

---

## Post #17 by @lausiv (2019-12-09 05:46 UTC)

<p>I will do it from your instruction. and let us know how it worked. Thanks.</p>

---

## Post #18 by @lausiv (2019-12-09 07:50 UTC)

<p>I’ve tried this on latest preview release and worked well. Please first follow steps described in the <a href="https://github.com/lassoan/SlicerSegmentMesher#tutorial" rel="noopener nofollow ugc">tutorial</a> and let us know if you run into any problems. If everything works well with the tutorial data set then you try with your data set and let us know how it worked.<br>
==&gt; it is working now. but my goal is coloring different color and attaching the cube on the mesh surface like below pictures^^.<br>
anyway very interesting but hard :-). i will try coloring different color now.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a85ed8c8777d220e1f35464a69b4e26e16ba0d3.png" alt="image" data-base62-sha1="3MDlUOhGqKgWSII65UTx8SRRHjB" width="283" height="152"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f8261af1125092ef1047c68237ecc5db9a2f6f2.png" data-download-href="/uploads/short-url/93Pq9HNdMNkBlUBaAnO0NE5q0pA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f8261af1125092ef1047c68237ecc5db9a2f6f2.png" alt="image" data-base62-sha1="93Pq9HNdMNkBlUBaAnO0NE5q0pA" width="593" height="499" data-dominant-color="9F9D6E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">672×566 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1515afb557557c5d53123fdb61d35a70fdc0cf4.png" data-download-href="/uploads/short-url/w9fJvrvOiz6V1shAhGT1awlVyss.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1515afb557557c5d53123fdb61d35a70fdc0cf4_2_554x500.png" alt="image" data-base62-sha1="w9fJvrvOiz6V1shAhGT1awlVyss" width="554" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1515afb557557c5d53123fdb61d35a70fdc0cf4_2_554x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1515afb557557c5d53123fdb61d35a70fdc0cf4_2_831x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1515afb557557c5d53123fdb61d35a70fdc0cf4_2_1108x1000.png 2x" data-dominant-color="BBBDC3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2100×1895 410 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #19 by @lausiv (2019-12-09 07:52 UTC)

<p>Is it possible to display like below picture not second picture?<br>
keyword : surface mesh representation</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f8261af1125092ef1047c68237ecc5db9a2f6f2.png" data-download-href="/uploads/short-url/93Pq9HNdMNkBlUBaAnO0NE5q0pA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f8261af1125092ef1047c68237ecc5db9a2f6f2.png" alt="image" data-base62-sha1="93Pq9HNdMNkBlUBaAnO0NE5q0pA" width="593" height="499" data-dominant-color="9F9D6E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">672×566 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f6d8d4d087bb31439073c0a10c9c24026629efe.png" data-download-href="/uploads/short-url/ksOZwf59ZEaqQDx08qSxD9kaTxk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f6d8d4d087bb31439073c0a10c9c24026629efe.png" alt="image" data-base62-sha1="ksOZwf59ZEaqQDx08qSxD9kaTxk" width="577" height="500" data-dominant-color="7B7E9D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">603×522 29.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #20 by @lassoan (2019-12-09 18:05 UTC)

<aside class="quote no-group" data-username="lausiv" data-post="18" data-topic="9376">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lausiv/48/4984_2.png" class="avatar"> lausiv:</div>
<blockquote>
<p>attaching the cube on the mesh surface like below pictures</p>
</blockquote>
</aside>
<p>You can do that by using Segment Editor module (before FEM mesh generation). You can grow a shell on the skin using “Hollow” effect, then cut out rectangular shapes using “Scissors” effect.</p>
<aside class="quote no-group" data-username="lausiv" data-post="19" data-topic="9376">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lausiv/48/4984_2.png" class="avatar"> lausiv:</div>
<blockquote>
<p>Is it possible to display like below picture not second picture?<br>
keyword : surface mesh representation</p>
</blockquote>
</aside>
<p>You can hide the background mesh in Models module / Display / Scalars section, enable Threshold and set lower value to 1.</p>

---

## Post #21 by @lausiv (2019-12-10 05:25 UTC)

<p>You can do that by using Segment Editor module (before FEM mesh generation). You can grow a shell on the skin using “Hollow” effect, then cut out rectangular shapes using “Scissors” effect.<br>
==&gt; good but, in the aspect of user, like fiducial tools(below picture),<br>
based on user fiducial 3d point on the surface mesh,  it is good to draw for the attaching cube (below picture by the hand) which follows surface normal vector</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c90ccea4fe2a3592e4a61b5bf2abd1e96f07733f.png" data-download-href="/uploads/short-url/sGzptnYiOcN68mv8byYOJkbyjiT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c90ccea4fe2a3592e4a61b5bf2abd1e96f07733f.png" alt="image" data-base62-sha1="sGzptnYiOcN68mv8byYOJkbyjiT" width="689" height="453" data-dominant-color="FBFBFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1148×754 13.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec19015c9ed6b6e26b39bd4cd3eb969b761bd852.png" data-download-href="/uploads/short-url/xGCfUF4yrGm6siDcO9Yw7yIjMki.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec19015c9ed6b6e26b39bd4cd3eb969b761bd852.png" alt="image" data-base62-sha1="xGCfUF4yrGm6siDcO9Yw7yIjMki" width="689" height="500" data-dominant-color="758492"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">881×639 46.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can hide the background mesh in Models module / Display / Scalars section, enable Threshold and set lower value to 1.<br>
<strong>==&gt;I think it is homogenous mesh than tetzen. i am now tunning cleaver parameter^^</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00c3a1591663eb9a7e4289927af7fda6122e0253.png" data-download-href="/uploads/short-url/6L8qrpl2WmHH5vLV6gaeYpBe71.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00c3a1591663eb9a7e4289927af7fda6122e0253_2_690x379.png" alt="image" data-base62-sha1="6L8qrpl2WmHH5vLV6gaeYpBe71" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00c3a1591663eb9a7e4289927af7fda6122e0253_2_690x379.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00c3a1591663eb9a7e4289927af7fda6122e0253_2_1035x568.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00c3a1591663eb9a7e4289927af7fda6122e0253_2_1380x758.png 2x" data-dominant-color="B1B9C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1785×981 90.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #22 by @lassoan (2019-12-10 21:36 UTC)

<p>What is your end goal? Why do you need to define those rectangles?</p>

---

## Post #23 by @lausiv (2019-12-11 00:15 UTC)

<p>like below, attaching pads(cube structure) on the surface of the brain, and generating mesh for brain electric fields analysis</p>
<p>related paper :<br>
COMETS2: An advanced MATLAB toolbox for the numerical analysis of<br>
electric fields generated by transcranial direct current stimulation</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cba729ef71bdd4d1939b40d1d5c9420da137d44.png" alt="image" data-base62-sha1="468PyHKNFkv1WeCafc7910vgHuA" width="489" height="217"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d21e26b1df5ccb403f9ecfde103efaab85fb5c3e.jpeg" alt="image" data-base62-sha1="tYMRM36lCzkpYM1WvvgDG49lGG2" width="444" height="355"></p>

---

## Post #24 by @lassoan (2019-12-11 01:51 UTC)

<p>For this, the approach that I described (create a shell using “Hollow” effect and cut out rectangular parts using “Scissors” effect) should work very well. You can automate everything by writing Python scripts (see examples <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations">here</a>). For example, the user defines pad position using a markup fiducial and from your script you generate a box-shaped segment around that point and intersect that with the shell segment to generate the pad segment.</p>

---

## Post #25 by @lausiv (2019-12-11 15:49 UTC)

<p>For this, the approach that I described (create a shell using “Hollow” effect and cut out rectangular parts using “Scissors” effect) <strong>should work very well.</strong> You can automate everything by writing Python scripts (see examples <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations" rel="nofollow noopener">here </a>). For example, the user defines pad position using a markup fiducial and from your script you generate a box-shaped segment around that point and intersect that with the shell segment to generate the pad segment</p>
<p>==&gt; should work very well. ==&gt; GOOD. very interesting expression^^  ==&gt; I will do it and let the result shared in this page ==&gt; in korea, there’s<br>
Ultrafine dust issue from the China, my body condition is not good today. i am also image processing engineer. i think you lassoan are very enthusiast in 3d slicer image analysis&amp; visualization. thank you for your concern sincerly in my heart .^^</p>

---

## Post #26 by @lausiv (2019-12-12 12:40 UTC)

<p>Normally you assign scalar values to points or cells of your mesh when generate the mesh (e.g., you can have a scalar attribute to specify material or a physical quantity).<br>
<strong>==&gt; How am i set Custom Scalar Table(the Scalars-&gt;Color Table) or assign the scalar array when generating mesh(cleaver parameter?)</strong></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a34c94ee75a7784d217c00fb24b059777bef64a.png" alt="image" data-base62-sha1="8iUMPj80VnveuOXNGp0ZAIfQWBs" width="551" height="209"></p>

---

## Post #27 by @lassoan (2019-12-12 14:29 UTC)

<p>You can create/edit colormaps in Colors module. Built-in colormaps are read-only, so you need to make a copy if you want to customize one. A color table is created automatically from current segment names and colors if you export segmentation node to labelmap, so you may use that for coloring, too.</p>

---

## Post #29 by @lausiv (2019-12-12 15:35 UTC)

<p>is it possible custmized assigning color to the segmentation or cell by the color map. in other words, custmized color function(or linear fomular like y=3x+5) can be built in Color table?</p>

---

## Post #30 by @lassoan (2019-12-12 16:19 UTC)

<p>Yes, you can create/modify color nodes using Python or C++ in any way you want. See <a href="https://apidocs.slicer.org/v4.8/classvtkMRMLColorTableNode.html">API specification</a>.</p>

---

## Post #31 by @lausiv (2019-12-13 00:50 UTC)

<p>I will do it and let the result share in this pages.</p>
<p>My final goal is to add FEM Analysis after mesh generation.final equation will be more complex and burden to CPU, Intel Math Kernel Library(MKL Solver DSS) may be used for global matrix equation.</p>

---

## Post #32 by @lausiv (2019-12-16 09:52 UTC)

<p>Could u indicate contents name about this hollow effect to rectagle on the surface of segment pointed by fiducials? I can’t find similar script^^</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45b7ba9c8137d2ebd15dbf95c3082e9c78b93cec.png" data-download-href="/uploads/short-url/9WKA8KFz2fq3HhZJDzKYmn9eXy4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45b7ba9c8137d2ebd15dbf95c3082e9c78b93cec_2_639x500.png" alt="image" data-base62-sha1="9WKA8KFz2fq3HhZJDzKYmn9eXy4" width="639" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45b7ba9c8137d2ebd15dbf95c3082e9c78b93cec_2_639x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45b7ba9c8137d2ebd15dbf95c3082e9c78b93cec.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45b7ba9c8137d2ebd15dbf95c3082e9c78b93cec.png 2x" data-dominant-color="ECEEF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">927×725 74.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #33 by @lassoan (2019-12-16 22:09 UTC)

<p>See examples here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a></p>

---

## Post #34 by @lausiv (2019-12-17 05:20 UTC)

<p>It is hard to me to hollow and scissor exactly</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da80a8aaf8054bebd4b7ef7c7692c9af8fd3f875.png" data-download-href="/uploads/short-url/vaXJOixDtwzdXpV7JXtVIVX9Okd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da80a8aaf8054bebd4b7ef7c7692c9af8fd3f875_2_690x364.png" alt="image" data-base62-sha1="vaXJOixDtwzdXpV7JXtVIVX9Okd" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da80a8aaf8054bebd4b7ef7c7692c9af8fd3f875_2_690x364.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da80a8aaf8054bebd4b7ef7c7692c9af8fd3f875_2_1035x546.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da80a8aaf8054bebd4b7ef7c7692c9af8fd3f875_2_1380x728.png 2x" data-dominant-color="9DA1A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1864×986 209 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e9339c3345f3b25c037bad36cf6100ceaf3621f.png" data-download-href="/uploads/short-url/mCORVvpUOpZPHJ2I6oo0skSifeL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e9339c3345f3b25c037bad36cf6100ceaf3621f_2_690x364.png" alt="image" data-base62-sha1="mCORVvpUOpZPHJ2I6oo0skSifeL" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e9339c3345f3b25c037bad36cf6100ceaf3621f_2_690x364.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e9339c3345f3b25c037bad36cf6100ceaf3621f_2_1035x546.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e9339c3345f3b25c037bad36cf6100ceaf3621f_2_1380x728.png 2x" data-dominant-color="9EA1A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1864×986 213 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol>
<li>Markup - Fiducial Mark on Skin face</li>
<li>SegmentEditor - Hollow Effect and Scissors</li>
</ol>
<p>For this, the approach that I described (create a shell using “Hollow” effect and cut out rectangular parts using “Scissors” effect) should work very well. You can automate everything by writing Python scripts (see examples <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations" rel="noopener nofollow ugc">here </a>). For example, the user defines pad position using a markup fiducial and from your script you generate a box-shaped segment around that point and intersect that with the shell segment to generate the pad segment.</p>

---

## Post #35 by @lausiv (2019-12-17 05:23 UTC)

<p>Hi, Andras, all of the source in the segmentation section is python script, but not related this issue.</p>
<p>Could you help me to write script</p>
<p>Workflow</p>
<ol>
<li>Markup - Fiducial Marks on Skin face</li>
<li>SegmentEditor - Hollow Effect and Scissors to generate pad segm.</li>
</ol>
<p>For this, the approach that I described (create a shell using “Hollow” effect and cut out rectangular parts using “Scissors” effect) should work very well. You can automate everything by writing Python scripts (see examples <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations" rel="noopener nofollow ugc">here </a>). For example, the user defines pad position using a markup fiducial and from your script you generate a box-shaped segment around that point and intersect that with the shell segment to generate the pad segment.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e947b184a03e1efed00a4e0bc5e2c4fb46e8638.png" data-download-href="/uploads/short-url/bd9mpjZtlUOan7JHxaH3lUSNM3C.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e947b184a03e1efed00a4e0bc5e2c4fb46e8638_2_513x500.png" alt="image" data-base62-sha1="bd9mpjZtlUOan7JHxaH3lUSNM3C" width="513" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e947b184a03e1efed00a4e0bc5e2c4fb46e8638_2_513x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e947b184a03e1efed00a4e0bc5e2c4fb46e8638_2_769x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e947b184a03e1efed00a4e0bc5e2c4fb46e8638_2_1026x1000.png 2x" data-dominant-color="1D2D3A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1485×1446 328 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #36 by @lausiv (2019-12-17 05:29 UTC)

<aside class="quote no-group" data-username="lausiv" data-post="34" data-topic="9376">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lausiv/48/4984_2.png" class="avatar"> lausiv:</div>
<blockquote>
<p>i</p>
</blockquote>
</aside>
<p>i am now cutting rectangle by scissor effect drawn by left to right mouse clicked^^</p>
<p>ok. i will duplicate original segment and  apply scissor effect and generate mesh</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2cd76b78871a60e76a8ca3f0da242fefa761d1e.png" data-download-href="/uploads/short-url/pvLc0QqF0vZfQOklDxvl3ubo3j8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b2cd76b78871a60e76a8ca3f0da242fefa761d1e_2_690x347.png" alt="image" data-base62-sha1="pvLc0QqF0vZfQOklDxvl3ubo3j8" width="690" height="347" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b2cd76b78871a60e76a8ca3f0da242fefa761d1e_2_690x347.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b2cd76b78871a60e76a8ca3f0da242fefa761d1e_2_1035x520.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b2cd76b78871a60e76a8ca3f0da242fefa761d1e_2_1380x694.png 2x" data-dominant-color="9697A6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2200×1107 223 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #37 by @lausiv (2019-12-17 13:19 UTC)

<p>i succedd in attatching pad on the skin<br>
but when i generating mesh<br>
it was not applied.</p>
<p>segment_1 : pad on the skin<br>
segment_2 : surface of face generated by threshold 30 &amp; smooth 6mm<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/470517eab4b9a6e99a0bcb05e03d0aed274dfb8e.png" data-download-href="/uploads/short-url/a8gOpebDQn4JMXQlsqLjnqa41NI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/470517eab4b9a6e99a0bcb05e03d0aed274dfb8e.png" alt="image" data-base62-sha1="a8gOpebDQn4JMXQlsqLjnqa41NI" width="690" height="290" data-dominant-color="EAEFF3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">859×362 10.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0df413b98fd85a7bdd7a5527972f4198ea8901f2.jpeg" data-download-href="/uploads/short-url/1Zr8FktAjokC5cmm5B8Uxfa9bBo.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0df413b98fd85a7bdd7a5527972f4198ea8901f2_2_533x500.jpeg" alt="image" data-base62-sha1="1Zr8FktAjokC5cmm5B8Uxfa9bBo" width="533" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0df413b98fd85a7bdd7a5527972f4198ea8901f2_2_533x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0df413b98fd85a7bdd7a5527972f4198ea8901f2_2_799x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0df413b98fd85a7bdd7a5527972f4198ea8901f2.jpeg 2x" data-dominant-color="BDAE95"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">911×853 190 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b22044c3267e6ca777f7a381fd8251699b3d173d.jpeg" data-download-href="/uploads/short-url/ppM7K7LcHEccCxAxFdQLlEqIrZb.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b22044c3267e6ca777f7a381fd8251699b3d173d_2_533x500.jpeg" alt="image" data-base62-sha1="ppM7K7LcHEccCxAxFdQLlEqIrZb" width="533" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b22044c3267e6ca777f7a381fd8251699b3d173d_2_533x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b22044c3267e6ca777f7a381fd8251699b3d173d_2_799x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b22044c3267e6ca777f7a381fd8251699b3d173d.jpeg 2x" data-dominant-color="BEAE95"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">911×853 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #38 by @lassoan (2019-12-17 13:46 UTC)

<p>You need to increase the mesh resolution. With default parameters, a quick coarse mesh is generated.</p>

---

## Post #39 by @lausiv (2019-12-18 01:50 UTC)

<p>Thank you <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> i will refer cleaver parameter.</p>
<p>And i will make this python script adding fiducial mark basement^^ refering below segmentation script link</p>
<ol>
<li>fiducial mark -&gt; 2. hollow and sccisors -&gt; 3.generate mesh</li>
</ol>
<p>[<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a> ]</p>

---
