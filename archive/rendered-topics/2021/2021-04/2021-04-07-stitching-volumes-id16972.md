# Stitching volumes

**Topic ID**: 16972
**Date**: 2021-04-07
**URL**: https://discourse.slicer.org/t/stitching-volumes/16972

---

## Post #1 by @mohammed_alshakhas (2021-04-07 04:36 UTC)

<p>i have neck and chest ct for same patient but in different series , is it possible to stitch the two ?<br>
thanks</p>

---

## Post #2 by @muratmaga (2021-04-07 04:53 UTC)

<p>As long as two series line up correctly (one continues from where the other left), one way to achieve merging:</p>
<ol>
<li>Use CropVolume to create a new volume that will encompass the full size of the combined volumes by defining a new ROI (you will probably have to go back and forth between your two series to make sure ROI spans the entire size)</li>
<li>Then use the Add Volumes module, to combine two series and specify the output volume as the volume from step 1.</li>
</ol>
<p>I am sure there are other ways too.</p>

---

## Post #3 by @mohammed_alshakhas (2021-04-07 05:20 UTC)

<p>Unfortunately there is overlap between two volumes</p>

---

## Post #4 by @pieper (2021-04-07 11:57 UTC)

<p>You can still use the method <a class="mention" href="/u/muratmaga">@muratmaga</a> suggested, just add a step to use CropVolume to cut off the overlapping part from one or the other series.</p>

---

## Post #5 by @lassoan (2022-10-20 15:11 UTC)

<p>Just in case somebody comes across this topic now: <a class="mention" href="/u/mikebind">@mikebind</a> recently contributed the <a href="https://github.com/PerkLab/SlicerSandbox#stitch-volumes">Stitch Volumes module</a> for stitching multiple volumes into one. It is available in Sandbox extension.</p>

---
