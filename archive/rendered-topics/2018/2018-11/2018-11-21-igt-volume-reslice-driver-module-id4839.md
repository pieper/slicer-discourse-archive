# IGT Volume Reslice Driver Module

**Topic ID**: 4839
**Date**: 2018-11-21
**URL**: https://discourse.slicer.org/t/igt-volume-reslice-driver-module/4839

---

## Post #1 by @sfrisken (2018-11-21 18:11 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.9.0<br>
Expected behavior: Volume Reslice Driver should apply a specified transform (driver) to reslice the views of the current volume and present the slices in the Red, Yellow and Green windows as specified in the module.</p>
<p>Preamble: I have been trying to use the driver logic in a custom module but have been trouble getting the views I expect. Thus, I revisited the IGT Volume Reslice Driver module to try to better understand its behavior.</p>
<p>Actual behavior:</p>
<ol>
<li>
<p>load a volume and view the axial (red), sagittal (yellow) and coronal (green) sections in 4-up mode</p>
</li>
<li>
<p>create a linear transform, “Reslice” and set it to the identity matrix</p>
</li>
<li>
<p>Go to the IGT/Volume Reslice Driver Module. For each view, set the driver to Reslice and the mode to Axial, Sagittal and Coronal for the red, yellow and green views. Expected behavior: the views should not change or, at most, views should be the same as before after re-centering. Actual behavior: The slices are flipped and/or rotated in various ways. I can fix this by editing the images using flipping and rotating in the Advanced options, but not by editing the Reslice transform. Notably, using sliders to rotate Relice does not change the slices at all.</p>
</li>
</ol>
<p>3B) The same thing happens when the modes are set to Transverse, Inline and Inline 90, but the flipping/rotating is different when Reslice is set to the identity transform.</p>
<ol start="4">
<li>
<p>For each view, reset the driver to None. Expected behavior: the view should revert to the original views. Instead, they stay flipped/rotated, even after re-centering the views.</p>
</li>
<li>
<p>Inconsistent behavior. Expected: I should get the same behavior every time I try this. Instead, the behavior seems to be state dependent. For example if I edit Reslice and then reset it to the identity, sometimes all slices return to the original state (before opening Reslice Driver). Sometimes not.</p>
</li>
</ol>
<p>I don’t know if the problem is with my expectations but it seems reasonable that driving reslicing with the identity transform and/or with no transform (None) should do nothing. Since that does not seem to be the case, it would be very helpful if one of the original contributors could add a written description of the expected behavior in the Help section of the Module and/or in the code.</p>
<p>Many thanks!</p>

---

## Post #2 by @lassoan (2018-11-21 19:09 UTC)

<aside class="quote no-group" data-username="sfrisken" data-post="1" data-topic="4839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/838e76/48.png" class="avatar"> sfrisken:</div>
<blockquote>
<p>Go to the IGT/Volume Reslice Driver Module. For each view, set the driver to Reslice and the mode to Axial, Sagittal and Coronal for the red, yellow and green views. Expected behavior: the views should not change or, at most, views should be the same as before after re-centering. Actual behavior: The slices are flipped and/or rotated in various ways. I can fix this by editing the images using flipping and rotating in the Advanced options, but not by editing the Reslice transform. Notably, using sliders to rotate Relice does not change the slices at all.</p>
</blockquote>
</aside>
<p>Identity matrix means position of (0,0,0) and orientation of (x,y,z) = (r,a,s). Using this transform as driver is expected to move the slices to (0,0,0) position. Most probably the slices they were not in the origin already (by default they are in the center of the volume), so they are expected to move.</p>
<p>The slices are flipped and/or rotated in various ways because there has to be a default of how to orient/flip the images. You can use flip and rotation setting to get any orientation you need. Never edit (translate/rotate) images if you just want to adjust how they appear in slice views (just keep them in anatomically correct orientation).</p>
<p>Axial/Sagittal/Coronal driving modes ignore the transform’s orientation component, so don’t expect transform rotation sliders to have any effect in these modes.</p>
<aside class="quote no-group" data-username="sfrisken" data-post="1" data-topic="4839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/838e76/48.png" class="avatar"> sfrisken:</div>
<blockquote>
<p>For each view, reset the driver to None. Expected behavior: the view should revert to the original views. Instead, they stay flipped/rotated, even after re-centering the views.</p>
</blockquote>
</aside>
<p>There is no such thing as “original view”, there is just the current state. You can change the current state by moving the slice offset slider, using the reformat widget, using volume reslice driver, choosing a slice orientation preset (axial, sagittal, coronal, …).</p>
<aside class="quote no-group" data-username="sfrisken" data-post="1" data-topic="4839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/838e76/48.png" class="avatar"> sfrisken:</div>
<blockquote>
<p>Inconsistent behavior. Expected: I should get the same behavior every time I try this. Instead, the behavior seems to be state dependent. For example if I edit Reslice and then reset it to the identity, sometimes all slices return to the original state (before opening Reslice Driver). Sometimes not.</p>
</blockquote>
</aside>
<p>There is no “original state”, so if the modified state happens to be the same as some previous state then it is a coincidence. Volume Reslice Driver changes SliceToRAS transform, while if you manually pan/zoom a slice view, you adjust SliceToXY transform. What you see on the screen is the combination of both transforms (XYToRAS). This is an extremely useful feature, as it allows you to zoom in and pan a slice view that is driven by a transform, but I can see that it may not be obvious how this feature works and what are the consequences. I think SliceToXY is reset when you click “Fit to slice”. You can use “Node info” module (in DebuggingTools extension) to see how these transform changes as you interact with the view (for example, choose “Input node”: Red, then click “Show node information window”; then look at XYZOrigin, FieldOfView, SliceToRAS, and XYToRAS properties).</p>
<aside class="quote no-group" data-username="sfrisken" data-post="1" data-topic="4839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/838e76/48.png" class="avatar"> sfrisken:</div>
<blockquote>
<p>I don’t know if the problem is with my expectations but it seems reasonable that driving reslicing with the identity transform and/or with no transform (None) should do nothing.</p>
</blockquote>
</aside>
<p>I’ve been using Volume reslice driver for long enough that to me it works as I expect, so it is not easy to figure out what would need documentation. If my explanations above helped then it would be great if you could add information to the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/VolumeResliceDriver">module’s documentation page</a> that you think would have been useful for you (and could help future users and developers). Thank you!</p>

---
