# How can I calculate an area on a CT image. I can calculate volumes (mm^3) but not areas (mm^2)

**Topic ID**: 1549
**Date**: 2017-11-28
**URL**: https://discourse.slicer.org/t/how-can-i-calculate-an-area-on-a-ct-image-i-can-calculate-volumes-mm-3-but-not-areas-mm-2/1549

---

## Post #1 by @Ert0 (2017-11-28 21:09 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2017-12-06 03:22 UTC)

<p>You can segment a single slice using Segment editor then compute surface using Segment statistics module. You need to divide the reported surface area value by 2, as surface of both sides of the segment are included in the reported number.</p>

---

## Post #3 by @TANG (2019-08-18 15:21 UTC)

<p>A single layer of the same dicom has different surface areas with different layers thickness (1mm,3mm,5mm), resulting in a large difference in surface area between the two.</p>

---

## Post #4 by @lassoan (2019-08-19 03:31 UTC)

<p>In recent Slicer Preview Releases, you can draw curves and get their surface area (2D surface, as you would expect - only one side, no thickness).</p>
<p>Select “Closed Curve” from the “Create and place” toolbar button:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d459c94af6ba0d0054e8f28404d91635078acf7.png" alt="image" data-base62-sha1="1TplEZMGMoJXDdxbqoiL5JEEdqn" width="405" height="482"></p>
<p>Left-click on the image to place curve control points and right-click to finish placement:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/afbfca82fc601e6495718a98b3c4735dc5f340bd.jpeg" data-download-href="/uploads/short-url/p4Kt09z7g2nQyXrcfHragp55kPb.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/afbfca82fc601e6495718a98b3c4735dc5f340bd_2_382x500.jpeg" alt="image" data-base62-sha1="p4Kt09z7g2nQyXrcfHragp55kPb" width="382" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/afbfca82fc601e6495718a98b3c4735dc5f340bd_2_382x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/afbfca82fc601e6495718a98b3c4735dc5f340bd.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/afbfca82fc601e6495718a98b3c4735dc5f340bd.jpeg 2x" data-dominant-color="56504F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">470×614 79.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Measurements on curves are still work in progress, but you can open the Python console (Ctrl-3) and copy-paste the code below to see the surface area:</p>
<pre data-code-wrap="python"><code class="lang-python">curves=slicer.util.getNodesByClass("vtkMRMLMarkupsClosedCurveNode")
for curve in curves:
    surfaceAreaMm2 = slicer.modules.markups.logic().GetClosedCurveSurfaceArea(curve)
    print("Curve {0}: surface area = {1:.2f} mm2".format(curve.GetName(), surfaceAreaMm2))
</code></pre>

---

## Post #5 by @TANG (2019-08-21 01:34 UTC)

<p>thank you very much. I try it.</p>

---

## Post #6 by @muratmaga (2019-08-21 16:03 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Would this calculation work with a closed curved drawn on a 3D model/segmentation?</p>

---

## Post #7 by @lassoan (2019-08-21 16:34 UTC)

<p>It computes the area of the closed curve, even if the curve points are not coplanar because they were picked from a model surface. A soap-bubble-like surface is computed for 3D curves and surface of that is reported.</p>
<p>To see that surface, you can use this code snippet:</p>
<pre><code class="lang-python">curve=slicer.util.getNodesByClass("vtkMRMLMarkupsClosedCurveNode")[0]
crossSectionSurface = vtk.vtkPolyData()
areaMm2 = slicer.modules.markups.logic().GetClosedCurveSurfaceArea(curve, crossSectionSurface)
crossSectionSurfaceModel = slicer.modules.models.logic().AddModel(crossSectionSurface)
crossSectionSurfaceModel.SetName("{0} surface".format(curve.GetName()))
crossSectionSurfaceModel.CreateDefaultDisplayNodes()
crossSectionSurfaceModel.GetDisplayNode().BackfaceCullingOff()
crossSectionSurfaceModel.GetDisplayNode().SetColor(curve.GetDisplayNode().GetColor())
crossSectionSurfaceModel.GetDisplayNode().SetOpacity(0.5)
crossSectionSurfaceModel.SetDescription("Area[mm2] = {0:.2f}".format(areaMm2))
print("Curve {0}: surface area = {1:.2f} mm2".format(curve.GetName(), areaMm2))
</code></pre>

---

## Post #8 by @muratmaga (2019-08-21 18:14 UTC)

<p>Thanks Andras. This is awesome.</p>

---

## Post #9 by @Sunilkumar_Leishangt (2020-08-03 20:09 UTC)

