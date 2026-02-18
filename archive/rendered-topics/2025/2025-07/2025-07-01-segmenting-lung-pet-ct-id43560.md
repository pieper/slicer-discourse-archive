# Segmenting lung PET/CT

**Topic ID**: 43560
**Date**: 2025-07-01
**URL**: https://discourse.slicer.org/t/segmenting-lung-pet-ct/43560

---

## Post #1 by @ScleroPID (2025-07-01 12:43 UTC)

<p>Hi, I’m new to 3D Slicer and still trying to get the hang of it. I would really appreciate your help with a few questions:</p>
<ol>
<li>
<p>I’m looking for an easy and reproducible way to segment lung CT scans. I’ve tried using the Segment Editor with the Threshold tool, but it segments the entire scan instead of just the lungs. Is there a way to restrict the segmentation to a region, like setting margins or a predefined ROI? Or maybe there’s a better tool for lung segmentation?</p>
</li>
<li>
<p>Within this lung ROI, I’d like to extract PET metrics such as SUVmax, MTV, and TLG, using a threshold like SUV &gt; 2.5. Is there an extension that allows for this? I came across PETTumorSegmentation and PET SUV Must Segmenter, but I wasn’t sure how to use them to get these values.</p>
</li>
<li>
<p>I’m also having trouble displaying fused PET/CT images. Even with the PETDICOMExtension installed, I can’t seem to find an easy way to display fusion views. Is there a simple and reliable method to visualize PET over CT?</p>
</li>
</ol>
<p>Thanks in advance for your help!</p>

---

## Post #2 by @Xiaojie_Guo (2025-07-04 02:28 UTC)

<p>Use TotalSegmentator to segment lung CT.</p>

---
