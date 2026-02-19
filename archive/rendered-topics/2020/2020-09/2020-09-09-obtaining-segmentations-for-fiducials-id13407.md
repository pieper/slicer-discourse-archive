---
topic_id: 13407
title: "Obtaining Segmentations For Fiducials"
date: 2020-09-09
url: https://discourse.slicer.org/t/13407
---

# Obtaining Segmentations for Fiducials

**Topic ID**: 13407
**Date**: 2020-09-09
**URL**: https://discourse.slicer.org/t/obtaining-segmentations-for-fiducials/13407

---

## Post #1 by @FatihSogukpinar (2020-09-09 18:59 UTC)

<p>Operating system: Windows 10 Pro<br>
Slicer version: 4.10 and / or 4.11<br>
Hi all,</p>
<p>I have a set of fiducial points and a segmentation and I need to obtain the segments which the points belong to.<br>
There are so many points that I need an automated way to do that.<br>
How can I obtain the segments for each point using the Python interface ?<br>
I can see the regions manually by pointing the mouse on them, but I don’t know how I can get them by code.</p>
<p>Thank you all and best regards.</p>

---

## Post #2 by @lassoan (2020-09-09 19:29 UTC)

<p>See this example in the script repository:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_segments_visible_at_a_selected_position" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_segments_visible_at_a_selected_position</a></p>

---

## Post #3 by @FatihSogukpinar (2020-09-11 02:30 UTC)

<p>Thanks !</p>
<p>Another related question : How can I obtain RAS coordinates of a segment ?<br>
I mean not just the extends or boundaries, but the whole segment.</p>
<p>Thank you and best regards.</p>

---

## Post #4 by @lassoan (2020-09-11 02:37 UTC)

<p>Sorry, I don’t understand what you mean. What would you like to do?</p>

---

## Post #5 by @FatihSogukpinar (2020-09-11 04:17 UTC)

<p>I mean obtaining the RAS coordinates the segments in a segmentation.</p>
<p>I can get the max / min RAS coordinates, but I need the coordinates of the whole 3-D region, in RAS coordinates.</p>

---

## Post #6 by @lassoan (2020-09-11 04:28 UTC)

<p>“coordinates of the whole 3-D region” is undefined. A region’s boundaries have coordinates, the region’s center of gravity has coordinates, each non-zero voxel in the region has coordinates, etc. If you explain what you want to do with the data (maybe draw a sketch or annotate a screenshot) then it may make it more clear.</p>

---

## Post #7 by @FatihSogukpinar (2020-09-11 04:51 UTC)

<p>Let me try to define what I need :</p>
<p>Let’s assume we have a region in a segmentation. That region covers a 3-D region in the MRI space.<br>
I need coordinates of the voxel in this 3-D, but not only in the MRI space, also in the RAS coordinates.</p>
<p>Or, if I can get the coordinates of all of the boundary points, that would also work well.</p>

---

## Post #8 by @lassoan (2020-09-11 05:23 UTC)

