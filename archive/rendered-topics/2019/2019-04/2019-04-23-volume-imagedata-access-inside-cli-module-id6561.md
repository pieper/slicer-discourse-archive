---
topic_id: 6561
title: "Volume Imagedata Access Inside Cli Module"
date: 2019-04-23
url: https://discourse.slicer.org/t/6561
---

# Volume ImageData access inside CLI module

**Topic ID**: 6561
**Date**: 2019-04-23
**URL**: https://discourse.slicer.org/t/volume-imagedata-access-inside-cli-module/6561

---

## Post #1 by @michalikthomas (2019-04-23 00:12 UTC)

<p>Is it possible to access volume imageData inside c++ CLI module?</p>

---

## Post #2 by @pieper (2019-04-23 12:12 UTC)

<p>Typically, Slicer MRML volumes are passed as nrrd files which the CLI reads using ITK to get an itk::Image.</p>

---
