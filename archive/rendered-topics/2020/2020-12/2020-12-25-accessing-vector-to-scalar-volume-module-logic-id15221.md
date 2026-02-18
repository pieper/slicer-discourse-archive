# Accessing Vector to Scalar Volume module logic

**Topic ID**: 15221
**Date**: 2020-12-25
**URL**: https://discourse.slicer.org/t/accessing-vector-to-scalar-volume-module-logic/15221

---

## Post #1 by @giovform (2020-12-25 04:03 UTC)

<p>I wasn’t able to access this module logic. If I do:</p>
<pre><code>slicer.modules.vectortoscalarvolume.logic()
</code></pre>
<p>I get:</p>
<pre><code>(SlicerBaseLogicPython.vtkSlicerScriptedLoadableModuleLogic)00000287A73FC0A8
</code></pre>
<p>Any thoghts on how to access the VectorToScalarVolumeLogic class functions?</p>
<p>I want to particularly use this function:</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/08789e8f2224f89206b2d6a49d1d452d4e677994/Modules/Scripted/VectorToScalarVolume/VectorToScalarVolume.py#L444-L452" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/08789e8f2224f89206b2d6a49d1d452d4e677994/Modules/Scripted/VectorToScalarVolume/VectorToScalarVolume.py#L444-L452" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/08789e8f2224f89206b2d6a49d1d452d4e677994/Modules/Scripted/VectorToScalarVolume/VectorToScalarVolume.py#L444-L452</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="444" style="counter-reset: li-counter 443 ;">
<li>def runWithVariables(self, inputVolumeNode, outputVolumeNode, conversionMethod, componentToExtract):</li><li>  """ Convenience method to run with variables, it creates a new parameterNode with these values. """</li><li></li><li>  parameterNode = self.getParameterNode()</li><li>  parameterNode.SetParameter("InputVectorVolume", getNodeID(inputVolumeNode))</li><li>  parameterNode.SetParameter("OutputScalarVolume", getNodeID(outputVolumeNode))</li><li>  parameterNode.SetParameter("ConversionMethod", conversionMethod)</li><li>  parameterNode.SetParameter("ComponentToExtract", str(componentToExtract))</li><li>  return self.run(parameterNode)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #2 by @lassoan (2020-12-26 05:31 UTC)

<p>See how to access module logic of scripted modules in the PerkLab Slicer programming tutorial: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials</a></p>

---

## Post #3 by @giovform (2021-02-12 13:01 UTC)

<p>vectorToScalarVolumeLogic = slicer.modules.vectortoscalarvolume.widgetRepresentation().self().logic</p>

---
