# Get center of gravity of a segment

**Topic ID**: 4287
**Date**: 2018-10-04
**URL**: https://discourse.slicer.org/t/get-center-of-gravity-of-a-segment/4287

---

## Post #1 by @ThomPote (2018-10-04 16:49 UTC)

<p>Hi,</p>
<p><em>I’m new on 3Dslicer with a new project, I try to search on topics but I’m still in troubles.</em></p>
<p>I’m using segmentation from CT-scan to isolate 2 masses.<br>
I need you to know how I can have the gravity mass center. Can I have coordinates x/y/z ?<br>
Does it run with models ? volumes ?</p>
<p>Thanks for all</p>
<p><em>Sorry for the mistakes I don’t speak english very well</em></p>

---

## Post #2 by @brhoom (2018-10-04 17:36 UTC)

<p>use this code or something similar:</p>
<pre><code>   n = getNode('your node') 
   s = n.GetSegmentation()
  ss = s.GetSegment('Segment_7')
  pd = ss.GetRepresentation('Closed surface')
  com = vtk.vtkCenterOfMass()
  com.SetInputData(pd)
  com.Update()
  com.GetCenter()</code></pre>

---

## Post #3 by @ThomPote (2018-10-04 18:42 UTC)

<p>Thanks !</p>
<p>The problem I have is that :</p>
<p>With this line pd = ss.GetRepresentation(‘Closed surface’) it requires a Closed surface representation but when I segment my 2 masses with threshold (and split island) it works with binary labelmap.</p>
<p>How can I do ?</p>
<p>(So it’s good with painted segments, but not tresholded)</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2018-10-04 18:49 UTC)

<p>You can also use segmentation node’s <a href="http://apidocs.slicer.org/master/classvtkMRMLSegmentationNode.html#a84bcb732330fc5a8efe74ef851cfbedb">GetSegmentCenter</a> or <a href="http://apidocs.slicer.org/master/classvtkMRMLSegmentationNode.html#aba8915642b3966206ad88980db489922">GetSegmentCenterRAS</a> method. It works for both labelmap and closed surface representations. It is used for giving a position inside the segment (used when you right-click the segment and select “Jump slices”) and so it does not use center of gravity. If you need strictly center of gravity then you can have a look at the source code of this method and create a modified version.</p>

---

## Post #5 by @brhoom (2018-10-04 19:05 UTC)

<blockquote>
<p>it works with binary labelmap.</p>
</blockquote>
<p>You can convert from labelmap to segmentation node and vice versa using segmentations module.</p>

---

## Post #6 by @cpinter (2018-10-05 12:39 UTC)

<p>If you have trouble modifying the GetSegmentCenter function to get the center of mass, this might help. In this Slicer programming tutorial the center of mass of a labelmap is calculated in python:<br>
<a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx" class="onebox" target="_blank">https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx</a></p>

---

## Post #7 by @cpinter (2018-10-05 15:17 UTC)

<p>It just occurred to me that we changed the bootcamp task to center of mass of fiducials not labelmap. Here’s an older one with the labelmap code:<br>
<a href="https://www.dropbox.com/s/ee58jil89rw0qxd/20160504_SlicerProgramming_Pinter.pptx?dl=0">https://www.dropbox.com/s/ee58jil89rw0qxd/20160504_SlicerProgramming_Pinter.pptx?dl=0</a> (slide 28). I need to reimplement just this for a completely unrelated reason, so if you want a few hours I’ll link a C++ code that calculates center of mass for a segment’s labelmap.</p>

---

## Post #8 by @cpinter (2018-10-05 19:07 UTC)

