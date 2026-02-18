# Many qMRMLThreeDWidgets impact application performance

**Topic ID**: 19539
**Date**: 2021-09-07
**URL**: https://discourse.slicer.org/t/many-qmrmlthreedwidgets-impact-application-performance/19539

---

## Post #1 by @xianger-qi (2021-09-07 12:07 UTC)

<p>If my application which base on slicer, need many qMRMLThreeDWidget, may be more than 10 qMRMLThreeDWidget. Is this will degrade the  window rendering perfermence? and how do i do? Thanks for your help!</p>

---

## Post #2 by @pieper (2021-09-07 17:18 UTC)

<p>There will certainly be overhead but exactly how much depends on the data and how often you update it.  The best thing to do is make a small example script and see how it performs.  Use a profiling tool if you can to see where the application is spending time.</p>

---
