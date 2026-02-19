---
topic_id: 13918
title: "Volume Display Interpolate Turned Off By Default In Newest S"
date: 2020-10-07
url: https://discourse.slicer.org/t/13918
---

# Volume display - Interpolate turned off by default in newest stable?

**Topic ID**: 13918
**Date**: 2020-10-07
**URL**: https://discourse.slicer.org/t/volume-display-interpolate-turned-off-by-default-in-newest-stable/13918

---

## Post #1 by @hherhold (2020-10-07 13:58 UTC)

<p>Hey all,</p>
<p>Newest stable looks awesome. Rock solid for me so far (MacOS).</p>
<p>I did notice that Interpolate is turned off by default in the Volumes module. Is this new?</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2020-10-07 20:32 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="1" data-topic="13918">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>Newest stable looks awesome. Rock solid for me so far (MacOS).</p>
</blockquote>
</aside>
<p><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji only-emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="hherhold" data-post="1" data-topic="13918">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>I did notice that Interpolate is turned off by default in the Volumes module. Is this new?</p>
</blockquote>
</aside>
<p>I don’t think we changed anything related to this. Is it possible that you changed this default in your application startup script (.slicerrc.py)?</p>

---

## Post #3 by @muratmaga (2020-10-07 20:53 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="13918">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I don’t think we changed anything related to this. Is it possible that you changed this default in your application startup script (.slicerrc.py)?</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/hherhold">@hherhold</a> did you install the .slicerrc.py we distribute during the slicerMorph workshop? That does disable the interpolation.</p>

---

## Post #4 by @hherhold (2020-10-07 21:16 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Hey, Murat, thanks for the reply. Nope - I’ve used bits and pieces from the .slicerrc.py you shared with me a while back, but nothing regarding interpolation. And I haven’t changed my .slicerrc.py in weeks.</p>
<p>I’ll double-check it against the 9-1 nightly (I keep a few around, just in case) and let you know.</p>

---

## Post #5 by @lassoan (2020-10-07 21:19 UTC)

<p>Note that using interpolation for image display is not just some trick or some arbitrary post-processing step that users may or may not want. Instead, interpolation provides (a good approximation) of the original continuous signal that is reconstructed from discrete point samples.</p>
<p>It is OK to temporarily disable interpolation for debugging or as a workaround for lack of image grid display during segmentation, but I don’t think it is a good idea to advertise disabling interpolation as a setting that users should use by default.</p>

---

## Post #6 by @jamesobutler (2020-10-07 21:25 UTC)

<p>The SlicerMorph extension is turning off interpolation by default if it is an installed extension?<br>
</p><aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/SlicerMorph/SlicerMorph/commit/3c304db06e3bbb9c6d880d22d735af89b1877322" target="_blank" rel="noopener nofollow ugc">github.com/SlicerMorph/SlicerMorph</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerMorph/SlicerMorph/commit/3c304db06e3bbb9c6d880d22d735af89b1877322" target="_blank" rel="noopener nofollow ugc">Add default SlicerMorphRC.py</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2020-09-30" data-time="18:56:29" data-timezone="UTC">06:56PM - 30 Sep 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener nofollow ugc">
          <img alt="pieper" src="https://avatars0.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
        
      </div>

      <div class="lines" title="changed 2 files with 121 additions and 22 deletions">
        <a href="https://github.com/SlicerMorph/SlicerMorph/commit/3c304db06e3bbb9c6d880d22d735af89b1877322" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+121</span>
          <span class="removed">-22</span>
        </a>
      </div>
    </div>

  </div>
</div>


  <div class="github-row">
    <pre class="github-content" style="white-space: normal;">Add the default cusomization behavior
including some shortcut keys and other
defaults to make morphometry easier.
Also add more options to the preferences
pane to...</pre>
  </div>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>cc: <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #7 by @pieper (2020-10-07 21:37 UTC)

<p>Yes, the most recent SlicerMorph has optional config with interpolation off, which I was told is the preference in that community.  You can either toggle off all SlicerMorph customizations (in the Edit-&gt;Application Preferences-&gt;SlicerMorph pane) or you can edit the SlicerMorphRC.py that we provide.</p>

