---
topic_id: 27393
title: "How To Get Mouse Position In 3D View"
date: 2023-01-21
url: https://discourse.slicer.org/t/27393
---

# How to get mouse position in 3D view?

**Topic ID**: 27393
**Date**: 2023-01-21
**URL**: https://discourse.slicer.org/t/how-to-get-mouse-position-in-3d-view/27393

---

## Post #1 by @dsa934 (2023-01-21 18:57 UTC)

<p>Operating system: window 10<br>
Slicer version: 5.2.1</p>
<pre><code class="lang-auto">## Custom add markups functions 
def test():

    # get crosshair 
    crosshairNode=slicer.util.getNode("Crosshair")

    pos = [0,0,0]

    crosshairNode.GetCursorPositionRAS(pos)

    print(pos)

    slicer.modules.markups.logic().AddControlPoint(pos[0], pos[1], pos[2])


</code></pre>
<p>This code is an implementation of a code that creates markups according to the mouse position in the slicer view (R,Y,G).</p>
<p>How to do this function in 3D view?</p>
<pre><code class="lang-auto">placeModePersistence = 1
slicer.modules.markups.logic().StartPlaceMode(placeModePersistence)

</code></pre>
<p>If you add markups through the code above, it is not added to the markups list, so it doesn’t fit the purpose I’m trying to do.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb1812995a7359782364ddb18e08988795321307.png" alt="image" data-base62-sha1="zPhq4pAFfrbitCApuzamAHwAOYT" width="437" height="239"></p>
<p>The purpose is to replace the process of taking markup by clicking the Point list in GUI mode with ‘shortcut’.</p>

---

## Post #2 by @rbumm (2023-01-21 23:45 UTC)

<p>Hi,</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-current-mouse-coordinates-in-a-slice-view">This code from the script repository</a> should help.</p>

---

## Post #3 by @dsa934 (2023-01-22 01:15 UTC)

<p>Hi,</p>
<p>The code above is what I’ve been looking at for reference.</p>
<p>The code outputs the coordinates whenever the mouse is moved, but what I need is a function that gets the mouse coordinates only once for a specific action( right_button_click_in_mouse … )</p>
<pre><code class="lang-auto">crosshairNode.AddObserver(slicer.vtkMRMLCrosshairNode.CursorPositionModifiedEvent, onMouseMoved)

</code></pre>
<p>Is there any way to make this work only once?</p>

---

## Post #4 by @jamesobutler (2023-01-22 01:37 UTC)

<p>Can you describe in more specific terms the workflow and functionality of what you desire? This will help us provide more specific feedback to help solve the workflow that you desire.</p>
<p>Something like:<br>
“While viewing a model in the 3D view, I would like to place a control point on the model at the location of the cursor as initiated by a keyboard shortcut so that I stay in ViewTransform mouse mode”</p>
<p>Are you looking for shortcuts to place multiple control points? Or shortcut to create an entirely new point list. Point lists can contain X number of control points so creating a new point list that only contains a single control point can be very inefficient.</p>

---

## Post #5 by @dsa934 (2023-01-22 02:18 UTC)

<p>Hi <a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/5065cf16babdce541c092d4db2551ae926ebafb3.png" alt="image" data-base62-sha1="btejYRzhkOIwy8yPxUVJuPgaY1R" width="428" height="287"></p>
<p>&lt;fig1. nodes in Scene&gt;</p>
<p>As in the example above, importing hundreds of markups through GUI manipulation in a 3D view is cumbersome, so I’m trying to create a new keyboard shortcut function.</p>
<pre><code class="lang-auto">def custom_import_markup() :

  #TODO

  1)   Get current mouse cursor position in 3D view.
 
  2)  Adds markup nodes to the 3D view based on the fetched mouse position.

  3)  Also add it to the nodes list you can see in fig1.

shortcut = qt.QShortcut(qt.QKeySequence("Ctrl+e"), slicer.util.mainWindow())
shortcut.connect("activated()", lambda: custom_import_markup())
 
