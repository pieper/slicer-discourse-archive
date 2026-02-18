# Copy contour to adjacent slices

**Topic ID**: 17239
**Date**: 2021-04-21
**URL**: https://discourse.slicer.org/t/copy-contour-to-adjacent-slices/17239

---

## Post #1 by @ferhue (2021-04-21 22:07 UTC)

<p>Hello,<br>
I was wondering what is the best way to exactly copy a contour from one slice to the adjacent one.</p>
<p>I would find such a plugin or feature useful when I am designing 3D printed supports for phantoms. This would allow me to adjust the wall thickness of the 3D printed part in later iterations directly on the CT / RTstruct.</p>
<p>Any workflow ideas?</p>
<p>See also this closed feature request: <a href="https://github.com/Slicer/Slicer/issues/5604" class="inline-onebox" rel="noopener nofollow ugc">Segment editor, copy contour to adjacent slice · Issue #5604 · Slicer/Slicer · GitHub</a></p>

---

## Post #2 by @lassoan (2021-04-25 15:38 UTC)

<p>The title and description of this topic may be misleading. Copy from neighbor slices should not be necessary for segmentation and it seems that people are not interested in doing this. However, according to the last comment in the referenced issue, your goal is to create support structure for 3D printing.</p>
<p>If you want to get ideas about how to create support structure for 3D printing in Slicer then I would recommend to create a new topic about this.</p>

---

## Post #3 by @ferhue (2021-04-26 09:52 UTC)

<p>I want to use it for 3D printing, but I do not think the feature is necessarily restricted to 3D printing.</p>
<p>Imagine I have a CT dicom directory of a QA phantom, usually a water phantom (1mm x 1mm x 1mm voxels) with an old RTstruct defining a “target” area (rectangular) that is a 3cm x 3cm x 2 cm cube.</p>
<p>Now, I import both CT and RTstruct into 3D slicer. I would like now to extend the target on the Slice-axis for irradiation, so that it is 3cm x 3cm x 3cm. Using CTRL+C on the last slice and CTRL+V on adjacent slices would be the fastest way to achieve this, as I used to do in MIM. Or a “Fill between slices feature with an extrapolate checkbox”.</p>

---

## Post #4 by @lassoan (2021-04-26 13:54 UTC)

<p>Fill between slices and interpolation is good and safe for segmentation. Some amount of extrapolation could be good, too. However, blind copy-paste would be harmful as a segmentation tool (it would deteriorate segmentation quality by introducing very significant bias) and would be a very poor modeling tool. We try to avoid spending time with implementing, maintaining, and supporting tools that are of very limited use and/or may lead to suboptimal results.</p>
<aside class="quote no-group" data-username="ferhue" data-post="3" data-topic="17239">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/c0e974/48.png" class="avatar"> ferhue:</div>
<blockquote>
<p>I import both CT and RTstruct into 3D slicer. I would like now to extend the target on the Slice-axis for irradiation, so that it is 3cm x 3cm x 3cm. Using CTRL+C on the last slice and CTRL+V on adjacent slices would be the fastest way to achieve this</p>
</blockquote>
</aside>
<p>Copy-paste would cause bias here, too. If the user extends the margin along an image axis direction (instead of the optimal anatomical direction) for convenience that is not good.</p>
<p>Instead, you can use Margin effect for extending the margin. It can be combined with masking features and Scissors or Paint effect to restrict margin in certain directions or areas. It may take a few more clicks than choosing one of the image axis directions, but if there is a common operation that requires extra clicks then you can create a new scripted Segment Editor effect that works with the minimum amount of user inputs. We can help with creating such highly optimized, application-specific tools (it may require writing just 20-30 lines of Python code).</p>

---
