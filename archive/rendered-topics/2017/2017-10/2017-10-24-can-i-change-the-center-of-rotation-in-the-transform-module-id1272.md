---
topic_id: 1272
title: "Can I Change The Center Of Rotation In The Transform Module"
date: 2017-10-24
url: https://discourse.slicer.org/t/1272
---

# Can I change the center of rotation in the 'transform' module?

**Topic ID**: 1272
**Date**: 2017-10-24
**URL**: https://discourse.slicer.org/t/can-i-change-the-center-of-rotation-in-the-transform-module/1272

---

## Post #1 by @Ramttoong (2017-10-24 01:35 UTC)

<p>Can I change the center of rotation in the ‘transform’ module?</p>

---

## Post #2 by @lassoan (2017-10-24 01:49 UTC)

<p>Trying to align objects by manually rotating a transform is a very difficult, long, iterative process, and there is no guarantee for optimal solution, no matter how much time you spend with it.</p>
<p>For quick initial alignment you can use the 3D transform editing widget (in Transforms module Display/Interaction section enable “Visible in 3D view”).</p>
<p>For accurate alignment, we always end up using landmark registration instead of sequence of manual rotations. These modules guarantee to give you optimal solution in deterministic time, optimizing translation and rotation around all axis simultaneously, in real-time and can also compute non-rigid alignments:</p>
<ul>
<li>Fiducial Registration Wizard (in SlicerIGT extension): usable for any nodes (images, models, etc), does not require any initial alignment; see tutorials at <a href="http://www.slicerigt.org">www.slicerigt.org</a></li>
<li>Landmark Registration module (in Slicer core): usable for images only, but contains nice features for defining the landmarks and setting up views; images need to be approximately aligned before</li>
</ul>
<p>This question has been asked before, you can find some additional thoughts there:</p><aside class="quote" data-post="4" data-topic="857">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michael_hardisty/48/1593_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/can-i-adjust-the-center-of-orientation-when-using-transform-module/857/4">Can I adjust the center of orientation when using 'transform module'?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi Woo-ram, 
We have done something similar to what you are suggesting by nesting 
transforms.  We created ‘local’ rotations by rotating an object that was 
already translated to the origin.  We then put the rotating transform 
within another transform that translated it back to position.  The effect 
is that rotations appear to be local, when adjusting the sliders in the 
transform editor. 
Michael
  </blockquote>
</aside>


---
