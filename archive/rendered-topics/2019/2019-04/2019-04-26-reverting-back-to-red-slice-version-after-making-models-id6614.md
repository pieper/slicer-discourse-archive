# Reverting back to Red Slice version AFTER making models

**Topic ID**: 6614
**Date**: 2019-04-26
**URL**: https://discourse.slicer.org/t/reverting-back-to-red-slice-version-after-making-models/6614

---

## Post #1 by @SMO (2019-04-26 02:27 UTC)

<p>Operating system:<br>
Slicer version:               4.10.1<br>
Expected behavior:       In the past I have been able to revert back to Red Slice versions AFTER having created a model. This allows me to modify Red Slice version errors/ make modifications.</p>
<p>Actual behavior: After finishing Red Slice traces and making the model, I am no longer able to revert back to Red Slice drawings, anymore. Thus, mistakes are not able to be corrected. This is a tremendous inconvenience, especially for beginners… who will naturally make mistakes while learning to work the program. Instead, a black screen automatically appears as soon as the model is made, and there is no way to return to the Red Slice drawings, anymore. Please tell me this is NOT a permanent change in the system!</p>

---

## Post #2 by @lassoan (2019-04-26 02:33 UTC)

<p>Please use “Segment Editor” module instead of the legacy “Editor” module.</p>
<p>You will not need to run Model Maker module anymore: it is enough to click “Show 3D” button to see segmentation results in 3D view (it is updated automatically as you are modifying the segmentation).</p>
<p>If you want to export segmentation to STL file for 3D printing then you can use “Export to files” feature (available in the “Segmentations” button’s menu in Segment Editor).</p>
<p>If you want to make models of the segmented structures, you can export segmentation to model nodes by right-clicking on the segmentation node in Data module and selecting “Export visible segments to models”.</p>

---

## Post #3 by @SMO (2019-05-01 14:31 UTC)

<p>Dear Mr Lasso,</p>
<p>Thank you for your reply. So I indeed DID attempt to open up the red slice view again, via the “Segment Editor” module instead of the legacy “Editor” module. But after going from the 3D view back to red slice (with “Segment Editor” open instead of “Editor”), it is still showing a black screen only (rather than the red screen version of rat brain MRI’s I am taking volumes of).</p>
<p>Please direct. Thank you for your assistance.</p>
<p>Sincerely,</p>
<p>Sandra Ocampos</p>

---

## Post #4 by @lassoan (2019-05-01 18:15 UTC)

<p>Use Segment Editor module and do not use Editor or Model maker modules. If you still have any problem, please describe the exact steps you make, what you expect to happen, and what happens instead. Also attach screenshots.</p>

---
