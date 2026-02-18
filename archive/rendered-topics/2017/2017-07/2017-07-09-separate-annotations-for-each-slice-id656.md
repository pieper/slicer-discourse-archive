# Separate annotations for each slice

**Topic ID**: 656
**Date**: 2017-07-09
**URL**: https://discourse.slicer.org/t/separate-annotations-for-each-slice/656

---

## Post #1 by @pyhat (2017-07-09 00:53 UTC)

<p>Operating system: Linux<br>
Slicer version: 4.6.2</p>
<p>When in the editor module to do slice annotations, I’ve noticed the same annotation is used for several slices, and when I change it on one slice, the others on the neighboring ~3 slices are changed in the same way; as in, the slices are linked. How can I ‘unlink’ them, so each slice has a unique annotation?</p>

---

## Post #2 by @lassoan (2017-07-09 11:45 UTC)

<p>Please try the latest nightly version of Slicer and use the ‘Segment editor’ module instead of the ‘Editor’ module and let us know if you still have problems.</p>

---

## Post #3 by @pyhat (2017-07-10 20:54 UTC)

<p>Thanks for the reply; I have tried the newest Segmentation Editor with the same results. All I want is the label map I draw on one slice to be independent of the map on the very next slice; as it is now, every three slices are linked (share the same label map). Is this a problem with my not knowing the correct setting to change, or is this just how slicer’s label maps are written?</p>

---

## Post #4 by @lassoan (2017-07-10 21:21 UTC)

<p>By default brush thickness = slice viewer step size = slice spacing. So, if you step to the next alice using arrow keys then you should get a clean slice each time.</p>
<p>What is the spacing of your volume?<br>
How much the slice offset changes when you press arrow keys in slice viewers?<br>
Is your volume tilted (in Volumes module, information section, direction matrix has values different from 0 and +/-1)?</p>
<p>If your volume is tilted, then click “Rotate to volume plane” in the slice view controller widget (at the top of slice view).</p>
<p>You can adjust brush thickness &amp; slice viewer step size by changing the spacing value in the slice view controller widget.</p>

---

## Post #5 by @pyhat (2017-07-13 17:53 UTC)

<p>I figured it out; it wasn’t the slice spacing that was the problem, but rather that every time I created a new segmentation volume, the default volume was identical to the dicom information on slice thickness.</p>
<p>If anyone else runs into this problem:</p>
<ol>
<li>Create a new segmentation.</li>
<li>navigate to the ‘volumes’ module.</li>
<li>Change the active volume to your segmentation.</li>
<li>Under “Volume Information” change the image spacing to your desired spacing (in my case, 1mm).</li>
</ol>
<p>That fixes it for me, thanks for all the help!</p>

---