---

## Post #8 by @lassoan (2020-10-07 23:46 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> What is the motivation for disabling interpolation? If it is just familiarity for the users then it may be managed by user training. If there are specific reasons then maybe they can be addressed directly, without disabling interpolation (e.g., display grid when voxel size reaches a certain threshold).</p>

---

## Post #9 by @muratmaga (2020-10-07 23:49 UTC)

<p>Most of our users need to use the manual segmentation as they are working on the microCT scans of dry bones in which intensity based tools don’t work well. In such cases, it is better to be able to see the voxel boundaries clearly (e.g., so that you can find the gap between the cranial sutures).</p>
<p>What is the benefit of interpolation in the slice view?</p>

---

## Post #10 by @lassoan (2020-10-08 04:41 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="9" data-topic="13918">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>What is the benefit of interpolation in the slice view?</p>
</blockquote>
</aside>
<p>Interpolated image shows you the faithfully reconstructed continuous signal from the discrete samples. This reconstruction is lossless if sample-rate criterion is satisfied (see more details <a href="https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem">here</a>). The criterion is not always satisfied - that’s when you see staircase artifacts in the reconstructed image (in both slice views, volume rendering, and reconstructed surfaces):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e2131f4e5e4dfc53650494641005ab3d8014a49.jpeg" data-download-href="/uploads/short-url/8RCIQSyJC6Le9lCBgPunGs1bNq1.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3e2131f4e5e4dfc53650494641005ab3d8014a49_2_515x500.jpeg" alt="image" data-base62-sha1="8RCIQSyJC6Le9lCBgPunGs1bNq1" width="515" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3e2131f4e5e4dfc53650494641005ab3d8014a49_2_515x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3e2131f4e5e4dfc53650494641005ab3d8014a49_2_772x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3e2131f4e5e4dfc53650494641005ab3d8014a49_2_1030x1000.jpeg 2x" data-dominant-color="484543"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1160×1126 260 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Interpolation is still about the best thing you can do, and definitely provides much more faithful reconstruction of the original signal than no interpolation (= nearest neighbor interpolation). Also, you can always make the sample-rate criterion satisfied by applying a low-pass filter on the data. That’s why we always apply surface smoothing when surface is reconstructed from from labelmap volume.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="9" data-topic="13918">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>they are working on the microCT scans of dry bones in which intensity based tools don’t work well. In such cases, it is better to be able to see the voxel boundaries clearly</p>
</blockquote>
</aside>
<p>You should be able to see small details better when interpolation is used. For example, try to draw the dark separating line in this image when it is displayed with/without interpolation:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8db9a31cfec55122a2e7162bc4e9332b98163b49.jpeg" data-download-href="/uploads/short-url/kdL32NVaMDTmCaElhFLyKPqfe7n.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8db9a31cfec55122a2e7162bc4e9332b98163b49_2_648x500.jpeg" alt="image" data-base62-sha1="kdL32NVaMDTmCaElhFLyKPqfe7n" width="648" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8db9a31cfec55122a2e7162bc4e9332b98163b49_2_648x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8db9a31cfec55122a2e7162bc4e9332b98163b49_2_972x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8db9a31cfec55122a2e7162bc4e9332b98163b49_2_1296x1000.jpeg 2x" data-dominant-color="BBB7AE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1406×1084 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You need to squint your eye and guess where to draw when voxels are shown without interpolation, while it is quite straightforward on the interpolated image.</p>
<p>I agree that it can be useful to show the voxel grid during segmentation so that you know how fine details you can paint and where. Note that this is the grid of the binary labelmap representation of the segmentation and not the grid of the background scalar volume.</p>
<p>We could quite easily add this grid display option to the segmentation displayable manager (above a certain zoom factor). You can simulate it with this Python code snippet:</p>
<pre data-code-wrap="python"><code class="lang-python">import SampleData
volumeNode = SampleData.SampleDataLogic().downloadCTACardio()

import numpy as np

ijkToRasVtk = vtk.vtkMatrix4x4()
volumeNode.GetIJKToRASMatrix(ijkToRasVtk)
ijkToRas = slicer.util.arrayFromVTKMatrix(ijkToRasVtk)

