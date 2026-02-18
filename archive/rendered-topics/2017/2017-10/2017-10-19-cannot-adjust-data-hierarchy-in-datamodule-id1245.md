# Cannot adjust data hierarchy in DataModule

**Topic ID**: 1245
**Date**: 2017-10-19
**URL**: https://discourse.slicer.org/t/cannot-adjust-data-hierarchy-in-datamodule/1245

---

## Post #1 by @shenziheng (2017-10-19 07:57 UTC)

<p>Hi,<br>
I want to try image-guided surgery using slicer developed module.</p>
<p>The main Notes (displayed in data module) include :</p>
<ol>
<li>
<p>Ultrasound ( <code>vtkMRMLVolumeNode</code> ,  real time transmission by openigtlink module through a  image grabber connected with ultrasound machine)</p>
</li>
<li>
<p><code>ImageToProbe</code> (constant linear transform), <code>ProbeToTracker</code> (real time linear transform acquired by NDI and transmitted by openigt module )  Their data type are both <code>vtkMRMLLinearTransformNode</code>.<br>
And with the help of openigtlink module, the hierarchy in Data module likes:</p>
</li>
</ol>
<pre><code class="lang-auto">|--Ultrasound
|--ImageToProbe
|--ProbeToTracker

In oder to  realize the function of image-guieded surgery, I need to transform Images (Ultrasound) from image coordinate system to tracker coordinate system. so I choose to adjust  hierarchy ( draging nodes):
|--ProbeToTracker
|------ImageToProbe (success)
|----------Ultrasound (fail)
</code></pre>
<p>I have tried many times, but failed to drag "ultrasound "node to the lower level of  <code>ImageToProbe</code> node.</p>
<p>More details about my system configuration are:<br>
Windows7   Slicer 4.5  Visual Studio2013</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0eb30c0b61931608c5db7d787d1e62d64197628f.jpeg" alt="image" data-base62-sha1="262i33MgCJnUQuc25Q5aPQpfagL" width="335" height="205"></p>

---

## Post #2 by @cpinter (2017-10-19 12:42 UTC)

<p>Hi! This was a known issue but it has been fixed since the release of 4.5 that was two years ago. 4.8 was released yesterday, please try with that. Thanks!</p>

---
