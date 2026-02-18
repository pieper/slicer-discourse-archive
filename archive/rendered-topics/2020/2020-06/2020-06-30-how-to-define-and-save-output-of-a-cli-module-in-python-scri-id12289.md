# How to define and save output of a cli module in Python script?

**Topic ID**: 12289
**Date**: 2020-06-30
**URL**: https://discourse.slicer.org/t/how-to-define-and-save-output-of-a-cli-module-in-python-script/12289

---

## Post #1 by @Ponyo2311 (2020-06-30 09:22 UTC)

<p>Hi,<br>
I’m trying to run <strong>N4ITK Bias correction</strong> (a cli module) from Jupyter Notebook and am struggling with defining the output parameter.<br>
The code I wrote reads my inputs and creates a node, but I don’t know whether it ran (executed the bias correction) and how to save the output. I am working with NIFTII images.<br>
<strong>My code:</strong></p>
<p>input_volume=slicer.util.loadVolume(path_to_T1)<br>
slicernb.ViewDisplay()<span class="hashtag">#it</span> worked<br>
mask_volume=slicer.util.loadVolume(path_to_mask)<br>
slicernb.ViewDisplay()<span class="hashtag">#it</span> worked<br>
output_volume=(slicer.mrmlScene.AddNewNodeByClass (“vtkMRMLCommandLineModuleNode”,“Name_for_corrected volume.nii”))</p>
<p>slicer.mrmlScene.AddNode(output_volume)</p>
<p>parameters={}<br>
parameters[‘initialMeshResolution’]=(1,1,1)<br>
parameters[‘splineDistance’]=0.00<br>
parameters[‘bfFWHM’]=0.00<br>
parameters[‘numberOfIterations’]=(200,200,200)<br>
parameters[‘convergenceThreshold’]=0.0001<br>
parameters[‘bsplineOrder’]=3<br>
parameters[‘shrinkFactor’]=4<br>
parameters[‘weightImageName’]=‘None’<br>
parameters[‘wienerFilterNoise’]=0.00<br>
parameters[‘nHistogramBins’]=0<br>
parameters[‘inputImageName’]=input_volume.GetID()<br>
parameters[‘maskImageName’]=mask_volume.GetID()<br>
parameters[‘outputImageName’]=output_volume.GetID()<br>
parameters[‘outputBiasFieldName’]=‘None’</p>
<p>slicer.cli.run(slicer.modules.n4itkbiasfieldcorrection,node=None,parameters=parameters)</p>
<p><strong>How could I make it save a corrected T1 volume?</strong></p>

---

## Post #2 by @pieper (2020-06-30 18:57 UTC)

<p>You probably want <code>slicer.cli.runSync</code></p>
<p>See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python</a></p>

---

## Post #3 by @lassoan (2020-06-30 20:36 UTC)

<p>This issues comes up so often that I think we should change the default behavior of run to be <code>runSync</code>. It would be a good opportunity to do it now (for Slicer5). What do you think? <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #4 by @pieper (2020-07-01 00:36 UTC)

<p>Yes, that makes sense - people expect a python api to by synchronous by default.  Rather than a <code>runAsync</code> how about .a method called <code>start</code> to be more explicit what it does.</p>

---

## Post #5 by @Ponyo2311 (2020-07-01 09:04 UTC)

<p>Thank you for the reply.</p>
<p>I tried to run the code replacing <em>slicer.cli.run</em> by <em>slicer.cli.runSync</em> and now the Jupyter cell is just running for very long, still with no outputs whatsoever.</p>
<p>It would be useful to know what is happening so i tried add these commands (after restarting the kernel):</p>
<p><em>newNode=slicer.cli.runSync(slicer.modules.n4itkbiasfieldcorrection,<br>
node=None,parameters=parameters)<br>
newNode.GetOutputText()<br>
newNode.GetErrorText()</em></p>
<p>but with no messages displayed - it seems that the execution is somehow stuck at slicer.cli.runSync() for some reason.</p>
<p>Is there something wrong with my code?</p>

---

## Post #6 by @lassoan (2020-07-17 19:27 UTC)

<p>Can you provide the complete script (using one of the Slicer sample data sets as input)?</p>

---