volumeExtent = np.array(volumeNode.GetImageData().GetExtent(), dtype=float)
volumeExtent[0] -= 0.5
volumeExtent[2] -= 0.5
volumeExtent[4] -= 0.5
volumeExtent[1] += 0.5
volumeExtent[3] += 0.5
volumeExtent[5] += 0.5

dimensions = volumeNode.GetImageData().GetDimensions()

pts = vtk.vtkPoints()
quads = vtk.vtkCellArray()

for axisIndex in range(3):
    if axisIndex == 0:
        pointsIjk = np.array([
            [volumeExtent[0], volumeExtent[2], volumeExtent[4], 1.0],
            [volumeExtent[0], volumeExtent[3], volumeExtent[4], 1.0],
            [volumeExtent[0], volumeExtent[3], volumeExtent[5], 1.0],
            [volumeExtent[0], volumeExtent[2], volumeExtent[5], 1.0]]).T
        offsetIjk = np.array([[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]], dtype=float).T
    elif axisIndex == 1:
        pointsIjk = np.array([
            [volumeExtent[0], volumeExtent[2], volumeExtent[4], 1.0],
            [volumeExtent[1], volumeExtent[2], volumeExtent[4], 1.0],
            [volumeExtent[1], volumeExtent[2], volumeExtent[5], 1.0],
            [volumeExtent[0], volumeExtent[2], volumeExtent[5], 1.0]]).T
        offsetIjk = np.array([[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]], dtype=float).T
    else:
        pointsIjk = np.array([
            [volumeExtent[0], volumeExtent[2], volumeExtent[4], 1.0],
            [volumeExtent[1], volumeExtent[2], volumeExtent[4], 1.0],
            [volumeExtent[1], volumeExtent[3], volumeExtent[4], 1.0],
            [volumeExtent[0], volumeExtent[3], volumeExtent[4], 1.0]]).T
        offsetIjk = np.array([[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]], dtype=float).T
    pointsRas = np.dot(ijkToRas, pointsIjk)
    offsetRas = np.dot(ijkToRas, offsetIjk)
    for planeIndex in range(dimensions[axisIndex]+1):
        quads.InsertNextCell(4)
        for pointIndex in range(4):
            quads.InsertCellPoint(pts.InsertNextPoint(pointsRas[0][pointIndex], pointsRas[1][pointIndex], pointsRas[2][pointIndex]))
        pointsRas += offsetRas

gridPoly = vtk.vtkPolyData()
gridPoly.SetPoints(pts)
gridPoly.SetPolys(quads)

gridModelNode = slicer.modules.models.logic().AddModel(gridPoly)
gridModelDisplayNode = gridModelNode.GetDisplayNode()
gridModelDisplayNode.SetVisibility2D(True)
gridModelDisplayNode.SetOpacity(0.3)
gridModelDisplayNode.SetVisibility3D(False)

# Running this line of code will show/hide the grid:
# gridModelDisplayNode.SetVisibility(not gridModelDisplayNode.GetVisibility())
</code></pre>
<p>See how the grid shows more relevant information than the non-interpolated master volume, especially when resolution of segmentation differs from the resolution of the master volume:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d27d59f16eae135f19dc16416064ad9365b72ab.png" data-download-href="/uploads/short-url/hRb1MtEbzNODQU7h8i9o7XZhVl9.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d27d59f16eae135f19dc16416064ad9365b72ab_2_690x331.png" alt="image" data-base62-sha1="hRb1MtEbzNODQU7h8i9o7XZhVl9" width="690" height="331" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d27d59f16eae135f19dc16416064ad9365b72ab_2_690x331.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d27d59f16eae135f19dc16416064ad9365b72ab_2_1035x496.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d27d59f16eae135f19dc16416064ad9365b72ab_2_1380x662.png 2x" data-dominant-color="ADABA2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2372×1138 563 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It is interesting to note that this way of showing the grid works well for arbitrarily reformatted slices:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de3222c9f1eeb3267d69733fa1e42e7194e4a365.png" data-download-href="/uploads/short-url/vHDpFMVcEUdAJiBFonSWJBZ0QSh.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de3222c9f1eeb3267d69733fa1e42e7194e4a365.png" alt="image" data-base62-sha1="vHDpFMVcEUdAJiBFonSWJBZ0QSh" width="534" height="500" data-dominant-color="787A76"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1160×1085 23.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<hr>
<p>It would be great if you could play around with the Python code snippet above and if you find grid display useful then we can discuss about adding it to segmentation displayable manager (similarly to how it worked in Slicer3).</p>

