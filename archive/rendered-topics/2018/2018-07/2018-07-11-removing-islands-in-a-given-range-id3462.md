---
topic_id: 3462
title: "Removing Islands In A Given Range"
date: 2018-07-11
url: https://discourse.slicer.org/t/3462
---

# Removing islands in a given range

**Topic ID**: 3462
**Date**: 2018-07-11
**URL**: https://discourse.slicer.org/t/removing-islands-in-a-given-range/3462

---

## Post #1 by @hherhold (2018-07-11 20:02 UTC)

<p>Greetings Slicers,</p>
<p>I’m trying to remove some islands in a given size range (100 voxels to 1000 voxels, for example) using some python code similar to that in SegmentEditorIslandsEffect.py. I can see where vtkITKIslandMath() is used to do the actual work, but how do I get the islandsMath for the segment in question? Is it in the segmentations module logic? Right now, I get zero for GetNumberOfIslands(), which I’m assuming is because it’s not “connected” to the segmentation. (I think…?)</p>
<p>I could modify SegmentEditorIslandsEffect to do this, I suppose, and just reload that, but I’d like to try my logic just on the python console for starters.</p>
<p>Hope this makes sense… Thanks in advance!!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2018-07-12 02:51 UTC)

<p>You can easily get islands of a given size range by removing islands below 100 and below 1000 (Islands effect) and then computing the difference (Logical operators effect). You can run Segment editor effects from your scripts as shown <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">here</a>.</p>

---

## Post #3 by @hherhold (2018-07-12 10:42 UTC)

<p>Wow, that’s about 100 times easier than what I had in mind…</p>
<p>Thanks, Andras!!!</p>
<p>-Hollister</p>

---

## Post #4 by @hherhold (2018-07-13 17:00 UTC)

<p>Here’s a gist of what I threw together to do this, if it’s useful for anyone.</p>
<p>Thanks for the tip!</p>
<aside class="onebox githubgist">
  <header class="source">
      <a href="https://gist.github.com/hherhold/ec3f74d20ca63866555f3e66d1f3621c" target="_blank" rel="nofollow noopener">gist.github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://gist.github.com/hherhold/ec3f74d20ca63866555f3e66d1f3621c" target="_blank" rel="nofollow noopener">https://gist.github.com/hherhold/ec3f74d20ca63866555f3e66d1f3621c</a></h4>
<h5>FindIslandsInSizeRange.py</h5>
<pre><code class="Python">original_Segment_Name = 'Segment_Name_Here'
low_island_size = 20
high_island_size = 200

#
# Switch to segment editor and pick logical effects, and get the segment to work on.
#
slicer.util.selectModule('SegmentEditor')
segmentEditorWidget = slicer.modules.segmenteditor.widgetRepresentation().self().editor
segmentEditorWidget.setActiveEffectByName("Logical operators")</code></pre>
This file has been truncated. <a href="https://gist.github.com/hherhold/ec3f74d20ca63866555f3e66d1f3621c" target="_blank" rel="nofollow noopener">show original</a>

<p>
</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
