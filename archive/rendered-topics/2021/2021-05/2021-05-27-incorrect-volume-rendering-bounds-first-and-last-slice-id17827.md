---
topic_id: 17827
title: "Incorrect Volume Rendering Bounds First And Last Slice"
date: 2021-05-27
url: https://discourse.slicer.org/t/17827
---

# Incorrect volume rendering bounds - first and last slice

**Topic ID**: 17827
**Date**: 2021-05-27
**URL**: https://discourse.slicer.org/t/incorrect-volume-rendering-bounds-first-and-last-slice/17827

---

## Post #1 by @alireza (2021-05-27 14:10 UTC)

<p><strong>Summary</strong>: volume rendering bounds are incorrect for the first and last slice and not consistent for CPU, GPU, and multi-volume settings</p>
<p>I was getting some wrong bounds on the volume rendering for vtk.js, but it seems to be in slicer as well. The test data to investigate can be found <a href="https://www.dropbox.com/sh/5bbydxnvl6vn87h/AAC306PdHRXyeu8WCGKe9DQQa?dl=0" rel="noopener nofollow ugc">here</a></p>
<p>I put a recording of this behavior in slicer here</p>
<aside class="onebox githubissue">
  <header class="source">

      <a href="https://github.com/Kitware/vtk-js/issues/1936#issuecomment-849659019" target="_blank" rel="noopener nofollow ugc">github.com/Kitware/vtk-js</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Kitware/vtk-js/issues/1936#issuecomment-849659019" target="_blank" rel="noopener nofollow ugc">Incorrect volume mapper bounds  </a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-05-25" data-time="20:14:58" data-timezone="UTC">08:14PM - 25 May 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/sedghi" target="_blank" rel="noopener nofollow ugc">
          <img alt="sedghi" src="https://avatars.githubusercontent.com/u/7490180?v=4" class="onebox-avatar-inline" width="20" height="20">
          sedghi
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type: bug 🐞</span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">### High-level description
Volume mapper bounds are incorrect


### Steps to<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> reproduce
&lt;!--
Steps to reproduce the behavior. If applicable, use:
  * lists
  * code snippets
    ```js
    code here
    ```
--&gt;

This is a bug for rendering the first and last slice.

 It is visible on any sample data (headsq.vti etc). Also, I have created a synthetic dicom data set with long stripes in each slice along the y-axis, which change position for each slice (illustration below).
In addition, if we manually change the intensity values of the first and last slice in `headsq.vti`, we can see the cut at the edges.
 




### Expected behavior
Bounds should be to the edge of the volume.

### Environment
- **vtk.js**:  17.xx, 18.xx
- **OS**:  MacOS
- **Browser**:  Chrome 90.0.4430.212

#### Code Sandbox link

https://codesandbox.io/s/volume-rendering-bounds-exp9h?file=/src/index.js


headsq.vti with the changed intensity value for the first and last slice
- As seen, the slice thickness is not consistent and the last slice is thinner (as if bounds are forcing it to get cut)
- If interpolation is nearest, the last slice is gone



