# Import DicomRT fault (caps open area)

**Topic ID**: 6147
**Date**: 2019-03-14
**URL**: https://discourse.slicer.org/t/import-dicomrt-fault-caps-open-area/6147

---

## Post #1 by @rtarver (2019-03-14 18:54 UTC)

<p>Operating system:  Windows<br>
Slicer version:  4.7<br>
Expected behavior:  DicomRT fidelity<br>
Actual behavior:  Incorrect import/display?</p>
<p>I’m working on some 3D printing projects and can successfully move data from my planning station to my printing tools.  However, it seems that when I import my DicomRT objects, 3Dslicer caps the top and bottom incorrectly.  There’s probably an easy way to fix or trim this issue, but I can’t figure it out.</p>
<p>Right now, I import the DicomRT Structures, and simply export/save as an *.stl file, then I take over with Simplify3D.  I’d rather not include another piece of software unless absolutely necessary.  I’ve tried to attach a picture where you can see the added top and bottom ‘plates’ that are added.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b78660b96de1dfd59656b05e7baa6901f626dbc.png" data-download-href="/uploads/short-url/3V0QmqpbtZLG5ziMdGfSUNpmNdi.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b78660b96de1dfd59656b05e7baa6901f626dbc_2_656x499.png" alt="image" data-base62-sha1="3V0QmqpbtZLG5ziMdGfSUNpmNdi" width="656" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b78660b96de1dfd59656b05e7baa6901f626dbc_2_656x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b78660b96de1dfd59656b05e7baa6901f626dbc_2_984x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b78660b96de1dfd59656b05e7baa6901f626dbc.png 2x" data-dominant-color="8888AC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1273×970 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-03-14 19:02 UTC)

<p>What do you mean by “caps the top and bottom incorrectly”? Can you upload a screenshot how it looks like and what would you expect it to look like?</p>
<p>DICOM RTSTRUCT is only intended to be used for radiation therapy planning and it is not suitable as a general-purpose mesh file format. There are geometries that simply cannot be stored accurately in RTSTRUCT. If possible, try to avoid RTSTRUCT and use any standard mesh file format instead. There are new DICOM objects that allow proper storage of surface meshes.</p>

---

## Post #3 by @rtarver (2019-03-15 00:47 UTC)

<p>Andras,</p>
<p>I think I’m limited to to DICOM-RT for my initial structure design and export based on my planning station capabilities.  If you look at the uploaded graphic in the original post, you can see the artifact I’m seeing.  You can see the general patient contour, and then at either end (top and bottom), you can see there’s a fine thin ‘plate’ with a sharp edge.  Neither of those are in my original design and I suspect are some sort artifact from the DicomRT export, or DicomRT import.</p>
<p>Ultimately I solved this particular problem by using a cheap free modeler to subtract off a mm at each end, but I’d rather not add another piece of software unless absolutely necessary.</p>

---

## Post #4 by @cpinter (2019-03-15 01:04 UTC)

<p>End-capping is performed for the following reason: “Since the image slices that are used to draw the contours are shown at the midline of the voxels comprising the slice but are infinitely thin, end-capping needs to be applied, so that the half-voxel thick volume at the top and bottom extremes are considered.”</p>
<p>If you don’t do end-capping, then the top and bottom contours will be flat (and thus unrealistic), and also incorrectly occupying the volume as explained above. This step is typically performed in software able to import DICOM-RT, but the ways may be different. SlicerRT does end-capping by adding an extra contour half slice from the extreme slices, which will be the same as the last contours, except eroded to be 50% of the area.</p>
<p>I don’t think this option can be disabled, but I can add this option easily.</p>
<aside class="quote no-group" data-username="rtarver" data-post="3" data-topic="6147">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/e79b87/48.png" class="avatar"> rtarver:</div>
<blockquote>
<p>using a cheap free modeler to subtract off a mm at each end</p>
</blockquote>
</aside>
<p>The Segment Editor module can do this, no need to use external software.</p>

