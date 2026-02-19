---
topic_id: 19647
title: "Change Roi Box Color Python"
date: 2021-09-13
url: https://discourse.slicer.org/t/19647
---

# Change ROI box color? (Python?)

**Topic ID**: 19647
**Date**: 2021-09-13
**URL**: https://discourse.slicer.org/t/change-roi-box-color-python/19647

---

## Post #1 by @hherhold (2021-09-13 14:22 UTC)

<p>Hey all,</p>
<p>Sometimes I use a white background in the 3D view as it matches color plates being prepared for publications. ROI cubes in the 3D view are drawn with white lines, making the box basically disappear. Is there some python I can use to change these lines to black? Not asking for any specific UI tweaks, changes, whatever - I realize this is likely a niche use case; just wondering if there is a back door to change the box line color.</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @pieper (2021-09-13 14:53 UTC)

<p>You can do this already with a Markups ROI by setting the color and turning off fill in the display settings.  Are you able to use those instead?  With the older Annotation ROI you could hack something by getting the Renderer from the threeD widget and iterating through the actors, which would be fragile but could solve your problem.  If you are writing a script it might be better to convert Annotation ROIs into Markups ROIs and set the color that way.</p>

---

## Post #3 by @hherhold (2021-09-13 14:57 UTC)

<p>Ah, okay! I will give this a shot.</p>
<p>Thanks Steve!</p>

---
