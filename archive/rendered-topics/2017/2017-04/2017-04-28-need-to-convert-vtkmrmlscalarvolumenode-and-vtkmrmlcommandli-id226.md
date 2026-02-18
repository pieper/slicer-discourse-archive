# Need to convert vtkMRMLScalarVolumeNode and vtkMRMLCommandLineVolumeNode to Numpy Array

**Topic ID**: 226
**Date**: 2017-04-28
**URL**: https://discourse.slicer.org/t/need-to-convert-vtkmrmlscalarvolumenode-and-vtkmrmlcommandlinevolumenode-to-numpy-array/226

---

## Post #1 by @siddiqueodu (2017-04-28 21:01 UTC)

<p>I am using slicer module in my own module to get bias corrected volume. The following function is working correctly.</p>
<pre><code class="lang-auto">def biascorrection(volumeNode1):
  parameters = {}
  parameters["inputImageName"] = volumeNode1.GetID()
  outModel = slicer.vtkMRMLScalarVolumeNode()
  slicer.mrmlScene.AddNode(outModel)
  parameters["outputImageName"] = outModel.GetID()
  biascorrect = slicer.modules.n4itkbiasfieldcorrection
  return (slicer.cli.run(biascorrect, None, parameters))

Vol1_biasCorrect = biascorrection(nodet1)
</code></pre>
<p>Output node is (vtkCommonCorePython.vtkMRMLCommandLineModuleNode)0x7fc11452a808. To get numpy array of this vtk node, I have been used the following code:</p>
<pre><code class="lang-auto">Vol1_biasCorrectNode = slicer.util.getNode('Volume')
Vol1_biasCorrect_array = slicer.util.array(Vol1_biasCorrectNode.GetID())
</code></pre>
<p>The following error appears:</p>
<pre><code class="lang-auto">File "/home/siddique/Slicer-4.6.2-linux-amd64/bin/Python/slicer/util.py", line 583, in array
    shape = list(n.GetImageData().GetDimensions())
AttributeError: 'NoneType' object has no attribute 'GetDimensions'
</code></pre>
<p>As output volume is created as <code>vtkMRMLScalarVolumeNode()</code>,  I think this volume should be converted to numpy array. Please help me to get the numpy array of bias corrected volume.</p>

---

## Post #2 by @lassoan (2017-04-28 21:30 UTC)

<p>Specify wait_for_completion=True to block execution until the CLI execution is complete. See details here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python</a></p>

---
