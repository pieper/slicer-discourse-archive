# Slicer Radiomics

**Topic ID**: 12791
**Date**: 2020-07-30
**URL**: https://discourse.slicer.org/t/slicer-radiomics/12791

---

## Post #1 by @mcastro (2020-07-30 15:22 UTC)

<p>Operating system: Windiows<br>
Slicer version: 4.10.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I am using Slicer Radiomics with a parameter file. The possible settings depends on the PyRadiomics version used within Slicer Radiomcis. How can I know the PyRadiomics version that is being used?</p>

---

## Post #2 by @fedorov (2020-07-30 20:45 UTC)

<p>SlicerRadiomics is using the latest version of pyradiomics.</p>
<p>For the reference, this is captured in <a href="https://github.com/Radiomics/SlicerRadiomics/blob/master/SuperBuild/External_python-pyradiomics.cmake#L26-L36">https://github.com/Radiomics/SlicerRadiomics/blob/master/SuperBuild/External_python-pyradiomics.cmake#L26-L36</a>.</p>

---

## Post #3 by @JoostJM (2020-07-31 04:43 UTC)

<p>Additionally, you can check the version in the output (part of the diagnostic features) and in the python interactor</p>
<pre><code class="lang-auto">import radiomics
print(radiomics.__version__)
</code></pre>

---
