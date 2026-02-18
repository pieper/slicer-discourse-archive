# Question on "export segments to models"

**Topic ID**: 39797
**Date**: 2024-10-22
**URL**: https://discourse.slicer.org/t/question-on-export-segments-to-models/39797

---

## Post #1 by @ckolluru (2024-10-22 14:31 UTC)

<p>Hi,</p>
<p>This is related to my earlier post: <a href="https://discourse.slicer.org/t/filters-and-parameters-used-in-export-visible-segments-to-model/37011" class="inline-onebox">Filters and parameters used in "export visible segments to model"</a>.</p>
<p>I’m trying to do the following: I have a binary labelmap that I load into Slicer. Then I click on the segment and select “Export visible segments to models”. In the model node, on its color box, I right click and select the checkbox for 2D visibility. The application then shows the segment as a thin contour in the 2D views. It seems to be smoother than the binary labelmap by default (see attached picture).</p>
<p>I’m trying to replicate this workflow from python - given a labelmap, I would like to process it to be able to get these contours. Does anyone have some suggestions on how I might be able to do this? If the specific VTK filters, parameters and code are available somewhere, can that be linked here?</p>
<p>Any help would be appreciated.</p>
<p>Thanks,<br>
Chaitanya</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b55145247a91bf9a1088467ff8a621970f38597f.png" data-download-href="/uploads/short-url/pS0xDpGm7hvMD51Vn4gmj6cz2nZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b55145247a91bf9a1088467ff8a621970f38597f.png" alt="image" data-base62-sha1="pS0xDpGm7hvMD51Vn4gmj6cz2nZ" width="226" height="228"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">226×228 5.91 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87920c8751b493d4567514573492b6b775442ae0.png" data-download-href="/uploads/short-url/jljmKryz5p8bivDa1T4rIdhlsli.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87920c8751b493d4567514573492b6b775442ae0.png" alt="image" data-base62-sha1="jljmKryz5p8bivDa1T4rIdhlsli" width="518" height="275"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">518×275 24.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2024-10-22 14:44 UTC)

