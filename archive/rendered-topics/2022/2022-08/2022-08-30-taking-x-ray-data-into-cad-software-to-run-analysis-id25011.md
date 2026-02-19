---
topic_id: 25011
title: "Taking X Ray Data Into Cad Software To Run Analysis"
date: 2022-08-30
url: https://discourse.slicer.org/t/25011
---

# Taking X-Ray Data into CAD Software to run analysis

**Topic ID**: 25011
**Date**: 2022-08-30
**URL**: https://discourse.slicer.org/t/taking-x-ray-data-into-cad-software-to-run-analysis/25011

---

## Post #1 by @seths (2022-08-30 17:51 UTC)

<p>Hello - I am a mechanical engineer and a brand new user of Slicer3D. I have some X-ray data of a spine and I am wanting to bring parts of that data into a Finite Element Analysis software to apply different loading conditions to the spine. However, I need help on the intermediary step (using 3D Slicer) to bring the X-ray into CAD. Can anyone guide me on how to best approach this? I think my application is simple enough, but not 100%. I would greatly appreciate any input on this subject!<br>
Thank you for your time.</p>

---

## Post #2 by @lassoan (2022-08-30 18:08 UTC)

<p>First you need to segment the spine CT and then generate a volumetric mesh from the segmentation. Many people use 3D Slicer for these and this topic has been discussed quite intensively on this forum. You can find the relevant post by <a href="https://discourse.slicer.org/search?q=spine">searching for “spine” on this forum</a>. If you have any specific questions then feel free to ask here.</p>

---

## Post #3 by @seths (2022-08-31 01:09 UTC)

<p>Hi Andras thank you for getting back to me. Unfortunately, I do not have CT data of the spine only X-rays. Is there a way to segment the spine using X-ray data not CT data to then take into CAD for analysis?</p>
<p>Thanks for your time.<br>
Seth</p>

---

## Post #4 by @lassoan (2022-08-31 03:00 UTC)

<p>You cannot reconstruct a 3D spine from just a few projection images. To reconstruct a 3D volume from projection images, you would need dozens (bet preferably hundreds) of projections.</p>
<p>You may be able to generate 3D volumes from less projections if you build shape models (e.g., statistical shape models) or train an AI network (e.g., GAN) for volume reconstruction.</p>

---
