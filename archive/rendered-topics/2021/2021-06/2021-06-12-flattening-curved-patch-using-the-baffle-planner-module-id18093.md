---
topic_id: 18093
title: "Flattening Curved Patch Using The Baffle Planner Module"
date: 2021-06-12
url: https://discourse.slicer.org/t/18093
---

# Flattening Curved Patch using the Baffle Planner Module

**Topic ID**: 18093
**Date**: 2021-06-12
**URL**: https://discourse.slicer.org/t/flattening-curved-patch-using-the-baffle-planner-module/18093

---

## Post #1 by @Fluvio_Lobo (2021-06-12 16:26 UTC)

<p>Hello,</p>
<p>I have been using the Baffle Planner module for cranial flaps and it works wonders!<br>
I want to expand its usage to create curved bone flaps that can be harvested from a thick part of the skull and used to form a missing structure. For instance, a nose bridge.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7ae2e5a67d9bcb48568a5080ec38d4c869b5340b.jpeg" data-download-href="/uploads/short-url/hx6njQ397w9stogyXYYkeRUP6xJ.jpeg?dl=1" title="nose_bridge_example.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ae2e5a67d9bcb48568a5080ec38d4c869b5340b_2_690x373.jpeg" alt="nose_bridge_example.PNG" data-base62-sha1="hx6njQ397w9stogyXYYkeRUP6xJ" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ae2e5a67d9bcb48568a5080ec38d4c869b5340b_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ae2e5a67d9bcb48568a5080ec38d4c869b5340b_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ae2e5a67d9bcb48568a5080ec38d4c869b5340b_2_1380x746.jpeg 2x" data-dominant-color="484E53"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">nose_bridge_example.PNG</span><span class="informations">1920×1040 365 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I have been trying to use the “Flatten Baffle” section of the module to match the curvature of a region of the skull that I believe would be good for harvesting, but I do not understand how to use the “Fixed points” fiducial markets to achieve this. The video showing the module does not cover this section.</p>
<p>Is this flattening tool even the right approach? Is it better to do a model registration and allow for deformation?</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2021-06-12 19:04 UTC)

<p>Flattening feature creates a flat shape corresponding to the curved shape with minimal distortion, originally developed for creating cutting template for fabric (see <a href="https://www.sciencedirect.com/science/article/abs/pii/S0003497521004574">this journal paper</a> for details). This should be applicable to other flat sheet of material, such as your case - tissue harvesting from relatively flat regions of the skull.</p>
<p>Fixed points are the landmark points that you will use to match points of the flattened model and the baffle model (so that you know how to align flattened model on the baffle model). They should be points that you can identify on the anatomy and distributed somewhat evenly. I added arrows to indicate potentially good candidate points (you need to choose minimum 2, and it is probably better not to choose more than 4).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35a6fc0b40960fd6adbed6838428ef8ad5aef496.jpeg" alt="image" data-base62-sha1="7ED4fZcxoB8BWUjVR1AwwTzf2js" width="370" height="292"></p>
<p>Let us know how it works out for you.</p>

---

## Post #3 by @Fluvio_Lobo (2021-06-12 19:54 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Thank you! The end result is a PNG that I can use for cutting a patch.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50312cbe65ac025507eae1c0e73bf6dd66249e3f.png" data-download-href="/uploads/short-url/brpym1w4vCIMlkkQGUonTw7umh9.png?dl=1" title="patch" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50312cbe65ac025507eae1c0e73bf6dd66249e3f.png" alt="patch" data-base62-sha1="brpym1w4vCIMlkkQGUonTw7umh9" width="507" height="500" data-dominant-color="BEBEBE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">patch</span><span class="informations">1024×1008 3.68 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2021-06-12 20:07 UTC)

<p>Nice! Note the tiny red dots, they are the landmark points that you can use for alignment. It seems that the labels are hidden, we should probably fix that, but as a a workaround you can change the default markups display options to show point labels.</p>

---