---

## Post #11 by @pieper (2020-10-08 18:02 UTC)

<p>Good explanation Andras.</p>
<p>Yes, we had the voxel grid option in Slicer3 and I sometimes found it helpful, but we ultimately never ported it because turning off  interpolation was just as easy, less visual clutter, and more informative.  One motivation for turning off interpolation is to understand the partial voluming that comes from thick slices, but personally I would usually leave it off.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> - it would be possible to move this from the SlicerMorphRC.py script to the SlicerMorph Preferences as a checkbox, so that users could easily decide which mode they prefer.</p>

---

## Post #12 by @muratmaga (2020-10-08 19:22 UTC)

<p>Here is an example. This is the mouse molar row, showing first molar and tiny bit of the second one. If the interpolation is on, these structures appear continuous. There is a tiny gap, probably much smaller than the voxel size between then, which becomes more clear if the interpolation is off.</p>
<p>We often have to segment things like this. Seeing voxel boundaries makes it a bit more clear.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/059daeab47916cbc349b1fbf294d64a7640f6f57.png" data-download-href="/uploads/short-url/NGdE9JO8ZnHCAuGIhZkna1qA07.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/059daeab47916cbc349b1fbf294d64a7640f6f57_2_556x500.png" alt="image" data-base62-sha1="NGdE9JO8ZnHCAuGIhZkna1qA07" width="556" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/059daeab47916cbc349b1fbf294d64a7640f6f57_2_556x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/059daeab47916cbc349b1fbf294d64a7640f6f57_2_834x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/059daeab47916cbc349b1fbf294d64a7640f6f57.png 2x" data-dominant-color="6D6D6D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">973×874 58.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/302499c4416eb7b7135cf6803b62d87e96bd82f0.jpeg" data-download-href="/uploads/short-url/6RTkMb8UQ9RHIGaDN3G8wlP7JEQ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/302499c4416eb7b7135cf6803b62d87e96bd82f0_2_386x500.jpeg" alt="image" data-base62-sha1="6RTkMb8UQ9RHIGaDN3G8wlP7JEQ" width="386" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/302499c4416eb7b7135cf6803b62d87e96bd82f0_2_386x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/302499c4416eb7b7135cf6803b62d87e96bd82f0_2_579x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/302499c4416eb7b7135cf6803b62d87e96bd82f0.jpeg 2x" data-dominant-color="868686"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">601×777 35.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @lassoan (2020-10-08 20:31 UTC)

<p>You may “feel” that you see something better in the pixelated image, but that may not be real. You could say that you can perfectly reconstruct the image, mentally, from the displayed samples, but that would only work in 2D images - in 3D volumes you would need to take into account voxel values in neighbor slices, which are not displayed in the slice view at all.</p>
<p>Choosing between nearest neighbor or higher-order interpolations is not some user preference, but nearest neighbor is objectively worse, it has much larger error in reproducing the real continuous image.</p>
<p>There are also practical reasons why disabling interpolation to see the image grid is not a good solution.</p>
<ol>
<li>Showing pixelated image does not work well when neighbor voxels happen to have similar intensity (you need to boost up the contrast to see voxel boundaries, but then you need to bring the contrast back if you want to interpret the image).</li>
<li>Background image grid is not always the same as the grid of segmentation labelmap representation (see example above).</li>
</ol>
<p>There could be some new “index mode” operation of Slicer, when everything is consistently constrained to integer positions (even markup points, lines, surface meshes, etc.), but it would be very limiting, it would only be useful for extremely low resolution or highly anisotropic images, would be a lot of work to implement, could be confusing for users, and you cannot do much 3D processing with such poorly sampled images anyway.</p>

