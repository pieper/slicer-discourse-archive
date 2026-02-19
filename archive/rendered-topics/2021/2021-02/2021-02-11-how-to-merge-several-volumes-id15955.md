---
topic_id: 15955
title: "How To Merge Several Volumes"
date: 2021-02-11
url: https://discourse.slicer.org/t/15955
---

# How to merge several volumes?

**Topic ID**: 15955
**Date**: 2021-02-11
**URL**: https://discourse.slicer.org/t/how-to-merge-several-volumes/15955

---

## Post #1 by @josephMeng (2021-02-11 17:16 UTC)

<p>Dear community,</p>
<p>Currently I am trying to <strong>merge several volumes into one large volume</strong>. This is what I have so far:</p>
<p>-<strong>Several volumes</strong> loaded into Slicer. The volumes were taken from one patient and show slightly different regions (e.g. volume 1 shows the segments of the liver right to the vena cava, volume 2 the segments left to the vena cava).<br>
-The <strong>volumes do include overlapping areas</strong> which shall be used in order to register the volumes and merge them into one large volume<br>
-As the volumes were taken at slightly different times, the <strong>registration has to balance</strong> not only <strong>translational and rotational</strong> differences between the volumes but also <strong>warping</strong> that results from altered tissue configuration (i.e. due to heartbeat and breathing).</p>
<p><strong>What would be the best way to do this?</strong><br>
Thank you very much in advance!!!</p>

---

## Post #2 by @lassoan (2021-02-11 17:38 UTC)

<p>This all sounds very doable.</p>
<ul>
<li>Choose one of the volume as “reference” and align/warp the images to each other using any of the manual or automatic <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">registration methods</a> that supports non-linear warping.</li>
<li>Expand the reference volume to a cover the entire region that you are interested in using Crop volume module</li>
<li>Resample all the volumes using this expanded reference volume as “reference”</li>
<li>Combine the volumes, probably quickest to do it with a few numpy commands</li>
</ul>
<p>Stitching of volumes has come up a few times on this forum, so you can find more detailed instructions for each step by searching here, but if anything is not clear then let us know.</p>
<p>If you need to do this regularly then it is probably worth creating a script (or module) for this that automates most of the steps.</p>

---
