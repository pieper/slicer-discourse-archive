---
topic_id: 4937
title: "Fetching Real World Postition Orientation Of Htc Vive Contro"
date: 2018-12-03
url: https://discourse.slicer.org/t/4937
---

# Fetching real world postition/orientation of HTC Vive controller/HMD

**Topic ID**: 4937
**Date**: 2018-12-03
**URL**: https://discourse.slicer.org/t/fetching-real-world-postition-orientation-of-htc-vive-controller-hmd/4937

---

## Post #1 by @Gaurav_Kumar (2018-12-03 13:14 UTC)

<p>Hello!<br>
I am trying to create slices using orientation of the HTC Vive HMD/controller loation for some custom visualization. Are the position/orientation of the HTC Vive hardware available through some python code using the SlicerIGT or SlicerVirtualReality extensions?</p>
<p>The Features section of the SlicerVirtualReality documentation page (<a href="https://github.com/KitwareMedical/SlicerVirtualReality" class="inline-onebox" rel="noopener nofollow ugc">GitHub - KitwareMedical/SlicerVirtualReality: A Slicer extension that enables user to interact with a Slicer scene using virtual reality.</a>) says</p>
<blockquote>
<p>Make position of controllers available as transforms in the Slicer scene. These transforms can be used in custom modules to reslice volumes (using Volume Reslice Driver module in SlicerIGT extension) or transform any nodes in the scene.</p>
</blockquote>
<p>But I don’t seem to be able to find any way to access it.</p>
<p>Please help me with it.</p>
<p>Cheers!</p>

---

## Post #2 by @lassoan (2018-12-03 14:29 UTC)

<p>Controller transforms can be exposed as transform nodes in the scene (in world coordinate system) as described here in <a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/README.md#using-controller-transforms" rel="nofollow noopener">SlicerVirtualReality extension module documentation</a>.</p>
<p>Controller poses could be made available in physical coordinate system, too. Best option depends on what you would use that information and how, so if you need this then please provide more details about what you would like to do.</p>

---

## Post #3 by @Gaurav_Kumar (2018-12-03 14:53 UTC)

<p>I am sorry, I do not have much of an experience in working with C++ variables exposed through Python, so I basically wanted to understand how to go about viewing the Controller Pose in Python. After my query, I took the bit of code “vrView=getNode(‘VirtualRealityView’)” on the page <a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/DeveloperGuide.md" class="inline-onebox" rel="noopener nofollow ugc">SlicerVirtualReality/DeveloperGuide.md at master · KitwareMedical/SlicerVirtualReality · GitHub</a> as my starting point and realized that I need to fetch the ‘node’ for one of the controllers (left in my case). I will post the process I followed, in case someone is stuck like I was.</p>
<p>First thing I tried was printing the vrView variable above. It contained a node called</p>
<blockquote>
<p>LeftController: vtkMRMLLinearTransformNodeVirtualReality.LeftController</p>
</blockquote>
<p>I used the above syntax to get “LCon= getNode(‘vtkMRMLLinearTransformNodeVirtualReality.LeftController’)”</p>
<p>Printing the above LCon variable gave me the first glimpse of the transformation matrix for the Left Controller. Then I was again stuck at extracting that matrix for a very long time when dir(LCon) came to my rescue and I was able to extract the matrix part using:</p>
<blockquote>
<p>TMatrix=LCon.GetMatrixTransformToParent()</p>
</blockquote>
<p>This TMatrix is again an object whose individual elements have to be accessed by:</p>
<blockquote>
<p>OneElement=TMatrix.GetElement(x,y)</p>
</blockquote>
<p>Where x,y are the row and column numbers. I am still not able to get the whole 4x4 matrix in a single go.</p>
<p>Phew! Now, my question is, is there a shorter way to go about it?</p>
<p>And, the main reason why I am doing this, is to get 3 points in the horizontal plane of the Controller so that I can pass them as fiducials to the code at <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Set_slice_position_and_orientation_from_3_markup_fiducials" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/ScriptRepository - Slicer Wiki</a> so that I can display a slice based on the Pose of the controller.</p>
<p>Any ideas how I can go about getting those fiducial points from the transformation matrix?</p>
<p>Cheers!</p>

