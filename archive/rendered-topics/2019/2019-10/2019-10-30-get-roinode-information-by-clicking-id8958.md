---
topic_id: 8958
title: "Get Roinode Information By Clicking"
date: 2019-10-30
url: https://discourse.slicer.org/t/8958
---

# Get ROINode Information by clicking

**Topic ID**: 8958
**Date**: 2019-10-30
**URL**: https://discourse.slicer.org/t/get-roinode-information-by-clicking/8958

---

## Post #1 by @CreepyTrick (2019-10-30 11:02 UTC)

<p>Hello,</p>
<p>I’m trying to get the all information about a drawed ROINode on the slice view:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e10c620ffb840dd59911386d8c4a0ff693babaf3.png" data-download-href="/uploads/short-url/w6RXBIXMN2t24cj8sevlHSirEPN.png?dl=1" title="Capture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e10c620ffb840dd59911386d8c4a0ff693babaf3_2_690x347.png" alt="Capture1" data-base62-sha1="w6RXBIXMN2t24cj8sevlHSirEPN" width="690" height="347" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e10c620ffb840dd59911386d8c4a0ff693babaf3_2_690x347.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e10c620ffb840dd59911386d8c4a0ff693babaf3_2_1035x520.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e10c620ffb840dd59911386d8c4a0ff693babaf3_2_1380x694.png 2x" data-dominant-color="54546D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture1</span><span class="informations">1509×761 20.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The goal is the following: I want to click on a white square to get all the ROINode informations / properties (coordinates for exemple).</p>
<p>I already search a lot, step by step, by trying to detect a ModifiedEvent on a non-locked node, but the only event i can get is when i move the square, witch is problematic when i want to manipulate a locked Node by clicking on it … i had this with</p>
<pre><code class="lang-auto">sliceNode.AddObserver(vtk.vtkCommand.ModifiedEvent, aFunc)
</code></pre>
<p>I trying with “AnyEvent” for tests, but the only two event detected is NoEvent and ModifiedEvent</p>
<p>Does anyone has a solution ?</p>

---

## Post #2 by @lassoan (2019-10-30 15:43 UTC)

<p>You can observe click events on markups (in recent preview releases). You can use those markups to draw ROIs (box-shaped model nodes). We plan to improve markups module to manage ROIs and then you’ll be able to get notifications about clicks, but you need to wait about 6-12 months (or help us implementing it).</p>

---

## Post #3 by @CreepyTrick (2019-10-31 10:33 UTC)

<p>So you suggest i should draw a lines between all my markups in order to have my ROI ? If yes, how ?</p>
<p>( for the click event i found that, i just put it here if someone need:</p>
<pre><code class="lang-auto">    slicer.util.mainWindow().moduleSelector().selectModule('Markups')
    slicer.modules.markups.logic().AddFiducial(5,5,5)
    
    fidNode = slicer.util.getNode("vtkMRMLMarkupsFiducialNode1")
    fidNode.AddObserver(slicer.vtkMRMLMarkupsNode.PointClickedEvent ,aFunction)
</code></pre>
<p>Thanks for the tips<br>
)</p>

---

## Post #4 by @lassoan (2019-10-31 11:12 UTC)

<p>If you want to create a box then you can create a VTK source for that and then create a model node. You can show box boundaries in slice view by enabling slice view intersections (2D visibility). See example in the script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer</a></p>

---

## Post #5 by @CreepyTrick (2019-10-31 14:44 UTC)

<p>Okay, i found a way with Markups and vtkMRMLModelDisplayNode to get something like this: (the square can move with the point)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85a4f05d1dc2e91c7819f0c4c8117093673030fc.png" data-download-href="/uploads/short-url/j4gSMtlgXQnGtGEyZXbqDL56ajW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85a4f05d1dc2e91c7819f0c4c8117093673030fc_2_652x500.png" alt="image" data-base62-sha1="j4gSMtlgXQnGtGEyZXbqDL56ajW" width="652" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85a4f05d1dc2e91c7819f0c4c8117093673030fc_2_652x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85a4f05d1dc2e91c7819f0c4c8117093673030fc_2_978x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85a4f05d1dc2e91c7819f0c4c8117093673030fc.png 2x" data-dominant-color="314D48"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">994×762 11.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But when i changed my markup with <code>SetLocked(1)</code> (to avoid movement of the markup) i cannot trigger a PointClickedEvent… (cant even click on the markup)</p>
<p>So i tried to change the color to transparent but i cannot find any method to manipulate the markup color… even try <code>SetDisplayVisibility(0)</code> , same conclusion, cannot select the point, even with a <code>SetSelectable(1)</code> after theses line…<br>
Any solution ?</p>

