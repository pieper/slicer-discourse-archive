# Adjust segmentation transparency of orthoslices and volumes independently for better contrast in 3d view

**Topic ID**: 44653
**Date**: 2025-10-02
**URL**: https://discourse.slicer.org/t/adjust-segmentation-transparency-of-orthoslices-and-volumes-independently-for-better-contrast-in-3d-view/44653

---

## Post #1 by @sulli419 (2025-10-02 22:10 UTC)

<p>When you select the “eye” to show an orthogonal slice in the 3D view, in the 3d viewer, it would nice if the segmentations could be shown as solid colors and the 3D segment volume could be translucent.  This would give a sense of how the 2d segmentation fits relative to the volume.  It seems like all the changes to transparency change the orthoslices <em><strong>and</strong></em> the 3d view at the same time.</p>
<p>Another way to state this: Adjust segmentation transparency of orthoslices and volumes independently for better contrast in 3d view.</p>
<p>Maybe this can be done?</p>
<p>Thanks,<br>
Steve</p>

---

## Post #2 by @mikebind (2025-10-03 19:06 UTC)

<p>I’m not sure I understand exactly what you are requesting.  In the Segmentations module, it is possible to independently control many aspects of opacity of segmentation elements, including independently controlling the opacity of the 3D surface representation and the Slice Fill opacity.  What you are asking for seems like it might correspond to making the Slice Fill opacity 1 and making the 3D opacity less than 1.   If you try that, what is not how you want it?</p>

---

## Post #3 by @sulli419 (2025-10-03 19:23 UTC)

<p>Apologies, this is hard to explain.  I have the 2d orthoslices displayed in the 3d viewer (by clicking the eye in the 2d viewer).  The 3d viewer opacity also adjusts the intensity of the ortho planes.  It would be convenient to see the otho planes as solid and then reduce the opacity of the 3d volume.  Hope that makes sense.  But maybe what I’m saying is possible (I have a version from ~5 months ago).</p>

---

## Post #4 by @mikebind (2025-10-03 19:51 UTC)

<p>Ah, I understand now.  And, in experimenting just now, I found out that things don’t work exactly as I thought they did in Slicer.  In fact, what appears to be happening is that there is no representation of the segmentation on the 2D slices shown in the 3D view at all. So, all you see is the transparent 3D representation intersecting the 2D orthoslice shown in 3D. Since only the 3D representation is there, the transparency you see is controlled entirely by the 3D segmentation opacity setting, as you were observing.  I was able to verify that there is no segmentation showing on the 2D slice in 3D at all by applying a clipping node to the segmentation which cut away half of the 3D view of my segment.  With that cut away, I could see that there is nothing on the orthoslice itself representing the segmentation.  So, with that understanding, I think that the feature you are requesting is actually to have the option to have the 2D representation of the segment (as it appears in the slice viewers) also appear when you show that slice in the 3D view. I do not see a way that that is possible currently in Slicer.</p>
<p>As a possible workaround, blended labelmaps are shown on the slice view, so you could export your segment to a labelmap, show that labelmap in your slice view, and that will show up on the 3D version of that orthoslice (I’m 95% sure that will work).  That is likely too cumbersome for interactive work, but if you wanted this feature for a presentation or a published figure, this would be one way to accomplish it.</p>

---

## Post #5 by @sulli419 (2025-10-04 19:40 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="4" data-topic="44653">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>I think that the feature you are requesting is actually to have the option to have the 2D representation of the segment (as it appears in the slice viewers) also appear when you show that slice in the 3D view.</p>
</blockquote>
</aside>
<p>Yes, this would be a nice (hopefully simple) way to achieve what I’m after.</p>
<p>Does your alternative approach involve volume rendering of the labelmap?  This has worked for me in the past, but it is less ideal and prone to error/drift as you fiddle with the controls.</p>

---

## Post #6 by @lassoan (2025-10-04 20:32 UTC)

<p>You can display a labelmap volume both as slice intersection and volume rendering in 3D. This could be implemented for segmentations, too. It was just not needed for any project that funded Slicer core development. Probably it was not needed because during segmentation the current visualization options are sufficient; and after the segmentation is finished you can easily convert to labelmap and add all the labelmap-based visualizations.</p>

---
