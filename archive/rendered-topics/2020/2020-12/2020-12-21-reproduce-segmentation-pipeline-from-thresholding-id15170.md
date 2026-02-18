# Reproduce Segmentation Pipeline from thresholding

**Topic ID**: 15170
**Date**: 2020-12-21
**URL**: https://discourse.slicer.org/t/reproduce-segmentation-pipeline-from-thresholding/15170

---

## Post #1 by @Optimox (2020-12-21 16:13 UTC)

<p>Hi,</p>
<p>I am currently using 3DSlicer to visualize segmentations coming from another framework.</p>
<p>Here is my pipeline:</p>
<ul>
<li>load a 3D tiff, that contains segmentation by voxels, i.e all voxels with value equals to 10 represents the same segmentation object for example. My segmentations are 3D surfaces.</li>
<li>Go to segment editor and create the segmentation using the Threshold button</li>
<li>Then I can visualize and export my segmentations in stl format</li>
</ul>
<p>I’m very happy with the results but would like to apply this process with python (ideally outside 3DSlicer). I’m having a hard time understanding what is the exact process happening inside 3DSlicer.</p>
<p>Could someone help me/ point to me the exact algorithm used for:</p>
<ul>
<li>defining the normals</li>
<li>defining the triangles</li>
<li>avoid mesh to have holes in it or bubbles</li>
</ul>
<p>Here is the nice result I get with 3Dslicer:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc9270b14f789be727393ac6f7e9ee9c98068631.jpeg" data-download-href="/uploads/short-url/vtgMZuVbJVbzOPjNHoLBzbgXig1.jpeg?dl=1" title="slicer_result" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dc9270b14f789be727393ac6f7e9ee9c98068631_2_496x500.jpeg" alt="slicer_result" data-base62-sha1="vtgMZuVbJVbzOPjNHoLBzbgXig1" width="496" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dc9270b14f789be727393ac6f7e9ee9c98068631_2_496x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dc9270b14f789be727393ac6f7e9ee9c98068631_2_744x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc9270b14f789be727393ac6f7e9ee9c98068631.jpeg 2x" data-dominant-color="232F23"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_result</span><span class="informations">763×768 70.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>And here is the uglier result I get with my current pipeline:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3ac1033bc750338e5ae9037d93b7815f2665cd11.jpeg" data-download-href="/uploads/short-url/8nLdHikbIKHphdAliJsjCCCNaV3.jpeg?dl=1" title="my_result" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ac1033bc750338e5ae9037d93b7815f2665cd11_2_620x500.jpeg" alt="my_result" data-base62-sha1="8nLdHikbIKHphdAliJsjCCCNaV3" width="620" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ac1033bc750338e5ae9037d93b7815f2665cd11_2_620x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3ac1033bc750338e5ae9037d93b7815f2665cd11.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3ac1033bc750338e5ae9037d93b7815f2665cd11.jpeg 2x" data-dominant-color="6D6D6E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">my_result</span><span class="informations">914×736 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>My current pipeline consists in:</p>
<ul>
<li>creating a point cloud from the point I would use inside the Threshold with 3DSlicer</li>
<li>inferring the normal</li>
<li>creating the mesh using Poisson algorithm</li>
<li>cropping boarders outside initial point cloud</li>
</ul>
<pre><code class="lang-auto">pcd = o3d.geometry.PointCloud()
positions = np.argwhere(original_image==10)
scaling = np.array(original_image.shape)
final_scale = scaling / np.max(scaling)
normalized_position = (2*(positions / scaling) - 1)*final_scale
normalized_position[:,[0,2]] = normalized_position[:,[2,0]]

pcd.points = o3d.utility.Vector3dVector(normalized_position)

distances = pcd.compute_nearest_neighbor_distance()
avg_dist = np.mean(distances)
radius = 3 * avg_dist

pcd.estimate_normals(search_param = o3d.geometry.KDTreeSearchParamHybrid(radius = radius, max_nn = 10))
poisson_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=10, width=0, scale=1.1, linear_fit=True)[0]

poisson_mesh.compute_triangle_normals()
bbox = pcd.get_axis_aligned_bounding_box()
p_mesh_crop = poisson_mesh.crop(bbox)
</code></pre>
<p>What am I missing here? Could someone help me understand what’s the exact pipeline that 3DSlicer is doing?</p>
<p>Thank you very much in advance for your help.</p>
<p>Best</p>

