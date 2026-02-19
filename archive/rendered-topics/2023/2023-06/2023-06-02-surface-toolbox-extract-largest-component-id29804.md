---
topic_id: 29804
title: "Surface Toolbox Extract Largest Component"
date: 2023-06-02
url: https://discourse.slicer.org/t/29804
---

# Surface toolbox - Extract largest component

**Topic ID**: 29804
**Date**: 2023-06-02
**URL**: https://discourse.slicer.org/t/surface-toolbox-extract-largest-component/29804

---

## Post #1 by @S_Motch_Perrine (2023-06-02 14:53 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 5.2.1 r31317<br>
Expected behavior: Extract largest component of skull<br>
Actual behavior: The model is performing as expected but I would actually like to extract the SECOND and THIRD largest components. Is there a way to do this, or to extract multiple large components, say the top 10 or 50 or whatever number is desired?<br>
The input data is a .ply file of an adult mouse skull. I was hoping to use the Surface Toolbox to extract what are essentially three large components - the neurocranium and the left and right hemi-mandibles. I want to work specifically with the (separated) left and right hemi-mandibles, which are the second and third largest components. I thought this tool would be fastest for a series with a large number of specimens. If I should use a different tool, or if there is a way to adjust the settings for the Surface toolbox, please let me know. Thank you!</p>

---

## Post #2 by @muratmaga (2023-06-02 16:13 UTC)

<p><a class="mention" href="/u/s_motch_perrine">@S_Motch_Perrine</a><br>
What you ask is normally done during the segmentation process. If you still have the segmentation of these models, you can run the island effect and instead of the default “keep largest component” choose “split islands to segments”. If they are not touching each other, then you should get three separate segments, and export models from there. Also this thread might be useful to deal with touching voxels. <a href="https://discourse.slicer.org/t/how-can-i-approximate-the-magic-wand-tool-in-avizo-amira/29611/4" class="inline-onebox">How can I approximate the magic wand tool in Avizo/Amira? - #4 by muratmaga</a></p>
<p>If you do not have the segmentation, but only the models you have couple options.</p>
<ol>
<li>
<p>I don’t think surface toolbox has the split islands mode exposed in the UI, but it might possibly be available as a python script (someone more knowledgable needs to comment <a class="mention" href="/u/pieper">@pieper</a> ?)</p>
</li>
<li>
<p>You can import/convert the models as segmentation then use the segment editor effects (such as island and scissors) to separate them and re-export as model. This might cause some loss of detail, as ideally this operation should be done as I described above. To give a try, right click on your models object in the data viewer, and choose “export to model to segmentation node”.</p>
</li>
<li>
<p>You might give “Dynamic Modeler” module a try, and experiment with separating the models with drawing closed curves around them.</p>
</li>
</ol>

---

## Post #3 by @S_Motch_Perrine (2023-06-02 19:40 UTC)

<p>Thank you, <a class="mention" href="/u/muratmaga">@muratmaga</a> ! I do not have the segmentation, only the models, so I will try your suggestions and thanks for tagging Pieper.</p>

---

## Post #4 by @pieper (2023-06-03 14:18 UTC)

<p>The Surface Toolbox code uses a very flexible VTK filter but only the basic functionality is exposed in the GUI.  If you are solving a one-off problem writing a short  custom python script is probably best.  If anyone feels motivated, it would be possible to expose more features of the filter in the Surface Toolbox GUI by adding <a href="https://github.com/Slicer/SlicerSurfaceToolbox/blob/master/SurfaceToolbox/SurfaceToolbox.py#L55-L147">more parameter widgets</a>.</p>
<p><a href="https://vtk.org/doc/nightly/html/classvtkPolyDataConnectivityFilter.html#details" class="onebox" target="_blank" rel="noopener">https://vtk.org/doc/nightly/html/classvtkPolyDataConnectivityFilter.html#details</a></p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerSurfaceToolbox/blob/master/SurfaceToolbox/SurfaceToolbox.py#L548-L555">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerSurfaceToolbox/blob/master/SurfaceToolbox/SurfaceToolbox.py#L548-L555" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerSurfaceToolbox/blob/master/SurfaceToolbox/SurfaceToolbox.py#L548-L555" target="_blank" rel="noopener">Slicer/SlicerSurfaceToolbox/blob/master/SurfaceToolbox/SurfaceToolbox.py#L548-L555</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="548" style="counter-reset: li-counter 547 ;">
          <li>def extractLargestConnectedComponent(inputModel, outputModel):
</li>
          <li>  """Extract the largest connected portion of a surface model.
</li>
          <li>  """
</li>
          <li>  connect = vtk.vtkPolyDataConnectivityFilter()
