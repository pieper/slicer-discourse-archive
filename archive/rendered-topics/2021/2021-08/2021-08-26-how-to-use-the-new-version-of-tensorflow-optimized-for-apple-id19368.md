---
topic_id: 19368
title: "How To Use The New Version Of Tensorflow Optimized For Apple"
date: 2021-08-26
url: https://discourse.slicer.org/t/19368
---

# How to use the new version of TensorFlow optimized for Apple Silicon M1 on Slicer

**Topic ID**: 19368
**Date**: 2021-08-26
**URL**: https://discourse.slicer.org/t/how-to-use-the-new-version-of-tensorflow-optimized-for-apple-silicon-m1-on-slicer/19368

---

## Post #1 by @Robb (2021-08-26 15:20 UTC)

<p>Now I have a Macbook Pro with Apple M1, and Operating System is MacOS Big Sur. I found that if I want to use TensorFlow on this Macbook Pro, I need a new version of TensorFlow specifically optimized for the M1 chip, and the download link is <a href="https://github.com/apple/tensorflow_macos" class="inline-onebox" rel="noopener nofollow ugc">GitHub - apple/tensorflow_macos: TensorFlow for macOS 11.0+ accelerated using Apple's ML Compu</a><br>
However, the Mac-optimized TensorFlow requires Python 3.8 or higher version, and the latest version of Slicer’s Python version is only 3.6.7. Thus the problem of mismatch between them arises. I can’t import tensorflow in Slicer now.<br>
I wonder if there is a solution to this problem. Or has anyone successfully configured TensorFlow for Slicer on an M1 Macbook before?<br>
Looking forward to some guidance! Thank you very much!</p>

---

## Post #2 by @pieper (2021-08-26 15:30 UTC)

<p>That looks cool, but it’s all new.  You can try building Slicer with python 3.8 and maybe you can contribute fixes to the the items in the issue linked below.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5014">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5014" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5014" target="_blank" rel="noopener">Update Python version from 3.6.7 to 3.7 (or 3.8)</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-06-25" data-time="21:14:44" data-timezone="UTC">09:14PM - 25 Jun 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This was initially discussed in https://github.com/Slicer/Slicer/issues/4859

<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">The following PR would need to be finalized:

* python-cmake-buildsystem/python-cmake-buildsystem#264
* python-cmake-buildsystem/python-cmake-buildsystem#267</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
