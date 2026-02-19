---
topic_id: 17169
title: "Brain Volume Mri"
date: 2021-04-19
url: https://discourse.slicer.org/t/17169
---

# Brain volume MRI

**Topic ID**: 17169
**Date**: 2021-04-19
**URL**: https://discourse.slicer.org/t/brain-volume-mri/17169

---

## Post #1 by @amjadibr (2021-04-19 12:48 UTC)

<p>Hi everyone, I am trying to measure the whole brain volume in MRI. I don’t know if the Slicer is the right tool to do it.<br>
The result would be numbers representing the volume of the whole brain</p>
<p>Thank you in advance</p>

---

## Post #2 by @pieper (2021-04-19 16:11 UTC)

<p>If you have compatible images you might be better off with something like <a href="https://surfer.nmr.mgh.harvard.edu/">freesurfer</a> or other software you can learn about at neuroimaging sites like <a href="https://neurostars.org/">neurostars</a>.</p>
<p>Within Slicer the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SwissSkullStripper">skull stripper extension</a> can also work well with the Label Statistics to get the volume.</p>

---
