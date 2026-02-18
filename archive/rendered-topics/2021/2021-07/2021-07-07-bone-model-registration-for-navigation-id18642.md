# Bone model registration for navigation

**Topic ID**: 18642
**Date**: 2021-07-07
**URL**: https://discourse.slicer.org/t/bone-model-registration-for-navigation/18642

---

## Post #1 by @qiqi5210 (2021-07-07 12:34 UTC)

<p>Hi, Mr. Lasso! Sorry to reopen this question, I recently met the same problem. I have a head model and a bone model, I want to make the relative position of the two models in the 3D view same with the real world(The bone is tracked). This is my hierarchy in Slicer.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ac675cc66340e437c9798a3c0700594b9b13393.png" data-download-href="/uploads/short-url/jNF5zjDdRhegap4f09Oa3CuoqRR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ac675cc66340e437c9798a3c0700594b9b13393.png" alt="image" data-base62-sha1="jNF5zjDdRhegap4f09Oa3CuoqRR" width="690" height="123" data-dominant-color="F8F8F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1107×198 3.81 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The main question of mine is how do I compute the <code>F4ToTool</code> transform?(The “F4” is a bone model and I have its 3D model in real world.)</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="9876">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/difficulty-with-multiple-landmark-registrations/9876/4">Difficulty With Multiple Landmark Registrations</a></div>
<blockquote>
<p>then you can collect points in “Marker6” coordinate system and mark the corresponding points on the model (“NewModel” coordinate system) and landmark registration computes NewModelToMarker6Transform.</p>
</blockquote>
</aside>
<p>How do I collect points? I use the <code>StylusTipToStylus</code> Transform point to the markpoint on the bone in the real world and click "place ‘from’ ", then mark the corresponding points on the bone model in Slicer, but the computed transform is not right for me. I also use the same method but the real world points is the “To” list, it is also not work for me.<br>
Could you give me some detailed guidance? Really Thanks!</p>
<p>If what I ask is not clear, please let me know.</p>

---

## Post #2 by @lassoan (2021-07-12 14:56 UTC)

<p>If you have already calibrated your stylus then Fiducial Registration Wizard can compute all the transforms that you need.</p>
<p>The names in the transform tree indicate errors. For example, you have placed <code>StylusToTracker</code> transform below <code>ReferenceToRas</code> transform - you missed a <code>TrackerToReference</code> transform in between. Similarly for <code>ToolToTracker</code> transform. Could you please attach a picture that shows what coordinate systems do you use? Something similar to this: <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/ApplicationfCalCoordinateSystemDefinitions.html" class="inline-onebox">Plus applications user manual: Coordinate system definitions used by fCal</a></p>
<p>What is the difference between the head model and the bone model? Are they both surface meshes?</p>

---
