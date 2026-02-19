---
topic_id: 26251
title: "Multivolume Mri How To Start Working With It"
date: 2022-11-15
url: https://discourse.slicer.org/t/26251
---

# Multivolume, MRI - how to start working with it?

**Topic ID**: 26251
**Date**: 2022-11-15
**URL**: https://discourse.slicer.org/t/multivolume-mri-how-to-start-working-with-it/26251

---

## Post #1 by @eNable_Polska (2022-11-15 18:19 UTC)

<p>I have an abdominal exam, MRI, contrast scan, I have a series after C+, I`d like to segment vessels, tumor and other part of abdomen. But this is multivolume exam, and I dont know how to start working with it. Could you help and tell me some instruction how to work with such of exam, where to start?<br>
Here is link to exam (anonymized) <a href="https://drive.google.com/file/d/1ccFS0NBiAKqDbQ5NFxgmsFhmBsfYDV45/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">901-+C mDIXON_ALL DYN.zip - Google Drive</a><br>
Best regards<br>
Krzysztof</p>

---

## Post #2 by @eNable_Polska (2022-11-16 20:43 UTC)

<p>Is it possible to improve this rendering?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efa05a0a42470ba36f05b748d8062ec645612d1a.jpeg" data-download-href="/uploads/short-url/ybPFnwHYWrUNJuWC8F8B7tPgXsm.jpeg?dl=1" title="Screenshot_20221116_213929" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/efa05a0a42470ba36f05b748d8062ec645612d1a_2_690x316.jpeg" alt="Screenshot_20221116_213929" data-base62-sha1="ybPFnwHYWrUNJuWC8F8B7tPgXsm" width="690" height="316" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/efa05a0a42470ba36f05b748d8062ec645612d1a_2_690x316.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/efa05a0a42470ba36f05b748d8062ec645612d1a_2_1035x474.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/efa05a0a42470ba36f05b748d8062ec645612d1a_2_1380x632.jpeg 2x" data-dominant-color="616380"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20221116_213929</span><span class="informations">1920×882 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Exam is posted above</p>

---

## Post #3 by @pieper (2022-11-18 03:04 UTC)

<p>Thanks for sharing the deidentified data.  This looks like a contrast volume time series that doesn’t match the patterns currently supported by the MultiVolume or Sequence importers, e.g. in <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMImageSequencePlugin.py#L56-L210">this logic</a>.  If someone wants to study the headers there is probably a pattern that could be added to reconstruct this correctly.  If nobody takes this up right now it should at least be captured in an issue.</p>

---
