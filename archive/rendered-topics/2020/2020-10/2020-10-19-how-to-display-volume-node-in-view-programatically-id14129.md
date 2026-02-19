---
topic_id: 14129
title: "How To Display Volume Node In View Programatically"
date: 2020-10-19
url: https://discourse.slicer.org/t/14129
---

# How to display volume node in view programatically

**Topic ID**: 14129
**Date**: 2020-10-19
**URL**: https://discourse.slicer.org/t/how-to-display-volume-node-in-view-programatically/14129

---

## Post #1 by @rbahegne (2020-10-19 08:27 UTC)

<p>I would like to show in all view a volume node present in the subject hierarchy, just like i click on the eye.<br>
I work in a loadable module in c++.</p>
<p>I searched for this function in Slicer sources, i found it in qSlicerSubjectHierarchyVolumesPlugin.<br>
IE : qSlicerSubjectHierarchyVolumesPlugin::showVolumeInAllViews</p>
<p>But my problem is that i did not manage to link to this plugin and use this function in my code, i know how to link to the modules, but here it is a plugin in the volumes module.</p>
<p>So how to achieve that ? Maybe there is another way to show a volume node in all view ?</p>

---

## Post #2 by @cpinter (2020-10-19 08:44 UTC)

<p>One way:</p>
<pre><code class="lang-auto">    appLogic = slicer.app.applicationLogic()
    selectionNode = appLogic.GetSelectionNode()
    selectionNode.SetActiveVolumeID(backgroundVolumeNodeID)
    appLogic.PropagateVolumeSelection()
</code></pre>
<p>Another way</p>
<pre><code class="lang-auto">    numberOfCompositeNodes = slicer.mrmlScene.GetNumberOfNodesByClass("vtkMRMLSliceCompositeNode")
    for i in range(numberOfCompositeNodes):
      compositeNode = slicer.mrmlScene.GetNthNodeByClass(i,"vtkMRMLSliceCompositeNode")
      compositeNode.SetBackgroundVolumeID(backgroundVolumeNodeID)
</code></pre>

---
