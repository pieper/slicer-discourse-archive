---
topic_id: 33601
title: "Custom Undo Redo Function For All Process"
date: 2024-01-03
url: https://discourse.slicer.org/t/33601
---

# Custom undo/redo function for all process

**Topic ID**: 33601
**Date**: 2024-01-03
**URL**: https://discourse.slicer.org/t/custom-undo-redo-function-for-all-process/33601

---

## Post #1 by @park (2024-01-03 14:53 UTC)

<p>Hi all</p>
<p>I am currently working on developing a custom program using 3D Slicer and have a question I’d like to discuss in here.</p>
<p>We need for an undo-redo feature for all functions (including camera view adjustments).</p>
<p>Upon my investigation, it seems this feature is not currently implemented.  I also get to find “UndoEnabledOn”  function but could not find example for all process, only fiducial.</p>
<p>We has considered saving executed functions (such as Python scripts) separately and then reverting by executing those or saving states at specific timelines.</p>
<p>What would be the most efficient way to implement an undo-redo feature?</p>

---

## Post #2 by @pieper (2024-01-03 18:11 UTC)

<p>The undo/redo architecture at the MRML level should work fine, but sometimes the GUI/Logic levels get out of sync.  See more info <a href="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/UndoRedo/">here</a>  You can pretty easily experiment with it to see how well it works for specific uses.</p>
<p>Another option is to auto-save the whole mrml scene periodically.  If the bulk data has not changed this can be a very quick operation and allow you to reset to a known state easily.</p>

---
