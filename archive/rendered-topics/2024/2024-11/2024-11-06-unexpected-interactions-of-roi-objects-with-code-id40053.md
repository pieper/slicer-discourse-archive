---
topic_id: 40053
title: "Unexpected Interactions Of Roi Objects With Code"
date: 2024-11-06
url: https://discourse.slicer.org/t/40053
---

# Unexpected interactions of ROI objects with code

**Topic ID**: 40053
**Date**: 2024-11-06
**URL**: https://discourse.slicer.org/t/unexpected-interactions-of-roi-objects-with-code/40053

---

## Post #1 by @shai-ikko (2024-11-06 13:43 UTC)

<p>This continues the topic <a href="https://discourse.slicer.org/t/configure-roi-to-match-volume-through-code/39695" class="inline-onebox">Configure ROI to match volume through code</a> but I think that post was not phrased very well, so let’s start again:</p>
<p>I’m creating a ROI with code based on an example from the script repository:</p>
<pre data-code-wrap="python"><code class="lang-python">self.roiNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsROINode")

cropVolumeParameters = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLCropVolumeParametersNode")
cropVolumeParameters.SetInputVolumeNodeID(self.volumeNode.GetID())
cropVolumeParameters.SetROINodeID(self.roiNode.GetID())
slicer.modules.cropvolume.logic().FitROIToInputVolume(cropVolumeParameters)
slicer.mrmlScene.RemoveNode(cropVolumeParameters)
</code></pre>
<p>I get this ROI object:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bef11f98100e31f03121908c2e8db91de0926299.jpeg" data-download-href="/uploads/short-url/rf9k58zDrtIa0tS6GviUceBpQx3.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bef11f98100e31f03121908c2e8db91de0926299_2_664x500.jpeg" alt="image" data-base62-sha1="rf9k58zDrtIa0tS6GviUceBpQx3" width="664" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bef11f98100e31f03121908c2e8db91de0926299_2_664x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bef11f98100e31f03121908c2e8db91de0926299.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bef11f98100e31f03121908c2e8db91de0926299.jpeg 2x" data-dominant-color="AFA4A2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">966×727 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But now if I tell it its ObjectToNode matrix is updated, it jumps (I need this because, as you can see, I give users rotation handles, and I also want to give them a “reset” button). And indeed, the center in the world has changed:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e142e429ac847e140c68176d2ac4458b7730d82.jpeg" data-download-href="/uploads/short-url/fHNL2tkKKux7LXYCJYdtUQn0mvU.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e142e429ac847e140c68176d2ac4458b7730d82_2_589x500.jpeg" alt="image" data-base62-sha1="fHNL2tkKKux7LXYCJYdtUQn0mvU" width="589" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e142e429ac847e140c68176d2ac4458b7730d82_2_589x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e142e429ac847e140c68176d2ac4458b7730d82_2_883x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e142e429ac847e140c68176d2ac4458b7730d82.jpeg 2x" data-dominant-color="B2B0AE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">968×821 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Now, here come some funnier parts: If I try to reset the center in the world, it doesn’t work:</p>
<pre data-code-wrap="python"><code class="lang-python">&gt;&gt;&gt; roi.SetCenterWorld(center)
&gt;&gt;&gt; roi.GetCenterWorld()
vtkmodules.vtkCommonDataModel.vtkVector3d([0.0, 0.0, 0.0])
&gt;&gt;&gt; center
vtkmodules.vtkCommonDataModel.vtkVector3d([0.38079845905303955, -22.919204711914062, -175.25])
</code></pre>
<p>If I first reset the center to 0, then it semi-works: After</p>
<pre><code class="lang-auto">&gt;&gt;&gt; roi.SetCenterWorld([0,0,0])
&gt;&gt;&gt; roi.SetCenterWorld(center)
</code></pre>
<p>the ROI is visually back to its place fitting the volume, but</p>
<pre><code class="lang-auto">&gt;&gt;&gt; roi.GetCenterWorld()
vtkmodules.vtkCommonDataModel.vtkVector3d([0.0, 0.0, 0.0])
</code></pre>
<p>I’m not even sure what exactly is the bug I should report, but I’m pretty convinced that this Can’t Be Right <img src="https://emoji.discourse-cdn.com/twitter/tm.png?v=12" title=":tm:" class="emoji" alt=":tm:" loading="lazy" width="20" height="20">.</p>
<p>Slicer 5.6.2 on Ubuntu 20.04.</p>

