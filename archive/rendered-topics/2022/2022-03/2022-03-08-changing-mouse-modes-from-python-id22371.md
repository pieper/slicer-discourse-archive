---
topic_id: 22371
title: "Changing Mouse Modes From Python"
date: 2022-03-08
url: https://discourse.slicer.org/t/22371
---

# Changing mouse modes from Python

**Topic ID**: 22371
**Date**: 2022-03-08
**URL**: https://discourse.slicer.org/t/changing-mouse-modes-from-python/22371

---

## Post #1 by @vanlangk (2022-03-08 15:03 UTC)

<p>Hello guys, I am new to Slicer and I am currently developing an extension. As part of this extension, I need to be able to switch between mouse interaction modes (e.g., ruler, fiducial, angle), from my Python script. Is there an easy way to this from the API?</p>
<p>I have looked into the <a href="https://apidocs.slicer.org/v4.8/classvtkMRMLInteractionNode.html" rel="noopener nofollow ugc">MRML interaction node</a>, but it appears that the mouse modes are limited to: place, view transform, and select; these are not specific enough for my use case. Also, it appears that the <a href="https://apidocs.slicer.org/v4.8/classvtkMRMLFiducial.html" rel="noopener nofollow ugc">MRML fiducial node</a> can place markers from the script, but it doesn’t change the mouse mode itself.</p>
<p>Please forgive me if I am simply missing something obvious <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"></p>
<p>Thanks a lot for your help!</p>

---

## Post #2 by @smrolfe (2022-03-08 22:09 UTC)

<p>The Markups toolbar has <a href="https://github.com/Slicer/Slicer/blob/537cda915f1662b871be68575ef3a82814f4ddbe/Modules/Loadable/Markups/Widgets/qMRMLMarkupsToolBar.cxx#L82" rel="noopener nofollow ugc">three keyboard shortcuts</a> that interact with the mouse mode:</p>
<p>Create new markups node of current/default type: Ctrl+Shift+A<br>
Toggle Place Mode persistence: Ctrl+Shift+T<br>
Place point in active markup node: Ctrl+Shift+Space</p>
<p>You can change the interaction mode through Python by creating a new node with of the type you want (or make an existing node active) and using the place point callback to initiate placement in that node. For example:</p>
<pre><code class="lang-auto">slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsROINode')
slicer.modules.markups.toolBar().onPlacePointShortcut()
</code></pre>

---

## Post #3 by @jamesobutler (2022-03-08 22:14 UTC)

<p>You may be interested in <code>SetReferenceActivePlaceNodeClassName("vtkMRMLMarkupsLineNode")</code> as might be used below.</p>
<pre><code class="lang-python">selection_node = slicer.mrmlScene.GetNodeByID("vtkMRMLSelectionNodeSingleton")
interaction_node = slicer.mrmlScene.GetNodeByID("vtkMRMLInteractionNodeSingleton")

slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsLineNode")
selection_node.SetReferenceActivePlaceNodeClassName("vtkMRMLMarkupsLineNode")
interaction_node.SetCurrentInteractionMode(interaction_node.Place)
</code></pre>

---

## Post #4 by @lassoan (2022-03-09 07:00 UTC)

<p>One more tip: the easiest way to add a button that places a markup node is the markups place widget. See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#add-a-button-to-module-gui-to-activate-control-point-placement">complete example in the script repository</a>. There are several <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#switching-to-markups-control-point-placement-mode">more markups placement examples</a> in the script repository.</p>

---

## Post #5 by @vanlangk (2022-03-10 00:08 UTC)

<p>Thanks a lot guys! I’ll get back to implementing my extension <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
