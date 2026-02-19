---
topic_id: 42809
title: "Python Console Messages"
date: 2025-05-06
url: https://discourse.slicer.org/t/42809
---

# Python console messages

**Topic ID**: 42809
**Date**: 2025-05-06
**URL**: https://discourse.slicer.org/t/python-console-messages/42809

---

## Post #1 by @SANTIAGO_PENDON_MING (2025-05-06 09:14 UTC)

<p>Why Slicer can not instantaine for example vtkvmtk, curveMarker other many issues. The messages are the following ones:</p>
<p>Failed to load vtkSlicerCrossSectionAnalysisModuleLogicPython: No module named vtkSlicerShapeModuleMRMLPython<br>
Failed to load vtkSlicerStenosisMeasurement3DModuleLogicPython: No module named vtkSlicerShapeModuleMRMLPython<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\santiago.pendon\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\imp.py”, line 169, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 613, in _exec<br>
File “”, line 850, in exec_module<br>
File “”, line 228, in _call_with_frames_removed<br>
File “C:/Users/santiago.pendon/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/CurveMaker/lib/Slicer-5.6/qt-scripted-modules/CurveMaker.py”, line 6, in <br>
from Endoscopy import EndoscopyComputePath<br>
ImportError: cannot import name ‘EndoscopyComputePath’ from ‘Endoscopy’ (C:\Users\santiago.pendon\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\Endoscopy.py)<br>
[Qt] loadSourceAsModule - Failed to load file “C:/Users/santiago.pendon/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/CurveMaker/lib/Slicer-5.6/qt-scripted-modules/CurveMaker.py”  as module “CurveMaker” !<br>
[Qt] Fail to instantiate module  “CurveMaker”<br>
[Qt] libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space<br>
[Qt] libpng warning: iCCP: known incorrect sRGB profile<br>
[Qt] libpng warning: iCCP: known incorrect sRGB profile<br>
[Qt] libpng warning: iCCP: known incorrect sRGB profile<br>
[Qt]   Error(s):<br>
[Qt]     CLI executable: C:/Users/santiago.pendon/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerVMTK/lib/Slicer-5.6/qt-loadable-modules/vtkvmtk.py<br>
[Qt]     The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.<br>
[Qt] Fail to instantiate module  “vtkvmtk”<br>
[Qt] The following modules failed to be instantiated:<br>
[Qt]    vtkvmtk<br>
[Qt]    CurveMaker<br>
[Qt] libpng warning: iCCP: known incorrect sRGB profile<br>
[Qt] libpng warning: iCCP: known incorrect sRGB profile<br>
[Qt] libpng warning: iCCP: known incorrect sRGB profile<br>
[Qt] libpng warning: iCCP: known incorrect sRGB profile<br>
[Qt] libpng warning: iCCP: known incorrect sRGB profile</p>
<p>There is a way to avoid the appearance of this info/solve the issues?</p>

---

## Post #2 by @jamesobutler (2025-05-06 10:25 UTC)

<p>Regarding CurveMaker:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/CurveMaker/issues/16">
  <header class="source">

      <a href="https://github.com/Slicer/CurveMaker/issues/16" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/CurveMaker</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/CurveMaker/issues/16" target="_blank" rel="noopener nofollow ugc">Retire CurveMaker extension for Slicer-5.7 and later?</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-01-03" data-time="21:38:24" data-timezone="UTC">09:38PM - 03 Jan 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Since introduction of curves in Markups module and MarkupsToModel extension, the<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> CurveMaker extension became redundant.

Recent rework of the Endoscopy module in Slicer core, the extension has been reported to not work anymore - see https://github.com/Slicer/Slicer/issues/7519

Instead of fixing the extension, I would recommend stopping development and support of the extension for Slicer-5.7 and later.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Regarding vtkvmtk message:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK/issues/22">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/22" target="_blank" rel="noopener nofollow ugc">github.com/vmtk/SlicerExtension-VMTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/22" target="_blank" rel="noopener nofollow ugc">Fail to instantiate module “vtkvmtk” error reported at startup</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-09-25" data-time="15:37:26" data-timezone="UTC">03:37PM - 25 Sep 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This error is reported at Slicer startup if SlicerVMTK extension is installed:
<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">
```
CLI executable: C:/Users/E/AppData/Roaming/NA-MIC/Extensions-29387/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules/vtkvmtk.py
The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.
Fail to instantiate module “vtkvmtk”
The following modules failed to be instantiated:
vtkvmtk
```</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @chir.set (2025-05-06 10:29 UTC)

<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="1" data-topic="42809">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>Failed to load vtkSlicerCrossSectionAnalysisModuleLogicPython: No module named vtkSlicerShapeModuleMRMLPython<br>
Failed to load vtkSlicerStenosisMeasurement3DModuleLogicPython: No module named vtkSlicerShapeModuleMRMLPython</p>
</blockquote>
</aside>
<p>In what version of Slicer are you seeing that? I just checked in a self-built Slicer and they are not apparent. I remember that it was <a href="https://github.com/Slicer/Slicer/commit/9c875033632aea198791c0960310c165cad487c4" rel="noopener nofollow ugc">resolved</a> of old.</p>

---

## Post #4 by @SANTIAGO_PENDON_MING (2025-05-06 10:52 UTC)

<p>My version is 5.6.2 at this moment</p>

---