---

## Post #6 by @lassoan (2019-10-31 15:01 UTC)

<p>If you want to prevent moving the point but you still want to click on it then don’t lock the entire markups node but lock each control point.</p>

---

## Post #7 by @CreepyTrick (2019-11-04 09:26 UTC)

<p>Okay, but now i got a problem with code logic …<br>
I tried to apply your solution via<br>
<code>markup.GetControlPoints()</code> but the debugger say there are no function with this say, BUT i saw it on the Doxygen…<br>
I try something like</p>
<pre><code class="lang-auto">e = slicer.vtkMRMLMarkupsNode()
print(type(e))
print(e.GetControlPoints())
</code></pre>
<p>I get</p>
<pre><code class="lang-auto">&lt;type 'vtkSlicerMarkupsModuleMRMLPython.vtkMRMLMarkupsNode'&gt;
</code></pre>
<p>and<br>
<code>"no attribute found for "GetControlPoint"</code><br>
I Try to workaround with other functions but none function related with control points work…</p>
<p>I’m working with python and slicer 4.10.2, i tried with the upper version without success</p>
<p>I dont know what is wrong ….</p>

---

## Post #8 by @lassoan (2019-11-04 12:05 UTC)

<p>Some widgets (ROI, ruler) are managed by the old Annotation module. Others (points, line, angle, curve, closed curve) by Markups module. The plan is to remove Annotations module when Markups module reaches feature parity, but we don’t have ROIs in Markups module yet.</p>
<p>You can enter <code>help(someNode)</code> to get API documentation or google <code>vtkMRMLAnnotationROINode</code>.</p>

---

## Post #9 by @CreepyTrick (2019-11-04 15:27 UTC)

<p>I found the answer …<br>
The code allow us to pick a square in the red yellow green view, and also get it’s information (without markup,</p>
<p>Here the code:</p>
<pre><code class="lang-auto">#We create a Model Node. In my case, he has a polydataConnection with a source vtk cube
self.model_node = slicer.mrmlScene.CreateNodeByClass('vtkMRMLModelNode')
slicer.mrmlScene.AddNode(self.model_node)

#Bind between VTK cube and our model node
self.model_node.SetPolyDataConnection(self.cube_source.GetOutputPort())
    
# . Create model display node
self.model_display_node = slicer.mrmlScene.CreateNodeByClass('vtkMRMLModelDisplayNode')
slicer.mrmlScene.AddNode(self.model_display_node)

self.model_node.SetAndObserveDisplayNodeID(self.model_display_node.GetID())
self.model_display_node.SetColor(0.0,1.0, 0.0) # green color
self.model_display_node.SetSliceDisplayModeToIntersection()

 # . Visibility
 self.model_display_node.SetSliceIntersectionVisibility(1)

#Get the RAS bound of our Model Node
self.tabRas = [0.0,0.0,0.0,0.0,0.0,0.0]
self.model_node.GetRASBounds(self.tabRas)

#We get The Red view (and the other if we want) and we put a observer to trigger a function if the observer detect a left click
interactorRed =slicer.app.layoutManager().sliceWidget('Red').sliceView().interactor()
self.crosshairNode=slicer.util.getNode('Crosshair') 
interactorRed.AddObserver(vtk.vtkCommand.LeftButtonPressEvent , self.SelectCube)

#This function compare the RAS Coordinate of cube's bound and our click, to detect if we click inside the cube on a RGY view:
 def SelectCube(self,caller,event):
      ras=[0,0,0]
      self.crosshairNode.GetCursorPositionRAS(ras)
      print(ras)
      if (ras[0]&gt;self.tabRas[0] and ras[0]&lt;self.tabRas[1]) and (ras[1]&gt;self.tabRas[2] and ras[1]&lt;self.tabRas[3]) and (ras[2]&gt;self.tabRas[4] and ras[2]&lt;self.tabRas[5]):
          self.model_display_node.SetColor(0.0,1.0,0.0) #Green Color if selected
      else:
          self.model_display_node.SetColor(1.0,0.0,0.0) #Red Color if deselected
</code></pre>
<p>Hope it help somebody <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
Thanks for your help &amp; your time lassoan</p>

---
