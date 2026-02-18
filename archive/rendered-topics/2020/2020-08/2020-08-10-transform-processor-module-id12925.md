# Transform processor module

**Topic ID**: 12925
**Date**: 2020-08-10
**URL**: https://discourse.slicer.org/t/transform-processor-module/12925

---

## Post #1 by @Selva (2020-08-10 12:52 UTC)

<p>Hi,</p>
<p>I am trying to decompose a linear transformation into rotation and translation components.<br>
What could be the easiest way to do this please.<br>
I have tried the transform processor module, but I am not sure what are the two input transforms to enter. I only have one, that is generated from model registration. (model A to model b registration, generated linear transform 3). What I m interested is the the angular and translational difference between model a and b separated.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-08-10 13:15 UTC)

<p>Transform processor provides translation vector and orientation matrix. If you need translation magnitude in a single mm value or representation of the total rotation in degrees (or rotation along specific axes) then you need to compute it from the transformation matrix using basic linear algebra. Note that rotation error in itself is often clinically not meaningful, as the error it causes depends on how far the coordinate system is from the region of interest.</p>
<p>If you write more about what exactly you want to evaluate, how the coordinate systems are defined, how transforms are computed between them, etc. then we may be able to give more specific advice.</p>

---

## Post #3 by @Selva (2020-08-11 08:46 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>This helps</p>

---

## Post #4 by @reddington.15 (2021-03-22 13:56 UTC)

<p>I know you aren’t a math professor, but how would one calculate the the translation magnitude or total rotation in degrees from the transformation matrix using linear algebra?</p>

---

## Post #5 by @JBeninca (2023-08-29 18:24 UTC)

<p>ok. the module works ok. but when its over, and i clear the scene, when the module is opened againg, by script, the 3dslice fails, and finally close<br>
the version i am using is    4.11.20210226 r29738 / 7a593c8</p>
<p>thanks for any suggestion.</p>
<p>ad:<br>
the code i am using is:</p>
<pre><code class="lang-python">def crea_nodo_Transform_Processor(nombre, transfo_in, transfo_out, param):
    transfo_in = slicer.util.getNode(transfo_in)
    transfo_out = slicer.util.getNode(transfo_out)
        
    transfoProcNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTransformProcessorNode')
    transfoProcNode.SetName(nombre)
    transfoProcNode.SetProcessingMode(transfoProcNode.PROCESSING_MODE_STABILIZE)
    transfoProcNode.SetStabilizationCutOffFrequency(param["filtro_transformada"])
    transfoProcNode.SetAndObserveInputUnstabilizedTransformNode(transfo_in)
    transfoProcNode.SetAndObserveOutputTransformNode(transfo_out)
    transfoProcNode.SetUpdateModeToAuto()
</code></pre>
<p>thanks</p>

---
