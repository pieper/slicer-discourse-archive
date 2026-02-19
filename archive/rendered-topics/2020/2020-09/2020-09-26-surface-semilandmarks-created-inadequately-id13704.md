---
topic_id: 13704
title: "Surface Semilandmarks Created Inadequately"
date: 2020-09-26
url: https://discourse.slicer.org/t/13704
---

# Surface semilandmarks created inadequately

**Topic ID**: 13704
**Date**: 2020-09-26
**URL**: https://discourse.slicer.org/t/surface-semilandmarks-created-inadequately/13704

---

## Post #1 by @lv_xiao (2020-09-26 01:21 UTC)

<p>I would like to use SlicerMorph to place surface semilandmarks. I tried two ways, either digitizing the fixed landmarks inside SlicerMorph or in external software. Both approaches failed.</p>
<p>For method 1, I used the “Creat fiducial markup” option in the Markup module to place fixed landmarks. I then switched to the SemiLandmark module for patching. A screenshot below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2df3e48c38c1e72540e8915b7e12c2922ffe14d9.jpeg" data-download-href="/uploads/short-url/6yw1uhTgse2pt16vBjtHegsIlpn.jpeg?dl=1" title="Snipaste_2020-09-26_08-37-18" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2df3e48c38c1e72540e8915b7e12c2922ffe14d9_2_690x375.jpeg" alt="Snipaste_2020-09-26_08-37-18" data-base62-sha1="6yw1uhTgse2pt16vBjtHegsIlpn" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2df3e48c38c1e72540e8915b7e12c2922ffe14d9_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2df3e48c38c1e72540e8915b7e12c2922ffe14d9_2_1035x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2df3e48c38c1e72540e8915b7e12c2922ffe14d9_2_1380x750.jpeg 2x" data-dominant-color="CFCF9E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snipaste_2020-09-26_08-37-18</span><span class="informations">3058×1663 644 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Obviously, the patching result falls short of expectation. I guess this is due to the inappropriate selection of Landmark set, where instead of selecting a set of landmarks, I only selected landmark 1. I followed the <a href="https://www.youtube.com/watch?v=SArudRq-M4A" rel="noopener nofollow ugc">Youtube tutorial</a> but this tutorial imported landmarks digitized elsewhere rather than producing fixed landmarks inside SlicerMorph. How can I patch semilandmarks based on fixed landmarkd digitized in SlicerMorph?</p>
<p>Method 2: I followed the video tutorial above and digitized landmarks 1 to 4 in Avizo. I then tried to create a fcsv file for import into SlicerMorph. Strangely, when I load the fcsv file into SlicerMorph, the four landmarks do not appear where they are expected to lie. Actually, they are hidden inside the bony structures. However, I checked in R and I am sure that there is no issue with the coordinates.<br>
I am therefore wondering if I am not making the correct format for the fcsv file. I did not file what is the format that landmarkd digitized externally should be imported. If it is fcsv, what should the format be like.</p>
<p>BTW, I have got a further question on how to obtain the pairing information for semilandmarks created. Using the example form the youtube video:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0ff14be77c0f0df1d73a65f5b0653e4d063607bc.jpeg" data-download-href="/uploads/short-url/2h28wgolNXxqqNMlj9mM1lKM4zO.jpeg?dl=1" title="Snipaste_2020-09-26_08-55-53" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ff14be77c0f0df1d73a65f5b0653e4d063607bc_2_512x500.jpeg" alt="Snipaste_2020-09-26_08-55-53" data-base62-sha1="2h28wgolNXxqqNMlj9mM1lKM4zO" width="512" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ff14be77c0f0df1d73a65f5b0653e4d063607bc_2_512x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ff14be77c0f0df1d73a65f5b0653e4d063607bc_2_768x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ff14be77c0f0df1d73a65f5b0653e4d063607bc_2_1024x1000.jpeg 2x" data-dominant-color="615F77"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snipaste_2020-09-26_08-55-53</span><span class="informations">1970×1921 324 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Landmark 36 and 37 are paired landmarks on right and left side. Similarly, semilandmark A and B are paired. While it is straightforward to keep a record that lm 36 and 37 are bilaterally corresponding landmarks, I wonder how could we extract such pairing information for semilandmarks?</p>
<p>Such pairing information is needed for both the geomorph and Morpho R package to implement GPA for specimens with object symmetry.</p>
<p>Sorry for my long question and thank you.</p>

