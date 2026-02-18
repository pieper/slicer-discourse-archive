# Lumbar Spine PCA

**Topic ID**: 35170
**Date**: 2024-03-29
**URL**: https://discourse.slicer.org/t/lumbar-spine-pca/35170

---

## Post #1 by @LeidyMoraV (2024-03-29 17:47 UTC)

<p>Hello! I’m new to Slicer and I need to use Principal Component Analysis (PCA) to get the mean shape of a dataset of L4 vertebrae, I’ve tried using SlicerSALT, and the topology of the files seem to be consistent for Circle/Torus/Mobius Strip. When I run the ShapeAnalysisModule the next error appears:</p>
<pre><code class="lang-auto">GenParaMesh standard output:
itk::BinaryMask3DEqualAreaParametricMeshSourceException (00000034D94FDC90)
Location: "Unknown" 
File: D:\D\S\SA-40-build\SPHARM-PDM\Libraries\Shape\Algorithms\BinaryMask3DEqualAreaParametricMeshSource.txx
Line: 183
Description: Warning: Euler equation not satisfied. Euler Number: 25860 - 25860 = 0
</code></pre>
<p>Is it related to the topology? Does slicer have other tools that can be used to do the PCA?</p>

---

## Post #2 by @muratmaga (2024-03-29 17:58 UTC)

<p>If you can’t get the SALT to work you can try landmark based approach with SlicerMorph:</p>
<ol>
<li>Use pseudoLMGenerator to create a large number of surfaceLMs in one of your L4 models. Pay attention to uniformness of the points etc. You probably will need to provide a good model, and then clean some of the redundant points. This will be your template.</li>
<li>use ALPACA to transfer the points on your template (source) model to your individual L4s (you can run in the batch mode).</li>
<li>Use the GPA (Generalized Procrustes Analysis) module to do a superimposition of these landmarks, a PCA decomposition and a mean shape. If scale of the data is important for the mean shape (otherwise it will be in unit size), make sure you check the “enable boaz coordinates” option.</li>
</ol>
<p>You can tutorials of for all three modules at <a href="https://github.com/SlicerMorph/Tutorials" class="inline-onebox">GitHub - SlicerMorph/Tutorials: SlicerMorph module tutorials</a>.</p>

---

## Post #3 by @LeidyMoraV (2024-03-29 19:49 UTC)

<p>Thank you! If I use the method that you described I need to aligned and center the L4s before?</p>

---

## Post #4 by @muratmaga (2024-03-29 20:04 UTC)

<p>No. Thats taken care of during alpaca</p>

---
