---
topic_id: 28184
title: "Slice Spacing In Fluoroscopic Angiography"
date: 2023-03-06
url: https://discourse.slicer.org/t/28184
---

# slice spacing in fluoroscopic angiography

**Topic ID**: 28184
**Date**: 2023-03-06
**URL**: https://discourse.slicer.org/t/slice-spacing-in-fluoroscopic-angiography/28184

---

## Post #1 by @pwaver (2023-03-06 03:39 UTC)

<p>Operating system: Ubuntu 22.04.2 LTS<br>
Slicer version:5.2.2<br>
Expected behavior: There is an image spacing warning on DICOM load of a fluoroscopic angiogram. Expect an edit of image spacing in the Volumes module to be sustained at least for the session.<br>
Actual behavior: After one or two clicks on the image panes the image spacing reverts to the wrong initial one. How to make an image spacing correction be retained?</p>

---

## Post #2 by @lassoan (2023-03-06 03:56 UTC)

<p>Slicer loads fluoroscopy images are time sequences: each timepoint is a separate image. You can apply a transform to change the physical scale of the entire sequence at once.</p>
<p>You could change the spacing of all images in the series by a few Python commands. However, what we see is that if someone uses Slicer (and not a basic 2D viewer) then fluoro images end up fused with 3D images, and then changing the pixel spacing is insufficient, but you need to compute a full projection transform.</p>
<p>What do you do with fluoro images in Slicer? Do you do just basic 2D visualization and measurements or you fuse them with 3D?</p>

---

## Post #3 by @pwaver (2023-03-06 14:28 UTC)

<p>Thank you — this gives me good reason to learn the Slicer-python interface. Any pointers on the precise python lines to apply the code? I wish to perform image by image segmentation and measurement then aggregate the frame-wise result into 2DxT ~ 3D-ish.</p>

---

## Post #4 by @lassoan (2023-03-06 22:46 UTC)

<aside class="quote no-group" data-username="pwaver" data-post="3" data-topic="28184">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pwaver/48/18641_2.png" class="avatar"> pwaver:</div>
<blockquote>
<p>Any pointers on the precise python lines to apply the code?</p>
</blockquote>
</aside>
<p>Something like this should work:</p>
<pre data-code-wrap="python"><code class="lang-python">volumeSequenceNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSequenceNode")

# Modify spacing in all nodes in the sequence
for volumeIndex in range(volumeSequenceNode.GetNumberOfDataNodes()):
    volumeNode = volumeSequenceNode.GetNthDataNode(volumeIndex)
    volumeNode.SetSpacing(2.0, 2.5, 1.4)

# Force update of volume node from sequence
sequenceLogic = slicer.modules.sequences.logic()
volumeSequenceBrowserNode = sequenceLogic.GetFirstBrowserNodeForSequenceNode(volumeSequenceNode)
sequenceLogic.UpdateProxyNodesFromSequences(volumeSequenceBrowserNode)
</code></pre>
<p>You can find more examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#sequences">script repository</a>.</p>
<p>To get started with Python scripting in Slicer, I would recommend the <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx">PerkLab Bootcamp Slicer programming tutorial</a>.</p>

---

## Post #5 by @LeonaTow (2023-03-27 01:18 UTC)

<p>Thanks for the link, you made my day.</p>

---

## Post #6 by @pwaver (2023-03-27 01:28 UTC)

<p>Agree, great answer by lassoan, thank you.</p>

---

## Post #7 by @LeonaTow (2023-03-27 12:51 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="4" data-topic="28184">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Something like this should work:</p>
<details>
<summary>
</summary>
<p>Yeah, I am glad I found this post. If you want to create an essay but don’t know how, you might visit this website: <a href="https://writinguniverse.com/essay-checklist/" rel="noopener nofollow ugc">https://writinguniverse.com/essay-checklist/</a> this instructs you on how to create an essay and how many different sorts of essays exist.</p>
</details>
<pre><code class="lang-auto">volumeSequenceNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSequenceNode")

# Modify spacing in all nodes in the sequence
for volumeIndex in range(volumeSequenceNode.GetNumberOfDataNodes()):
    volumeNode = volumeSequenceNode.GetNthDataNode(volumeIndex)
    volumeNode.SetSpacing(2.0, 2.5, 1.4)

# Force update of volume node from sequence
sequenceLogic = slicer.modules.sequences.logic()
volumeSequenceBrowserNode = sequenceLogic.GetFirstBrowserNodeForSequenceNode(volumeSequenceNode)
sequenceLogic.UpdateProxyNodesFromSequences(volumeSequenceBrowserNode)
</code></pre>
<p>You can find more examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#sequences" rel="noopener nofollow ugc">script repository</a>.</p>
<p>To get started with Python scripting in Slicer, I would recommend the <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx" rel="noopener nofollow ugc">PerkLab Bootcamp Slicer programming tutorial</a>.</p>
</blockquote>
</aside>
<p>Yeah, I am glad I found this post.</p>

---