<p>Here you go:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/Beams/MRML/vtkMRMLRTPlanNode.cxx#L790-L850" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/Beams/MRML/vtkMRMLRTPlanNode.cxx#L790-L850" target="_blank">SlicerRt/SlicerRT/blob/master/Beams/MRML/vtkMRMLRTPlanNode.cxx#L790-L850</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="790" style="counter-reset: li-counter 789 ;">
<li>bool vtkMRMLRTPlanNode::ComputeTargetVolumeCenter(double center[3])
</li>
<li>{
</li>
<li>center[0] = center[1] = center[2] = 0.0;
</li>
<li>
</li>
<li>if (!this-&gt;Scene)
</li>
<li>{
</li>
<li>  vtkErrorMacro("ComputeTargetVolumeCenter: Invalid MRML scene");
</li>
<li>  return false;
</li>
<li>}
</li>
<li>
</li>
<li>// Get a labelmap for the target
</li>
<li>vtkSmartPointer&lt;vtkOrientedImageData&gt; targetLabelmap = this-&gt;GetTargetOrientedImageData();
</li>
<li>if (targetLabelmap.GetPointer() == NULL)
</li>
<li>{
</li>
<li>  return false;
</li>
<li>}
</li>
<li>
</li>
<li>// Compute image center
</li>
<li>int extent[6] = {0,-1,0,-1,0,-1};
</li>
<li>targetLabelmap-&gt;GetExtent(extent);
</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/SlicerRt/SlicerRT/blob/master/Beams/MRML/vtkMRMLRTPlanNode.cxx#L790-L850" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #9 by @ThomPote (2018-10-07 11:12 UTC)

<p><strong>Thanks to everybody !</strong><br>
It’s now ok for me for center of gravity with your help !</p>
<p>Another question :</p>
<p>–&gt; Can I analyse surface points coordinates to compute the most distants points for visualizing some 2 or 3 largest diameters of the mass ?</p>

---

## Post #10 by @lassoan (2018-10-07 16:45 UTC)

<p>It would be more robust to compute principal axes from labelmap representation. You can then get diameters along those axes.</p>
<p>There may be ITK or VTK filters that can help. Let us know about your progress, we may give further help and we could integrate the final solution to Segment Statistics module.</p>

---

## Post #11 by @brhoom (2018-10-12 14:07 UTC)

<p><strong>Related question:</strong></p>
<p>how can I change the origin of a model to the center of mass?</p>
<p>I found  two useful functions GetBounds and GetMesh().GetCenter() . I  think the origin is stored in the minimum values  Xmin,Ymin and Zmin. The problem I can not find something like model.SetBounds. Here is the idea:</p>
<pre><code>                 bounds =[0]*6
                 model.GetBounds(bounds)
                 center = model.GetMesh().GetCenter() 
                 bounds [0] = center[0] 
                 bounds [2 ]= center[1]
                 bounds [4] = center[2]
                #model.SetBounds(bounds)</code></pre>

---

## Post #12 by @lassoan (2018-10-12 18:14 UTC)

<aside class="quote no-group" data-username="brhoom" data-post="11" data-topic="4287">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>how can I change the origin of a model to the center of mass?</p>
</blockquote>
</aside>
<p>See this post: <a href="https://discourse.slicer.org/t/how-to-display-and-move-the-origin-coordinates-of-the-surface-model-stl/3329/2" class="inline-onebox">How to display and move the origin coordinates of the surface model (.STL) - #2 by pieper</a></p>

---

## Post #13 by @brhoom (2018-10-12 19:32 UTC)

<p>I just found today that values are different when computing the center from a model e.g.:</p>
<pre><code> center = model.GetMesh().GetCenter()
 output: (-4.173086166381836, -155.35969924926758, -259.25328826904297)
</code></pre>
<p>and from computing the center using segment</p>
<pre><code> center = vtk.vtkCenterOfMass()
 center.SetInputData(pd)
 center.Update()
 center.GetCenter()
 output: (-4.462736238549897, -146.88848545865304, -257.3132177804882)         
</code></pre>
<p>Apparently, the second one is more accurate as I get the same value in Blender. Is there a way to get the same values using model?</p>

---

## Post #14 by @brhoom (2018-10-18 12:17 UTC)

<p><strong>Solved!</strong></p>
<p>It seems  I can get polydata from the model and use the second method e.g.</p>
<pre><code>pd= model.GetPolyData()
center = vtk.vtkCenterOfMass()
center.SetInputData(pd)
center.Update()
center.GetCenter()</code></pre>

---

## Post #15 by @lassoan (2018-10-18 14:30 UTC)

<p>You have many options to compute “center” of a segment.</p>
<ol>
<li>Model node’s GetMesh().GetCenter() method returns center of the bounding box. Depending on the model’s shape it may be close to the center of mass, but they are computed very differently.</li>
</ol>
<details>
<summary>
See method help</summary>
<pre><code>&gt;&gt;&gt; help(modelNode.GetMesh().GetCenter)
Help on built-in function GetCenter:

GetCenter(...)
    V.GetCenter() -&gt; (float, float, float)
    C++: double *GetCenter()
    V.GetCenter([float, float, float])
    C++: void GetCenter(double center[3])
    
    Get the center of the bounding box. THIS METHOD IS NOT THREAD
    SAFE.
</code></pre>
</details>
<ol start="2">
<li>
<p>vtk.vtkCenterOfMass() applied to a segment’s closed surface representation returns center of mass of the surface points. Depending on the shape and density of points on the surface, it may be similar to center of mass of the of the solid object enclosed by the surface, but they are not the same.</p>
</li>
<li>
<p>You can compute true center of mass of the enclosed volume from binary labelmap representation (as <a class="mention" href="/u/cpinter">@cpinter</a> described above).</p>
</li>
</ol>

---

## Post #16 by @brhoom (2018-10-18 14:45 UTC)

<p>Thanks for explaining!</p>

---

## Post #17 by @mangotee (2018-11-27 13:24 UTC)

<p>Thanks for asking this questions and for the answers, it helped me a lot. However, here’s a little note, in case someone else gets stuck like I did just now. I tried this code segment and this line:</p>
<blockquote>
<p>pd = ss.GetRepresentation(‘Closed surface’)</p>
</blockquote>
<p>returned a “None” for me. In this case, press “Show 3D” in the Segment Editor at least once, then the “Closed surface” representation gets calculated internally and this line returns a vtkPolyData object (a surface model) as expected. Alternatively, the calculation of this representation can also be triggered in code, via the following line (beware, I did not fully test whether the result makes sense and can be worked with further, I just checked whether pd is not None in the next line):</p>
<blockquote>
<p>ss.AddRepresentation(‘Closed surface’,vtk.vtkPolyData())</p>
</blockquote>
<p>Another tip: the following line assumes that the segment ID is known:</p>
<blockquote>
<p>ss = s.GetSegment(‘Segment_7’)</p>
</blockquote>
<p>If this ID is not known, the following line gets the segment by its Name, rather than by its ID:</p>
<blockquote>
<p>ss = s.GetSegment(s.GetSegmentIdBySegmentName(‘Calcified mass’))</p>
</blockquote>

---

## Post #18 by @cpinter (2018-11-27 17:08 UTC)

<aside class="quote no-group" data-username="mangotee" data-post="17" data-topic="4287">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c57346/48.png" class="avatar"> mangotee:</div>
<blockquote>
<p>ss.AddRepresentation(‘Closed surface’,vtk.vtkPolyData())</p>
</blockquote>
</aside>
<p>Please do not do this, it will result in inconsistent content in the segmentation object, and subsequent operations may yield unwanted results. This is how you can trigger conversion internally:</p>
<pre><code>s.CreateRepresentation(‘Closed surface’)
</code></pre>
<p>If you want to learn more about the infrastructure, then you can refer to the documentation:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations</a><br>
or the source code, which is <a href="https://github.com/Slicer/Slicer/blob/master/Libs/vtkSegmentationCore/vtkSegmentation.h#L43-L88">well commented</a>.</p>

---

## Post #19 by @lassoan (2018-11-28 06:36 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="18" data-topic="4287">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>s.CreateRepresentation(‘Closed surface’)</p>
</blockquote>
</aside>
<p>Or you can use <code>segmentationNode.CreateClosedSurfaceRepresentation()</code> convenience function.</p>

---

## Post #20 by @Saima (2020-11-25 03:51 UTC)

<p>Hi Andras,<br>
How can I get center of gravity or centriod position for each of these electrode positions. The dots are in one labelmap segmentation.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcfffe8352ad8f3b8ecc56c5cc223f8f729bbed6.png" alt="image" data-base62-sha1="A68MPs1SV720vCeFUbXVLNnjIWy" width="521" height="338"></p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #21 by @muratmaga (2020-11-25 16:52 UTC)

<p>Through the UI, you can import the labelmap as segmentation, turn them into individual segments using island tool, and then use the segment statistics module to get the centroids for each of those segments.</p>
<p>If you will do it more than once, scripting is probably the better approach.</p>

---

## Post #22 by @Saima (2020-11-27 04:40 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="21" data-topic="4287">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>d then use the segment statistics m</p>
</blockquote>
</aside>
<p>Hi muratmaga,<br>
I got the results like this</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f299eed5d0c30ab58579d08f4b26f98fb2137fb7.png" data-download-href="/uploads/short-url/yC9lysfvmZuTHeSvmKA3gf2vLSv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f299eed5d0c30ab58579d08f4b26f98fb2137fb7_2_690x195.png" alt="image" data-base62-sha1="yC9lysfvmZuTHeSvmKA3gf2vLSv" width="690" height="195" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f299eed5d0c30ab58579d08f4b26f98fb2137fb7_2_690x195.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f299eed5d0c30ab58579d08f4b26f98fb2137fb7_2_1035x292.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f299eed5d0c30ab58579d08f4b26f98fb2137fb7.png 2x" data-dominant-color="F0F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1057×300 49.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How can I get the position coordinates for each of the centroide of a segment and then replace it with a fiducial</p>
<p>thank you</p>
<p>regards,<br>
Saima safdar</p>

---

## Post #23 by @Saima (2020-11-27 05:14 UTC)

<p>Hi,<br>
Thanks I found the solution</p>

---

## Post #24 by @lassoan (2020-11-27 05:15 UTC)

<p>You can find a complete example of placing markups at segment centroids: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_centroid_of_each_segment">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_centroid_of_each_segment</a></p>
<p>Here is another example, which draws oriented bounding boxes around each segment: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_size.2C_position.2C_and_orientation_of_each_segment">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_size.2C_position.2C_and_orientation_of_each_segment</a></p>

---

## Post #25 by @Saima (2020-11-27 06:42 UTC)

<p>Hi Andras,<br>
The electrodes which I extracted now I can represent them with fiducials.</p>
<p>is there a way to project these fiducials onto the brain cortical surface on the T1 MRI? I need to calculate the distance between the projected and actual electrode positions in CT scan.</p>
<p>Any idea how can I get? Can I use the nearest neighbour to find cells  on brain and then get cell centroid and convert to fiducials or is there a better way of projecting onto brain surface.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #26 by @lassoan (2020-11-27 06:49 UTC)

<p>Projection to a curved surface is not a well-defined operation: it can be done many different ways, with slightly different results.</p>
<p>Can you post a few screenshots that show where the electrode positions are, how the cortical surface looks like, and where do you think they should be projected to?</p>

---

## Post #27 by @Saima (2020-12-01 05:44 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="26" data-topic="4287">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>n you post a few screenshots that show where the electrode positi</p>
</blockquote>
</aside>
<p>Hi andras,<br>
I am attaching the screen shot.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca96bd66c9547879679be2db08c42493743162b9.png" alt="image" data-base62-sha1="sUbph4XHVdrHgSl6tjLpZh40YNb" width="445" height="309"></p>
<p>How can I project to surface. The electrodes shown in red are segmented from CT and shown with fiducials</p>

---

## Post #28 by @Saima (2020-12-03 05:11 UTC)

<p>Hi andras,<br>
I need to go for an algorithm that can dynamically picks surface triangles with respect to the electrodes identified from ct of the same patient. I need to do it for multiple patients.</p>
<p>Is there anything I can do to do this automatically.</p>
<p>I need to calculated the displacements of the cells of the brain done during craniotomy and through placing these electrodes.</p>
<p>Thank you</p>

---

## Post #29 by @lassoan (2020-12-04 06:09 UTC)

<p>You can get the closest surface point or cell to a markup point as it is shown in these examples:</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Select_cells_of_a_model_using_markups_fiducial_points">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Select_cells_of_a_model_using_markups_fiducial_points</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Measure_distance_of_points_from_surface">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Measure_distance_of_points_from_surface</a></li>
</ul>

---

## Post #30 by @Saima (2020-12-16 04:54 UTC)

<p>Hi Andras,<br>
I got the selected cells of the model. It is possible to get the centroid for each selected cell.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #31 by @Saima (2020-12-16 05:29 UTC)

<p>Hi Andras,<br>
I got it. I got the cell point ids and from there I get three points and then averaging over x axis y axis and z axis. to get the centroid.</p>
<p>Many thanks</p>

---
