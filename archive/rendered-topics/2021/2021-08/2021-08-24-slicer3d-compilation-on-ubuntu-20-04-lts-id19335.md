---
topic_id: 19335
title: "Slicer3D Compilation On Ubuntu 20 04 Lts"
date: 2021-08-24
url: https://discourse.slicer.org/t/19335
---

# Slicer3d compilation on Ubuntu 20.04 lts

**Topic ID**: 19335
**Date**: 2021-08-24
**URL**: https://discourse.slicer.org/t/slicer3d-compilation-on-ubuntu-20-04-lts/19335

---

## Post #1 by @Chintha_Siva_Prasad (2021-08-24 10:28 UTC)

<p>I am trying to build slicer by compiling the source code. When I am building it through cmake command it’s saying that it requires atleast 5.15.1. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3ab2389947c71764df9232792c4c7a0280512d05.jpeg" data-download-href="/uploads/short-url/8nfwS7oHUTlZTi8ijS4ZGfrGYvj.jpeg?dl=1" title="IMG-20210824-WA0035" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ab2389947c71764df9232792c4c7a0280512d05_2_690x310.jpeg" alt="IMG-20210824-WA0035" data-base62-sha1="8nfwS7oHUTlZTi8ijS4ZGfrGYvj" width="690" height="310" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ab2389947c71764df9232792c4c7a0280512d05_2_690x310.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ab2389947c71764df9232792c4c7a0280512d05_2_1035x465.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3ab2389947c71764df9232792c4c7a0280512d05.jpeg 2x" data-dominant-color="705F67"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG-20210824-WA0035</span><span class="informations">1280×576 87.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
But when I am using qt-default , it’s not installing the required version. And when tried to install latest version(6.x) through qt-online installer,it’s installing in a custom directory and while building slicer it’s using the older version.How can I resolve this issue? Is there a way to specify qt directory when I am compiling slicer? Or there is a optimal way to resolve this issue?</p>

---

## Post #2 by @pieper (2021-08-24 11:47 UTC)

<p>You can work around this by setting Slicer_REQUIRED_QT_VERSION CMake variable to 5.12.8.  You can follow further discussion here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5804">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5804" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5804" target="_blank" rel="noopener">Build on Ubuntu fails due to strict Qt version check</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-08-18" data-time="05:31:15" data-timezone="UTC">05:31AM - 18 Aug 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          priority:medium
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When following linux build instructions on Ubuntu 20.04, the [prerequisites that<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> are installed by the provided command](https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#ubuntu-20-04-focal-fossa) are not sufficient to build Slicer: I got a CMake error message that minimum Qt-5.12.1 is required.

Either the build instructions have to be updated so that it gets the required Qt version, or the Qt version check has to be relaxed.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
