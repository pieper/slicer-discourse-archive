# Applying different Wavelet Filters

**Topic ID**: 25029
**Date**: 2022-08-31
**URL**: https://discourse.slicer.org/t/applying-different-wavelet-filters/25029

---

## Post #1 by @Ella1 (2022-08-31 14:50 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 5.0.3<br>
Expected behavior: Applying different Wavelet (db, coeif, …) and expect to see some differences<br>
Actual behavior: Do not see any differences between values after and before applying different Wavelet filter.<br>
This is my code:<br>
extractor.enableImageTypes(Wavelet={‘db’:[1.0]}, LoG={‘sigma’:[1.0, 3.0, 5.0]})<br>
extractor.enableImageTypes(Wavelet={‘coif’:[1]})<br>
Is this the correct way to apply different Wavelet filters?<br>
I only need to use Daubechies wavelet filter but I am not sure I am applying it correctly.<br>
One more question, which Wavelet filter is the default if I use this command<br>
extractor.enableImageTypes(Wavelet={})<br>
Thanks</p>

---
