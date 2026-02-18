# How to set dimensions and slice thickness when reconstructing FIB stack

**Topic ID**: 43165
**Date**: 2025-05-30
**URL**: https://discourse.slicer.org/t/how-to-set-dimensions-and-slice-thickness-when-reconstructing-fib-stack/43165

---

## Post #1 by @Biaxialerzug (2025-05-30 12:47 UTC)

<p>Hi,</p>
<p>I’m using 3D Slicer to reconstruct a material volume. The slices of this volume were createt using FIB (Focused Ion Beam) in a SEM. At this point I struggle to set the correct dimensions of my volume. Each image of my stack is 250x250 pixel and 1 pixel is equivalent to 0.025µm. My stack consists of 199 images, where one image reprents one slice created using FIB with a slice thickness of 40nm. How can I implement the slice thickness of 40nm and the correct dimensions to have a correct length bar?</p>

---

## Post #2 by @muratmaga (2025-05-30 14:47 UTC)

<p>After you import your data, you can edit those fields in the <code>Volumes</code> module. From your description it sounds like spacing should be (0.000025, 0.000025, 0.00004). Default units in slicer is millimeters.</p>

---

## Post #3 by @Biaxialerzug (2025-05-30 14:56 UTC)

<p>Thank you very much!<br>
I changed the values and verified them by using the measurement tool and indeed it shows the correct distance.</p>

---

## Post #4 by @Biaxialerzug (2025-06-06 12:06 UTC)

<p>Now, with everything set, the ruler in the 3D view is not correct. I imported the stack via SlicerMorph import tool and set the correct values for image spacing. Then I did the segmentation and export the segmentation to models to use the clipping planes. When I then turn on the ruler, it shows something with meters but the 2D windows show the correct nanometer values. How to fix this?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/926f83e2f2b6ecb1ae748fb1a43effbefab4c6e8.jpeg" data-download-href="/uploads/short-url/kTqD71IjCYDeEjtgr4KF7e7JK2I.jpeg?dl=1" title="Screenshot 2025-06-06 140553" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/926f83e2f2b6ecb1ae748fb1a43effbefab4c6e8_2_690x331.jpeg" alt="Screenshot 2025-06-06 140553" data-base62-sha1="kTqD71IjCYDeEjtgr4KF7e7JK2I" width="690" height="331" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/926f83e2f2b6ecb1ae748fb1a43effbefab4c6e8_2_690x331.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/926f83e2f2b6ecb1ae748fb1a43effbefab4c6e8_2_1035x496.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/926f83e2f2b6ecb1ae748fb1a43effbefab4c6e8_2_1380x662.jpeg 2x" data-dominant-color="A2A9B3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-06-06 140553</span><span class="informations">1914×920 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @muratmaga (2025-06-06 15:25 UTC)

<p>I assume you changed the default unit to nanometers, and then enter the spacing value in ImageStacks? Is that the correct description of the steps?</p>
<p>If so, this is might be related to some issue with Units support in Slicer; it  is not entirely complete. If you can file a bug detailing the steps of what you have done  at the <a href="https://github.com/Slicer/Slicer" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/Slicer: Multi-platform, free open source software for visualization and image computing.</a>. Not sure when it can be fixed, but it will be put in the queue</p>
<p>If you want your ruler and measurement values to display the right units, bring back the default unit to mm, and when you are using the ImageStacks enter the value in form of millimeters, not nanometers. Then both units should display correctly.</p>
<p>Altneratively, use can edit the ruler unit manually after you have taken a screenshot. (the scale will be correct, it appears it is displaying wrong unit).</p>

---
