---
topic_id: 773
title: "Ct Grey White Matter Segmenation"
date: 2017-07-27
url: https://discourse.slicer.org/t/773
---

# CT grey/white matter segmenation

**Topic ID**: 773
**Date**: 2017-07-27
**URL**: https://discourse.slicer.org/t/ct-grey-white-matter-segmenation/773

---

## Post #1 by @hph10128 (2017-07-27 04:01 UTC)

<p>Hi all,</p>
<p>I have perfusion CT maps that I registered to 24 hour post-op CTs. My end goal is to segment grey and white matter in both the perfusion and post-op CTs. I attempted to use the EM segmentation module for MRI segmentation but am unable to register the post-op non-perfusion CT to the atlas. Does anyone have any suggestions on how to perform this segmentation? Should I be using the EM segmentation module? Any advice/suggestions are greatly appreciated.</p>
<p>Thanks,</p>
<p>Hailey</p>

---

## Post #2 by @pieper (2017-07-27 13:46 UTC)

<p>Hi Hailey -</p>
<p>Using CT for gray/white matter segmentation is be pretty hard.  Here’s a recent paper that shows good results and it should give some ideas.  The described method is not currently implemented in Slicer, but the building blocks should mostly be available.</p>
<p>-Steve</p>
<p><a href="https://www.nature.com/articles/s41598-017-00239-z" class="onebox" target="_blank">https://www.nature.com/articles/s41598-017-00239-z</a></p>

---