---

## Post #5 by @lassoan (2019-03-15 01:50 UTC)

<aside class="quote no-group" data-username="rtarver" data-post="3" data-topic="6147">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/e79b87/48.png" class="avatar"> rtarver:</div>
<blockquote>
<p>you can see there’s a fine thin ‘plate’ with a sharp edge</p>
</blockquote>
</aside>
<p>Would you mind posting an image that shows the issue better? Mark the part where the issue is and if possible attach a picture that shows a screenshot from a rendering by your TPS.</p>
<p>Do you try to define an open surface in your TPS? Do you draw lines or closed curves in the image slices?</p>
<p>Why do you use your TPS for segmentation? It is likely that you can do the segmentation faster and better quality using the Segment Editor module in Slicer. Also, you can avoid lossy and unpredictable conversion of your surface to and from DICOM RTSTRUCT (you can export segmentations from Slicer directly to STL).</p>

---

## Post #6 by @rtarver (2019-03-15 19:07 UTC)

<p>Andras,</p>
<p>Thank you so much for the responses.</p>
<p>First image below is directly from my planning station (Varian Eclipse if that matters).<br>
Second image is from Simplify3D showing the caps created by Slicer3D.<br>
Third image is from Slicer3D.</p>
<p>I tried to keep the same aspect for all three images.  The area of concern is the only ‘flat space’ in the whole structure and should be readily apparent.  This isn’t a simple capping of an existing contour but instead is some type of interpolation between points.</p>
<p>If there’s an easy way to correct this in Slicer3D, then that would make my process flow much easier.  I would really appreciate the tip/trick to do that easily.  In general, I don’t bring in any of the images, only the structure.</p>
<p>Regarding my workflow.  It’s much easier to design the device in the planning station because ultimately I need it there for calculation purposes, and it’s design is a function of existing beam placement and is facilitated by those tools.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/baf095733c5c0b372578e0bdf0d8767a64ab6734.jpeg" alt="image" data-base62-sha1="qFKfZlJ76cavxizvkktOtFEze1S" width="690" height="457"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/383d1be4247ffd004f3dfad9ff95f2bae7f686f3.png" data-download-href="/uploads/short-url/81vF98jVJfbg2JESiCvOtRVOSmD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/383d1be4247ffd004f3dfad9ff95f2bae7f686f3_2_690x479.png" alt="image" data-base62-sha1="81vF98jVJfbg2JESiCvOtRVOSmD" width="690" height="479" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/383d1be4247ffd004f3dfad9ff95f2bae7f686f3_2_690x479.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/383d1be4247ffd004f3dfad9ff95f2bae7f686f3_2_1035x718.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/383d1be4247ffd004f3dfad9ff95f2bae7f686f3.png 2x" data-dominant-color="CBCDC4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1116×776 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f0f0dbfe6bfb3c0fa579259912f1662847bf656.png" data-download-href="/uploads/short-url/6IiGZWLuLu8ex9OJGAMSf3ioN7w.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f0f0dbfe6bfb3c0fa579259912f1662847bf656_2_650x500.png" alt="image" data-base62-sha1="6IiGZWLuLu8ex9OJGAMSf3ioN7w" width="650" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f0f0dbfe6bfb3c0fa579259912f1662847bf656_2_650x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f0f0dbfe6bfb3c0fa579259912f1662847bf656_2_975x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f0f0dbfe6bfb3c0fa579259912f1662847bf656.png 2x" data-dominant-color="9293AF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1280×984 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @cpinter (2019-03-15 19:13 UTC)

