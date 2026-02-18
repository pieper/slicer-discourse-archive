# Markup notification

**Topic ID**: 7541
**Date**: 2019-07-11
**URL**: https://discourse.slicer.org/t/markup-notification/7541

---

## Post #1 by @gcsharp (2019-07-11 22:11 UTC)

<p>Hi, I am testing out the repository script “Get a notification if a markup point position is modified”.   It is working (stuff being printed in python console) in Slicer 4.10.1, but I am getting no notifications in the version I just compiled early this week.  Any idea what is going on?</p>
<p>Below is the script.</p>
<pre><code>def onMarkupsNodeModified(markupsNode, unusedArg2=None, unusedArg3=None):
  sliceView = markupsNode.GetAttribute('Markups.MovingInSliceView')
  if not sliceView:
    print("Markup list was modified")
    return
  movingMarkupIndex = markupsNode.GetAttribute('Markups.MovingMarkupIndex')
  pos = [0,0,0]
  markupsNode.GetNthFiducialPosition(int(movingMarkupIndex), pos)  
  print("Markup {0} was moved in slice view {1} to {2}".format(movingMarkupIndex, sliceView, pos))

markupsNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")
markupsNode.CreateDefaultDisplayNodes()
markupsNode.AddFiducial(0,0,0)
markupsNode.AddObserver(vtk.vtkCommand.ModifiedEvent, onMarkupsNodeModified)</code></pre>

---

## Post #2 by @jamesobutler (2019-07-11 22:23 UTC)

<p>I see that the wiki ScriptRepository might have some outdated examples as you are referring to.<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_a_notification_if_a_markup_point_position_is_modified" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_a_notification_if_a_markup_point_position_is_modified</a><br>
<a class="mention" href="/u/lassoan">@lassoan</a> Do you mind updating these examples for the nightly documentation wiki pages?</p>
<p>Markups has changed a good bit in the Slicer nightly. I would suggest reading the markups section of the migration guide which details some changes about markup events. <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Markups" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Markups</a></p>
<p>Another discussion about recent changes to Markups events can be found at:<br>
<a href="https://discourse.slicer.org/t/handle-markups-events-from-an-external-module/6332" class="inline-onebox">Handle Markups events from an external module</a></p>

---

## Post #3 by @gcsharp (2019-07-11 22:29 UTC)

<p>Very informative links.  Thanks!</p>

---

## Post #4 by @lassoan (2019-07-12 14:24 UTC)

<p>I’ve updated the markups observation examples in the script repository according to the changed API.</p>

---

## Post #5 by @timeanddoctor (2019-12-15 13:29 UTC)

<p>There is still a problem  for me that when I add the marksup in a transform, and this seems naver change unless ‘harden’ the transform.<br>
So, is there any method to find wheater a marksup was in a transform already?</p>

---

## Post #6 by @lassoan (2019-12-15 14:10 UTC)

<p>If you want to get notification about transform changes, you can observe vtkMRMLTransformableNode::TransformModifiedEvent.</p>
<p>For performance reasons, it is important to be able to observe point coordinates changes from node transform changes, but if we find that observing two events instead of only one puts unreasonable burden on developers then we can add a new “PointModifiedWorld” event.</p>

---
