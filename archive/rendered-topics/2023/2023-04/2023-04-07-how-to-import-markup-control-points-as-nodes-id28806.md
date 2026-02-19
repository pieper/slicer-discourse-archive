---
topic_id: 28806
title: "How To Import Markup Control Points As Nodes"
date: 2023-04-07
url: https://discourse.slicer.org/t/28806
---

# How to import markup control points as nodes?

**Topic ID**: 28806
**Date**: 2023-04-07
**URL**: https://discourse.slicer.org/t/how-to-import-markup-control-points-as-nodes/28806

---

## Post #1 by @Vathsan (2023-04-07 22:22 UTC)

<p>I’ve exported a set of <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/markups.html#markups-control-points-table-file-format-csv-tsv" rel="noopener nofollow ugc">markup control points as a table</a> (.csv format). When I import the table, the control points do not appear under nodes section of the markup module. I need to apply a set of transformations to these coordinates. Is there a way to achieve this instead of creating separate .fcsv files?</p>
<p>Thanks,<br>
Vathsan</p>

---

## Post #2 by @lassoan (2023-04-08 20:28 UTC)

<p>You can read the CSV as a table and then import the points from the table in Markups module.</p>

---

## Post #3 by @Vathsan (2023-04-10 18:31 UTC)

<p>Yes, I tried that and it works fine. I was wondering if there is a way to create separate nodes for each control points, instead of having all the control points under a single node (F_1)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62aa982b440400044108803d1db2dc3619e1e0a1.png" data-download-href="/uploads/short-url/e4QhUH0zktNoBwIss2v4H5bxWwN.png?dl=1" title="Screenshot from 2023-04-10 12-29-31" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62aa982b440400044108803d1db2dc3619e1e0a1_2_384x500.png" alt="Screenshot from 2023-04-10 12-29-31" data-base62-sha1="e4QhUH0zktNoBwIss2v4H5bxWwN" width="384" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62aa982b440400044108803d1db2dc3619e1e0a1_2_384x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62aa982b440400044108803d1db2dc3619e1e0a1_2_576x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62aa982b440400044108803d1db2dc3619e1e0a1_2_768x1000.png 2x" data-dominant-color="E5E6E7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2023-04-10 12-29-31</span><span class="informations">1606×2089 280 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2023-04-10 20:33 UTC)

<p>This it is easily doable by a few-line Python script (probably chatgpt can generate it for you), but it is not commonly needed. Can you write a bit more about what you want to achieve? What does each point represent? How many points do you have? Why do you want each point to be a separate node?</p>

---
