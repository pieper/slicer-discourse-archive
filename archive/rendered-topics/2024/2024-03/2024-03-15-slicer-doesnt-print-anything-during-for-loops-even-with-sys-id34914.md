# Slicer doesn't print anything during for loops even with sys.stdout.flush()

**Topic ID**: 34914
**Date**: 2024-03-15
**URL**: https://discourse.slicer.org/t/slicer-doesnt-print-anything-during-for-loops-even-with-sys-stdout-flush/34914

---

## Post #1 by @leadro (2024-03-15 15:46 UTC)

<p>I’m developing a 3DSlicer extension that includes very long processes (huge for loops). I’d like to show the progress with a progressbar (like tqdm) or at least print some progress information at each iteration but nothing is printed in Slicer’s python console before the end of the process.<br>
This is what I obtain with tqdm, but only at the end as previously said.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/5683964f89f96e9456d4878549255e568ed5de7d.png" alt="image" data-base62-sha1="clkZaBv4ZWDTaLAD2ukqVVM3uFf" width="370" height="216"></p>
<p>I would be grateful for any help!</p>

---

## Post #2 by @Sunderlandkyl (2024-03-15 15:50 UTC)

<p>Have you tried adding slicer.app.processEvents() after each print statement to trigger the Qt update?</p>

---
