# Getting file name from a DICOM slice

**Topic ID**: 12364
**Date**: 2020-07-03
**URL**: https://discourse.slicer.org/t/getting-file-name-from-a-dicom-slice/12364

---

## Post #1 by @DavidCai1246 (2020-07-03 20:00 UTC)

<p>I would like to get a filename/path from a particular slice of a dicom image. For example I have loaded a DICOM file with several hundred slices and I would like to get the filename/path of a particular slice.</p>
<p>I have went through this link:</p><aside class="quote" data-post="1" data-topic="11968">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincent_c/48/5759_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/identify-a-dicom-instance-file-name-in-3d-dicom-volume/11968">Identify a DICOM Instance file name in 3D DICOM volume</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi all, 
How can I identify a the file name of a single slice in a loaded 3D DICOM volume? I have loaded a DICOM directory with several hundred slices, but after I have identified a single slice of interest, I would like to know which file name it is. 
Thanks
  </blockquote>
</aside>

<p>And was able to develop a python script that allowed me to get a filename of a particular slice, but now I want to do it in C++ as well. However, many of the functionalities and modules available in python are not available in C++.</p>
<p>Currently, I am able to get the VTKMRMLvolume node, but was wondering where I can go from there.</p>
<p>Any help is appreciated!</p>

---

## Post #2 by @lassoan (2020-07-03 21:43 UTC)

<p>All Slicer features are available in both C++ and Python. If you have difficulty figuring out the syntax for any particular method then let us know.</p>

---

## Post #3 by @DavidCai1246 (2020-07-04 00:13 UTC)

<p>Thank you for the reply Andras!</p>
<p>There are two methods in particular that I would like to know:</p>
<ol>
<li>
<p>For a given DICOM file, I would like to know which particular slice I am on (the slice number), I know that we would get this information from the DataProbe, and in python we would do<br>
<code>infoWidget = slicer.modules.DataProbeInstance.infoWidget</code><br>
<code>infoWidget.layerIJKs['B']</code><br>
to get the voxel coordinate, what would be the syntax to achieve this in C++?</p>
</li>
<li>
<p>If I currently have the instanceUID, how would I get the filename from it? In python I would do:<br>
<code>filename=slicer.dicomDatabase.fileForInstance(instUids[k])</code><br>
where k is the voxel coordinate, but what would the syntax be in C++?</p>
</li>
</ol>
<p>Thank you in advance and I really appreciate your help!</p>

---

## Post #4 by @lassoan (2020-07-04 03:28 UTC)

<aside class="quote no-group" data-username="DavidCai1246" data-post="3" data-topic="12364">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/e99b99/48.png" class="avatar"> DavidCai1246:</div>
<blockquote>
<p>For a given DICOM file, I would like to know which particular slice I am on (the slice number), I know that we would get this information from the DataProbe, and in python we would do</p>
</blockquote>
</aside>
<p>There are many ways for getting position from a view. If you want to know the current position of the mouse pointer, you can get it from the crosshair node (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_current_mouse_coordinates_in_a_slice_view">example</a>). If you want the user to mark a position then I would recommend to make the user place a markup point. If you just want the user to select a slice then you can get slice position and orientation from the slice node.</p>
<aside class="quote no-group" data-username="DavidCai1246" data-post="3" data-topic="12364">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/e99b99/48.png" class="avatar"> DavidCai1246:</div>
<blockquote>
<p>If I currently have the instanceUID, how would I get the filename from it? In python I would do:<br>
<code>filename=slicer.dicomDatabase.fileForInstance(instUids[k])</code></p>
</blockquote>
</aside>
<p>You can get the DICOM database by calling</p>
<pre><code>qSlicerApplication::application()-&gt;dicomDatabase()
</code></pre>

---

## Post #5 by @DavidCai1246 (2020-07-06 18:22 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="12364">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you just want the user to select a slice then you can get slice position and orientation from the slice node.</p>
</blockquote>
</aside>
<p>Thanks for the reply!</p>
<p>Could we also access the slice position from DataProbe?</p>

---

## Post #6 by @lassoan (2020-07-06 18:35 UTC)

<p>Data Probe module has no a logic class therefore there is no clean way of getting slice position from it. But since it is so simple to get slice index and position information from MRML nodes, there is no need to use the Data Probe module for this.</p>

---

## Post #8 by @DavidCai1246 (2020-07-06 18:50 UTC)

<p>Sounds good I will look into this!</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="12364">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you just want the user to select a slice then you can get slice position and orientation from the slice node.</p>
</blockquote>
</aside>
<p>I’m a bit new to slicer so I was wondering by slice node do you mean the volume node? Because I cant seem to find anything regarding a slice node. Also what would the syntax be to pull a slice index from a slice node?</p>

---

## Post #9 by @lassoan (2020-07-06 19:04 UTC)

<p>There is actually a slice node (<a href="http://apidocs.slicer.org/master/classvtkMRMLSliceNode.html">vtkMRMLSliceNode</a>) for each slice view, which stores slice position and orientation in its <code>SliceToRAS</code> matrix. Slice position in RAS coordinate system is stored in the last column of the matrix.</p>

---
