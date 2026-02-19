---
topic_id: 13588
title: "Meshing Self Intersecting Faces"
date: 2020-09-21
url: https://discourse.slicer.org/t/13588
---

# Meshing: Self-intersecting faces

**Topic ID**: 13588
**Date**: 2020-09-21
**URL**: https://discourse.slicer.org/t/meshing-self-intersecting-faces/13588

---

## Post #1 by @Fluvio_Lobo (2020-09-21 14:45 UTC)

<p>Hello,</p>
<p>These question may be a little outside the realm of Slicer, but it never hurts to ask!</p>
<p>Our team has been using Cleaver to create some amazing multi-material, conforming meshes. However, we have found mesh quality is sometimes dependent on the un-even-ness of the volume. In other words, we get better results when the input/base volume (DICOM volume is isotropic in size and voxel-spacing).</p>
<ul>
<li>Does anyone know why this happens?</li>
</ul>
<p>We have also been trying to use tetgen, but it only seems to work with volumes that are fully enclosed. Otherwise, it throws a self-intersecting error.</p>
<ul>
<li>Has anyone figure our a way around this issue?</li>
<li>Does anyone have any advice on methods for cleaning/correcting self-intersecting faces?</li>
<li>Is there a way in slicer to use the raw nrrd or a label-map as an input to tetgen?</li>
</ul>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2020-09-21 15:29 UTC)

<aside class="quote no-group" data-username="Fluvio_Lobo" data-post="1" data-topic="13588">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/fluvio_lobo/48/81262_2.png" class="avatar"> Fluvio_Lobo:</div>
<blockquote>
<p>Our team has been using Cleaver to create some amazing multi-material, conforming meshes.</p>
</blockquote>
</aside>
<p>Awesome! Could you share a few screenshots?</p>
<aside class="quote no-group" data-username="Fluvio_Lobo" data-post="1" data-topic="13588">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/fluvio_lobo/48/81262_2.png" class="avatar"> Fluvio_Lobo:</div>
<blockquote>
<p>we have found mesh quality is sometimes dependent on the un-even-ness of the volume. In other words, we get better results when the input/base volume (DICOM volume is isotropic in size and voxel-spacing).</p>
</blockquote>
</aside>
<p>This is expected. If spacing along any axis is significantly more than spacing along other axes then essentially your voxels are shaped like sticks, so you cannot represent arbitrary 3D shapes with them. If spacing difference along any of the image axis is more than a few ten percent then I use “Crop volume” module to resample the input volume to have isotropic spacing (and crop it to the region of interest to keep the volume size small).</p>
<aside class="quote no-group" data-username="Fluvio_Lobo" data-post="1" data-topic="13588">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/fluvio_lobo/48/81262_2.png" class="avatar"> Fluvio_Lobo:</div>
<blockquote>
<p>We have also been trying to use tetgen, but it only seems to work with volumes that are fully enclosed. Otherwise, it throws a self-intersecting error.</p>
</blockquote>
</aside>
<p>Tetgen is mainly added for reference, because 5-10 years ago it was a popular mesher and we wanted to make it easy to compare. It has restrictive license (you need to buy a license for commercial applications) and not robust (can crash quite easily for complex meshes that come out of medical image segmentation), so I would not recommend using it.</p>
<p>There are many other meshers, some of the popular ones include <a href="https://github.com/NGSolve/netgen">netgen</a>, <a href="https://gitlab.onelab.info/gmsh/gmsh">gmsh</a>, <a href="https://github.com/Yixin-Hu/TetWild">TetWild</a> (see <a href="http://www.robertschneiders.de/meshgeneration/software.html">this page</a> for lots of more - not very up-to-date but gives an idea how many meshers are out there.). As far as I know, <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> plans to add some more meshers to SegmentMesher.</p>

---

## Post #3 by @Fluvio_Lobo (2020-09-21 15:37 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I will get you some good screenshots by the end of the day for sure!</p>
<p>Regarding Cleaver, I have a few concerns;</p>
<ol>
<li>
<p>The Cleaver team does not seem too active and the doc. seems to be very limited</p>
</li>
<li>
<p>We have issues with ‘holes’ in meshes with &gt;3 materials, which seems kind-of lame</p>
</li>
<li>
<p>It is not clear to me the dynamic between the scale and multiplier parameters. Could you provide some insight on the difference and use?</p>
</li>
</ol>

---

## Post #4 by @lassoan (2020-09-21 16:05 UTC)

