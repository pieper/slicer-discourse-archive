# Convert STL file back to an NRRD format

**Topic ID**: 14418
**Date**: 2020-11-04
**URL**: https://discourse.slicer.org/t/convert-stl-file-back-to-an-nrrd-format/14418

---

## Post #1 by @Andreas (2020-11-04 07:13 UTC)

<p>Is it possible to convert an STL file back into an NDDR format so that, for example, the wall thickness can be adjusted again?</p>
<p>I know that you can save it as a lumen, but this takes a lot of time (Croped Volume).</p>
<p>If I only save the Croped Volume File, my segmentation is no longer available and only the original model is loaded. Saving everything takes what feels like 2 hours or more.</p>

---

## Post #2 by @lassoan (2020-11-10 21:31 UTC)

<p>You convert a model to segmentation node by right-clicking on it in the Data module.</p>
<p>You can speed up saving by disabling Compression option in Save data window and buy getting more RAM and faster disk.</p>
<p>What node takes a long time to save? How large is it?</p>

---
