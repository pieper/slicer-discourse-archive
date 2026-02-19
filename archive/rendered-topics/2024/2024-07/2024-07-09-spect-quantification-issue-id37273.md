---
topic_id: 37273
title: "Spect Quantification Issue"
date: 2024-07-09
url: https://discourse.slicer.org/t/37273
---

# SPECT quantification issue

**Topic ID**: 37273
**Date**: 2024-07-09
**URL**: https://discourse.slicer.org/t/spect-quantification-issue/37273

---

## Post #1 by @Jan_Lennart (2024-07-09 07:56 UTC)

<p>Hi Slicer Users,</p>
<p>I desperately need some help here. I would like to quantify a few SPECT images and wanted to calculate the calibration factor of a the protocol/camera by looking at a phantom scan.</p>
<p>When I place a few segments in the phantom (outside the hotter spheres) I get values of around 6000-6700 counts. In other programs like VivoQuant or Hermes Affinity, the results are more like 3500 counts.</p>
<p>Does anybody know why there is this discrepancy?</p>
<p>Thank you so much,<br>
Jan</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/6138a40f9d64216c01394a862a647c9657cdff50.png" data-download-href="/uploads/short-url/dS3FmqbV14XAfb4VKMHIM5ZvsYw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/6138a40f9d64216c01394a862a647c9657cdff50_2_690x382.png" alt="image" data-base62-sha1="dS3FmqbV14XAfb4VKMHIM5ZvsYw" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/6138a40f9d64216c01394a862a647c9657cdff50_2_690x382.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/6138a40f9d64216c01394a862a647c9657cdff50_2_1035x573.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/6138a40f9d64216c01394a862a647c9657cdff50_2_1380x764.png 2x" data-dominant-color="696965"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1839×1020 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @MAY (2024-07-24 08:24 UTC)

<p>Hello, I would like to ask you, how do you get these counts? What plug-ins are used? I would appreciate it if you could provide me with this information.</p>

---

## Post #3 by @Jan_Lennart (2024-07-24 08:34 UTC)

<p>this was done with the module “segment statistics” (no plug in was used)</p>

---

## Post #4 by @MAY (2024-07-25 15:37 UTC)

<p>Thank you very much. I have another question. Do you know the meanings of mean, voxel count (LM) and voxel count (SV) respectively in the picture?</p>

---

## Post #5 by @akmal871026 (2024-09-05 01:57 UTC)

<p>Dear <a class="mention" href="/u/jan_lennart">@Jan_Lennart</a> ,</p>
<p>In segment statistics, It just gave you the mean count in the segment. If you want to know total counts of your segments, you have to multiply mean count with voxel counts.  Then you will get the total counts.</p>
<p>6000-6700 counts as you mentioned is what? mean? or min? or total?</p>
<p>then 3500 counts using Hermes is what? mean? or min? or total?</p>

---
