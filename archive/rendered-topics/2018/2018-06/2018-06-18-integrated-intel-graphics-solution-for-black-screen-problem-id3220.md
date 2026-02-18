# Integrated Intel Graphics - solution for black screen problem

**Topic ID**: 3220
**Date**: 2018-06-18
**URL**: https://discourse.slicer.org/t/integrated-intel-graphics-solution-for-black-screen-problem/3220

---

## Post #1 by @JamesGalea (2018-06-18 19:09 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.9.0<br>
Expected behavior: GPU volumetric rendering<br>
Actual behavior: Black screen</p>
<p>Version 4.9 brings much improvement and refinement with GPU rendering (Ray Casting) especially a Quality (Normal) option.  With Intel Integrated Graphics esp HD 520, there may be a problem with program running. This is easily sorted by installing the new May 2018 Intel update for integrated graphics. If your laptop or computer needs a specific driver and is unable to install the driver directly from Intel do as follows. Open the *.exe file using 7Zip or equivalent. Go to device manager, choose the video card, choose update driver, have my own driver, then choose the driver from the *.exe folder you have just unzipper. The file should end in *inf. Then restart 3D Slicer and that should be it.</p>

---