<p>Sir… i need to calculate visceral and subcutaneous adipose tissue areas in abdominal ct scans…by adjusting HU between -30 to -190… my slicer is not showing those functions u r saying…pluz see this pic…pliz help<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14199bd7a7f54ed9a00384978071b885a3392cc2.jpeg" data-download-href="/uploads/short-url/2ROpMO5l6S9MysCBoM2PoJgMbdg.jpeg?dl=1" title="1596485293036-493539886" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/14199bd7a7f54ed9a00384978071b885a3392cc2_2_690x388.jpeg" alt="1596485293036-493539886" data-base62-sha1="2ROpMO5l6S9MysCBoM2PoJgMbdg" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/14199bd7a7f54ed9a00384978071b885a3392cc2_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/14199bd7a7f54ed9a00384978071b885a3392cc2_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/14199bd7a7f54ed9a00384978071b885a3392cc2_2_1380x776.jpeg 2x" data-dominant-color="7D7D7E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1596485293036-493539886</span><span class="informations">4160×2340 2.36 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @Sunilkumar_Leishangt (2020-08-03 20:11 UTC)

<p>I hav been calculating in siemens ct consoles in our institute… it is easy in dat…using ROI function in volume tool…but need to do in laptop as covid is not allowing me access in console</p>

---

## Post #11 by @muratmaga (2020-08-03 20:51 UTC)

<p>You are using an old version. Install the latest preview and you will have the other markup types available to you.</p>

---

## Post #12 by @pieper (2020-08-03 21:13 UTC)

<p><a class="mention" href="/u/sunilkumar_leishangt">@Sunilkumar_Leishangt</a> - can you try the method described in this post?  It would be great if you could compare it to results from the CT console and let us know how it goes.</p>
<p><a href="https://discourse.slicer.org/t/new-module-for-measuring-cross-section-area-of-segments/11293" class="inline-onebox">New module for measuring cross-section area of segments</a></p>

---

## Post #13 by @Sunilkumar_Leishangt (2020-08-04 05:46 UTC)

<p>Thanx… i shall try n let u know…<br>
Actually right now m on covid duty in PGIMER, Chandigarh, India… quarantined in a hotel…so the waifi is not good here…may b i shall take some time…thanks again.</p>

---

## Post #14 by @Sunilkumar_Leishangt (2020-08-07 22:10 UTC)

<p>Sir…can anyone help me on how to adjust HU</p>

---

## Post #15 by @Sunilkumar_Leishangt (2020-08-07 22:15 UTC)

<p>In the siemens console in my institute… i can adjust the HU in the right pannel from -30 to -120<br>
Correlating adipose tissue… i just have to use the ROI to demarcate the region inside which i want to calculate the adipose tissue…and then click on evaluate button…it automatically colours and calculates the area of adipose tissue or those from -30 to -190 HU lying inside the area i marked with ROI…Dats it…simple…<br>
But m puzzled with this</p>

---

## Post #16 by @lassoan (2020-08-07 22:49 UTC)

<p>You are already familiar with the Siemens console and that software has also much less features, so of course you feel that 3D Slicer is not as simple to use. However, if you spend a little time with Slicer, too, then you’ll find how to do the same things and much more, without any difficulties.</p>
<p>For example, to get area of tissue within a specific HU range in a specified region, you can do the following steps:</p>
<ul>
<li>Go to Segment editor module</li>
<li>Create new segment</li>
<li>Click Threshold effect, set voxel range to -190 … -30, and click “Use for masking”</li>
<li>Use any tools (Paint, Draw, Scissors, etc.) to define the region of interest (can be a single slice or you can segment many slices, to get cross-section areas in all those slices at once)</li>
<li>Go to “Segment cross-section area” module to get cross-section areas as a plot and/or table</li>
</ul>

---

## Post #17 by @Sunilkumar_Leishangt (2020-08-07 23:02 UTC)

<p>All these effects are shown blurred…i guess they r not installed…do i hav to download n install them…?</p>

---

## Post #18 by @lassoan (2020-08-07 23:20 UTC)

<aside class="quote no-group" data-username="Sunilkumar_Leishangt" data-post="17" data-topic="1549">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sunilkumar_leishangt/48/3876_2.png" class="avatar"> Sunilkumar_Leishangt:</div>
<blockquote>
<p>All these effects are shown blurred</p>
</blockquote>
</aside>
<p>You need to select a master volume (if not selected automatically) and create a new segment (click “Add” button).</p>

---

## Post #19 by @Sunilkumar_Leishangt (2020-08-07 23:51 UTC)

<p>Can u pliz demonstrate how to calculate area of adipose tissues inside peritonium and that of subcutaneous adipose tissue outside peritonium…</p>

---

## Post #20 by @Sunilkumar_Leishangt (2020-08-08 00:13 UTC)

