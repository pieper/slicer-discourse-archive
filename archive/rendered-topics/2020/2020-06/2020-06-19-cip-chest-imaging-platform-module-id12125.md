---
topic_id: 12125
title: "Cip Chest Imaging Platform Module"
date: 2020-06-19
url: https://discourse.slicer.org/t/12125
---

# CIP (chest imaging platform) module

**Topic ID**: 12125
**Date**: 2020-06-19
**URL**: https://discourse.slicer.org/t/cip-chest-imaging-platform-module/12125

---

## Post #1 by @szhang (2020-06-19 23:16 UTC)

<p>Hello,<br>
I would like to call the module segmentlungairways in a loadable module, but not sure what is the syntax and what parameters are needed. Could you please provide an example?</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2020-06-20 03:46 UTC)

<p>See an example here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/CropVolume/Logic/vtkSlicerCropVolumeLogic.cxx#L493-L595" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/CropVolume/Logic/vtkSlicerCropVolumeLogic.cxx#L493-L595" target="_blank">Slicer/Slicer/blob/master/Modules/Loadable/CropVolume/Logic/vtkSlicerCropVolumeLogic.cxx#L493-L595</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="493" style="counter-reset: li-counter 492 ;">
<li>vtkMRMLCommandLineModuleNode* cmdNode = this-&gt;Internal-&gt;ResampleLogic-&gt;CreateNodeInScene();</li>
<li>if (cmdNode == nullptr)</li>
<li>  {</li>
<li>  vtkErrorMacro("CropVolume: failed to create resample node");</li>
<li>  return -4;</li>
<li>  }</li>
<li>
</li><li>cmdNode-&gt;SetParameterAsString("inputVolume", inputVolume-&gt;GetID());</li>
<li>cmdNode-&gt;SetParameterAsString("outputVolume", outputVolume-&gt;GetID());</li>
<li>
</li><li>std::stringstream sizeStream;</li>
<li>sizeStream &lt;&lt; (outputExtent[1] - outputExtent[0] + 1)  &lt;&lt; ","</li>
<li>  &lt;&lt; (outputExtent[3] - outputExtent[2] + 1) &lt;&lt; ","</li>
<li>  &lt;&lt; (outputExtent[5] - outputExtent[4] + 1);</li>
<li>cmdNode-&gt;SetParameterAsString("outputImageSize", sizeStream.str());</li>
<li>
</li><li>// Center the output image in the ROI. For that, compute the size difference between</li>
<li>// the ROI and the output image.</li>
<li>double sizeDifference_IJK[3] =</li>
<li>  {</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/CropVolume/Logic/vtkSlicerCropVolumeLogic.cxx#L493-L595" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @szhang (2020-06-20 20:13 UTC)

<p>Thank you, Andras.<br>
However, I do not see in this example any place calling slicer.modules.segmentlungairways. Am I missing something?</p>
<p>Thanks again.</p>

---

## Post #4 by @lassoan (2020-06-20 20:48 UTC)

<p>You can run any other CLI modules the same way, you just change the module name and parameters.</p>
<p>To get started, I would recommend to write Python scripted modules, as the Python syntax is much simpler and you don’t need to rebuild anything and restart Slicer if you make changes.</p>

---

## Post #5 by @szhang (2020-06-20 21:22 UTC)

<p>I have to admit I need more help here.<br>
How I used to call airwaysegmentationcli is as below, but a simple substitution of the module name to “segmentlungairway” produces no error and no result, so how to correctly call this module then?</p>
<blockquote>
<p>cliParams = {“inputVolume”: inputVolume.GetID(), “reconstructionKernelType”: convolutionKernel,<br>
“label”: outputVolume.GetID(),“seed”: fiducialsList.GetID(),<br>
“labelValue”: self.labelValue}<br>
slicer.cli.run(slicer.modules.airwaysegmentationcli, None, cliParams, wait_for_completion = True)</p>
</blockquote>

---

## Post #6 by @lassoan (2020-06-20 21:36 UTC)

<p>If any error occurs then you can find it in the application log.</p>
<p>I would also suggest to check out this <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python">documentation section</a>. In particular, run the <em>Get list of parameter names</em> script to verify that the module name and all parameter names are correct.</p>

---

## Post #7 by @rbumm (2021-09-16 19:47 UTC)

<p>I got the CLI call working like this in 4.13:</p>
<pre><code class="lang-auto"># Create labelmap
self.airwayLabelMap = slicer.util.getFirstNodeByClassByName("vtkMRMLLabelMapVolumeNode",
                "AirwayLabelMap")
if not self.airwayLabelMap:
    self.airwayLabelMap = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode",
                    "AirwayLabelMap")
# Set parameters
parameters = {}
# CT
parameters["inputVolume"] = self.inputVolume
# define one fiducial in the trachea
parameters["seed"] = self.tracheaFiducials
# output labelmap
parameters["airwayLabel"] = self.airwayLabelMap

# Kernel type parameter
# STANDARD: Most details, but susceptible for leaks 
# LUNG: Less details, more robust concerning leaks
# B70f: Low detail level, very robust
parameters["reconstructionKernelType"] = "STANDARD"

# Execute
segmentAirways = slicer.modules.segmentlungairways
cliNode = slicer.cli.runSync(segmentAirways, None, parameters)
# Process results
if cliNode.GetStatus() &amp; cliNode.ErrorsMask:
    # error
    errorText = cliNode.GetErrorText()
    slicer.mrmlScene.RemoveNode(cliNode)
    raise ValueError("CLI execution failed: " + errorText)
# success
slicer.mrmlScene.RemoveNode(cliNode)
</code></pre>

---
