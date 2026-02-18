# Multimodality imaging registration

**Topic ID**: 38151
**Date**: 2024-09-02
**URL**: https://discourse.slicer.org/t/multimodality-imaging-registration/38151

---

## Post #1 by @Mouadh_Ben_Nasr (2024-09-02 01:23 UTC)

<p>I am actually struggling with a project using multi-modalities to evaluate minimal distance between a treated area and tumor.<br>
I am using CE CT and/or MRI for pre procedural images and 90Y PETCT or MRI images as post procedural images.<br>
I am looking for a method to superpose radiation volume and tumor, based on Liver contours most likely.<br>
I am facing problems:</p>
<ul>
<li>when importing PETCT/MRI images, there is an error message for space orientation and image scaling.</li>
<li>As the metabolic image (radiation volume) and low resolution image in PET are been uploaded in 2 different volumes, how to merge their segmentations into one segmentation node?</li>
<li>I do liver and tumor segmentations in MRI/CT images</li>
<li>How to superpose the segmentations obtained using liver contours (couldn’t find an extension).</li>
<li>Calculating minimal distances  is obtained by model to model distance, the distance map is visualized as 3D map superposed to tumor. How to display it as a matrix?</li>
</ul>
<p>Do you have other suggestions?</p>
<p>Thank you in advance for your time.</p>

---

## Post #2 by @pieper (2024-09-02 14:32 UTC)

<p>What you describe sounds very feasible, but there are no easy answers to your list of questions.  But if you study the literature, examples, code, etc you can learn to do all the things on your list, or at least learn what’s feasible to accomplish with existing tools and what might need more develoment.</p>

---
