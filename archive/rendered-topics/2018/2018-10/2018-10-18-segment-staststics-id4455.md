# Segment staststics

**Topic ID**: 4455
**Date**: 2018-10-18
**URL**: https://discourse.slicer.org/t/segment-staststics/4455

---

## Post #1 by @Ash_Alarfaj (2018-10-18 16:27 UTC)

<p>Problem report for Slicer 4.9.0-2018-10-16 macosx-amd64: [please describe expected: show the statstics value for segment</p>
<p>and actual behavior: apply icon did not work?<br>
this is the same problem I’ve faced in 3Dslicer4.8</p>

---

## Post #2 by @cpinter (2018-10-18 18:22 UTC)

<p>Seems to work for me. This is what I did:</p>
<ol>
<li>Load CT</li>
<li>Do segmentation in Segment Editor</li>
<li>Go to Segment Statistics</li>
<li>Select new segmentation as Segmentation and the CT as Scalar volume</li>
<li>Create new Output table</li>
<li>Click Apply</li>
</ol>
<p>What did you do differently?</p>

---

## Post #3 by @Ash_Alarfaj (2018-10-18 18:41 UTC)

<p>After doing 2or 3 studies the statstics seems to hangout and I have to save my work close the sence then reload it.</p>

---

## Post #4 by @cpinter (2018-10-18 18:59 UTC)

<p>We’ll need a way to reproduce it in order to fix it, so if you could present a sequence of steps that brings out this issue that would be great help.</p>
<p>It would be also useful to see the log of a session where you have this problem. Get the log in About / Report a problem.</p>

---

## Post #5 by @lassoan (2018-10-18 19:06 UTC)

<p>If you close the scene then you need to right-click on “Parameter set” selector and create a new parameter set by clicking “Create new ScriptedModule”.</p>

---
