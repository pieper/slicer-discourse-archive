# ".vtk" surface mesh to segmentation

**Topic ID**: 15795
**Date**: 2021-02-02
**URL**: https://discourse.slicer.org/t/vtk-surface-mesh-to-segmentation/15795

---

## Post #1 by @rohand24 (2021-02-02 13:11 UTC)

<p>Operating system:Mac OS Catalina 10.15.7<br>
Slicer version: 4.13.0-2020-12-16 r29527 / d63012c</p>
<p>Hi,</p>
<p>I have a DICOM series and “.vtk” segmentation files (yellow) in the image.<br>
I am able to load these files only as models.</p>
<p>How do I convert these surface meshes to segmentations.<br>
<strong>Note:</strong> These are <strong>not closed</strong> surface meshes.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09cd382fb4faae7b1ae738f790d540474fdb72cf.jpeg" data-download-href="/uploads/short-url/1oHYDbWZy8eQmolFbeNcebnTwir.jpeg?dl=1" title="Screen Shot 2021-02-01 at 9.11.47 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09cd382fb4faae7b1ae738f790d540474fdb72cf_2_517x349.jpeg" alt="Screen Shot 2021-02-01 at 9.11.47 PM" data-base62-sha1="1oHYDbWZy8eQmolFbeNcebnTwir" width="517" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09cd382fb4faae7b1ae738f790d540474fdb72cf_2_517x349.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09cd382fb4faae7b1ae738f790d540474fdb72cf_2_775x523.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09cd382fb4faae7b1ae738f790d540474fdb72cf_2_1034x698.jpeg 2x" data-dominant-color="9092BF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-02-01 at 9.11.47 PM</span><span class="informations">2176×1470 217 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bd7ace99a8b915bfc23ae0b262529f5c8a6f7db.jpeg" data-download-href="/uploads/short-url/fo1aExlTkyiQSmQKUG8F4So0d5N.jpeg?dl=1" title="Screen Shot 2021-02-01 at 9.12.31 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bd7ace99a8b915bfc23ae0b262529f5c8a6f7db_2_517x339.jpeg" alt="Screen Shot 2021-02-01 at 9.12.31 PM" data-base62-sha1="fo1aExlTkyiQSmQKUG8F4So0d5N" width="517" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bd7ace99a8b915bfc23ae0b262529f5c8a6f7db_2_517x339.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bd7ace99a8b915bfc23ae0b262529f5c8a6f7db_2_775x508.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bd7ace99a8b915bfc23ae0b262529f5c8a6f7db_2_1034x678.jpeg 2x" data-dominant-color="68697B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-02-01 at 9.12.31 PM</span><span class="informations">2180×1434 242 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Attached below is the pyvista visualization of an example mesh.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/0581073040e90fe35eaf250b25dfedafed557a84.jpeg" data-download-href="/uploads/short-url/MGPnFEWHmO41kjoIXcWGnbXmMk.jpeg?dl=1" title="Screen Shot 2021-02-01 at 9.16.23 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0581073040e90fe35eaf250b25dfedafed557a84_2_500x375.jpeg" alt="Screen Shot 2021-02-01 at 9.16.23 PM" data-base62-sha1="MGPnFEWHmO41kjoIXcWGnbXmMk" width="500" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0581073040e90fe35eaf250b25dfedafed557a84_2_500x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0581073040e90fe35eaf250b25dfedafed557a84_2_750x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0581073040e90fe35eaf250b25dfedafed557a84_2_1000x750.jpeg 2x" data-dominant-color="4C4D4D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-02-01 at 9.16.23 PM</span><span class="informations">2046×1532 85.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2021-02-02 13:24 UTC)

<p>Reconstructing a surface from closed curves is not a trivial operation.</p>
<p>Are the curves all planar? Are the planes parallel? Then you can import them by installing SlicerRT extension and doing the same as it is done in the OsiriX ROI importer:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/ImportOsirixROI/ImportOsirixROI.py#L276-L281" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerSandbox/blob/master/ImportOsirixROI/ImportOsirixROI.py#L276-L281" target="_blank" rel="noopener">PerkLab/SlicerSandbox/blob/master/ImportOsirixROI/ImportOsirixROI.py#L276-L281</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="276" style="counter-reset: li-counter 275 ;">
<li>segment = slicer.vtkSegment()</li><li>segment.SetName(name)</li><li>segment.SetColor(color)</li><li>segment.AddRepresentation(slicer.vtkSegmentationConverter.GetPlanarContourRepresentationName(), roiPolyData)</li><li></li><li>segmentation.AddSegment(segment)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>If curves are on arbitrarily oriented planes then it is more complicated but even then there are many options available to reconstruct. For example, you can straighten the centerline using Curved Planar Reformat module (in Sandbox extension) and import the parallel contours as segmentation, then warp it back using the reformatting transform to the original geometry. Alternatively, you can rasterize each contour to a binary labelmap and then use Volume reconstructor (in SlicerIGSIO extension) to reconstruct a Cartesian segmentation volume from the oblique slices.</p>

---
