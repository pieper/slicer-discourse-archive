# How can I set absolute bound

**Topic ID**: 11263
**Date**: 2020-04-23
**URL**: https://discourse.slicer.org/t/how-can-i-set-absolute-bound/11263

---

## Post #1 by @codecrazer (2020-04-23 08:11 UTC)

<p>Dear all, due to some of CT will have maximum Housefield units value more than 3000. Is it possible for me to absolute bound HU before binwith resampling in pyradiomics batch parameter file? Thanks for your help!</p>

---

## Post #2 by @JoostJM (2020-04-27 15:46 UTC)

<p>PyRadiomics supports <code>resegmentRange</code> in the settings section, which allows you to exclude voxels from the intensity mask (used for all classes except shape, shape is calculated on the non-resegmented mask).</p>
<p>For more info, see <a href="https://pyradiomics.readthedocs.io/en/latest/customization.html#feature-extractor-level">the documentation</a>, subsection Resegmentation</p>

---

## Post #3 by @codecrazer (2020-04-28 12:23 UTC)

<p>Why remove the voxel has bigger HU? It seems to me that set the bigger HU to a fixed value to be more reasonable!</p>

---

## Post #4 by @JoostJM (2020-05-06 19:42 UTC)

<p>First off, that would introduce artificial homogeneity, as all values above the threshold will be set to a single value, making that value seem more common. For more information, check out the IBSI document, it contains a more detailed explanation.</p>

---

## Post #5 by @mcastro (2020-12-08 23:14 UTC)

<p>I have a related question. When declaring the resegmentation variables in the parameter file, it finds an error that I understand is when reading the information from the file. Is it possible that the syntaxis is not correct? For example:</p>
<h1>--------------------------------------------------------------------------------------------------------</h1>
<h1>RESEGMENTATION</h1>
<h1>--------------------------------------------------------------------------------------------------------</h1>
<p>resegmentRange: [-1000, 0]<br>
resegmentMode:<br>
- ‘absolute’<br>
resegmentShape: True</p>

---

## Post #6 by @mcastro (2020-12-09 04:01 UTC)

<p>Never mind, just missing spaces in each row:</p>
<pre><code>resegmentRange: [-1000,0]
resegmentMode: 'absolute'
resegmentShape: True</code></pre>

---
