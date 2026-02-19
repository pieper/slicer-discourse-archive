---
topic_id: 26045
title: "How To Disable Double Click When Placing Markups"
date: 2022-11-03
url: https://discourse.slicer.org/t/26045
---

# How to disable double click when placing markups

**Topic ID**: 26045
**Date**: 2022-11-03
**URL**: https://discourse.slicer.org/t/how-to-disable-double-click-when-placing-markups/26045

---

## Post #1 by @nnzzll (2022-11-03 09:01 UTC)

<p>When placing markups consistently (check the <code>Place multiple control points</code> button), if I double clicked then it will terminate the place process. How can I avoid it?</p>

---

## Post #2 by @muratmaga (2022-11-03 10:31 UTC)

<aside class="quote no-group" data-username="nnzzll" data-post="1" data-topic="26045">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nnzzll/48/16350_2.png" class="avatar"> nnzzll:</div>
<blockquote>
<p>if I double clicked then it will terminate the place process. How can I avoid it?</p>
</blockquote>
</aside>
<p>Why do you need to double-click? Just curious?</p>

---

## Post #3 by @nnzzll (2022-11-03 11:08 UTC)

<p>In fact I don’t need double-click but sometimes you may just do it accidentally, and that is how I find this problem.</p>

---

## Post #4 by @muratmaga (2022-11-03 11:18 UTC)

<p>There needs to be a function to stop the placement so that, for example you can reorient your object in 3D view to get the new ones. That’s normally the right-click. I never tried double-click before, but I can confirm that it does indeed stop the placement mode. I don’t know whether its intentional, so I included <a class="mention" href="/u/smrolfe">@smrolfe</a> <a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<p>As for re-activating the placement mode, whether you stopped accidentally or intentionally, can be done via a quick keyboard shortcut CTRL+SHIFT+SPACE. See the documentation for <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html#keyboard-shortcuts" rel="noopener nofollow ugc">Markups keyboard shortcuts here</a></p>
<p>You can also define your own (provided that it does not conflict with already existing ones).</p>

---

## Post #5 by @jamesobutler (2022-11-03 19:50 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="26045">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I never tried double-click before, but I can confirm that it does indeed stop the placement mode. I don’t know whether its intentional, so I included</p>
</blockquote>
</aside>
<p>Yes, in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html#place-new-markups" rel="noopener nofollow ugc">Markups module documentation</a>:</p>
<blockquote>
<ol start="2">
<li>Left-click in a slice view or 3D view to place points.</li>
<li>Double-left-click or right-click to finish point placement.</li>
</ol>
</blockquote>
<p>Double-left-click is a thing as I believe it is a standard thing for ending for example a closed curve group of points.</p>

---

## Post #6 by @nnzzll (2022-11-04 01:31 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> Thanks for the reply.</p>
<p>Since it is designed intentionally, I decided not to deal with it and found another way to solve my problem.</p>
<p>The solution goes like:</p>
<pre><code class="lang-auto">qvtkConnect(interactionNode, vtkMRMLInteractionNode::EndPlacementEvent, this,
                 SLOT(onEndPlacement()));
</code></pre>
<p>and in the slot function make a judgement when to reactive the placement mode.</p>
<pre><code class="lang-auto">void XXX::onEndPlacement()
{
  auto scene = qSlicerApplication::application()-&gt;mrmlScene();
  auto interactionNode = vtkMRMLInteractionNode::SafeDownCast(
      scene-&gt;GetNodeByID("vtkMRMLInteractionNodeSingleton"));
  auto selectionNode = vtkMRMLSelectionNode::SafeDownCast(
      scene-&gt;GetNodeByID("vtkMRMLSelectionNodeSingleton"));
  auto nodeID = selectionNode-&gt;GetActivePlaceNodeID();
  auto node = vtkMRMLMarkupsFiducialNode::SafeDownCast(scene-&gt;GetNodeByID(nodeID));
  if (Judgement about the MarkupsNode)
  {
    interactionNode-&gt;SetCurrentInteractionMode(vtkMRMLInteractionNode::Place);
  }
}
</code></pre>

---

## Post #7 by @lassoan (2022-11-07 18:58 UTC)

<p>Maybe it is a bit simpler if you customize the event mappings as shown in examples the script repository: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-keyboard-mouse-gestures-in-viewers">[1]</a> and <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#assign-custom-actions-to-markups">[2]</a></p>
<p>For example, you can remove the double-click shortcut in the first 3D view like this:</p>
<pre><code class="lang-python">threeDViewWidget = slicer.app.layoutManager().threeDWidget(0)
markupsDisplayableManager = threeDViewWidget.threeDView().displayableManagerByClassName('vtkMRMLMarkupsDisplayableManager')
markupsDisplayNodes = slicer.util.getNodesByClass("vtkMRMLMarkupsDisplayNode")
for markupsDisplayNode in markupsDisplayNodes:
  markupsWidget = markupsDisplayableManager.GetWidget(markupsDisplayNode)
  markupsWidget.SetEventTranslation(markupsWidget.WidgetStateDefine, vtk.vtkCommand.LeftButtonDoubleClickEvent, vtk.vtkEvent.NoModifier, vtk.vtkWidgetEvent.NoEvent)
</code></pre>
<p>Similarly, you can remove double-click event processing in the camera widget to prevent double-click from maximizing/restoring the current view.</p>

---
