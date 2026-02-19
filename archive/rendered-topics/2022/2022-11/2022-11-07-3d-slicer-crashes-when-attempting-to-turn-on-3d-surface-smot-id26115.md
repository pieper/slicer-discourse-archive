---
topic_id: 26115
title: "3D Slicer Crashes When Attempting To Turn On 3D Surface Smot"
date: 2022-11-07
url: https://discourse.slicer.org/t/26115
---

# 3D Slicer crashes when attempting to turn on 3D surface smothing

**Topic ID**: 26115
**Date**: 2022-11-07
**URL**: https://discourse.slicer.org/t/3d-slicer-crashes-when-attempting-to-turn-on-3d-surface-smothing/26115

---

## Post #1 by @granizado (2022-11-07 16:31 UTC)

<p>Hi,</p>
<p>One year ago I was doing segmentation of a sample. To speed up the process I turned off the surface smooting. Now I opened the file on a powerful workstation wanting to smooth the 3D model, but every time when I try to hit the surface smoothing bottom the programme instantly crashes. Do you have any advice?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2022-11-07 19:07 UTC)

<p>After you restart Slicer, please check select in menu “Help” → “Report a bug”, choose log file of the <em>previous session</em>, and see if there are any errors or warnings that could give a hint about what went wrong.</p>
<p>Also try the latest Slicer Preview release to see if it has any problems with applying smoothing.</p>
<p>If we don’t get any specific information from these above, then we would probably need your scene (saved as a single-file .mrb) so that we can investigate further.</p>

---
