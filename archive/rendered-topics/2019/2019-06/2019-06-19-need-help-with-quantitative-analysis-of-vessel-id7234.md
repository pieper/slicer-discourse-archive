# Need help with quantitative analysis of  vessel

**Topic ID**: 7234
**Date**: 2019-06-19
**URL**: https://discourse.slicer.org/t/need-help-with-quantitative-analysis-of-vessel/7234

---

## Post #1 by @Roni (2019-06-19 11:39 UTC)

<p>Hi there,</p>
<p>I am new o the community. My clinical problem trying to solve is: Calculate vessel diameter/radius at each volume. I have done the follwoing:</p>
<ol>
<li>load my volume</li>
<li>generated label map with only vessel of interest and croped both the volume and label map</li>
<li>generated a vessel shape with “Model Maker”</li>
<li>used VMTK centerline module to create centerline.</li>
<li>Also used Extract skeleton to get the 1D centerline points (just to double check)</li>
</ol>
<p>Problems:</p>
<ol>
<li>Which information to use and how to export in a format that will be useful for further radius calculation in MATLAB?</li>
<li>I found the following tutorial about VMTK module, in the older version there was possibility to export centerline data as .dat format. However, in the newer module installed by extention wizard of slicer version 4.10.2, i do not see the option to export data to “.dat” file</li>
</ol>
<p><a>https://na-mic.org/w/images/4/40/TutorialVMTKCoronariesCenterlinesMRI_Winter2010AHM.pdf</a></p>
<ol start="3">
<li>
<p>After installtion of the latest  VMTK  module, Vessel Enhancement sub module is missing. So i can’t follow the tutorial mentioned in the link completely.</p>
</li>
<li>
<p>Apart from the approach of exporting data and using it in MATLAB, is there a way in 3D Slicer, that i could directly see the information about, at each centerline point the radius i used?</p>
</li>
</ol>
<p>Your valuable hep is appericiated very much.<br>
Thanks!<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b5ba2186bc874f284dab1817a4a7b44e5ff3169.png" data-download-href="/uploads/short-url/8t6uCKak6JCIo4JPUFlIMxALyhr.png?dl=1" title="vessel_with_centerline_VMTK" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b5ba2186bc874f284dab1817a4a7b44e5ff3169_2_690x471.png" alt="vessel_with_centerline_VMTK" data-base62-sha1="8t6uCKak6JCIo4JPUFlIMxALyhr" width="690" height="471" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b5ba2186bc874f284dab1817a4a7b44e5ff3169_2_690x471.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b5ba2186bc874f284dab1817a4a7b44e5ff3169_2_1035x706.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b5ba2186bc874f284dab1817a4a7b44e5ff3169.png 2x" data-dominant-color="9A9CD2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">vessel_with_centerline_VMTK</span><span class="informations">1316×899 35 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-06-19 15:05 UTC)

<p>VMTK module’s centerline directly provides radius measurement at each centerline points. You can copy-paste this code snippet into Slicer’s Python console to get each point’s position and radius at that position.</p>
<pre><code class="lang-python">c = getNode('CenterlineComputationModel')
points = slicer.util.arrayFromModelPoints(c)
radii = slicer.util.arrayFromModelPointData(c, 'Radius')
for i, radius in enumerate(radii):
  print("Point {0}: position={1}, radius={2}".format(i, points[i], radius))
</code></pre>

---

## Post #3 by @Roni (2019-06-28 18:10 UTC)

<p>Dear Andras,</p>
<p>Thank you very much for the reply. This was perfact. I have a couple of followup question…</p>
<ol>
<li>
<p>Is the radius mentioned in the model same as the distance shown (voronoimodel overlayed on labelmap) in fig 1 of this post ?</p>
</li>
<li>
<p>I want to overlay the sphere or circle with the found radius and display its overlayed shape boundary with red color on to the main vessel model (as shown in fig1 of the thread)  Can i visualise the overlayed sphere at each point?</p>
</li>
<li>
<p>How can i see properties/variables defined inside a model?<br>
e.g.<br>
when i type the following</p>
</li>
</ol>
<pre><code class="lang-auto">&gt;&gt;&gt; c = getNode('CenterlineComputationModel')
&gt;&gt;&gt; c
</code></pre>
<p>i could see the <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07bd4ee9e302231bdd33ffb041a9718b1a1e0bc1.png" data-download-href="/uploads/short-url/16sVRQeZOxyIMaIF3AVeDO5sgr7.png?dl=1" title="labelmap_voronoimodel" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07bd4ee9e302231bdd33ffb041a9718b1a1e0bc1_2_690x380.png" alt="labelmap_voronoimodel" data-base62-sha1="16sVRQeZOxyIMaIF3AVeDO5sgr7" width="690" height="380" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07bd4ee9e302231bdd33ffb041a9718b1a1e0bc1_2_690x380.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07bd4ee9e302231bdd33ffb041a9718b1a1e0bc1_2_1035x570.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07bd4ee9e302231bdd33ffb041a9718b1a1e0bc1.png 2x" data-dominant-color="050302"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">labelmap_voronoimodel</span><span class="informations">1280×706 6.58 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> properties after typing “c” in python interactor. However, When i want to look at the properties/variables in “Voronoi” model after typing</p>
<pre><code class="lang-auto">&gt;&gt;&gt; c = getNode('VoronoiModel')
&gt;&gt;&gt; c
(MRMLCorePython.vtkMRMLModelNode)000001940CAAC588
</code></pre>
<p>i only get that message and i could not expand the model with it’s properties.</p>

