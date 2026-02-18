# Nth Fidutial Color

**Topic ID**: 3579
**Date**: 2018-07-25
**URL**: https://discourse.slicer.org/t/nth-fidutial-color/3579

---

## Post #1 by @sarafv (2018-07-25 21:26 UTC)

<p>Hi,<br>
I want to change the color of Nth Fidutial of a vtkMRMLMarkupsFiducialNode on a python script (As in Markups Module =&gt; Advanced =&gt; Display Properties =&gt; Selected Color)</p>
<p>I can modify the color of the entired list through the markups display node, but I didn’t find a method to change the color of a fiducial in the List.</p>
<p>Thanks for your help!<br>
Sara</p>

---

## Post #2 by @pieper (2018-07-25 21:41 UTC)

<p>The colors are specified for the whole list, so there’s not per-fiducial color.  But you can set the selected state on a per-fiducial basis and assign different colors to selected and non-selected fiducials.  Or you could use different lists with different colors.</p>
<p>HTH,<br>
Steve</p>

---
