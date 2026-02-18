# Adjusting the spacial orientation of 2D data loaded as a single slice

**Topic ID**: 24960
**Date**: 2022-08-28
**URL**: https://discourse.slicer.org/t/adjusting-the-spacial-orientation-of-2d-data-loaded-as-a-single-slice/24960

---

## Post #1 by @nileshkurwale (2022-08-28 09:30 UTC)

<p>Operating system: Mac IOS Big sur 11.6.5<br>
Slicer version: 4.11<br>
Expected behavior:<br>
Actual behavior:</p>
<p>When I load a single dicom slice in to the scene, it loads it as a volume but by default it loads it in axial view. Is there any way to change this orientation to coronal or sagital? I tried to reorient the scaler volume but it doesn’t help.<br>
Is there any way out?</p>

---

## Post #2 by @lassoan (2022-08-28 12:13 UTC)

<p>By default, slice views are rotated to match closest volume axes. If the slice orientation is closest to axial then you’ll see the complete slice in the red view (and maybe two thin lines in orthogonal views). You can drag-and-drop the image into any other slice views.</p>
<p>What is your workflow? What are you trying to achieve?</p>

---

## Post #3 by @nileshkurwale (2022-08-28 15:19 UTC)

<p>I am trying to use C arm or intraoperative X ray based 2 D navigation in two planes.  I want to use two images sets in planes perpendicular to each other ( AP and Lat) to get in same coordinate space using common reference points during imaging and then register it with camera coordinate space.</p>
<p>but unfortunately, slicer does not recognize it as sagittal or coronal view but a axial view. let me know your inputs.</p>

---

## Post #4 by @lassoan (2022-08-28 18:28 UTC)

<p>C-arm images are a whole different matter. These don’t have <code>image position patient</code> and <code>image orientation patient</code> fields.</p>
<p>You can compute some approximate orientation based on primary and secondary angles and choose a position along the projection line (in the isocenter or in the detector position). However, you can expect 5-10mm error, mostly due to that you have to assume that the detector and generator rotate around an isocenter but most C-arms are not isocentric by design; and there is also additional sagging of the C-arm in lateral position (you see slightly different area in the image center in an LAO90 image than in RAO90 image).</p>
<p>If you attach an optical tracker marker on the C-arm then you may get more accurate detector and generator positions, but it is hard to find ensure line of sight for these, because the field of view of surgical tracking cameras, such as an NDI Polaris are quite small, mostly just sufficient for tracking in the middle of the surgical field.</p>
<p>Some groups mount a tracker or a surface scanner on the detector, which may lead to better accuracy.</p>
<p>Overall, the best what Slicer could do is the trivial but inaccurate isocentric C-arm based model. We’ll make this available soon in SlicerHeart extension, but it is mainly for training and for finding optimal viewing angles and not for registration for surgical navigation.</p>
<p>Can you tell a bit about your use case? Are you trying to register pre-op CT to intra-op fluoro for navigated pedicle screw insertion? Or other MSK or vascular procedures ? Or lower-accuracy applications, such as transcatheter valve replacements? Do you use an optical tracker and/or a surface scanner for registration and tool tracking?</p>

---

## Post #5 by @nileshkurwale (2022-08-29 02:10 UTC)

<p>In fact, I am trying to do all these, but first, a simple X ray based navigation. I am working around if we can image the known geometry with markers, along with the spine in both the views perpendicular to each other and based on those known configurations confirmed by the user, estimate the magnification factor and orientations of C arm and populate a hypothetical volume to work with in the same coordinate space.<br>
I have two set of challenges</p>
<ol>
<li>identifying the image orientation with some flag and loading it correctly.</li>
<li>working around the magnification factor of C arm. either with optical tracker or from the markers in the field.<br>
question: 1. which module ( if at all already available) will allow me best to manipulate the restimation of C arm image using these computations.</li>
<li>if not, can you suggest the closest possible way?</li>
</ol>

---

## Post #6 by @lassoan (2022-08-29 04:42 UTC)

<aside class="quote no-group" data-username="nileshkurwale" data-post="5" data-topic="24960">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nileshkurwale/48/9386_2.png" class="avatar"> nileshkurwale:</div>
<blockquote>
<p>identifying the image orientation with some flag and loading it correctly.</p>
</blockquote>
</aside>
<p>There should be no need for any manual flagging. You can use <code>Positioner Primary Angle</code> and <code>Positioner Secondary Angle</code> DICOM fields to get the angle of the gantry.</p>
<aside class="quote no-group" data-username="nileshkurwale" data-post="5" data-topic="24960">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nileshkurwale/48/9386_2.png" class="avatar"> nileshkurwale:</div>
<blockquote>
<p>working around the magnification factor of C arm. either with optical tracker or from the markers in the field.</p>
</blockquote>
</aside>
<p>You can get magnification factor near the center of rotation from the ratio of <code>Source to Image Distance</code> and <code>Source to Object Distance</code> DICOM fields. Of course, the object of interest may not be in that nominal position, so it is just an approximation.</p>
<aside class="quote no-group" data-username="nileshkurwale" data-post="5" data-topic="24960">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nileshkurwale/48/9386_2.png" class="avatar"> nileshkurwale:</div>
<blockquote>
<p>which module ( if at all already available) will allow me best to manipulate the restimation of C arm image using these computations</p>
</blockquote>
</aside>
<p>There is no module for this, because this cannot be solved in software but you need a complete calibration/tracking system to address this.</p>
<aside class="quote no-group" data-username="nileshkurwale" data-post="5" data-topic="24960">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nileshkurwale/48/9386_2.png" class="avatar"> nileshkurwale:</div>
<blockquote>
<p>if not, can you suggest the closest possible way?</p>
</blockquote>
</aside>
<p>Hundreds of solutions have been proposed for C-arm calibration and C-arm/navigation system registration, and tracking over the few decades, using external or C-arm mounted optical trackers, cameras, surface scanners, fluoro tracking markers (such as <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3438694/">FTRAC</a>). Check out papers from Jeffrey Siewerdsen, Nassir Navab, Gabor Fichtinger. Some ideas have turned into products, such as Medtronic’s O-arm, or <a href="https://7dsurgical.com/flash-navigation/spine/">7d Surgical</a>’s OR-light-integrated surface scanner.</p>
<p>I don’t see any specific method to stand out; and one method probably would not address the needs of the wide variety of clinical applications anyway.</p>

---

## Post #7 by @drvarunagarwal (2022-09-01 04:27 UTC)

<p>as far as I understand with my experience with such kinds of system</p>
<p>C arm calibration, magnification etc are to be taken into account if you are registring with a pre op Ct scan</p>
<p>If all you are doing is a 2D navigation, based on an analog fluoro -</p>
<p>you just need to put a patient tracker and a c arm tracker</p>
<p>take an AP shot and a lateral shot and put them in the scene since it is a tracked c arm.<br>
and navigate using these imported shots in the scene.</p>
<p>I don’t think they require calibration</p>

---
