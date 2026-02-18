# Problem with Segment registration

**Topic ID**: 11182
**Date**: 2020-04-19
**URL**: https://discourse.slicer.org/t/problem-with-segment-registration/11182

---

## Post #1 by @mccarthyvetsurg (2020-04-19 01:12 UTC)

<p>Good evening,</p>
<p>I have been trying to register 2 segmentations and after I choose the files (moving and fixed and click perform registration, a watch pops up and the two segments never register?  I am not sure what the best route to take would be… uninstall the segmentation register module and then  reinstall?</p>
<p>Thanks.</p>

---

## Post #2 by @timeanddoctor (2020-04-19 05:41 UTC)

<p>If you registrated this segementations and you will get a transform(A).<br>
then, open the transform module and add your fix segmentation to the transform(A).</p>

---

## Post #3 by @cpinter (2020-04-19 19:45 UTC)

<p>Can you please check if there are any errors in the Python interactor (open from View menu), or if not then can you please send us the log (About / Report an error)?</p>

---
