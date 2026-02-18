# When tracing tissues on MRI sometimes the segment goes past the desired layer onto the next level

**Topic ID**: 32566
**Date**: 2023-11-02
**URL**: https://discourse.slicer.org/t/when-tracing-tissues-on-mri-sometimes-the-segment-goes-past-the-desired-layer-onto-the-next-level/32566

---

## Post #1 by @Bryan (2023-11-02 20:45 UTC)

<p>I am tracing muscle and leg tissue with a 10 mm separation between each layer. Most of the time I have no issue of tracing the tissues and moving on to the next layer. Sometimes when I draw on one layer it continues to go to the next layer and doesn’t allowing for a new segment on that new layer. Any ideas of what I can change or do to not have this happen. In this example I created a midpoint and made 5 layers above and worked my way back to the midpoint. I had an Issue on the first and second layers after the midpoint but not the other 3.</p>
<p>Windows 11 Pro<br>
version 22H2<br>
build 22621.2428<br>
3D Slicer version 5.4.0</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b56ffde0c3293bfb370dfd7ad33b94653dcaf572.jpeg" data-download-href="/uploads/short-url/pT4mwt1TsO7G9eQ5BOYJmXkNuzE.jpeg?dl=1" title="Screenshot 2023-11-02 113104" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b56ffde0c3293bfb370dfd7ad33b94653dcaf572_2_690x433.jpeg" alt="Screenshot 2023-11-02 113104" data-base62-sha1="pT4mwt1TsO7G9eQ5BOYJmXkNuzE" width="690" height="433" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b56ffde0c3293bfb370dfd7ad33b94653dcaf572_2_690x433.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b56ffde0c3293bfb370dfd7ad33b94653dcaf572_2_1035x649.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b56ffde0c3293bfb370dfd7ad33b94653dcaf572_2_1380x866.jpeg 2x" data-dominant-color="888C8E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-11-02 113104</span><span class="informations">1920×1207 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8957a1eaa22d772f52787634255d14571f616b85.jpeg" data-download-href="/uploads/short-url/jAZaeYTJ0WObTDSYIHYaRaFqBdb.jpeg?dl=1" title="Screenshot 2023-11-02 113032" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/8957a1eaa22d772f52787634255d14571f616b85_2_690x436.jpeg" alt="Screenshot 2023-11-02 113032" data-base62-sha1="jAZaeYTJ0WObTDSYIHYaRaFqBdb" width="690" height="436" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/8957a1eaa22d772f52787634255d14571f616b85_2_690x436.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/8957a1eaa22d772f52787634255d14571f616b85_2_1035x654.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/8957a1eaa22d772f52787634255d14571f616b85_2_1380x872.jpeg 2x" data-dominant-color="878C8E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-11-02 113032</span><span class="informations">1920×1215 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-11-03 00:18 UTC)

<p>If you cannot paint independently on each slice of the background volume then most likely the geometry (origin, spacing, axis directions) of the segmentation is not the same as the background volume’s geometry. You can use the “Specify geometry” button to resample the segmentation to match the source volume’s geometry.</p>
<p>Note that it is very unusal and probably unnecessary to create a new segment for each slice. If you use the same segment for the same structure on different slices then that makes things much simpler. You can also create a full 3D segmentation from a couple of slices using the “Fill between slices” effect.</p>

---
