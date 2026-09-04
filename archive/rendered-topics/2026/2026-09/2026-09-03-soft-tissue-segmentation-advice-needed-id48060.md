---
topic_id: 48060
title: "Soft-tissue segmentation: advice needed"
date: 2026-09-03
url: https://discourse.slicer.org/t/48060
last_bumped: 2026-09-03T22:20:55.562Z
---

# Soft-tissue segmentation: advice needed

**Topic ID**: 48060
**Date**: 2026-09-03
**URL**: https://discourse.slicer.org/t/soft-tissue-segmentation-advice-needed/48060

---

## Post #1 by @Toumia_Bessedik (2026-09-03 22:20 UTC)

<p>Hello,</p>
<p>I would like to get your opinion on an approach I am currently using to refine the segmentation of soft tissues in a head MRI.</p>
<p>I used TotalSegmentator (MR) to automatically segment the soft tissues, particularly fat and muscle. I then defined an external 3 mm layer from the outer surface of the head, which I am currently assuming represents the dermal/skin layer. The remaining soft-tissue regions that are not classified as fat or muscle were grouped into a fourth region that I called “Others”.</p>
<p>This gives me four distinct material regions:</p>
<ul>
<li>
<p>Skin/dermal layer: 3 mm external layer</p>
</li>
<li>
<p>Fat</p>
</li>
<li>
<p>Muscle</p>
</li>
<li>
<p>Others</p>
</li>
</ul>
<p>This is part of a research project focused on hearing protection and the study of sound propagation through the tissues of the head. The objective is mainly technological/modeling-oriented, rather than clinical or anatomical diagnosis.</p>
<p>My main question is whether this level of differentiation seems relevant for an acoustic/biomechanical model. In particular:</p>
<ul>
<li>
<p>Is it reasonable to consider four distinct materials?</p>
</li>
<li>
<p>Would it be appropriate to interpret the “Others” region as mainly epidermis/other superficial soft tissues, or would you recommend treating it differently?</p>
</li>
<li>
<p>More generally, does this segmentation approach seem physically meaningful for studying sound propagation through the soft tissues?</p>
</li>
</ul>
<p>I would greatly appreciate any feedback or recommendations on how you would approach this segmentation.</p>

---
