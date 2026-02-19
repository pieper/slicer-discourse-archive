---
topic_id: 19345
title: "Elastix Registration Jupyter"
date: 2021-08-24
url: https://discourse.slicer.org/t/19345
---

# Elastix registration-Jupyter

**Topic ID**: 19345
**Date**: 2021-08-24
**URL**: https://discourse.slicer.org/t/elastix-registration-jupyter/19345

---

## Post #1 by @gevindug (2021-08-24 17:33 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11</p>
<p>Elastix registration is not working with the ‘generic rigid’ parameter file. can anyone help me to solve this issue? Actually, I wants to perform the wrist registration.</p>
<p>Current time: Tue Aug 24 22:54:02 2021.<br>
Reading the elastix parameters from file …</p>
<p>ERROR: when reading the parameter file:</p>
<p>itk::ExceptionObject (000000C375D1F210)<br>
Location: “unknown”<br>
File: D:\D\S\S-1-E-b\SlicerElastix-build\elastix\Common\ParameterFileParser\itkParameterFileParser.cxx<br>
Line: 116<br>
Description: itk::ERROR: itk::ERROR: ParameterFileParser(00000257A0F2A430): ERROR: the file E:\slicer\Slicer 4.11.20210226\NA-MIC\Extensions-29738\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Resources\RegistrationParameters\g does not exist.</p>
<p>ERROR: Something went wrong during initialization of the configuration object.<br>
ERROR:<br>
The configuration object has not been initialized.<br>
Errors occurred!</p>

---

## Post #2 by @lassoan (2021-08-25 05:49 UTC)

<p>It seems that the parameter file got corrupted. Reinstalling the extension should solve the problem.</p>

---

## Post #3 by @gevindug (2021-08-25 10:05 UTC)

<p>I reinstall the extension. Still, the same error occurs.<br>
my code is as follows</p>
<pre><code>RegistrationPresets_ParameterFilenames = 2
parameterFilenames = logic.getRegistrationPresets()[24][RegistrationPresets_ParameterFilenames]
outputVolume = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode')
outtrans=slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTransformNode')
slicer.mrmlScene.AddNode(outputVolume)
outputVolume.CreateDefaultDisplayNodes()
outputVolume.SetName(Nodename)
outtrans.SetName(Nodename)
logic.registerVolumes(fixedVolumeNode= fixedVolumeNode,movingVolumeNode=movingVolumeNode, parameterFilenames = parameterFilenames , outputVolumeNode = outputVolume ,outputTransformNode =outtrans, fixedVolumeMaskNode = dialatedmasklabelmapVolumeNode)
</code></pre>
<p>When using the following combination it works. but not registering properly.</p>
<p>RegistrationPresets_ParameterFilenames = 5<br>
parameterFilenames = logic.getRegistrationPresets()[1][RegistrationPresets_ParameterFilenames]</p>

---

## Post #4 by @lassoan (2021-08-26 05:50 UTC)

<p>OK, so it seems that the previous problem was solved.</p>
<p>The problems that you have now is due to modifying a built-in constant. <code>Elastix.RegistrationPresets_ParameterFilenames</code> constant is set to 5 and must be kept that way. This is the index of the parameter filenames in the preset list.</p>
<p>This code works perfectly for me:</p>
<pre><code class="lang-python">import Elastix
import SampleData

fixedVolume =  SampleData.downloadSample('MRBrainTumor1')
movingVolume =  SampleData.downloadSample('MRBrainTumor2')
outputVolume = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode')
outputTransform = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTransformNode')
presetIndex = 0

elastixLogic = Elastix.ElastixLogic()
parameterFilenames = elastixLogic.getRegistrationPresets()[presetIndex][Elastix.RegistrationPresets_ParameterFilenames]
elastixLogic.registerVolumes(
    fixedVolume, movingVolume,
    outputVolumeNode = outputVolume,
    parameterFilenames = parameterFilenames,
    outputTransformNode = outputTransform,
    forceDisplacementFieldOutputTransform = True)
</code></pre>
<p>You can change the <code>presetIndex = 2</code>, it might give a tiny bit better result, but it also take much longer. In general, I’ve found that the two “generic” presets work very well, but the other presets are hit and miss. They are taken from the Elastix parameter database, so they should work for the specific use cases they developed for, but you may need to experiment with them a bit and tune parameters to work well for your registration tasks.</p>
<p>Also note that Elastix-&gt;ITK transformation file conversion is not robust (<a href="https://github.com/lassoan/SlicerElastix/issues/33" class="inline-onebox">BSpline output transform is not always correct · Issue #33 · lassoan/SlicerElastix · GitHub</a>), but the resampled output volume and grid transform output are always correct.</p>
<p>ANTs registration extension has been recently added to Slicer. It works very well, too (default presets should work without parameter tuning). You may give it a try.</p>

---

## Post #5 by @gevindug (2021-08-28 20:17 UTC)

<p>This works for me. Thank you for that. But in some cases the accuracy is questionable. Is there any other way to perform rigid registration.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4adfd393ce650f931e6db6792605288b205dbab0.png" alt="image" data-base62-sha1="aGmSubY5GDMeCXkrzZjWsgH4dNe" width="204" height="187"></p>
<p>I got the results somewhat like this</p>

---

## Post #6 by @lassoan (2021-08-28 22:14 UTC)

<p>Does the output image (resampled moving image) aligns well with the fixed image?<br>
If yes, then the misalignment is probably due to the Elastix transform reading bug that I mentioned above (that you can solve by forcing grid transform output).</p>

---

## Post #7 by @gevindug (2021-08-29 14:29 UTC)

<p>It gives good outputs only the displacement of the moving image is small. When it comes to large deformation it is not working properly.<br>
I was thinking to perform registration again and again until it gives a good result. So Is there any way to register with an initial transform?</p>

---
