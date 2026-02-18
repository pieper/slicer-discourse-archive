# Crop Volume causing failure

**Topic ID**: 5573
**Date**: 2019-01-30
**URL**: https://discourse.slicer.org/t/crop-volume-causing-failure/5573

---

## Post #1 by @justdcinaus (2019-01-30 03:03 UTC)

<p>Good day to you all.<br>
I’ve downloaded the latest versions (4.10.1 and 4.11.0 from the 15th Jan) and installed over the top of my previous install folders.</p>
<p>I can Segment and use Volume Rendering with no issues, except when I use the Crop volume module first.</p>
<p>I loaded a DICOM CT study (actually I’ve tried with 2) that I’ve used before.</p>
<p>In the Crop Volume module I create a new volume as “New Volume” and a new “Crop Volume ROI” then crop in each panel and click apply.</p>
<p>It appears to work, however when I then move to either Segment Editor or Volume Rendering and select the new cropped volume slicer immediately crashes to desktop.</p>
<p>Has anyone else had similar issues recently?</p>
<p>Thanks<br>
David</p>

---

## Post #2 by @lassoan (2019-01-31 00:33 UTC)

<p>Most probably you run out of memory. After you cropped the volume, delete it (and keep only the cropped version) to free up some memory. You may also consider increasing the Spacing scale or reduce the region of interest size to reduce memory usage.</p>

---

## Post #3 by @justdcinaus (2019-03-01 03:32 UTC)

<p>Many thanks Andras<br>
I found my issue was actually a significantly delayed write of the cropped volume, I ended up saving the  information to disk and actually waiting till it completed (watching the folder in file explorer) and all was well.</p>
<p>I suspect you are correct with the memory, it was probably delayed with paging.<br>
Regards David</p>

---
