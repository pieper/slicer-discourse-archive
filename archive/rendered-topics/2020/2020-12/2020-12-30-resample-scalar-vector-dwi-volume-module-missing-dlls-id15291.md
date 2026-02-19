---
topic_id: 15291
title: "Resample Scalar Vector Dwi Volume Module Missing Dlls"
date: 2020-12-30
url: https://discourse.slicer.org/t/15291
---

# Resample Scalar/Vector/DWI Volume Module missing DLLs

**Topic ID**: 15291
**Date**: 2020-12-30
**URL**: https://discourse.slicer.org/t/resample-scalar-vector-dwi-volume-module-missing-dlls/15291

---

## Post #1 by @YBurakD (2020-12-30 10:48 UTC)

<p>Hi,<br>
I was using Resample Scalar/Vector/DWI Volume module from Slicer’s GUI and had successful results. Now I’m trying to use the CLI module to do batch processing but I get error of this list of dll files missing.</p>
<p>ITKFactoryRegistration.dll<br>
ITKIOImageBase-5.1.dll<br>
ITKIOTransformBase-5.1.dll</p>
<p>May it be because of the flags I use or should I get these dll’s for CLI to work and if latter, how?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @pieper (2020-12-30 15:36 UTC)

<p>Yes, you need to <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Launcher">use the launcher</a> to set the library paths so you can use a CLI in a batch mode.</p>

---
