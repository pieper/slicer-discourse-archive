# How to extract 2d flat surface from contour planes 

**Topic ID**: 40592
**Date**: 2024-12-09
**URL**: https://discourse.slicer.org/t/how-to-extract-2d-flat-surface-from-contour-planes/40592

---

## Post #1 by @v.p.r (2024-12-09 19:26 UTC)

<p>Hi, im trying to get a flattened slice from a nifty file , in order to mesh in 2d it later. My objective is to obtain something like this :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e82ea9ff1ee69af48ef919a975a37fbb9b12143.png" data-download-href="/uploads/short-url/fLD0yQ7abUAHkIXnbh9QJq9vrpN.png?dl=1" title="Captura de pantalla 2024-12-09 201933" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e82ea9ff1ee69af48ef919a975a37fbb9b12143.png" alt="Captura de pantalla 2024-12-09 201933" data-base62-sha1="fLD0yQ7abUAHkIXnbh9QJq9vrpN" width="292" height="226"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-12-09 201933</span><span class="informations">292×226 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have segmented the brain and obteined the contours with the slicer rt extension, but i dont know how to export the 2d slice contoured as a stl file, in order to mesh it later, and not the whole volume. This is where i am at:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0842bef44f94d49910db034db719f663f4b1a5b.png" data-download-href="/uploads/short-url/yjHLHb16442GYPmZlYkTPw8ntR9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0842bef44f94d49910db034db719f663f4b1a5b_2_690x387.png" alt="image" data-base62-sha1="yjHLHb16442GYPmZlYkTPw8ntR9" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0842bef44f94d49910db034db719f663f4b1a5b_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0842bef44f94d49910db034db719f663f4b1a5b_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0842bef44f94d49910db034db719f663f4b1a5b_2_1380x774.png 2x" data-dominant-color="78727A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×1079 403 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Thank you in advance.</p>

---

## Post #2 by @mau_igna_06 (2024-12-09 20:29 UTC)

<p>I think a pipeline using the following filters could help you:</p>
<ol>
<li><a href="https://examples.vtk.org/site/Cxx/Filtering/ContoursFromPolyData/" rel="noopener nofollow ugc">https://examples.vtk.org/site/Cxx/Filtering/ContoursFromPolyData/</a></li>
<li><a href="https://vtk.org/doc/nightly/html/classvtkContourTriangulator.html#details" class="inline-onebox" rel="noopener nofollow ugc">VTK: vtkContourTriangulator Class Reference</a></li>
<li><a href="https://github.com/Slicer/SlicerSurfaceToolbox/blob/172c9d917ae695d14a3f1ad456e5bf61997b6231/SurfaceToolbox/SurfaceToolbox.py#L396-L402" class="inline-onebox" rel="noopener nofollow ugc">SlicerSurfaceToolbox/SurfaceToolbox/SurfaceToolbox.py at 172c9d917ae695d14a3f1ad456e5bf61997b6231 · Slicer/SlicerSurfaceToolbox · GitHub</a></li>
</ol>

---

## Post #3 by @cpinter (2024-12-10 12:46 UTC)

<p>This is the pipeline that Slicer uses for this:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Segmentations/MRMLDM/vtkMRMLSegmentationsDisplayableManager2D.cxx#L134">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Segmentations/MRMLDM/vtkMRMLSegmentationsDisplayableManager2D.cxx#L134" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Segmentations/MRMLDM/vtkMRMLSegmentationsDisplayableManager2D.cxx#L134" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Modules/Loadable/Segmentations/MRMLDM/vtkMRMLSegmentationsDisplayableManager2D.cxx#L134</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="124" style="counter-reset: li-counter 123 ;">
          <li>}</li>
          <li></li>
          <li>//---------------------------------------------------------------------------</li>
          <li>class vtkMRMLSegmentationsDisplayableManager2D::vtkInternal</li>
          <li>{</li>
          <li>public:</li>
          <li></li>
          <li>  vtkInternal( vtkMRMLSegmentationsDisplayableManager2D* external );</li>
          <li>  ~vtkInternal();</li>
          <li></li>
          <li class="selected">  struct Pipeline</li>
          <li>  {</li>
          <li>    Pipeline()</li>
          <li>    {</li>
          <li>      this-&gt;WorldToSliceTransform = vtkSmartPointer&lt;vtkTransform&gt;::New();</li>
          <li>      this-&gt;NodeToWorldTransform = vtkSmartPointer&lt;vtkGeneralTransform&gt;::New();</li>
          <li>      this-&gt;WorldToNodeTransform = vtkSmartPointer&lt;vtkGeneralTransform&gt;::New();</li>
          <li></li>
          <li>      this-&gt;SliceIntersectionUpdatedTime = 0;</li>
          <li></li>
          <li>      // Create poly data pipeline</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
