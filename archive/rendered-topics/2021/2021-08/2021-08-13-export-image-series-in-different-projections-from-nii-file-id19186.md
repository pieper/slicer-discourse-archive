# Export image series in different projections from .nii file

**Topic ID**: 19186
**Date**: 2021-08-13
**URL**: https://discourse.slicer.org/t/export-image-series-in-different-projections-from-nii-file/19186

---

## Post #1 by @Emporio (2021-08-13 12:52 UTC)

<p>Hello dear experts. My English is very bad and therefore I am writing to you via google translate. I have a problem. How to get and save a series of photos from a .nii file from different projections in headless mode. I looked at the api for the built-in “Screen capture” module, but very likely it will not work as it just takes screenshots from the UI, which is simply absent in headless mode.</p>

---

## Post #2 by @pieper (2021-08-13 13:04 UTC)

<p>If you need to render, the easiest is to provide a virtual desktop, which can be done with <a href="https://www.x.org/releases/X11R7.6/doc/man/man1/Xvfb.1.xhtml">xvfb</a> or with a containerized Slicer (see <a href="https://github.com/pieper/SlicerDockers">here</a> or <a href="https://github.com/Slicer/SlicerDocker">here</a> for examples).</p>

---

## Post #3 by @Emporio (2021-08-16 05:11 UTC)

<p>Thank you for advice, but I’m interested in a solution without a virtual machine, where images are read and saved through a python script.</p>

---

## Post #4 by @Emporio (2021-08-17 05:40 UTC)

<p>Up post, pls help. I’m interested in a solution without a virtual machine, where images are read and saved through a python script.</p>

---