<p>I hav set threshold n drawn the outline but the line disappears soon after completion of drawing even if i press a or enter…<br>
N i cant find “segment cross section area” anywhere…even in install extensions list…pliz help</p>

---

## Post #21 by @Sunilkumar_Leishangt (2020-08-08 01:07 UTC)

<p>I hav understood now how to calculate…but only one problem… the calculation comes in volume cm3 not in area cm2…</p>

---

## Post #22 by @lassoan (2020-08-08 01:40 UTC)

<p>“Segment cross section area” is only available in recent Slicer Preview Releases, in Sandbox extension.</p>

---

## Post #23 by @lqiu (2021-05-18 17:34 UTC)

<p>Hello, I recently segmented over 200 DICOM files of MRI enterographies where I segmented one mask of the psoas muscle and another mask of the paraspinal muscle. I then ask slicer to determine the 2D area of that one slice I segmented and divided by 2 as instructed. However, it seems like slicer takes account for the thickness of the slice (1mm, 3mm, 5mm, etc.) into the area output, so dividing the output by 2 would still have half the amount of that thickness. Is there a way to ONLY get the true 2D area without any thickness?</p>

---

## Post #24 by @lassoan (2021-05-18 17:52 UTC)

<p>If you segmented a single slice and the slice is so thick that the area of the side wall is not negligible (this should be very rare) then you can compute the circumference and cross-section area from the known volume, surface area, and slice thickness with a simple formula (because you have two unknowns <code>cross_section_area</code> and <code>circumference</code> and two equations: <code>volume = cross_section_area * slice_thickness</code> and <code>surface_area = 2 * cross_section_area + circumference * slice_thickness</code>).</p>
<p>Alternatively, you can also use <a href="https://discourse.slicer.org/t/new-module-for-measuring-cross-section-area-of-segments/11293">Segment Cross-Section Area</a> module as described above (this is mostly useful if you have segmented on many slices).</p>
<p>In the future, you can measure 2D surface area directly using Closed curve markups:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c1f878ed57053691e50691f2145e5ba534e0ca6.jpeg" data-download-href="/uploads/short-url/mh82ixGbbsLNJ9nojL6pXwdwSvY.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c1f878ed57053691e50691f2145e5ba534e0ca6_2_690x368.jpeg" alt="image" data-base62-sha1="mh82ixGbbsLNJ9nojL6pXwdwSvY" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c1f878ed57053691e50691f2145e5ba534e0ca6_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c1f878ed57053691e50691f2145e5ba534e0ca6_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c1f878ed57053691e50691f2145e5ba534e0ca6_2_1380x736.jpeg 2x" data-dominant-color="9E9E9A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2156×1152 325 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #25 by @Numan_Kutaiba (2022-01-20 21:11 UTC)

<p>When you segment an area on a single slice, calculate the volume for the segmented area. Then multiply the volume in cm3 x (10/slice thickness in mm). This will give you the area in cm2.</p>
<p>This is because the volume is calculated by multiplying the area x slice thickness which is usually less than 1 cm (10mm).</p>
<p>If you do not know the slice thickness, go to DICOM from the drop down menu, then right-click to get DICOM metadata and search for slice thickness.</p>

---

## Post #26 by @Dryan711 (2023-03-30 08:06 UTC)

<p>Hello! Sir. I used this algorithm to find the area of a closed curve in a 2D film plane, but the result I get is wrong. Is it because the algorithm does not support this situation?</p>

---

## Post #27 by @lassoan (2023-03-30 12:09 UTC)

<p>3D Slicer can measure cross-sectional area, surface area, volume, etc. various ways. They are all correct, but they may be used improperly (e.g., you measure surface area and you interpret it as cross-sectional area).</p>
<p>Above we discussed many different methods. Which one did you use? What kind of data you measured on? How the image was acquired (provided as a DICOM file by a medical device, captured using a flatbed scanner and saved as TIFF, captured using a digital camera and saved as JPEG,…)? What result did you get? What result did you expect?</p>

---

## Post #28 by @Dryan711 (2023-03-31 13:51 UTC)

<p>Dear Professor:</p>
<p>Thanks for your reply!</p>
<p>I used 3D slicer 5.2.2. I have two formats for my images: provided as a DICOM file by a medical device (Eclipse treatment planning system, Varian), captured using a flatbed scanner and saved as TIFF (EBT3 film scanned by Epson V850 pro). The film mhd file is obtained through the dose curve.</p>
<p>I want to generate isodose lines in these images and use them as the outer contour to calculate the area inside the contour.</p>
<p>Hope your guidance!</p>
<p>Best wishes!</p>

---