---

## Post #2 by @muratmaga (2020-09-26 03:34 UTC)

<p><a class="mention" href="/u/lv_xiao">@lv_xiao</a> couple things: SlicerMorph is under constant development, so please use a recent version of Slicer and then install SlicerMorph extension. That will give you the latest changes. You can find the official install instructions here: <a href="https://github.com/SlicerMorph/SlicerMorph#installation" rel="noopener nofollow ugc">https://github.com/SlicerMorph/SlicerMorph#installation</a></p>
<p>Also we renamed the modules to reflect their functions better. SemiLandmark module is now called CreateSemiLMPatches. This module will create triangular patches based on the three fixed landmarks you specified. The nasal area has a lot of curvature changes so you will need to play with the advanced features (maximum projection and smoothing of the projection vectors) to get a triangular patch of points (right now you are only seeing a line, I suspect all other rows ended up in side the model). It also takes a few iterations to find the ideal triangulation pattern that works for your needs.</p>
<p>There is currently no way to make distinguish left and right pairs of semi-landmarks created this way.</p>
<p>You may also want to try the PseudoLMGenerator, which will take a mesh and give you almost uniformly sampled points on the surface. See the instructions in here: <a href="https://github.com/SlicerMorph/S_2020/blob/master/Day_3/Spherical_sampling/Spherical_Sampling.md#template-estimated-from-the-specimen-geometry" rel="noopener nofollow ugc">https://github.com/SlicerMorph/S_2020/blob/master/Day_3/Spherical_sampling/Spherical_Sampling.md#template-estimated-from-the-specimen-geometry</a>. One benefit of PseudoLMGenerator is, soon it will support defining a plane of symmetry and reflecting the points to the other side to create symmetrized point cloud. For that, you can get the pairing information.</p>
<p>If all your specimen has fixed landmarks, you can use ProjectSemiLMPatches to transfer this template to new samples. If you do not have fixed landmarks, alternatively you can use the ALPACA module to transfer to new models. Here is the tutorial for alpaca <a href="https://github.com/SlicerMorph/S_2020/blob/master/Lab_ALPACA/README.md" rel="noopener nofollow ugc">https://github.com/SlicerMorph/S_2020/blob/master/Lab_ALPACA/README.md</a></p>
<p>As for why your points from Avizo doesn’t show up correctly in Slicer, I suspect that’s a coordinate issue. Slicer assumes models to be saved in LPS coordinate system. If this is not what Avizo does, that might explain the issue. You can specify the coordinate system for the model to be RAS and see if that helps. If that still doesn’t solve the issue, please send me a PLY model saved out of Avizo and coordinates of four landmarks as shown in avizo (a text file would suffice, do not try to convert them to fcsv), and I can take a look.</p>
<p>In general, if you do both your digitization and analysis in SlicerMorph, you won’t have to worry about this coordinate change issue.</p>

---

## Post #3 by @muratmaga (2020-09-26 03:53 UTC)

<p>Actually looking more closely to your screenshot, now I see what might have gone wrong. You have created each fiducial as a separate node. Instead you want to have single fiducial node that stores all those four points. <a class="mention" href="/u/smrolfe">@smrolfe</a> can we limit the numbers to be legitimate entries?</p>
<p>This is one of the Slicer gotchas. There are two icons that look almost identical but have different functions. The top red box is the fiducial placement only. It will keep adding new fiducials to the currently active fiducial node. Whereas the second button (same icon with the little + sign) will simultaneously both create a new fiducial node and place the first point in. The second time you click this icon, it will create a second node and assign the newly created point this node. What you really want to use is the icon in the top row.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/7860b9b6c4a868495e73eb892db900d328c3cf09.png" data-download-href="/uploads/short-url/haUwQpDQzLi9rl8PPtegtRT7pbz.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/7860b9b6c4a868495e73eb892db900d328c3cf09_2_690x388.png" alt="image" data-base62-sha1="haUwQpDQzLi9rl8PPtegtRT7pbz" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/7860b9b6c4a868495e73eb892db900d328c3cf09_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/7860b9b6c4a868495e73eb892db900d328c3cf09_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/7860b9b6c4a868495e73eb892db900d328c3cf09.png 2x" data-dominant-color="C3C4DB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1280×720 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can read more about the markup module details here: <a href="https://github.com/SlicerMorph/S_2020/blob/master/Day_2/Markups/Markups.md#markup-management-and-important-considerations-for-data-collections" class="inline-onebox">S_2020/Day_2/Markups/Markups.md at master · SlicerMorph/S_2020 · GitHub</a></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> we really have to do something about this as this is confusing to almost everyone starting to use Slicer first time to do landmark. May be we can try to come up with different icons for these two functions?</p>

