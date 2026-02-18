# VTK build fails on Windows in Debug mode

**Topic ID**: 42590
**Date**: 2025-04-16
**URL**: https://discourse.slicer.org/t/vtk-build-fails-on-windows-in-debug-mode/42590

---

## Post #1 by @ungi (2025-04-16 21:04 UTC)

<p>Hi, I followed the Slicer build instructions today on Windows with default CMake options. The Release build went well with no errors. But in Debug mode, one project from VTK resulted in a link error. Looks like the resulting binary would exceed the maximum size. Slicer couldn’t be build because of the dependencies.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Severity</th>
<th>Code</th>
<th>Description</th>
<th>Project</th>
<th>File</th>
<th>Line</th>
<th>Suppression State</th>
<th>Details</th>
</tr>
</thead>
<tbody>
<tr>
<td>Error</td>
<td>LNK1248</td>
<td>image size (1044EE70F) exceeds maximum allowable size (FFFFFFFF)</td>
<td>CommonCore-objects</td>
<td>C:\D\SD\VTK-build\Common\Core\CommonCore-objects.dir\Debug\CommonCore-objects.lib</td>
<td>1</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div>

---

## Post #2 by @ungi (2025-04-17 00:03 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> suggested to revert to the previous VTK version. With this setting in CMake, the build was successful: Slicer_VTK_VERSION_MINOR=2</p>

---

## Post #3 by @lassoan (2025-04-20 02:28 UTC)

<p>I could reproduce this issue independently from Slicer and determined what the root cause is. It is purely a VTK problem, so I’ve posted more details about this on the VTK forum:</p>
<aside class="onebox discoursetopic" data-onebox-src="https://discourse.vtk.org/t/vtk-9-4-debug-build-fails-with-msvc-due-to-image-size-exceeds-maximum-allowable-size/15520">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.vtk.org/t/vtk-9-4-debug-build-fails-with-msvc-due-to-image-size-exceeds-maximum-allowable-size/15520" target="_blank" rel="noopener" title="02:27AM - 20 April 2025">VTK – 20 Apr 25</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/369;"><img src="https://discourse.vtk.org/uploads/default/original/1X/b7d45ff6520965c4fbd148f8d0b1f7720956fa24.png" class="thumbnail" width="690" height="369"></div>

<div class="title-wrapper">
  <h3><a href="https://discourse.vtk.org/t/vtk-9-4-debug-build-fails-with-msvc-due-to-image-size-exceeds-maximum-allowable-size/15520" target="_blank" rel="noopener">VTK 9.4 debug build fails with MSVC due to "image size ... exceeds maximum...</a></h3>
  <div class="topic-category">
      <span class="badge-wrapper bullet">
        <span class="badge-category-bg" style="background-color: #0088CC;"></span>
        <span class="badge-category clear-badge">
          <span class="category-name">Development</span>
        </span>
      </span>
  </div>
</div>

  <p>Debug build of VTK-9.4 fail on Windows if VTK_ENABLE_KITS is enabled, with this error:   CommonCore-objects.dir\Debug\CommonCore-objects.lib : fatal error LNK1248: image size (10098384C) exceeds maximum allowable size (FFFFFFFF)...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
