# Error using MultiVolumeImporter for a nifti multivolume

**Topic ID**: 12644
**Date**: 2020-07-20
**URL**: https://discourse.slicer.org/t/error-using-multivolumeimporter-for-a-nifti-multivolume/12644

---

## Post #1 by @agomez (2020-07-20 15:59 UTC)

<p>Hi, we have found this and want to check if it may be a bug.</p>
<p>In MultiVolumeImporter there is a Helper function in<br>
…/Slicer-4.10.2-linux-amd64/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterLib/Helper.py</p>
<pre><code class="lang-python">-----------------------------------------------------------------------------------
from __main__ import vtk, slicer

class Helper( object ):

  @staticmethod
  def SetBgFgVolumes(bg, fg):
    appLogic = slicer.app.applicationLogic()
    selectionNode = appLogic.GetSelectionNode()
    selectionNode.SetReferenceActiveVolumeID(bg)
    selectionNode.SetReferenceSecondaryVolumeID(fg)
    appLogic.PropagateVolumeSelection()
------------------------------------------------------------------------------------------
</code></pre>
<p>This Helper function is called from MultiVolumeImporter.py in two places with this line:</p>
<p>Helper.SetBgFgVolumes(mvNode.GetID(),None)</p>
<p>This causes an error in the line of the Helper:</p>
<pre><code>selectionNode.SetReferenceSecondaryVolumeID(fg)

TypeError: SetReferenceSecondaryVolumeID argument 1: expected a sequence of 0 values, got NoneType
</code></pre>
<p>This error was found when loading a nifti multivolume.<br>
We could temporarily fix the error by editing MultiVolumeImporter.py or the Helper and changing None by [] or ‘’ but there must be a better solution.  If this is not a bug, please let us know the correct use of the module.</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2020-07-20 16:19 UTC)

<p>You can replace <code>fg</code> by <code>fg if fg else ''</code>. If it fixes the issue the. Please send a pull request with this change. Thank you!</p>

---

## Post #3 by @agomez (2020-07-20 18:56 UTC)

<p>Thanks Andras.<br>
This has been taken into account in MultiViewImporter some time ago but after the build of the stable release.<br>
</p><aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/fedorov/MultiVolumeImporter/commit/b7e43f29d27c0169a9f7909499b7d2c85a4c5201" target="_blank" rel="nofollow noopener">github.com/fedorov/MultiVolumeImporter</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/fedorov/MultiVolumeImporter/commit/b7e43f29d27c0169a9f7909499b7d2c85a4c5201" target="_blank" rel="nofollow noopener">BUG: account for None</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2019-07-02" data-time="20:50:24" data-timezone="UTC">08:50PM - 02 Jul 19 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/fedorov" target="_blank" rel="nofollow noopener">
          <img alt="fedorov" src="https://avatars1.githubusercontent.com/u/313942?v=4" class="onebox-avatar-inline" width="20" height="20">
          fedorov
        </a>
        
      </div>

      <div class="lines" title="changed 1 files with 5 additions and 3 deletions">
        <a href="https://github.com/fedorov/MultiVolumeImporter/commit/b7e43f29d27c0169a9f7909499b7d2c85a4c5201" target="_blank" rel="nofollow noopener">
          <span class="added">+5</span>
          <span class="removed">-3</span>
        </a>
      </div>
    </div>

  </div>
</div>




  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @agomez (2020-07-20 22:24 UTC)

<p>Thanks Andras.<br>
The issue was taken into account in MultiVolumeImporter some time ago but after the build of the last stable release.<br>
</p><aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/fedorov/MultiVolumeImporter/commit/b7e43f29d27c0169a9f7909499b7d2c85a4c5201" target="_blank" rel="nofollow noopener">github.com/fedorov/MultiVolumeImporter</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/fedorov/MultiVolumeImporter/commit/b7e43f29d27c0169a9f7909499b7d2c85a4c5201" target="_blank" rel="nofollow noopener">BUG: account for None</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2019-07-02" data-time="20:50:24" data-timezone="UTC">08:50PM - 02 Jul 19 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/fedorov" target="_blank" rel="nofollow noopener">
          <img alt="fedorov" src="https://avatars1.githubusercontent.com/u/313942?v=4" class="onebox-avatar-inline" width="20" height="20">
          fedorov
        </a>
        
      </div>

      <div class="lines" title="changed 1 files with 5 additions and 3 deletions">
        <a href="https://github.com/fedorov/MultiVolumeImporter/commit/b7e43f29d27c0169a9f7909499b7d2c85a4c5201" target="_blank" rel="nofollow noopener">
          <span class="added">+5</span>
          <span class="removed">-3</span>
        </a>
      </div>
    </div>

  </div>
</div>




  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @lassoan (2020-07-22 14:10 UTC)

<p>Thanks for checking. I would recommend to use a recent Slicer Preview Release then.</p>

---
