---
topic_id: 18923
title: "Have The Open Surface Editing Extension Or Function Is Publi"
date: 2021-07-26
url: https://discourse.slicer.org/t/18923
---

# Have the "open surface editing" extension or function is published?

**Topic ID**: 18923
**Date**: 2021-07-26
**URL**: https://discourse.slicer.org/t/have-the-open-surface-editing-extension-or-function-is-published/18923

---

## Post #1 by @StephenLeePeng (2021-07-26 02:44 UTC)

<p>Operating system: Ubuntu 18.04<br>
Slicer version: self-build, 4.13.0-2021-07-07<br>
Expected behavior:<br>
As the question topic: " <a href="https://discourse.slicer.org/t/how-to-create-an-open-surface-constrained-by-markup-points-and-split-the-current-segment-by-this-surface/13254">How to create an open surface constrained by markup points，and split the current segment by this surface?</a>" mentioned, <a class="mention" href="/u/lassoan">@lassoan</a> said, “we have implemented 3D open source editing that is very similar to the animation above …”.<br>
Now exist a requiremet, I have to create a open surface, and edit the created open surface by some exist or added new control point, then use this surface to segment the 3d model in the 3d Viewer.<br>
So I want to know, “3d open surface edit” existed in the 3d Slicer module or extension?  If exist, how I can find it to load to use?</p>
<p>Any answer is appreciated from community.</p>

---

## Post #2 by @lassoan (2021-07-26 02:58 UTC)

<p>A couple of relevant tools:</p>
<ul>
<li>
<a href="https://discourse.slicer.org/t/new-module-baffle-planner-for-designing-surface-patches/16799">Baffle Planner</a>: define open surface using boundary curve and surface points</li>
<li>Dynamic modeler module (in recent Slicer Preview Releases): cut out arbitrary piece from a mesh using cutting plane(s) or a rectangular ROI</li>
<li>Resect objects using warped plane (in <a href="https://github.com/ALive-research/Slicer-LiverAnalysis">LiverAnalysis extension</a>): Unfortunately, this extension has not been submitted to the extension manager yet and therefore you need to build it. <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> is there a reason why this extension has not been submitted to the extension manager?</li>
</ul>

---

## Post #3 by @StephenLeePeng (2021-07-26 03:07 UTC)

<p>Thank you for your reply.<br>
I will try these tools recent days.</p>

---

## Post #4 by @RafaelPalomar (2021-07-26 07:20 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>. The extension is not finished yet. We have all the core components but need to connect them all and work on the Qt gui. We will try to push this during August.</p>

---

## Post #5 by @StephenLeePeng (2021-07-27 07:43 UTC)

<p>I have installed “Baffle Planner” extension, and have defined an open surface model.<br>
Then I want to use this surface to cut a loaded 3d stl model, How I will to do in the next?</p>
<p>You say in the “Dynamic modeler module”. Now I have download Preview Releases: Slice-4.13.0-2021-07-26-linux-amd64 version, and switch to “Dynamic Modeler” module, and there exist “Plane cut”, “Curve cut”, and so on.</p>
<p>When I choose “Plane cut” option, and load the original stl model to be cutted in the Model node, I can’t select the surface model I have created in the Baffle Planner model in the ROI node, so I can’t cut the stl model by the surface model.<br>
How I could solve this problem?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc4c4ad54c448c1458e006bde571dd4818114943.png" data-download-href="/uploads/short-url/qRLdDBpX2gqCvBs1DBsNa4MV323.png?dl=1" title="dynamic-modeler" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc4c4ad54c448c1458e006bde571dd4818114943_2_690x369.png" alt="dynamic-modeler" data-base62-sha1="qRLdDBpX2gqCvBs1DBsNa4MV323" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc4c4ad54c448c1458e006bde571dd4818114943_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc4c4ad54c448c1458e006bde571dd4818114943_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc4c4ad54c448c1458e006bde571dd4818114943_2_1380x738.png 2x" data-dominant-color="B0B2C3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dynamic-modeler</span><span class="informations">1849×989 260 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2021-07-27 22:56 UTC)

<p>The options that I described above are exclusive - you either use one approach or another. If you generate a surface using Baffle Planner then you need to use Combine Models module to cut with it. I don’t think Combine models work with open surfaces, so you probably need to make it a thick shell and subtract it from the vessel tree, then extract the largest component from the resulting model using the Surface Toolbox module.</p>

---

