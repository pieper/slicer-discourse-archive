# How to segment brain tumor in offline enviroment?

**Topic ID**: 25776
**Date**: 2022-10-19
**URL**: https://discourse.slicer.org/t/how-to-segment-brain-tumor-in-offline-enviroment/25776

---

## Post #1 by @jay1987 (2022-10-19 12:29 UTC)

<p>should i buld a monai label server local?<br>
or there is another way to do these work?</p>

---

## Post #2 by @lassoan (2022-10-20 00:58 UTC)

<p>If you don’t need any GUI (the segmentation is always good enough) using MONAILabel then yes, all you need is to set up the server and use its REST API.</p>

---

## Post #3 by @jay1987 (2022-10-20 01:29 UTC)

<p>thank you very much lassoan<br>
use REST API is enough for me . i want to package the monaillabel with slicer,is there a extension to start monailabel server? or it need to write custom codes to do the work?</p>

---
