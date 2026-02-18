# Double click to maximize view

**Topic ID**: 15824
**Date**: 2021-02-03
**URL**: https://discourse.slicer.org/t/double-click-to-maximize-view/15824

---

## Post #1 by @pieper (2021-02-03 22:39 UTC)

<p>This OHIF feature request might be good for slicer too - any thoughts?</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/OHIF/Viewers/issues/2269" target="_blank" rel="noopener">github.com/OHIF/Viewers</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/OHIF/Viewers/issues/2269" target="_blank" rel="noopener">UI/UX - Double click viewport to toggle between full size and grid layout</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-02-03" data-time="22:08:10" data-timezone="UTC">10:08PM - 03 Feb 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/richsmith123" target="_blank" rel="noopener">
          <img alt="richsmith123" src="https://avatars.githubusercontent.com/u/23708609?v=4" class="onebox-avatar-inline" width="20" height="20">
          richsmith123
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">Hello,
In most commercial PACS viewers you can double click an image (a single viewport) to toggle between the grid layout (eg....</p>
</div>

<div class="labels">
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">Community: Question :question:</span>
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">Triage :white_flag:</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #2 by @lassoan (2021-02-04 20:09 UTC)

<p>Yes, many software makes temporary maximization of a single view easily accessible, and I agree that it would be useful to offer this in Slicer, too.</p>
<p>We can already add a keyboard shortcut to change the layout, but keyboard shortcuts are not easily discoverable. We could add an icon in the view controller, and maybe even associate double-click on an empty region to this function (although we already use double-click on image for resetting window/level in the “Adjust window/level” mouse mode).</p>

---

## Post #3 by @pieper (2021-02-04 20:10 UTC)

<p>Yes, an icon in the title bar would make sense - something like the fully screen icon in youtube.</p>

---

## Post #4 by @lassoan (2021-02-04 20:25 UTC)

<p>We already have an issue to track this: <a href="https://github.com/Slicer/Slicer/issues/1409" class="inline-onebox">Add shortcut to maximize the current/focus/active view · Issue #1409 · Slicer/Slicer · GitHub</a></p>

---

## Post #5 by @lassoan (2021-09-01 13:39 UTC)

<p>This has now been implemented in the latest Slicer Preview Release.</p>

---

## Post #6 by @ezgimercan (2024-07-16 20:57 UTC)

<p>Is there a way to disable this behavior with Python scripting ect? When I am interacting with 3D view, Slicer picks up my quick rotations as double click and more than once I found myself in an unwanted full screen.</p>
<p>P.S. You can never make everyone happy, right? I’ll probably get used to it but figure I’d ask if there is an easy way. Thanks!</p>

---

## Post #7 by @cpinter (2024-07-17 08:27 UTC)

<p>Please see this entry and several more below, they will serve as an example. The way to disable it will be to reroute it to an empty action (<code>WidgetEventNone</code>)<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#custom-shortcut-for-moving-crosshair-in-a-slice-view" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#custom-shortcut-for-moving-crosshair-in-a-slice-view</a></p>
<p>Update: And the event will be <code>vtk.vtkCommand.LeftButtonDoubleClickEvent</code></p>

---
