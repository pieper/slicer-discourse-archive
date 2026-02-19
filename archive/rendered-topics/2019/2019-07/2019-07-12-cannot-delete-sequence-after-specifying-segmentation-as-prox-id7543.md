---
topic_id: 7543
title: "Cannot Delete Sequence After Specifying Segmentation As Prox"
date: 2019-07-12
url: https://discourse.slicer.org/t/7543
---

# Cannot delete sequence after specifying segmentation as proxy node

**Topic ID**: 7543
**Date**: 2019-07-12
**URL**: https://discourse.slicer.org/t/cannot-delete-sequence-after-specifying-segmentation-as-proxy-node/7543

---

## Post #1 by @ungi (2019-07-12 00:41 UTC)

<p>Hi,<br>
I cannot delete sequences, once I add a segmentation as proxy node to a sequence in the same browser. Could somebody please look into this issue?<br>
I tested this with version 2019-07-04 (BTW, there is no Sequences extension in today’s Extension Manager for Windows). Here is a screen video of the issue: <a href="https://1drv.ms/v/s!AhiABcbe1DBygu57EAFEs6T-O6sdDQ" rel="nofollow noopener">https://1drv.ms/v/s!AhiABcbe1DBygu57EAFEs6T-O6sdDQ</a><br>
Thanks,<br>
Tamas</p>

---

## Post #2 by @jcfr (2019-07-12 02:26 UTC)

<aside class="quote no-group" data-username="ungi" data-post="1" data-topic="7543">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ungi/48/78573_2.png" class="avatar"> ungi:</div>
<blockquote>
<p>there is no Sequences extension in today’s Extension Manager for Windows</p>
</blockquote>
</aside>
<p>This will be fixed by</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/SlicerRt/Sequences/pull/80">
  <header class="source">

      <a href="https://github.com/SlicerRt/Sequences/pull/80" target="_blank" rel="noopener">github.com/SlicerRt/Sequences</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/SlicerRt/Sequences/pull/80" target="_blank" rel="noopener">COMP: Fix windows link error adding dependency to VolumeRendering MRML library</a>
      </h4>

    <div class="branches">
      <code>SlicerRt:master</code> ← <code>jcfr:fix-windows-link-error</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2019-07-12" data-time="02:25:47" data-timezone="UTC">02:25AM - 12 Jul 19 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jcfr" target="_blank" rel="noopener">
            <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
            jcfr
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 1 additions and 0 deletions">
          <a href="https://github.com/SlicerRt/Sequences/pull/80/files" target="_blank" rel="noopener">
            <span class="added">+1</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This commit fixes a regression introduced in previous commit. It fixes
the foll<span class="show-more-container"><a href="https://github.com/SlicerRt/Sequences/pull/80" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">owing error:

```
  vtkMRMLNodeSequencer.obj : error LNK2019: unresolved external symbol "__declspec(dllimport) public: static class vtkMRMLVolumePropertyNode  [...]
```

Reported-by: Tamas Ungi &lt;ungi@queensu.ca&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @ungi (2019-07-12 21:34 UTC)

<p>Thanks, Sequences is there for Windows today.</p>
<p>FYI, the original issue may be fixed tomorrow by <a href="https://github.com/Slicer/Slicer/commit/fb0b277eca7af84cceb29aabb9fef521a29fb4c4" rel="nofollow noopener">https://github.com/Slicer/Slicer/commit/fb0b277eca7af84cceb29aabb9fef521a29fb4c4</a><br>
I will test again tomorrow.</p>

---

## Post #4 by @ungi (2019-07-13 19:03 UTC)

<p>This problem is still there in today’s version. I think the list widget does not update correctly when a sequence is deleted. But I’m not sure why the problem only occurs after a segmentation is specified as proxy node.</p>

---
