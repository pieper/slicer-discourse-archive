# Hide a markupList

**Topic ID**: 5418
**Date**: 2019-01-19
**URL**: https://discourse.slicer.org/t/hide-a-markuplist/5418

---

## Post #1 by @timeanddoctor (2019-01-19 02:31 UTC)

<p>I want to hide a markup, just like close the eye in the “DATA module”. I searched in this forum and the wiki but found nothing, excemple the wrong code.<br>
F = getNode(“F”)<br>
F.SetVisibility(False)</p>
<p>I test some and just found a fiducials setting, while it seems like not my goal.<br>
F = getNode(“F”)<br>
F.SetNthFiducialVisibility(0,0)<br>
If I want hide a Node such as a fiducialList, which codes I should write?<br>
Thanks.</p>

---

## Post #2 by @lassoan (2019-01-19 03:04 UTC)

<p>Display properties are stored in display node(s) associated with the fiducial node. See examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_markup_fiducial_display_properties" rel="nofollow noopener">script repository</a>.</p>

---

## Post #3 by @timeanddoctor (2019-01-19 06:48 UTC)

<p>Thank you very much.</p>

---
