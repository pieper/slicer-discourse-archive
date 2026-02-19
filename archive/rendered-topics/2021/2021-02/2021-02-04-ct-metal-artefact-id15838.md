---
topic_id: 15838
title: "Ct Metal Artefact"
date: 2021-02-04
url: https://discourse.slicer.org/t/15838
---

# CT/ Metal Artefact 

**Topic ID**: 15838
**Date**: 2021-02-04
**URL**: https://discourse.slicer.org/t/ct-metal-artefact/15838

---

## Post #1 by @igaschi (2021-02-04 13:25 UTC)

<p>How can I remove metal artifacts from CT? Which plugin should I use?</p>

---

## Post #2 by @gcsharp (2021-02-04 17:42 UTC)

<p>Most successful metal artifact reduction is projection-based.  You would need to process the sinogram data, replace metal in sinogram with interpolated data, and then reconstruct.  I have never heard of anyone doing this in 3D Slicer.</p>
<p>Alternatively, you might segment out the artifacts manually and replace the intensity of those segments.  The decision to do this will depend on your intended application.  What is your intent?</p>

---

## Post #3 by @igaschi (2021-02-04 18:00 UTC)

<p>I am an orthopedic surgeon. I tried to use “3D slicer” for pre-operative and post-operative CT scan for comparison and decide bone reduction quality after surgery in acetabulum fractures. With threshold masking, 3D slicer was perfectly reconstructed pelvis bone from pre-operative CT scan, but due to metal artifacts, post-operative CT scan’s reconstruction was un-acceptable.</p>

---

## Post #4 by @gcsharp (2021-02-04 20:51 UTC)

<p>I see, thank you for explaining.  For your application, I think you will want a projection-based metal artifact reduction implementation.  Since all major CT vendors offer this capability, one option could be to find an imaging centers in your area that can do this, and then refer the patient(s) to that center for the post-operative imaging study.</p>

---

## Post #5 by @lassoan (2021-02-05 04:00 UTC)

<p>I fully agree with <a class="mention" href="/u/gcsharp">@gcsharp</a> that the best results can be achieved with using proper imaging equipment. If it is not possible to get a better scan and the current scan is good enough so that you can distinguish metal artifact from bone then you may be able to clean up the segmentation manually or use semi-automatic segmentation tools.</p>
<p>One option is to start with thresholding and then remove large artifacts using Scissors effect and clean up the rest using Paint effect. It is tedious work, but if you don’t aim for a perfect segmentation everywhere but you know where you need accuracy and you focus your efforts there then it may be manageable.</p>
<p>Alternatively, you can try “Grow from seeds” effect (create a “bone” and an “other” segment paint a few seeds, and see if the algorithm can distinguish the artifact from bone). You can also try “Fill between slices” effect, which allows you to manually segment a small number of slices and smoothly interpolate in between them. If you post a few screenshots then we may be able to give more specific suggestions.</p>
<p>To get started with image segmentation in Slicer, check out <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">this documentation page</a>.</p>

---

## Post #6 by @igaschi (2021-02-05 16:19 UTC)

<p>CT scan can supress metal artefacts but unfortunately, we used our database for research and old CT scanS were not avaliable for this process. So i tried to use 3d slicer but as far as I understand, the program is not suitable for it.</p>

---

## Post #7 by @lassoan (2021-02-05 16:29 UTC)

<aside class="quote no-group" data-username="igaschi" data-post="6" data-topic="15838">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/igaschi/48/9769_2.png" class="avatar"> igaschi:</div>
<blockquote>
<p>i tried to use 3d slicer but as far as I understand, the program is not suitable for it.</p>
</blockquote>
</aside>
<p>In general, you cannot effectively remove metal artifacts <em>after</em> reconstruction fully automatically. For specific use cases it is possible to create post-processing methods to suppress metal artifacts and enhance certain features, but since this problem is largely solved in current scanners, there is little incentive to invest too much effort into this.</p>
<p>If your eye can still distinguish artifact from bone then you can fix the segmentation using the techniques I described above.</p>

---

## Post #8 by @igaschi (2021-02-05 16:37 UTC)

<p>I used appropriate threshold masking for bone and plate. After that, i was segmented all bone parts and plate. In coronal, sagittal and axial images, I were painted all segments after than with growing seed, I was reconstructed model. Cortical bone’s threshold density and plate’s threshold density was similar so I couldn’t separated them. I tried to use island module and delete small islands but artefacts were connected each other and I couldn’t delete them. Forevaluation of bone reduction quality, i don’t want to use fill between slices modul.</p>

---

## Post #9 by @lassoan (2021-02-25 05:57 UTC)

<p>2 posts were merged into an existing topic: <a href="/t/mar-of-ct-development/16200/2">MAR of CT development</a></p>

---