---

## Post #2 by @lassoan (2020-12-21 18:28 UTC)

<aside class="quote no-group" data-username="Optimox" data-post="1" data-topic="15170">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/optimox/48/9288_2.png" class="avatar"> Optimox:</div>
<blockquote>
<p>I’m very happy with the results but would like to apply this process with python (ideally outside 3DSlicer)</p>
</blockquote>
</aside>
<p>If you would like to reimplement the pipeline outside 3D Slicer then have a look at the source code and take whatever you need, it is all open and freely usable. The most relevant parts are here: <a href="https://github.com/Slicer/Slicer/tree/master/Libs/vtkSegmentationCore" class="inline-onebox">Slicer/Libs/vtkSegmentationCore at main · Slicer/Slicer · GitHub</a></p>
<p>We use VTK for all segmentation processing operations, so you may find <a href="https://kitware.github.io/vtk-examples/site/">VTK examples site</a> useful.</p>

---

## Post #3 by @Optimox (2020-12-21 19:10 UTC)

<p>Yes thank you, I know in the end I’ll have to deep dive into the source code.</p>
<p>As I’m new to this I wanted to understand 3DSlicer approach and what makes it much nicer at first sight.</p>
<p>Is there a specific post-processing which smoothes things and make sure that no ‘bubbles’ will appear in the final segmentation? no holes? Is there some sort of outliers removal from point cloud or something like this?</p>
<p>Does it seem a common problem to have artefacts like the ones I have and what makes the result so different than the one from Slicer?</p>
<p>Again, thank you for pointing me the right folder to dig further, but I would really appreciate a general understanding of the differences between my basic pipeline and the one used in 3DSlicer and why?</p>
<p>Really appreciate your support.</p>

---

## Post #4 by @lassoan (2020-12-21 19:40 UTC)

<aside class="quote no-group" data-username="Optimox" data-post="3" data-topic="15170">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/optimox/48/9288_2.png" class="avatar"> Optimox:</div>
<blockquote>
<p>Is there some sort of outliers removal from point cloud or something like this?</p>
</blockquote>
</aside>
<p>We represent segmentation as a structured rectilinear grid (volume of voxels), not as a point cloud.</p>
<p>I would recommend to use VTK instead of Open3D. Open3D makes you think that it is some large, mature library developed by Intel for processing any kind of 3D data, but in reality it is a small library primarily developed by a single person in a university research lab (with a few other active contributors), which does a good job in surface reconstruction and alignment. It is not a general 3D processing framework and it is not well positioned to become one.</p>
<aside class="quote no-group" data-username="Optimox" data-post="3" data-topic="15170">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/optimox/48/9288_2.png" class="avatar"> Optimox:</div>
<blockquote>
<p>I would really appreciate a general understanding of the differences between my basic pipeline and the one used in 3DSlicer and why?</p>
</blockquote>
</aside>
<p>If you want to implement and maintain your own pipeline outside Slicer then you need to develop a full understanding of all algorithms involved. You can read the source code or use a debugger to step through and inspect everything in Slicer and use VTK library’s excellent resources (examples site, textbook, API documentation) to learn more. I can see that we could assist you in this learning process, but I find it hard to justify this time investment as you are not expected to become a Slicer user or developer. Maybe others can help you out here or in the <a href="https://www.vtk.org">VTK forum</a>, or you can get paid support from <a href="https://slicer.readthedocs.io/en/latest/user_guide/about.html#commercial-partners">Slicer commercial partners</a>.</p>

---

## Post #5 by @Optimox (2020-12-21 22:23 UTC)

<p>Sir,</p>
<p>Thank you for your advice and suggestions, they will definitely be useful in the right choice of framework.</p>
<p>Thank you also for taking the time to give me this answer.</p>
<p>As per the justification of time investment, I’ve seen you answering enough questions on this forum to be sure that you know about the joy of learning, teaching and sharing. That you know about the beauty of open source projects and the magnificence of serendipity. I’ve started to pay back my debt to the open source community myself, one brick at a time. Who knows maybe one day I’ll have something to give to 3DSlicer.</p>
<p>But for the moment, I have plenty of readings and work to do to reach that point! Please be sure that your help is much appreciated and that your time is well invested when helping people getting better.</p>
<p>Congratulations for the job accomplished already.</p>
<p>Bests,</p>
<p>Seb</p>

---
