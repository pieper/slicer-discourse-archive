---
topic_id: 6828
title: "Incorrect Overlay Of Vti And Stl From The Same Dicom Series"
date: 2019-05-17
url: https://discourse.slicer.org/t/6828
---

# Incorrect overlay of vti and stl from the same dicom series

**Topic ID**: 6828
**Date**: 2019-05-17
**URL**: https://discourse.slicer.org/t/incorrect-overlay-of-vti-and-stl-from-the-same-dicom-series/6828

---

## Post #1 by @rjsgml5698 (2019-05-17 02:47 UTC)

<p>Hello!</p>
<p>I have a question.</p>
<p>I want to implement volume rendering using vtk.js and overlay the segmented stl.</p>
<p>The following figure shows a screen with volume rendering and stl at the same time.</p>
<p>The problem occured here.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bb158c64dc5f6bbf34f2df24780525d39f6b150.png" data-download-href="/uploads/short-url/8w48kUj5YzHYCuAbShWk2ncZTFe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bb158c64dc5f6bbf34f2df24780525d39f6b150_2_690x325.png" alt="image" data-base62-sha1="8w48kUj5YzHYCuAbShWk2ncZTFe" width="690" height="325" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bb158c64dc5f6bbf34f2df24780525d39f6b150_2_690x325.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bb158c64dc5f6bbf34f2df24780525d39f6b150.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bb158c64dc5f6bbf34f2df24780525d39f6b150.png 2x" data-dominant-color="010809"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">794×374 27.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I used a 3d slicer to export stl and apply it, but it is not overlayed exactly.</p>
<p>I assumed that the location value would be the same because it was an exported stl file from the same dicom file.</p>
<p>But the result seems to be not.</p>
<p><strong>Is there an option to equalize positions in 3d slicer? Or is there a part I misunderstood in use?</strong></p>
<p>+(In the same dicom, vti files are exported from paraview and stl files are exported with 3dslicer)</p>

---

## Post #2 by @lassoan (2019-05-17 03:11 UTC)

<p>What coordinate system vtk.js renderer is using? LPS or RAS? Slicer uses RAS but LPS is more common. You may need to flip the first two axes (or choose LPS coordinate system when you export the segmentation using “Export to files”).</p>

---

## Post #4 by @rjsgml5698 (2019-05-17 04:45 UTC)

<p>Thank you for your comment.</p>
<p>The coordinate system of vtk.js seems to be LPS.</p>
<p>I am currently following your advice.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/1/15e764a601922e3dd95fd9af9b22d2483c7801b2.jpeg" data-download-href="/uploads/short-url/37LMDmCy1VaIq4f4JvlOIU0YLwm.jpeg?dl=1" title="image.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/15e764a601922e3dd95fd9af9b22d2483c7801b2_2_690x357.jpeg" alt="image.jpg" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/15e764a601922e3dd95fd9af9b22d2483c7801b2_2_690x357.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/15e764a601922e3dd95fd9af9b22d2483c7801b2_2_1035x535.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/15e764a601922e3dd95fd9af9b22d2483c7801b2_2_1380x714.jpeg 2x" data-dominant-color="8F9196"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">1916×992 506 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The STL was exported based on the LPS system. The exported stl seems binary, is there an option to choose ascii?</p>
<p>Because my code does not seem to read the binary right now. So I have to select the ascii through the blender and save the stl file to render it.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/468210e453a7c539c93dad0862e3f1556734a1bf.png" alt="image" data-base62-sha1="a3K5skTVh51Pk1vKu7HwaOkJWIn" width="236" height="263"></p>
<p>As a result, the same result was obtained. Is it a problem to re-export stl files in ascii format via blender?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/487cf30d4b05b343aa6c538889c25540cd1625a7.png" data-download-href="/uploads/short-url/alg50uzASmZreJUPThyF3shdhFd.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/487cf30d4b05b343aa6c538889c25540cd1625a7_2_438x500.png" alt="image.png" data-base62-sha1="alg50uzASmZreJUPThyF3shdhFd" width="438" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/487cf30d4b05b343aa6c538889c25540cd1625a7_2_438x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/487cf30d4b05b343aa6c538889c25540cd1625a7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/487cf30d4b05b343aa6c538889c25540cd1625a7.png 2x" data-dominant-color="010708"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">629×717 31.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank  you!!</p>

---

## Post #5 by @lassoan (2019-05-17 11:44 UTC)

<p>Text format STL is very is much slower to read and takes much more space, so I would not complicate the segmentation export with an ASCII option.</p>
<p>However, you can read the binary STL file and write it as ASCII STL with a few lines of Python code (<a href="https://vtk.org/doc/nightly/html/classvtkSTLReader.html" rel="nofollow noopener">vtkSTLReader</a>, <a href="https://vtk.org/doc/nightly/html/classvtkSTLWriter.html" rel="nofollow noopener">vtkSTLWriter</a>).</p>

---

## Post #6 by @rjsgml5698 (2019-05-20 00:49 UTC)

<p>Thank you for your comment</p>
<p>I also think Text format STL is very inefficient.</p>
<p>I am using vtk.js. I’ll take a closer look at the STLReader in vtk.js.</p>
<p>Thanks!</p>

---
