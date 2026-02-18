# How to apply RescaleIntensityImageFilter automatically by a python script

**Topic ID**: 39575
**Date**: 2024-10-07
**URL**: https://discourse.slicer.org/t/how-to-apply-rescaleintensityimagefilter-automatically-by-a-python-script/39575

---

## Post #1 by @oscampo (2024-10-07 22:06 UTC)

<p>Hi.<br>
I’m developing a very simple script to load MR and automatically rescale Intensity range for furter analisys. I need access to the filter module and I’m using:<br>
slicer.modules.simplefilters</p>
<p>but how I can access to RescaleIntensityImageFilter() ?</p>

---

## Post #2 by @lassoan (2024-10-07 22:11 UTC)

<p>See a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#running-an-itk-filter-in-python-using-simpleitk">complete example in the script repository</a>.</p>

---
