# Access to Error Metric during VMTK Level Set Evolution in Python

**Topic ID**: 37306
**Date**: 2024-07-10
**URL**: https://discourse.slicer.org/t/access-to-error-metric-during-vmtk-level-set-evolution-in-python/37306

---

## Post #1 by @tuingc159 (2024-07-10 14:47 UTC)

<p>Hi all,</p>
<p>I have implemented the <code>vmtkLevelSetSegmentation</code> module in Python for my segmentation tasks using VMTK. During the evolution of level sets, I am interested in accessing the error metric (such as RMS error) to monitor convergence directly within my Python script.</p>
<p>Currently, the segmentation stops based on <code>self.MaximumRMSError</code>, which sets the maximum allowable RMS error. (or when self.NumberOfIterations is reached)  However, I would like to retrieve this error metric programmatically during the evolution process to monitor convergence more closely.<br>
I understand that <code>self.PrintProgress</code> captures progress as a percentage via a <code>"ProgressEvent"</code>. However, this does not provide insight into the specific error between iterations.</p>
<p>Could someone please provide the method to access the error metric (RMS error or similar) during level set evolution in Python? Alternatively, a feature enhancement for this capability would greatly assist in monitoring convergence and optimizing parameters.</p>
<p>So for example:<br>
levelSets = vmtk.vmtkLevelSetSegmentation()<br>
levelSets.Execute()<br>
currentRmsError = levelSets.GetCurrentRMSError()</p>
<p>Thank you.</p>

---
