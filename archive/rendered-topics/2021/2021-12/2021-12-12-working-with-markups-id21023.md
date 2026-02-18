# Working with markups

**Topic ID**: 21023
**Date**: 2021-12-12
**URL**: https://discourse.slicer.org/t/working-with-markups/21023

---

## Post #1 by @keri (2021-12-12 01:18 UTC)

<p>Hi,</p>
<p>My understanding about markups is pretty limited and I don’t have much experience yet.</p>
<p>From C++ I need to visualize points of constant size regardless of the zoom.<br>
Probably it would be pretty nice if every point could have its name and multiple points are set in the list with the ability to add/delete points.<br>
Also the points must be undraggable by user (locked).</p>
<p>I think I could try to use markups especially <code>vtkMRMLMarkupsNode</code> with <code>LockedOn()</code> method enabled. I have made some attempts to avoid using <code>vtkMRMLMarkupsModuleLogic</code> and instead I linked to <code>vtkSlicerMarkupsModuleMRML</code>. The code that I used:</p>
<pre><code class="lang-cpp">  vtkNew&lt;vtkMRMLMarkupsNode&gt; mNode;
  mNode-&gt;SetCenterPosition(0, 0 0);
  mNode-&gt;LockedOn();

  this-&gt;GetMRMLScene()-&gt;AddNode(mNode);
  mNode-&gt;CreateDefaultDisplayNodes();
</code></pre>
<p>but the application has broken when I triggered this function.</p>
<p>Do I need to use markups logic instead? Or something like:</p>
<pre><code class="lang-cpp">vtkSmartPointr&lt;vtkMRMLMarkupsNode&gt; mNode = 
vtkMRMLMarkupsNode::SafeDownCast(
this-&gt;GetMRMLScene()-&gt;AddNewNodeByClass("vtkMRMLMarkupsNode"));
</code></pre>
<p>Appreciate for advice.</p>

---

## Post #2 by @keri (2021-12-14 02:46 UTC)

<p>To solve this problem I needed to use <code>vtkMRMLMarkupsFiducialNode</code> instead.</p>
<p>The class is pretty straightforward: each instance of that class stores points of type <code>vtkMRMLMarkupsNode::ControlPoint</code> wich is a struct with some fields like name, description, locked etc.<br>
One may add/remove points and there are events when point added or removed.</p>
<p>One nuance:<br>
is it possible to add event like <code>PointAboutToBeRemovedEvent</code>? When I use <code>PointRemovedEvent</code> I get index of a point that is already deleted so I cannot retrieve insformation about deleted point (like name or description).<br>
I can’t say that I’m stuck with that as when I’was struggling with markups my logic used to poor and now I have found a better solution for my use case that doesn’t involve using markups events. But probably in the future this <code>PointAboutToBeRemovedEvent</code> will help me.</p>

---

## Post #3 by @pieper (2021-12-14 18:25 UTC)

<aside class="quote no-group" data-username="keri" data-post="2" data-topic="21023">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>But probably in the future this <code>PointAboutToBeRemovedEvent</code> will help me.</p>
</blockquote>
</aside>
<p>That sounds like a reasonable event to add.  If you want to make a PR we can review.</p>

---

## Post #4 by @keri (2021-12-18 00:22 UTC)

<p><a href="https://github.com/Slicer/Slicer/pull/6085" rel="noopener nofollow ugc">Added the PR</a></p>

---
