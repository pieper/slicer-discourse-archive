# ITK Simple Filters SubtractImageFilter

**Topic ID**: 24515
**Date**: 2022-07-27
**URL**: https://discourse.slicer.org/t/itk-simple-filters-subtractimagefilter/24515

---

## Post #1 by @Will (2022-07-27 06:13 UTC)

<p>Hello,</p>
<p>I am trying to replicate the effect of CT angiography by creating a subtraction from two DICOM stacks. One is a mask, which is a CT without contrast injected into the patients arteries. The other is a fill, which is the same image (ideally) but with contrast.</p>
<p>I think I should be able to use ITK Simple Filter’s “SubtractImageFilter” to create a subtraction from these two scans. Initially, the status in the bottom right of the parameters field says “idle.” Then, I put my scans in as inputs (I have tried both orders) and a new volume as the output. I click apply and a popup says:</p>
<p>Exception before execution of SubtractImageFilter<br>
&lt;class ‘slicer.util.MRMLNodeNotFoundException’&gt;</p>
<p>After this attempt, the status says “exception” for all of the ITK filters.</p>
<p>How can I fix this? Other than scripting, are there any free alternatives that will allow me to create subtractions?</p>
<p>Thanks,<br>
Will</p>

---

## Post #2 by @lassoan (2022-07-27 10:02 UTC)

<p>I could not reproduce this error. Could you please upload the application log (menu: Help / Report a bug) somewhere and post the link here?</p>

---
