# How to get all the observers of a node?

**Topic ID**: 19150
**Date**: 2021-08-11
**URL**: https://discourse.slicer.org/t/how-to-get-all-the-observers-of-a-node/19150

---

## Post #1 by @slicer (2021-08-11 06:15 UTC)

<p>Operating system: Windows<br>
Version: 4.11</p>
<p>How to get all the observers of a node?</p>

---

## Post #2 by @pieper (2021-08-11 13:21 UTC)

<p>The observers aren’t really meant to be operated on externally because they don’t have any well defined meaning except to the code that added them.  That is, when one piece of code adds an observer it provides a C++ vtkCommand instance or python callable but these are opaque to any other part of the codebase.  Each module should keep track of the observations it adds so that it can cleanly remove them when needed (<code>AddObserver</code> returns a tag that uniquely identifies the observer for that observed <code>vtkObject</code>)</p>

---
