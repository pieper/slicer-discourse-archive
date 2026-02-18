# Addressing issue with "pip install itk"

**Topic ID**: 21763
**Date**: 2022-02-02
**URL**: https://discourse.slicer.org/t/addressing-issue-with-pip-install-itk/21763

---

## Post #1 by @ebrahim (2022-02-02 16:46 UTC)

<p>I was also playing with pip installing itk, but this <a href="https://github.com/KitwareMedical/lungair-desktop-application/issues/6#issuecomment-1025792437" rel="noopener nofollow ugc">doesn’t seem to work at the moment.</a></p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> was looking into this. It may have to do with the pip-installed ITK and the compiled ITK libraries working with the same shared memory, each under the assumption that it is their memory to manage. I don’t know, but when I backtrace the crash it seems to happen while ITK is trying to free some memory.</p>

---

## Post #2 by @jcfr (2022-02-02 19:25 UTC)

<p>Analyzing the backtrace seems to indicate that the pip installed ITK libraries are attempting to register the ITK IO factories already loaded in Slicer through the built-in ITK:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/2881ae0c670eff87b156fa607b3bbad30c248899.png" data-download-href="/uploads/short-url/5MkW4zhT7xkXn1Vd5PF1J5j0UCR.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/2881ae0c670eff87b156fa607b3bbad30c248899.png" alt="image" data-base62-sha1="5MkW4zhT7xkXn1Vd5PF1J5j0UCR" width="690" height="284" data-dominant-color="D1D1D1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1570×648 36.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After talking with <a class="mention" href="/u/thewtex">@thewtex</a> , we identified a path forward and will follow up.</p>
<p>In a nutshell, we are evaluating approaches like these:</p>
<ul>
<li>delegating the loading and registration of ITK IO to python<br>
or</li>
<li>configure the registration code in the C++ build so that the static variable uniquely identify a given build</li>
</ul>

---

## Post #3 by @thewtex (2022-02-03 16:54 UTC)

<p>Patch is here:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/InsightSoftwareConsortium/ITK/pull/3156">
  <header class="source">

      <a href="https://github.com/InsightSoftwareConsortium/ITK/pull/3156" target="_blank" rel="noopener nofollow ugc">github.com/InsightSoftwareConsortium/ITK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/InsightSoftwareConsortium/ITK/pull/3156" target="_blank" rel="noopener nofollow ugc">io factory registration python</a>
    </h4>

    <div class="branches">
      <code>InsightSoftwareConsortium:master</code> ← <code>thewtex:io-factory-registration-python</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-02-03" data-time="16:50:46" data-timezone="UTC">04:50PM - 03 Feb 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/thewtex" target="_blank" rel="noopener nofollow ugc">
          <img alt="thewtex" src="https://avatars.githubusercontent.com/u/25432?v=4" class="onebox-avatar-inline" width="20" height="20">
          thewtex
        </a>
      </div>

      <div class="lines" title="1 commits changed 26 files with 341 additions and 70 deletions">
        <a href="https://github.com/InsightSoftwareConsortium/ITK/pull/3156/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+341</span>
          <span class="removed">-70</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Load IO and FFT factories at runtime based on the itk-module.cmake
FACTORY_NAME<span class="show-more-container"><a href="https://github.com/InsightSoftwareConsortium/ITK/pull/3156" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">S metadata, as is done with C++ static binary
initialization.

This enables run-time discovery of all Python IO or FFT implementations.
Some may be added with remote module Python packages.

This also addresses Slicer's use case where Slice is performing
initialization of IO factories with static initialization. Only
one static binary initialization is intended to be supported per
application. Do not perform static binary initialization in the Python
modules.

FFTImageFilter consolidation was finalized, and the required
corresponding VnlFFTImageFilterFactory and FFTWFFTImageFilterFactory
classes created and wrapped.

Add the missing required TransformIO wrapping.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
