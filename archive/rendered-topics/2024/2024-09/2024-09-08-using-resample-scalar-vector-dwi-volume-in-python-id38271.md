---
topic_id: 38271
title: "Using Resample Scalar Vector Dwi Volume In Python"
date: 2024-09-08
url: https://discourse.slicer.org/t/38271
---

# Using Resample Scalar/Vector/DWI Volume in python

**Topic ID**: 38271
**Date**: 2024-09-08
**URL**: https://discourse.slicer.org/t/using-resample-scalar-vector-dwi-volume-in-python/38271

---

## Post #1 by @lord_bubbacub (2024-09-08 03:18 UTC)

<h1><a name="p-116060-httpsslicerreadthedocsioenlatestuser_guidemodulesresamplescalarvectordwivolumehtml-1" class="anchor" href="#p-116060-httpsslicerreadthedocsioenlatestuser_guidemodulesresamplescalarvectordwivolumehtml-1" aria-label="Heading link"></a><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/resamplescalarvectordwivolume.html" class="inline-onebox" rel="noopener nofollow ugc">Resample Scalar/Vector/DWI Volume — 3D Slicer documentation</a></h1>
<p>Hi I’m trying to automate use of the resamplescalarvectordwivolume using python in the slicer console. My operation involves rescaling a ct based volume to match the geometry of a registered mri volume. The operation I am trying to do works great using the GUI but I am not making any progress on using this module in python. I’ve tried the docs and forums but have only found examples related to the older deprecated resample scalar volume module which does not work on my data sets.</p>
<p>I’ve got a few hundred operations to perform so would value being able to do this programatically.</p>
<p>My current code is below. The transform is a (previously computed) transform that is applied to register the CT binary labelmap to the MRI. The croppedCT input is cropped to match the exact volume of the mri volume (using ROI tools within python)</p>
<pre><code>reslicedVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", final_output)
parameters = {
    "inputVolume":croppedCT.GetID(),
    "interpolationType":'nn',
    "referenceVolume": mriNode.GetID(),
    "outputVolume":reslicedVolumeNode.GetID(),
    "transformationFile":loadedTransform.GetID()}

res = slicer.cli.run(slicer.modules.resamplescalarvectordwivolume, parameters)
</code></pre>
<p>I would really value some help in finding out how to use the amazing features of this module within python.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @pieper (2024-09-08 16:00 UTC)

<p><code>slicer.cli.run</code> operates in a thread.  Try <code>runSync</code> instead?</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/PerkLab/SlicerSandbox/blob/8c2da5d800018289a53bade31802650113140f2c/CurvedPlanarReformat/CurvedPlanarReformat.py#L436-L446">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerSandbox/blob/8c2da5d800018289a53bade31802650113140f2c/CurvedPlanarReformat/CurvedPlanarReformat.py#L436-L446" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerSandbox/blob/8c2da5d800018289a53bade31802650113140f2c/CurvedPlanarReformat/CurvedPlanarReformat.py#L436-L446" target="_blank" rel="noopener">PerkLab/SlicerSandbox/blob/8c2da5d800018289a53bade31802650113140f2c/CurvedPlanarReformat/CurvedPlanarReformat.py#L436-L446</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="436" style="counter-reset: li-counter 435 ;">
          <li># Resample input volume to straightened volume</li>
          <li>parameters = {}</li>
          <li>parameters["inputVolume"] = volumeNode.GetID()</li>
          <li>parameters["outputVolume"] = outputStraightenedVolume.GetID()</li>
          <li>parameters["referenceVolume"] = outputStraightenedVolume.GetID()</li>
          <li>parameters["transformationFile"] = straighteningTransformNode.GetID()</li>
          <li># Use nearest neighbor interpolation for label volumes (to avoid incorrect labels at boundaries)</li>
          <li># and higher-order (bspline) interpolation for scalar volumes.</li>
          <li>parameters["interpolationType"] = "nn" if volumeNode.IsA('vtkMRMLLabelMapVolumeNode') else "bs"</li>
          <li>resamplerModule = slicer.modules.resamplescalarvectordwivolume</li>
          <li>parameterNode = slicer.cli.runSync(resamplerModule, None, parameters)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lord_bubbacub (2024-09-08 17:44 UTC)

<p>Thank you. That’s magic, Problem solved.<br>
I wonder if the docs could be improved with some basic information on using this module within python and 3d slicer.</p>

---

## Post #4 by @pieper (2024-09-08 18:05 UTC)

<aside class="quote no-group" data-username="lord_bubbacub" data-post="3" data-topic="38271">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/d26b3c/48.png" class="avatar"> lord_bubbacub:</div>
<blockquote>
<p>I wonder if the docs could be improved</p>
</blockquote>
</aside>
<p>Yes, please make any suggestions as a <a href="https://github.com/Slicer/Slicer/blob/main/Docs/index.md">pull request on the docs</a>.</p>

---