---

## Post #4 by @lassoan (2020-09-26 04:04 UTC)

<p>I agree that changing the icons could help. We should remove the arrow from the create new node icons and add multiple points for the markup fiducial icon. Please send a pull request with the proposed change.</p>
<p>We should also put a place point button prominently in the Markups module GUI. Maybe in the Control points section?</p>

---

## Post #5 by @smrolfe (2020-09-26 22:21 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="13704">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Actually looking more closely to your screenshot, now I see what might have gone wrong. You have created each fiducial as a separate node. Instead you want to have single fiducial node that stores all those four points. <a class="mention" href="/u/smrolfe">@smrolfe</a> can we limit the numbers to be legitimate entries?</p>
</blockquote>
</aside>
<p>Correct, all the landmarks should be in a single set, specified in the field ‘Landmark set’ I will add some error checking to make sure this is more obvious.</p>

---

## Post #6 by @smrolfe (2020-09-26 22:24 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="13704">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I agree that changing the icons could help. We should remove the arrow from the create new node icons and add multiple points for the markup fiducial icon. Please send a pull request with the proposed change.</p>
</blockquote>
</aside>
<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>, I will follow up with this.</p>

---

## Post #7 by @lv_xiao (2020-09-27 10:37 UTC)

<p>Thank you Prof. Murat and everyone else. I am expecting the incorporation of plane of symmetry into PseudoLMGenerator. That will allow for GMM analysis of degree of symmetry of specimens.</p>
<p>Following your recommendations, I also learned ALPACA. In your preprint paper, you described the step in which the predicted landmarks are projected to the target surface mesh as “final and optional”. I would like to ask:</p>
<ol>
<li>
<p>How to technically perform this optional step in SlicerMorph module in 3D Slicer? I did not seem to find a button for such projection. I could only see “Run CPD non-rigid registration” and “Show registered source model”.</p>
</li>
<li>
<p>For downstream GMM analysis, is it preferrable to perform or not to perform this “final and optional” step?</p>
</li>
</ol>

---

## Post #8 by @muratmaga (2020-09-27 16:07 UTC)

<aside class="quote no-group" data-username="lv_xiao" data-post="7" data-topic="13704">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lv_xiao/48/8224_2.png" class="avatar"> lv_xiao:</div>
<blockquote>
<ul>
<li>How to technically perform this optional step in SlicerMorph module in 3D Slicer? I did not seem to find a button for such projection. I could only see “Run CPD non-rigid registration” and “Show registered source model”.</li>
</ul>
</blockquote>
</aside>
<p>You should see those options in here:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc1da24ba6cc82ecc2293bc8b9189189b300a041.png" data-download-href="/uploads/short-url/zYjOpiQmFiL5EFeBcntOH2FOJRT.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc1da24ba6cc82ecc2293bc8b9189189b300a041_2_690x303.png" alt="image" data-base62-sha1="zYjOpiQmFiL5EFeBcntOH2FOJRT" width="690" height="303" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc1da24ba6cc82ecc2293bc8b9189189b300a041_2_690x303.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc1da24ba6cc82ecc2293bc8b9189189b300a041_2_1035x454.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc1da24ba6cc82ecc2293bc8b9189189b300a041.png 2x" data-dominant-color="3F3F3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1249×550 21.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In fact projection is applied unless you actually do not want it. If you don’t see this, install a newer version of 3D Slicer and then SlicerMorph extension.</p>
<aside class="quote no-group" data-username="lv_xiao" data-post="7" data-topic="13704">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lv_xiao/48/8224_2.png" class="avatar"> lv_xiao:</div>
<blockquote>
<ul>
<li>For downstream GMM analysis, is it preferrable to perform or not to perform this “final and optional” step?</li>
</ul>
</blockquote>
</aside>
<p>The answer to that is data dependent. You should try to experiment with different options until you achieve what you think the best point correspondence for your analysis, and then conduct GMM.</p>

---
