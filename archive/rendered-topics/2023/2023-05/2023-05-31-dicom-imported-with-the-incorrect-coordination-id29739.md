# Dicom imported with the incorrect coordination

**Topic ID**: 29739
**Date**: 2023-05-31
**URL**: https://discourse.slicer.org/t/dicom-imported-with-the-incorrect-coordination/29739

---

## Post #1 by @B4D (2023-05-31 02:36 UTC)

<p>Many dental scanners in dentistry now compress their dicom exports into one file, as opposed to many individual slices. When trying to load I get this message.<br>
Unamed series (Scalar Volume)" Multi-frame image…<br>
The dicom loads, but the orientation is incorrect. When I use two different software and make stl models and import the models into slicer, they are clearly in a different location. I would like to email someone for urgent help please. I have all the files.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0ad930997e75830f79bc9c9afbedc89517dd1f90.png" alt="dicom1" data-base62-sha1="1xY6jiDYP2iWKAl0RAHFgrC7eta" width="519" height="245"></p>
<p>The green is the segmentation model and the Yellow is a model from a different software.</p>
<p>Here is a dropbox link to the files. <a href="https://www.dropbox.com/sh/enm4itjlk7t6pgj/AAAR6arhvO9sRZJhUnJs-BAsa?dl=1" class="inline-onebox" rel="noopener nofollow ugc">Dicom Issue</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1328d3aa0907d1e8ef9567736868cd5bf6cf1982.jpeg" data-download-href="/uploads/short-url/2JuxFdX0nSpx9mBTCJIlRoizy0O.jpeg?dl=1" title="dicom3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/1328d3aa0907d1e8ef9567736868cd5bf6cf1982_2_690x394.jpeg" alt="dicom3" data-base62-sha1="2JuxFdX0nSpx9mBTCJIlRoizy0O" width="690" height="394" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/1328d3aa0907d1e8ef9567736868cd5bf6cf1982_2_690x394.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/1328d3aa0907d1e8ef9567736868cd5bf6cf1982_2_1035x591.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/1328d3aa0907d1e8ef9567736868cd5bf6cf1982_2_1380x788.jpeg 2x" data-dominant-color="4E5054"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dicom3</span><span class="informations">1877×1073 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-05-31 02:46 UTC)

<p>We need at least one example image that we can test on. If you only have patient images that you cannot share then maybe you can acquire images of calibration or quality assurance phantom.</p>

---

## Post #3 by @B4D (2023-05-31 02:47 UTC)

<p>I have supplied the dicom and the stl files in a dropbox link.</p>

---

## Post #4 by @lassoan (2023-05-31 04:20 UTC)

<h2><a name="p-95524-summary-1" class="anchor" href="#p-95524-summary-1" aria-label="Heading link"></a>Summary</h2>
<p>Slicer loads the image correctly (tested with Slicer-5.2.2 on Windows).</p>
<p>The STL file that you attached is in incorrect location (it seems that it is shifted so that all its point coordinates are positive).</p>
<h2><a name="p-95524-details-2" class="anchor" href="#p-95524-details-2" aria-label="Heading link"></a>Details</h2>
<h3><a name="p-95524-info-from-dicom-image-header-3" class="anchor" href="#p-95524-info-from-dicom-image-header-3" aria-label="Heading link"></a>Info from DICOM image header</h3>
<p>Rows x Columns: 390 x 390<br>
PixelSpacing: 0.2, 0.2<br>
=&gt; This means that the frame size is: 78mm x 78mm</p>
<p>ImageOrientationPatient: 1, 0, 0, 0, 1, 0<br>
=&gt; This means that slices are axial</p>
<p>ImagePositionPatient for each frame (in LPS):<br>
-39, -39, 30.5<br>
-39, -39, 30.3<br>
-39, -39, 30.1<br>
…<br>
-39, -39, -30.3</p>
<p>=&gt; This means that the image bounds (in LPS) are: [-39 to 39, -39 to 39, -30.3 to 30.5]</p>
<h3><a name="p-95524-comparison-to-image-and-stl-file-bounds-4" class="anchor" href="#p-95524-comparison-to-image-and-stl-file-bounds-4" aria-label="Heading link"></a>Comparison to image and STL file bounds</h3>
<p>These bounds are exactly where the Slicer-imported image appears in:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91f4fe7a7ddb7a84b81485c703eaa0b49e58092e.jpeg" data-download-href="/uploads/short-url/kPc85Se8yuKl8p8DIoSZSNcy1DE.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91f4fe7a7ddb7a84b81485c703eaa0b49e58092e_2_690x416.jpeg" alt="image" data-base62-sha1="kPc85Se8yuKl8p8DIoSZSNcy1DE" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91f4fe7a7ddb7a84b81485c703eaa0b49e58092e_2_690x416.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91f4fe7a7ddb7a84b81485c703eaa0b49e58092e_2_1035x624.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91f4fe7a7ddb7a84b81485c703eaa0b49e58092e_2_1380x832.jpeg 2x" data-dominant-color="5F474D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1159 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Therefore, Slicer loads the image into correct location, as specified in the DICOM header.</p>
<p>In contrast, the STL file that you included in the zip file is in incorrect location, as its bounds (in LPS) are: [0 to 78, 0 to 78, 0 to 60.8].</p>
<h2><a name="p-95524-what-to-do-5" class="anchor" href="#p-95524-what-to-do-5" aria-label="Heading link"></a>What to do?</h2>
<p>If you just use Slicer and other software that loads the images and saves segmentations correctly then you don’t need to change anything - just keep using these software.</p>
<p>If you want to use that software that created the STL file in the incorrect location then you may able re-export correctly by either adjusting its STL export settings (disable enforcing of positive point coordinates), or by saving the mesh in a different file format (such as ply or obj).</p>
<p>Note that point coordinates in STL files are forced to positive in some software because 35 years ago in the original STL file specification they specified an arbitrary limitation that coordinates in STL files must be positive. While most software simply ignore this unnecessary limitation, some sofware modifies the mesh during export to ensure that coordinates are all positive. This shift cannot be undone: the original, correct coordinates are permanently and irreversibly lost.</p>

---
