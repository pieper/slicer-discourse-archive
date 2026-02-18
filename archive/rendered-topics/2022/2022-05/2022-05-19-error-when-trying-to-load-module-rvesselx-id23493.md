# Error when trying to load module RVesselX

**Topic ID**: 23493
**Date**: 2022-05-19
**URL**: https://discourse.slicer.org/t/error-when-trying-to-load-module-rvesselx/23493

---

## Post #1 by @n0wm3 (2022-05-19 16:09 UTC)

<p>Hello, I’m trying to install an extension <a href="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation" rel="noopener nofollow ugc">SilcerRVXLiverSegmentation</a>, and when I couldn’t load the module.</p>
<p>Here is the error log:<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\karis\AppData\Local\NA-MIC\Slicer 5.1.0-2022-05-18\lib\Python\Lib\imp.py”, line 169, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 613, in _exec<br>
File “”, line 850, in exec_module<br>
File “”, line 228, in <em>call_with_frames_removed<br>
File “C:/Users/karis/AppData/Local/NA-MIC/Slicer 5.1.0-2022-05-18/NA-MIC/Extensions-30955/RVesselX/lib/Slicer-5.1/qt-scripted-modules/RVXLiverSegmentation.py”, line 8, in <br>
from RVXLiverSegmentationLib import RVXLiverSegmentationLogic, Settings, DataWidget, addInCollapsibleLayout, <br>
File "C:\Users\karis\AppData\Local\NA-MIC\Slicer 5.1.0-2022-05-18\NA-MIC\Extensions-30955\RVesselX\lib\Slicer-5.1\qt-scripted-modules\RVXLiverSegmentationLib_<em>init</em></em>.py", line 18, in <br>
from .VesselHelpWidget import VesselHelpWidget, VesselHelpType<br>
ModuleNotFoundError: No module named ‘RVXLiverSegmentationLib.VesselHelpWidget’</p>
<p>Does anyone know how to solve this problem? I have no knowledge in Python and am utterly confused.</p>

---

## Post #2 by @lassoan (2022-05-19 20:27 UTC)

<p>The problem was that the developers added a new file (<code>VesselHelpWidget.py</code>) but forgot to add to the Slicer extension package. I’ve submitted a pull request that fixes the issue:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation/pull/5">
  <header class="source">

      <a href="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation/pull/5" target="_blank" rel="noopener">github.com/R-Vessel-X/SlicerRVXLiverSegmentation</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation/pull/5" target="_blank" rel="noopener">Add missing file to the extension package</a>
    </h4>

    <div class="branches">
      <code>R-Vessel-X:main</code> ← <code>lassoan:patch-1</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-05-19" data-time="20:23:55" data-timezone="UTC">08:23PM - 19 May 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 1 additions and 0 deletions">
        <a href="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation/pull/5/files" target="_blank" rel="noopener">
          <span class="added">+1</span>
          <span class="removed">-0</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Fixes the error

from .VesselHelpWidget import VesselHelpWidget, VesselHelpTyp<span class="show-more-container"><a href="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation/pull/5" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">e
ModuleNotFoundError: No module named ‘RVXLiverSegmentationLib.VesselHelpWidget’</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>In the meantime, you can download the missing <a href="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation/blob/main/RVXLiverSegmentation/RVXLiverSegmentationLib/VesselHelpWidget.py"><code>VesselHelpWidget.py</code> file</a> and copy it to <code>C:/Users/karis/AppData/Local/NA-MIC/Slicer 5.1.0-2022-05-18/NA-MIC/Extensions-30955/RVesselX/lib/Slicer-5.1/qt-scripted-modules/RVXLiverSegmentationLib</code></p>

---

## Post #3 by @n0wm3 (2022-05-19 21:53 UTC)

<p>Thank you so much! This solved my problem.</p>

---

## Post #4 by @Thibault_Pelletier (2022-05-20 06:25 UTC)

<p>Thanks <a class="mention" href="/u/n0wm3">@n0wm3</a> for reporting this bug and thanks <a class="mention" href="/u/lassoan">@lassoan</a> for submitting the fix.<br>
I have merged the PR, so this issue should be fixed for the next extension release.</p>
<p>Don’t hesitate to reach out to us if you have any question or feedback regarding this extension!</p>

---
