---
topic_id: 44008
title: "Are There Any Extensions For Filling Large Holes On Surface"
date: 2025-08-07
url: https://discourse.slicer.org/t/44008
---

# Are there any extensions for filling large holes on surface models for conversion to segments?

**Topic ID**: 44008
**Date**: 2025-08-07
**URL**: https://discourse.slicer.org/t/are-there-any-extensions-for-filling-large-holes-on-surface-models-for-conversion-to-segments/44008

---

## Post #1 by @ZackA (2025-08-07 18:55 UTC)

<p>Hello,</p>
<p>I am attempting to compare some laser scans I took of bone samples to manual segmentations from MRI scans for my research. The scans are stl files and contain holes in the surface shell due to limitations of the laser scanner (see photos below).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae9e8dba3fd6b969dd6bc6a1a599f66a6551d016.jpeg" data-download-href="/uploads/short-url/oUKMk7MT42snsw4f1LEjZIR9imO.jpeg?dl=1" title="BoneScansExample" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae9e8dba3fd6b969dd6bc6a1a599f66a6551d016_2_345x202.jpeg" alt="BoneScansExample" data-base62-sha1="oUKMk7MT42snsw4f1LEjZIR9imO" width="345" height="202" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae9e8dba3fd6b969dd6bc6a1a599f66a6551d016_2_345x202.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae9e8dba3fd6b969dd6bc6a1a599f66a6551d016_2_517x303.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae9e8dba3fd6b969dd6bc6a1a599f66a6551d016_2_690x404.jpeg 2x" data-dominant-color="9B9DB4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">BoneScansExample</span><span class="informations">1366×803 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3137d7b9a0a6023ad0fc7f010b512248d3f1cc6.jpeg" data-download-href="/uploads/short-url/ngDAhpleo1LQ93Ws22YkZjmUxrU.jpeg?dl=1" title="BoneScansExample2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3137d7b9a0a6023ad0fc7f010b512248d3f1cc6_2_345x202.jpeg" alt="BoneScansExample2" data-base62-sha1="ngDAhpleo1LQ93Ws22YkZjmUxrU" width="345" height="202" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3137d7b9a0a6023ad0fc7f010b512248d3f1cc6_2_345x202.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3137d7b9a0a6023ad0fc7f010b512248d3f1cc6_2_517x303.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3137d7b9a0a6023ad0fc7f010b512248d3f1cc6_2_690x404.jpeg 2x" data-dominant-color="9D9FB6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">BoneScansExample2</span><span class="informations">1366×803 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As a result, converting the scans to segments using the typical “Convert Model to Segmentation Node” option leads to really weird segments that are not useable (also see photo below).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10825645ce788e993a0a9225e5c6132ca0fe3621.jpeg" data-download-href="/uploads/short-url/2m2SSY2mS25TSf5zr8P1ADGySS5.jpeg?dl=1" title="BadSegmentExample" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10825645ce788e993a0a9225e5c6132ca0fe3621_2_345x210.jpeg" alt="BadSegmentExample" data-base62-sha1="2m2SSY2mS25TSf5zr8P1ADGySS5" width="345" height="210" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10825645ce788e993a0a9225e5c6132ca0fe3621_2_345x210.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10825645ce788e993a0a9225e5c6132ca0fe3621_2_517x315.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10825645ce788e993a0a9225e5c6132ca0fe3621_2_690x420.jpeg 2x" data-dominant-color="36342C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">BadSegmentExample</span><span class="informations">1366×834 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I assume the easiest way to fix this is to repair the holes in my scan and then convert the model node to a segment as usual. That said, I am having a little difficulty finding a module or extension with this capability. SurfaceToolbox Fill Holes function did not work for the large posterior holes and even seemed to invert the surface at points (blue model in the photo below). Is there an extension that can solve my issue, or am I better off filling holes in some other mesh editing software before importing to 3Dslicer?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37b0aec8d4f4f4eb457d9af5baf23f1b3b5898da.jpeg" data-download-href="/uploads/short-url/7WENIBamHxqRuZ3M9tmxK4RcJMm.jpeg?dl=1" title="SurfaceToolboxFillHolesResult" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37b0aec8d4f4f4eb457d9af5baf23f1b3b5898da_2_345x202.jpeg" alt="SurfaceToolboxFillHolesResult" data-base62-sha1="7WENIBamHxqRuZ3M9tmxK4RcJMm" width="345" height="202" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37b0aec8d4f4f4eb457d9af5baf23f1b3b5898da_2_345x202.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37b0aec8d4f4f4eb457d9af5baf23f1b3b5898da_2_517x303.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37b0aec8d4f4f4eb457d9af5baf23f1b3b5898da_2_690x404.jpeg 2x" data-dominant-color="7796B2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SurfaceToolboxFillHolesResult</span><span class="informations">1366×803 69.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Operating system: Windows 10<br>
Slicer version: 5.8.1</p>

