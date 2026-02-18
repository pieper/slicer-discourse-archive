# Is there any callback for the mouse click when adding a new markup?

**Topic ID**: 25695
**Date**: 2022-10-14
**URL**: https://discourse.slicer.org/t/is-there-any-callback-for-the-mouse-click-when-adding-a-new-markup/25695

---

## Post #1 by @Eduardo_Fares (2022-10-14 00:09 UTC)

<p>Hello, I am developing a new application for 3D Slicer, however I cannot find a resolution to my problem. I am running a way to add control points via mouse click, the way I found in the repository script.</p>
<pre><code class="lang-python">selectionNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSelectionNodeSingleton")
selectionNode.SetReferenceActivePlaceNodeClassName("vtkMRMLMarkupsFiducialNode")
interactionNode = slicer.mrmlScene.GetNodeByID("vtkMRMLInteractionNodeSingleton")
placeModePersistence = 1
interactionNode.SetPlaceModePersistence(placeModePersistence)
# mode 1 is Place, can also be accessed via slicer.vtkMRMLInteractionNode().Place
interactionNode.SetCurrentInteractionMode(1)
</code></pre>
<p>Would it be possible to associate some callback for when a new control point is added?<br>
Thank you all for your attention.</p>

---

## Post #2 by @jamesobutler (2022-10-14 00:19 UTC)

<p>I think you’re looking for the PointPositionDefinedEvent. <code>slicer.vtkMRMLMarkupsNode.PointPositionDefinedEvent</code></p>
<p><a href="https://apidocs.slicer.org/main/classvtkMRMLMarkupsNode.html#aceeef8806df28e3807988c38510e56caaf1067cd7bcb1bd0992112b22daf219d5" class="onebox" target="_blank" rel="noopener nofollow ugc">https://apidocs.slicer.org/main/classvtkMRMLMarkupsNode.html#aceeef8806df28e3807988c38510e56caaf1067cd7bcb1bd0992112b22daf219d5</a></p>

---

## Post #3 by @Eduardo_Fares (2022-10-14 14:05 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="25695">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>slicer.vtkMRMLMarkupsNode.PointPositionDefinedEvent</p>
</blockquote>
</aside>
<p>It’s worked, thank you!!<br>
I made a new function:</p>
<pre><code class="lang-auto">def AddNewMarkup(self, caller, event):
        markupsNode = caller
        sliceView = markupsNode.GetAttribute("Markups.PointPositionDefinedEvent")
        movingMarkupIndex = markupsNode.GetDisplayNode().GetActiveControlPoint()
        addingMarkup = slicer.vtkMRMLMarkupsNode.PointAddedEvent 
        if addingMarkup &gt;= 0:
            newMarkup = f"fiducial_{movingMarkupIndex+1}"
            self.mMarkupid.addItem(newMarkup)
            self.mMarkupid.setCurrentIndex(movingMarkupIndex)
        else:
            self.interactionNode.SetCurrentInteractionMode(0)
</code></pre>
<p>and I call it by:<br>
<code>self.tnode.AddObserver(slicer.vtkMRMLMarkupsNode.PointPositionDefinedEvent, self.AddNewMarkup)</code></p>

---
