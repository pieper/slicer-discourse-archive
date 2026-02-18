# 3d slicer 4.10.0 GUI can not display correctly

**Topic ID**: 4584
**Date**: 2018-10-30
**URL**: https://discourse.slicer.org/t/3d-slicer-4-10-0-gui-can-not-display-correctly/4584

---

## Post #1 by @morewd (2018-10-30 06:59 UTC)

<p>Operating system:win10 professional 1803 with latest update<br>
Slicer version:4.10.0<br>
Expected behavior: normal GUI display with “file”,“edit”,“view”,“help”  menu bars.<br>
Actual behavior:when open 3d slicer 4.10.0 , there are no  “file”,“edit”,“view”,“help”  menu bars. and the mouse position is not correctly.</p>

---

## Post #2 by @pieper (2018-10-30 11:40 UTC)

<p>Thanks for reporting <a class="mention" href="/u/dan">@Dan</a> - could you post a screenshot so we can get an idea what’s going on?  Also the error log from the Help-&gt;Report a bug menu dialog could be helpful.</p>

---

## Post #3 by @lassoan (2018-10-30 11:58 UTC)

<p>This is most likely caused by an Intel display driver bug. See this topic for details and solution: <a href="https://discourse.slicer.org/t/all-menus-and-buttons-misplaced-in-slicer-window-nighlty-build-version/3224">All menus and buttons misplaced in Slicer window (nighlty build version)</a></p>

---

## Post #4 by @morewd (2018-11-01 01:34 UTC)

<p>Hi,</p>
<p>Thanks for your reply.Please confirm the screenshot in attached.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/e/ea2451cf3e518c5fb043954f50846ff61e009d57.jpeg" data-download-href="/uploads/short-url/xpjxCZx2xZ7TF7PMRCGcVjD0XBB.jpeg?dl=1" title="4.10.0.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ea2451cf3e518c5fb043954f50846ff61e009d57_2_690x388.jpeg" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ea2451cf3e518c5fb043954f50846ff61e009d57_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ea2451cf3e518c5fb043954f50846ff61e009d57_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea2451cf3e518c5fb043954f50846ff61e009d57.jpeg 2x" data-dominant-color="C1C1CA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4.10.0.jpg</span><span class="informations">1152×648 90.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2018-11-01 02:02 UTC)

<p>Yes, this is definitely the Intel display driver bug. Intel fixed the issue, so the best is to update your display driver. Background information, affected driver versions, workarounds, etc. are described in the topic referenced above.</p>

---

## Post #6 by @morewd (2018-11-01 02:10 UTC)

<p><a class="mention" href="/u/lassoan">@Lassoan</a>  Thank you!  You are right.My laptop has intel and nvidia display card. this bug is just solved by changing intel display card to nvidia card.</p>

---

## Post #7 by @morewd (2018-11-01 05:28 UTC)

<p>my solve steps:<br>
1,uninstall 3D slicer 4.10.0 .<br>
2,open “nvidia controll panel”  --&gt; click “manage 3D setting” --&gt;  select “high performance Nvidia processor”.<br>
3,instal 3D slicer 4.10.0 agai.</p>

---
