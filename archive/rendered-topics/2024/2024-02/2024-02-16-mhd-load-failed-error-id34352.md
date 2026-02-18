# .mhd load failed error

**Topic ID**: 34352
**Date**: 2024-02-16
**URL**: https://discourse.slicer.org/t/mhd-load-failed-error/34352

---

## Post #1 by @Payton_Johnson (2024-02-16 02:13 UTC)

<p>I am trying to load data from an .mhd and .raw file set into Slicer 5.6.1. I keep getting an error notice that says the files failed to load. I have tried different versions of Slicer (5.6.0), different operating systems on different computers (macOs, windows), and different sets of files without a change in this error. Any idea what I am missing (extension, etc) that is required to be able to open these files?</p>

---

## Post #2 by @lassoan (2024-02-16 02:14 UTC)

<p>Can other software read this file?</p>

---

## Post #3 by @jamesobutler (2024-02-16 03:30 UTC)

<p>Have you by chance renamed the files? The mhd has a tag at the very bottom called <code>ElementDataFile</code> which specifies the name of the corresponding raw file.</p>

---
