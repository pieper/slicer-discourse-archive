# Exporting labelmap without croped dimensions

**Topic ID**: 12342
**Date**: 2020-07-02
**URL**: https://discourse.slicer.org/t/exporting-labelmap-without-croped-dimensions/12342

---

## Post #1 by @DiamondKMG (2020-07-02 17:38 UTC)

<p>Problem report for Slicer 4.11.0-2020-06-30 linux-amd64:<br>
When I export a set of segments to a labelmap, if I don’t select a reference volume under the advanced tab of the ‘export/import models and labelmaps’ portion of the ‘Segmentations’ module, the latest version of Slicer crops the volume of the labelmap instead of keeping the volume of the label map the same as the volume used to create the segments/ labelmap.<br>
Previous versions kept the dimensions of exported labelmaps the same as the volumes used to create segmentations. Its there any way to get the default to keep the volume dimensions the same when exporting labelmaps?</p>

---

## Post #2 by @lassoan (2020-07-03 01:27 UTC)

<p>I cannot reproduce this. Maybe you have opened a segmentation file that was created with an older Slicer version? If not, then please give step-by-step instructions of what you did (start slicer, load X sample data set, go to Segment Editor module, …).</p>

---

## Post #3 by @DiamondKMG (2020-07-03 15:28 UTC)

<p>Before the June 30th preview version of slicer, my work flow was:<br>
Start slicer. Load a segment (.seg.nrrd) and corresponding volume data (.nrrd). In the Segmentations module expand the ‘Export/import models and labelmaps’, select Export for operation and Labelmap for output type and create a new node. This would give me a labelmap with the same dimensions as the corresponding volume data with the label of 0 for any areas that there were no labels.</p>
<p>As of the June 30th preview, if I follow this same protocol the output is a labelmap that is cropped to only include the space immediately surrounding the labels, so a different dimension than the corresponding volume.</p>
<p>Murat did find a work around that if when I export the labelmap, under the advanced options I can choose a ‘reference volume’. When I do this I do export labelmaps with the same volumes as the original volumes.</p>

---

## Post #4 by @DiamondKMG (2020-07-03 16:51 UTC)

<p>Also I believe the segment files (.seg.nrrd) were created using the 6/15 preview</p>

---

## Post #5 by @lassoan (2020-07-03 16:58 UTC)

<p>Thank you, these instructions were helpful. I was able to reproduce the behavior: if you load a saved segmentation and then export it to labelmap node then the minimum necessary extent is used.</p>
<p>While the current behavior is correct (and optimizes memory usage), I see how it can be unexpected for users and agree that it would be more convenient if the original extent would be used by default, mainly for better compatibility with software that ignores physical space information.</p>
<p>I’ve <a href="https://github.com/Slicer/Slicer/commit/a9cf5395792d44e3d7446b8ca09e41684660b91d">changed</a>  the default behavior now, so in tomorrow’s Slicer Preview Release the export will work as you expect .</p>

---
