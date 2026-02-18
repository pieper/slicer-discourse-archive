# How to access Node in Scene?

**Topic ID**: 27197
**Date**: 2023-01-12
**URL**: https://discourse.slicer.org/t/how-to-access-node-in-scene/27197

---

## Post #1 by @dsa934 (2023-01-12 02:16 UTC)

<p>Operating system: window 11<br>
Slicer version: 4.13.0</p>
<p>Hi , Slicer users</p>
<p>I’m implementing an extension that draws a depthmap in slicer through a python module.<br>
Depthmap is almost done, but there is a problem in considering convenience.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d428a422d021554e0cdc6b1dba31965df293acb.png" alt="Question" data-base62-sha1="dj0XU4iwrC76eSqfr0uNNLtkrhN" width="535" height="230"></p>
<p>Q1. How do I access nodes belonging to a Scene? ( not getNode(‘F’) )</p>
<p>=&gt; Whenever markups are added, I would like to obtain a list of markups and extract them<br>
in the form of stack.pop() rather than importing getNode(‘F_1’) or getNode(‘F_2’) individually.</p>
<p>Q2. When deleting markup, why isn’t it completely deleted?</p>
<p>=&gt; If you delete the F-3 markup, when you take a new markup,<br>
it should be named F-3, but why does it become f-4?</p>
<p>As a result, I want to handle nodes internally to increase the usability of the function that draws the depthmap(I made), So that I want to know about the functions that can be involved in their insertion and deletion.</p>

---

## Post #2 by @RafaelPalomar (2023-01-12 08:46 UTC)

<aside class="quote no-group" data-username="dsa934" data-post="1" data-topic="27197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar"> dsa934:</div>
<blockquote>
<p>Q1. How do I access nodes belonging to a Scene? ( not getNode(‘F’) )</p>
<p>=&gt; Whenever markups are added, I would like to obtain a list of markups and extract them<br>
in the form of stack.pop() rather than importing getNode(‘F_1’) or getNode(‘F_2’) individually.</p>
</blockquote>
</aside>
<p>You can observe events and use callbacks to react to these events. A simple example could be something like this (from <a href="https://www.slicer.org/wiki/Documentation/4.10/Developers/FAQ/Python_Scripting#How_can_I_access_callData_argument_in_a_VTK_object_observer_callback_function" class="inline-onebox" rel="noopener nofollow ugc">Documentation/4.10/Developers/FAQ/Python Scripting - Slicer Wiki</a>):</p>
<pre data-code-wrap="python"><code class="lang-python">@vtk.calldata_type(vtk.VTK_OBJECT)
def nodeAddedCallback(caller, eventId, callData):
  print("Node added")
  print("New node: {0}".format(callData.GetName()))

