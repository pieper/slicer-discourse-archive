---
topic_id: 16650
title: "How To Update Python Version From 3 67 To 3 8"
date: 2021-03-19
url: https://discourse.slicer.org/t/16650
---

# How to update Python version from 3.67 to 3.8

**Topic ID**: 16650
**Date**: 2021-03-19
**URL**: https://discourse.slicer.org/t/how-to-update-python-version-from-3-67-to-3-8/16650

---

## Post #1 by @full_stack_master (2021-03-19 18:25 UTC)

<p>I want to update My slicer’s Python version from 3.6.7 to 3.8 because I am going to use Torch package<br>
As you know, this package is working on Python 3.8<br>
Can you help me?</p>

---

## Post #2 by @pieper (2021-03-19 18:30 UTC)

<p>To answer your question it’s not easy to change python versions.  We update fairly frequently but it’s not always easy (perhaps these minor versions would be, I don’t know).</p>
<p>But if your goal is to use torch, I was able to pip_install torch with recent Slicer versions and it worked great.</p>

---

## Post #3 by @fbordignon (2021-10-29 14:45 UTC)

<p>Hey <a class="mention" href="/u/pieper">@pieper</a>, I am willing to give this a go (upgrade to 3.8). Do you remember the sort of problems I may face when doing so? There are a few libs that could benefit from the upgrade.<br>
Thanks!</p>

---

## Post #4 by @lassoan (2021-10-29 15:53 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> recommended at least Python-3.9 and maybe Python-3.10.</p>
<p>You can try updating <code>python-source</code> in Slicer’s External_python.cmake to 3.10 and report any errors you get and cannot fix by yourself to the <a href="https://github.com/python-cmake-buildsystem/python-cmake-buildsystem">python-cmake-buildsystem project</a>.</p>

---

## Post #5 by @jamesobutler (2021-10-29 15:55 UTC)

<p>Already started work on the python-cmake-buildsystem project is detailed in this Slicer issue. There is indeed changes needed on the python-cmake-buildsystem front to support the upgrade.</p><aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5014">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5014" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5014" target="_blank" rel="noopener nofollow ugc">Update Python version from 3.6.7 to 3.10</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-06-25" data-time="21:14:44" data-timezone="UTC">09:14PM - 25 Jun 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener nofollow ugc">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:enhancement
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          priority:high
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This was initially discussed in https://github.com/Slicer/Slicer/issues/4859

<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">The following PR would need to be finalized:

- [ ] python-cmake-buildsystem/python-cmake-buildsystem#264
- [ ] python-cmake-buildsystem/python-cmake-buildsystem#267
- [ ] When Slicer's Python is upgraded then post a comment to MONAILabel issue https://github.com/Project-MONAI/MONAILabel/pull/378 (so that they can remove Python-3.6 support from MONAILabel)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
