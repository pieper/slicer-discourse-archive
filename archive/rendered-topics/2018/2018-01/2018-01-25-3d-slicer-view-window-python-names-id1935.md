---
topic_id: 1935
title: "3D Slicer View Window Python Names"
date: 2018-01-25
url: https://discourse.slicer.org/t/1935
---

# 3D Slicer View Window Python Names

**Topic ID**: 1935
**Date**: 2018-01-25
**URL**: https://discourse.slicer.org/t/3d-slicer-view-window-python-names/1935

---

## Post #1 by @Ahmed_Soufane (2018-01-25 21:10 UTC)

<p>What would the python node names be for the red, yellow, and green views?<br>
I am getting a error in which the:</p>
<pre><code>markupsNode =slicer.mrmlScene.GetFirstNodeByName("CTChest") 
</code></pre>
<p>command does not grab the individual views causing this error:</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
AttributeError: ‘vtkCommonCorePython.vtkMRMLScalarVolumeNode’ object has no attribute<br>
’GetNthFiducialPosition’</p>
<p>So it would seem like the node name would be the issue, is that the case?</p>

---

## Post #2 by @pieper (2018-01-25 23:17 UTC)

<p>In the code and error you pasted you are getting the vtkMRMLScalarVolumeNode, but if you want to get the vtkMRMLMarkupsFiducialNode (default name “F”) and get the point you get call:</p>
<pre><code class="lang-auto">markupsNode = slicer.mrmlScene.GetFirstNodeByName("F")
p = [0,]*3
markupsNode.GetNthFiducialPosition(0, p)
</code></pre>
<p>Not sure what you mean by trying to get with the view names - did need fiducial positions or something about the views?</p>

---

## Post #3 by @Ahmed_Soufane (2018-01-26 00:41 UTC)

<p>Hi,<br>
What I am trying to do is to control the brightness, zooming in/out, and rotation via the python interactor or window in the 3d slicer. I have been trying so hard to figure out the code that would enable me to manipulate these three characteristics, but I have been not able to understand the logic of 3dslicer code. Would you please provide me with the proper code that would allow me to edit/manipulate the brightness, zooming in/out, and rotation via the python interactor ?</p>
<p>Thank you</p>

---

## Post #4 by @pieper (2018-01-26 13:31 UTC)

<p>Hi Ahmed -</p>
<p>Probably you need to start by getting comfortable with doing python programming in Slicer.  This tutorial goes through the whole process and even if it has some steps that aren’t exactly what you need it will give you the background you need to understand the documentation and examples:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Training#Developing_and_contributing_extensions_for_3D_Slicer" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/4.8/Training#Developing_and_contributing_extensions_for_3D_Slicer</a></p>
<p>As I mentioned in response to your previous question, you can control the views by accessing the various associated nodes.  Did you try the SetFieldOfView example I sent?</p>
<aside class="quote" data-post="1" data-topic="1912">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/b38774/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/rotation-zooming/1912">Rotation&amp;zooming </a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello, 
How can I modify or call the rotation of an image on the python interactor  on 3dslicer ? 
Is it possible to modify or edit zooming in and out of the image on python console ?
  </blockquote>
</aside>


---

## Post #5 by @lassoan (2019-07-25 12:46 UTC)

<p>A post was split to a new topic: <a href="/t/select-cells-of-a-3d-model/7753">Select cells of a 3D model</a></p>

---
