# How to write the code for resample in 3D slicer

**Topic ID**: 32693
**Date**: 2023-11-09
**URL**: https://discourse.slicer.org/t/how-to-write-the-code-for-resample-in-3d-slicer/32693

---

## Post #1 by @Chuan (2023-11-09 12:47 UTC)

<p>Hi all,</p>
<p>Does anyone know what is the correct code for resampling and resave the volume file as mhd format?<br>
Basically, what I have is a nrrd file named disp, a reference nrrd file named ref, and a tranform file named tran.<br>
I would like to go to the module of ’ Resample Scalar/Vector/DWI Volume’ and output a new vector volume, and save this new output vector volume as mhd format.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c73aa5ca44d55d7c767490c5781c07527871faf9.png" alt="image" data-base62-sha1="sqsFrWIuKpMoZ616nrf3jBI5Ssx" width="532" height="382"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/246bdf29ad15ccdd4aeb8886b06ecf7897501c47.png" data-download-href="/uploads/short-url/5cciMVz3ygK00Mj54zcjFBGOG1N.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/246bdf29ad15ccdd4aeb8886b06ecf7897501c47_2_540x500.png" alt="image" data-base62-sha1="5cciMVz3ygK00Mj54zcjFBGOG1N" width="540" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/246bdf29ad15ccdd4aeb8886b06ecf7897501c47_2_540x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/246bdf29ad15ccdd4aeb8886b06ecf7897501c47.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/246bdf29ad15ccdd4aeb8886b06ecf7897501c47.png 2x" data-dominant-color="E2E5E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">569×526 74.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da2288af968fd1d78e9cf60a37dd7972eca79622.png" data-download-href="/uploads/short-url/v7I4MBpEzGmzpyO9UOQLi6F3UTU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da2288af968fd1d78e9cf60a37dd7972eca79622_2_420x500.png" alt="image" data-base62-sha1="v7I4MBpEzGmzpyO9UOQLi6F3UTU" width="420" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da2288af968fd1d78e9cf60a37dd7972eca79622_2_420x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da2288af968fd1d78e9cf60a37dd7972eca79622.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da2288af968fd1d78e9cf60a37dd7972eca79622.png 2x" data-dominant-color="EBEEF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">541×643 72.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is what I used.</p>
<p>############# save as mhd file<br>
parameters = {}<br>
parameters[‘inputVolume’] = slicer.util.getNode(‘DISP’)<br>
<span class="hashtag-raw">#Set</span> output as vector volume<br>
parameters[‘outputVolume’] = slicer.util.getNode(‘DISP’)<br>
parameters[‘referenceVolume’] = slicer.util.getNode(REF)<br>
parameters[‘transformationFile’] = slicer.util.getNode(‘TRAN’)<br>
parameters[‘interpolationType’] = interpolationType</p>
<p>cliNode = slicer.cli.runSync(slicer.modules.resamplescalarvectordwivolume,None,parameters)</p>
<p>volumeNode = slicer.mrmlScene.GetFirstNodeByClass(‘vtkMRMLScalarVolumeNode’)<br>
slicer.util.saveNode(volumeNode , outputDisplacementfield_resampled,{“useCompression”: 0})</p>
<p>But this is wrong, I am so confused that I can not get the correct output from my code. Does anyone help me to check my code?</p>
<p>Thanks for any kinds of discussion and help.<br>
Best,<br>
Chuan</p>

---

## Post #2 by @Chuan (2023-11-09 19:38 UTC)

<p>I use below code, and seems work!</p>
<p>############# save as mhd file<br>
outputVectorNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLVectorVolumeNode”)<br>
outputVectorNode.SetName(‘disp_PIPER_skinskel_afterDemons_afterresample’)</p>
<p>parameters = {}<br>
parameters[‘inputVolume’] = slicer.util.getNode(‘disp_PIPER_skinskel_afterDemons’)<br>
<span class="hashtag-raw">#Set</span> output as vector volume<br>
parameters[‘outputVolume’] = slicer.util.getNode(‘disp_PIPER_skinskel_afterDemons_afterresample’)<br>
parameters[‘referenceVolume’] = slicer.util.getNode(name_ref)<br>
parameters[‘transformationFile’] = slicer.util.getNode(‘LinearTransform_3’)<br>
parameters[‘interpolationType’] = interpolationType</p>
<p>cliNode = slicer.cli.runSync(slicer.modules.resamplescalarvectordwivolume,None,parameters)</p>
<p>slicer.util.saveNode(outputVectorNode, outputDisplacementfield_resampled,{“useCompression”: 0})</p>

---