---

## Post #2 by @mau_igna_06 (2025-08-07 19:10 UTC)

<p>You could try this filter:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://vtk.org/doc/nightly/html/classvtkSmoothPolyDataFilter.html#details">
  <header class="source">
      <img src="https://vtk.org/doc/nightly/html/vtk_favicon.png" class="site-icon" alt="" width="16" height="16">

      <a href="https://vtk.org/doc/nightly/html/classvtkSmoothPolyDataFilter.html#details" target="_blank" rel="noopener nofollow ugc">vtk.org</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://vtk.org/doc/nightly/html/classvtkSmoothPolyDataFilter.html#details" target="_blank" rel="noopener nofollow ugc">VTK: vtkSmoothPolyDataFilter Class Reference</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It says this:</p>
<blockquote>
<p>Optionally you can further control the smoothing process by defining a second input: the Source. If defined, the input mesh is constrained to lie on the surface defined by the Source ivar.</p>
</blockquote>
<p>You can check the WrapSolidifyEffect implementation as example of how it is used, link below:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify/blob/600681438bca4ab900511d8677b7cb3046767dc2/SegmentEditorWrapSolidify/SegmentEditorWrapSolidifyLib/SegmentEditorEffect.py#L557">
  <header class="source">

      <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify/blob/600681438bca4ab900511d8677b7cb3046767dc2/SegmentEditorWrapSolidify/SegmentEditorWrapSolidifyLib/SegmentEditorEffect.py#L557" target="_blank" rel="noopener nofollow ugc">github.com/sebastianandress/Slicer-SurfaceWrapSolidify</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify/blob/600681438bca4ab900511d8677b7cb3046767dc2/SegmentEditorWrapSolidify/SegmentEditorWrapSolidifyLib/SegmentEditorEffect.py#L557" target="_blank" rel="noopener nofollow ugc">SegmentEditorWrapSolidify/SegmentEditorWrapSolidifyLib/SegmentEditorEffect.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify/blob/600681438bca4ab900511d8677b7cb3046767dc2/SegmentEditorWrapSolidify/SegmentEditorWrapSolidifyLib/SegmentEditorEffect.py#L557" rel="noopener nofollow ugc"><code>600681438</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="547" style="counter-reset: li-counter 546 ;">
          <li>spacing = self._inputSpacing / self.remeshOversampling</li>
          <li></li>
          <li>for iterationIndex in range(self.shrinkwrapIterations):</li>
          <li></li>
          <li>  # shrink</li>
          <li>  self._checkCancelRequested()</li>
          <li>  self._log('Shrinking %s/%s...' %(iterationIndex+1, self.shrinkwrapIterations))</li>
          <li>  if shrunkenPd.GetNumberOfPoints()&lt;=1 or self._inputPd.GetNumberOfPoints()&lt;=1:</li>
          <li>    # we must not feed empty polydata into vtkSmoothPolyDataFilter because it would crash the application</li>
          <li>    raise ValueError("Mesh has become empty during shrink-wrap iterations")</li>
          <li class="selected">  smoothFilter = vtk.vtkSmoothPolyDataFilter()</li>
          <li>  smoothFilter.SetInputData(0, shrunkenPd)</li>
          <li>  smoothFilter.SetInputData(1, self._inputPd)  # constrain smoothed points to the input surface</li>
          <li>  smoothFilter.Update()</li>
          <li>  shrunkenPd = vtk.vtkPolyData()</li>
          <li>  shrunkenPd.DeepCopy(smoothFilter.GetOutput())</li>
          <li>  self._saveIntermediateResult("Shrunken", shrunkenPd)</li>
          <li></li>
          <li>  # remesh</li>
          <li>  self._checkCancelRequested()</li>
          <li>  self._log('Remeshing %s/%s...' %(iterationIndex+1, self.shrinkwrapIterations))</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Also, you may need to use the filter this twice, one time per bone</p>

