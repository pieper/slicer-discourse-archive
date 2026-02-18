# Create a new window with multiple slice views

**Topic ID**: 28132
**Date**: 2023-03-02
**URL**: https://discourse.slicer.org/t/create-a-new-window-with-multiple-slice-views/28132

---

## Post #1 by @rhodesdante (2023-03-02 00:12 UTC)

<p>Is it possible to create a new window with multiple slice views? <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-a-slice-view-outside-the-view-layout" rel="noopener nofollow ugc">This example</a> shows how to create a single additional view, but I am attempting to create multiple additional views so I can display them on a separate monitor. I am assuming this requires some sort of creation of layoutNodes and the like, as is done in the <a href="https://github.com/Slicer/Slicer/blob/fca9db1aa635e5bcf2d61b62ac6beccce844cf86/Base/QTApp/qSlicerMainWindow.cxx" rel="noopener nofollow ugc">qSlicerMainWindow</a>. Is this correct, or is there a simpler way to acheive this functionality?<br>
Thanks!</p>

---

## Post #2 by @jamesobutler (2023-03-02 00:28 UTC)

<p>You’ll actually be interested in the concept of multiple viewports for a given layout which is specifically for the use case of multiple monitors. This is available using latest Slicer 5.3 Preview builds.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/advanced_topics.html#example-layout-containing-two-viewports" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/advanced_topics.html#example-layout-containing-two-viewports</a></p>
<p>The associated PR that added this functionality:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6776">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6776" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/6776" target="_blank" rel="noopener nofollow ugc">Multi monitor layout</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:multi-monitor-layout</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-01-10" data-time="22:43:12" data-timezone="UTC">10:43PM - 10 Jan 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="2 commits changed 23 files with 563 additions and 110 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/6776/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+563</span>
            <span class="removed">-110</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Layouts can now contain multiple viewports. The default viewport is displayed as<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6776" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden"> the center widget of the application main window, additional Additional viewports can be independent top-level windows or docking windows.

Views can be maximized/restored separately in each viewport.

Currently, a single new dual-viewport layout is added: Dual Monitor Four-Up View

![image](https://user-images.githubusercontent.com/307929/211677816-0a77cd67-f564-46b3-87d0-944f19da22c8.png)

Associated CTK pull request (already merged): https://github.com/commontk/CTK/pull/1061 first.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @rhodesdante (2023-03-03 17:54 UTC)

<p>Thanks so much <a class="mention" href="/u/jamesobutler">@jamesobutler</a>! This solution worked very well for me. Using the developer guide example you showed and the snippet below (modified from the compare volumes module), I was able to customize the layout of the second monitor view to fit my needs.</p>
<pre><code>#customLayout is the user's custom XML string specifying the layout, as in the example above
# Built-in layout IDs are all below 100, so you can choose any large random number for your custom layout ID.
customLayoutId = 501
layoutManager = slicer.app.layoutManager()
layoutManager.layoutLogic().GetLayoutNode().AddLayoutDescription(customLayoutId, customLayout)
# Switch to the new custom layout
layoutManager.setLayout(customLayoutId)
</code></pre>

---
