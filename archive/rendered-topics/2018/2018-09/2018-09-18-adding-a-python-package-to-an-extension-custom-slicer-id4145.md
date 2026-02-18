# Adding a python package to an extension/custom Slicer

**Topic ID**: 4145
**Date**: 2018-09-18
**URL**: https://discourse.slicer.org/t/adding-a-python-package-to-an-extension-custom-slicer/4145

---

## Post #1 by @Sam_Horvath (2018-09-18 17:13 UTC)

<p>I need to add a python package (girder_client) to a custom Slicer version I am working on.  With the current difficulties in using pip in Slicer, I wanted to have it added during the build.   Does anyone have an example/tips for doing this?</p>
<p>Thanks</p>

---

## Post #2 by @jcfr (2018-09-18 17:33 UTC)

<p>Hi,</p>
<p>Step 1: try to pip install girder client using python 2.7 in slicer in a build tree. I am assuming this will go smoothly.</p>
<p>Step 2: look at <a href="https://github.com/Radiomics/SlicerRadiomics/blob/master/SuperBuild/External_python-pyradiomics.cmake">https://github.com/Radiomics/SlicerRadiomics/blob/master/SuperBuild/External_python-pyradiomics.cmake</a> and try to have an extension packing the client along with is dependencies.</p>
<p>Step 3: add that external project to the custom app and update the slicer dependencies like we did for scipy in Slicer Salt.</p>
<p>Hth</p>
<p>Jc</p>

---
