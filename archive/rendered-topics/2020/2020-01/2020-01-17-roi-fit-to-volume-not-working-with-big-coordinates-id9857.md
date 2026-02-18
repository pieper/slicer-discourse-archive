# ROI fit to volume not working with big coordinates

**Topic ID**: 9857
**Date**: 2020-01-17
**URL**: https://discourse.slicer.org/t/roi-fit-to-volume-not-working-with-big-coordinates/9857

---

## Post #1 by @fbordignon (2020-01-17 19:40 UTC)

<p>If I set the S origin coordinate of my volume to -5 000 000, when I click fit to volume, the ROI does not fit. It stays at -1 000 000<br>
I’ve tried to change the settings of length at the unit options window, but I cannot de/increase the min/max below/above -10 000 and 10 000</p>
<p>Funny thing is that if I save a volume as nrrd and load it with the origin coordinates set, when I show it at the volume viewer, a ROI is created with the correct coordinates surrounding my volume. As soon as I click fit to volume, the ROI is screwed.</p>

---

## Post #2 by @lassoan (2020-01-18 14:32 UTC)

<p>Thanks for reporting this, I’ve fixed the problem in revision 28736. It’ll be available in the next nightly build.</p>

---

## Post #3 by @fbordignon (2020-01-20 14:20 UTC)

<p>Thanks Andras. I will test and report back.</p>

---

## Post #4 by @fbordignon (2020-01-21 20:41 UTC)

<p>It is working as expected. Great job, thank you Andras.</p>

---
