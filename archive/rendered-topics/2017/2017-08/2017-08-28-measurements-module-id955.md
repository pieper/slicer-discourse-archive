# Measurements Module

**Topic ID**: 955
**Date**: 2017-08-28
**URL**: https://discourse.slicer.org/t/measurements-module/955

---

## Post #1 by @CRS (2017-08-28 00:16 UTC)

<p>Hi guys, new to Slicer. Trying to figure the way to do a parameter or diameter measurement of a brain tumor. Is it even possible with Slicer?</p>
<p>Thanks</p>
<p>RS</p>

---

## Post #2 by @lassoan (2017-08-28 00:22 UTC)

<p>You can make simple 2D diameter measurements by placing a ruler (<a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/MainApplicationGUI#Mouse_Modes">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/MainApplicationGUI#Mouse_Modes</a>).</p>
<p>For volumetric measurements, segment the tumor using <a href="http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">Segment editor module</a>. You can segment well-visible brain tumors in a few minutes using Grow from seeds effect (you paint inside and outside the tumor in a few slices and Slicer creates a full 3D model automatically). Then, compute volume using Segment statistics volume.</p>

---

## Post #3 by @CRS (2017-08-28 11:45 UTC)

<p>Hi Andras,</p>
<p>Thanks. I think i’m getting it. Managed to get the ruler out but I’m not sure why the interface is always behind the segmentation? Unable to see the measurement<br>
On the other hand, managed to segment out the healthy segment from the fracture frontal bone ( Bone as Value :2 and fragment bone as background 0)  but it still appear once we go for render a new model.</p>
<p>The end result is to render out a remodel bone to cover the defect , I’m thinking of using GROW from Seed since there are some fragment which we can use as reference or is there a module like MIRROR Image?</p>
<p>Cheers</p>
<p>RS</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb573bb8169d194e2a69cb002bcbbe4a379d4eac.png" alt="image" data-base62-sha1="zRsJYoyXe9PFkzs1Aoj5rCAh3GY" width="628" height="480"></p>

---

## Post #4 by @lassoan (2017-08-28 15:58 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-edit-stl-file/960">How to edit STL file</a></p>

---

## Post #5 by @lassoan (2017-08-31 05:22 UTC)

<aside class="quote no-group" data-username="CRS" data-post="3" data-topic="955">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/977dab/48.png" class="avatar"> CRS:</div>
<blockquote>
<p>I’m not sure why the interface is always behind the segmentation?</p>
</blockquote>
</aside>
<p>Ruler is a straight line in 3D. If any other structure is in front of that line, the line will not be visible. You can go to <code>Segmentations</code> module to temporarily hide the 3D representation or make it semi-transparent.</p>
<aside class="quote no-group" data-username="CRS" data-post="3" data-topic="955">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/977dab/48.png" class="avatar"> CRS:</div>
<blockquote>
<p>managed to segment out the healthy segment from the fracture frontal bone ( Bone as Value :2 and fragment bone as background 0)  but it still appear once we go for render a new model.</p>
</blockquote>
</aside>
<p>If you want to remove a region from a volume (by filling it with some background value), then use <code>Mask volume</code> effect (install <code>SegmentEditorExtraEffects</code> extension to get it).</p>
<aside class="quote no-group" data-username="CRS" data-post="3" data-topic="955">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/977dab/48.png" class="avatar"> CRS:</div>
<blockquote>
<p>is there a module like MIRROR Image</p>
</blockquote>
</aside>
<p>You can mirror a node by using <code>Transforms</code> module. Simply create a transform where one of the values in the diagonal is set from the original <code>1.0</code> to <code>-1.0</code>. Then apply and harden this transform on the node. After this you have to register the mirrored node to the original image - you can do that by using landmark-based registration, for example <code>Fiducial registration wizard</code> module in <code>SlicerIGT</code> extension.</p>

---
