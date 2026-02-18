# Fast marching (SegmentEditorExtraEffects) runs indefinitely without result

**Topic ID**: 3634
**Date**: 2018-08-02
**URL**: https://discourse.slicer.org/t/fast-marching-segmenteditorextraeffects-runs-indefinitely-without-result/3634

---

## Post #1 by @Svenyos (2018-08-02 06:55 UTC)

<p>Operating system: Windows 7 ultimate<br>
Slicer version: 4.8.1 stable<br>
Expected behavior: iterative creation of a larger segment based on user-provided seed segment (eg paint)<br>
Actual behavior: Upon intitialisation, tool runs indefinitely with no outcome and heavy physical memory use</p>
<p>Model: HP Z820<br>
Processor: Intel® Xeon® CPU E5-2643<br>
Graphics Card: AMD firepro V4900</p>
<p>Please help. I have only recently begun using Slicer so apologies if this is an error on my part and not a problem with the SegmentEditorExtraEffects extension. I have been trying to use the fast arching tool in Slicer and I’m failing.  Each time I attempt to extend a seed segment (painted with an organ of interest) using fast marching, I get the impression the tool is trying to perform an operation (Physical memory use increases notably) but it runs indefinitely and I am forced to end slicer and restart the software (longest I left it running is 3 hours). I have attempted this using max volume percentages as low as 1% and up to 30%. The volume being segmented is not medical in origin, but rather a biological sample that was imported as a sequence of image files (I mention this in case the tool is only useable in DICOM volumes for example?). Segmentation using the standard suite of tools available in the segmentation editor works fine, despite the small physical space occupied by the volume (the scanned sample is less than 1cm3 in volume, with image spacing already adjusted appropriately in the volume module). I have also had problems with flood filling (nothing happens at all). The Hollow tool works as expected however.</p>
<p>Has anyone encountered this problem?</p>
<p>Sorry in advance if more info is needed.</p>

---

## Post #2 by @lassoan (2018-08-02 07:17 UTC)

<aside class="quote no-group" data-username="Svenyos" data-post="1" data-topic="3634">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/df705f/48.png" class="avatar"> Svenyos:</div>
<blockquote>
<p>Each time I attempt to extend a seed segment (painted with an organ of interest) using fast marching, I get the impression the tool is trying to perform an operation</p>
</blockquote>
</aside>
<p>This indicates that “Watershed” or “Grow from seeds” effect is running in the background. Go to these effects and click “Cancel” to deactivate (if “Cancel” button is disabled then it means that it is already deactivated).</p>

---

## Post #3 by @Svenyos (2018-08-02 19:07 UTC)

<p>Hello Andras,<br>
Unfortunately neither tool appears to be running in the background, as the cancel button was disabled in both cases. I presume another problem is at play. In case it’s pertinent, the computer isn’t networked so I had to install the extension offline by downloading it separately from kitware, having searched for the extension under the release ID that corresponded to the stable version of Slicer 4.8.1 (26813?), for windows 64.<br>
Any other possibilities?</p>

---

## Post #4 by @lassoan (2018-08-02 21:28 UTC)

<p>Please try the latest nightly version. If you still have problems, please attach the application log (menu: Help / Report a bug).</p>

---

## Post #5 by @Svenyos (2018-08-03 09:01 UTC)

<p>Can’t get the nightly version to run on that computer (Issue with graphics card I suspect). In any case I tried on another networked computer with the most recent nightly build and this problems persists. However I attempted to perform the same task on another volume which had not been linear transformed and it worked. I wanted to ask about that as the linear transforms I have performed on the problematic volume were an axis flip and a rotation (one nested within the other). Is this what’s causing the problem? I tried performing the fast marching on both this hard-transformed volume and after resampling to create a new volume with the same problem. There are other indications that both volumes are behaving strangely: paint (without sphere enabled) is not solid with regular triangular holes appearing in the painted region (but paint with sphere is solid) and; level tracing behaves as if it is trying to select pixels from a volume in a different orientation (you can see that the same region is being targeted based on it’s shape, but it does not overlay the background volume exactly, being skewed in a different axis).   Perhaps all these problems relate to the nested trasform. I don’t understand why the resampled volume is also misbehaving though…</p>

---

## Post #6 by @lassoan (2018-08-03 09:32 UTC)

<p>This is very useful information. Axis flip (any linear transformation with negative determinant) turns the volume inside out, which may cause problems. I think issues related to this are fixed in recent 4.9 versions, but I’ll check again. Until then, you can resample the transformed volume using Crop volumes module (make sure the cropping ROI node is not transformed).</p>

---
