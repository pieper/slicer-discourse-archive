---
topic_id: 13158
title: "Vtkmrmlannotationroinode Instantiation Before Changing Inter"
date: 2020-08-25
url: https://discourse.slicer.org/t/13158
---

# vtkMRMLAnnotationROINode instantiation before changing Interaction Mode

**Topic ID**: 13158
**Date**: 2020-08-25
**URL**: https://discourse.slicer.org/t/vtkmrmlannotationroinode-instantiation-before-changing-interaction-mode/13158

---

## Post #1 by @EricM (2020-08-25 16:12 UTC)

<p>Hi Slicer Community,</p>
<p>I apologize in advance if the answer to my question is out there. I’ve seen related threads, but I haven’t been able to piece it together to get my solution working.</p>
<p>Basically, I would like to instantiate a <code>vtkMRMLAnnotationROINode</code> <em>before</em> having the user switch Interaction Modes (to Place mode) in order to change certain properties of the AnnotationROINode, such as the Name etc. so that the user doesn’t see the default names (like R, R_1, R_2), etc.</p>
<p>Basically, I have created a button <code>addBoundingBoxButton</code> which is connected to a function <code>onAddBoundingBox</code>, which I would like to do the following:</p>
<pre><code class="lang-auto">def onAddBoundingBox(self):

  boundingBoxName = 'Finding {}'.format(self.findingCounter) #internal counter for number of findings identified

  #add vtkMRMLAnnotationROINode and change name
  annotationROINode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLAnnotationROINode',boundingBoxName)

  slicer.mrmlScene.GetNodeByID("vtkMRMLSelectionNodeSingleton").SetReferenceActivePlaceNodeClassName("vtkMRMLAnnotationROINode")
  slicer.mrmlScene.GetNodeByID("vtkMRMLInteractionNodeSingleton").SetCurrentInteractionMode(1)
  
</code></pre>
<p>The problem is that the <code>annotationROINode</code> object is not the one modified when the InteractionNode is changed to Place mode, and when the <code>vtkMRMLAnnotationROINode</code> is placed, a new object is created with a default name. Weirdly, when I do this same approach with <code>vtkMRMLMarkupsLineNode</code>, I get the desired behavior (i.e., I can create the <code>vtkMRMLMarkupsLineNode</code> beforehand and the InteractionNode lets me place the line that I have already created in my script). Perhaps this behavior is because of some inherent differences in the Annotations vs the Markups modules? Is there a way to link the <code>annotationROINode</code> object I’ve created to the one that will be created in Place mode?</p>
<p>Another method I was thinking of was creating the <code>vtkMRMLAnnotationROINode</code> and then using two fiducial points to let the user choose the center and radius of the bounding box (I suspect this is how it is done in practice, but I couldn’t find a clear procedure for this in the source code, and I would like to take advantage of this being implemented in Place mode through the Interaction Node). I have looked at other threads like <a href="https://discourse.slicer.org/t/how-to-get-input-value-from-mouse-click/5903/10">this one</a> and <a href="https://discourse.slicer.org/t/capturing-mouse-input/789">this one</a>, but it’s not clear to me how to create a button with a connecting function that (1) lets me place two fiducial points, (2) waits for the user to place them, (3) then extracts the Control Points, and (4) creates/modifies the <code>vtkMRMLAnnotationROINode</code> with the desired properties. It seems that when I put all of these functions in a connector function, it runs to the very end of the function without waiting for the fiducial points to be placed, so obviously this produces errors downstream.</p>
<p>One last thing I will say is that I am aware that the AnotationROI nodes will be moved to the Markups module sometime in the near future, but I unfortunately can’t wait that long (although, I’m excited for it!).</p>
<p>Thanks for any guidance or help,<br>
Eric</p>

---

## Post #2 by @EricM (2020-08-26 12:17 UTC)

<p>Hello Community,</p>
<p>Thanks to a great tip by <a class="mention" href="/u/fernando">@Fernando</a>, who suggested to connect the event with a function that listens and does something if there are two fiducials in the markups node, I was able to figure out how to place a <code>vtkMRMLAnnotationROINode</code> with two Fiducial Points.</p>
<p>I still have some follow-up questions (see below), so I would appreciate any help on those, but otherwise, here is some working code:</p>
<pre><code class="lang-auto">import numpy as np

def onFiducialPlaced(caller, event):
    numberOfFiducials = caller.GetNumberOfFiducials()
    if numberOfFiducials != 2:
        print("Not yet 2")
        return
    #turn off fiducial placement
    slicer.mrmlScene.GetNodeByID("vtkMRMLInteractionNodeSingleton").SetCurrentInteractionMode(2)
    fiducialWorldCoordinatesDict = {}
    for n in range(numberOfFiducials):
      p = [0,0,0,1]
      caller.GetNthFiducialWorldCoordinates(n,p)
      fiducialWorldCoordinatesDict[n] = p
      print("Fiducial Point {}: {}".format(n+1,p))
    #Get XYZ and RadiusXYZ
    XYZ = np.array(fiducialWorldCoordinatesDict[0])[:3] #only take x,y,z
    R = np.array(fiducialWorldCoordinatesDict[1])[:3] #only take x,y,z
    dx,dy,_ = np.abs(XYZ-R)
    #Create annotationROINode and set location
    annotationROINode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLAnnotationROINode',caller.GetName())
    annotationROINode.SetXYZ(XYZ)
    annotationROINode.SetRadiusXYZ(dx,dy,10) #fix radius in z direction to 10
    #delete markups
    caller.RemoveAllMarkups()

