---
topic_id: 12053
title: "Restarting Slicer To Load Loadable Module"
date: 2020-06-16
url: https://discourse.slicer.org/t/12053
---

# Restarting slicer to load loadable module

**Topic ID**: 12053
**Date**: 2020-06-16
**URL**: https://discourse.slicer.org/t/restarting-slicer-to-load-loadable-module/12053

---

## Post #1 by @fpsiddiqui91 (2020-06-16 11:35 UTC)

<p>Dear all,</p>
<p>I have been working with slicer modules for a couple of months now. I think there has already been a solution to this which I might have missed.</p>
<p>I am working with a custom C++ loadable module, do I have to restart slicer every time if I want to reload the module?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @pieper (2020-06-16 11:51 UTC)

<p>Yes, unfortunately for C++ loadable modules you do need to restart the application every time you rebuild.  Technically you could unload and reload the shared libraries, but in development reloading is usually done because of some kind of bug or feature change so proper cleanup would be hard.</p>
<p>One way to approach this is to put the C++ code like itk classes, filters, io, etc into a helper library, like the logic classes you’ll find in some modules, which can usually be debugged using well defined tests.  Then write the GUI as scripted modules that you can reload quickly.  SlicerVMTK might be a good one to study, but many follow this pattern.</p>

---