</li>
          <li>  connect.SetInputData(inputModel.GetPolyData())
</li>
          <li>  connect.SetExtractionModeToLargestRegion()
</li>
          <li>  connect.Update()
</li>
          <li>  outputModel.SetAndObservePolyData(connect.GetOutput())
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @tsehrhardt (2023-06-07 12:11 UTC)

<p>If the parts are not connected in your ply model, there is a filter in Meshlab called “Split in Connected Components” that you can apply by right-clicking on your model name. The first new layer (“CC0”) is the largest and the rest mostly are sorted by size but not necessarily. If your mesh contains many many parts like floaties, the program might crash.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d08aa699d73a048cfbd55eab747fcb31bf643ce7.jpeg" data-download-href="/uploads/short-url/tKQn39Zd2BUP2hGkNGYvVaseGCX.jpeg?dl=1" title="2023-06-07_8-08-46" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d08aa699d73a048cfbd55eab747fcb31bf643ce7_2_338x500.jpeg" alt="2023-06-07_8-08-46" data-base62-sha1="tKQn39Zd2BUP2hGkNGYvVaseGCX" width="338" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d08aa699d73a048cfbd55eab747fcb31bf643ce7_2_338x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d08aa699d73a048cfbd55eab747fcb31bf643ce7_2_507x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d08aa699d73a048cfbd55eab747fcb31bf643ce7_2_676x1000.jpeg 2x" data-dominant-color="ECEDEE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-06-07_8-08-46</span><span class="informations">704×1040 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @MarkusHeller (2023-06-07 14:24 UTC)

<p>As indicated before, such functionality is available in VTK and thus accessible in slicer but also in other geometry processing libraries which may/may not build on VTK.</p>
<p>A little Python script using vedo could likely do the job.</p>
<p><a href="https://vedo.embl.es/docs/vedo.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://vedo.embl.es/docs/vedo.html</a></p>
<p>split mesh in connected components:<br>
<a href="https://vedo.embl.es/docs/vedo/mesh.html#Mesh.split" class="onebox" target="_blank" rel="noopener nofollow ugc">https://vedo.embl.es/docs/vedo/mesh.html#Mesh.split</a></p><aside class="onebox githubblob" data-onebox-src="https://github.com/marcomusy/vedo/blob/master/examples/advanced/splitmesh.py">
  <header class="source">

      <a href="https://github.com/marcomusy/vedo/blob/master/examples/advanced/splitmesh.py" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/marcomusy/vedo/blob/master/examples/advanced/splitmesh.py" target="_blank" rel="noopener nofollow ugc">marcomusy/vedo/blob/master/examples/advanced/splitmesh.py</a></h4>


      <pre><code class="lang-py">"""Split a mesh by connectivity and
order the pieces by increasing surface area"""
from vedo import dataurl, Volume, show

em = Volume(dataurl+"embryo.tif").isosurface(80)

# return the list of the largest 10 connected meshes:
splitem = em.split(maxdepth=40)[0:9]

show(splitem, __doc__, axes=1, viewup='z').close()
</code></pre>




  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>extract just the largest connected component:<br>
<a href="https://vedo.embl.es/docs/vedo/mesh.html#Mesh.extract_largest_region" class="onebox" target="_blank" rel="noopener nofollow ugc">https://vedo.embl.es/docs/vedo/mesh.html#Mesh.extract_largest_region</a></p><aside class="onebox githubblob" data-onebox-src="https://github.com/marcomusy/vedo/blob/master/examples/basic/largestregion.py">
  <header class="source">

      <a href="https://github.com/marcomusy/vedo/blob/master/examples/basic/largestregion.py" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/marcomusy/vedo/blob/master/examples/basic/largestregion.py" target="_blank" rel="noopener nofollow ugc">marcomusy/vedo/blob/master/examples/basic/largestregion.py</a></h4>


      <pre><code class="lang-py">"""Extract the mesh region that
has the largest connected surface"""
from vedo import dataurl, Volume, printc, Plotter

mesh1 = Volume(dataurl+"embryo.tif").isosurface(80).c("yellow")
printc("area1 =", mesh1.area(), c="yellow")

mesh2 = mesh1.extract_largest_region().color("lb")
printc("area2 =", mesh2.area(), c="lb")

plt = Plotter(shape=(2,1), axes=7)
plt.at(0).show(mesh1, __doc__)
plt.at(1).show(mesh2)
plt.interactive().close()
</code></pre>




  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Best wishes,</p>

---

## Post #7 by @S_Motch_Perrine (2023-06-07 16:09 UTC)

<p>Thanks, everyone! This has all been very helpful! I appreciate the time you took and the useful information provided. This is a very good community for learning.</p>

---
