# saveNode doesn't work properly

**Topic ID**: 16308
**Date**: 2021-03-02
**URL**: https://discourse.slicer.org/t/savenode-doesnt-work-properly/16308

---

## Post #1 by @user20s (2021-03-02 15:00 UTC)

<p>Operating system: Linux Ubuntu 18.04.5 LTS<br>
Slicer version: 4.11.20210226-linux-amd64<br>
Expected behavior: saving a nifti file using saveNode<br>
Actual behavior: not saving</p>
<p>Hi all, I have a code written in python which should load some volumes and a transform and use the module brain resample.</p>
<p>It seems to work fine and when I run it using the command:</p>
<blockquote>
<p>./Slicer --no-main-window --python-script /home/user/Desktop/test_3D_slicer.py</p>
</blockquote>
<p>it outputs a table with standard output and at the end the line: "Resample Image (BRAINS) completed without errors. The problem is that it doesn’t save the new resampled image. I attach part of the code I use below. This is within a for loop where I change all parameters each iteration.</p>
<blockquote>
<pre><code>resampledNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
parameters = {'inputVolume': itemCT, 'referenceVolume': itemMR, 'outputVolume': resampledNode,
              'warpTransform': itemTransform, 'interpolationMode': 'Linear'}

slicer.cli.run(slicer.modules.brainsresample, None, parameters)
slicer.util.saveNode(resampledNode, output_filename)
</code></pre>
</blockquote>
<p>It seems to run fine except for not saving the new nifti. But if I copy paste each line of my code in the python interactor (CTRL+3) for just one iteration, it saves it and also in the right folder so surely output_filename is defined correctly.</p>
<p>Any ideas why this happens?</p>

---

## Post #2 by @lassoan (2021-03-02 15:04 UTC)

<p>A post was merged into an existing topic: <a href="/t/savenode-not-working-properly/16309">saveNode not working properly </a></p>

---

## Post #3 by @lassoan (2021-03-02 15:04 UTC)



---
