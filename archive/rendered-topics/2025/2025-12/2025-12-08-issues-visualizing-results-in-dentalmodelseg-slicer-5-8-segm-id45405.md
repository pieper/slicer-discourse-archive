# Issues visualizing results in DentalModelSeg (Slicer 5.8) – segmentation runs but no output appears

**Topic ID**: 45405
**Date**: 2025-12-08
**URL**: https://discourse.slicer.org/t/issues-visualizing-results-in-dentalmodelseg-slicer-5-8-segmentation-runs-but-no-output-appears/45405

---

## Post #1 by @Brendy_Villanueva (2025-12-08 17:25 UTC)

<p>Hello everyone,</p>
<p>I am trying to segment teeth from STL dental models using <strong>DentalModelSeg</strong>, but I am running into visualization issues, and I would really appreciate some guidance.</p>
<p>I used:</p>
<ul>
<li>
<p>3D Slicer version 5.8</p>
</li>
<li>
<p>DentalModelSeg installed via the Extension Manager</p>
</li>
<li>
<p>Running on Linux</p>
</li>
<li>
<p>I also tried installing and running it using Anaconda, but obtained the same behavior</p>
</li>
</ul>
<p>The issue:</p>
<ul>
<li>
<p>The segmentation process appears to have completed successfully (with error messages)</p>
</li>
<li>
<p>The log indicates that the segmentation was performed</p>
</li>
</ul>
<p>However:</p>
<ul>
<li>No segmented models appear in the Data module</li>
<li>Nothing is visible in the 3D view</li>
<li>No output seems to be generated or displayed</li>
</ul>
<p>What I am working with:</p>
<ul>
<li>
<p>STL dental models (upper/lower arches)</p>
</li>
<li>
<p>Goal: individual tooth segmentation for quantitative analysis</p>
</li>
</ul>
<p>Questions:</p>
<ol>
<li>
<p>Which Slicer version is known to work reliably with DentalModelSeg?</p>
</li>
<li>
<p>Is Slicer 5.8 fully supported, or should I downgrade to an earlier version?</p>
</li>
<li>
<p>Are there any known visualization issues, or are any steps required to load or display the output manually?</p>
</li>
<li>
<p>Are there specific module settings or dependencies that are commonly missed?</p>
</li>
</ol>
<p>If logs or screenshots would be helpful, I’m happy to share them.</p>
<p>Thank you very much for your time and support.</p>
<p>Best regards,</p>
<p>Brendy</p>

---

## Post #2 by @amyers (2025-12-11 20:38 UTC)

<p>Are you using the STL models as input? It only segments CBCT or CT scans.</p>

---
