# AbcissaMetric does not write

**Topic ID**: 19012
**Date**: 2021-08-01
**URL**: https://discourse.slicer.org/t/abcissametric-does-not-write/19012

---

## Post #1 by @cborras (2021-08-01 11:40 UTC)

<p>Operating system: Windows 10</p>
<p>Hi everybody! I am working on aortas and I am using this command for the writing of the angular and abcissa coordinates:</p>
<pre><code class="lang-auto">#vmtkbranchmetrics -ifile aorta_clipped.vtp -centerlinesfile Ht_Lum_StAc_cl.vtp -abscissasarray Abscissas -normalsarray ParallelTransportNormals -groupidsarray GroupIds -centerlineidsarray CenterlineIds -tractidsarray TractIds -blankingarray Blanking -radiusarray MaximumInscribedSphereRadius -ofile aorta_clipped_metrics.vtp
</code></pre>
<p>However, the AbcissaMetric is writing the same value for the whole geometry while the angularMetric works fine as expected.</p>
<p>I do not know what could be the problem since I am just following the vmtk page (<a href="http://www.vmtk.org/tutorials/MappingAndPatching.html" class="inline-onebox" rel="noopener nofollow ugc">Mapping and Patching | vmtk - the Vascular Modelling Toolkit</a>).</p>
<p>I would really appreciate it if anyone has encountered or know how to solve this!</p>
<p>Thanks!<br>
Concepción</p>

---
