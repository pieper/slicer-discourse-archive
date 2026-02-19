---
topic_id: 16890
title: "Multivolume Data Load"
date: 2021-04-01
url: https://discourse.slicer.org/t/16890
---

# Multivolume data load

**Topic ID**: 16890
**Date**: 2021-04-01
**URL**: https://discourse.slicer.org/t/multivolume-data-load/16890

---

## Post #1 by @selmanca (2021-04-01 02:57 UTC)

<p>Operating system: Win 10<br>
Slicer version: 4.13.0 (Latest)<br>
Expected behavior: Loading multivolume data<br>
Actual behavior:</p>
<p>Hi developers,<br>
I am trying to load my t2 images map with different TEs and python interactor gives this message:</p>
<p>Loading with imageIOName: GDCM<br>
Window/level found in DICOM tags (center=3602.0, width=7204.0) has been applied to volume 8: SAG T2MAP<br>
Failed to read a multivolume: module ‘vtkmodules.all’ has no attribute ‘VTK_MAJOR_VERSION’<br>
Traceback (most recent call last):<br>
File “C:/Users/selma/AppData/Local/NA-MIC/Slicer 4.13.0-2021-03-27/bin/…/lib/Slicer-4.13/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 665, in load<br>
if vtk.VTK_MAJOR_VERSION &lt;= 5:<br>
AttributeError: module ‘vtkmodules.all’ has no attribute ‘VTK_MAJOR_VERSION’<br>
Could not load: SAG T2MAP - as a 8 frames MultiVolume by EchoTime as a MultiVolume</p>
<p>Thanks for any help you can offer.</p>

---

## Post #2 by @lassoan (2021-04-02 00:12 UTC)

<p>Thanks for reporting, the problem is resolved - see details here:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/5560" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5560" target="_blank" rel="noopener">Multivolume data load bug</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-03-31" data-time="19:14:22" data-timezone="UTC">07:14PM - 31 Mar 21 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2021-04-01" data-time="13:57:59" data-timezone="UTC">01:57PM - 01 Apr 21 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/selmanca" target="_blank" rel="noopener">
          <img alt="selmanca" src="https://avatars.githubusercontent.com/u/67283781?v=4" class="onebox-avatar-inline" width="20" height="20">
          selmanca
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">It is probably a simple bug because when I installed vtk on Conda, "vtk.VTK_MAJOR_VERSION" works but on Slicer it can't find...</p>
</div>

<div class="labels">
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:bug</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
