---
topic_id: 24046
title: "Nrrd File Unable To Load"
date: 2022-06-25
url: https://discourse.slicer.org/t/24046
---

# Nrrd file unable to load

**Topic ID**: 24046
**Date**: 2022-06-25
**URL**: https://discourse.slicer.org/t/nrrd-file-unable-to-load/24046

---

## Post #1 by @aakk (2022-06-25 13:03 UTC)

<p>Hi, I’m very new to Slicer but I couldn’t find an answer to this on any of the previous support questions. I am trying to load a gif that was sent to me as an nrrd file into Slicer. It is giving the error message “load failed” and I am unsure what to do.</p>

---

## Post #2 by @lassoan (2022-06-25 16:29 UTC)

<p>Slicer does not support the GIF file format (see list of supported file formats <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#supported-data-formats">here</a>). GIF is a very old and limited file format, so probably it will not be supported in the future either.</p>
<p>If somebody sent you data in this format then you can <a href="https://www.onlineconverter.com/gif-to-tiff">convert it to a supported format</a> before loading it into Slicer.</p>

---

## Post #3 by @aakk (2022-06-25 23:55 UTC)

<p>Thanks! I converted it to a set of png images</p>

---
