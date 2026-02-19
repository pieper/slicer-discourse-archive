---
topic_id: 30194
title: "Programatically Load Save Scenes And Saving Folders"
date: 2023-06-23
url: https://discourse.slicer.org/t/30194
---

# Programatically load/save scenes and saving folders

**Topic ID**: 30194
**Date**: 2023-06-23
**URL**: https://discourse.slicer.org/t/programatically-load-save-scenes-and-saving-folders/30194

---

## Post #1 by @Patrick_Li (2023-06-23 12:57 UTC)

<p>For a custom module I was making, I was wondering whether or not it was possible to load and save scenes (MRML files) without user input. For example the scene would save to a directory when the application was closed and would load from a directory when the user selected the module.</p>

---

## Post #2 by @pieper (2023-06-23 13:14 UTC)

<p>No reason you can’t do that.  There’s an <code>enter</code> method that gets called when a module is selected.  Of course there would need to be logic so the scene doesn’t get loaded multiple times, etc.</p>

---
