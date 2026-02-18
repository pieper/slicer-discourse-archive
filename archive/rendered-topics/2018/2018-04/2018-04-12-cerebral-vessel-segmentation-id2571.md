# Cerebral vessel segmentation

**Topic ID**: 2571
**Date**: 2018-04-12
**URL**: https://discourse.slicer.org/t/cerebral-vessel-segmentation/2571

---

## Post #1 by @Vinny (2018-04-12 16:13 UTC)

<p>Hi,</p>
<p>I was wondering if there was a method or a module in 3d Slicer to segment out cerebral vessels (cortical and/or subcortical) from a gado enhanced MR scan and to build a 3d model out of it.  Is the VMTKVesselEnhancement module the appropriate one to use?</p>
<p>Thanks for your help.</p>

---

## Post #2 by @pieper (2018-04-12 17:52 UTC)

<p>Sure, if the contrast is good then pure thresholding might even work, but enhancing the vessels first could help.</p>
<p>Have a look at the segmentation materials:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Training#Segmentation" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Training#Segmentation</a></p>
<p><a href="http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html" class="onebox" target="_blank">http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html</a></p>

---

## Post #3 by @Baez (2018-04-12 18:17 UTC)

<p>Best regards<br>
Exactly, the contrast we use in the MDTC is ultravist, or any other iodine-based as Ray Diagnostic apparatuses, with a dose of 1 ml/kg.</p>
<details>
<summary>
Spanish original</summary>
<p>Saludos<br>
Exacto, el contraste que empleamos en el MDTC es el ultravist, o cualquier otro con base a yodo como iopamiro, con una dosis de 1 ml/kg.</p>
</details>

---

## Post #4 by @Vinny (2018-04-12 18:27 UTC)

<p>Great thanks!  I’ve used the Seg Editor before for segmenting out electrodes based on threshold effect.  I’ll see if this works for the enhanced vessels in the scans I have.</p>

---
