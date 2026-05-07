---
topic_id: 46937
title: "How To Get The Clicked Markup Node In The 3D View"
date: 2026-05-06
url: https://discourse.slicer.org/t/46937
---

# How to get the clicked markup node in the 3D view?

**Topic ID**: 46937
**Date**: 2026-05-06
**URL**: https://discourse.slicer.org/t/how-to-get-the-clicked-markup-node-in-the-3d-view/46937

---

## Post #1 by @NogginBops (2026-05-06 14:34 UTC)

<p>Hi,</p>
<p>I’m interested in knowing what node is selected/hovered by the mouse when the left mouse button is pressed.<br>
I’ve tried using the scene interactor and trying to use the vtk picker, but I’m not really able to get it to work.<br>
I’ve also tried adding observers to my markup objects in the hope that they would receive the left mouse button event, but instead the display node receives NoEvent when I press the left mouse button which is not very useful.</p>
<p>So I’m wondering, how do I get the node that was clicked on in the 3D view. I know it must be possible as Slicer is able to highlight the markup object when the mouse is hovered over them, but I can’t really find the code that does that.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @pieper (2026-05-06 17:01 UTC)

<p>Here’s what I got from <a href="https://discourse.slicer.org/t/new-slicer-skill-ai-tool/46243">the slicer-skill</a>.</p>
<blockquote>
<p><img src="https://emoji.discourse-cdn.com/twitter/robot.png?v=15" title=":robot:" class="emoji" alt=":robot:" loading="lazy" width="20" height="20"> This post contains AI-generated content.</p>
</blockquote>
<p>Here’s a reply you can post to the forum:</p>
<hr>
<p>The piece you’re missing is that Slicer’s 3D view doesn’t really hand raw mouse events to MRML nodes — it routes them through <em>displayable managers</em>, which is also why your observers on the display nodes never see anything useful. The good news is that the model displayable manager already exposes the picker you want, and there’s an official snippet for it in the Script Repository under “Get 3D coordinates from 2D display coordinates” (<a>gui.md</a>).</p>
<p>Wire it up to the 3D view’s interactor and you get the clicked node directly:</p>
<pre><code class="lang-auto">import slicer, qt, vtk

threeDView = slicer.app.layoutManager().threeDWidget(0).threeDView()
viewNode = threeDView.mrmlViewNode()
modelDM = slicer.app.applicationLogic().GetViewDisplayableManagerByClassName(
    viewNode, "vtkMRMLModelDisplayableManager")

def onLeftClick(caller, event):
    x, y = caller.GetEventPosition()
    # VTK's y is bottom-up; the displayable manager's Pick expects that, so no flip needed.
    if modelDM.Pick(x, y) and modelDM.GetPickedNodeID():
        nodeID = modelDM.GetPickedNodeID()  # this is the *display* node ID
        displayNode = slicer.mrmlScene.GetNodeByID(nodeID)
        dataNode = displayNode.GetDisplayableNode() if displayNode else None
        ras = modelDM.GetPickedRAS()
        cellID = modelDM.GetPickedCellID()
        print(f"Clicked {dataNode.GetName() if dataNode else '(none)'} "
              f"at RAS={tuple(ras)} cell={cellID}")

interactor = threeDView.interactor()
tag = interactor.AddObserver(vtk.vtkCommand.LeftButtonPressEvent, onLeftClick, 0.0)
# To remove later: interactor.RemoveObserver(tag)
</code></pre>
<p>A couple of gotchas that probably bit you:</p>
<ul>
<li><code>GetPickedNodeID()</code> returns the <strong>display node ID</strong>, not the data node ID. Call <code>GetDisplayableNode()</code> on it to get the model/markup/segmentation node.</li>
<li>A priority of <code>0.0</code> (or negative) means you observe <em>after</em> the standard interactor style, so you don’t break camera rotation. If you want to suppress default behavior on a hit, raise the priority and call <code>caller.AbortFlagOn()</code>.</li>
<li><code>vtkMRMLModelDisplayableManager.Pick()</code> only finds things rendered as polydata (models, segmentation surfaces, markup glyphs). Volume rendering and slice planes need different displayable managers.</li>
</ul>
<p>For <strong>hover</strong> (highlight as the cursor moves), swap <code>LeftButtonPressEvent</code> for <code>vtk.vtkCommand.MouseMoveEvent</code>. Be sure to throttle — <code>Pick()</code> on every move event in a heavy scene will hurt FPS; a <code>qt.QTimer</code> with <code>setSingleShot(True)</code> reset on each move is the usual trick.</p>
<p>If you also need this for markups specifically (control-point hover highlight), that’s done inside <code>vtkMRMLMarkupsDisplayableManager</code> via the <code>CanProcessInteractionEvent</code> / <code>ProcessInteractionEvent</code> API on <code>vtkMRMLAbstractDisplayableManager</code> — it’s the modern path for writing a custom interaction, but for “what node did the user click?” the snippet above is the simplest answer.</p>

---