## Post #5 by @Fluvio_Lobo (2021-06-12 23:53 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>This may not be a huge deal but I just realized that the flattened model is on the workspace, just very very very far away from the model. This is why I did not know if the module was working! I essentially just saved the PNG before, did not realize that the surface model was visible.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfcb69a5d0e729e01fff2ca9785b660d0105717f.png" data-download-href="/uploads/short-url/vVMhHLUbcBqcqvkDanZDKqKYaHJ.png?dl=1" title="flattened_model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfcb69a5d0e729e01fff2ca9785b660d0105717f_2_690x373.png" alt="flattened_model" data-base62-sha1="vVMhHLUbcBqcqvkDanZDKqKYaHJ" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfcb69a5d0e729e01fff2ca9785b660d0105717f_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfcb69a5d0e729e01fff2ca9785b660d0105717f_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfcb69a5d0e729e01fff2ca9785b660d0105717f_2_1380x746.png 2x" data-dominant-color="47484E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">flattened_model</span><span class="informations">1920×1040 337 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2021-06-13 01:31 UTC)

<aside class="quote no-group" data-username="Fluvio_Lobo" data-post="5" data-topic="18093">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/fluvio_lobo/48/81262_2.png" class="avatar"> Fluvio_Lobo:</div>
<blockquote>
<p>I essentially just saved the PNG before, did not realize that the surface model was visible.</p>
</blockquote>
</aside>
<p>Thanks for the feedback. The model is in a completely different coordinate system. It is just used during the PNG saving and not for anything else. Maybe we should just delete the model after the PNG export to not confuse anyone with it.</p>

---

## Post #7 by @Fluvio_Lobo (2021-06-13 01:49 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I actually think the model is beneficial!<br>
I can see myself overlaying the model over a thick area of the skull, given some thickness mapping, as part of a planning session.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d99d5a0c410c6c7b0b48c99ebfe38b5f732f40f7.jpeg" data-download-href="/uploads/short-url/v36JBRoTwjK719j1g0dbnI7PpFd.jpeg?dl=1" title="Inkedsuperior_view_thickness_mapping_LI" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d99d5a0c410c6c7b0b48c99ebfe38b5f732f40f7_2_460x500.jpeg" alt="Inkedsuperior_view_thickness_mapping_LI" data-base62-sha1="v36JBRoTwjK719j1g0dbnI7PpFd" width="460" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d99d5a0c410c6c7b0b48c99ebfe38b5f732f40f7_2_460x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d99d5a0c410c6c7b0b48c99ebfe38b5f732f40f7.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d99d5a0c410c6c7b0b48c99ebfe38b5f732f40f7.jpeg 2x" data-dominant-color="9E88A5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Inkedsuperior_view_thickness_mapping_LI</span><span class="informations">658×715 83.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2021-06-13 04:13 UTC)

<p>OK. I’ve just updated the <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/README.md#baffle-planner-module">module documentation</a> to make things a bit more clear.</p>
<p>Note that you can use “Fiducial registration wizard” module in SlicerIGT extension to fit the flattened surface to the skull:</p>
<ul>
<li>Choose “From fiducials” → “Model flattened fixed points”</li>
<li>Create a new set of fiducials for “To fiducials” and place the fixed points on the skull where you want to harvest tissue from.</li>
<li>Choose “Create new linear transform” for registration result.</li>
<li>Apply the computed transform to the flattened “Model” node. This will move the flat surface patch to the target location.</li>
</ul>

---

## Post #9 by @Fluvio_Lobo (2021-06-13 16:22 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I followed through with these steps and this is the result.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c37de3228e0363639ef8cbdc4a0b81e7c5e7b96.png" data-download-href="/uploads/short-url/k0qxCZ4IpYFr1ezT2sLjtlMZ31k.png?dl=1" title="overlaying_harvest_patch" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c37de3228e0363639ef8cbdc4a0b81e7c5e7b96_2_690x373.png" alt="overlaying_harvest_patch" data-base62-sha1="k0qxCZ4IpYFr1ezT2sLjtlMZ31k" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c37de3228e0363639ef8cbdc4a0b81e7c5e7b96_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c37de3228e0363639ef8cbdc4a0b81e7c5e7b96_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c37de3228e0363639ef8cbdc4a0b81e7c5e7b96_2_1380x746.png 2x" data-dominant-color="777593"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">overlaying_harvest_patch</span><span class="informations">1920×1040 343 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol>
<li>I had to translate the flattened mesh from Z=0 to a similar height as the thickness map</li>
<li>Then used the fiducial registration wizard to contour the flattened model to a target area on the surface of the thickness map</li>
<li>I allowed the model to <strong>warp</strong> to match the contour as much as possible</li>
<li>I added more points to lift the infinitesimal surface our of the surface of the thickness map (too many points throws the entire thing off!)</li>
</ol>
<p>Any suggestions on how to improve this registration? My guess is that the flattened model should be made thicker!</p>

