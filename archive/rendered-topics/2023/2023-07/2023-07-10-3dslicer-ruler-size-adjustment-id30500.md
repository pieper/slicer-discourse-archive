# 3Dslicer ruler size adjustment

**Topic ID**: 30500
**Date**: 2023-07-10
**URL**: https://discourse.slicer.org/t/3dslicer-ruler-size-adjustment/30500

---

## Post #1 by @Young_Wang (2023-07-10 15:29 UTC)

<p>Hi there, I wonder if there is a way to change the ruler size and location. I know there are options for thin and thick, and different colour but I wonder are there more options for customization?</p>

---

## Post #2 by @pieper (2023-07-10 16:09 UTC)

<p>Many things are possible, but most things that aren’t currently exposed would require C++ coding to change.  If you are interested in that, you could <a href="https://github.com/Slicer/Slicer/blob/ff1ba1679ae98a6a2e669d79dde1ad8620b60c04/Libs/MRML/DisplayableManager/vtkMRMLRulerDisplayableManager.h#L31">start here</a>.</p>

---
