---
topic_id: 19394
title: "Getselectionnode Getactivevolumeid Always Returns None"
date: 2021-08-28
url: https://discourse.slicer.org/t/19394
---

# `GetSelectionNode().GetActiveVolumeID()` always returns None

**Topic ID**: 19394
**Date**: 2021-08-28
**URL**: https://discourse.slicer.org/t/getselectionnode-getactivevolumeid-always-returns-none/19394

---

## Post #1 by @keri (2021-08-28 14:54 UTC)

<p>Hi,</p>
<p>Probably I misunderstand what is selection node but here is the example:</p>
<pre><code class="lang-python">import numpy as np
import math

def some_func(x, y, z):
  return 0.01*x*x + 0.01*y*y + 0.01*z*z

a = np.fromfunction(some_func,(128,128,128))

volumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode')

print(slicer.app.applicationLogic().GetSelectionNode().GetActiveVolumeID())    # returns `None`
</code></pre>
<p>What do I do wrong?<br>
Is it possible to have multiple nodes displayed on the scene and get the latest node that I picked with Mouse_1 btn?</p>

---

## Post #2 by @lassoan (2021-08-28 21:46 UTC)

<p>Active volume concept was introduced in very early Slicer versions. We have not actively removed it to reduce unnecessary breaking of backward compatibility, but bnow it is not used for anything. The main reason is that there can be any number of “active” volumes. Even in one view we can show 3 volumes (and any number of models, markups, transforms, etc).</p>
<p>It comes up quite often that some kind of selection feature would be useful, for example to make it easier to find an object in different views, reduce the chance of accidental modifications, etc. What is your use case? How do you envision the concept of selected volumes (and other nodes)?</p>

---

## Post #3 by @keri (2021-08-29 00:25 UTC)

<p>Thank you for reply,</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="19394">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What is your use case? How do you envision the concept of selected volumes (and other nodes)?</p>
</blockquote>
</aside>
<p>For now I would like to write a module that displays <code>vtkCubeAxesActor</code> around chosen object on the scene.</p>
<p>I can see that in Slicer we usually chose the “active” volume by selecting in pop-up menu (maybe in volume module or volume rendering or in widget controller).</p>
<p>Nevertheless I’m a geoscientist and I’m working on custom app for geoscience and there we usually have numerous of objects: seismic data (usually displayed as <code>vtkImageData</code>), wells (displayed as curves and each well has its name), surfaces (also has its name) and other type of data (like points, polygons etc). When there are plenty of displayed objects on the screen it is very simple to forget what name has some object but chosing object from the scene (by clicking on that object) is very efficient way to chose the object needed.</p>
<p>Thus I see my module should have drop-down menu for chosing current object (usual for Slicer) but the user should be able to set current object in two ways:</p>
<ol>
<li>directly (from drop down menu);</li>
<li>interactively from the scene (when he clicks on the object from the scene the active object should be changed in that drop-down menu).</li>
</ol>
<p>Or make a pop-up menu when user clicks on scene’s object Mouse 2 and there add action <strong>“Set active”</strong>. That is even better I think and the possibility to add custom actions there would make Slicer more user frienly and more customizable (my opinion).</p>
<p>P.S. Slicer has module concept. That make allows for any who is familiar with python or C++ to easilly develop custom modules. I very like that. But for me there are two things that are unusual:</p>
<ol>
<li>you cannot invoke pop-up menu by clicking on scene and have some object properties;</li>
<li>there is no <code>QTreeView</code> widgets where user could see his data on the disk (not loaded to RAM) but there is only <code>Data</code> module where all loaded data resides. In my SlicerCAT I add this and it looks like diplayed on the picture:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/239b36b990ab9cdb8e7c00c93d32b0539e1e37f0.png" data-download-href="/uploads/short-url/54ZfPSCQiJzHSRJJx5sYlx7vLQ4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/239b36b990ab9cdb8e7c00c93d32b0539e1e37f0_2_690x367.png" alt="image" data-base62-sha1="54ZfPSCQiJzHSRJJx5sYlx7vLQ4" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/239b36b990ab9cdb8e7c00c93d32b0539e1e37f0_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/239b36b990ab9cdb8e7c00c93d32b0539e1e37f0_2_1035x550.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/239b36b990ab9cdb8e7c00c93d32b0539e1e37f0_2_1380x734.png 2x" data-dominant-color="ACADB8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1600×852 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>
<p>The concept of this is when user checks-on data in tree view then the data gets load to the RAM (or that sets some module active and in that module user choses wich part of that big data he wants to load to the RAM). When data is loaded user can see it in <code>Data</code> module. Probably Slicer could display filesystem in treeview using <a href="https://doc.qt.io/qt-5/qdirmodel.html" rel="noopener nofollow ugc"> QDirModel</a> (also as I remember user can drag and drop files to load it, with this treeview would look nice)</p>
<p>These two features are standard in geoscience world.<br>
Though I’m pretty sure you are familiar with some other 3D applications from other science field but have a look at short video of well known in geoscience world <a href="https://www.youtube.com/watch?v=8GVZaa61l40&amp;list=PLhc-TLhz11noHiMlReaToRresBie08h-G&amp;ab_channel=SacredGeoScience" rel="noopener nofollow ugc">Petrel commercial app (video)</a> (it is also based on VTK as I know). Perhaps you will find somethin useful</p>

---

## Post #4 by @lassoan (2021-09-01 05:05 UTC)

<aside class="quote no-group" data-username="keri" data-post="3" data-topic="19394">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>you cannot invoke pop-up menu by clicking on scene and have some object properties</p>
</blockquote>
</aside>
<p>This is because for many years we tried to make VTK widgets work and they were just bad. A few years ago we started to rework the widget infrastructure and we have now a nice way to to pick objects by right-clicking on them and perform any action on them (edit properties, etc.). We have only implemented this for markups so far, but would be straightforward to implement it for any other node types. It would be great if you could work on this.</p>
<aside class="quote no-group" data-username="keri" data-post="3" data-topic="19394">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>there is no <code>QTreeView</code> widgets where user could see his data on the disk (not loaded to RAM) but there is only <code>Data</code> module where all loaded data resides. In my SlicerCAT I add this and it looks like diplayed on the picture:</p>
</blockquote>
</aside>
<p>Slicer, similarly to most other applications, do not have an always-on local file browser. This need has only come up very few times over the years and it is getting less and less relevant. Nowadays you browse remote data stores, you get all the metadata live from there, and the local file system only serves as a cache for bulk data.</p>
<p>You can very easily add a local file browser module that shows a folder/file tree and allows partial loading (similarly to ImageStacks module in SlicerMorph extension), but this just feels very dated. I would recommend to not spend time with implementing a local file browser but instead implement a nice and convenient GUI for browsing and retrieving data from a storage service. Such a service is needed to meet expectations of users who want to access their data anywhere, share it, get updates in real-time, etc. The storage service can be hosted on the cloud, but could also run locally, so you would not be forced to use a remote server, if you don’t want.</p>
<p>You can have a look at the <a href="https://github.com/lassoan/SlicerDICOMwebBrowser/">DICOMweb Browser</a> or <a href="https://github.com/flywheel-apps/SlicerFlywheelConnect">FlyWheel</a> extensions for some simple examples.</p>

---
