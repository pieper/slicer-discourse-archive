---
topic_id: 46670
title: "Landmark Based Alignment Of Separate Ct Elements"
date: 2026-04-06
url: https://discourse.slicer.org/t/46670
---

# Landmark-based alignment of separate CT elements

**Topic ID**: 46670
**Date**: 2026-04-06
**URL**: https://discourse.slicer.org/t/landmark-based-alignment-of-separate-ct-elements/46670

---

## Post #1 by @JaredAmudeo (2026-04-06 14:54 UTC)

<p>Dear all,<br>
I hope you are doing well. I am reaching out in search of guidance and advice.</p>
<p>I would like to know whether it is possible, using landmarks or point-based methods (I am not very familiar with this, so I apologize if I misuse the terminology), to assemble or “retro-deform” separate elements directly within 3D Slicer.</p>
<p>To explain my case: I have three separate medical CT scans of the posterior portion of a dinosaur skull. These correspond to three elements that were preserved separately (the exoccipital complex, basisphenoid, and left prootic), but the elements articulate anatomically.</p>
<p>Previously, I aligned these elements in Blender to create a unified model, but the process was quite tedious. I am wondering if there is a way in 3D Slicer to define corresponding points between elements for example, placing points along the fracture surfaces between the prootic and opisthotic on both elements and then have the software align them accordingly.</p>
<p>Thank you very much in advance for your help.</p>

---

## Post #2 by @pieper (2026-04-06 15:01 UTC)

<p>These links should help:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/fiducialregistration.html">https://slicer.readthedocs.io/en/latest/user_guide/modules/fiducialregistration.html</a></p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">https://slicer.readthedocs.io/en/latest/user_guide/registration.html</a></p>

---
