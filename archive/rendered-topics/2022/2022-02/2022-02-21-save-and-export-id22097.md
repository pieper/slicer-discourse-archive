---
topic_id: 22097
title: "Save And Export"
date: 2022-02-21
url: https://discourse.slicer.org/t/22097
---

# Save and Export

**Topic ID**: 22097
**Date**: 2022-02-21
**URL**: https://discourse.slicer.org/t/save-and-export/22097

---

## Post #1 by @19lollo95 (2022-02-21 22:36 UTC)

<p>Hi everyone,<br>
I did a segmentation of a brain with a tumor (specifically the MRBrainTumor1 in BuiltIn). I’m having trouble with the save operation. I need to get 3 .mhd files:</p>
<p>The first which contains the skull;<br>
The second which contains GM, WM, and CFS;<br>
The third which contains the tumor;</p>
<p>How can I get 3 different mhd files for the two objects?<br>
Thanks in advance</p>

---

## Post #2 by @ebrahim (2022-02-22 00:26 UTC)

<p>You could use the eyeball symbol in the data module to hide the segments you want to omit, then right click on the segmentation and choose “Export visible segments to binary labelmap.” This will create a new volume item, which you can right click and “Export to file…”, choosing mhd as the format.</p>
<p>So do this once with only the skull visible, then again with only the GM/WM/CSF visible, etc.</p>

---
