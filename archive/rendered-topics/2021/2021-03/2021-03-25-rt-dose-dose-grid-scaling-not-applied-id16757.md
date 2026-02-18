# RT Dose dose grid scaling not applied

**Topic ID**: 16757
**Date**: 2021-03-25
**URL**: https://discourse.slicer.org/t/rt-dose-dose-grid-scaling-not-applied/16757

---

## Post #1 by @Renata_Chmielewski (2021-03-25 02:23 UTC)

<p>Operating system: Windows 10<br>
Slicer version:4.11.202<br>
Expected behavior:<br>
Actual behavior:<br>
Hi,</p>
<p>I am trying to subtract one dose from another. I am importing RT Dose files from Pinnacle. When I click on “Convert to RT Dose volume” the dose unit value is 0.00556. After I convert to RT Dose volume and run a DVH it is clear that the scaling was not applied the max dose is off by a factor 0.00556. How do I get Slicer to apply the correct dose unit value? Thank you!</p>
<p>Renata</p>

---

## Post #2 by @cpinter (2021-03-25 08:51 UTC)

<p>The dose grid scaling is applied when importing from DICOM, so if you add it later then it will have no effect on the image contents, only when you export then re-import. Do you know why your Pinnacle dataset does not contain the proper dose scaling value?</p>
<p>To multiply the voxel values you can use the Simple Filters / ShiftScaleImageFilter.</p>

---

## Post #3 by @Renata_Chmielewski (2021-04-08 15:47 UTC)

<p>The Simple Filters worked however the dose was a bit off since I have to round up or down the scaling factor. Sorry I don’t know that much about Pinnacle nor am I finding information about the dose scaling factor in the Pinnacle documentation. How do you change the dose scaling value in Pinnacle? Thanks!</p>

---

## Post #4 by @cpinter (2021-04-08 16:30 UTC)

<p>I am not familiar with Pinnacle itself. This is the Slicer forum so I’d suggest asking Pinnacle-related questions from that community or the manufacturer.</p>

---