<p>It is smoother because the closed surface conversion does some smoothing after the triangle creation (according to a parameter that is easy to change), so that the object approximate better the reality. The vertices in the closed surface representation have an infinite accuracy as opposed to the fixed sized voxels of the binary labelmap, so it makes sense to try to make it more realistic.</p>
<p>The visualization pipeline is in the displayable manager, and in that there is a cutter filter that creates the 2D contours from the 3D surface based on the slice plane:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Segmentations/MRMLDM/vtkMRMLSegmentationsDisplayableManager2D.cxx#L147">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Segmentations/MRMLDM/vtkMRMLSegmentationsDisplayableManager2D.cxx#L147" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Segmentations/MRMLDM/vtkMRMLSegmentationsDisplayableManager2D.cxx#L147" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Modules/Loadable/Segmentations/MRMLDM/vtkMRMLSegmentationsDisplayableManager2D.cxx#L147</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="137" style="counter-reset: li-counter 136 ;">
          <li>{</li>
          <li>  this-&gt;WorldToSliceTransform = vtkSmartPointer&lt;vtkTransform&gt;::New();</li>
          <li>  this-&gt;NodeToWorldTransform = vtkSmartPointer&lt;vtkGeneralTransform&gt;::New();</li>
          <li>  this-&gt;WorldToNodeTransform = vtkSmartPointer&lt;vtkGeneralTransform&gt;::New();</li>
          <li></li>
          <li>  this-&gt;SliceIntersectionUpdatedTime = 0;</li>
          <li></li>
          <li>  // Create poly data pipeline</li>
          <li>  this-&gt;PolyDataOutlineActor = vtkSmartPointer&lt;vtkActor2D&gt;::New();</li>
          <li>  this-&gt;PolyDataFillActor = vtkSmartPointer&lt;vtkActor2D&gt;::New();</li>
          <li class="selected">  this-&gt;Cutter = vtkSmartPointer&lt;vtkPlaneCutter&gt;::New();</li>
          <li>  this-&gt;ModelWarper = vtkSmartPointer&lt;vtkTransformPolyDataFilter&gt;::New();</li>
          <li>  this-&gt;Plane = vtkSmartPointer&lt;vtkPlane&gt;::New();</li>
          <li>  this-&gt;Triangulator = vtkSmartPointer&lt;vtkContourTriangulator&gt;::New();</li>
          <li></li>
          <li>  // Set up poly data outline pipeline</li>
          <li>  this-&gt;Cutter-&gt;SetInputConnection(this-&gt;ModelWarper-&gt;GetOutputPort());</li>
          <li>  this-&gt;Cutter-&gt;SetPlane(this-&gt;Plane);</li>
          <li>  this-&gt;Cutter-&gt;BuildTreeOff(); // the cutter crashes for complex geometries if build tree is enabled</li>
          <li>  vtkSmartPointer&lt;vtkTransformPolyDataFilter&gt; polyDataOutlineTransformer = vtkSmartPointer&lt;vtkTransformPolyDataFilter&gt;::New();</li>
          <li>  vtkNew&lt;vtkGeometryFilter&gt; geometryFilter;</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @ckolluru (2024-10-22 15:07 UTC)

<p>Thanks, this helps. Is this the function that does the binary labelmap to closed surface conversion? Are these the primary variables that control smoothing?</p>
<ul>
<li><code>smoothingFactor</code></li>
<li><code>jointSmoothing</code> ’</li>
<li><code>decimationFactor</code></li>
</ul>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/88245c9ccc69144cd3ca983cfd71792400f7a0a5/Libs/vtkSegmentationCore/vtkBinaryLabelmapToClosedSurfaceConversionRule.cxx#L141">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/88245c9ccc69144cd3ca983cfd71792400f7a0a5/Libs/vtkSegmentationCore/vtkBinaryLabelmapToClosedSurfaceConversionRule.cxx#L141" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/88245c9ccc69144cd3ca983cfd71792400f7a0a5/Libs/vtkSegmentationCore/vtkBinaryLabelmapToClosedSurfaceConversionRule.cxx#L141" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/88245c9ccc69144cd3ca983cfd71792400f7a0a5/Libs/vtkSegmentationCore/vtkBinaryLabelmapToClosedSurfaceConversionRule.cxx#L141</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="131" style="counter-reset: li-counter 130 ;">
          <li>  {</li>
          <li>    return (vtkDataObject*)vtkPolyData::New();</li>
          <li>  }</li>
          <li>  else</li>
          <li>  {</li>
          <li>    return nullptr;</li>
          <li>  }</li>
          <li>}</li>
          <li></li>
          <li>//----------------------------------------------------------------------------</li>
          <li class="selected">bool vtkBinaryLabelmapToClosedSurfaceConversionRule::Convert(vtkSegment* segment)</li>
          <li>{</li>
          <li>  this-&gt;CreateTargetRepresentation(segment);</li>
          <li></li>
          <li>  vtkDataObject* sourceRepresentation = segment-&gt;GetRepresentation(this-&gt;GetSourceRepresentationName());</li>
          <li>  vtkDataObject* targetRepresentation = segment-&gt;GetRepresentation(this-&gt;GetTargetRepresentationName());</li>
          <li></li>
          <li>  vtkPolyData* closedSurfacePolyData = vtkPolyData::SafeDownCast(targetRepresentation);</li>
          <li>  if (!closedSurfacePolyData)</li>
          <li>  {</li>
          <li>    vtkErrorMacro("Convert: Target representation is not poly data");</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @cpinter (2024-10-22 15:39 UTC)

<p>What I posted is the displayable manager that creates the 2D contours for the slice. It has nothing to do with internal conversion within segmentations, which is 3D-&gt;3D.</p>

---

## Post #5 by @ckolluru (2024-10-22 17:23 UTC)

<p>I’m sorry, maybe I wasn’t clear. I was referring to the code snippet I posted in my response. I’m looking at this function.</p>
<p><code>bool vtkBinaryLabelmapToClosedSurfaceConversionRule::Convert(vtkSegment* segment)</code></p>
<p>Is that the place where the conversion from binary labelmap to closed surface happens? I see some variables there that seem to control smoothing (<code>smoothingFactor</code>, <code>jointSmoothing</code>, <code>decimationFactor</code>) - were those the parameters you were referring to? Are those parameters available to change from Slicer’s UI?</p>

---

## Post #6 by @ckolluru (2024-10-22 20:49 UTC)

<p>Found these parameters in Segmentations &gt; Representations &gt; Closed Surface &gt; Advanced create…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8da224fa68a44254d56099988f90f4c5d9b3ca2.png" data-download-href="/uploads/short-url/xdU7DmxI789EZp6f5TROSqoEjIK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8da224fa68a44254d56099988f90f4c5d9b3ca2_2_483x500.png" alt="image" data-base62-sha1="xdU7DmxI789EZp6f5TROSqoEjIK" width="483" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8da224fa68a44254d56099988f90f4c5d9b3ca2_2_483x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8da224fa68a44254d56099988f90f4c5d9b3ca2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8da224fa68a44254d56099988f90f4c5d9b3ca2.png 2x" data-dominant-color="EEF2F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">661×683 34.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @cpinter (2024-10-23 08:26 UTC)

<aside class="quote no-group" data-username="ckolluru" data-post="5" data-topic="39797">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/ecccb3/48.png" class="avatar"> ckolluru:</div>
<blockquote>
<p>Is that the place where the conversion from binary labelmap to closed surface happens?</p>
</blockquote>
</aside>
<p>Yes it is. Sorry if I misunderstood. This is the filter that internally converts the source (formerly master) labelmap into closed surface when requested for 3D visualization, as the conversion diagram shows here</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html#representations">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html#representations" target="_blank" rel="noopener">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html#representations" target="_blank" rel="noopener">Image Segmentation — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The parameters you found are the parameters that these conversion “rules” expose. You can fine-tune the output using these.</p>
<p>The displayable managers on the other hand are classes that create the actors in the views (2D and 3D) to show the desired displayed representation. This is why the 2D displayable manager for the segmentation needs to do cutting if the representation to show is closed surface, because we need to show the contour that is the intersection of the surface with the slice plane.</p>

---