#### With linear interpolation
![image](https://user-images.githubusercontent.com/7490180/119558297-3994ba80-bd6f-11eb-9f5f-c0ebc56ee546.png)

With nearest interpolation
![image](https://user-images.githubusercontent.com/7490180/119559871-38648d00-bd71-11eb-832e-6d2850865e2c.png)

This becomes more clear if we intentionally increase the slice thickness (below screenshot is from local running of demo, not in sandbox)
![image](https://user-images.githubusercontent.com/7490180/119562346-3a7c1b00-bd74-11eb-95ea-7d89cd1343f4.png)


Test dicom files can be downloaded from [my dropbox (9kb)-10 slices](https://www.dropbox.com/s/eng1kkqkl5ec49d/Archive.zip?dl=0) and can be dropped into paraview glance for volume rendering as well

Synthetic data illustration
![image](https://user-images.githubusercontent.com/7490180/119561408-1d931800-bd73-11eb-9728-74c334a59c05.png)


Paraview glance volume rendering on the left, with the slice rendering on the right

![image](https://user-images.githubusercontent.com/7490180/119563109-2be23380-bd75-11eb-8ffb-3e87b137c892.png)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I appreciate any comments</p>

---

## Post #2 by @pieper (2021-05-27 18:19 UTC)

<p>Thanks for the report <a class="mention" href="/u/alireza">@alireza</a>, I agree the behavior is not consistent and should be improved.  As in the vtkjs case it would help to know if this is an application issue or something in the library.  It would help to have a pure vtk example to diagnose.</p>

---

## Post #3 by @alireza (2021-05-27 19:14 UTC)

<p>Thank you <a class="mention" href="/u/pieper">@pieper</a><br>
I have created a code sandbox with vtk.js only functionalities here with another dataset though.<br>
I’m manually manipulating the first and last slice intensities to be large values for volume rendering to get shown.</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://codesandbox.io/favicon.ico" class="site-icon" width="15" height="15">

      <a href="https://codesandbox.io/s/volume-rendering-bounds-exp9h" target="_blank" rel="noopener nofollow ugc" title="07:32PM - 25 May 2021">CodeSandbox – 25 May 21</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:130/68;"><img src="https://codesandbox.io/api/v1/sandboxes/exp9h/screenshot.png" class="thumbnail" width="130" height="68"></div>

<h3><a href="https://codesandbox.io/s/volume-rendering-bounds-exp9h" target="_blank" rel="noopener nofollow ugc">volume-rendering-bounds - CodeSandbox</a></h3>

  <p>volume-rendering-bounds by sedghi using kw-web-suite, parcel-bundler, vtk.js</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @pieper (2021-05-27 19:18 UTC)

<p>Excellent, yes.  I was also thinking we should have the same thing in python so we can make sure all the renderers are consistent.</p>

---

## Post #5 by @alireza (2021-05-28 13:11 UTC)

<p>I created a repo with python implementation here. I’m seeing similar behavior.</p>
<p>I took the example from <a href="https://kitware.github.io/vtk-examples/site/Python/Medical/MedicalDemo4/" rel="noopener nofollow ugc">here</a> and adapted it.</p>
<p>It is using <code>vtkFixedPointVolumeRayCastMapper</code> for the volume mapper. Is there any other type of volume mappers available in vtk python? and what does slicer use?</p>
<p>I wanted to create a google colab, but vtk is not rendering there for some reason (probably rendering)</p>
<aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/sedghi/vtk-volume-render-bounds-bug" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/e32023d782f5122cb94ab5b816e23f0e02197795c8694ed5be2153df0ec183a4/sedghi/vtk-volume-render-bounds-bug" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/sedghi/vtk-volume-render-bounds-bug" target="_blank" rel="noopener nofollow ugc">sedghi/vtk-volume-render-bounds-bug</a></h3>


  <p><span class="label1">Contribute to sedghi/vtk-volume-render-bounds-bug development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @pieper (2021-05-28 14:23 UTC)

<p>Thanks <a class="mention" href="/u/alireza">@alireza</a>, this looks like exactly what we need.  Based on this would you be able to file an issue on the VTK (c++) bug tracker?</p>
<aside class="quote no-group" data-username="alireza" data-post="5" data-topic="17827">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alireza/48/67173_2.png" class="avatar"> alireza:</div>
<blockquote>
<p>s there any other type of volume mappers available in vtk python? and what does slicer use?</p>
</blockquote>
</aside>
<p><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/VolumeRendering/MRMLDM/vtkMRMLVolumeRenderingDisplayableManager.cxx">Slicer uses two mapper types</a>, <code>vtkFixedPointVolumeRayCastMapper</code> and <code>vtkGPUVolumeRayCastMapper</code>, but see <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/VolumeRendering/MRMLDM/vtkMRMLVolumeRenderingDisplayableManager.cxx#L240-L259">this comment</a> about how multi-volume is used.  As you showed in your video the three modes are inconsistent and it would be great if they could all have consistently correct behavior.</p>

---

## Post #7 by @lassoan (2021-05-28 20:45 UTC)

<p>I’ve run into similar issues before due to <a href="https://discourse.vtk.org/t/bounding-box-of-vtkimagedata/2178/4?u=lassoan">misinterpreting meaning vtkImageData bounds</a>. It all comes down to how you define “bounds” for a VTK data set. It makes things much simpler if bounds are computed as the box that contains all data points. It is very easy to compute this, it works for all data sets (polygonal and volumetric meshes, point sets, etc), and this is the definition that is used throughout VTK. However, developers often don’t know or forget that vtkImageData extends 0.5 voxel beyond its “bounds” (so <code>GetBounds()</code> output is not the same as the image’s physical bounds), which can lead to seemingly incorrect or inconsistent behavior. Sometimes these can be considered to be bugs, but often you can justify and document the current behavior instead of changing the behavior that so many current software depend on.</p>
<p>I’ve tested with your data set and it seems that all renderers use VTK bounds for rendering (not the physical bounds). Since this has been like this forever (and extrapolating the image might be complicated and/or computationally intensive), I don’t think that this will be changed. You can address this by adding a single-voxel boundary (e.g., repeating the border voxels or setting to some uniform value). Considering these, behavior of the 3 raycast mappers in VTK:</p>
<ul>
<li>GPU volume raycast mapper works consistently with all settings.</li>
<li>CPU volume raycast mapper’s nearest neighbor interpolation’s behavior is quite surprising (does not make sense to me) and I would consider it as a bug. You can report this to the VTK bugtracker, but since the mapper’s development stopped about 10-15 years ago and probably not many people care about rendering with nearest neighbor “interpolation”, probably if you need a fix then you would need to implement it yourself.</li>
<li>GPU multivolume raycast mapper indeed computes one side of the bounds incorrectly (it is asymmetric and inconsistent with all other mappers). This mapper is still a work in progress. It has many (more serious) issues. So, it makes sense to report this so that when VTK developers take care of the other issues then they fix this one, too. Submit the sample data set as a mha or non-compressed nrrd image instead of DICOM so that VTK developers can use it more easily.</li>
</ul>

---

## Post #8 by @alireza (2021-06-06 23:11 UTC)

<p>Thanks Steve,<br>
Thanks for the links, we had some progress in digging where the problem is coming from in vtk.js and updated the issue on vtk.js repo.<br>
I will file an issue on C++ bug tracker as well</p>

---

## Post #9 by @alireza (2021-06-06 23:18 UTC)

<p>Thanks Andras for your comprehensive reply,<br>
Yes, we have noticed the boundary issue as well and I also understand how it will break a lot of things that rely on it if it gets changed</p>
<p>Single-voxel boundary might make sense, but I was hoping whether we can fix this by adding a flag to volume mappers for the exactExtent (?) and default to be false so that it doesn’t break things up.</p>
<p>Please let me know your opinion about this</p>

---

## Post #10 by @lassoan (2021-06-07 00:06 UTC)

<p>Adding a flag (disabled by default) to enable extrapolation beyond the last voxel would be probably OK. This is what is implemented in <a href="https://vtk.org/doc/nightly/html/classvtkImageReslice.html#ab956ee3fe0b8e5427266f049db49da2a">vtkImageReslice::SetBorder</a>, so I think it would make sense to implement the same options for volume rendering, too.</p>
<p>If you care about half voxels at the boundary then it is important to note that showing something beyond the last voxel’s center is extrapolation (if you display interpolated voxel values, either by reslicing or volume rendering). You want to display information that you don’t have. You can try to guess what should be there (most common methods are duplication, mirroring, and wraparound) but it may have performance impact and if you make a bad choice then it can cause artifacts or cause quantification errors. So, overall, the safest solution is actually not to add an extrapolated border, for either slice or volume rendering views.</p>

---