<p>You can get all segment voxels as numpy array (using <code>arrayFromVolume</code> method), get IJK coordinates of non-zero voxels using standard numpy array operations (<code>where</code>, …),and convert IJK to RAS as shown in examples in the script repository (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_markup_fiducial_RAS_coordinates_from_volume_voxel_coordinates">here</a>). You can also export segmentation to model and get coordinates of model points (see examples in script repository).</p>
<p>Although you can obtain all these data, this should be very rarely necessary. Are you sure you need coordinates of all these hundreds of thousands or millions of points? What is your overall goal?</p>

---

## Post #9 by @FatihSogukpinar (2020-09-11 18:50 UTC)

<p>I agree but I need this for a complicated project where the segmentation itself is not perfect…<br>
I tried your suggestion but I have some problems - the resulting RAS coordinates are not correct yet.<br>
Also, I get this warning :</p>
<p><em>arrayFromSegment is deprecated! Binary labelmap representation may be shared between multiple segments! Use arrayFromSegmentBinaryLabelmap to access a copy of the binary labelmap that will not modify the original labelmap. Use arrayFromSegmentInternalBinaryLabelmap to access a modifiable internal lablemap representation that may be shared between multiple segments.</em></p>
<p>I must be doing a mistake during IJK to RAS conversion, but I don’t know what it is.<br>
I am using Slicer 4.11. Should I do anything different for this version ? Or is the code provided in</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_markup_fiducial_RAS_coordinates_from_volume_voxel_coordinates" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_markup_fiducial_RAS_coordinates_from_volume_voxel_coordinates</a></p>
<p>fine for 4.11 ?</p>
<p>Thank you so much.</p>

---

## Post #10 by @lassoan (2020-09-11 19:09 UTC)

<aside class="quote no-group" data-username="FatihSogukpinar" data-post="9" data-topic="13407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fatihsogukpinar/48/7257_2.png" class="avatar"> FatihSogukpinar:</div>
<blockquote>
<p>arrayFromSegment is deprecated! Binary labelmap repr</p>
</blockquote>
</aside>
<p>This is just a deprecation warning. Since you don’t modify the segment, you can still use <code>arrayFromSegment</code>, but it would be more clear if you switched to <code>arrayFromSegmentBinaryLabelmap</code> function.</p>
<aside class="quote no-group" data-username="FatihSogukpinar" data-post="9" data-topic="13407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fatihsogukpinar/48/7257_2.png" class="avatar"> FatihSogukpinar:</div>
<blockquote>
<p>this for a complicated project where the segmentation itself is not perfect</p>
</blockquote>
</aside>
<p>That’s fine - there is no such thing as a perfect segmentation. There are tools and best practices to manage that. If you tell what is your overall goal and what your problems are then we can give advice of what methods have been developed to address them.</p>

---

## Post #11 by @FatihSogukpinar (2020-09-11 19:38 UTC)

<p>Let me summariza what my overall goal is :</p>
<p>I need to assign some fiducial points to their corresponding segments. But since the segmentation has errors, some points, though they are quite close to the segment, are not assigned to their regions.<br>
So I am trying to assign the points if they are close enough to a segment (say, 1mm away from the segment boundaries). This is why I need the RAS coordinates.<br>
But if there is a built-in function in Slicer which can do these kind of things, that would work, too.</p>
<p>Thanks !</p>

---

## Post #12 by @lassoan (2020-09-11 19:45 UTC)

<p>There are many ways to achieve this, but one simple way is to export the segmentation to a model node then <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Measure_distance_of_points_from_surface">get the closest point on the surface</a>.</p>

---

## Post #13 by @FatihSogukpinar (2020-09-11 19:53 UTC)

<p>I also have models of the segmentation but the model seems even more imperfect than the segmentation.</p>
<p>Is there a way to do this with the segmentation itself ?</p>

---

## Post #14 by @lassoan (2020-09-11 20:02 UTC)

<p>The model that Segmentations module generates from the segment should not be worse. Maybe you can smooth the binary labelmap representation and disable smoothing for the surface generation to make the generated surface more closely match the labelmap. Can you attach an example image so that we have a better idea of the difficulty of the problem?</p>

---

## Post #15 by @FatihSogukpinar (2020-09-11 20:16 UTC)

<p>Here is an example. I think the model boundaries aren’t really close enough to the segmentation itself.<br>
Also in some cases, two neighboring models cross each other , i.e. one single point seems to belong to two different models at the same time.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/040096e2e23316333e6c84f57ccb1adcd3728fc1.jpeg" data-download-href="/uploads/short-url/zpaHIKdDJKi9zsd8csLxtCmuPv.jpeg?dl=1" title="Screenshot_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/040096e2e23316333e6c84f57ccb1adcd3728fc1_2_690x480.jpeg" alt="Screenshot_1" data-base62-sha1="zpaHIKdDJKi9zsd8csLxtCmuPv" width="690" height="480" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/040096e2e23316333e6c84f57ccb1adcd3728fc1_2_690x480.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/040096e2e23316333e6c84f57ccb1adcd3728fc1_2_1035x720.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/040096e2e23316333e6c84f57ccb1adcd3728fc1.jpeg 2x" data-dominant-color="343532"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_1</span><span class="informations">1327×924 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #16 by @lassoan (2020-09-11 20:18 UTC)

<p>This segmentation looks good. There is no significant noise or other issues.</p>
<p>You can reduce or disable surface smoothing to make the generated surface match the labelmap more closely.</p>

---

## Post #17 by @FatihSogukpinar (2020-09-11 20:27 UTC)

<p>I don’t know how to disable surface smoothing to generate the model, could you help me with that ?</p>

---

## Post #18 by @lassoan (2020-09-11 20:30 UTC)

<aside class="quote no-group" data-username="FatihSogukpinar" data-post="17" data-topic="13407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fatihsogukpinar/48/7257_2.png" class="avatar"> FatihSogukpinar:</div>
<blockquote>
<p>how to disable surface smoothing to generate the model</p>
</blockquote>
</aside>
<p>See <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#panels-and-their-use">Segment editor documentation page</a> (look for “smoothing”).</p>

---

## Post #19 by @FatihSogukpinar (2020-09-12 03:29 UTC)

<p>Thank you for all the information !<br>
I found the smoothing settings.</p>
<p>But when I try to view new models I cannot see them, even though the visibilty box is checked. What might cause that ?</p>
<p>And I also obtained the minimum distances. But some of the distances are negative. Should I take their absolute value ?</p>
<p>Thanks !</p>

---

## Post #20 by @lassoan (2020-09-12 04:06 UTC)

<aside class="quote no-group" data-username="FatihSogukpinar" data-post="19" data-topic="13407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fatihsogukpinar/48/7257_2.png" class="avatar"> FatihSogukpinar:</div>
<blockquote>
<p>But when I try to view new models I cannot see them, even though the visibilty box is checked. What might cause that ?</p>
</blockquote>
</aside>
<p>Computaiton of closed surface representation takes time, so it is not created unless it is requested.<br>
You can create it in Segmentations module by clicking “Create” button in the corresponding row in Representations section (or in Segment Editor module click “Show 3D”).</p>
<aside class="quote no-group" data-username="FatihSogukpinar" data-post="19" data-topic="13407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fatihsogukpinar/48/7257_2.png" class="avatar"> FatihSogukpinar:</div>
<blockquote>
<p>And I also obtained the minimum distances. But some of the distances are negative. Should I take their absolute value ?</p>
</blockquote>
</aside>
<p>Negative distance means inside, positive distance means outside.</p>

---

## Post #21 by @FatihSogukpinar (2020-09-18 20:26 UTC)

<p>Hi again,<br>
I have a few questions about this :<br>
See this example in the script repository:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_segments_visible_at_a_selected_position" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_segments_visible_at_a_selected_position </a></p>
<ol>
<li>
</li></ol>
<p>When I run this script, I got the error:</p>
<p>AttributeError: ‘NoneType’ object has no attribute ‘AddObserver’</p>
<p>(In line: markupsFiducialNode.AddObserver(slicer.vtkMRMLMarkupsPlaneNode.PointModifiedEvent, printSegmentNames)<br>
How can we solve this error ?</p>
<ol start="2">
<li>Assume that some of the segmentations are visible in the current segment, but are visible in different anterior/posterior positions. Can this script find those segments ? Ie., I need to do this in 3D coordinates, not just in one slice.</li>
</ol>
<p>Thank you so much.</p>

---

## Post #22 by @lassoan (2020-09-19 15:01 UTC)

<p>You need to place a markups fiducial point before you run the script.</p>

---

## Post #23 by @FatihSogukpinar (2020-09-19 20:56 UTC)

<p>I already have them, but I am still getting the same error.</p>

---

## Post #24 by @lassoan (2020-09-19 20:59 UTC)

<p>Do you use latest Slicer Preview Release?</p>

---

## Post #25 by @FatihSogukpinar (2020-09-19 21:01 UTC)

<p>I am using Slicer 4.11. Should I switch to 4.10 ?</p>

---

## Post #26 by @lassoan (2020-09-19 21:05 UTC)

<p>Latest Slicer-4.11 should work well.</p>
<p>This line sets the first markups fiducial node in the scene in variable <code>markupsFiducialNode</code>:</p>
<pre><code>markupsFiducialNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLMarkupsFiducialNode")
</code></pre>
<p>If you get an error that <code>markupsFiducialNode</code> is <code>None</code> then it means that there is no markups fiducial node in your scene, so you need to add one. Can you post a screenshot of your Slicer application window?</p>

---

## Post #27 by @FatihSogukpinar (2020-09-19 21:28 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="26" data-topic="13407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>t of your Slicer application window?</p>
</blockquote>
</aside>
<p>I think I found the problem, by your help.<br>
But I have another question : I have several different fiducial files. How can I modify</p>
<pre><code class="lang-auto">markupsFiducialNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLMarkupsFiducialNode")
</code></pre>
<p>to pick the one that I need to use ?</p>
<p>Thanks.</p>

---

## Post #28 by @lassoan (2020-09-19 21:30 UTC)

<p>Complete this programming tutorial to learn about basics of Python scripting in Slicer: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials</a></p>

---

## Post #29 by @FatihSogukpinar (2020-09-19 21:59 UTC)

<p>OK I also solved it.</p>
<p>So the last thing : I need to check the segments in all slices, not just in one. It seems like this script is missing the segments which are not visible in the current slice.<br>
Is it possible to loop over all slices so that segments of different slices are also covered ?</p>
<p>Thanks.</p>

---

## Post #30 by @lassoan (2020-09-20 02:01 UTC)

<p>If you show the binary labelmap representation in the slice view then you should be able to get all segments.</p>
<p>You can also use vtkMRMLSegmentationsDisplayableManager3D’s Pick3D method, and then get GetPickedNodeID and GetPickedSegmentID to get the picked node and segment, but these only return the first hit.</p>

---

## Post #31 by @FatihSogukpinar (2020-09-20 06:35 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="30" data-topic="13407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>vtkMRMLSegmentationsDisplayableManager3D’s</p>
</blockquote>
</aside>
<p>I have many segments and I don’t think I can make all of them visible in just one slice… Any suggestions about that ?</p>
<p>I couldn’t find an example for using   vtkMRMLSegmentationsDisplayableManager3D. I am trying :<br>
sliceViewWidget = slicer.app.layoutManager().sliceWidget(sliceViewLabel)<br>
segmentationsDisplayableManager = sliceViewWidget.sliceView().displayableManagerByClassName(‘vtkMRMLSegmentationsDisplayableManager3D’)</p>
<p>But segmentationsDisplayableManager is returned as None.</p>

---

## Post #32 by @lassoan (2020-09-20 15:43 UTC)

<p>Individual segments don’t have to be visible in that slice view, just the segmentation overall. Again, it is important to set the visible representation to binary labelmap.</p>
<p>If you want to try 3D displayable manager then retrieve that from a 3D view.</p>

---
