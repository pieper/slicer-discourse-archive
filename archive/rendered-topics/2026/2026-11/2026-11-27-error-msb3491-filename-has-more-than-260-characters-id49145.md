---
topic_id: 49145
title: "Error MSB3491, filename has more than 260 characters"
date: 2026-11-27
url: https://discourse.slicer.org/t/49145
last_bumped: 2026-11-28T01:07:23.927Z
---

# Error MSB3491, filename has more than 260 characters

**Topic ID**: 49145
**Date**: 2026-11-27
**URL**: https://discourse.slicer.org/t/error-msb3491-filename-has-more-than-260-characters/49145

---

## Post #1 by @mau_igna_06 (2026-11-27 17:31 UTC)

<p>Hi,</p>
<p>It’s the first time in a few years that I’m building Slicer on Windows. I did a release build according to latest documentation but I get:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51a769d2140a5b3d92985ac7757c36b743769f0e.png" data-download-href="/uploads/short-url/bElm6GWKE4g604MNHefL42LSC3Y.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51a769d2140a5b3d92985ac7757c36b743769f0e_2_690x388.png" alt="image" data-base62-sha1="bElm6GWKE4g604MNHefL42LSC3Y" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51a769d2140a5b3d92985ac7757c36b743769f0e_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51a769d2140a5b3d92985ac7757c36b743769f0e_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51a769d2140a5b3d92985ac7757c36b743769f0e_2_1380x776.png 2x" data-dominant-color="29292A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2559×1439 372 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>(6 files have too long names)</p>

---

## Post #2 by @jamesobutler (2026-11-28 01:07 UTC)

<p>I ran into it during a packaging step on Windows. See written GitHub issue below where you can provide your observations as well.</p>
<aside class="onebox githubissue github-onebox" data-onebox-src="https://github.com/Slicer/Slicer/issues/9586">
    <header class="source github-onebox__header">
  <span class="github-onebox__label" role="img" aria-label="Open issue" title="Open issue">
    <svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path></svg>
    <span>Open issue</span>
  </span>
    <a class="github-onebox__repo" href="https://github.com/Slicer/Slicer/issues/9586" target="_blank" rel="noopener nofollow ugc">
      <svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M6.766 11.328c-2.063-.25-3.516-1.734-3.516-3.656 0-.781.281-1.625.75-2.188-.203-.515-.172-1.609.063-2.062.625-.078 1.468.25 1.968.703.594-.187 1.219-.281 1.985-.281.765 0 1.39.094 1.953.265.484-.437 1.344-.765 1.969-.687.218.422.25 1.515.046 2.047.5.593.766 1.39.766 2.203 0 1.922-1.453 3.375-3.547 3.64.531.344.89 1.094.89 1.954v1.625c0 .468.391.734.86.547C13.781 14.359 16 11.53 16 8.03 16 3.61 12.406 0 7.984 0 3.563 0 0 3.61 0 8.031a7.88 7.88 0 0 0 5.172 7.422c.422.156.828-.125.828-.547v-1.25c-.219.094-.5.156-.75.156-1.031 0-1.64-.562-2.078-1.609-.172-.422-.36-.672-.719-.719-.187-.015-.25-.093-.25-.187 0-.188.313-.328.625-.328.453 0 .844.281 1.25.86.313.452.64.655 1.031.655s.641-.14 1-.5c.266-.265.47-.5.657-.656"></path></svg>
      <span>Slicer/Slicer</span>
    </a>
</header>


  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/9586" target="_blank" rel="noopener nofollow ugc">Errors during Windows packaging</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2026-11-26" data-time="01:04:48" data-timezone="UTC">01:04AM - 26 Nov 26 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

With environment Visual Studio 2026 (18.12.0), CMake 4.5.0, Qt 6.11.<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">3 and building Slicer as of https://github.com/Slicer/Slicer/commit/b48ed846855eccca1dc695dd2eed6e806c69be2f, I observed some errors during the packaging step

