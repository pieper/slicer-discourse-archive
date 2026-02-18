# SlicerVMTK not building on cdash for stable

**Topic ID**: 42763
**Date**: 2025-05-01
**URL**: https://discourse.slicer.org/t/slicervmtk-not-building-on-cdash-for-stable/42763

---

## Post #1 by @chir.set (2025-05-01 17:36 UTC)

<p>I just noticed that SlicerVMTK is not building on cdash for stable.</p>
<p>A file is not found for inclusion. I tried a clean build and hit the same build failure. If I run cmake again after this failure, the build does complete. It’s obviously not a solution for your build machine.</p>
<p>I request any suggestion to fix that. The last solution will be to revert the patch that led to this troublesome situation. I am sorry for this disruption.</p>

---

## Post #2 by @chir.set (2025-05-01 19:08 UTC)

<p>I have added a <a href="https://github.com/vmtk/SlicerExtension-VMTK/pull/149" rel="noopener nofollow ugc">PR</a> for this issue and would like the opinion of core developers before merging it. A clean build succeeds in one step on mu machine. Thanks for any hint.</p>

---
