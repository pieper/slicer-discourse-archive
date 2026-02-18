# Alternative to recommended way to respond to volume loading

**Topic ID**: 40906
**Date**: 2024-12-30
**URL**: https://discourse.slicer.org/t/alternative-to-recommended-way-to-respond-to-volume-loading/40906

---

## Post #1 by @shai-ikko (2024-12-30 15:12 UTC)

<p>Hi all,</p>
<p>The script repository recommends, if you want to respond to a volume being loaded, to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-volume-rendering-automatically-when-a-volume-is-loaded" rel="noopener nofollow ugc">respond to the Node-Added event</a>, but then call the responding method using a timer:</p>
<pre data-code-wrap="python"><code class="lang-python">    # Call showVolumeRendering using a timer instead of calling it directly
    # to allow the volume loading to fully complete.
    qt.QTimer.singleShot(0, lambda: showVolumeRendering(node))
</code></pre>
<p>In my experience (Slicer 5.6.2), this doesn’t work well when the volume loading is not immediate (e.g. loading a 300M Minc2 file typically takes a few seconds on my machine) – the listener is called before loading finishes.</p>
<p>I found an alternative – listen, instead, for changes in the scene’s Selection Node:</p>
<p>(in a module widget’s <code>setup()</code>: )</p>
<pre data-code-wrap="python"><code class="lang-python">        selectionNode = slicer.app.applicationLogic().GetSelectionNode()
        self.addObserver(selectionNode, vtk.vtkCommand.ModifiedEvent, self.onSelectionModified)
</code></pre>
<p>The Selection Node is changed only when the volume loading ends, so the responding code can handle it without waiting further.</p>
<p>I’ve seen some posts and comments objecting to the idea of a single selected volume; but the functionality is still there, and using it is still <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-a-volume-in-slice-views" rel="noopener nofollow ugc">recommended in a similar context</a>.</p>
<p>Is there some non-obvious disadvantage to this method?</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2024-12-31 16:03 UTC)

<p>This makes sense because sometimes the volume loading shows a transient progress bar, and that could be what triggers the singleShot.  Using the selection node as a workaround is also reasonable, and it’s nice that it doesn’t rely on Qt.</p>
<p>Another option could be to check the <code>slicer.mrmlScene.IsImporting()</code> and not do the volume rendering option until it’s False (i.e. just reset the singleShot until the importing is over).  I haven’t tested this but it might work.</p>
<p>It would be great if you could a PR to the script repository with whatever you decide is the best solution.</p>

---

## Post #3 by @shai-ikko (2025-01-08 13:06 UTC)

<p>Thanks again for your advice and support.</p><aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8127">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8127" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8127" target="_blank" rel="noopener nofollow ugc">DOC: Describe responding to change in selected volume</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>shai-ikko:doc-respond-selection-change</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-01-08" data-time="13:03:08" data-timezone="UTC">01:03PM - 08 Jan 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/shai-ikko" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://avatars.githubusercontent.com/u/93923471?v=4" class="onebox-avatar-inline" width="20" height="20">
            shai-ikko
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 35 additions and 0 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8127/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+35</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This is useful also for responding to volume loading in some cases, so also add <span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8127" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">a reference to the new section from the existing "Show volume rendering automatically when a volume is loaded".

See https://discourse.slicer.org/t/alternative-to-recommended-way-to-respond-to-volume-loading/40906</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
