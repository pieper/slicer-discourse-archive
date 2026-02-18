# Smoothing is causing crashes - help!!

**Topic ID**: 33934
**Date**: 2024-01-23
**URL**: https://discourse.slicer.org/t/smoothing-is-causing-crashes-help/33934

---

## Post #1 by @JMcWilliams (2024-01-23 21:11 UTC)

<p>Hi all,</p>
<p>I am using Slicer 3D 5.6.1 for oil droplet analysis. I have managed to edit the segment down and now just need to smooth the droplets. This is where the issue is!! Whenever I try to smooth it, the program just becomes completely unresponsive. Any advice? I was using Median smoothing at 3 mm</p>

---

## Post #2 by @muratmaga (2024-01-23 22:10 UTC)

<p>Any what is the image spacing of your data?</p>
<p>E.g., if it is 10 micron, 3mm smoothing kernel will be something like 300x300x300 voxels, causing a massive amount memory usage and can cause unresponsiveness you mention.</p>

---
