---
topic_id: 48550
title: "PRISMrendering not loading"
date: 2026-10-19
url: https://discourse.slicer.org/t/48550
last_bumped: 2026-10-19T15:14:21.344Z
---

# PRISMrendering not loading

**Topic ID**: 48550
**Date**: 2026-10-19
**URL**: https://discourse.slicer.org/t/prismrendering-not-loading/48550

---

## Post #1 by @Atticus (2026-10-19 12:13 UTC)

<p>Hi!</p>
<p>As the title says, the PRISMrendering module appears in red boldface in the module finder and it only displays “PRISMRendering module is not loaded”</p>
<p>I installed it from the Extension Manager and restarted 3DSlicer as requested.</p>
<p>Running 3DSlicer 5.12.4 on Win11. I have never used this extension in the past.</p>
<p>Any info is much appreciated.</p>
<p>Thanks in Advance,</p>
<p>Atticus</p>

---

## Post #2 by @muratmaga (2026-10-19 15:14 UTC)

<p>I noticed that few days ago. It is due to.an outdated library. I left a pr that fixes it. If you apply it should work</p>
<p>Not sure how actively Simon is tracking the forum or the repo.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/ETS-vis-interactive/SlicerPRISMRendering/pull/44">
  <header class="source">

      <a href="https://github.com/ETS-vis-interactive/SlicerPRISMRendering/pull/44" target="_blank" rel="noopener nofollow ugc">github.com/ETS-vis-interactive/SlicerPRISMRendering</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/ETS-vis-interactive/SlicerPRISMRendering/pull/44" target="_blank" rel="noopener nofollow ugc">BUG: Fix module loading on Python 3.12 (remove unused imp/distutils imports) (#44)</a>
      </h4>

    <div class="branches">
      <code>master</code> ← <code>muratmaga:fix-python312-imports</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2026-10-15" data-time="23:26:11" data-timezone="UTC">11:26PM - 15 Oct 26 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/muratmaga" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://avatars.githubusercontent.com/u/21285140?v=4" class="onebox-avatar-inline" width="20" height="20">
            muratmaga
          </a>
        </div>

        <div class="lines" title="1 commits changed 3 files with 0 additions and 5 deletions">
          <a href="https://github.com/ETS-vis-interactive/SlicerPRISMRendering/pull/44/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+0</span>
            <span class="removed">-5</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">@drouin-simon — PRISMRendering currently fails to load in Slicer 5.12 (Python 3.<span class="show-more-container"><a href="https://github.com/ETS-vis-interactive/SlicerPRISMRendering/pull/44" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">12):

```
File ".../qt-scripted-modules/PRISMRendering.py", line 9, in &lt;module&gt;
    import imp
ModuleNotFoundError: No module named 'imp'
[Qt] Fail to instantiate module  "PRISMRendering"
```

Python 3.12 removed both `imp` and `distutils` from the standard library. In this extension both imports are dead code (`imp` is never referenced, and `strtobool` is imported but never called), so this PR just deletes them:

- `PRISMRendering/PRISMRendering.py`: remove `import imp` and `from distutils.util import strtobool`
- `PRISMRendering/PRISMRenderingLogic/PRISMRenderingLogic.py`: same
- `PRISMRendering/PRISMRenderingShaders/CustomShader.py`: remove `import imp`

`distutils` currently happens to resolve through setuptools' shim, but that's not guaranteed, so it's removed too. Line endings (CRLF) are preserved.

**Tested:** Slicer 5.12.4 (r34645, Python 3.12.10) on Linux — I applied the same change to the installed extension, and the module now loads, the widget/logic instantiate, and the Custom Shader list (Outline, Sphere Carving, Chroma Depth, Opacity Peeling, Plane Intersecting) populates.

🤖 Generated with [Claude Code](https://claude.com/claude-code)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