<p>This seems like an open countour, but SlicerRT currently does not support open countours</p><aside class="onebox githubissue" data-onebox-src="https://github.com/SlicerRt/SlicerRT/issues/45">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/issues/45" target="_blank" rel="noopener">github.com/SlicerRt/SlicerRT</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerRt/SlicerRT/issues/45" target="_blank" rel="noopener">Add support for open contours</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2017-09-15" data-time="20:50:52" data-timezone="UTC">08:50PM - 15 Sep 17 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/cpinter" target="_blank" rel="noopener">
          <img alt="cpinter" src="https://avatars.githubusercontent.com/u/1325980?v=4" class="onebox-avatar-inline" width="20" height="20">
          cpinter
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Issue reported in http://www.na-mic.org/Bug/view.php?id=4087
Adding this suppor<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">t will be also useful for future projects.

The open contours are to be loaded to segmentation objects with
* Non-planar contour
  * Contains the raw contour points
  * Converter is needed to closed surface
* Closed surface containing the tube model
  * What should be the radius of the tube? Half of the slice thickness calculated from the planar contours from the other contained structures? Constant 1mm? -&gt; Start with 1mm, it will be a conversion parameter

Migrated from https://app.assembla.com/spaces/slicerrt/tickets/786-add-support-for-open-contours/details</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Is it supposed to be open, or is it just really thin?</p>

---

## Post #8 by @rtarver (2019-03-15 21:23 UTC)

<p>This particular device is a solid shell with a thickness of 3mm.  It’s a closed shell, but the surfaces of interest (those large flat surfaces) should not be there.</p>
<p>Russ</p>

---

## Post #9 by @lassoan (2019-03-15 21:51 UTC)

<p>Maybe we haven’t tested the end-capping algorithm thoroughly enough with thin shell geometries. Please share a data set with us (use a publicly available CT series to avoid privacy issues) and we’ll test and fix up end-capping.</p>

---

## Post #10 by @rtarver (2019-03-18 12:59 UTC)

<p>Andras,</p>
<p>Do you need the original CT set?  The Structure started as DICOM-RT from my planning station.  Generating contours outside of the planning station (and thus endcapping in Slicer3D), would complicate things for me.</p>
<p>For calculation purposes, I need to generate the structures in my planning station.  For diagnostic purposes, I’ll generate a thicker shell and see if we have the same issue.</p>
<p>Russ</p>

---

## Post #11 by @lassoan (2019-03-18 13:08 UTC)

<aside class="quote no-group" data-username="rtarver" data-post="10" data-topic="6147">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/e79b87/48.png" class="avatar"> rtarver:</div>
<blockquote>
<p>Do you need the original CT set?</p>
</blockquote>
</aside>
<p>The original CT is needed to determine slice spacing (it is one of the many limitations of RTSTRUCT IOD that it cannot be fully interpreted without a referenced image IOD), but if it is missing then I think Slicer’s importer tries to guess slice spacing from the minimum distance between planar contour planes. So, it is nice to have the CT but if it is problematic to share then we can probably do without it.</p>

---

## Post #12 by @cpinter (2019-03-18 13:33 UTC)

<p>CT is not considered when triangulating RTSTRUCT (slice thickness is not needed from the CT for this step, but it is calculated from the contours, see <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/ConversionRules/vtkPlanarContourToClosedSurfaceConversionRule.cxx#L1206" rel="nofollow noopener">here</a>). We only need the structure set to fix this. However, if you don’t mind sharing the whole dataset for future test purposes, then we’d appreciate having it if it’s anonymized. Thanks!</p>

---

## Post #13 by @rtarver (2019-03-18 21:09 UTC)

<p>What’s the best way to upload/store this amount of data?</p>
<p>Russ</p>

---

## Post #14 by @lassoan (2019-03-18 21:30 UTC)

<p>Upload to dropbox/onedrive/googledrive/etc and post the link. Thanks!</p>

---

## Post #15 by @timeanddoctor (2019-03-19 05:06 UTC)

<p>you can use “modify” in blender another free software</p>

---

## Post #16 by @cpinter (2019-03-19 11:43 UTC)

<p>The problem with this is that he has DICOM-RT, not STL or OBJ.</p>

---