```
454&gt;C:\Program Files\Microsoft Visual Studio\18\Professional\MSBuild\Microsoft\VC\v180\Microsoft.CppBuild.targets(358,5): error MSB3501: Could not read lines from file "x64\Release\qSlicerTransformsSubjectHierarchyPluginsPythonQt_autogen_timestamp_deps\qSlicerT.0D765B61.tlog\qSlicerTransformsSubjectHierarchyPluginsPythonQt_autogen_timestamp_deps.lastbuildstate". Could not find a part of the path 'C:\S5R\Slicer-build\Modules\Loadable\Transforms\SubjectHierarchyPlugins\x64\Release\qSlicerTransformsSubjectHierarchyPluginsPythonQt_autogen_timestamp_deps\qSlicerT.0D765B61.tlog\qSlicerTransformsSubjectHierarchyPluginsPythonQt_autogen_timestamp_deps.lastbuildstate'.
463&gt;C:\Program Files\Microsoft Visual Studio\18\Professional\MSBuild\Microsoft\VC\v180\Microsoft.CppBuild.targets(358,5): error MSB3501: Could not read lines from file "x64\Release\qSlicerSegmentationsSubjectHierarchyPluginsPythonQt_autogen_timestamp_deps\qSlicerS.13F809CD.tlog\qSlicerSegmentationsSubjectHierarchyPluginsPythonQt_autogen_timestamp_deps.lastbuildstate". Could not find a part of the path 'C:\S5R\Slicer-build\Modules\Loadable\Segmentations\SubjectHierarchyPlugins\x64\Release\qSlicerSegmentationsSubjectHierarchyPluginsPythonQt_autogen_timestamp_deps\qSlicerS.13F809CD.tlog\qSlicerSegmentationsSubjectHierarchyPluginsPythonQt_autogen_timestamp_deps.lastbuildstate'.
504&gt;C:\Program Files\Microsoft Visual Studio\18\Professional\MSBuild\Microsoft\VC\v180\Microsoft.CppBuild.targets(358,5): error MSB3501: Could not read lines from file "x64\Release\qSlicerVolumeRenderingSubjectHierarchyPluginsPythonQt_autogen_timestamp_deps\qSlicerV.95CA0B59.tlog\qSlicerVolumeRenderingSubjectHierarchyPluginsPythonQt_autogen_timestamp_deps.lastbuildstate". Could not find a part of the path 'C:\S5R\Slicer-build\Modules\Loadable\VolumeRendering\SubjectHierarchyPlugins\x64\Release\qSlicerVolumeRenderingSubjectHierarchyPluginsPythonQt_autogen_timestamp_deps\qSlicerV.95CA0B59.tlog\qSlicerVolumeRenderingSubjectHierarchyPluginsPythonQt_autogen_timestamp_deps.lastbuildstate'.
506&gt;C:\Program Files\Microsoft Visual Studio\18\Professional\MSBuild\Microsoft\VC\v180\Microsoft.CppBuild.targets(358,5): error MSB3501: Could not read lines from file "x64\Release\qSlicerDynamicModelerSubjectHierarchyPluginsPythonQt_autogen_timestamp_deps\qSlicerD.F37E2B52.tlog\qSlicerDynamicModelerSubjectHierarchyPluginsPythonQt_autogen_timestamp_deps.lastbuildstate". Could not find a part of the path 'C:\S5R\Slicer-build\E\SurfaceToolbox\DynamicModeler\SubjectHierarchyPlugins\x64\Release\qSlicerDynamicModelerSubjectHierarchyPluginsPythonQt_autogen_timestamp_deps\qSlicerD.F37E2B52.tlog\qSlicerDynamicModelerSubjectHierarchyPluginsPythonQt_autogen_timestamp_deps.lastbuildstate'.
```
These occurred because the reference path was greater than 260 characters long. I would otherwise have to manually enable `[longPathAware`](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry#enable-long-paths-in-windows-10-version-1607-and-later).

Slicer currently does a check of using a 40 character limit to pre-determine if there will be a max path length issue, however it isn't alerting about this current case.
https://github.com/Slicer/Slicer/blob/b48ed846855eccca1dc695dd2eed6e806c69be2f/CMakeLists.txt#L148-L153

Note that my build tree was a short "C:/S5R" per the recommendation in the Slicer documentation and it can't really get any shorter to accommodate the long file path issues during packaging on Windows.

@lassoan Have you run into this locally on Windows when doing the package step with the mentioned build tools?</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
