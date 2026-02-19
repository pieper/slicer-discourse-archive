---
topic_id: 40128
title: "Slice Interval Advice"
date: 2024-11-11
url: https://discourse.slicer.org/t/40128
---

# Slice interval advice

**Topic ID**: 40128
**Date**: 2024-11-11
**URL**: https://discourse.slicer.org/t/slice-interval-advice/40128

---

## Post #1 by @SuperMatt (2024-11-11 18:34 UTC)

<p>Hi, I’m a novice user of 3D slicer without a medical radiations background (other science).</p>
<p>I have a CT scan collected on a Canon Vitrea machine but when I import into 3D slicer the dimensions appear incorrect for the coronal and sagittal views, both elongated (approx 2-fold?). I’m told the slice interval should be 0.8mm with a 1mm thickness but I’m unsure how to rescale the images with these values? Could someone with more experience let me know what these fields should be, and perhaps explain why? Thanks very much in advance<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04a5c0af3616881093a188b481afbbc8cbe47f0c.jpeg" data-download-href="/uploads/short-url/F724bweHgT9kywQE2sN4RfKaDi.jpeg?dl=1" title="1_dimensions" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04a5c0af3616881093a188b481afbbc8cbe47f0c.jpeg" alt="1_dimensions" data-base62-sha1="F724bweHgT9kywQE2sN4RfKaDi" width="617" height="406"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1_dimensions</span><span class="informations">617×406 36.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-11-11 19:18 UTC)

<p>You can type the 0.8 value into the third entry of the Image Spacing row.  But you probably also need to find out the in-plane pixel spacing (the first two entries).  The fact that your data is unsigned char (0 to 255) means you probably have loaded from some kind of consumer image format that doesn’t store spacing metadata.  You would be better off to use the original DICOM.</p>

---

## Post #3 by @SuperMatt (2024-11-11 21:46 UTC)

<p>Thanks very much Steve, yes, I suspected as much that this was pared back DICOM data but was told this was the only scan data available. I used MicroDICOM to view the metadata which noted the pixel spacing was 0.429 / 0.429 and the scans look much better now.</p>
<p>Thanks so much for the help and explanation!</p>

---