</code></pre>
<p>Therefore, I would like to implement a function that, when I put the mouse somewhere in the 3D view and press ‘ctrl+e’, the markup is added to the 3D VIEW and at the same time, the markup node of ‘F_n(example_case n =5 )’ is added to the node list of fig.1.</p>
<p><strong>TODO - 3)  means</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd10cb96ae77a2ed1e346dd0085ab6f9add26f55.png" data-download-href="/uploads/short-url/qYydZfj5qGQewmLecWbLQKTHfhz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd10cb96ae77a2ed1e346dd0085ab6f9add26f55_2_690x250.png" alt="image" data-base62-sha1="qYydZfj5qGQewmLecWbLQKTHfhz" width="690" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd10cb96ae77a2ed1e346dd0085ab6f9add26f55_2_690x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd10cb96ae77a2ed1e346dd0085ab6f9add26f55_2_1035x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd10cb96ae77a2ed1e346dd0085ab6f9add26f55_2_1380x500.png 2x" data-dominant-color="AFB1DB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1468×533 28.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<pre><code class="lang-auto">placeModePersistence = 1
slicer.modules.markups.logic().StartPlaceMode(placeModePersistence)
</code></pre>
<p>This code adds markup whenever the mouse is clicked in the 3D view. This feature works great for my purpose. <strong>However, there is a problem that it cannot be added to the node on the left.</strong></p>
<p>I would appreciate it if you could let me know if you have any reference material or code to implement the above function.</p>

---

## Post #6 by @jamesobutler (2023-01-22 03:10 UTC)

<aside class="quote no-group" data-username="dsa934" data-post="5" data-topic="27393">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar"> dsa934:</div>
<blockquote>
<pre><code class="lang-auto">placeModePersistence = 1
slicer.modules.markups.logic().StartPlaceMode(placeModePersistence)
</code></pre>
<p>This code adds markup whenever the mouse is clicked in the 3D view. This feature works great for my purpose. <strong>However, there is a problem that it cannot be added to the node on the left.</strong></p>
</blockquote>
</aside>
<p>I observe that the code appropriately adds a Markup Point List to the scene and persistently adds Control Points to the Markup Point List. The first table in the Markups module is the list of nodes. In the “Control Points” section there is the table that shows all the control points that are in the Point List Markup node.</p>
<p>Markup node Type: “Point List” (vtkMRMLMarkupsFiducialNode)<br>
Markup node name: “F”<br>
Markup “F” Control Points: F-1, F-2, F-3, F-4, F-5<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/801c8bce985459d3e2d9d22cf4415298de5931bc.png" data-download-href="/uploads/short-url/ihkh6Ww4SWV4P7PZCsbKhpAP7Va.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/801c8bce985459d3e2d9d22cf4415298de5931bc_2_690x370.png" alt="image" data-base62-sha1="ihkh6Ww4SWV4P7PZCsbKhpAP7Va" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/801c8bce985459d3e2d9d22cf4415298de5931bc_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/801c8bce985459d3e2d9d22cf4415298de5931bc_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/801c8bce985459d3e2d9d22cf4415298de5931bc_2_1380x740.png 2x" data-dominant-color="B4B7DE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1030 85.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>There is also the Markups toolbar that allows for creating new markup nodes and accessing the placement mode button to add control points to the selected markup. Creating a new Point List markup through the toolbar, automatically puts the state into control point placement mode.<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html#place-new-markups" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html#place-new-markups</a></p>

---

## Post #7 by @dsa934 (2023-01-22 03:55 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>
<p>Oh my god,</p>
<p>Until now I had mistakenly thought that ‘vtkMRMLMarkupsFiducialNode’ was a position.<br>
I clearly understood that ‘vtkMRMLMarkupsFiducialNode’ is a list of points.</p>
<p>Previously, I implemented the cunstom_undo function by deleting the node, but I need to modify it by individually accessing the control point elements of the point list.</p>

---

## Post #8 by @dsa934 (2023-01-25 02:43 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>
<p>Hello again,</p>
<p>With your help, I was able to complete the desired feature. However ,When I asked the company, they were using the inefficient method you mentioned for various reasons.<br>
They were using only one control point per point list.</p>
<p>So my other question is how can I create a ‘Point List’ with a mouse click?  ( one click → make one point list) If you can refer to any reference material, I will do it.</p>

