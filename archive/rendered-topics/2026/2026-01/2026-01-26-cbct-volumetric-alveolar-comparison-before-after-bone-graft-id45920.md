---
topic_id: 45920
title: "Cbct Volumetric Alveolar Comparison Before After Bone Graft"
date: 2026-01-26
url: https://discourse.slicer.org/t/45920
---

# CBCT volumetric alveolar comparison before after bone graft

**Topic ID**: 45920
**Date**: 2026-01-26
**URL**: https://discourse.slicer.org/t/cbct-volumetric-alveolar-comparison-before-after-bone-graft/45920

---

## Post #1 by @Zah (2026-01-26 10:35 UTC)

<p>Hi there, I am totally new to slicer and would like to use it for a research study where volumetric changes of alveolar bone is measured before and after grafting. I have gone through the tutorials and there is a quantitative imaging tutorial, however this is only helpful in measuring volumetric change in pathologic lesions with well circumscribed margins. I basically need to align and superimpose two dicom images T1 and T2 and measure horizontal and vertical difference between the two over a defined area, an extraction socket. I would greatly appreciate it if someone could point me in the right direction.</p>

---

## Post #2 by @drnoorfatima (2026-02-17 12:45 UTC)

<p>Hi!</p>
<p>This is a really well defined research question and you’re right that the standard quantitative imaging tutorial doesn’t quite cover this use case, the registration and superimposition of two timepoints with localized volumetric measurement over a specific region like an extraction socket is a different workflow entirely.</p>
<p>The tricky part here isn’t the measurement itself, it’s getting the two DICOM datasets accurately aligned first. With CBCT data especially, even small misregistrations compound into significant volumetric errors which can undermine the research findings.</p>
<p>I work with medical image registration and segmentation workflows and have a clinical background, so this kind of before/after comparative analysis is something I’m familiar with on both the technical and research methodology side.</p>
<p>DM me if you need my help! happy to help you get this right.</p>

---
