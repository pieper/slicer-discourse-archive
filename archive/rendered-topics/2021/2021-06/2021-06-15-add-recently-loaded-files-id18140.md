---
topic_id: 18140
title: "Add Recently Loaded Files"
date: 2021-06-15
url: https://discourse.slicer.org/t/18140
---

# Add Recently Loaded Files

**Topic ID**: 18140
**Date**: 2021-06-15
**URL**: https://discourse.slicer.org/t/add-recently-loaded-files/18140

---

## Post #1 by @OpenSource_Contri (2021-06-15 10:38 UTC)

<p>Hello,<br>
I’ve add these to .slicerrc.py to open the DICOM import popup-<br>
slicer.util.selectModule(‘DICOM’)<br>
slicer.util.getModuleGui(‘DICOM’).importFolder()</p>
<p>Now, I wanted to add “recently opened DICOM” in the pop up. What steps to be followed?</p>

---

## Post #2 by @lassoan (2021-06-17 01:28 UTC)

<p>By default, Slicer shows imported patients based on the import time, so you will always see the patient that you have just imported at the top of the list.</p>

---
