---
topic_id: 46720
title: "slicer runs out of memory with large  file."
date: 2026-04-12
url: https://discourse.slicer.org/t/46720
last_bumped: 2026-04-15T18:31:02.486Z
---

# slicer runs out of memory with large  file.

**Topic ID**: 46720
**Date**: 2026-04-12
**URL**: https://discourse.slicer.org/t/slicer-runs-out-of-memory-with-large-file/46720

---

## Post #1 by @mhsheikh25 (2026-04-12 14:55 UTC)

<p>I have a Dell running 2 Platinum 8160 Xeons and 720GB ecc memory with a Nvidia 3090 24 GB video card and 3D slicer crashes on a large file with 300 Gb of memory remaining - error says that there isn’t enough memory. Is there a max addressable limit for memory?</p>

---

## Post #2 by @pieper (2026-04-12 18:14 UTC)

<p>You’ll need to provide more details on what you were trying to accomplish.</p>

---

## Post #3 by @mhsheikh25 (2026-04-12 21:26 UTC)

<p>I have a CT scan 90 micron per scan 7.7 Gb file.  I have segmented the scan and when I try to create another island, I get an “out of memory” and you might fix it with increasing swap and ram.</p>

---

## Post #4 by @hherhold (2026-04-13 14:07 UTC)

<p>I have a snippet of code in my .slicerrc.py file that would set the number of undo levels (which I think is defaulted to 10), I sometimes set it to 1 (or 0 if I’m feeling lucky). I don’t have it handy at the moment, but this may be something to try. I work with volumes larger than this on a machine with 128GB of ram and a 16GB NVIDIA RTX A5000, so you should be fine.</p>

---

## Post #5 by @hherhold (2026-04-15 16:53 UTC)

<p>This is it - I’ve found it to be helpful with large segmentations.</p>
<pre><code class="lang-auto">def setUndoLevels(numLevels):
  segmentEditorWidget = slicer.modules.segmenteditor.widgetRepresentation().self().editor
  segmentEditorWidget.setMaximumNumberOfUndoStates(numLevels)

</code></pre>

---

## Post #6 by @mhsheikh25 (2026-04-15 18:31 UTC)

<p>Thanks, I’ll try it.</p>

---
