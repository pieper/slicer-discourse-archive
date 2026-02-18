# How top crop the volume using python?

**Topic ID**: 13791
**Date**: 2020-10-01
**URL**: https://discourse.slicer.org/t/how-top-crop-the-volume-using-python/13791

---

## Post #1 by @Chintha_Siva_Prasad (2020-10-01 09:41 UTC)

<p>I had selected the ROI of a volume.And want to crop it in python.<br>
How can I do this?</p>

---

## Post #2 by @chir.set (2020-10-01 10:13 UTC)

<p>Assuming roi  and inputVolume are defined :</p>
<pre><code class="lang-python">cropLogic = slicer.modules.cropvolume.logic()
cvpn = slicer.vtkMRMLCropVolumeParametersNode()

cvpn.SetROINodeID(roi.GetID())
cvpn.SetInputVolumeNodeID(inputVolume.GetID())
cropLogic.Apply(cvpn)
</code></pre>

---
