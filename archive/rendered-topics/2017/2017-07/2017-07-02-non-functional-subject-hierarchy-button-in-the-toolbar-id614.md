---
topic_id: 614
title: "Non Functional Subject Hierarchy Button In The Toolbar"
date: 2017-07-02
url: https://discourse.slicer.org/t/614
---

# Non-functional "Subject hierarchy" button in the toolbar

**Topic ID**: 614
**Date**: 2017-07-02
**URL**: https://discourse.slicer.org/t/non-functional-subject-hierarchy-button-in-the-toolbar/614

---

## Post #1 by @fedorov (2017-07-02 19:07 UTC)

<p>There is a button in the toolbar that has “Subject hierarchy” tooltip, that does not appear to do anything. The icon looks similar to that of the “Data” module that works. This is how it looks in the today’s nightly: <a href="https://www.screencast.com/t/6jR88WWON">https://www.screencast.com/t/6jR88WWON</a></p>

---

## Post #2 by @pieper (2017-07-02 21:21 UTC)

<p>Hi Andrey - I believe this is a byproduct of merging the Data module with the Subject Hierarchy and there was a discussion of it at the time.  Can you try deleting your settings and see if that resolves the issue?</p>
<p>-Steve</p>

---

## Post #3 by @lassoan (2017-07-02 23:18 UTC)

<p>Deleting Slicer.ini file fixes it. If you don’t want to reset other settings, it is enough to delete the shortcut and add a shortcut for Data module instead.</p>

---

## Post #4 by @fedorov (2017-07-03 02:57 UTC)

<p>It doesn’t bother me really. I just didn’t realize this is expected behavior.</p>

---

## Post #5 by @cpinter (2017-07-04 16:05 UTC)

<p>FYI, I updated the default module list when making this change, so first-time users who install Slicer after this change should see the Data module button where the dummy SH button is for you (and was for me as well due to the already found settings file)</p>

---

## Post #6 by @pieper (2017-07-04 16:38 UTC)

<p>I wonder if we can detect this situation with the settings and fix it<br>
automatically?</p>

---

## Post #7 by @lassoan (2017-07-04 16:46 UTC)

<p>Definition of shortcuts are shared between all Slicer versions, so if the shortcut is changed SubjectHierarchy-&gt;Data in the nightly then it would break shortcut in stable version. We could add an automatic fix when a new stable is released.</p>

---
