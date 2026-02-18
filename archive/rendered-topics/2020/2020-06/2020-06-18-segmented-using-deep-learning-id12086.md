# Segmented using deep learning

**Topic ID**: 12086
**Date**: 2020-06-18
**URL**: https://discourse.slicer.org/t/segmented-using-deep-learning/12086

---

## Post #1 by @khikho (2020-06-18 08:26 UTC)

<p>HI<br>
•	I have a problem when running  TOMAAT not running and exiting ?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a65195688279e3a8c5e66aaef534332f82d0618.png" alt="image" data-base62-sha1="8kAip4lWw6uO6bXcZWP6DhLQI1W" width="390" height="270"><br>
•	I installed DeepInfer and that’s next steps ((extensions manager + install + restart)) But when I go to the front slicer 3d, I can’t find it ?<br>
•	Can the spine be segmented using NVidia AIAA extension ?</p>

---

## Post #2 by @lassoan (2020-06-18 21:36 UTC)

<p>I would only consider DeepInfer and TOMAAT to be useful mainly for learning purposes, to see what approaches can be used to run inference within Slicer.</p>
<p>The only currently actively developed and well supported method is NVidia’s AIAA extension. You can train your own models using NVidia Clara and use the trained model in 3D Slicer using this extension.</p>
<p>I’m not aware of a publicly available spine segmentation deep learning model, but if you find one then it should be possible to make it available in NVidia AIAA.</p>
<p>If there is no existing model then you can create one, by segmenting a few hundred images using manual/semi-automatic tools in Slicer’s Segment Editor, then use those for training a network. You can try any general-purpose frameworks or those specialized to medical images, such as <a href="https://developer.nvidia.com/clara">NVidia Clara Train</a> (the resulting model can be directly uploaded to be used by NVidia AIAA), <a href="https://towardsdatascience.com/ten-eisen-features-that-changed-the-way-i-do-deep-learning-f0358f664dec">Eisen</a> (it automates a lot of tasks), niftynet, etc.</p>

---
