# slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode() Not workign with given SegmentIDs

**Topic ID**: 27998
**Date**: 2023-02-23
**URL**: https://discourse.slicer.org/t/slicer-modules-segmentations-logic-importlabelmaptosegmentationnode-not-workign-with-given-segmentids/27998

---

## Post #1 by @Alex_Shen (2023-02-23 05:42 UTC)

<p>Hi, having this issue trying to convert labelmap volume to a segmentation node.<br>
My labelmap volume here has only 0s and 1s, so theoretically, only one segment will be created running this function.</p>
<p>If I run the following code without specifying segmentIDs, everything works fine:</p>
<pre><code class="lang-auto">slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(volumeNode, segmentationNode)
</code></pre>
<p>The function returns true and expected segment is created with the default name (“jake”)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17e5cbf0c5ffa93a3ee292f788eb6fa990b65f3c.png" data-download-href="/uploads/short-url/3ppjLGsbK9LQvz1V3syJ0oBGBxG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17e5cbf0c5ffa93a3ee292f788eb6fa990b65f3c_2_690x50.png" alt="image" data-base62-sha1="3ppjLGsbK9LQvz1V3syJ0oBGBxG" width="690" height="50" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17e5cbf0c5ffa93a3ee292f788eb6fa990b65f3c_2_690x50.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17e5cbf0c5ffa93a3ee292f788eb6fa990b65f3c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17e5cbf0c5ffa93a3ee292f788eb6fa990b65f3c.png 2x" data-dominant-color="EEF3F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">735×54 4.57 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I want to give the segment a specific ID, so I can call it afterwards by running:</p>
<pre><code class="lang-auto">id = 'Fem_P'
ids = vtk.vtkStringArray()
ids.InsertNextValue(id)
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(volumeNode, segmentationNode, ids)
</code></pre>
<p>The function returns True and does NOT create segments.</p>
<p>Anyone knows why? Did I do something wrong when creating the <code>vtkStringArray</code>?</p>
<p>Thanks ahead</p>

---

## Post #2 by @Sunderlandkyl (2023-02-23 19:07 UTC)

<p>I’ve created a PR that should fix the issue here: <a href="https://github.com/Slicer/Slicer/pull/6835" class="inline-onebox" rel="noopener nofollow ugc">BUG: Create non-existing segments in ImportLabelmapToSegmentationNode by Sunderlandkyl · Pull Request #6835 · Slicer/Slicer · GitHub</a></p>

---

## Post #3 by @Alex_Shen (2023-02-23 23:09 UTC)

<p>Thanks for the quick PR on fixing this. Now I understand that to work around this problem, I can create an empty segment with the ID that I want to name it.</p>
<p>The following code works now:</p>
<p>id = ‘Fem_P’<br>
segmentationNode.GetSegmentation().AddEmptySegment(id)<br>
ids = vtk.vtkStringArray()<br>
ids.InsertNextValue(id)<br>
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(volumeNode, segmentationNode, ids)</p>

---
