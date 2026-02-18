# Segmentation issue

**Topic ID**: 14032
**Date**: 2020-10-14
**URL**: https://discourse.slicer.org/t/segmentation-issue/14032

---

## Post #1 by @Carl_Slicer (2020-10-14 12:14 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.1120200903<br>
Expected behavior: segmentation<br>
Actual behavior:</p>
<p>I have a CT scan with contrast. The scanning has been performed as a bolus tracking scan to maximize interaterial contrast. I want to segment bones, aterial vessels and kidneys in the abdominal region.<br>
I start with defining one segment R_kidney. I then use segmentation = (threshold, smooting and keep largest part) to isolate the above organs. I the define a new box segment around the kidney using scissors. I the try to use logical operation intersect to select the kidney. But this operation just cuts out the kidney or actual the whole box area of the R_kidney. My next approach was to use the scissors to cut out the R_kidney. Then I define the L_kidney segment and do the above segmentation again. But when I cut out the left kidney, the R_kidney segment is also cleared.<br>
Next approach was to do each segment once at at time and the convert into volumes. I the succeded to create R_kidney, L_kidney and bone. I now want to subtract theese volumes from the last segment aterial vessels, to get the vessels only. But I cannot select the volumes in the logical operations?<br>
So my question is how can I do this? And I suspect there must be an easier way to do this than my somewhat cumbersome method above? I would love to hear suggestions.<br>
Best<br>
Carl_Slicer</p>

---

## Post #2 by @lassoan (2020-10-15 05:10 UTC)

<p>If you want to reassign a part of an existing segment to a new segment, you can use Scissors effect with these settings:</p>
<ul>
<li>Operation -&gt; “Fill inside” (to not erase but paint instead)</li>
<li>Masking / Editable area -&gt; Inside all segments (to not paint solid blocks but to keep the shape of already existing segments)</li>
</ul>
<p>There are many other approaches, which may be even better. For example, using Grow from seeds effect and masking with editable intensity range, as described in this segmentation recipe: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/AortaMaskedGrowFromSeeds/">https://lassoan.github.io/SlicerSegmentationRecipes/AortaMaskedGrowFromSeeds/</a> (you can add more seeds, e.g., one for for each kidney).</p>

---

## Post #3 by @Carl_Slicer (2020-10-15 16:31 UTC)

<p>Thanks a lot for a very fast reply to my question. I have tried the suggested approach, which is much faster than my previous approach. You answer also deepened my understanding of how 3D slicer works.<br>
Thanks<br>
Jesper</p>

---
