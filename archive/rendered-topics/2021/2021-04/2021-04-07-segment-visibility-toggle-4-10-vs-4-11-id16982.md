# Segment visibility toggle 4.10 vs 4.11

**Topic ID**: 16982
**Date**: 2021-04-07
**URL**: https://discourse.slicer.org/t/segment-visibility-toggle-4-10-vs-4-11/16982

---

## Post #1 by @ottensmeyer (2021-04-07 14:20 UTC)

<p>Hello,</p>
<p>Just installed 4.11.20210226, up from 4.10.2, running on Win10 Pro v20H2, build 19042.867</p>
<p>In the Segment Editor, in 4.10.2, when one segment is selected, one can toggle visibility (change open/closed eye icon state) of another segment without simultaneously selecting the other segment.  In 4.11, if I click the eye icon to toggle visibility of some segment, I lose focus on the segment on which I’m actually working, leading me to accidentally start editing the segment that I want to see but not edit.</p>
<p>In 4.10.2, hovering over the eye icon shows a dotted border around the visibility icon, which does not appear in 4.11.</p>
<p>Is this an intended behavior new behavior I’ll need to get used to?  At the moment, I keep on clicking the icon to see another segment for reference, and start accidentally editing that one instead of the one I want to change.</p>
<p>(I see, for example, that mouse mode selection is new since 4.10.2 - took reference to the manual to find out why left-click/drag didn’t change contrast/brightness any more, but that one seems reasonable.)</p>
<p>thanks very much!</p>

---

## Post #2 by @lassoan (2021-04-14 05:35 UTC)

<p>We reworked the segment list to add many new features (searching, filtering, states) and along the way management of checkboxes changed. I agree that the previous behavior was better, but it is not trivial to achieve that again in the new architecture. I would suggest to submit a feature request to the <a href="http://issues.slicer.org/">Slicer issue tracker</a>.</p>

---

## Post #3 by @ottensmeyer (2021-04-14 10:30 UTC)

<p>Thanks very much!  Will do.</p>

---
