---
topic_id: 37168
title: "Hide Node And Refresh View"
date: 2024-07-03
url: https://discourse.slicer.org/t/37168
---

# Hide node and refresh view

**Topic ID**: 37168
**Date**: 2024-07-03
**URL**: https://discourse.slicer.org/t/hide-node-and-refresh-view/37168

---

## Post #1 by @fqzhice (2024-07-03 09:18 UTC)

<p>Hi，</p>
<p>I just loaded segment file nii.gz by API slicer.util.loadSegmentation, then</p>
<p>i want to hide this node named “post_result”</p>
<pre><code class="lang-auto">auto vesselNode = vtkMRMLSegmentationNode::SafeDownCast(
    d-&gt;scene-&gt;GetFirstNodeByName("post_result")); //post_result
if (vesselNode == nullptr)
    return;
vesselNode-&gt;SetDisplayVisibility(false);
qSlicerLayoutManager* layoutManager = qSlicerApplication::application()-&gt;layoutManager();
if (layoutManager == nullptr)
    return;
for (auto viewName : layoutManager-&gt;sliceViewNames())
{
    layoutManager-&gt;sliceWidget(viewName)-&gt;sliceView()-&gt;forceRender();
}
</code></pre>
<p>the segmentation mask is still displayed on slicer view.<br>
But in “Data” Model, i can hide by click "eye"icon<br>
How can i solve it ?<br>
Thanks for help</p>

---

## Post #2 by @fqzhice (2024-07-04 10:33 UTC)

<p>Fixed!</p>
<aside class="quote" data-post="3" data-topic="13826">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/5f9b8f/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segmentation-visibility-by-code/13826/3">Segmentation visibility by code</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    hi 
this works to hide all segmentation: 
disp=slicer.util.getNode('Segmentation')
disp.SetDisplayVisibility(False)

but I can’t make it show only Left-Cerebral-Cortex . 
try this: 
slicer.vtkMRMLSegmentationDisplayNode('Segmentation').SetAllSegmentsVisibility(False)

but I have the following error: 
ValueError: could not extract hexadecimal address from argument string
  </blockquote>
</aside>


---
