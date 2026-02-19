---
topic_id: 11543
title: "Using Mri Open Datasets From Standford"
date: 2020-05-14
url: https://discourse.slicer.org/t/11543
---

# Using MRI open datasets from Standford

**Topic ID**: 11543
**Date**: 2020-05-14
**URL**: https://discourse.slicer.org/t/using-mri-open-datasets-from-standford/11543

---

## Post #1 by @PameZurita (2020-05-14 19:59 UTC)

<p>I’m new using 3D Slicer. I’m currently working with MRI in order to segment it and create a socket. I’m working with datasets from Standford (<a href="http://mridata.org" rel="nofollow noopener">mridata.org</a>) wich has all their MRI in H5 format.<br>
When I upload them, it fails and says it “H5Gopen2 failed”.<br>
How can I fix it?</p>

---

## Post #2 by @Chris_Rorden (2020-05-15 16:35 UTC)

<p>You will need to <a href="https://github.com/MRSRL/mridata-recon/" rel="nofollow noopener">reconstruct</a> this data into images. This will generate images in <a href="https://github.com/mrirecon/bart" rel="nofollow noopener">BART</a> format as described <a href="https://mrirecon.github.io/bart/" rel="nofollow noopener">here</a>. The format has a simple text header (.hdr) in one file and the 64-bit float (<code>double</code> precision) image data in another file (.cfl). I would suggest using your favorite scripting language to generate a <a href="http://teem.sourceforge.net/nrrd/format.html" rel="nofollow noopener">NRRD</a> header based on the .hdr file that you can view with Slicer.</p>

---
