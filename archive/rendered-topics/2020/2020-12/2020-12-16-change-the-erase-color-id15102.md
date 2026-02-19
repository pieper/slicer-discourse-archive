---
topic_id: 15102
title: "Change The Erase Color"
date: 2020-12-16
url: https://discourse.slicer.org/t/15102
---

# Change the erase color

**Topic ID**: 15102
**Date**: 2020-12-16
**URL**: https://discourse.slicer.org/t/change-the-erase-color/15102

---

## Post #1 by @aldoSanchez (2020-12-16 20:08 UTC)

<p>hi today I was wondering if is possible to change the eraser color<br>
because when I´m editing in the editor I use shortcuts in the Wacom but when I use the tool erase is so easy to work and I would like to switch this color for 0 to another label solo in some parts I use 0 labels and in other ones I use label 2 or label 41 (from freesurfer) so I was thinking on messing with the original script to create something like<br>
slight_smile:</p><li>
<b>q:</b> erase value 2.</li><br>
if key == ‘q’:<br>
pipeline.errase().value(2)<br>
abortEvent = True<p></p>
<p>but I don’t find the script that contents the eraser tool</p>

---
