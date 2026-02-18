# Image is not aligned with segmentation

**Topic ID**: 12190
**Date**: 2020-06-23
**URL**: https://discourse.slicer.org/t/image-is-not-aligned-with-segmentation/12190

---

## Post #1 by @Gourav_Modanwal (2020-06-23 20:11 UTC)

<p>Hi,</p>
<p>I also faced a similar problem while importing a .stl file (3D segmentation) in Slicer 3D. My segmentation is off the location. The imported segmentation is of the same patient and generated using TeraRecon Aquarius Intuition. How can I ensure that the imported segmentation in Slicer 3D matches with the CT Volume?</p>
<p>Thanks</p>

---

## Post #2 by @muratmaga (2020-06-23 23:02 UTC)

<p>Are you using a recent preview version (4.11)? If so, try loading the loading the STL as a model (as oppose to segmentation) and check the option and try different coordinate systems to import (RAS vs LPS). If the model shows up in the right space, then you can use the <code>Segmentations</code> module to import it as a segmentation.</p>

---

## Post #3 by @Gourav_Modanwal (2020-06-25 05:58 UTC)

<p>Thanks!<br>
It worked with the latest version 4.11.</p>

---
