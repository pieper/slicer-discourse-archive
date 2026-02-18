# The difference in the results of running Isodose from Python Interactor between the two versions of 3DSlicer and the result from the Isodose module

**Topic ID**: 41842
**Date**: 2025-02-23
**URL**: https://discourse.slicer.org/t/the-difference-in-the-results-of-running-isodose-from-python-interactor-between-the-two-versions-of-3dslicer-and-the-result-from-the-isodose-module/41842

---

## Post #1 by @shahrokh (2025-02-23 07:28 UTC)

<p>Hello Dear Developers and Users</p>
<p><a href="https://discourse.slicer.org/t/issue-with-generating-specific-isodose-surface-using-the-isodose-module-in-python-interactor/41826">In my attempt to generate the Isodose surface of 47.00 Gy</a>, I noticed that the output of the isodose surfaces differed between two versions of 3DSlicer, versions 5.6.2 and 5.0.2. I executed the following commands in the Python Interactor of both versions of 3DSlicer.</p>
<pre><code class="lang-auto"># Get the dose volume node by class and name
doseVolumeNode = slicer.util.getFirstNodeByClassByName('vtkMRMLScalarVolumeNode', '2: RTDOSE: DOSIsoft:RTDOSE:Phase #1 Dosi Dosi 1: Beam setup 1 (GY) [11]: Beam setup 1')

# Create a new Isodose node instance for displaying isodose surfaces
object_vtkMRMLIsodoseNode = slicer.vtkMRMLIsodoseNode().CreateNodeInstance()

# Set the scene for the isodose node to match the dose volume node's scene
object_vtkMRMLIsodoseNode.SetScene(doseVolumeNode.GetScene())

# Set the dose units to Gray (Gy)
object_vtkMRMLIsodoseNode.SetDoseUnits(slicer.vtkMRMLIsodoseNode.Gy)

# Set the reference dose value (in Gy) for isodose levels
object_vtkMRMLIsodoseNode.SetReferenceDoseValue(47.00)

# Observe the dose volume node to track its changes
object_vtkMRMLIsodoseNode.SetAndObserveDoseVolumeNode(doseVolumeNode)

# Setup the color table for the isodose node based on the dose volume
slicer.modules.isodose.logic().SetupColorTableNodeForDoseVolumeNode(doseVolumeNode)
#slicer.util.getModuleLogic('Isodose').SetupColorTableNodeForDoseVolumeNode(doseVolumeNode)

# Create isodose surfaces based on the configured isodose node
slicer.modules.isodose.logic().CreateIsodoseSurfaces(object_vtkMRMLIsodoseNode)
</code></pre>
<p>Result of execution in 3DSlicer version 5.0.2:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e538029b2313c4b921d51041b4c2cc1c13fda4a.png" data-download-href="/uploads/short-url/22JAcpBoKzxGV0QZX0cK9NDHX4K.png?dl=1" title="5.0.2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e538029b2313c4b921d51041b4c2cc1c13fda4a_2_690x391.png" alt="5.0.2" data-base62-sha1="22JAcpBoKzxGV0QZX0cK9NDHX4K" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e538029b2313c4b921d51041b4c2cc1c13fda4a_2_690x391.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e538029b2313c4b921d51041b4c2cc1c13fda4a_2_1035x586.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e538029b2313c4b921d51041b4c2cc1c13fda4a_2_1380x782.png 2x" data-dominant-color="DBDBE4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">5.0.2</span><span class="informations">1851×1051 289 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Result of execution in 3DSlicer version 5.6.2:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31292a2e97da65da23cad6537fdcc38f0f18892d.png" data-download-href="/uploads/short-url/70TAEsVJ13fqWMHihl820GsHwex.png?dl=1" title="5.6.2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31292a2e97da65da23cad6537fdcc38f0f18892d_2_690x391.png" alt="5.6.2" data-base62-sha1="70TAEsVJ13fqWMHihl820GsHwex" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31292a2e97da65da23cad6537fdcc38f0f18892d_2_690x391.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31292a2e97da65da23cad6537fdcc38f0f18892d_2_1035x586.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31292a2e97da65da23cad6537fdcc38f0f18892d_2_1380x782.png 2x" data-dominant-color="DEDFE8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">5.6.2</span><span class="informations">1851×1051 252 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As you can see, I believe that these commands in 3DSlicer version 5.6.2 result in just one isodose surface, although I’m not sure about this. However, the outcome of these commands in 3DSlicer version 5.0.2 is practically ineffective, and the generated isodose surfaces are related to the default settings of the Isodose module’s graphical interface.</p>
<p>Then, I generated the Isodose surface at 47.00 Gy through the Isodose module in 3DSlicer version 5.6.2. The result was different from the outcome of the commands mentioned earlier in the same version of 3DSlicer as seen below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d6484df1baa44804fb49845716cf9baf4fd30dc.png" data-download-href="/uploads/short-url/dkbLtEyKVT2mzNEQPxjv1JkHlz6.png?dl=1" title="compare" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d6484df1baa44804fb49845716cf9baf4fd30dc_2_690x391.png" alt="compare" data-base62-sha1="dkbLtEyKVT2mzNEQPxjv1JkHlz6" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d6484df1baa44804fb49845716cf9baf4fd30dc_2_690x391.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d6484df1baa44804fb49845716cf9baf4fd30dc_2_1035x586.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d6484df1baa44804fb49845716cf9baf4fd30dc_2_1380x782.png 2x" data-dominant-color="BDC0D9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">compare</span><span class="informations">1851×1051 200 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The node named Isodose_Surface_Generated_by_Python is the result of running the commands in Python Interactor, and the node named Isodose_Surface_Generated_by_Isodose_Module is the result of running the Isodose module in 3DSlicer version 5.6.2.</p>
<p>The data used to run these commands is available through <a href="https://drive.google.com/file/d/1PPHmktnGrZqYGR6nSXDwrglHPgR9J9M7/view?usp=sharing" rel="noopener nofollow ugc">this link</a>.<br>
Please guide me.<br>
Best regards.<br>
Shahrokh</p>

---

## Post #2 by @shahrokh (2025-02-26 04:46 UTC)

<p>Dear Developers and Users,</p>
<p>I apologize for taking your time again, but I have not received a response regarding my previous problem. Could you kindly help and guide me with the issue I encountered regarding the isodose surfaces in 3DSlicer? Your guidance would be greatly appreciated.</p>
<p>Best regards,<br>
Shahrokh</p>

---

## Post #3 by @shahrokh (2025-03-03 10:44 UTC)

<p>Hello Dear Developers and Users</p>
<p>Unfortunately, I haven’t been able to solve this problem yet. I would be very happy if you could guide me.<br>
Best regards.<br>
Shahrokh</p>

---
