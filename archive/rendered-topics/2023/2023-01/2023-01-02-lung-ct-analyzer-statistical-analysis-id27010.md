# Lung CT analyzer - statistical analysis

**Topic ID**: 27010
**Date**: 2023-01-02
**URL**: https://discourse.slicer.org/t/lung-ct-analyzer-statistical-analysis/27010

---

## Post #1 by @handicapped71498 (2023-01-02 17:16 UTC)

<p>Thank you for always your help.<br>
I can’t click the button on the <strong>computer results</strong> in the lung CT analyzer. Is there any installation required?<br>
I was successful in setting the threshold. However, I am unable to perform statistical analysis.<br>
Could you please give me a good resolution?</p>
<p>Slicer version: 3Dslicer 5.2.1</p>

---

## Post #2 by @rbumm (2023-01-02 17:27 UTC)

<p>Here is the normal workflow:</p>
<ul>
<li>
<p>Start 3D Slicer</p>
</li>
<li>
<p>Load your data set (you can try the CTChest sample dataset)</p>
</li>
<li>
<p>Select the Lung CT Segmenter extension</p>
</li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/619a74e2d36b12be82a9fd511e88205be00b5c89.png" alt="image" data-base62-sha1="dVreEvapVt7orxG0XM2ruyFmGWR" width="525" height="178"></p>
<ul>
<li>
<p>Create a lung segmentation</p>
</li>
<li>
<p>Select the Lung CT Analyzer extension</p>
</li>
<li>
<p>Select the segmentation you made</p>
</li>
<li>
<p>Press “Compute results”</p>
</li>
</ul>

---
