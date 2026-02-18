# Slicer Slice view scrolling lag

**Topic ID**: 2336
**Date**: 2018-03-16
**URL**: https://discourse.slicer.org/t/slicer-slice-view-scrolling-lag/2336

---

## Post #1 by @jperdomo23 (2018-03-16 15:56 UTC)

<p>Hello Slicer Discourse,</p>
<p>Our team is developing software using the Slicer <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets" rel="nofollow noopener">Slicelets</a> model. We are experiencing some lag with scrolling through volumes in the Slice views, and were trying to isolate the issue. It occurs after we have added several of our own ‘Segment’ objects. Each one of these objects is composed of:</p>
<ul>
<li>A Slicer vtkMRMLMarkupsFiducialNode</li>
<li>A Slicer vtkMRMLModelNode which represents a spline around those points.</li>
</ul>
<p>We also observe the vtkCommand.Modified event from Slicer vtkMRMLSliceLogic, which checks to see if the Slice offset matches our “Segment” fiducial positions, and if the background volume for the Slice has been updated.</p>
<p>I was wondering if any of you could provide some feedback on what might be the major causes of the Slice views beginning to lag after several (10+) of our “Segment” objects have been added to the Slice view.</p>
<p>Thank you,</p>
<p>Jonathan Perdomo</p>

---

## Post #2 by @lassoan (2018-03-16 16:58 UTC)

<p>Which Slicer version  you are based on? Do you see performance is better if you use a regular Slicer main window instead of a slicelet? How big your segments are (you can find info on than in Data module or when you print the node).</p>

---

## Post #3 by @lassoan (2018-03-18 12:24 UTC)

<p>Do you use MarkupsToModel module (in MarkupsToModel extension) to create and update splines in real-time based on markup fiducial nodes? How many points do you have in each markups fiducial list? If you have more than 10-20 points in a curve then you should store points in a model node instead (it is hundreds or thousands time faster if you have many points). MarkupsToModel module can create curves from model points, too.</p>

---

## Post #4 by @jamesobutler (2018-03-18 18:40 UTC)

<p>I can provide at least some additional information as I work with Jon:</p>
<p>We’re running Slicer version 4.8.1.<br>
We have a function that gets the fiducial points from the vtkMRMLMarkupsFiducialNode, creates vtkPoints and set the points to a vtkParametricSpline object.  Usually there is not much more than 7 points per spline to create our “Segment” objects.</p>
<p>We’re primarily segmenting ellipsoidal shapes and using the segment editor cursor draw tool where you click and hold to freehand draw the region was too difficult to control with a regular mouse and the paint brush tool was too tedious.  That’s the primary reason for this different method for segmenting. After running fill between slices we can easily grab and move the location of a fiducial point if we’re not happy with it and run the interpolation again.<br>
Here is a <a href="https://youtu.be/FNgyVBT7WAg?t=38s" rel="nofollow noopener">video</a> from last year of the implementation</p>

---

## Post #5 by @lassoan (2018-03-18 21:03 UTC)

<p>The video looks nice! A couple of groups have been asking for spline-based drawing effect, so it would be good to offer it soon. I’m working on adding a new Markups curve widget, which will simplify things, as it’ll take care of curve generation.</p>
<p>If you don’t have too many markup points and generated curves don’t have high point count (they should not) then it is not clear why scrolling would be slowed down significantly. If the effect is only slows down slice browsing after 3D closed surface representation is created then maybe slicing of that model takes too much time? You could try to increase decimation factor in representation conversion settings. Is the effect available publicly so that we can test it? (public release would be nice anyway, otherwise it will have to be developed independently, from scratch) Have you tried performance profiling?</p>
<p>Have you tried the Surface cut effect (in SegmentEditorExtraEffects extension) you can drop points at the boundary on any number of slices and get a 3D shape immediately. A limitation is that it only works well for convex or slightly concave shapes.</p>
<p>When there is so visible contrast difference as in the demo video, <code>Grow from seeds</code> effect should work well, too. Maybe you can apply some noise filtering on the master volume and/or use <code>Watershed effect</code> to make the boundary smooth.</p>

---

## Post #6 by @jamesobutler (2018-03-18 22:59 UTC)

<p>It looks like we set the resolution of the vtkParametricFunctionSource to 2500 of u,v,w.  The code for this is within a private repo, but is a couple of python classes. We haven’t tried performance profiling yet.</p>
<p>I just tried the Surface Cut effect and must say this is really similar to what we’ve implemented. If it could have curves instead of straight lines between points that would be what we would want.  I do like how you can add additional points between other points and the boundary updates accordingly to use the new point.  Our implementation requires the points to be placed in order.</p>
<p>Using contrasts differences could potentially work in some volumes, but not a reliable option for many.  There are times where there will be bright reflections within our ROI which would mess that up or shadows from certain anatomical features that hides the true boundary in some areas.  We also segment the same tumor region based on blood vessel-only volumes. These type of volumes can be seen <a href="https://sonovol.com/technology/acoustic-angiography/" rel="nofollow noopener">here</a>.</p>

---

## Post #7 by @lassoan (2018-03-19 00:00 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="6" data-topic="2336">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>If it could have curves instead of straight lines</p>
</blockquote>
</aside>
<p>Points get connected using curved lines as soon as you you add points on more than one plane.</p>

---

## Post #8 by @jamesobutler (2018-03-19 02:40 UTC)

<p>oh wow, that’s actually really nice! Much better than doing 2D drawings in combination with the fill between slices effect.</p>

---
