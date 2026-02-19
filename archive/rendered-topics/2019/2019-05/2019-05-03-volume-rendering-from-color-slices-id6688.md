---
topic_id: 6688
title: "Volume Rendering From Color Slices"
date: 2019-05-03
url: https://discourse.slicer.org/t/6688
---

# Volume rendering from color slices

**Topic ID**: 6688
**Date**: 2019-05-03
**URL**: https://discourse.slicer.org/t/volume-rendering-from-color-slices/6688

---

## Post #1 by @sreyankar (2019-05-03 19:17 UTC)

<p>Hi, I have a stack of color images with predefined colormap in matlab. Is it possible to get volume rendering while preserving the colormap? The only options I am getting are the pre set volume color maps.</p>

---

## Post #2 by @lassoan (2019-05-03 19:19 UTC)

<p>Direct volume rendering of RGBA volumes is very uncommon, so we did not expose it on the GUI. You can <a href="https://discourse.slicer.org/t/merge-colored-images-and-show-them-as-1-volume/6472/6">enable it by typing a single line of code in the console</a>.</p>

---

## Post #3 by @sreyankar (2019-05-03 20:41 UTC)

<p>Thank so much for the quick reply. I tried your suggestion and created an alpha stack and merged with the RGB stack. For the volume rendering I turned off the independent components. However, when I do the volume rendering it is still rendering it only on the scalar volume. Am I doing something wrong?<br>
Thanks</p>

---

## Post #4 by @lassoan (2019-05-03 20:52 UTC)

<p>Use GPU volume rendering and latest stable version. If does not work then maybe you could share your scene so that we can test it, too.</p>

---
