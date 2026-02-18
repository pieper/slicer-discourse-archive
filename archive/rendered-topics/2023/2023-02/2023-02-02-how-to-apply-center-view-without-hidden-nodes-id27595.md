# How to apply "Center view" without hidden nodes?

**Topic ID**: 27595
**Date**: 2023-02-02
**URL**: https://discourse.slicer.org/t/how-to-apply-center-view-without-hidden-nodes/27595

---

## Post #1 by @wrc (2023-02-02 01:58 UTC)

<p>Hello. There are several hidden nodes in my scene. I want to apply  “Center view” without these hidden nodes. Is there any method? (I cannot delete these nodes.) Thank you.</p>

---

## Post #2 by @pieper (2023-02-06 18:59 UTC)

<p>That sounds like a bug that should be fixed in the way the centered view is calculated.  Is there any chance you are a C++ programmer who would be able to help implement a solution?  If not maybe you could file an issue on github with example data (like a pointer to a dropbox folder with an example .mrb file that can be used to easily reproduce the issue) and hopefully someone else can have a look.  It may be as easy as a one-line change somewhere.</p>

---
