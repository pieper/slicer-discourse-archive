---
topic_id: 20133
title: "Calculating Volumes From Image Stacks Scale Does Not Match U"
date: 2021-10-13
url: https://discourse.slicer.org/t/20133
---

# Calculating volumes from image stacks, scale does not match up.

**Topic ID**: 20133
**Date**: 2021-10-13
**URL**: https://discourse.slicer.org/t/calculating-volumes-from-image-stacks-scale-does-not-match-up/20133

---

## Post #1 by @Jeroen_n (2021-10-13 12:20 UTC)

<p>Im working on a project where i need to determine the volume of fibrosis in cochlea’s. the raw data consists of +/- 100 microscopic photo’s of the cut up cochlea that i aligned and stacked in order(.tiff file). I coloured the segments ( bone; internal space; fibrosis) and tried to use segment statistics to find the volumes of the different segments. when i did this however i got volumes in the thousands cm3. The size differences between the segments seem right but the scale is not.</p>
<p>Can i fix this in a way that will get me an accurate volume size?</p>

---

## Post #2 by @muratmaga (2021-10-13 16:23 UTC)

<p>İf your format is tiff, it doesn’t necessarily report the correct voxel spacing. İf you know the correct voxel value, you can enter them in the volumes module.</p>

---

## Post #3 by @Jeroen_n (2021-10-20 08:03 UTC)

<p>I know the pixel size, 226nm/pixel (which should be the voxel value). I need to enter that in the volumes module.<br>
However, i do not know where</p>

---

## Post #4 by @muratmaga (2021-10-20 15:13 UTC)

<p>How do you load your data? If you used SlicerMorph’s ImageStacks, the very first thing you enter is the image spacing prior to importing the image stack.</p>
<p>If you already loaded the volume, you can change the spacing in the volumes module. Or right click on its name in the Data module and choose “Edit Properties”.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80807945dcd5010fcc96f379efbee0483453771c.png" alt="image" data-base62-sha1="ikMmVT2TwlaQc7gpvwFCOwuOA7a" width="328" height="467"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/799933fba013ecbfd6243c05898248282e44c121.png" alt="image" data-base62-sha1="hlI0Ciq0u7b2R7QLWBnxGUYQGOZ" width="673" height="375"></p>

---
