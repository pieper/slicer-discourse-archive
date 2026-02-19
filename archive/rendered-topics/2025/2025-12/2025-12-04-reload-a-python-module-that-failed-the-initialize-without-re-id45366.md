---
topic_id: 45366
title: "Reload A Python Module That Failed The Initialize Without Re"
date: 2025-12-04
url: https://discourse.slicer.org/t/45366
---

# Reload a python module that failed the initialize without restarting Slicer

**Topic ID**: 45366
**Date**: 2025-12-04
**URL**: https://discourse.slicer.org/t/reload-a-python-module-that-failed-the-initialize-without-restarting-slicer/45366

---

## Post #1 by @muratmaga (2025-12-04 16:54 UTC)

<p>Is there a way to reload a failed module without restarting the slicer? I can’t use the “Reload” button if the module hasn’t successfully initialized…</p>

---

## Post #2 by @pieper (2025-12-04 17:14 UTC)

<p>You could try dragging the directory onto Slicer again, but generally I just restart since 90+% of the debugging can be done once the module loads the first time.  In fact, good practice is to just start with the template and incrementally modifiy it so it is always reloadable.</p>

---