<aside class="quote no-group" data-username="Fluvio_Lobo" data-post="3" data-topic="13588">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/fluvio_lobo/48/81262_2.png" class="avatar"> Fluvio_Lobo:</div>
<blockquote>
<p>Cleaver team does not seem too active</p>
</blockquote>
</aside>
<p>The SCI group is still very much active but it is true that not much development is going on for this particular project recently. My understanding is that they are still committed to maintaining their software and Kitware helps them in this, too. Latest release is 3 months old, so it is not too bad.</p>
<aside class="quote no-group" data-username="Fluvio_Lobo" data-post="3" data-topic="13588">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/fluvio_lobo/48/81262_2.png" class="avatar"> Fluvio_Lobo:</div>
<blockquote>
<p>We have issues with ‘holes’ in meshes with &gt;3 materials, which seems kind-of lame</p>
</blockquote>
</aside>
<p>Can you show examples? You should be able to resolve this, but you may need to increase the resolution of the mesh near boundaries. Cleaver is intended for biomedical applications, so it may smoothen sharp edges, and where multiple materials meet, sharp edges are inevitable. Also check out how the input segmentation looked like. There might have been 1-2 empty voxels at the junction point.</p>
<aside class="quote no-group" data-username="Fluvio_Lobo" data-post="3" data-topic="13588">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/fluvio_lobo/48/81262_2.png" class="avatar"> Fluvio_Lobo:</div>
<blockquote>
<p>It is not clear to me the dynamic between the scale and multiplier parameters. Could you provide some insight on the difference and use?</p>
</blockquote>
</aside>
<p>See this page: <a href="https://github.com/lassoan/SlicerSegmentMesher#mesh-generation-parameters" class="inline-onebox">GitHub - lassoan/SlicerSegmentMesher: Create volumetric mesh from segmentation using Cleaver2 or TetGen</a></p>
<p>The main difference is that <code>scale</code> essentially specifies how densely the input is sampled (if you take few samples from the mesh then execution will be faster but you will lose lots of details), while <code>multiplier</code> controls element size (if you have large elements then you will have a simpler mesh but cannot represent small details).</p>

---

## Post #5 by @Fluvio_Lobo (2020-09-21 16:25 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="13588">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The main difference is that <code>scale</code> essentially specifies how densely the input is sampled (if you take few samples from the mesh then execution will be faster but you will lose lots of details), while <code>multiplier</code> controls element size (if you have large elements then you will have a simpler mesh but cannot represent small details).</p>
</blockquote>
</aside>
<p>Lets say we have a boundary layer we are measuring at <strong>2 mm</strong>, have does the value of multiplier and, thus, element size match to the units of the volume? Does a value of 0.2 mean I will have about 10 elements in that boundary?</p>

---

## Post #6 by @lassoan (2020-09-21 16:27 UTC)

<p>I don’t remember these details (segmentation spacing may have an effect, too). The best is to experiment with this on simple examples and if you figure out something then share what you have found (we will add it to SegmentMesher documentation).</p>

---

## Post #7 by @Fluvio_Lobo (2020-09-21 16:30 UTC)

<p>Will do, here is what that looks like <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61b46412461535c979f7839498e6f94cbf68b949.png" data-download-href="/uploads/short-url/dWkNCAOie6cIog02Bbf8Qf4xsal.png?dl=1" title="thin_layer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61b46412461535c979f7839498e6f94cbf68b949.png" alt="thin_layer" data-base62-sha1="dWkNCAOie6cIog02Bbf8Qf4xsal" width="690" height="422" data-dominant-color="737A38"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">thin_layer</span><span class="informations">842×515 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>We usually just thicken the layer, but I am feeling like reducing the multiplier value to see if that helps!</p>

---

## Post #8 by @Fluvio_Lobo (2020-09-22 03:49 UTC)

