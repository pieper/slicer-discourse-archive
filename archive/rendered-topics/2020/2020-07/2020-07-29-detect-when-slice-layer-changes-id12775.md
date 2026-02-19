---
topic_id: 12775
title: "Detect When Slice Layer Changes"
date: 2020-07-29
url: https://discourse.slicer.org/t/12775
---

# Detect when slice layer changes

**Topic ID**: 12775
**Date**: 2020-07-29
**URL**: https://discourse.slicer.org/t/detect-when-slice-layer-changes/12775

---

## Post #1 by @Jakew (2020-07-29 19:47 UTC)

<p>I’m looking for a way to detect when the scroll bar at the top of a view moves, or when the slice view changes. This can be done by detecting when the scroll wheel moves or when arrow keys are used, but I’d like to be able to detect the event itself. Is there a signal like that that can initiate a function when detected?</p>

---

## Post #2 by @pieper (2020-07-29 20:03 UTC)

<p>The suggested way is add an observer to the vtkMRMLSlliceNode corresponding to the view, but this won’t tell you how (mouse vs keyboard) the slice offset was modified, just that it did move.  What’s your use case?</p>

---

## Post #3 by @Jakew (2020-07-29 21:07 UTC)

<p>Yes my intended use is for just to see it was modified. Thanks for pointing me in the right direction!</p>

---

## Post #4 by @Jakew (2020-07-30 23:49 UTC)

<p>Just wanted to confirm, is the observer method doable in C++ or just Python? I’m looking into C++ observer methods and it doesn’t seem to be able to be used for MRMLSliceNodes or MRMLScenes.</p>

---

## Post #5 by @lassoan (2020-07-31 02:58 UTC)

<p>All Slicer features are available in both C++ and Python. In Slicer source code there are many examples for adding observers: search for <code>AddObserver</code> if you are interested in adding observer from VTK classes, and search for <code>qvtkReconnect</code> if you want to add observer from Qt classes.</p>

---
