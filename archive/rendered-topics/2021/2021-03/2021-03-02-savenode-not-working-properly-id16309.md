---
topic_id: 16309
title: "Savenode Not Working Properly"
date: 2021-03-02
url: https://discourse.slicer.org/t/16309
---

# saveNode not working properly

**Topic ID**: 16309
**Date**: 2021-03-02
**URL**: https://discourse.slicer.org/t/savenode-not-working-properly/16309

---

## Post #1 by @user20s (2021-03-02 15:01 UTC)

<p>Hi. I am trying to use the python interactor tool to make some resampling automatic using the module brainresample.<br>
I have a code that loads the volumes, loads a transform and then gives parameters and calls the module. I am pretty sure this works all fine.</p>
<p>Before setting up the parameters, I create a new node using “AddNewNodeByClass”, and then I want to save the new node as nifti.</p>
<blockquote>
<pre><code>resampledNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
parameters = {'inputVolume': itemCT, 'referenceVolume': itemMR, 'outputVolume': resampledNode, 'warpTransform': itemTransform, 'interpolationMode': 'Linear'}

slicer.cli.run(slicer.modules.brainsresample, None, parameters)    
slicer.util.saveNode(resampledNode, output_filename)
</code></pre>
</blockquote>
<p>I try to run this piece of code (with the previous part defining the volumes and all) as an external file using: ./Slicer --no-main-window --python-script /home/user/Desktop/test_3D_slicer.py. It seems to run the module ok (Resample Image (BRAINS) completed without errors) but then does not save the new image.<br>
What’s strange is that if I input my code line by line in the python interactor (CTRL+3), it works and saves the new image. I wouldn’t want to do that though since the python file contains a for loop and it would just be easier if I could manage it through the external .py file.</p>
<p>Does anybody know why this happens?</p>

---

## Post #2 by @lassoan (2021-03-02 15:03 UTC)

<p>You need to use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html?highlight=runsync#slicer.cli.runSync"><code>runSync</code></a>, otherwise you save the output node before CLI execution is completed.</p>

---

## Post #4 by @user20s (2021-03-02 16:49 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks! That fixed it.</p>

---
