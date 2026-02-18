# Force2D parameter when input is a 3D VOI

**Topic ID**: 11467
**Date**: 2020-05-08
**URL**: https://discourse.slicer.org/t/force2d-parameter-when-input-is-a-3d-voi/11467

---

## Post #1 by @radio5 (2020-05-08 17:01 UTC)

<p>Hi! I am using pyRadiomics v3.0. I have a VOI of an organ, which was created by consecutively delineating 2D ROIs on the axial plane, i.e., in each slice. I want to characterise the whole volume using radiomic features.<br>
If I use this VOI and the respective label map volume as inputs, what are the differences of the features when using:<br>
i) Force2D = True (on axial plane)<br>
ii) Force 2D = False ?</p>
<p>Ideally, my idea would be to analyse the whole volume. However, out-of-plane resolution is very low compared to in-plane resolution (MR image). I am not very interested in the information “out-of-plane”, more so on the junction of the information portrayed in all axial slices.</p>
<p>Thank you!</p>

---

## Post #2 by @JoostJM (2020-05-14 05:15 UTC)

<p>In both cases, the whole volume is used. With force2D set to true offsets that move between slices are skipped (only affects texture features). In your case, I’d go for force2D set to True</p>

---

## Post #3 by @radio5 (2020-05-14 14:34 UTC)

<p>Thank you for your help <a class="mention" href="/u/joostjm">@JoostJM</a>!</p>

---
