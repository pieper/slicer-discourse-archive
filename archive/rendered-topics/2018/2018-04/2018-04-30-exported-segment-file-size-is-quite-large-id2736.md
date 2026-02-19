---
topic_id: 2736
title: "Exported Segment File Size Is Quite Large"
date: 2018-04-30
url: https://discourse.slicer.org/t/2736
---

# Exported segment file size is quite large

**Topic ID**: 2736
**Date**: 2018-04-30
**URL**: https://discourse.slicer.org/t/exported-segment-file-size-is-quite-large/2736

---

## Post #1 by @anandmulay3 (2018-04-30 14:33 UTC)

<p>I’m using scripted module to export segmentation in obj format, today i have updated the slicer latest nightly build version. and now the size is increased again.<br>
Do we have any code or method to reduce or compress the 3D object file size while exporting.</p>

---

## Post #2 by @lassoan (2018-04-30 18:19 UTC)

<p>You can apply decimation to reduce number of mesh points without decreasing important details:</p>
<ul>
<li>Go to Segmentations modul</li>
<li>In Representations section, click Update in Closed surface row</li>
<li>Click Binary labelmap-&gt;Closed surface rule</li>
<li>Change Decimation factor value to 0.8 to reduce number of points by 80%. You can try values up to about 0.99, the higher the value, the more points are removed.</li>
</ul>

---
