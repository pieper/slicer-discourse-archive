---
topic_id: 25704
title: "Reading Multi Energy Ct Data In 3D Slicer"
date: 2022-10-14
url: https://discourse.slicer.org/t/25704
---

# Reading Multi-energy CT data in 3D Slicer

**Topic ID**: 25704
**Date**: 2022-10-14
**URL**: https://discourse.slicer.org/t/reading-multi-energy-ct-data-in-3d-slicer/25704

---

## Post #1 by @khyatisethia (2022-10-14 12:06 UTC)

<p>Hi Slicer Community,</p>
<p>I have Multi-energy CT data from Siemens Hardware and would like to visualize it in Slicer. I want to visualize different materials like (iodine, calcium) from this CT. But I am not sure how it can be done.<br>
I understand that different materials have different characteristics for different energy levels. How can energy and HU pixel values be related?</p>
<p>I would be grateful if you could give me some guidance on how this can be achieved. Thank you.</p>

---

## Post #2 by @pieper (2022-10-14 13:22 UTC)

<p>I don’t know of any existing code to process that kind of images.  Probably the dicom headers would have all the metadata needed to implement any appropriate computation, but it would require some programming work.</p>

---

## Post #3 by @lassoan (2022-10-19 06:07 UTC)

<p>The programming work might be very easy (depending on the complexity of the formula you need to apply to combine the multi-energy images). You can find a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#combine-multiple-volumes-into-one">simple example in the script repository</a>.</p>
<aside class="quote no-group" data-username="khyatisethia" data-post="1" data-topic="25704">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/khyatisethia/48/13453_2.png" class="avatar"> khyatisethia:</div>
<blockquote>
<p>How can energy and HU pixel values be related?</p>
</blockquote>
</aside>
<p>Density of the material (voxel value in HU) is energy dependent. See more details for example in this <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7772378/">nice review paper</a>. There are also some formulae in this paper that you can use to process these multi-energy CT images.</p>

---
