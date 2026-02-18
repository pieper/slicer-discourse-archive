# Export images with window width end level settings

**Topic ID**: 6348
**Date**: 2019-04-01
**URL**: https://discourse.slicer.org/t/export-images-with-window-width-end-level-settings/6348

---

## Post #1 by @n2018 (2019-04-01 04:33 UTC)

<p>Hi,<br>
could you please tell me if it is possible to export images from slicer with contrast settings?<br>
I adjust contrast but when I export these images and open them in other programs images look like previous one without any contrast adjustments</p>

---

## Post #2 by @Amine (2019-04-01 07:02 UTC)

<p>Under Volume module you can find the displayed threshold, by changing “manual W/L” to “manual min/max” , note the values then go to “simple filters module” then select “intensityWindowingImagefilter” in the list and enter your min/max values and apply, your volume should be converted to the intensity you specified.</p>

---