nodeAddedModifiedObserverTag = slicer.mrmlScene.AddObserver(slicer.vtkMRMLScene.NodeAddedEvent, nodeAddedCallback)
</code></pre>
<p>You can test this snippet directly on the python interpreter. In this example, every time that a new node is added to the scene,  the <code>nodeAddedCallback</code> function wil lbe called (you can make this function a member of your <code>Logic</code> in your module. <code>caller</code>, <code>eventId</code> and <code>callData</code> have all the information you need about the event happening and you can use it to discriminate the node type you are interested in and react to it.</p>
<p>Another thing is that you probably want to act on new control points added instead of new markups nodes added. In that case, you could add the observer on the <code>NodeModifiedEvent</code> instead; or even better you can (1) observe the scene for new nodes (<code>vtkMRMLMarkupsFiducialNode</code>) and  whenever one of them is added, (2) you add a new callback that observes the <code>ModifiedEvent</code> of that particular node to monitor the changes on the number of control points.</p>
<aside class="quote no-group" data-username="dsa934" data-post="1" data-topic="27197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar"> dsa934:</div>
<blockquote>
<p>Q2. When deleting markup, why isn’t it completely deleted?</p>
<p>=&gt; If you delete the F-3 markup, when you take a new markup,<br>
it should be named F-3, but why does it become f-4?</p>
</blockquote>
</aside>
<p>Not decrementing the control point number is the expected behaviour according to the code documentation (<a href="https://github.com/Slicer/Slicer/blob/38d8d9911dcf0a72df73bec658cf2e985c95c049/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsNode.h#L706-L712" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/38d8d9911dcf0a72df73bec658cf2e985c95c049/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsNode.h#L706-L712</a>):</p>
<pre data-code-wrap="c++"><code class="lang-c++">  ///@{
  /// This value is used for generating number in the control point's name when a new point is added.
  /// The value is not decremented when a control point is deleted to keep the control point names unique.
  /// The value is reset to 0 when \sa RemoveAllControlPoints is called.
  vtkGetMacro(LastUsedControlPointNumber, int);
  vtkSetMacro(LastUsedControlPointNumber, int);
  ///@}
</code></pre>
<p>I suppose you need to manage the control points names in your module.</p>

---

## Post #3 by @dsa934 (2023-01-12 09:18 UTC)

<p>Wow, I love you man (very x 100 Thx)</p>

---

## Post #4 by @dsa934 (2023-01-13 06:39 UTC)

<aside class="quote no-group" data-username="RafaelPalomar" data-post="2" data-topic="27197">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p><code>nodeAddedModifiedObserverTag = slicer.mrmlScene.AddObserver(slicer.vtkMRMLScene.NodeAddedEvent, nodeAddedCallback)</code></p>
</blockquote>
</aside>
<p>Dear <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a><br>
Looking at your answer, I think I misunderstood the question, so I’m going to ask the question again.</p>
<h1><a name="p-88829-function-flow-1" class="anchor" href="#p-88829-function-flow-1" aria-label="Heading link"></a>function flow</h1>
<p>mouse_click_event_occured → get params → start my depthmap(‘new markup name’, ‘other infomation’ )</p>
<p>I plan to design a module that receives the markup name information when a new markup appears through a mouse click event and draws a depth map.</p>
<p>So, my current situation is as follows.</p>
<ul>
<li>
<p>Draw depthmap module ( okay )</p>
</li>
<li>
<p>Mouse click event (not yet)</p>
</li>
<li>
<p>bring node’s information (not yet)</p>
</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ada709e74cc00d8bf3274d186f2898f933d156f6.png" data-download-href="/uploads/short-url/oMctPqCFDMMx9Yrxu5KQHZRoQqG.png?dl=1" title="Question" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ada709e74cc00d8bf3274d186f2898f933d156f6.png" alt="Question" data-base62-sha1="oMctPqCFDMMx9Yrxu5KQHZRoQqG" width="465" height="321"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Question</span><span class="informations">465×321 8.92 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
When the latest markup ‘F_3’ appears through a mouse click, my module needs to receive ‘F-3’(new_markup_name’) as an input.</p>
<p>This part seems to be all you need to know how to access information about all the data that node has, but I didn’t understand this part through the doc you mentioned. can i know how?</p>

---

## Post #5 by @RafaelPalomar (2023-01-13 16:20 UTC)

<p>Hello again,</p>
<p>If I understand your problem correctly, you are probably not interested in the mouse click itself, you are interested to know when a new markups control point is placed (and yes, usually this comes after a mouse click, but it could also come from a python command). Therefore, I think you should focus on the event of adding a new control point.</p>
<p>If your design only requires to have one <code>vtkMRMLMarkupsFiducialNode</code> with several control points, I would create one in my code during initialization, and observe</p>
<pre><code class="lang-auto"># This should go in your logic initialization and should be called only
# once
self.markupsFiducialNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode')
self.markupFiducialNode.AddObserver(self.markupsFiducialNode.PointPositionDefinedEvent, self.onControlPointAdded)
</code></pre>
<p><code>self.onControlPointAdded</code> is a callback function that will be called every time a new control point on <code>self.markupsFiducialNode</code> is added. The callback function will have some parameters that will help you get all the information about the node and the control points. There is more information about this mechanism in: <a href="https://discourse.slicer.org/t/handle-markups-events-from-an-external-module/6332/28" class="inline-onebox">Handle Markups events from an external module - #28 by Fangwen_Zhai</a></p>
<p>I hope this works for you.</p>

---

## Post #6 by @dsa934 (2023-01-16 02:46 UTC)

<p><a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a></p>
<p>Hi again,</p>
<pre><code class="lang-auto">
@vtk.calldata_type(vtk.VTK_OBJECT)
def Margin_added_Callback(caller, eventId, callData):
 print("Margin added" )
 print("New node: {0}".format(callData.GetName()))
 # find margin data
 if callData.GetClassName() == 'vtkMRMLMarkupsClosedCurveNode' :
  # TODO ... 

nodeAddedModifiedObserverTag = slicer.mrmlScene.AddObserver(slicer.vtkMRMLScene.NodeAddedEvent, Margin_added_Callback)



</code></pre>
<p>Through the code you gave me, I understood how to access any data expressed in node.<br>
But I have one more question.</p>
<p>In the case of the ‘markups’ , as soon as the mouse is clicked on the markups, the information of ‘vtkMRMLMarkupsFiducialNode’ is obtained, so there is no position coordinate.</p>
<p>In the case of other data, it doesn’t matter because it is loaded in advance, but in the case of markup, creating and locating are separate actions, so it seems to be a problem.</p>
<p>In this case, how can I get the coordinates of the markup after placing it in the 3D view??</p>

---

## Post #7 by @RafaelPalomar (2023-01-16 07:18 UTC)

<p>In <code>nodeAddedCallback</code> you will “get notified” about new <code>vtkMRMLMarkupsFiducialNode</code> nodes. Every time a new of these nodes is added, you can add an observer to that node for observing the addition of new control points on that node. Something on the lines of:</p>
<pre><code class="lang-auto">markupFiducialNode.AddObserver(self.markupsFiducialNode.PointPositionDefinedEvent,
self.onControlPointAdded)
</code></pre>
<p>Then again <code>onControlPointAdded</code> should also be a callback function that will react to the addition of a control point to the fiducial markup.</p>
<p>If you think that only one <code>vtkMRMLMarkupsFiducialNode</code> will be used, you can generate it during initialization of your module yourself and you can save the first callback.</p>

---