---

## Post #10 by @lassoan (2021-06-16 23:21 UTC)

<p>Creating a thick 3D model (e.g., for 3D printing) and creating a 2D cutting template (e.g., for cutting a shape from surgical fabric) are two completely different workflows. If you flatten the thick 3D model then it will flatten its entire surface area (edge and both sides), so it will not be useful.</p>
<p>Displaying the disk over the skull without registration, just to approximately see how much bone you need make sense. However, trying to warp the flattened disk to the bone does not sound like a valid approach to me. What would this deformable warping simulate?</p>
<p>Instead, if you want to create a realistic bone reconstruction plan then I would recommend to simulate the surgical procedure. For example, if you cut the bone with a straight saw then you can simulate that by placing a cutting plane, then use that plane to cut a piece from the skull, then cut it into two then move these pieces to the target location to verify that they look good. You can complete this workflow manually to test the concept (using Segment Editor and/or Dynamic modeler module) or automate it, similarly to the <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner">fibula flap bone reconstruction planner module</a>:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="wsr_g_1E_pw" data-video-title="Mandible reconstruction on Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=wsr_g_1E_pw" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/wsr_g_1E_pw/hqdefault.jpg" title="Mandible reconstruction on Slicer" width="" height="">
  </a>
</div>

<p>You may also consider getting a virtual reality headset, because it allows you to take bone fragments and position them as you would to it in real world (but more easily, because there is no gravity, so when you release a piece then it just stays there; you can zoom in the space as much as you want, so you can manipulate things very accurately; and you save time and money, because you don’t need to 3D print anything).</p>
<div class="youtube-onebox lazy-video-container" data-video-id="VzVjvnKuBAE" data-video-title="3D Slicer reconstruction of fragmented bones in virtual reality" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=VzVjvnKuBAE" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/VzVjvnKuBAE/maxresdefault.jpg" title="3D Slicer reconstruction of fragmented bones in virtual reality" width="" height="">
  </a>
</div>


---

## Post #11 by @Fluvio_Lobo (2021-06-17 00:05 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="18093">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Displaying the disk over the skull without registration, just to approximately see how much bone you need make sense. However, trying to warp the flattened disk to the bone does not sound like a valid approach to me. What would this deformable warping simulate?</p>
</blockquote>
</aside>
<p>You are right, this is not the right approach. I will look into the mandibular reconstruction video and module to recreate the procedure, then warp the harvested piece and evaluate.</p>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="18093">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You may also consider getting a virtual reality headset, because it allows you to take bone fragments and position them as you would to it in real world (but more easily, because there is no gravity, so when you release a piece then it just stays there; you can zoom in the space as much as you want, so you can manipulate things very accurately; and you save time and money, because you don’t need to 3D print anything).</p>
</blockquote>
</aside>
<p>This would be really useful for procedures like craniosynostosis. I thick I can find a VR headset somewhere, thanks for the advice!</p>

---

## Post #12 by @lassoan (2021-06-17 01:56 UTC)

<aside class="quote no-group" data-username="Fluvio_Lobo" data-post="11" data-topic="18093">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/fluvio_lobo/48/81262_2.png" class="avatar"> Fluvio_Lobo:</div>
<blockquote>
<p>This would be really useful for procedures like craniosynostosis.</p>
</blockquote>
</aside>
<p>If you are interested in craniosynostosis then you might find these prior work useful:</p>
<ul>
<li><a href="https://www.nature.com/articles/s41598-019-54148-4" class="inline-onebox">Craniosynostosis surgery: workflow based on virtual surgical planning, intraoperative navigation and 3D printed patient-specific guides and templates | Scientific Reports</a></li>
<li><a href="https://blog.kitware.com/introducing-osteotomy-planner-a-3d-slicer-extension-module-to-simulate-bone-cutting-remodeling-and-repositioning/">https://blog.kitware.com/introducing-osteotomy-planner-a-3d-slicer-extension-module-to-simulate-bone-cutting-remodeling-and-repositioning/</a></li>
</ul>

---