---

## Post #4 by @lassoan (2019-06-28 22:42 UTC)

<aside class="quote no-group" data-username="Roni" data-post="3" data-topic="7234">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/eada6e/48.png" class="avatar"> Roni:</div>
<blockquote>
<p>Is the radius mentioned in the model same as the distance shown (voronoimodel overlayed on labelmap) in fig 1 of this post ?</p>
</blockquote>
</aside>
<p>Yes.</p>
<aside class="quote no-group" data-username="Roni" data-post="3" data-topic="7234">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/eada6e/48.png" class="avatar"> Roni:</div>
<blockquote>
<p>want to overlay the sphere or circle with the found radius and display its overlayed shape boundary with red color on to the main vessel model (as shown in fig1 of the thread) Can i visualise the overlayed sphere at each point?</p>
</blockquote>
</aside>
<p>Yes. You can generate the spheres using VTK glyph filter. Choose to scale the spheres using the “Radius” array. Create a model node from the filter output using <code>slicer.modules.models.logic().AddModel()</code>. See details and examples in Slicer programming tutorials. [quote=“Roni, post:3, topic:7234”]<br>
How can i see properties/variables defined inside a model?<br>
[/quote]</p>
<p>Data associated with points and cells of a model are listed on Models module / Display / Scalars section.</p>

---

## Post #5 by @Roni (2019-07-08 09:15 UTC)

<p>Hi Andras,</p>
<p>Thanks for the reply. I tried to implement what you suggested. However, unsccessful. So i searched online and found ur reply to similar post. Here is the link :<a href="http://massmail.spl.harvard.edu/public-archives/slicer-devel/2015/038673.html" rel="nofollow noopener">Old reply to create glyph</a>.</p>
<p>Based on your recommendation, i tried to combine your 2 replies, however, i got an error in line (4).</p>
<p>The words after % sign suggest my understanding of the lines. Would it be possible for you to please confirm if the steps are correct? and also my understanding of them?</p>
<pre><code>`c=getNode('CenterlineComputationModel_1')`                             % Get the modelnode
     points = slicer.util.arrayFromModelPoints(c)
     radii = slicer.util.arrayFromModelPointData(c,'Radius')              % Get radius

 slicer.module.createmodels.logic().CreateSphere(radii)         %create pheremodel with radius array
 modelNode = slicer.util.getNode('SphereModel')                    % get node of the model
 glyph3D = vtk.vtkGlyph3D()                                                   % create glyph node
 glyph3D.SetInputConection(modelNode.GetPolyDataConnection())           % set the input connection from 'Spheremodel node'

 arrowSource = vtk.vtkArrowSource()                    % create arrowsource
 glyph3D.SetSourceConnection(arrowSource.GetOutputPort())  %   No idea for what
 glyph3D.SetVectorModeToUseNormal()                                       % no idea why it is used
 glyph3D.SetScaleFactor(radii)                                                   % scling with radius array
 glyph3D.Update()                                                                       % update
 modelNode.SetAndObservePolyData(glyph3D.GetOutput())  % you get the output
</code></pre>
<p>I am not sure where and how should i use the line<br>
<code>slicer.modules.models.logic().AddModel()</code>     in my code to get the final result.</p>
<p>Your help is very much helpful for me to proceed further. Thanks for your time and help.</p>

---

## Post #6 by @lassoan (2019-07-09 03:59 UTC)

<p><code>slicer.modules.models.logic().AddModel()</code> requires a vtkPolyData object or a filter output connection that produces vtkPolyData. This is exactly what centerline computation module provides.</p>
<p>If you want to create a tube model from the points and radii then use feed the centerline computation module output into a vtkTubeFilter, if you want to show the points as spheres then use vtkGlyph3D filter. You can configure both filters to change radius based on a chosen point data array.</p>
<p>If you do not need to modify point positions or radii then there is no need to use numpy (do not call slicer.util.arrayFrom…), just use VTK filters.</p>

---

## Post #7 by @lassoan (2019-07-13 23:55 UTC)

<p>A post was split to a new topic: <a href="/t/display-fibers-as-tube-with-non-uniform-radius/7562">Display fibers as tube with non-uniform radius</a></p>

---
