---
topic_id: 7081
title: "Slice Viewer Bug When Using Reformat"
date: 2019-06-08
url: https://discourse.slicer.org/t/7081
---

# Slice viewer bug when using reformat

**Topic ID**: 7081
**Date**: 2019-06-08
**URL**: https://discourse.slicer.org/t/slice-viewer-bug-when-using-reformat/7081

---

## Post #1 by @Amine (2019-06-08 12:22 UTC)

<p>Slicer version 4.10.1 r27931<br>
Windows 10<br>
There is this bug when using reformat module with “normal to camera” checked (happened 3 times after working fine for a while each time). The green slice (wich i used reformat on) goes completely green as you can see, turning off reformat or setting the slice to axial/coronal doesn’t solve it</p>
<p>saving the scene and restarting slicer solves the problem</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41e373453cfe4126db99f26358c05d153a4dd566.jpeg" data-download-href="/uploads/short-url/9oSlqhon46xxyB3Moduhysk9uqG.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/41e373453cfe4126db99f26358c05d153a4dd566_2_690x472.jpeg" alt="PNG" data-base62-sha1="9oSlqhon46xxyB3Moduhysk9uqG" width="690" height="472" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/41e373453cfe4126db99f26358c05d153a4dd566_2_690x472.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/41e373453cfe4126db99f26358c05d153a4dd566_2_1035x708.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41e373453cfe4126db99f26358c05d153a4dd566.jpeg 2x" data-dominant-color="758576"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1375×942 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Amine (2019-06-08 12:30 UTC)

<p>when i reloaded the scene, the same slice was so much zoomed in that a vertex (or even less) was filling all of it, i was also using shift+cursor drag on the 3d viewer if that helps</p>

---

## Post #3 by @pieper (2019-06-08 19:25 UTC)

<p>That’s odd - looks like the renderview got removed (or crashed) and the controller is stretched in the layout.  Can you look in the error log for any info? (use the menu below to get to the log files)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/598acfbb205f679fe5a0dff556919d4535e08324.png" alt="image" data-base62-sha1="cM7TCaT8MdyjMQzMe3HTHPenrrC" width="362" height="319"></p>

---

## Post #4 by @lassoan (2019-06-08 19:28 UTC)

<p>I could not reproduce the problem using 4.10.1 or recent 4.11 versions. Does the problem also occur with the latest preview (nightly) version? Can you give us a list of steps that reproduce the problem?</p>

---

## Post #5 by @Amine (2019-06-09 15:59 UTC)

<p>I did not try on the nightly version. The issue happened 3 times randomly (after everything working fine for around 20 minutes) when using Reformat module along with Shift+clic and segment editor tools, i will try to replicate the issue and keep you updated</p>
<p>here is the log file when the error happened:</p>
<pre><code>[ERROR][VTK] 08.06.2019 12:06:03 [vtkTransformPolyDataFilter (000001D5D07C7F50)] (D:\D\S\Slicer-4101-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data

[ERROR][VTK] 08.06.2019 12:06:03 [vtkTransformPolyDataFilter (000001D5D07C9670)] (D:\D\S\Slicer-4101-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data

[ERROR][VTK] 08.06.2019 12:06:09 [vtkTransformPolyDataFilter (000001D5D07C7F50)] (D:\D\S\Slicer-4101-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data

[ERROR][VTK] 08.06.2019 12:06:09 [vtkTransformPolyDataFilter (000001D5D07C9670)] (D:\D\S\Slicer-4101-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data

[ERROR][VTK] 08.06.2019 12:06:14 [vtkTransformPolyDataFilter (000001D5D07C7F50)] (D:\D\S\Slicer-4101-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data

[ERROR][VTK] 08.06.2019 12:06:14 [vtkTransformPolyDataFilter (000001D5D07C9670)] (D:\D\S\Slicer-4101-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data

[ERROR][VTK] 08.06.2019 12:06:24 [vtkTransformPolyDataFilter (000001D5D07C7F50)] (D:\D\S\Slicer-4101-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data

[ERROR][VTK] 08.06.2019 12:06:24 [vtkTransformPolyDataFilter (000001D5D07C9670)] (D:\D\S\Slicer-4101-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data

[ERROR][VTK] 08.06.2019 12:06:47 [vtkTransformPolyDataFilter (000001D5D07C7F50)] (D:\D\S\Slicer-4101-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data

[ERROR][VTK] 08.06.2019 12:06:47 [vtkTransformPolyDataFilter (000001D5D07C9670)] (D:\D\S\Slicer-4101-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data

[ERROR][VTK] 08.06.2019 12:06:58 [vtkTransformPolyDataFilter (000001D5D07C7F50)] (D:\D\S\Slicer-4101-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data

[ERROR][VTK] 08.06.2019 12:06:58 [vtkTransformPolyDataFilter (000001D5D07C9670)] (D:\D\S\Slicer-4101-build\VTK\Filters\General\vtkTransformPolyDataFilter.cxx:85) - No input data</code></pre>

---
