# Calibration for optimised lung parenchyma analysis

**Topic ID**: 4777
**Date**: 2018-11-16
**URL**: https://discourse.slicer.org/t/calibration-for-optimised-lung-parenchyma-analysis/4777

---

## Post #1 by @nikkikto (2018-11-16 16:38 UTC)

<p>Hi,</p>
<p>Chest analysis is more clinically accurate if the hounsfield units are calibrated prior to analysis, is this possible or already built in to the CIP (specifically the parenchyma analysis module)?</p>
<p>Eg. air outside patient set to -1000HU and blood in aorta set to 50HU</p>
<p>Thanks!</p>

---

## Post #2 by @raul (2018-11-20 03:47 UTC)

<p>Hi,</p>
<p>That is an excellent suggestion. Unfortunately, we don’t currently have an autocalibration approach within CIP to perform a linear correction of HU values based on reference values. We will incorporate this into our wish list of features.</p>
<p>In the meantime, you could use a combination of the editor and label statistics module to gather mean values in the trachea and aorta to perform a correction.</p>
<p>Best,</p>
<p>Raul</p>

---

## Post #3 by @nikkikto (2019-04-08 10:46 UTC)

<p>Hi,<br>
Thank you for adding this to the wish list. Just an update that may help any developers - when I tried doing the calibration manually it didn’t give a linear difference (this may not be the correct terminology). For example the tracheal air would be 14 HU more than -1000 and the aortic blood would be 63 HU more than 50. Therefore I couldn’t simply adjust by adding/subtracting.<br>
There would also be different differences between various slices from the same patient.<br>
So it may be most accurate and reproducible to segment internal sections of the trachea and aorta for calibration rather than one slice.</p>

---
