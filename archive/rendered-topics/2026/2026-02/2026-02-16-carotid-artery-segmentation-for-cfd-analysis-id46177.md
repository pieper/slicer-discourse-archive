# Carotid Artery Segmentation for CFD analysis

**Topic ID**: 46177
**Date**: 2026-02-16
**URL**: https://discourse.slicer.org/t/carotid-artery-segmentation-for-cfd-analysis/46177

---

## Post #1 by @Arundhati (2026-02-16 16:51 UTC)

<p>Is there any tutorial to create 3D carotid artery to be used for CFD analysis by using any of the sample images available in the 3D slicer itself ?</p>

---

## Post #2 by @drnoorfatima (2026-02-17 08:35 UTC)

<p>Yes it’s doable with the sample data! I’ve actually worked on a very similar pipeline recently.<br>
Honestly I haven’t come across a good end-to-end tutorial for this specific use case , most resources either stop too early or assume you already know the CFD side.<br>
What’s the end goal, research or a specific project? The approach can vary quite a bit depending on that.</p>

---

## Post #3 by @Arundhati (2026-02-17 10:49 UTC)

<p>First of all Thank you for your response…My goal is to do research in CFD.. I want to create 3 D geometry to be used in Ansys for CFD analysis.. My professor will provide me the patient specific images.. I’ll have to create 3 - D model for analysis… So, I was asked to learn this software as early as possible.. However, I want more YouTube or Online resources..</p>

---

## Post #4 by @drnoorfatima (2026-02-17 11:08 UTC)

<p>That’s a great research direction!</p>
<p>Honestly for patient-specific geometry and ANSYS CFD prep specifically, I haven’t come across YouTube resources that cover the full pipeline end to end , most stop at the segmentation and don’t touch the mesh cleanup, capping, and solver-ready geometry side which is where the real work is for ANSYS.</p>
<p>The learning curve is steeper than most tutorials suggest, especially with patient-specific images where every case is different.</p>
<p>Since you’re working under a professor with a research deadline, it might actually save you a lot of time to have someone walk you through it on your actual data rather than piecing it together from scattered resources.</p>
<p>Best of Luck!</p>

---
