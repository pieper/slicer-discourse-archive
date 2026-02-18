# Error message: `vtkMRMLStorableNode::UpdateScene failed: Failed to read node`

**Topic ID**: 24225
**Date**: 2022-07-07
**URL**: https://discourse.slicer.org/t/error-message-vtkmrmlstorablenode-updatescene-failed-failed-to-read-node/24225

---

## Post #1 by @sandigeeup (2022-07-07 15:48 UTC)

<p>Error: Loading C:/Users/sandi/OneDrive/Desktop/Slicer - Canine Liver/Tumour cases/2022-07-06-Tumour case 1mrml.mrml - ERROR: In D:\D\S\S-0\Libs\MRML\Core\vtkMRMLStorableNode.cxx, line 322<br>
vtkMRMLScalarVolumeNode (000001C707605640): vtkMRMLStorableNode::UpdateScene failed: Failed to read node AbsImageFilter Output (vtkMRMLScalarVolumeNode4) using storage node vtkMRMLVolumeArchetypeStorageNode4.</p>
<p>I have numerous error messge coming on when loading the dicom datasets. I have no clue what this means. Please help.</p>

---

## Post #2 by @muratmaga (2022-07-07 16:54 UTC)

<aside class="quote no-group" data-username="sandigeeup" data-post="1" data-topic="24225">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sandigeeup/48/13722_2.png" class="avatar"> sandigeeup:</div>
<blockquote>
<p>C:/Users/sandi/OneDrive/Desktop/Slicer - Canine Liver/Tumour case</p>
</blockquote>
</aside>
<p>You are storing your data on OneDrive share. I can’t say for sure that’s the root of the problem, but I have seen strange data loading issues in such cases.</p>
<p>I suggest trying to copy your your data that’s not inside the onedrive and load from there (e.g.,try c:/temp).</p>

---

## Post #3 by @lassoan (2022-07-07 18:18 UTC)

<p>It might be some orphan storage node of some volume that was not saved (maybe it was empty or invalid or it was just not selected to be saved when the scene was saved). You can probably ignore the error.</p>

---

## Post #4 by @sandigeeup (2022-07-08 09:21 UTC)

<p>Thank you! I am having problems with my one drive. Also, slicer is crashing a lot. I will try what you suggest and go from there.  Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
