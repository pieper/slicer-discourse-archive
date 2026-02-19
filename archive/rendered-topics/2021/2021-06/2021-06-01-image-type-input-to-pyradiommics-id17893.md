---
topic_id: 17893
title: "Image Type Input To Pyradiommics"
date: 2021-06-01
url: https://discourse.slicer.org/t/17893
---

# Image type input to pyRadiommics

**Topic ID**: 17893
**Date**: 2021-06-01
**URL**: https://discourse.slicer.org/t/image-type-input-to-pyradiommics/17893

---

## Post #1 by @11117 (2021-06-01 08:28 UTC)

<p>Hi,<br>
pyRadiommics knows how to handle float input? (nrrd file with float arrays)<br>
or it will convert it to int?</p>
<p>or there is a any problem with very high float variable?</p>
<p>Tnx</p>

---

## Post #2 by @JoostJM (2022-01-21 10:07 UTC)

<p>Float images are accepted and treated as float. Masks are forced to an integer datatype.</p>

---
