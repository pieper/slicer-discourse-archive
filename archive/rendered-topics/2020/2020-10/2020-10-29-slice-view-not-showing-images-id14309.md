# Slice view not showing images?

**Topic ID**: 14309
**Date**: 2020-10-29
**URL**: https://discourse.slicer.org/t/slice-view-not-showing-images/14309

---

## Post #1 by @adamrankin (2020-10-29 17:11 UTC)

<p>Hello,</p>
<p>In recent Slicer builds, images are not showing up in the slice view. The data probe shows correct pixel data, but the slice view is all black.</p>
<p>Has anyone else experienced this?</p>
<p>Adam</p>

---

## Post #2 by @jamesobutler (2020-10-29 17:23 UTC)

<p>It is the top open issue. See</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5220">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5220" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5220" target="_blank" rel="noopener nofollow ugc">VTK 9: Slicer viewer do not show the Slice</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-10-01" data-time="06:25:31" data-timezone="UTC">06:25AM - 01 Oct 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-12-04" data-time="15:19:53" data-timezone="UTC">03:19PM - 04 Dec 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener nofollow ugc">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Bug
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Priority: High
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Working on the slice view issue, here are some results.

Below are the **Resul<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ts**  obtained after running the **Test1** and **Test2** in two builds of Slicer, One with VTK8 and one with VTK9.

* VTK8: Slicer/Slicer@d52af6b303
* VTK9: This PR at https://github.com/Slicer/Slicer/pull/5141/commits/47672a73f6442205083b7ede0cd34696b92d652a

# Results

## Summary

| | VTK 8 | VTK 9 |
|---|----|---|
| Test1| :heavy_check_mark:  | :heavy_check_mark: |
| Test2|  :heavy_check_mark:  | :x: |

I suspect the problem is related to the use of [vtkLightBoxRendererManager](https://github.com/commontk/CTK/blob/support-build-with-vtk89/Libs/Visualization/VTK/Core/vtkLightBoxRendererManager.h) in [ctkVTKSliceView](https://github.com/commontk/CTK/blob/support-build-with-vtk89/Libs/Visualization/VTK/Widgets/ctkVTKSliceView.h)


## Outputs

| | VTK 8 | VTK 9 |
|---|----|---|
| Test1| ![image](https://user-images.githubusercontent.com/219043/92126306-04ee6680-edce-11ea-8b9d-da5024824099.png)  | ![image](https://user-images.githubusercontent.com/219043/92126424-28b1ac80-edce-11ea-955e-a5bd7ea0765f.png) |
| Test2|  ![image](https://user-images.githubusercontent.com/219043/92126511-44b54e00-edce-11ea-8f5b-3c4ed85c6ebc.png)  | ![image](https://user-images.githubusercontent.com/219043/92126607-631b4980-edce-11ea-9a48-a796af2e335f.png) |





# Tests

## Test1: Visualize slice pipeline output using vtkDataSetMapper/vtkRenderer/vtkRenderWindow

```python
import vtk
import SampleData

SampleData.downloadSample("MRHead")

sliceLogic = slicer.app.layoutManager().sliceWidget("Red").sliceLogic()
imageData = sliceLogic.GetImageDataConnection().GetProducer().GetOutputDataObject(0)

mapper = vtk.vtkDataSetMapper()

actor = vtk.vtkActor()
actor.SetMapper(mapper)

ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

ren.AddActor(actor)

renWin.SetSize(300,300)

mapper.SetInputData(imageData)
renWin.Render()
```

## Test2: Visualize slice pipeline output using ctkSliceView

```python
import ctk
import SampleData

SampleData.downloadSample("MRHead")

sliceLogic = slicer.app.layoutManager().sliceWidget("Red").sliceLogic()
imageDataConnection = sliceLogic.GetImageDataConnection()

sliceView = ctk.ctkVTKSliceView()
sliceView.setImageDataConnection(imageDataConnection)
sliceView.show()
sliceView.forceRender()
```

_Originally posted by @jcfr in https://github.com/Slicer/Slicer/pull/5141#issuecomment-686523379_</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote" data-post="2" data-topic="14267">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e79b87/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/only-black-image-shown-in-red-green-yellow-view/14267/2">Only black image shown in red/green/yellow view</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I tried some different versions of 3D Slicer: 
r29407: only black slices in the red/green/yellow views 
r29402: everything works fine 
So the problem appeared somewhere between those two versions.
  </blockquote>
</aside>
<aside class="quote quote-modified" data-post="1" data-topic="13973">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/a-few-problems-with-slicer-4-13/13973">A few problems with Slicer 4.13</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I know you are in a big process of upgrading Slicer with VTK9 in particular, and some runtime problems can be expected. Just reporting what I found so far on Arch Linux / Qt 5.15.1. 
Factory built Slicer 


Only Slicer appearence themes are proposed in Application Settings, and not system themes like Breeze and Oxygen. 


2D slice views are black empty. 


Home built Slicer 


2D slice views are black empty. 


Rotating 3D view with left mouse button down changes window state from maximized to ‘…
  </blockquote>
</aside>
<aside class="quote quote-modified" data-post="1" data-topic="13899">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/am_49/48/8346_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/no-image-comes-up-in-the-viewers-after-loading-data/13899">No images shown in slice viewers in latest preview release (Slicer-4.13.0)</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Problem report for Slicer 4.13.0-2020-10-05 win-amd64: [please describe expected and actual behavior] 
I am running Windows 10 on ASUS AiO desktop (Intel Core i5, RAM 16 GB, NVIDIA GeForce GTX 1050, updated drivers and application software). The loaded image is there - intensity values are displayed along with mouse cursor coordinates when moved over the viewers. The viewers brightness does not change, remains black when attempting to control it with mouse (left-click-and-drg in slice view). 
Wh…
  </blockquote>
</aside>


---
