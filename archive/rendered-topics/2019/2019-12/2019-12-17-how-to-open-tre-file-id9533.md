---
topic_id: 9533
title: "How To Open Tre File"
date: 2019-12-17
url: https://discourse.slicer.org/t/9533
---

# How to open .TRE file?

**Topic ID**: 9533
**Date**: 2019-12-17
**URL**: https://discourse.slicer.org/t/how-to-open-tre-file/9533

---

## Post #1 by @Duy_H (2019-12-17 19:51 UTC)

<p>Dataset at “<a href="https://public.kitware.com/Wiki/TubeTK/Data" rel="nofollow noopener">https://public.kitware.com/Wiki/TubeTK/Data</a>” have “VascularNetwork.tre” file. How can i open this file using 3DSlicer?</p>

---

## Post #2 by @pieper (2019-12-17 20:17 UTC)

<p>You probably need to check with the TubeTK team to find out the current status.</p>
<p><a href="https://public.kitware.com/Wiki/TubeTK/Contact" class="onebox" target="_blank">https://public.kitware.com/Wiki/TubeTK/Contact</a></p>

---

## Post #3 by @lassoan (2019-12-17 21:53 UTC)

<p>The .tre file is an ITK spatial object (scene) file. You should be able to read it using ITK or SimpleITK and save it as a vtk, vtp, ply, obj, or stl file that Slicer can read. If TubeTK contact does not respond then you can ask on the <a href="https://discourse.itk.org/">ITK forum</a>.</p>

---
