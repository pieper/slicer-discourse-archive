# qSlicerMarkupsPlaceWidget - Get control point coordinates

**Topic ID**: 26506
**Date**: 2022-11-30
**URL**: https://discourse.slicer.org/t/qslicermarkupsplacewidget-get-control-point-coordinates/26506

---

## Post #1 by @LuisaDantas (2022-11-30 10:51 UTC)

<p>Hey!</p>
<p>I’m building a module for Slicer and using qSlicerMarkupsPlaceWidget() to let the user place a control point on the image. The ideia is just to get the coordinates of this control point, but I’m not sure how to acces this information and store it. I would appreciate some help.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @cpinter (2022-11-30 14:10 UTC)

<p>There is a Script repository that contains hundreds of little code examples, including this: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-to-markups-point-list-properties" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>
<p>Btw I just posted a piece of code in another thread that among other things gets the position of a control point. You could use it as inspiration. Here it is: <a href="https://discourse.slicer.org/t/importing-a-model-to-stl-with-markups/26502/2" class="inline-onebox">Exporting a model to STL with markups - #2 by cpinter</a></p>

---

## Post #3 by @LuisaDantas (2022-11-30 16:06 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> Great it worked just fine, and the repository will help me a lot, huge thank you!</p>

---

## Post #4 by @cpinter (2022-12-01 11:55 UTC)

<p>Sorry I put the wrong link in my comment. I fixed it in case someone needs it in the future.</p>

---

## Post #5 by @LuisaDantas (2022-12-01 16:24 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> I having trouble to understand one thing. On the script you mentioned from the other thread, on this line <code>fiducialNode = getNode('F')</code> your node name is ‘F’, so if there’s n control points they all would be on node F?</p>
<p>On my case, I need to get the coordinates from a user inserted control point (they can only insert one, but I will deal with that later). Is there a way to get the coordinates without having to pass the name of the node? If we suppose that there’s only one.</p>
<p>Edit: I have one more question, how can I get the coordinates in pixels?</p>

---

## Post #6 by @cpinter (2022-12-07 10:20 UTC)

<p>You need to get the node somehow so that you can do operations on it. If you are sure you only have one node, you can use this function <a href="https://apidocs.slicer.org/master/classvtkMRMLScene.html#a21560f853d73548021e75d991d5aa34d" class="inline-onebox">Slicer: vtkMRMLScene Class Reference</a><br>
Feel free to look at other scripted modules for inspiration. They all use nodes.</p>
<aside class="quote no-group" data-username="LuisaDantas" data-post="5" data-topic="26506">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/b38774/48.png" class="avatar"> LuisaDantas:</div>
<blockquote>
<p>I have one more question, how can I get the coordinates in pixels?</p>
</blockquote>
</aside>
<p>See here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-voxel-coordinates-from-markup-control-point-ras-coordinates" class="inline-onebox">Script repository — 3D Slicer documentation</a><br>
The script repository is a very valuable resource, I recommend that too.</p>

---
