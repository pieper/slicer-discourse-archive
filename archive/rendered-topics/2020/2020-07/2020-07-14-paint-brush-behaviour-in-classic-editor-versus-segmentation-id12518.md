# Paint brush behaviour in Classic Editor versus Segmentation Editor

**Topic ID**: 12518
**Date**: 2020-07-14
**URL**: https://discourse.slicer.org/t/paint-brush-behaviour-in-classic-editor-versus-segmentation-editor/12518

---

## Post #1 by @Jaswant (2020-07-14 03:38 UTC)

<p>I am a novice, so please re-direct to the feature that I would like to use. I am working with whole body contrast CT data set from a dog for teaching and 3D printing purspose.</p>
<p>Previously, I used classical editor to Threshold paint (with selected upper and lower pixel values) with “Paint over” option being unchecked. That allowed to select only those pixels within my selection range so it was a quick method to segment a bone for example and make a model.</p>
<p>I would like to use similar threshold painting in the Segmentation Editor on 30 to40% slices so that I could fill in the rest of the slices by using the “Fill slices” tool. Please help!</p>

---

## Post #2 by @lassoan (2020-07-14 03:44 UTC)

<p>This works exactly the same way in Segment Editor: select Threshold effect to set threshold range, then click “Use for masking”.</p>
<p>Note that there are so many and so much better segmentation tools in Segment Editor that most likely you will be able to segment much faster and achieve higher quality results. Check out this <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">segmentation overview</a> and <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation">segmentation tutorials</a>. We can also help with specific advice if you share some more details about what you want to segment and provide a few screenshots that illustrate the main challenges.</p>

---