def onAddBoundingBox():
    fiducialList = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode",'MyNode')
    tag = fiducialList.AddObserver(slicer.vtkMRMLMarkupsNode.PointPositionDefinedEvent, lambda caller, event: onFiducialPlaced(caller,event))
    placeWidget = slicer.qSlicerMarkupsPlaceWidget()
    placeWidget.setMRMLScene(slicer.mrmlScene)
    placeWidget.setCurrentNode(fiducialList)
    placeWidget.setPlaceMultipleMarkups(placeWidget.ForcePlaceMultipleMarkups)
    placeWidget.placeButton().click()

addBoundingBoxButton = qt.QPushButton('Add')
addBoundingBoxButton.clicked.connect(onAddBoundingBox)
addBoundingBoxButton.show()
</code></pre>
<p>Question 1: I would have expected that <code>slicer.vtkMRMLMarkupsNode.PointEndInteractionEvent</code> would have been the event for dropping the Fiducial point the first time (with the way my code is written), yet this signal is only emitted after picking it back up and dropping it (i.e., it is only emitted if you pick up the fiducial point, drag it, and drop it a second, third, etc. time). The code seems to do exactly what I want with <code>slicer.vtkMRMLMarkupsNode.PointPositionDefinedEvent</code>, so I’m not complaining, but any insights would make me feel a bit more comfortable.</p>
<p>Question 2: Is there a way to specify <em>a priori</em> how many Markups can be added to a MarkupsFiducialNode whn using <code>placeWidget.setPlaceMultipleMarkups(placeWidget.ForcePlaceMultipleMarkups)</code>? For a bounding box, I just need two, so I have an if loop in <code>onFiducialPlaced</code> to check how many Fiducials are part of the node, and once I’m satisfied, I change the InteractionMode to 2 to get out of Place mode. However, this seems quite “hacky”. Is there a better way to do this?</p>
<p>Hope this can help the general Slicer community,<br>
Eric M</p>

---

## Post #3 by @lassoan (2020-08-26 14:57 UTC)

<aside class="quote no-group" data-username="EricM" data-post="2" data-topic="13158">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/48db29/48.png" class="avatar"> EricM:</div>
<blockquote>
<p>Question 1: I would have expected that <code>slicer.vtkMRMLMarkupsNode.PointEndInteractionEvent</code> would have been the event for dropping the Fiducial point the first time (with the way my code is written), yet this signal is only emitted after picking it back up and dropping</p>
</blockquote>
</aside>
<p>The event is exactly for this purpose. For example, can be used for performing operations that you don’t want to do continuously, but when the user finished interaction with the control point.</p>
<aside class="quote no-group" data-username="EricM" data-post="2" data-topic="13158">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/48db29/48.png" class="avatar"> EricM:</div>
<blockquote>
<p>Is there a way to specify <em>a priori</em> how many Markups can be added to a MarkupsFiducialNode whn using <code>placeWidget.setPlaceMultipleMarkups(placeWidget.ForcePlaceMultipleMarkups)</code> ?</p>
</blockquote>
</aside>
<p>Yes, you can use <code>SetMaximumNumberOfControlPoints</code> to set the expected number of points. If that number is reached then placement is finished. We will tune/optimize the behavior, including predefine name of markups (<a class="mention" href="/u/muratmaga">@muratmaga</a>’s team is working on this).</p>
<p>Also note that <a href="https://github.com/Slicer/Slicer/issues/5061">@Sunderlandkyl is working on adding a markups ROI</a>, which would be a much improved version of Annotation ROI (and annotation module will be deprecated).</p>

---

## Post #4 by @EricM (2020-08-27 07:39 UTC)

<p>Hi Iassoan,</p>
<p>Thanks for the answer.</p>
<p>Regarding, my second question, I modified <code>onAddBoundingBox</code> as below and commented out the line where I add an observer just to see if Slicer goes out of Place mode after the second control point.</p>
<pre><code class="lang-auto">def onAddBoundingBox():
    fiducialList = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode",'MyNode')
    fiducialList.SetMaximumNumberOfControlPoints(2)
    #tag = fiducialList.AddObserver(slicer.vtkMRMLMarkupsNode.PointPositionDefinedEvent, lambda caller, event: onFiducialPlaced(caller,event))
    placeWidget = slicer.qSlicerMarkupsPlaceWidget()
    placeWidget.setMRMLScene(slicer.mrmlScene)
    placeWidget.setCurrentNode(fiducialList)
    placeWidget.setPlaceMultipleMarkups(placeWidget.ForcePlaceMultipleMarkups)
    placeWidget.placeButton().click()
</code></pre>
<p>But after clicking the <code>placeButton</code>, it just keeps letting me add more fiducial points (‘MyNode’, ‘F’,‘F_1’,‘F_2’, etc.). I tried this with <code>placeWidget.ForcePlaceSingleMarkup</code>, but it stops after the first Control Point. I imagine that I coded this incorrectly. In any case, my “hack” is working for now.</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="13158">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Also note that <a href="https://github.com/Slicer/Slicer/issues/5061" rel="noopener nofollow ugc">@Sunderlandkyl is working on adding a markups ROI</a>, which would be a much improved version of Annotation ROI (and annotation module will be deprecated).</p>
</blockquote>
</aside>
<p>I’m really looking forward to the new and improved markups ROI!</p>
<p>Thanks again,<br>
Eric</p>

---
