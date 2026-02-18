# Readjusting threshold on singular segment

**Topic ID**: 19164
**Date**: 2021-08-12
**URL**: https://discourse.slicer.org/t/readjusting-threshold-on-singular-segment/19164

---

## Post #1 by @jrickman (2021-08-12 02:12 UTC)

<p>How are you able to readjust the threshold of a singular segment excluding others?</p>
<p>For context: trying to analyze singular bones from scan of multiple bones in a tube. Used threshold to select the bones and then segmented out the bones individually using islands. Unfortunately one of the bones was also touching the bottom of the tube, and when I tried to segment it there was a still a large portion of the tube attached to the bottom of the bone. I was able to delete the tube portion of the segment paint back in around the bottom of the bone. However, I am studying bone structure and only need the actual bone selected - not the blank space inside the bone. Currently, my segment does not include the tube anymore, but the portion of the segment I painted in contains more than the bone - there is also some space outside and blank space inside that is now a part of my segment.</p>
<p>So my question is - for the segment that contains my bone that I repainted the end on, is there a way to readjust the threshold so it is again just the bone I’m looking at? Ideally I would like to have a segment that contains only this bone with no portion of the tube or empty space in the middle.</p>

---

## Post #2 by @lassoan (2021-08-12 03:56 UTC)

<p>I find it hard to follow what happened exactly and what you would like to achieve. Could you please attach a screenshot to illustrate what you described?</p>

---

## Post #3 by @muratmaga (2021-08-12 04:02 UTC)

<p>It sounds like your starting threshold may not be appropriate for the selecting bone. As oppose to fixing it after the fact, you can use the local threshold option in the threshold effect and sample a small region within the cortical bone to get the distribution of the intensities associated with the bone. If you do in few different places, you will get values that represent the cortical bone more robustly. If you do this, I suspect you won’t need to second guess your threshold values and circumvent the problem.</p>
<p>If you break the connection of tube with one of your bones before the island (but after the threshold) via using Scissors tool or the Erase tool, then you can run the Island tool with the split islands option, and you will get your individual bones as separate segments.</p>
<p>As for retouching a segment without overwriting the others, please pay attention to the “Masking” field of the segment editor, which is sometimes overlooked. There is an option called <strong>Modify Other Segments</strong>, which is set to Everywhere by default. If you set this to <strong>Allow Overlap</strong>, you should be able to make changes without impacting the others.</p>
<p>Editable area is also a useful settings from which you can restrict what parts of the segment(s) is allowed to be changed.</p>
<p>If you are new to Slicer, I would highly encourage you to take a look at Slicer’s official Segmentation documentation. <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="inline-onebox" rel="noopener nofollow ugc">Image Segmentation — 3D Slicer documentation</a></p>
<p>There are also some additional tutorials which covers basics of each segment editor effects, along with masking/editing options under SlicerMorph tutorials: <a href="https://github.com/SlicerMorph/Spr_2021/blob/main/Day_2/Segmentation/Segmentation_tutorial.md" class="inline-onebox" rel="noopener nofollow ugc">Spr_2021/Segmentation_tutorial.md at main · SlicerMorph/Spr_2021 · GitHub</a></p>

---

## Post #4 by @jrickman (2021-08-13 08:13 UTC)

<p>Thank you, I was able to find a solution using these suggestions! I was able use the Erase brush to remove the unsatisfactory area of my bone segment, and then created a masking brush to select just my bone with “Use for Masking” in Thresholds.</p>
<p>I appreciate the help!</p>

---