## Post #7 by @StephenLeePeng (2021-08-03 08:03 UTC)

<p>Thank you for your reply, it sounds very complex.<br>
Now I have found a open surface cut project, I will tried this project and transplant the open surface cut into the 3d Slicer.</p>

---

## Post #8 by @lassoan (2021-08-03 12:44 UTC)

<p>You can also cut surfaces with each other using Combine Models module (in Sandbox extension).</p>

---

## Post #9 by @StephenLeePeng (2021-08-04 03:05 UTC)

<p>Thank you for reply.<br>
I finally realize the open surface cut func by the 3d Slicer module althrough the procedure is a little complex. The procedure are as follows:</p>
<ol>
<li>Load a stl model named ‘bronchus’ into the 3d view.</li>
<li>Switch to “Markups” module, select Create ClosedCurve Markups button, then I draw a closed curve named “CC”,  generated by some control point around the upper part of bronchus model.</li>
<li>Swith to “Baffle Planner” module (in the SlicerHeart extension), select “CC” as Input curve, select “Create new model as” in the Baffle model, then default Baffle model named “Baffle” generat.</li>
<li>Select “Surface points”, click fiducial button, then place some control point in the closed curve, and you can adjust control point position to adjust surface.</li>
<li>Switch to “Combine Models” module (in the Sandbox extension), select “bronchus” as Input model A, select “Baffle” as Input model B.</li>
<li>Select “Intersection (A&amp;B)” operation, select “Create new model node” as Output model. Then click “Apply” button, and the output model, named “Model” will appear.</li>
<li>Swith to “Data” module, hide the exist model except new “Model”, set the other color different from the bronchus model.</li>
<li>Switch to “Combine Models” module, select “bronchus” as Input model A, select “Model” as Input model B, select “Difference (A-B)” as operation, then click Apply button. The new Model_1 will generate. Set other color for Model_1, and you will see the two models cut by open surface model.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6cae605e16581c25a281f8930e5e4eabb08460b.jpeg" data-download-href="/uploads/short-url/uE8SYJ7ToJPzFC2D6XGr7qNSgTp.jpeg?dl=1" title="001" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6cae605e16581c25a281f8930e5e4eabb08460b_2_690x467.jpeg" alt="001" data-base62-sha1="uE8SYJ7ToJPzFC2D6XGr7qNSgTp" width="690" height="467" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6cae605e16581c25a281f8930e5e4eabb08460b_2_690x467.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6cae605e16581c25a281f8930e5e4eabb08460b_2_1035x700.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6cae605e16581c25a281f8930e5e4eabb08460b.jpeg 2x" data-dominant-color="9C9AB0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">001</span><span class="informations">1376×932 95.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76f3b9938ca6c46349866cd4a632469263854609.png" alt="Baffle Planner module" data-base62-sha1="gYiwdNGOJMnnwOdDyppQkmpvsjD" width="477" height="495"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79e2b94c41b89a09bfcda4ebe7c360f183cb8d9c.png" data-download-href="/uploads/short-url/hofwHApiCI3s0z74MMBw9WX1PBO.png?dl=1" title="Combine Models module" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79e2b94c41b89a09bfcda4ebe7c360f183cb8d9c_2_426x500.png" alt="Combine Models module" data-base62-sha1="hofwHApiCI3s0z74MMBw9WX1PBO" width="426" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79e2b94c41b89a09bfcda4ebe7c360f183cb8d9c_2_426x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79e2b94c41b89a09bfcda4ebe7c360f183cb8d9c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79e2b94c41b89a09bfcda4ebe7c360f183cb8d9c.png 2x" data-dominant-color="E9E9E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Combine Models module</span><span class="informations">474×556 42.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63b407bf8a927647f4008732528cbfb765eb96bc.png" data-download-href="/uploads/short-url/ee0YVgXElyxSmcjwiEjmXGP2mEk.png?dl=1" title="result1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63b407bf8a927647f4008732528cbfb765eb96bc_2_690x358.png" alt="result1" data-base62-sha1="ee0YVgXElyxSmcjwiEjmXGP2mEk" width="690" height="358" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63b407bf8a927647f4008732528cbfb765eb96bc_2_690x358.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63b407bf8a927647f4008732528cbfb765eb96bc_2_1035x537.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63b407bf8a927647f4008732528cbfb765eb96bc_2_1380x716.png 2x" data-dominant-color="9CA8C0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">result1</span><span class="informations">1915×996 281 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