---

## Post #9 by @jamesobutler (2023-01-25 03:04 UTC)

<p>You would need to add code that utilizes AddNewNodeByClass methods for vtkMRMLMarkupsFiducialNode. As in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#add-a-button-to-module-gui-to-activate-control-point-placement" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a>.</p>
<p>What is the reason for having multiple point list nodes with only one control point in each? There can be a drop in performance when there are a lot of nodes in the scene. To code, it would be easier to use one point list and access the individual control point locations in the point list.</p>

---

## Post #10 by @dsa934 (2023-01-25 04:27 UTC)

<p>Hi ! <a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>
<p>As you said, using one control point in one point list is very inefficient.</p>
<p>Here’s a quick summary of what my colleague told me:</p>
<ul>
<li>A label is required for each control point.</li>
<li>In the case of an efficient method, when saving as a json file, one json file for one point list is saved.</li>
<li>They want to save and manage one control point each as a json file, and it has been in the past.</li>
<li>It is annoying to press the point list on the GUI and press the control point.</li>
</ul>
<p>I also don’t understand why you use this method.<br>
I know how to save each control point as a json file, but I have to implement it in an inefficient way because it takes too long to apply to what my company has done before.</p>
<p>======================================</p>
<p>In slicer view (R, Y, G), you can know the current coordinates of the mouse through the ‘crosshair node’, but is that impossible in 3D view?</p>
<p>In my opinion, one actions are required to achieve this inefficient method:</p>
<h1><a name="p-89486-h-1-get-mouse-coordinates-from-3d-view-only-once-1" class="anchor" href="#p-89486-h-1-get-mouse-coordinates-from-3d-view-only-once-1" aria-label="Heading link"></a>1. Get mouse coordinates from 3d view (only once)</h1>
<pre><code class="lang-auto">def onMouseMoved(observer,eventid):
  ras=[0,0,0]
  crosshairNode.GetCursorPositionRAS(ras)
  print(ras)

crosshairNode=slicer.util.getNode("Crosshair")
crosshairNode.AddObserver(slicer.vtkMRMLCrosshairNode.CursorPositionModifiedEvent, onMouseMoved)
</code></pre>
<p>In the case of the code above, the coordinates are retrieved whenever the mouse position is modified. Is there a way to obtain the coordinates only once when the mouse is clicked?</p>
<p>The rest is just a matter of creating a point list with the imported coordinate values.</p>

---

## Post #11 by @jamesobutler (2023-01-25 04:40 UTC)

<aside class="quote no-group" data-username="dsa934" data-post="10" data-topic="27393">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar"> dsa934:</div>
<blockquote>
<p>A label is required for each control point.</p>
</blockquote>
</aside>
<p>In the Markups module a point list can show labels for each control point, or the labels can be hidden. Is the existing behavior not what is desired?</p>

---

## Post #13 by @dsa934 (2023-01-25 06:20 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>
<aside class="quote no-group" data-username="dsa934" data-post="10" data-topic="27393">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar"> dsa934:</div>
<blockquote>
<ul>
<li>In the case of an efficient method, when saving as a json file, one json file for one point list is saved.</li>
<li>They want to save and manage one control point each as a json file, and it has been in the past.</li>
<li>It is annoying to press the point list on the GUI and press the control point.</li>
</ul>
</blockquote>
</aside>
<p>No</p>
<p>There is only one thing I want to know.</p>
<pre><code class="lang-auto">def test():

    # get crosshair 
    crosshairNode=slicer.util.getNode("Crosshair")

    pos = [0,0,0]

    crosshairNode.GetCursorPositionRAS(pos)

    print(pos)

    pointListNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode","F")

    pointListNode.AddControlPoint(pos[0], pos[1], pos[2])


shortcut = qt.QShortcut(qt.QKeySequence("Ctrl+r"), slicer.util.mainWindow())
shortcut.connect("activated()", lambda: test())

</code></pre>
<p>The above code gets the position of the mouse cursor in slicer view ( R,Y,G ), but it does not work in 3D view. Any way to solve this?</p>

---
