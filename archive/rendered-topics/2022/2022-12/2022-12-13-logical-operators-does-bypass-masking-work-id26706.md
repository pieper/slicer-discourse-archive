---
topic_id: 26706
title: "Logical Operators Does Bypass Masking Work"
date: 2022-12-13
url: https://discourse.slicer.org/t/26706
---

# Logical operators - does "Bypass masking" work?

**Topic ID**: 26706
**Date**: 2022-12-13
**URL**: https://discourse.slicer.org/t/logical-operators-does-bypass-masking-work/26706

---

## Post #1 by @hherhold (2022-12-13 12:08 UTC)

<p>In the Logical operators tool in Segment editor, the “Bypass masking” checkbox appears to have no effect, at least when it comes to Editable intensity range. When I have this checkbox enabled and I copy from one segment to another, the range limits are applied, even if I have Bypass masking set. Is it only the Editable area that is checked, and not the other parameters? If so, “Bypass masking” should be renamed, as Editable area, Editable intensity range, and Modify other segments are all in the “Masking” group.</p>

---

## Post #2 by @lassoan (2022-12-14 13:28 UTC)

<p>Maybe the label “bypass masking” is misleading (we wanted to keep the text short), and the perhaps the tooltip can be interpreted different ways, too. The important part of the tooltip is: <code>only modify the selected segment</code> (ignores all masking options that contradict this).</p>
<p>Do you have any suggestion for checkbox label and tooltip text that would be short and clear and match the current behavior?</p>
<p>Do you have any issue with the current behavior?</p>

---
