# Standard alignment for 3D surface models

**Topic ID**: 15657
**Date**: 2021-01-25
**URL**: https://discourse.slicer.org/t/standard-alignment-for-3d-surface-models/15657

---

## Post #1 by @anromero (2021-01-25 16:36 UTC)

<p>Operating system: iOS 11.1<br>
Slicer version: 4.11.0<br>
Expected behavior: Standardize alignment of 3D surface models before landmarking<br>
Actual behavior:</p>
<p>Hello there,</p>
<p>I’m using 3D Slicer to place fixed and semi-landmarks across macaque and baboon cranial surfaces, but I’m having trouble figuring out a way to standardize the alignment of these models in 3D Slicer before starting the landmarking process. I think this should be possible through the Transforms module using the linear transform function, but I need to make sure that all skulls are aligned in the same way so as not to mess up the landmark configurations.</p>
<p>I’d appreciate any input or ideas anyone has on how I can accomplish this task.</p>
<p>All the best,<br>
Ashly</p>

---

## Post #2 by @muratmaga (2021-01-25 17:09 UTC)

<p>You can definitely align 3D models using the manual alignment tool (Transforms module). Here is the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html" rel="noopener nofollow ugc">documentation for it</a></p>
<p>The question is whether it is worthwhile to do so?<br>
Surely not for anatomical landmarks, because you can orient the 3D model interactively in 3D viewer, and put your landmarks on it. You can then turn the model around and evaluate their placement in different views. Having consistent orientation might be useful for ‘reconstructed landmarks’ such as picking up the highest degree of curvature along a structure, but those tend to be very poor choice of landmarks particularly in 3D models due to their subjectivity.</p>
<p>As for the semi-landmarks, it also depends on what you want to do? Are you using one of the SLicerMorph modules such as PseudoLMGenerator or SemiLMGenerator? Tells us a bit more and we can advise whether it makes sense to try to reorient your models.</p>

---

## Post #3 by @muratmaga (2021-01-25 17:27 UTC)

<aside class="quote no-group" data-username="anromero" data-post="1" data-topic="15657">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anromero/48/10120_2.png" class="avatar"> anromero:</div>
<blockquote>
<p>I need to make sure that all skulls are aligned in the same way so as not to mess up the landmark configurations.</p>
</blockquote>
</aside>
<p>If you put your existing LM configurations under the same transform as the 3D model, they will all transform in the same way. So you won’t mess up anything.</p>

---

## Post #4 by @anromero (2021-01-25 19:14 UTC)

<p>Is orienting each crania in exactly the same position within the bounding box (box with S, I, R, L, A, P) important when collecting landmarks manually for each specimen? I have been loading in the 3D model and then clicking the center view button to move the specimen to the middle of the box. Sometimes, the specimen isn’t lined up correctly within that box (e.g., the A letter doesn’t line up with the anterior portion of the specimen). I know I can manually change this in the Transforms module, but my concern is that if I change this manually, then all my specimens will be situated slightly differently within this box.</p>
<p>If this alignment within this box doesn’t matter to the actual landmark collection process, then I will just align the few specimens that don’t load in correctly manually using the Transforms module. I want to make sure that the landmark configurations I’m collecting are valid even if I don’t have each cranium aligned within that box exactly the same way. This is my main concern.</p>
<p>I’m using the CreateSemiLMPatches module to place patches on each specimen. I haven’t quite figured out how to do this automatically across specimens yet.</p>

---

## Post #5 by @anromero (2021-01-25 19:15 UTC)

<p>I plan to place fixed LMs as in this figure.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bd0c6dd99de362814068679f33a3596057bcbe1.jpeg" data-download-href="/uploads/short-url/jWRFA1Z5Xk1pbkNKQ9iwjM13eF3.jpeg?dl=1" title="LM figure" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8bd0c6dd99de362814068679f33a3596057bcbe1_2_364x500.jpeg" alt="LM figure" data-base62-sha1="jWRFA1Z5Xk1pbkNKQ9iwjM13eF3" width="364" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8bd0c6dd99de362814068679f33a3596057bcbe1_2_364x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8bd0c6dd99de362814068679f33a3596057bcbe1_2_546x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8bd0c6dd99de362814068679f33a3596057bcbe1_2_728x1000.jpeg 2x" data-dominant-color="929EC3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">LM figure</span><span class="informations">2220×3046 1.31 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @anromero (2021-01-25 19:25 UTC)

<p>Here is an example of the misalignment within the box that I’m asking about.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c36ec4cef29b015085865b935b44530ea8a5eb6.jpeg" data-download-href="/uploads/short-url/41B2yBW2eoPmyS5AAemte520PXw.jpeg?dl=1" title="Screen Shot 2021-01-25 at 1.25.15 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c36ec4cef29b015085865b935b44530ea8a5eb6_2_690x490.jpeg" alt="Screen Shot 2021-01-25 at 1.25.15 PM" data-base62-sha1="41B2yBW2eoPmyS5AAemte520PXw" width="690" height="490" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c36ec4cef29b015085865b935b44530ea8a5eb6_2_690x490.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c36ec4cef29b015085865b935b44530ea8a5eb6_2_1035x735.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c36ec4cef29b015085865b935b44530ea8a5eb6_2_1380x980.jpeg 2x" data-dominant-color="BBBDD4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-01-25 at 1.25.15 PM</span><span class="informations">3008×2138 523 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @muratmaga (2021-01-25 19:44 UTC)

<p>Couple things:</p>
<p>In practice aligning things with the bounding box is not a good choice. Because bounding is box is determined by the principal axis of the specimen. If you imagine the specimen rotated 45 degrees clockwise in this view, you will get a very different bounding box. So if your goal is to get consistent alignment, you should align specimens not the bounding box.</p>
<p>If your goal is landmarking, you can safely disregard the anatomical labels and orientations. You will feed this data into a Procrustes alignment tool (within SLicerMorph or elsewhere), and for that the important thing is the landmark order correspond to each other. For example as long as LM1 is on Nasion for all your samples it doesn’t matter if the bounding box label is showing that side to be posterior or left.</p>
<p>As for transferring semiLMs across samples we provide multiple ways of doing this:</p>
<ol>
<li>You can do this once on a sample of your choice and save the connectivity table, and the resultant semiLM set and then use <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/CreateSemiLMPatches" rel="noopener nofollow ugc">ProjectSemiLMPatches</a>.</li>
<li>Or you can use <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ProjectSemiLM" rel="noopener nofollow ugc">ProjectSemiLM</a>, which uses a TPS warp of existing landmarks to transfer the semiLM template.</li>
</ol>
<p>A paper that evaluate how these two perform in great ape skulls (chimp, gorilla, and orangutans) is just published. You can check it out at <a href="https://dx.doi.org/10.1002/ajpa.24214" rel="noopener nofollow ugc">https://dx.doi.org/10.1002/ajpa.24214</a>. I think you will find it useful for your project.</p>
<p>If you are doing a single species/population study, <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ALPACA" rel="noopener nofollow ugc">ALPACA</a> can be also useful. The help link also provides the tutorial and the associated preprint in Biorxiv.</p>
<p>good luck with the project, it looks cool and let us know how it goes.</p>

---

## Post #8 by @anromero (2021-01-25 19:46 UTC)

<p>Great, thank you so much! This is exactly the information I needed.</p>

---
