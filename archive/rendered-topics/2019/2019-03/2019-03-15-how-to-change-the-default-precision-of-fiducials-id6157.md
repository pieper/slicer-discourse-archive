# How to change the default precision of fiducials?

**Topic ID**: 6157
**Date**: 2019-03-15
**URL**: https://discourse.slicer.org/t/how-to-change-the-default-precision-of-fiducials/6157

---

## Post #1 by @smrolfe (2019-03-15 15:43 UTC)

<p>Hello,<br>
I’d like to add more significant digits to fiducial points when saving to a FCSV file. I can set the values I want using Python, but the Markups table and the output FCSV file show the default precision. I have tried changing the precision under Application Settings-&gt; Units but this doesn’t impact the fiducial points. Is there a way to do this?</p>
<p>Thank you for your help.<br>
Sara</p>

---

## Post #2 by @pieper (2019-03-18 13:55 UTC)

<p>I would think that be default we should change the save precision to be lossless with respect to the datatype (float) in <a href="https://github.com/Slicer/Slicer/blob/a02f79c7c788708a3dccfeb9ff4df76b6a5868be/Libs/MRML/Core/vtkMRMLFiducialListStorageNode.cxx#L498" rel="nofollow noopener">this code</a>.  Currently it looks like we use default precision.</p>
<p>It would be analogous to what’s done <a href="https://github.com/Slicer/Slicer/blob/d9cad8916139374f5462e137b878697387874cb8/Libs/vtkTeem/vtkTeemNRRDWriter.cxx#L349-L352" rel="nofollow noopener">here</a> for double.</p>

---

## Post #3 by @lassoan (2019-03-18 14:01 UTC)

<p>I agree, file writing must be lossless.</p>
<p>Should we remove <code>std::setprecision(17)</code> from the code referenced above? I guess <code>itk::NumberToString&lt;double&gt;</code> generates a string, so setting precision should not be necessary.</p>

---

## Post #4 by @lassoan (2019-03-18 14:06 UTC)

<p><a class="mention" href="/u/smrolfe">@smrolfe</a> Somewhat related: I have added <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsNode.h#L112" rel="nofollow noopener">PositionStatus</a> attribute to markup points. A point can be defined, undefined, or previewed. This can be used for defining landmark points (with name, description, order, etc.) without specifying a position. If a point is undefined then you would need to leave position values empty in the written file (or set position to 0.0 and add a new PositionStatus column).</p>

---

## Post #5 by @pieper (2019-03-18 15:07 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="6157">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Should we remove <code>std::setprecision(17)</code> from the code referenced above? I guess <code>itk::NumberToString&lt;double&gt;</code> generates a string, so setting precision should not be necessary.</p>
</blockquote>
</aside>
<p>Yes, agreed, it’s probably a holdover.</p>

---

## Post #6 by @smrolfe (2019-03-18 17:03 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>!  I will try out the new PositionStatus attribute.</p>

---

## Post #7 by @smrolfe (2019-03-18 17:11 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/lassoan">@lassoan</a>, I will add this fix and confirm that it solves the issue.</p>

---

## Post #8 by @lassoan (2019-03-18 17:16 UTC)

<p>PositionStatus is only implemented in the markups MRML node (and used in some modules for distinguishing points being previewed vs. finally placed), but we don’t have storage node or GUI support yet. It would be great if you could contribute these.</p>

---

## Post #9 by @smrolfe (2019-03-18 17:24 UTC)

<p>Sounds like a good plan. I’ll update you on how it goes.</p>

---

## Post #10 by @smrolfe (2019-03-21 00:49 UTC)

<p>It looks like the precision was set in the Markups module <a href="https://github.com/Slicer/Slicer/blob/a02f79c7c788708a3dccfeb9ff4df76b6a5868be/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsFiducialStorageNode.cxx#L432" rel="nofollow noopener">here</a>. I removed the default precision of 3 and formatted the output string using itk::NumberToString, following the <a href="https://github.com/Slicer/Slicer/blob/d9cad8916139374f5462e137b878697387874cb8/Libs/vtkTeem/vtkTeemNRRDWriter.cxx#L349-L352" rel="nofollow noopener">example</a> suggested by <a class="mention" href="/u/pieper">@pieper</a>.</p>
<p>This is working well for me, so I’ve submitted a pull request for this update <a href="https://github.com/Slicer/Slicer/pull/1121" rel="nofollow noopener">here</a>.</p>

---

## Post #11 by @smrolfe (2019-03-26 18:05 UTC)

<p>It would be helpful to have this fix added to one of the nightly builds soon. Is there any update on the timing of this? Thanks!</p>

---

## Post #12 by @pieper (2019-03-26 18:22 UTC)

<p>Ah - yes, I’ll do that - thanks for the reminder.</p>

---

## Post #13 by @pieper (2019-03-26 18:31 UTC)

<p>Okay, done now.  Thanks Sara.</p>

---

## Post #14 by @smrolfe (2019-03-26 18:52 UTC)

<p>Great news. Thanks <a class="mention" href="/u/pieper">@pieper</a>.</p>

---
