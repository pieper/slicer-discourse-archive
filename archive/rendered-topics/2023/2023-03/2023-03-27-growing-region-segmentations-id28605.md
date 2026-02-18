# Growing Region Segmentations

**Topic ID**: 28605
**Date**: 2023-03-27
**URL**: https://discourse.slicer.org/t/growing-region-segmentations/28605

---

## Post #1 by @nysfour (2023-03-27 21:44 UTC)

<p>Is there a method for essentially ‘corralling’ a growing region segmentation? For example, if I want a dropped seed to expand throughout an anatomical region but I want to add a border so that the seed will not grow into the next region. Is there any way to do this? Thresholding has not always been sufficient, especially with nonuniform lighting.</p>

---

## Post #2 by @pieper (2023-03-27 22:07 UTC)

<p>You could try using the grow from seeds tool for this.</p>

---

## Post #3 by @lassoan (2023-03-28 02:07 UTC)

<p>Yes, the grow from seeds supports this, as it respects masking settings. For example, you can choose “Editable area” → “Inside …” (where the chosen segment covers the entire region where growing is allowed).</p>

---

## Post #4 by @nysfour (2023-06-08 19:40 UTC)

<p>Where is the editable area module? Sorry for the late reply, I appreciate the help!</p>

---

## Post #5 by @jamesobutler (2023-06-08 21:14 UTC)

<p>Editable area is part of the masking options in the Segment Editor. See the link below to the documentation for more details:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#masking-options" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#masking-options</a></p>

---

## Post #6 by @rbumm (2023-06-08 21:17 UTC)

<p>The editatble area can be selected here:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d119cba8177f34a3a9e268be3ccc60bf65ce906.jpeg" data-download-href="/uploads/short-url/mpuHcLy4LIbjoIXKfzQgoWcAkyq.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d119cba8177f34a3a9e268be3ccc60bf65ce906_2_690x477.jpeg" alt="image" data-base62-sha1="mpuHcLy4LIbjoIXKfzQgoWcAkyq" width="690" height="477" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d119cba8177f34a3a9e268be3ccc60bf65ce906_2_690x477.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d119cba8177f34a3a9e268be3ccc60bf65ce906_2_1035x715.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d119cba8177f34a3a9e268be3ccc60bf65ce906.jpeg 2x" data-dominant-color="BBBCB9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1111×769 197 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @nysfour (2023-06-09 14:19 UTC)

<p>How do I use this setting when inside the growing seeds module? I can only find that setting in the Segment Editor module, but I am trying to delimit the area the seeds can grow in to before I place them</p>

---

## Post #8 by @rbumm (2023-06-09 14:36 UTC)

<p>You would need to create an additional segment that just contains the area of interest.<br>
Example: We create lung masks, combine them to “lungs” segment, then choose “inside lungs” in Grow from seeds or Local threshold in order to segment a tumor.</p>

---

## Post #9 by @nysfour (2023-06-09 16:01 UTC)

<p>I seem to be unable to open both modules at the same time</p>

---

## Post #10 by @rbumm (2023-06-09 16:42 UTC)

<p>You must just create one more segment which defines “outside” or “outerborder” in Grow from seeds. This will automatically be blended out  (unchecked) when you have pressed “Apply”.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a7c28ff6b2760eaceaa8ea6b638bcb0a9feb8e6.png" alt="image" data-base62-sha1="jL5TYp76jaAxDP3GS0OkLBUXD6e" width="495" height="139"></p>
<p><a href="https://www.youtube.com/watch?v=9iiOBmaP8bA">See a video example here</a>.</p>

---

## Post #11 by @nysfour (2023-06-09 18:06 UTC)

<p>Thank you! How do I open both modules in split screen like you have in your image sent a few messages earlier?</p>

---

## Post #12 by @rbumm (2023-06-09 18:30 UTC)

<p>Please explain. What do you mean by split screen?</p>

---

## Post #13 by @nysfour (2023-06-09 19:47 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21a0876ac85dc640dea25e53771514823999cfa6.png" data-download-href="/uploads/short-url/4NtGFGtlxZQLyiDuD23ijBCglOS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21a0876ac85dc640dea25e53771514823999cfa6.png" alt="image" data-base62-sha1="4NtGFGtlxZQLyiDuD23ijBCglOS" width="538" height="500" data-dominant-color="F5F5F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">566×526 15.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
This is what my growing region module looks, even when I add seeds, it doesn’t show the segment editor</p>

---

## Post #14 by @rbumm (2023-06-09 20:18 UTC)

<p>Please use 3D Slicer 5.22 stable and the module “Segment Editor”.<br>
Create your segments. Do not forget to add the “outer” to “outbound” segment, which will generate the ROI you were describing.</p>
<p>Click “Grow from Seeds” effect.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3f2174fd11d8e920a556566ad712e933496d2c4.png" data-download-href="/uploads/short-url/ueXqhKseS4d7lon7lZzMyKIH820.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3f2174fd11d8e920a556566ad712e933496d2c4_2_366x500.png" alt="image" data-base62-sha1="ueXqhKseS4d7lon7lZzMyKIH820" width="366" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3f2174fd11d8e920a556566ad712e933496d2c4_2_366x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3f2174fd11d8e920a556566ad712e933496d2c4_2_549x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3f2174fd11d8e920a556566ad712e933496d2c4.png 2x" data-dominant-color="F1F3F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">572×781 47.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #15 by @nysfour (2023-06-12 15:53 UTC)

<p>When I use that functionality inside the segment editor module, it doesn’t seem to let me create a seed point list</p>

---

## Post #16 by @rbumm (2023-06-12 16:52 UTC)

<p>Just place paint strokes or paint dots in the regions you want to segment.</p>

---

## Post #17 by @nysfour (2023-06-12 18:09 UTC)

<p>When I do that, even with ‘Allow Overlap’ selected, when I apply the growing segmenter it removes both layers (the initial segment that demarcates the region and then the second new layer)</p>
<p>Thank you again for the guidance, I greatly appreciate it</p>

---

## Post #18 by @rbumm (2023-06-13 05:13 UTC)

<p>There are tons of video tutorials available on Youtube, they should help.</p>
<p><a href="https://www.youtube.com/results?search_query=grow+from+seeds+3d+slicer" class="onebox" target="_blank" rel="noopener">https://www.youtube.com/results?search_query=grow+from+seeds+3d+slicer</a></p>

---
