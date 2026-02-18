# Subsample a 3D volume

**Topic ID**: 1692
**Date**: 2017-12-20
**URL**: https://discourse.slicer.org/t/subsample-a-3d-volume/1692

---

## Post #1 by @jonieva (2017-12-20 15:28 UTC)

<p>Hi guys,</p>
<p>I’m trying to subsample a 3D volume in a particular plane, while keeping the same spacing in the other two. I found an example of something similar here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.6/ScriptRepository#Thick_slab_reconstruction_and_maximum.2Fminimum_intensity_volume_projections" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.6/ScriptRepository#Thick_slab_reconstruction_and_maximum.2Fminimum_intensity_volume_projections</a></p>
<p>However, I don’t want to use any kind of projection/interpolation, just a simple subsampling setting a concrete spacing in one axis (axial plane).</p>
<p>Do you have any idea which would be the best way to achieve this?</p>
<p>Also, once that I use the sliceLogic, I don’t know how to reset the state (even when closing the scene, the volume is not displayed correctly in the used Window). What’s the right way to reset it?</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2017-12-20 16:25 UTC)

<p>Hi Jorge -</p>
<p>Maybe you can use this module [1] under Legacy-&gt;Filtering.  It gives you control over the spacing in the image planes and creates a new volume that you can save and restore.</p>
<p>[1] <a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/ResampleScalarVolume">https://www.slicer.org/wiki/Documentation/4.8/Modules/ResampleScalarVolume</a></p>
<p>HTH,<br>
Steve</p>

---

## Post #3 by @jonieva (2017-12-21 15:01 UTC)

<p>Hi Steve,</p>
<p>I don’t know the history of module to be under Legacy, but it worked like a charm. I hope it doesn’t get deprecated anytime soon <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Tx!</p>
<p>Jorge Onieva</p>

---

## Post #4 by @lassoan (2017-12-21 15:04 UTC)

<p>With non-deprecated modules, you would create an empty volume to specify spacing and extent and then use Crop Volume module or any of the image resample modules to conform the input module to that geometry.</p>

---

## Post #5 by @jonieva (2018-02-06 15:16 UTC)

<p>Hi guys,</p>
<p>As a follow up to this question, I have an issue with the visualization of the volume when the volume spacing is higher than the SliceWidget spacing. If I navigate the volume using keyboard arrows or mouse wheel, there is no problem.  But if I drag and drop in the slider on the top of the SliceWidget, I can get to “intermediate” slices where a merge between slices is displayed (see attached screenshot to show the effect).</p>
<p>I tried to manually set the SliceWidget offset using the SetSliceOffset function, but it doesn’t seem to have any effect when using drag and drop.</p>
<p>Is there any way to really force the SliceWidget minimum offset so that it matches the spacing of the displayed foreground volume?</p>
<p>Thank you</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54c906e41f9cb21ce705d5658e0a6b5afd533123.png" data-download-href="/uploads/short-url/c62NX7P8SlQzFzTpVZqzCo9SdgL.png?dl=1" title="04%20AM"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54c906e41f9cb21ce705d5658e0a6b5afd533123_2_690x485.png" alt="04%20AM" data-base62-sha1="c62NX7P8SlQzFzTpVZqzCo9SdgL" width="690" height="485" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54c906e41f9cb21ce705d5658e0a6b5afd533123_2_690x485.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54c906e41f9cb21ce705d5658e0a6b5afd533123.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54c906e41f9cb21ce705d5658e0a6b5afd533123.png 2x" data-dominant-color="514F4F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">04%20AM</span><span class="informations">1020×717 266 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2018-02-06 15:44 UTC)

<aside class="quote no-group" data-username="jonieva" data-post="5" data-topic="1692">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/91b2a8/48.png" class="avatar"> jonieva:</div>
<blockquote>
<p>volume spacing is higher than the SliceWidget spacing</p>
</blockquote>
</aside>
<p>Slice widget’s spacing is set by default to be the same as the voxel spacing along that axis (you can change from auto to a custom value in the slice controller widget). So, it seems that your problem is that using the slice offset slider you can make smaller steps.</p>
<p>I’m not sure how to solve this in general. Slicer does not enforce snapping to middle of a slice, as often there is no exact slice position (when there are multiple images with different geometries, or when slice view is not aligned with image axes) and you can move the slice to any position by shift + mouse move or when you jump to a markup that is not in the middle of a slice, etc.</p>
<p>You may implement a solution in your particular workflow: observe the slice node and whenever it is changed, update its position to snap to the middle of a slice of a specific volume. Instead of updating the position in the observer callback, probably you need to use a resettable timer with a timeout of a fraction of a second.</p>

---