<p>Here is one of the highest quality meshes we generated today;<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/849722dd0b78416083e36825831e4e0609a92a55.png" data-download-href="/uploads/short-url/iUWPHrGfanrbA9uDtkOZlwE90i1.png?dl=1" title="mesh" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/849722dd0b78416083e36825831e4e0609a92a55_2_690x373.png" alt="mesh" data-base62-sha1="iUWPHrGfanrbA9uDtkOZlwE90i1" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/849722dd0b78416083e36825831e4e0609a92a55_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/849722dd0b78416083e36825831e4e0609a92a55_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/849722dd0b78416083e36825831e4e0609a92a55_2_1380x746.png 2x" data-dominant-color="ADAFBE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mesh</span><span class="informations">1920×1040 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The mesh is about 13M tets, which I am not a fan of, but I need a solid starting point! There are 6 materials in the model. This is a breast cancer model, so the materials represent: chest cavity, soft tissue, fibro-glandular tissue, and masses/tumors. We get holes in areas/regions where 3 models intersect;</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1192f46068412bf3ceabcfde596863e2cc0855a.png" data-download-href="/uploads/short-url/pgGt9iaT1yctVYK7RBLWUIFEcdQ.png?dl=1" title="mesh_holes" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1192f46068412bf3ceabcfde596863e2cc0855a_2_690x373.png" alt="mesh_holes" data-base62-sha1="pgGt9iaT1yctVYK7RBLWUIFEcdQ" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1192f46068412bf3ceabcfde596863e2cc0855a_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1192f46068412bf3ceabcfde596863e2cc0855a_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1192f46068412bf3ceabcfde596863e2cc0855a_2_1380x746.png 2x" data-dominant-color="9BA09A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mesh_holes</span><span class="informations">1920×1040 179 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Now here is the interesting part. Although I started with the <strong>adaptive</strong> parameters (scale, multiplier, etc.), these results were obtained using the <strong>alpha</strong> flags the developers presented <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4142801/" rel="noopener nofollow ugc">here</a></p>
<p>I will continue to explore adaptive meshing parameters to see if better results are obtained.</p>
<p>Any suggestions or information would be greatly appreciated</p>

---

## Post #9 by @lassoan (2020-09-22 05:00 UTC)

<p>I guess you want to model breast deformation between imaging (prone) and surgery (supine) patient positions. These deformations are huge and with 13M elements it would be an extremely hard problem, not just because there are many elements (so computation time would be really long), but it would be very unstable (many of those millions of tiny elements would collapse and self-intersect if you want to get near realistic deformations).</p>
<p>You will need much larger elements, and some adaptive element sizing to have similar shapes as in the input segmentation.</p>
<p>Since you don’t have accurate parient-specific material properties anyway, you probably don’t need to worry about minor imperfections, such as slightly smoothed out boundaries or tiny holes at junction points.</p>

---

## Post #10 by @Fluvio_Lobo (2020-09-22 12:23 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="13588">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You will need much larger elements, and some adaptive element sizing to have similar shapes as in the input segmentation.</p>
</blockquote>
</aside>
<p>Agree 100! The problem is that as I start smoothing, holes begin to appear on the <strong>skin</strong>;<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d3294fbeb7f5bb0c3f759a7c52a5d45a2be903c.png" alt="holes_on_skin" data-base62-sha1="1SKzRH4Q7xYYix1XDIWeGBrmJzK" width="496" height="344"></p>
<p>A balance needs to exist between the adaptive parameters, but I think it may come down to a <strong>case-to-case</strong> basis.</p>
<p>The adaptive parameters I used for the first adaptive mesh were;<br>
<code>--scale 1.00 --multiplier 2.00 --grading 5</code></p>
<p>Starting with an aggressive <strong>sigma blend</strong>, the the holes show;<br>
<code>--scale 1.00 --multiplier 2.00 --grading 5 --blend_sigma 2.50</code></p>

---

## Post #11 by @lassoan (2020-09-22 12:58 UTC)

<p>I don’t think the meshing is that sensitive to input parameters that you would need tuning for each case. If you determine parameters for a specific image spacing then it should work well for all cases.</p>
<p>Blend-sigma controls strength of Gaussian smoothing applied to remove staircase artifacts. See documentation:</p>
<blockquote>
<p>Sigma of Gaussian smoothing filter that is applied to the input labelmap to remove step artifacts (anti-aliasing). Higher values may shrink structures and remove small details.</p>
</blockquote>
<p>You should use the smallest possible value that removes staircase artifacts. If you use higher than necessary values then structures will shrink and holes will appear between them. If you find that holes appear and staircase artifacts are still visible then resample the input volume to have smaller spacing (using Crop volume module) and redo the segmentation.</p>

---

## Post #12 by @Fluvio_Lobo (2020-09-22 13:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="13588">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I don’t think the meshing is that sensitive to input parameters that you would need tuning for each case. <strong>If you determine parameters for a specific image spacing</strong> then it should work well for all cases.</p>
</blockquote>
</aside>
<p>I am going to keep this in my notes. Most of out data should end-up with about the same spacing.</p>
<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="13588">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You should use the smallest possible value that removes staircase artifacts. If you use higher than necessary values then structures will shrink and holes will appear between them. If you find that holes appear and staircase artifacts are still visible then resample the input volume to have smaller spacing (using Crop volume module) and redo the segmentation.</p>
</blockquote>
</aside>
<p>We actually do a considerable amount of smoothing, so perhaps I should keep the blend sigma low;<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc32139b3fac8a0efc43b22f310b8a30e54d009f.png" data-download-href="/uploads/short-url/vpWkAz4jErEq1FsTmwZJ8T55Zwz.png?dl=1" title="smooth" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc32139b3fac8a0efc43b22f310b8a30e54d009f_2_640x499.png" alt="smooth" data-base62-sha1="vpWkAz4jErEq1FsTmwZJ8T55Zwz" width="640" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc32139b3fac8a0efc43b22f310b8a30e54d009f_2_640x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc32139b3fac8a0efc43b22f310b8a30e54d009f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc32139b3fac8a0efc43b22f310b8a30e54d009f.png 2x" data-dominant-color="7D96B9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">smooth</span><span class="informations">779×608 93.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I will keep trying parameters and I will post results!</p>