---

## Post #3 by @ZackA (2025-08-20 16:46 UTC)

<p>Thanks for the suggestion Mauro. I’m having difficulty implementing this filter since I admittedly have zero experience with VTK, and only basic proficiency in Python. I tried skimming the script repository at <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#apply-vtk-filter-on-a-model-node" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a> and the first couple tutorials at <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Tutorials_for_software_developers" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Training - Slicer Wiki</a> but I was having trouble finding info specific to my application (lots of varied commands and applications but nothing seemingly specific enough to work).<br>
I especially don’t understand how to convert my model node correctly into vtkPolyData so I can run the filter, then back into a model I can manipulate in the 3Dslicer GUI.</p>
<p>My best attempt was below. I’m pretty sure this is complete nonsense code, sorry:</p>
<pre data-code-wrap="python"><code class="lang-python">modelNode = getNode('vtkMRMLModelNode5')

filterItUp = vtk.vtkSmoothPolyDataFilter()
filterItUp.SetInputData(0, modelNode.GetPolyData())
#I also tried filterItUp.SetInputData(modelNode.GetPolyData())
filterItUp.Update()

modelNode.SetPolyDataConnection(filterItUp.GetOutputPort())
#I also tried
modelNode.SetAndObservePolyData(filterItUp.GetOutput())
</code></pre>
<p>I see no change in my original model in the 3D viewer after running this.</p>

---

## Post #4 by @mau_igna_06 (2025-08-20 17:05 UTC)

<p>You should be able to update as follows:</p>
<pre data-code-wrap="python"><code class="lang-python"># overwrite the model contents
getNode('myModelToModifyName').SetAndObservePolyData(somePolydataFilter.GetOutput())
# or create a new model
modelsLogic = slicer.modules.models.logic()
model = modelsLogic.AddModel(somePolydataFilter.GetOutput())
</code></pre>
<p>I suggest you start with a SourceFilter and the second method, till you understand how it works</p>

---

## Post #5 by @ZackA (2025-10-16 19:23 UTC)

<p>Super late follow up to close this question.</p>
<p>I was able to apply vtkSmoothPolyDataFilter to my models but had no luck filling the large holes on the model at all.<br>
I also found a vtkFillHolesFilter ( <a href="https://vtk.org/doc/nightly/html/classvtkFillHolesFilter.html" class="inline-onebox" rel="noopener nofollow ugc">VTK: vtkFillHolesFilter Class Reference</a> ) which seems applicable to this situation, but it was unable to recognize the major gaps in my surface model despite me trying many different values for the SetHoleSize function. It must not be applicable for surfaces as incomplete as mine. See the image attached, which is slightly altered from the blue femur model in my initial post.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/866a61496711ccf1c4685c4015bbc7e13affe949.png" data-download-href="/uploads/short-url/jb5TKvquJ4WvP6rBenEun0shSD7.png?dl=1" title="FillHolesEx1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/866a61496711ccf1c4685c4015bbc7e13affe949_2_690x281.png" alt="FillHolesEx1" data-base62-sha1="jb5TKvquJ4WvP6rBenEun0shSD7" width="690" height="281" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/866a61496711ccf1c4685c4015bbc7e13affe949_2_690x281.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/866a61496711ccf1c4685c4015bbc7e13affe949_2_1035x421.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/866a61496711ccf1c4685c4015bbc7e13affe949.png 2x" data-dominant-color="9B85A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">FillHolesEx1</span><span class="informations">1327×542 249 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In the end I ended up using a proprietary model post-processing software that comes with the scanner I used to originally make the surface models. After making the surface watertight, I had no further issues converting into a volumetric segmentation object in 3Dslicer.</p>

---
