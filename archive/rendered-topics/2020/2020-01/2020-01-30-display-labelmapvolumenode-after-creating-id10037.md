# Display LabelMapVolumeNode After creating

**Topic ID**: 10037
**Date**: 2020-01-30
**URL**: https://discourse.slicer.org/t/display-labelmapvolumenode-after-creating/10037

---

## Post #1 by @kleingeo (2020-01-30 19:27 UTC)

<p>In Python, I create a script to create a segmentation of a vertebrae after selecting it with a fiducial marker. It works as expected, but I am unable to have the segmentation automatically display. Here is what I currently have, but I am unsure why this isn’t working.</p>
<pre><code class="lang-python">segVolumeNode = sitkUtils.PushVolumeToSlicer(seg,
                                             name='Segmentation',
                                             className='vtkMRMLLabelMapVolumeNode')

slicer.mrmlScene.AddNode(segVolumeNode)
segVolumeNode.CreateDefaultDisplayNodes()
segVolumeNode.SetVisibility(1)
</code></pre>
<p>This does not seem to work, and I am not entirely sure what the issue is.</p>

---

## Post #2 by @lassoan (2020-01-30 19:30 UTC)

<p>A post was merged into an existing topic: <a href="/t/automatically-view-labelmapnodes/10036">Automatically view LabelMapNodes</a></p>

---

## Post #3 by @lassoan (2020-01-30 19:30 UTC)



---
