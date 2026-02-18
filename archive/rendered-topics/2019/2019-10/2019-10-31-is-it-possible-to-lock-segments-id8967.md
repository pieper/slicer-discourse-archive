# Is it possible to lock segments

**Topic ID**: 8967
**Date**: 2019-10-31
**URL**: https://discourse.slicer.org/t/is-it-possible-to-lock-segments/8967

---

## Post #1 by @Leon (2019-10-31 11:37 UTC)

<p>As my topic mentions I would like to know if it’s possible to lock segments in order to prevent them from accidently being removed or cleared.<br>
This happened to me lately when I forgot to set the ‘Overwrite other segments’ to ‘None’. After having closed and reopened the project at a later time, I discovered that one of my segments was empty. First I was puzzled but then I noticed the ‘wrong’ setting so I had to resegment it.</p>
<p>Greetings,<br>
Léon</p>

---

## Post #2 by @lassoan (2019-10-31 12:46 UTC)

<p>Yes, you can protect segments by moving them to a separate segmentation node. The feature is available in Segmentations module Copy/Move section.</p>
<p>In recent Slicer Preview Releases we introduced state for each segment (not started, in progress, completed, flagged), which could be usable to alter masking settings. However, masking is already quite complicated, so I’m afraid that adding more options to it would make it harder to use.</p>
<p>Anyway, it’s important to get such feedback, we’ll keep it in mind and if other users have similar problems then we’ll see if there are better ways to address it.</p>

---

## Post #3 by @sfglio (2020-04-05 16:06 UTC)

<p>I’m using the nighty version from 2020-02-22 and I was looking for the same feature, i.e. I want to draw adjacent to a segmentation without overwriting the original segmentation.<br>
However, I do not have this option “none” in slicer among “modify other segments” (just: overwrite all, overwrite visible, allow overlap).</p>
<p>Are there any alternatives or do I just have to update slicer??</p>
<p>kind regards<br>
florian</p>

---

## Post #4 by @lassoan (2020-04-05 17:10 UTC)

<p>Name of “Modify other segments” options were changed in Slicer Preview Release to make them a bit more clear, but functionality did not change.</p>
<p>If you don’t want segments overwrite each other then choose “Modify other segments” -&gt; “allow overlap”. If you want to paint only in regions that are not segmented yet, choose “Editable area” -&gt; “outside all segments”.</p>
<p>Probably you don’t have to update your Slicer now, but in general, it is recommended to use latest stable release or latest preview release of Slicer.</p>

---
