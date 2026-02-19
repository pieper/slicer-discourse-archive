---
topic_id: 20669
title: "3D View Ruler Doesnt Change Units Suffix"
date: 2021-11-17
url: https://discourse.slicer.org/t/20669
---

# 3D view ruler doesn't change units suffix

**Topic ID**: 20669
**Date**: 2021-11-17
**URL**: https://discourse.slicer.org/t/3d-view-ruler-doesnt-change-units-suffix/20669

---

## Post #1 by @keri (2021-11-17 22:43 UTC)

<p>Hi,</p>
<p>When I add volume and change units from <code>mm</code> to say <code>m</code> I can see no difference on the ruler but in the same time the slice control widget’s spinbox changes units to meter. I suspect this is a bug?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a93a93b4e857c5902d3f6b138a569d10ed1177d1.png" data-download-href="/uploads/short-url/o94bYik69iaAsbHxbbqhfmLOi6R.png?dl=1" title="Screenshot from 2021-11-18 01-39-16" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a93a93b4e857c5902d3f6b138a569d10ed1177d1_2_690x388.png" alt="Screenshot from 2021-11-18 01-39-16" data-base62-sha1="o94bYik69iaAsbHxbbqhfmLOi6R" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a93a93b4e857c5902d3f6b138a569d10ed1177d1_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a93a93b4e857c5902d3f6b138a569d10ed1177d1_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a93a93b4e857c5902d3f6b138a569d10ed1177d1_2_1380x776.png 2x" data-dominant-color="9E9EA4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-11-18 01-39-16</span><span class="informations">1600×900 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is the code to create a volume:</p>
<pre data-code-wrap="python"><code class="lang-python">nodeName = "MyNewVolume"
imageSize = [10, 10, 10]
imageOrigin = [10.0, 0.0, 0.0]
imageSpacing = [1, 1.0, 1.0] 

scalars = vtk.vtkDoubleArray()
scalars.SetName("my_scalars")

for i in range(0, imageSize[0]*imageSize[1]*imageSize[2]):
    v = scalars.InsertNextValue(i)

# Create an image volume
imageData = vtk.vtkImageData()
imageData.SetDimensions(imageSize)
imageData.GetPointData().SetScalars(scalars)
# Create volume node
volumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", nodeName)
volumeNode.SetOrigin(imageOrigin)
volumeNode.SetSpacing(imageSpacing)
volumeNode.SetAndObserveImageData(imageData)
volumeNode.CreateDefaultDisplayNodes()
volumeNode.CreateDefaultStorageNode()
</code></pre>
<p>Slicer 4.11.2</p>

---

## Post #2 by @lassoan (2021-11-18 00:14 UTC)

<p>Not all widgets are unit-aware. See list of widgets that require update in this issue:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5040">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5040" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5040" target="_blank" rel="noopener">Fix custom unit management</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-07-11" data-time="18:44:38" data-timezone="UTC">06:44PM - 11 Jul 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">For numerical stability of various processing methods, it is important to avoid <span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">very small and very large numbers.

By default, Slicer uses millimeter as unit, therefore for microscopy images the image spacing could be very small (for example, 0.00006mm) and derived values even smaller (volume of a voxel would be 0.000000000000216mm3). This could lead to display issues (hard to read the numbers, not enough space to display them) and numerical instabilities and loss of precision. The solution is to use a more appropriate unit, such as micrometer or tenth of a micrometer.

Slicer allows specifying what is the unit of length values of the scene and has unit-aware slider and spinbox widgets to correctly display them. However, the implementation is not fully complete and consistent. Remaining tasks:

- [ ] Use unit-aware widgets (or unit-aware formatting) whenever displaying numerical values with units. There are a number of places where “mm” unit is hardcoded and should be display should be replaced with unit-aware widgets.
  - [ ] Transforms module display settings: I remember I had crashes with these widgets in Transform module’s display section and could not easily find the root cause, so just hardcoded mm, but we should give this another go. Examples include: view rulers (horizontal line at the bottom of views) and markups measurements (length of line and curves, surface area of closed curves).
  - [x] Markups measurements
  - [x] Slice offset slider
  - [ ] Segment statistics
  - [ ] Labelmap statistics
  - [ ] View ruler (horizontal ruler displayed in slice and 3D view nodes)
  - [ ] Models module, information section
- [ ] Importers should convert distance units. For example, when loading a DICOM file and the length unit is not mm, the voxel size must be scaled accordingly.
- [ ] Exporters should write distance units into files.
- [ ] CLI module interface should be made unit-aware.
- [ ] All transformable data in the scene must be rescaled when length unit is changed.
- [ ] All transformable data in the scene must be rescaled when a scene with a different unit is imported.

Until all these are implemented, a workaround is to enter values in a different unit (e.g., enter 0.06 "mm" instead of the real 0.06 micrometer), but don't change the unit in application settings. Then user would know that all units that Slicer displays in millimeters are actually in the other chosen unit (i.e., micrometer). See some more details and explanation here: https://discourse.slicer.org/t/distance-measurement-and-rendering-of-microscopy-images/791</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It would be great if you could work on this.</p>

---

## Post #3 by @keri (2021-11-18 00:19 UTC)

<p>Thank you, I will keep in mind</p>

---
