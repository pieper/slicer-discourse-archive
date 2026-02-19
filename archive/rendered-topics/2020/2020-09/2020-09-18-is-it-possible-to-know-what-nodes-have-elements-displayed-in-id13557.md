---
topic_id: 13557
title: "Is It Possible To Know What Nodes Have Elements Displayed In"
date: 2020-09-18
url: https://discourse.slicer.org/t/13557
---

# Is it possible to know what nodes have elements displayed in a slice view? And where?

**Topic ID**: 13557
**Date**: 2020-09-18
**URL**: https://discourse.slicer.org/t/is-it-possible-to-know-what-nodes-have-elements-displayed-in-a-slice-view-and-where/13557

---

## Post #1 by @mikebind (2020-09-18 23:29 UTC)

<p>I would like to know programmatically what scene elements are currently visible in a slice view.  Is there a way to find this out?  In a typical slice view, I might have MarkupsCurves which are in the plane of the slice or passing through the slice, and I might have models which have a 2D intersection with the slice.  For a given slice view, I would like to know how to find out which models are currently visible in that slice (as 2D intersections) and which curves are in or passing through the displayed slice.  Even better would be if I knew where in the slice view they were (so that I could add a label nearby if I wished), but I think I could manage to figure out where each element was if I knew that it was shown somewhere. Slicer is obviously figuring all this out in order to create the slice view we see; I was hopeful that I could piggy-back off that knowledge rather than trying to figure it out on my own in an assuredly less efficient manner.</p>

---

## Post #2 by @pieper (2020-09-19 14:52 UTC)

<p>Information about model slice intersections and whether they are within the clipping range of the current view parameters is handled by the MRML Displayable Mangers and ultimately some is done by the VTK rendering pipeline or even in the GPU itself, so as a general matter it’s not recorded or accessible to the application.  I agree it would be good to make that information available wherever feasible, perhaps by making some of the intermediate calculation data available via an api  or by providing a way to probe the views for that kind of information.  It would be important not to add overhead to the core rendering.</p>

---

## Post #3 by @mikebind (2020-09-21 21:52 UTC)

<p>Thanks for the information.  It sounds like for now I’m on my own for generating or extracting this information.  If I figure something helpful out, I’ll post here.  Thanks for pointing me in an initial direction!</p>

---

## Post #4 by @lassoan (2020-09-21 22:01 UTC)

<p><a class="mention" href="/u/mikebind">@mikebind</a> What is your overall goal?</p>

---

## Post #5 by @mikebind (2020-09-22 05:08 UTC)

<p>One of the applications I work in is imaging for stereotactically placed depth electrodes for epilepsy (SEEG).  One of the goals for the clinicians I work with is to thoroughly understand the 3D relationships between electrode contact locations and brain anatomy, as well as electrode contact locations with each other. Depth electrodes can be positioned more or less arbitrarily with respect to the brain and with respect to each other, and it can be challenging to find good ways to assist understanding what is present in a particular slice view.  For example, a sagittal slice through a brain might have several electrodes crossing through it at different locations and at different angles.  Some might have electrically sensitive contacts (which for me are represented as control points for a MarkupsCurve) in the viewed slice plane, whereas for others the slice plane might be between contacts (so no control point is visible, just the curve line).</p>
<p>In a particular view, it would be helpful if I could turn on a label which identified each element in the slice view (e.g. each electrode name, and possibly which contact number the slice plane is nearest).  I have experimented with distinguishing  the electrodes via color, but it is difficult to find a set of colors which are readily separable by eye as well as visible against any grayscale background image.  Also, while there might be 20 different electrodes, a typical view of interest might contain only 3-5, so a list of labels or a key in one corner might be feasible.</p>
<p>In addition to markups curves I have also experimented with cylinder or tube models along the electrode trajectory.  These provide a consistent visualization of the intersection with the slice view without the out of plane fading behavior of the markups curves (which can be helpful or can be distracting). However, while I can label control points of markups curves, I don’t know of any way to have a label show for a model intersection on a slice view.  In the 3D view I can add a markups fiducial point with the label I want and just make the point size 0, but to get that to work in a slice view I would need to know where to position that point, and more fundamentally, whether I need that label for that particular view (depending on whether the model appears in that slice).</p>

---

## Post #6 by @pieper (2020-09-22 12:18 UTC)

<p>Thanks for the extra info, that does make sense.  There are definitely ways to accomplish what you describe, but it sounds like a bit of work to make a clean and efficient implementation.  I did something like this years ago with a custom rendering pass into an off-screen buffer so that I got object ids and triangle ids per pixel, so you could easily identify how arbitrary geometry was rasterized.  I haven’t looked, but something like this may be built into some part of the latest VTK.  Such an image could be post-processed to generate a set of labels on the slice.  A lot will depend on how much time you have to invest in exploring this.</p>

---

## Post #7 by @lassoan (2020-09-22 12:49 UTC)