---

## Post #14 by @pieper (2020-10-08 20:48 UTC)

<p>Another issue with nearest neighbor is that it falls apart when you rotate the sample plane.</p>
<p>To Murat’s point though, there are some cases where NN sampling might give you some hints about the fine detail that is otherwise smoothed out by interpolation when you are at the limits of resolution.</p>
<p>Consider a 1D example NN sampling of a sine wave. If it is at the right at twice the sampling frequency, you’ll get alternating positive and negative  pixel values.  But with linear interpolation you would get all zero values.</p>

---

## Post #15 by @lassoan (2020-10-08 22:30 UTC)

<aside class="quote no-group" data-username="pieper" data-post="14" data-topic="13918">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Consider a 1D example NN sampling of a sine wave. If it is at the right at twice the sampling frequency, you’ll get alternating positive and negative pixel values. But with linear interpolation you would get all zero values.</p>
</blockquote>
</aside>
<p>I’m not sure I understand this correctly. If you use nearest neighbor then you get square wave, while linear interpolation provides triangle wave (not a constant). Triangle wave is more similar to sine wave than square wave.</p>
<p>Sinc kernel would reproduce the sine wave perfectly at any resolution (provided the input sampling was dense enough for the signal bandwidth), but linear is good enough for most cases.</p>

---

## Post #16 by @pieper (2020-10-09 00:48 UTC)

<p>If you have dense sampling (zoomed in), yes, you will get a triangle wave, but if your pixel sampling grid is close to the voxel sample spacing but they are not aligned (e.g. panned by half a pixel) then linear interpolation will lose the peaks of a high frequency signal.  So with NN you will get aliasing but may also get visual clues about fine details.</p>
<p>I’m not sure when it was added but <a href="https://vtk.org/doc/nightly/html/classvtkImageReslice.html#abf45cdc75808e0e7836cb529beec43e2">vtkImageReslice</a> supports <a href="https://vtk.org/doc/nightly/html/classvtkAbstractImageInterpolator.html">sinc</a> if anyone feels like trying it out.  It’s probably fast enough for real time for most window sizes / CPUs.</p>

---

## Post #17 by @lassoan (2020-10-09 02:12 UTC)

<p>Thanks for the suggestion, it is very interesting to compare appearance of interpolated/non-interpolated image when voxel size is approximately the same as the pixel size on the display. I created a video of a continuous zoom from smaller voxels than display pixels to much larger voxels than display pixels (and zoomed in the video 4x so that it is easier to see differences):</p>
<div class="youtube-onebox lazy-video-container" data-video-id="s5ufry8eqxk" data-video-title="Interpolated/non-interpolated side-by-side zoom" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=s5ufry8eqxk" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/s5ufry8eqxk/hqdefault.jpg" title="Interpolated/non-interpolated side-by-side zoom" width="" height="">
  </a>
</div>

<p>If image is not interpolated then there are waves running over the image as you zoom in (or pan), depending on which voxels are skipped when voxel size is similar to display pixel size. If image is interpolated then zoom is continuous, smooth. Without the 4x zoom, the waves are barely visible on a modern high-resolution screen, so in everyday usage these artifacts are not that distracting.</p>
<p>At the very end there is a very clearly recognizable C-shaped dark structure in the interpolated image, but it is barely visible in the non-interpolated image, probably because our eyes do not average voxel intensities very well. For me, this image demonstrates very well why we need to use interpolation for image display.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca7f03c5829f8da8652c8f5050dce12b0111e7e5.jpeg" data-download-href="/uploads/short-url/sTmzLn8WjLBZ1osafsxQecSxTMh.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca7f03c5829f8da8652c8f5050dce12b0111e7e5_2_690x448.jpeg" alt="image" data-base62-sha1="sTmzLn8WjLBZ1osafsxQecSxTMh" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca7f03c5829f8da8652c8f5050dce12b0111e7e5_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca7f03c5829f8da8652c8f5050dce12b0111e7e5.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca7f03c5829f8da8652c8f5050dce12b0111e7e5.jpeg 2x" data-dominant-color="525252"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">790×514 34.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
