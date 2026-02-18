# Finding a midpoint between a line

**Topic ID**: 32678
**Date**: 2023-11-08
**URL**: https://discourse.slicer.org/t/finding-a-midpoint-between-a-line/32678

---

## Post #1 by @SlicerNewUser (2023-11-08 16:39 UTC)

<p>Hi there,</p>
<p>If I make a Line in Markup (so there is 2 points). Is there anyway for the software to automatically mark another point that is the midpoint of that line?</p>
<p>Thank you</p>

---

## Post #2 by @MariaGraf (2024-07-08 11:27 UTC)

<p>Does anyone have an update on how to do this? I have been completing the midpoint by hand and it is quite time consuming.</p>

---

## Post #3 by @cpinter (2024-07-08 11:39 UTC)

<p>It is a few lines of Python code. This is an example for going through the points of a fiducial list:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#write-markup-control-point-positions-to-json-file" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#write-markup-control-point-positions-to-json-file</a></p>
<p>From here you only need to average the two points.</p>

---