<p>If you import electrode model into segmentation then you can see the name of the electrode in the Data Probe window (lower-left corner) when you move the crosshair over it (Shift+MouseMove). You could do the same in 3D view with a short script (see example script in <a href="https://discourse.slicer.org/t/obtaining-segmentations-for-fiducials/13407/30">this topic</a>). You could also write a short script for highlighting the segment in all views (temporarily changing its override color in the display node) and displaying the text next to it (by adding a temporary markups fiducial node and set its label to the name of the segment).</p>
<aside class="quote no-group" data-username="mikebind" data-post="5" data-topic="13557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>These provide a consistent visualization of the intersection with the slice view without the out of plane fading behavior of the markups curves</p>
</blockquote>
</aside>
<p>You can enable projection and the same distance-encoded coloring for model nodes: Models module / Display / Mode → Distance encoded projection. By editing the color table, you can set arbitrary fadeout and/or color change behavior.</p>
<aside class="quote no-group" data-username="mikebind" data-post="5" data-topic="13557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>I don’t know of any way to have a label show for a model intersection on a slice view.</p>
</blockquote>
</aside>
<p>Line/plane intersection position is a very simple computation and once you have that position, you can see if it is in the slice view’s region (something like this: transform it to the slice’s coordinate system by applying inv(XYToRAS) transform and see if its XY coordinates are within FieldOfView size and Z is within slice thickness).</p>
<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="13557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I did something like this years ago with a custom rendering pass into an off-screen buffer so that I got object ids and triangle ids per pixel, so you could easily identify how arbitrary geometry was rasterized. I haven’t looked, but something like this may be built into some part of the latest VTK. Such an image could be post-processed to generate a set of labels on the slice.</p>
</blockquote>
</aside>
<p>This would be useful as a general solution, and I think VTK hardware pickers (e.g., vtkPropPicker) provide this. SEEG case is a simple special case, as electrodes can be modeled as points or cylinders (lines), so it is trivial to compute intersection position with a plane.</p>

---

## Post #8 by @mikebind (2020-09-22 19:52 UTC)

<p>Thanks, these are good thoughts.  The segmentation hover approach may be good enough for the clinicians I can get to use Slicer.  For the rest, I am often generating a set of screen captures to illustrate views and answer questions.  Automatically generated labels would be a large time-saver for me in that process.  In general, I don’t need these labels generated or updated in real time, rather if they could be generated on request within a few seconds that would be high enough performance for my purposes.</p>
<p>Could I generate the segmentation volume with electrode labels as Andras suggests, and then obtain essentially the slice of the segmentation volume as a 2D array?   That would let me obtain essentially a 2D labelmap for the view.  A quick scan of the values would tell me what segments were visible in that view (and a quick analysis (e.g. segment centroid) would tell me where).  Is this something which is relatively easily obtainable? The slice through a labelmap or segmentation volume which corresponds with the viewport (if that’s the right term) of a slice view?  I will definitely sometimes be doing these in slices which are not aligned with the voxel grid (either because the anatomical axes are not aligned with the voxel grid or because I am working with an oblique reformat slice).</p>

---

## Post #9 by @lassoan (2020-09-22 20:09 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="8" data-topic="13557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>Could I generate the segmentation volume with electrode labels as Andras suggests, and then obtain essentially the slice of the segmentation volume as a 2D array?</p>
</blockquote>
</aside>
<p>Yes, this should be no problem. You write a script that iterates through the slices, add labels, and captures a screenshot of the view.</p>
<aside class="quote no-group" data-username="mikebind" data-post="8" data-topic="13557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>Automatically generated labels would be a large time-saver for me in that process.</p>
</blockquote>
</aside>
<p>Placing labels in the middle of a target (e.g, intersection point of an electrode and a slice) should be easy. The complication starts when you want to add callouts because then you need to arrange all the callouts so that they don’t overlap.</p>
<aside class="quote no-group" data-username="mikebind" data-post="8" data-topic="13557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>Could I generate the segmentation volume with electrode labels as Andras suggests, and then obtain essentially the slice of the segmentation volume as a 2D array?</p>
</blockquote>
</aside>
<p>Segmentation does this automatically. You can create your electrodes as models and import them into a segmentation node.</p>
<aside class="quote no-group" data-username="mikebind" data-post="8" data-topic="13557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>A quick scan of the values would tell me what segments were visible in that view (and a quick analysis (e.g. segment centroid) would tell me where). Is this something which is relatively easily obtainable?</p>
</blockquote>
</aside>
<p>Since tube/plane intersection is so easy to compute, I would just go that route (no need to analyze images). But you can certainly do it using image processing, too (export segmentation to labelmap, get the resliced labelmap as shown <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_reformatted_image_from_a_slice_viewer_as_numpy_array">here</a> and analyze the image).</p>
<p>In the long term, such auto-labeling will be part of Slicer core, driven by OpenAnatomy and other projects.</p>

---

## Post #10 by @Saima (2021-10-12 05:32 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="13557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>such auto-labeling will be part of Slicer core,</p>
</blockquote>
</aside>
<p>Hi Andras,<br>
Could it be possible to show labels of segmentation on the slice views. I used fiducials to show the segments and placed fiducials at the center of the segment. It shows the fiducials only in corresponding slice. would it be possible to have a label in red yellow and green window on the segments.</p>
<p>Regards,<br>
Saima Safdar</p>

---
