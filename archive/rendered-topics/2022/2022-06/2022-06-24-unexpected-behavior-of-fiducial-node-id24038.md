# Unexpected behavior of fiducial node

**Topic ID**: 24038
**Date**: 2022-06-24
**URL**: https://discourse.slicer.org/t/unexpected-behavior-of-fiducial-node/24038

---

## Post #1 by @tristan421 (2022-06-24 23:11 UTC)

<p>Ok not really unexpected, but annoying.<br>
I’m using a script to loop over control points in a fiducial node, then delete the ones that do not belong to a given labelmap.</p>
<p>To delete a control point, I only found the method removeNthcontrolpoint. But here is the issue : the list of controlpoints gets reordered after each deletion. So my loop gets broken.</p>
<p>For example if I delete the 4t control point, the next loop iteration will jump to what was the 6th control point, because it is now the 5th.</p>
<p>Not sure if I’m understandable here.</p>
<p>Is there a workaround ? I could workaround it but it would be a dirty hack</p>
<p>Thank you , have a good weekend</p>

---

## Post #2 by @lassoan (2022-06-25 04:10 UTC)

<p>When you erase items from a list by index then always start with last item that you want to delete, then the second last, etc. and finally the first one (because deleting an item only invalidates indices of the items after it).</p>

---

## Post #3 by @tristan421 (2022-06-25 15:57 UTC)

<p>Simple and effective. Thank you for all your work around here</p>

---
