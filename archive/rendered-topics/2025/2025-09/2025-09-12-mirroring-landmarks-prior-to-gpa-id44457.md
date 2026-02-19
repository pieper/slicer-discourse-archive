---
topic_id: 44457
title: "Mirroring Landmarks Prior To Gpa"
date: 2025-09-12
url: https://discourse.slicer.org/t/44457
---

# Mirroring landmarks prior to GPA

**Topic ID**: 44457
**Date**: 2025-09-12
**URL**: https://discourse.slicer.org/t/mirroring-landmarks-prior-to-gpa/44457

---

## Post #1 by @macorreia42 (2025-09-12 14:34 UTC)

<p>Dear Support,</p>
<p>I have a number of incomplete mandibles on which I have placed landmarks prior to GM analyses. For each one, I only placed landmarks on the most complete side, so some .mrk.json have landmarks on a left mandible and others on the right, but never both. Prior to landmarking, I roughly “aligned” the model so that they all match the planes in 3D Slicer (e.g., chin facing anterior).<br>
I’ve read on the geomorph package that to mirror the landmarks, I only need to multiply the x axis by -1, but the truth is that the coordinate system isn’t always the same since many mandibles are incomplete. For instance, in the images below you can see that the right side isn’t always negative x and vice versa. Some example .mrk.json is here.<br>
I don’t want to mirror across the sagittal plane exactly as <a href="https://discourse.slicer.org/t/mirroring-landmarks-across-midsagittal-plane/41249/3">here</a>, or conduct asymmetry analyses as <a href="https://discourse.slicer.org/t/mirror-landmarks-and-evaluate-mandible-asymmetry-in-deca/43177/3">here</a> or reflect to the other side so I have both sets as <a href="https://discourse.slicer.org/t/reflect-markups-landmarks/20301">here</a>. I just want them to all “look“ as right or left prior to GPA.<br>
I was looking for solutions and found this workflow: <strong>Using Landmark Registration Module; Go to Modules → Registration → Landmark Registration; Load your fiducial points (landmarks); Create a new transform; In the transform matrix, set the scaling values: For X-axis reflection: set X scaling to -1, Y and Z to 1; Apply the transform to your model; Harden the transform (Data module → right-click → Harden transform).</strong><br>
Is this reasonable or am I doing something horrible to my data?<br>
Thank you!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e95e1c0863816a0827b44d9f0e551c5341d4f08.png" data-download-href="/uploads/short-url/mCUyLkEol3mHdN2JIbytrlcqilq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e95e1c0863816a0827b44d9f0e551c5341d4f08_2_690x378.png" alt="image" data-base62-sha1="mCUyLkEol3mHdN2JIbytrlcqilq" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e95e1c0863816a0827b44d9f0e551c5341d4f08_2_690x378.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e95e1c0863816a0827b44d9f0e551c5341d4f08_2_1035x567.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e95e1c0863816a0827b44d9f0e551c5341d4f08_2_1380x756.png 2x" data-dominant-color="C1C3DF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2559×1405 437 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9de42d7a30c93b6108bd252edc824fa679bd8b87.jpeg" data-download-href="/uploads/short-url/mwLPxb3skGbZ3nslud2TLSMB04T.jpeg?dl=1" title="image (1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9de42d7a30c93b6108bd252edc824fa679bd8b87_2_690x410.jpeg" alt="image (1)" data-base62-sha1="mwLPxb3skGbZ3nslud2TLSMB04T" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9de42d7a30c93b6108bd252edc824fa679bd8b87_2_690x410.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9de42d7a30c93b6108bd252edc824fa679bd8b87_2_1035x615.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9de42d7a30c93b6108bd252edc824fa679bd8b87_2_1380x820.jpeg 2x" data-dominant-color="C4C5DB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image (1)</span><span class="informations">1920×1143 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3598b5de9d5402faa47dfe5e48608247666aa8d.png" data-download-href="/uploads/short-url/wreeuGcAeNgoBiwmOXItdHL8opf.png?dl=1" title="image (2)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3598b5de9d5402faa47dfe5e48608247666aa8d_2_690x405.png" alt="image (2)" data-base62-sha1="wreeuGcAeNgoBiwmOXItdHL8opf" width="690" height="405" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3598b5de9d5402faa47dfe5e48608247666aa8d_2_690x405.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3598b5de9d5402faa47dfe5e48608247666aa8d_2_1035x607.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3598b5de9d5402faa47dfe5e48608247666aa8d_2_1380x810.png 2x" data-dominant-color="C6C7E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image (2)</span><span class="informations">2554×1501 420 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2025-09-12 14:55 UTC)

<aside class="quote no-group" data-username="macorreia42" data-post="1" data-topic="44457">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/macorreia42/48/80835_2.png" class="avatar"> macorreia42:</div>
<blockquote>
<p>I was looking for solutions and found this workflow: <strong>Using Landmark Registration Module; Go to Modules → Registration → Landmark Registration; Load your fiducial points (landmarks); Create a new transform; In the transform matrix, set the scaling values: For X-axis reflection: set X scaling to -1, Y and Z to 1; Apply the transform to your model; Harden the transform (Data module → right-click → Harden transform).</strong></p>
</blockquote>
</aside>
<p>This is equivalent to multiplying the X axis with -1 (as suggested in the geomorph).</p>
<aside class="quote no-group" data-username="macorreia42" data-post="1" data-topic="44457">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/macorreia42/48/80835_2.png" class="avatar"> macorreia42:</div>
<blockquote>
<p>Is this reasonable or am I doing something horrible to my data?</p>
</blockquote>
</aside>
<p>No you are not (you can always reverse things by multiplying them one more time). However, from data management purposes I suggest adding a suffix (e.g., _mirrored) to object name to distinguish them from the original dataset (or save it to a different folder). Because after you harden the transform and save the landmarks, they will no longer align with the model they are generated from. Unless you document this somewhere (or use convention), you might be confused when you get back to your data after sometime.</p>

---

## Post #3 by @macorreia42 (2025-09-12 14:57 UTC)

<p>Thank you so very much! And the fact that the sagittal landmarks are not exactly at 0 will not be an issue, then?<br>
I’ll make sure to add the _mirrored.</p>

---