---

## Post #2 by @lassoan (2024-11-07 05:13 UTC)

<p>I cannot reproduce any “jump” with neither the latest Slicer Stable Release (Slicer-5.6.2) nor the latest Slicer Preview Release (Slicer-5.7):</p>
<pre data-code-wrap="python"><code class="lang-python">import SampleData
volumeNode = SampleData.downloadSample('CTChest')

roiNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsROINode")
cropVolumeParameters = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLCropVolumeParametersNode")
cropVolumeParameters.SetInputVolumeNodeID(volumeNode.GetID())
cropVolumeParameters.SetROINodeID(roiNode.GetID())
slicer.modules.cropvolume.logic().FitROIToInputVolume(cropVolumeParameters)
slicer.mrmlScene.RemoveNode(cropVolumeParameters)

print(roiNode.GetCenter())
print(roiNode.GetCenterWorld())
roiNode.GetObjectToNodeMatrix().Modified()
print(roiNode.GetCenter())
print(roiNode.GetCenterWorld())
</code></pre>

---

## Post #3 by @shai-ikko (2024-11-07 15:02 UTC)

<p>Thanks for the quick turnaround.</p>
<p>Following your message, I went and dug deeper, and was able to pinpoint the issue. Indeed, the code in the script repository is innocent. The issue turns out to be elsewhere.</p>
<p>Besides what I reported earlier, I have a callback for changes in the ROI. Among other things, it takes the ROI’s <code>ObjectToWorldMatrix</code>, and changes it a little in order to do some computations. I didn’t think this was relevant, because the documentation specifically <a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsROINode.html#a540216cdf23db6e5766b84238e638996" rel="noopener nofollow ugc">says</a> that “Changes made to the matrix will not be applied”. And indeed, in most uses, this appears to be the case – but not if the change is in a callback for modifications.</p>
<p>To reproduce the jump:</p>
<pre data-code-wrap="python"><code class="lang-python">import SampleData
volumeNode = SampleData.downloadSample('CTChest')

roiNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsROINode")
cropVolumeParameters = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLCropVolumeParametersNode")
cropVolumeParameters.SetInputVolumeNodeID(volumeNode.GetID())
cropVolumeParameters.SetROINodeID(roiNode.GetID())
slicer.modules.cropvolume.logic().FitROIToInputVolume(cropVolumeParameters)
slicer.mrmlScene.RemoveNode(cropVolumeParameters)

def onROIModified(roi, event) -&gt; None:
    mat4 = roi.GetObjectToWorldMatrix()
    for i in range(3):
        mat4.SetElement(i, 3, 0.0)
roiNode.AddObserver(vtk.vtkCommand.ModifiedEvent, onROIModified)

print(roiNode.GetCenter())
print(roiNode.GetCenterWorld())
roiNode.GetObjectToNodeMatrix().Modified()
print(roiNode.GetCenter())
print(roiNode.GetCenterWorld())
</code></pre>
<p>Now I know how to avoid the problem in my code; I maintain that the behavior shown here is surprising and even buggy, but I can totally see why fixing it would be more trouble than it’s worth – and perhaps some documentation fix is most appropriate.</p>

---

## Post #4 by @lassoan (2024-11-07 16:31 UTC)

<p>ObjectToWorldMatrix is computed internally and must not be modified. The <code>Changes made to the matrix will not be applied</code> note meant to say that developers should not modify the matrix (if modifications has no effect then why would anyone change it?), but it seems that we have to be more explicit.</p>
<p>We could also change the API to require an input vtkMatrix4x4 object. It would prevent any invalid changes, but it would be a bit less convenient (you would need to create a new object before you call the Get… function).</p>

---

## Post #5 by @shai-ikko (2024-11-11 09:49 UTC)

<p>I made a little initial <a href="https://github.com/Slicer/Slicer/pull/8034" rel="noopener nofollow ugc">PR</a> for this.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="40053">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>developers should not modify the matrix (if modifications has no effect then why would anyone change it?)</p>
</blockquote>
</aside>
<p>As hinted, in my case, I’m using the ROI as a control element, to pick a rotation which I want to apply elsewhere; however, I don’t want to apply the translation. One way to achieve this, if I’m not mistaken, is to take this matrix, and zero out the first three cells of the last column.</p>

---
