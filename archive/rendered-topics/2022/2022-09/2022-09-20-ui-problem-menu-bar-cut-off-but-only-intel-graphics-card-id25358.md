---
topic_id: 25358
title: "Ui Problem Menu Bar Cut Off But Only Intel Graphics Card"
date: 2022-09-20
url: https://discourse.slicer.org/t/25358
---

# UI problem: menu bar cut off (but only Intel graphics card)

**Topic ID**: 25358
**Date**: 2022-09-20
**URL**: https://discourse.slicer.org/t/ui-problem-menu-bar-cut-off-but-only-intel-graphics-card/25358

---

## Post #1 by @cmartin (2022-09-20 14:19 UTC)

<p>Hi togehter,</p>
<p>I have the problem that the menu bar of 3D slicer is cut off and the mouse clicks have an offset of around 50 pixels. It seems that I’m not the only user with this problem, but the solutions I have found so far so far do not work on my laptop.</p>
<p>One solution is to activate a NVIDIA graphics card, but there is no NVIDIA graphics card in my laptop, only an Intel graphics card.</p>
<p>Another solution is to update the graphics card driver. I have an Intel HD Graphics 530, and the driver version is 21.20.16.4678 from 2017-05-17. This is the latest version, so there is no update possible. Going back one version is also no solution, since the last version is from 2006 (which is very old), and 3DSlicer does not even start with such an old version.</p>
<p>If anybody has another solution, I’m happy to try it out.</p>

---

## Post #2 by @lassoan (2022-09-20 15:30 UTC)

<p>Intel HD Graphics 530 was released 7 years ago, and the current Slicer version is only supported (tested, issues investigated, etc.) for any hardware that is not older than 5 years.</p>
<p>Nevertheless, Slicer might still work on your computer, as there seems to be many much more recent drivers for Intel HD Graphics 530 - see <a href="https://www.intel.com/content/www/us/en/support/articles/000090440/graphics.html" class="inline-onebox">List of Drivers for Intel Graphics</a> and <a href="https://www.intel.com/content/www/us/en/download/18799/intel-graphics-driver-for-windows-15-45.html" class="inline-onebox">Intel® Graphics Driver for Windows* [15.45]</a>. You can also try to use an older Slicer version (Slicer-4.x), but of course then you lose all the new features and lots of fixes.</p>

---

## Post #3 by @cmartin (2022-09-21 08:41 UTC)

<p>It’s working now, thank you very much.<br>
Previously, I used the device manager from Windows to search for new driver versions, but it did not find any.<br>
Now, I used the second link that you proposed, which is indeed a newer version (21.20.16.5174 from 2020-11-08). Somehow the device manager was not aware of this newer version.<br>
So thanks again for providing the link to the newer driver version on the Intel webpage.</p>

---
