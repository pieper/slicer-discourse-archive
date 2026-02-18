# 3D View Lag when Hundreds of Models Loaded and OpenIGTLinkIF Running

**Topic ID**: 12792
**Date**: 2020-07-30
**URL**: https://discourse.slicer.org/t/3d-view-lag-when-hundreds-of-models-loaded-and-openigtlinkif-running/12792

---

## Post #1 by @Ryan_Morrison (2020-07-30 15:48 UTC)

<p>Slicer Version: 4.11.0<br>
PC: Windows 10, AMD 8320, 8Gb RAM, GTX660ti 3Gb</p>
<p>My issue comes in the second I turn on <a href="http://www.slicerigt.org/wp/" rel="nofollow noopener">OpenIGTLinkIF</a> to view live <a href="https://www.ndigital.com/msci/products/drivebay-trakstar/" rel="nofollow noopener">motion tracker data</a> when ~500 models are loaded into the 3D View. Slicer lags significantly (<a href="https://youtu.be/cgYqOi3Z6d0" rel="nofollow noopener">video</a>). If only a few models are loaded, slicer very smoothly displays the motion tracker data (<a href="https://youtu.be/LBU31D8MB3A" rel="nofollow noopener">video</a>). My CPU, memory, and GPU usage are <strong>not</strong> near maximum usage.</p>
<p>Is there any remedy to my issue? I know this combined task of having hundreds of models loaded while running OpenIGTLinkIF to import live motion data is demanding for slicer, but I was really hoping I could have both running simultaneously.</p>

---

## Post #2 by @lassoan (2020-07-30 16:24 UTC)

<p>Thanks for reporting, I don’t think there is a good reason for this to happen. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> could you check if there is an easy fix? If the fix is not trivial, then we could think about various workarounds.</p>

---

## Post #3 by @lassoan (2020-08-02 03:18 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> has <a href="https://github.com/Slicer/Slicer/pull/5075">fixed the update performance issue</a>. Refresh speed should be good in Slicer Preview Release downloaded on Monday or later.</p>

---

## Post #4 by @Ryan_Morrison (2020-08-03 19:40 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>! I’ll give that a shot and see if it fixes the problem.</p>

---

## Post #5 by @Ryan_Morrison (2020-08-04 02:27 UTC)

<p>So it’s still an issue even after updating the preview release version 4.11.0 revision 29250 built 2020-08-03. It may be because the .obj and .stl files have a large file sizes due to the files being modeled after a full sized adult male. Here is the link to the <a href="https://drive.google.com/drive/folders/1mjIl521pzQ4rwyhzpkNtsCfRC-wnLe3R?usp=sharing" rel="nofollow noopener">google drive with all the files</a>. Even viewing all of the files in the 3D view is shows a lag.</p>

---
