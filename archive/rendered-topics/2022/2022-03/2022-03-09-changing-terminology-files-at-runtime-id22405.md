# Changing terminology files at runtime

**Topic ID**: 22405
**Date**: 2022-03-09
**URL**: https://discourse.slicer.org/t/changing-terminology-files-at-runtime/22405

---

## Post #1 by @marcosrdac (2022-03-09 13:30 UTC)

<p>Hello everyone.</p>
<p>I need to change the set of segmentation terminology entries I am able to select in the segment editor (when I double click the color of a segment in the segments table) depending on the context I am working on.</p>
<p>For example, I want to have a method that only allows bone categories to appear when I am changing my segment color, but then I want to run segmentation of different tissues at another scale in other context, then I would change the categories appearing to another set, by running a different method (hopefully in Python).</p>
<p>I tried creating different <code>*.term.json</code> files and put them in <code>share/$SLICER_APP/qt-loadable-modules/Terminologies</code> but I have no clue how to change between them when using Slicer. I read the documentation on the Terminologies module and also tried understanding the code, but still I was not able to do so.</p>
<p>Do you have any tips on how to do that?</p>
<p>Also, does Slicer read every terminology file in that <code>Terminologies</code> folder, or only a specific filename?</p>
<p>Thank you beforehand for your attention.</p>

---

## Post #2 by @marcosrdac (2022-03-11 11:55 UTC)

<p>I ended up discovering how to use terminology categories and storing every entry in the same JSON file. I did not see the left arrow to open the category filter there before I made this post.</p>

---
