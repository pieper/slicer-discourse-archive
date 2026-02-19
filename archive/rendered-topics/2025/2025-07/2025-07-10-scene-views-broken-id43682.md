---
topic_id: 43682
title: "Scene Views Broken"
date: 2025-07-10
url: https://discourse.slicer.org/t/43682
---

# Scene views broken?

**Topic ID**: 43682
**Date**: 2025-07-10
**URL**: https://discourse.slicer.org/t/scene-views-broken/43682

---

## Post #1 by @muratmaga (2025-07-10 20:51 UTC)

<p>When I try to use scene views, I can capture the node state but cannot restore from it. This is on latest preview on Mac. There are also messages like this in the log file:</p>
<pre><code class="lang-auto">Switch to module:  "SceneViews"
"Segmentation" Reader has successfully read the file "/Users/amaga/Desktop/MD_Repos/human_trunk-issue-16/issue-16.seg.nrrd" "[0.15s]"
Switch to module:  "Data"
Module  "Annotations"  associated with node class  "vtkMRMLAnnotationSnapshotNode"  does not have widget
</code></pre>

---

## Post #2 by @pieper (2025-07-11 14:14 UTC)

<p>I tried some simple things using the mac preview from July 9 and scene views seem to work as expected.</p>

---

## Post #3 by @muratmaga (2025-07-11 15:41 UTC)

<p>ok will try july 9, mine was 8th. it just restore the state. no error, nothing.</p>

---

## Post #4 by @muratmaga (2025-07-11 19:04 UTC)

<p>Further testing show that lack of response related to 3D models. Everything works fine if the rendered object is a volume. Scene views doesn’t restore the layout, if a model or a segmentation is loaded.</p>

---