---

## Post #4 by @lassoan (2018-12-03 14:59 UTC)

<p>To show a custom model or markup at the controller’s position you don’t even need to do any programming. You can apply a transform to any transformable node by drag-and-dropping the node under the transform node in Data module / Transform hierarchy (or use Transforms module).</p>
<p>To apply a transform to a node programmatically, you can use <code>SetAndObserveTransformNodeID</code> method as described in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms#Examples" rel="nofollow noopener">Transforms module documentation</a>.</p>

---

## Post #5 by @Gaurav_Kumar (2018-12-03 15:07 UTC)

<p>I beg your pardon, I should have clarified before. I am not trying to show a custom model or creating a markup at the controller’s position. In fact, I am not trying to display anything in VR at all.</p>
<p>Let me try to explain myself with an analogy: I am just trying to make use of the controller as a sword to slice (in this case, horizontal to the Pose of the controller) the 3D model and display the slice, continually updating as the location and the orientation of the controller changes.</p>
<p>Please clarify another doubt that I have: is the transformation matrix obtained above is the same as a Quaternion? I have always been running away from understanding how Quaternions work. But if this requires it, I will give it another shot.</p>
<p>Thank you for your patience.</p>
<p>Cheers!</p>

---

## Post #6 by @lassoan (2018-12-03 15:21 UTC)

<aside class="quote no-group" data-username="Gaurav_Kumar" data-post="5" data-topic="4937">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/b782af/48.png" class="avatar"> Gaurav_Kumar:</div>
<blockquote>
<p>I am not trying to display anything in VR at all</p>
</blockquote>
</aside>
<p>I’m not sure what you would like to do. What do you mean by VR? Volume rendering or virtual reality?</p>
<p>If you mean that you would like to reslice the volume using controllers then use the controller transforms in SlicerIGT extension’s <em>Volume reslice driver</em> module.</p>
<p>Using the HTC Vive to track hand pose is a huge overkill. You can use a <a href="https://www.youtube.com/watch?v=MOqh6wgOOYs">webcam and a simple 2D barcode to define transforms</a>, use an inertial measurement unit (using <a href="http://www.plustoolkit.org">PLUS toolkit</a>), a <a href="https://www.youtube.com/watch?v=BG8udCVo1gg">LeapMotion controller</a>, or a low-cost professional-grade pose tracker (such as <a href="https://optitrack.com/products/v120-trio/">OptiTrack Duo</a>) which have various advantages over using an HTC Vive for this.</p>

---

## Post #7 by @Gaurav_Kumar (2018-12-03 15:37 UTC)

<p>I found exactly what I am trying to achieve. I would like to replicate the project shown in the following video:<br>
</p><div class="lazyYT" data-youtube-id="478ynSlt_TA" data-youtube-title="Magic Slicer v0.1" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>I played around with SlicerIGT extension’s <em>Volume reslice driver</em> module but I am not able replicate the above effect using the module. Did I miss anything?</p>
<p>Cheers!</p>

---

## Post #8 by @lassoan (2018-12-03 15:51 UTC)

<p>I confirm that you can do the above by using <em>Volume reslice driver</em> module, without writing a single line of code. In fact, this was one of the demos that we showed last week at RSNA - you can download the Slicer scene from <a href="https://1drv.ms/u/s!Arm_AFxB9yqHtoRIs5m64GtnsGboKw">here</a>. Just load the scene, enable virtual reality view, and move your hand into the volume to see the slices. You can switch to a one-up slice view to see the slice full-screen on your tablet.</p>
<aside class="quote no-group" data-username="Gaurav_Kumar" data-post="7" data-topic="4937">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/b782af/48.png" class="avatar"> Gaurav_Kumar:</div>
<blockquote>
<p>Did I miss anything?</p>
</blockquote>
</aside>
<p>Yes, I think so. We can only help if you describe exactly what you did, what you expected to happen, and what happened instead.</p>

---