---

## Post #13 by @lassoan (2020-09-22 13:42 UTC)

<aside class="quote no-group" data-username="Fluvio_Lobo" data-post="12" data-topic="13588">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/fluvio_lobo/48/81262_2.png" class="avatar"> Fluvio_Lobo:</div>
<blockquote>
<p>I am going to keep this in my notes. Most of out data should end-up with about the same spacing.</p>
</blockquote>
</aside>
<p>Note that you can always crop&amp;resample your input to the desired resolution and size as part of your image import process. Therefore, you can use the same meshing protocol for all images, even if their native resolution were different.</p>

---

## Post #15 by @Fluvio_Lobo (2020-10-02 01:25 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Apologies for the double-post. I wanted to add more info but I was unable to edit the response itself. Here is a more detailed explanation of the current challenge.</p>
<p>First, here is perhaps the most extreme model we have been able to simulate.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f19781f86ca6af4816d4ab0be4ddd43e4507882a.png" data-download-href="/uploads/short-url/ytdFNk60VR4nIsCiY0DWSXXUHii.png?dl=1" title="state0" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f19781f86ca6af4816d4ab0be4ddd43e4507882a_2_357x375.png" alt="state0" data-base62-sha1="ytdFNk60VR4nIsCiY0DWSXXUHii" width="357" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f19781f86ca6af4816d4ab0be4ddd43e4507882a_2_357x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f19781f86ca6af4816d4ab0be4ddd43e4507882a_2_535x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f19781f86ca6af4816d4ab0be4ddd43e4507882a.png 2x" data-dominant-color="C5CBD4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">state0</span><span class="informations">675×707 14.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec844c0fc16f64ccf55503816aa999ce2768d9ba.png" data-download-href="/uploads/short-url/xKk7X8K804JjFBlZ0A9cnUPUc9I.png?dl=1" title="state75" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ec844c0fc16f64ccf55503816aa999ce2768d9ba_2_517x340.png" alt="state75" data-base62-sha1="xKk7X8K804JjFBlZ0A9cnUPUc9I" width="517" height="340" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ec844c0fc16f64ccf55503816aa999ce2768d9ba_2_517x340.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ec844c0fc16f64ccf55503816aa999ce2768d9ba_2_775x510.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec844c0fc16f64ccf55503816aa999ce2768d9ba.png 2x" data-dominant-color="D7DAE1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">state75</span><span class="informations">1016×669 18.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
If I did not mention this earlier, we are using FEBio for the FEA and PostView for visualization.</p>
<p>The initial mesh was generated using the <code>Segment Mesher</code> module and <code>Cleaver2</code>. The most effective parameters were <code>--scale 1.00 --multiplier 2.00 --grading 5.00 --blend_sigma 1.75</code>. I would also note that we are now smoothing the compartments heavily prior to meshing, so our latest <code>--blend_sigma</code> parameters are small. The resultant mesh features about <strong>1.1M tets</strong> and a <strong>minimum dihedral angle = 4.80</strong>, which is now the parameter we are tracking the most.</p>
<p>As is, using FEBio, we probably get about 20% of the simulation done before one or multiple tets invert (i.e. negative jacobian).</p>
<p>To solve this issue, we have approached the problem in two ways:</p>
<ol>
<li>Remesh (using tetgen) the failed model and continue simulating from the failed time-step</li>
<li>Remesh (using tetgen) the original mesh and restart simulation</li>
</ol>
<p>Thus far, we have had success in both approaches. The model depicted above still fails due to penetrating tets, which we will address differently.</p>
<p>Our questions are;</p>
<ol>
<li>
<strong>Can we export an .ele and .node (or other mesh extensions) from segment mesher?</strong> <em>–This would streamline the re-meshing process</em>
</li>
<li><strong>Are there other means of remeshing using <code>Segment Mesher</code> and/or <code>Cleaver</code>?</strong></li>
</ol>

---
