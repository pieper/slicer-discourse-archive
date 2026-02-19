---
topic_id: 2048
title: "Sequences Module Question"
date: 2018-02-07
url: https://discourse.slicer.org/t/2048
---

# Sequences module question

**Topic ID**: 2048
**Date**: 2018-02-07
**URL**: https://discourse.slicer.org/t/sequences-module-question/2048

---

## Post #1 by @gcsharp (2018-02-07 18:41 UTC)

<p>I’m interested in visualizing a (2D x time) vector field.overlaid on a (2D x time) image.  Is this possible with the sequences module?  How would I format my files (which are currently raw, not DICOM) to achieve this?</p>

---

## Post #2 by @lassoan (2018-02-07 18:58 UTC)

<p>If you load the displacement fields into the scene (each transform as a separate transform node) then you can use the Sequences modul GUI to put them into a sequence node.</p>
<p>Then, to visualize the time sequence, create a sequence browser node in Sequence browser module, and add the sequence that you created.</p>
<p>This can of course all by scripted in Python.</p>
<p>Let me know if you get stuck at any point.</p>

---
