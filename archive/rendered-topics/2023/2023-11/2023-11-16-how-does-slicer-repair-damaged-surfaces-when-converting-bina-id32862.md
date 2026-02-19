---
topic_id: 32862
title: "How Does Slicer Repair Damaged Surfaces When Converting Bina"
date: 2023-11-16
url: https://discourse.slicer.org/t/32862
---

# How does slicer repair damaged surfaces when converting binary labelmap into closed surfaces?

**Topic ID**: 32862
**Date**: 2023-11-16
**URL**: https://discourse.slicer.org/t/how-does-slicer-repair-damaged-surfaces-when-converting-binary-labelmap-into-closed-surfaces/32862

---

## Post #1 by @aebopi1999 (2023-11-16 15:59 UTC)

<p>I noticed that in Slicer, when converting a binary labelmap to a closed surface, it automatically repairs damaged surfaces, as shown in the right image.</p>
<p><img src="https://lh3.googleusercontent.com/pw/ADCreHe_N6AjpZ9Ce48JNctUQSnYAoovFSRznjI0hhXN4DNqpl_6s38yCNbaJv0M2cZz4keR-X8F0fQdHZa29_Dv6rBCTjHsk3uZ6VJoMl9d1seZiVNHPJMtv5xuj_02h7N9kQwwptXQNLV-MJtcYSj0ExoAxJiXOzwKJvjyVgqjGjb5H2ARYW5mBM93MvPl6j1sW7DiN-GcsM75UlbtystJL3j122yZFTFmKCXyrSXvfaeCwQLFAn8OWdlP_RwcYK-nBb3iI3wVBUdXJJX0Csq68o3EAxtuN8jVB6LjSm1RVUeWIDV1BHmPbHKI-TdmLgLfrN1XM5gYiyYtuZyp0JjF38yIl-ae1ZoWWU-i1oYH3cf6Sru7RjA-UnYeW8-F_7-QY4yw6qrfoVHFJNsQFeoNg5vdQP-wuuZ5Untvo0Aiyt_cxyeZDKpZBVfkRhjH-kyy4dgPXtZwF3FVAMFIR8ACsXjnDstT3C1W_v2BxDe-3MGDWMh2MgCUY1Jd18CWhtfOisTm3hoBSxtJoBW9EHIaNPHtUJ4hItksTuqOCsHL6dzgLa2AlSQM6EywIikT7NmDTTTRJ7Br9u_2F73DA8CdPfFKSZuAzlA2NioABcgHlXiIZeX4bQf590GEFVTwTIKqXNvlbkmKcgTIbRNT8nRPPii7cbAW_o4k_zKs7zpkTsO-j9cwSzFLf3kcwUe9pXZ_Lg3s430fA6knWiVgLIJ8cke4V3C_RlU18hHbm54sCILAfPkvLqAgOVj0-tIqG1Y8UQJ3-iSyuiY5FtJiXZcJR65jbkEs6F5E1g573PhFXMeBsxd7raNns0idBPzgVozdc6918KONgf5r7KFZdHYYxdOOd8csoRplcCxl3kv0OpjUCrIwMQGkVzSQXbmOK2LKW69KBg03jzodfm9ch9Sk=w767-h380-s-no-gm?authuser=0" alt="Image" width="" height=""></p>
<p>However, when I tried to use some VTK methods to convert a labelmap to a closed surface, I couldn’t achieve the same result. My code is as follows:</p>
<pre data-code-wrap="python"><code class="lang-python">reader = vtk.vtkNIFTIImageReader()
reader.SetFileName(segmentation_file_path)
reader.Update()

desired_label = 1

threshold = vtk.vtkImageThreshold()
threshold.SetInputData(reader.GetOutput())

threshold.ThresholdBetween(desired_label, desired_label)
threshold.ReplaceInOn()
threshold.SetInValue(1)
threshold.ReplaceOutOn()
threshold.SetOutValue(0)

marching_cubes = vtk.vtkDiscreteFlyingEdges3D()
marching_cubes.SetInputConnection(threshold.GetOutputPort())
marching_cubes.SetValue(0, 1)

decimate_filter = vtk.vtkDecimatePro()
decimate_filter.SetInputConnection(marching_cubes.GetOutputPort())
decimate_filter.SetTargetReduction(0.3)

smooth_filter = vtk.vtkWindowedSincPolyDataFilter()
smooth_filter.SetInputConnection(decimate_filter.GetOutputPort())
smooth_filter.SetNumberOfIterations(15)
smooth_filter.BoundarySmoothingOff()
smooth_filter.FeatureEdgeSmoothingOff()
smooth_filter.SetFeatureAngle(120.01)
smooth_filter.SetPassBand(0.001)
smooth_filter.NonManifoldSmoothingOn()
smooth_filter.NormalizeCoordinatesOn()
smooth_filter.Update()

clean_filter = vtk.vtkCleanPolyData()
clean_filter.SetInputConnection(smooth_filter.GetOutputPort())
clean_filter.SetTolerance(0.0001)

stl_writer = vtk.vtkSTLWriter()
stl_writer.SetFileName(output_file_path)
stl_writer.SetInputConnection(clean_filter.GetOutputPort())
stl_writer.Write()
</code></pre>
<p>I want to know what methods I should use to repair the damaged surfaces in the left image of the illustration.</p>

---

## Post #2 by @aebopi1999 (2023-11-17 12:27 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9b9331eeac062bcc0d059e93b9f6d335f72b3c7.png" data-download-href="/uploads/short-url/sMwL7Hik92fsixGezNjWHpL2jFd.png?dl=1" title="cbfa473d723e8d1e5416cd926895e36" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9b9331eeac062bcc0d059e93b9f6d335f72b3c7_2_690x341.png" alt="cbfa473d723e8d1e5416cd926895e36" data-base62-sha1="sMwL7Hik92fsixGezNjWHpL2jFd" width="690" height="341" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9b9331eeac062bcc0d059e93b9f6d335f72b3c7_2_690x341.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9b9331eeac062bcc0d059e93b9f6d335f72b3c7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9b9331eeac062bcc0d059e93b9f6d335f72b3c7.png 2x" data-dominant-color="CDCED4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">cbfa473d723e8d1e5416cd926895e36</span><span class="informations">767×380 61.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
This is the picture mentioned.</p>

---
