# Convert relative 3ddose to absolute dose in 3DSlicer

**Topic ID**: 42852
**Date**: 2025-05-09
**URL**: https://discourse.slicer.org/t/convert-relative-3ddose-to-absolute-dose-in-3dslicer/42852

---

## Post #1 by @TaHamI (2025-05-09 13:37 UTC)

<p>Hello,<br>
I know, DOSXYZnrc like other monte-carlo simulations reports relative (normalized) dose (averaging on the number of histories, the number of histories just relates to dose uncertainty, no change the dose value).<br>
I run DOSXYZnrc, then import the .3ddose output file into 3DSlicer and try to convert it to RT Dose. When I want to convert 3ddose to RT Dose, it takes “unit name” and “dose unit value(scaling)”. I guess, if I change the value scaling, it will change the absolute dose. But I see, when I change the value scaling, no change in absolute dose, and surprisingly, when I change the number of histories (in DOSXYZnrc simulation), I see the absolute dose changes!<br>
Where am I doing wrong?</p>
<p>Operating system: windows 10 64bit<br>
Slicer version: 5.8.1</p>
<p>Any help would be appreciated.</p>

---

## Post #2 by @cpinter (2025-05-12 13:56 UTC)

<p>The dose unit scaling that you enter when converting a regular volume to RT dose volume does not get hard-applied on the image. Instead, it is considered when calculating the DVH, or when using the Dose Accumulation module. If you want to apply it, I suggest you either do a dose accumulation with this single volume, or you apply it manually. For that I’d use the Simple Filters module / ShiftScaleImageFilter.</p>
<p>If I didn’t answer your question then probably I misunderstood and need some more information.</p>

---
