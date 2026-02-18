# Quantifying adjacent/touching segmentations-areas

**Topic ID**: 26477
**Date**: 2022-11-28
**URL**: https://discourse.slicer.org/t/quantifying-adjacent-touching-segmentations-areas/26477

---

## Post #1 by @JonatanS (2022-11-28 13:13 UTC)

<p>Hi all,</p>
<p>I need some assistance regarding quantifying the surface areas of my segmentations. I have several segmentations of structures in close proximity and in certain places physical contact with oneanother. Is there a way to quantify the area where 2 segmentations meet? What I want is to be able to say is how many percent of segment A´s area is in contact with the surface of segment B and C.<br>
NOTE: They do not overlap nor intersect, they are segmented to respect borders. I am no programmer and a very new 3D-slicer user, if there is a solution not requiring coding please let me know.<br>
Thank you in advance.</p>

---

## Post #2 by @mikebind (2022-11-28 16:34 UTC)

<p>I am not aware of a Slicer tool which will give you this exact answer.  However, I can suggest a solution which will give you an approximate answer which may be usable for you and which does not require any coding.</p>
<ul>
<li>Make a copy of segment A (Logical operators → Copy in segment editor).</li>
<li>Expand the segment A copy (Margin–&gt; Grow, by 1 voxel in each dimension).  Be sure that the Masking Settings are set to allow overlap, or else this operation will overwrite the original Segment A and the areas of B and C that it expands into.</li>
<li>Subtract the original segment A from the expanded copy (Logical operators → Subtract), leaving just the new expanded shell.  We are going to quantify the fraction of this shell which is inside B or inside C, which should be a pretty decent proxy for the fraction of surface area is in contact with each.</li>
<li>Make two additional copies of the segment A expanded shell (create new segment, Logical operators → copy, repeat). On the first copy, find the intersection with segment B (Logical operators → Intersect); on the second, find the intersection with segment C.</li>
<li>Open the Segment Statistics module.  Select your segmentation as the Segmentation input. In the Advanced section, uncheck “Scalar Volume Statistics” and “Closed Surface Statistics”.  Click the Apply button.  A table will appear with the volumes of all the visible segments of your segmentation.  Compare the values for the expanded shell with the values for the shell intersections.</li>
</ul>
<p>These volume ratios are not exactly the same as a ratio of surface areas, but it does capture basically the same idea in a straightforward to understand and calculate way.  Surface area of contact is also not going to have a single unambiguous method of calculation: for example, are the surfaces smoothed in any way, or are you adding up the areas of flat voxel faces which are in contact?  The resolution of the imaging and the roughness of the segment surfaces at that resolution are going to have effects which will change the resulting surface area ratios in small ways depending on the method of calculation.</p>

---

## Post #3 by @lassoan (2022-11-29 03:32 UTC)

<p>This is a very nice solution for highlighting adjacent regions. For measuring surface, you can export the segments to models, use ModelToModelDistance extension to compute distance, and use thresholding to preserve parts of the model that are very close to the other model.</p>
<p>Thresholding is not available on the GUI, but all you need to do is to copy-paste this into the Python console after you computed the distance (I hope you don’t consider this as “programming”):</p>
<pre><code class="lang-python">modelWithDistance = getNode('VTK Output File')
maximumDistance = 2.0

threshold = vtk.vtkThreshold()
threshold.SetInputConnection(modelWithDistance.GetPolyDataConnection())
threshold.SetThresholdFunction(threshold.THRESHOLD_LOWER)
threshold.SetLowerThreshold(maximumDistance)
surface = vtk.vtkGeometryFilter()
surface.SetInputConnection(threshold.GetOutputPort())
thresholdedModel = slicer.modules.models.logic().AddModel(surface.GetOutputPort())
</code></pre>

---

## Post #4 by @JonatanS (2022-11-30 10:50 UTC)

<p>Thank you for your help! It worked really well for getting an approximation of the ratio between segment B and C and their surface-interaction with segment A. However, since the surface-value that I get is both the “top” and “bottom” of the shape, it is not only the surface-to-surface area with segment A that I get. The method is by no means useless, having the ration between segment B and C is great, but the actual value in square-millimeters is not representative of the physical strucutre.<br>
Do you have a suggestion for this? If not, that fine, the aformentioned method works well!</p>
<p>Best regards</p>

---

## Post #5 by @lassoan (2022-11-30 22:29 UTC)

<aside class="quote no-group" data-username="JonatanS" data-post="4" data-topic="26477">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/74df32/48.png" class="avatar"> JonatanS:</div>
<blockquote>
<p>Thank you for your help! It worked really well for getting an approximation of the ratio between segment B and C and their surface-interaction with segment A. However, since the surface-value that I get is both the “top” and “bottom” of the shape,</p>
</blockquote>
</aside>
<p>If you follow the first idea (based on margin effect) then you need to divide the surface area by 2.</p>
<p>If you follow the second idea (use model to model distance filter) then you directly get the contact surface only (not a 3D closed surface, just a surface patch).</p>
<p>The surface area you get in Models module / Information section is the correct physical surface area. If coordinate system unit of the segmentation is in millimeters (if you created the segmentation from clinical DICOM images then it is) then the surface area is in square millimeters.</p>

---

## Post #6 by @mikebind (2022-11-30 22:37 UTC)

<p>Instead of the surface area of the interaction regions, I imagined using the ratios of the volumes of these thin shells.  However, using 1/2 the surface area should also work well as approximations, and is a way to get numbers in square mm if you want the actual areas (approximately, of course). As long as the contact area much ‘wider’ than it is ‘thick’, the extra surface area due to the thickness of the shell volume should be pretty negligible.</p>

---

## Post #7 by @lassoan (2022-12-01 00:47 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="6" data-topic="26477">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>Instead of the surface area of the interaction regions, I imagined using the ratios of the volumes of these thin shells. However, using 1/2 the surface area should also work well as approximations,</p>
</blockquote>
</aside>
<p>Yes, dividing the volume by the thickness and dividing the surface area by 2 should be both approximately same as the contact surface area. They may be a bit less accurate than cutting out a surface patch by thresholding, because the surface thickness is not exactly zero and the surface thickness may not be exactly constant.</p>

---
