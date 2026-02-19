---
topic_id: 7348
title: "Select Vtkmrmlmodelnode On Mouse Click"
date: 2019-06-28
url: https://discourse.slicer.org/t/7348
---

# Select vtkMRMLModelNode on mouse click

**Topic ID**: 7348
**Date**: 2019-06-28
**URL**: https://discourse.slicer.org/t/select-vtkmrmlmodelnode-on-mouse-click/7348

---

## Post #1 by @zacbaum (2019-06-28 02:41 UTC)

<p>Hello,</p>
<p>I am trying to implement a mouse interaction wherein the user clicks on a model from the 3D viewer and the model which was clicked is made available so that it can be modified in some way (such as colour change, etc.). I was able to find a similar example <a href="https://lorensen.github.io/VTKExamples/site/Python/Interaction/HighlightPickedActor/" rel="nofollow noopener">here</a> from the VTK examples page but have not been able to reproduce the behaviour with vtkMRMLModelNodes within Slicer.</p>
<p>Any help is appreciated.</p>

---

## Post #2 by @lassoan (2019-06-28 23:07 UTC)

<p>We plan to add a feature like this within a couple of months, but until then you can use something like what is implemented <a href="https://github.com/Slicer/Slicer/commit/f1b55fc99e948629e8a048c619d685a25ac0ba4d" rel="nofollow noopener">here</a>.</p>

---

## Post #3 by @Saima (2023-06-01 03:12 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="7348">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>couple of months, but un</p>
</blockquote>
</aside>
<p>Hi Andras,<br>
Is the modelnode selection function available.</p>
<p>I have a model and selected nodes with using fiducials. Is there a way to left mouse click the fiducial and save that fiducial coordinates. For example if the user has model and selected nodes but the user needs the location of only few control points. is it possible to get the location by only left mouse click on the fiducial.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/febb331bb2f9d93128c07deac91ec11ea79506f1.png" data-download-href="/uploads/short-url/AlslKLAfxzQ9wwQwspI3RN9ODQt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/febb331bb2f9d93128c07deac91ec11ea79506f1.png" alt="image" data-base62-sha1="AlslKLAfxzQ9wwQwspI3RN9ODQt" width="189" height="500" data-dominant-color="584E2F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">200×529 35.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @cpinter (2023-06-01 12:05 UTC)

<p>This example could be a starting point:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-a-notification-if-a-markup-control-point-position-is-modified" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-a-notification-if-a-markup-control-point-position-is-modified</a></p>
<p>I’d probably try to use the <code>PointEndInteractionEvent</code> event to get notified about the click, and by getting the active control point index you know which one was clicked.</p>

---

## Post #5 by @Saima (2023-06-07 04:12 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="4" data-topic="7348">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>point index you know which one was clicked.</p>
</blockquote>
</aside>
<p>Hi,<br>
I am having trouble with connecting mouse click.</p>
<p>How can I attach the mouse click event with this method or may be I am understanding it wrong.</p>
<p>in main process code I have<br>
markupsNode = slicer.util.getNode(inputFiducial.GetID())<br>
print(markupsNode)<br>
markupsNode.AddObserver(slicer.vtkMRMLMarkupsNode.PointEndInteractionEvent, self.onMarkupEndInteraction)</p>
<p>and the method</p>
<p>def onMarkupEndInteraction(self, caller, event):<br>
markupsNode = caller<br>
sliceView = markupsNode.GetAttribute(“Markups.MovingInSliceView”)<br>
movingMarkupIndex = markupsNode.GetDisplayNode().GetActiveControlPoint()<br>
logging.info(“End interaction: point ID = {0}, slice view = {1}”.format(movingMarkupIndex, sliceView))</p>
<p>regards,<br>
saima</p>

---

## Post #6 by @cpinter (2023-06-07 09:45 UTC)

<p>You didn’t say anything about what the problem was, but from the code you pasted (which is identical to what we can see in the script repository) the problem I see is that you added an argument <code>self</code> to the <code>onMarkupEndInteraction</code> function, which won’t work outside of a class. Of course I can make assumptions all day but it would be easier if you told us what is the problem. Thanks.</p>

---

## Post #7 by @Saima (2023-06-13 01:35 UTC)

<aside class="quote no-group" data-username="Saima" data-post="5" data-topic="7348">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>aving trouble with connecting mouse c</p>
</blockquote>
</aside>
<p>Hi Pinter,<br>
I have the markup control points already defined for the model nodes. I want a program where user can click on the markup point and can get the node number along with the x,y,z coordinates.</p>
<p>regards,<br>
Saima</p>

---

## Post #8 by @Saima (2023-06-13 05:53 UTC)

<p>Hi,<br>
I got the control point I am clicking but why it is printing it multiple times. here are the lines of code.</p>
<p>In the main def process:<br>
markupsNode = slicer.util.getNode(inputFiducial.GetID())<br>
markupsNode.AddObserver(slicer.vtkMRMLMarkupsNode.PointEndInteractionEvent, self.onMarkupEndInteraction)</p>
<p>in the method within the class, def<br>
def onMarkupEndInteraction(self, caller, event):<br>
<span class="hashtag-raw">#print</span>(“inside”)<br>
markupsNode = caller<br>
sliceView = markupsNode.GetAttribute(“Markups.MovingInSliceView”)<br>
movingMarkupIndex = markupsNode.GetDisplayNode().GetActiveControlPoint()<br>
print(movingMarkupIndex)</p>
<h2><a name="p-96173-the-output-is-like-below-in-the-console-1" class="anchor" href="#p-96173-the-output-is-like-below-in-the-console-1" aria-label="Heading link"></a>the output is like below in the console.</h2>
<p>Reloading module: SurfaceModelNodesSelector</p>
<hr>
<p>inside</p>
<p>inside</p>
<p>inside</p>
<p>inside</p>
<p>inside</p>
<p>inside</p>
<p>2667</p>
<p>[-83.58309173583984, -56.84154510498047, 108.15825653076172]</p>
<p>2667</p>
<p>2667</p>
<p>2667</p>
<p>2667</p>
<p>2667</p>
<p>2667</p>

---

## Post #9 by @Saima (2023-06-15 02:09 UTC)

<p>Hi,<br>
I am getting the index and the control point position with the following lines.</p>
<p>def onMarkupEndInteraction(self, caller, event):<br>
markupsNode = caller<br>
markupsNodeindex = int(caller.GetAttribute(‘Markups.MovingMarkupIndex’))<br>
pos = [0,0,0]<br>
markupsNode.GetNthControlPointPosition(markupsNodeindex, pos)</p>
<p>I am having problem with the slicer everytime I reload the application is not reloading properly to show the changes in the code i have to restart the slicer every time i do changes in the code so that it reflects inside the slicer application.<br>
Any thing how i can fix this?</p>
<p>regards,<br>
saima</p>

---

## Post #10 by @cpinter (2023-06-15 14:04 UTC)

<p>If I understand correctly you successfully solved the problem in this topic. Correct?</p>
<p>Your next question is unrelated, but as a quick advice, you can use the <code>Reload</code> button on the top of your module UI, or add some code to your <code>.slicerrc.py</code> so that Slicer sets up your scene correctly before continuing with testing/development. If you have more questions about this please do a search in the forum first then open a new topic if you don’t find an answer.</p>

---

## Post #11 by @lassoan (2023-06-25 12:13 UTC)

<p>A post was split to a new topic: <a href="/t/select-locked-control-points-in-markuo/30221">Select locked control points in markuo</a></p>

---
