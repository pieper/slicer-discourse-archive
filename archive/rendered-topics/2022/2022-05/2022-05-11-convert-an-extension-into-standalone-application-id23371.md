# Convert an extension into standalone application

**Topic ID**: 23371
**Date**: 2022-05-11
**URL**: https://discourse.slicer.org/t/convert-an-extension-into-standalone-application/23371

---

## Post #1 by @Mrwa_Awoda (2022-05-11 10:26 UTC)

<p>Operating system: windows 10<br>
Slicer version: 4.13<br>
Actual behavior:</p>
<p>Is it possible to convert an extension into standalone application and works with no need to install the 3D Slicer in my computer?</p>
<p>I tried to build the extension and then I get this error <code>Slicer_DIR-NOTFOUND</code>. I followed the instructions by replacing <code>Slicer_DIR-NOTFOUND</code> by  <code>c:/D/S4D/Slicer-build</code>, but still didn’t work.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b06a7b23f3da5a57ce875c590455b874e5e48a5.jpeg" data-download-href="/uploads/short-url/8qaqBHUjnXpO5IaeDMuElh2jAqx.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3b06a7b23f3da5a57ce875c590455b874e5e48a5_2_690x449.jpeg" alt="image" data-base62-sha1="8qaqBHUjnXpO5IaeDMuElh2jAqx" width="690" height="449" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3b06a7b23f3da5a57ce875c590455b874e5e48a5_2_690x449.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b06a7b23f3da5a57ce875c590455b874e5e48a5.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b06a7b23f3da5a57ce875c590455b874e5e48a5.jpeg 2x" data-dominant-color="F0ECEC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">886×577 77.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Does that mean the extension is connected to the 3D Slicer either way?</p>

---

## Post #2 by @jamesobutler (2022-05-11 11:15 UTC)

<p>Regarding the instructions on how to build an extension (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html" class="inline-onebox" rel="noopener nofollow ugc">Extensions — 3D Slicer documentation</a>) setting <code>Slicer_DIR</code> to the path <code>c:/D/S4D/Slicer-build</code> is an example path. Based on reading your other posts it appears you have built Slicer in a <code>c:D/S4R</code> directory so your <code>Slicer_DIR</code> is at <code>c:/D/S4R/Slicer-build</code>.</p>

---

## Post #3 by @Mrwa_Awoda (2022-05-11 19:16 UTC)

<blockquote>
<p>Based on reading your other posts it appears you have built Slicer in a <code>c:D/S4R</code> directory so your <code>Slicer_DIR</code> is at <code>c:/D/S4R/Slicer-build</code> .</p>
</blockquote>
<p>Right… CMake problem solved, but I get the same build error with VS, although it was previously resolved by</p>
<blockquote>
<p>rename the <code>C:/Users/toshiba/AppData/Local/Programs/Python</code> to something else (e.g., <code>C:/Users/toshiba/AppData/Local/Programs/PythonTemp</code> )</p>
</blockquote>
<p>*Python folder’s name still PythonTemp…<br>
here:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0ce9ece9bd711e6f41ad593b8d95a4e3ea9651dc.jpeg" data-download-href="/uploads/short-url/1QeUA0mljsBI08zUorgimGeSOzG.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ce9ece9bd711e6f41ad593b8d95a4e3ea9651dc_2_690x235.jpeg" alt="image" data-base62-sha1="1QeUA0mljsBI08zUorgimGeSOzG" width="690" height="235" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ce9ece9bd711e6f41ad593b8d95a4e3ea9651dc_2_690x235.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ce9ece9bd711e6f41ad593b8d95a4e3ea9651dc_2_1035x352.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0ce9ece9bd711e6f41ad593b8d95a4e3ea9651dc.jpeg 2x" data-dominant-color="313031"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1080×369 59.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is the output of the build:</p>
<blockquote>
<p><a href="https://docs.google.com/document/d/1EgmAdmFUo3p8Uc5CSP609zhDYsKE-C9a/edit?usp=sharing&amp;ouid=109318822956054168149&amp;rtpof=true&amp;sd=true" class="inline-onebox" rel="noopener nofollow ugc">SlicerRT-Build Output.docx - Google Docs</a></p>
</blockquote>

---

## Post #4 by @lassoan (2022-05-12 02:03 UTC)

<p>The <code> CMake variable EXTENSION_WC_REVISION is empty !</code> error is due to building an extension that is not under revision control. You can choose to either build the extension from a git version-controlled folder or specify the extension revision manually as described <a href="https://discourse.slicer.org/t/3d-slicer-release-build-error-variable-slicer-wc-last-changed-date-is-expected-to-be-defined-in-slicerpackageanduploadtarget/20984/23">here</a>.</p>
<p>While obviously developers must always use revision control, Slicer project should probably not enforce this as a mandatory rule. Therefore, I’ve submitted a pull request that changes the build error to just a warning:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6365">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6365" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/6365" target="_blank" rel="noopener">COMP: Do not require building extension from git repository</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>lassoan:allow-non-git-extension-repo</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-05-12" data-time="01:56:01" data-timezone="UTC">01:56AM - 12 May 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="1 commits changed 2 files with 7 additions and 11 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/6365/files" target="_blank" rel="noopener">
          <span class="added">+7</span>
          <span class="removed">-11</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Developers often complained that their extension build failed for some unknown r<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6365" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">eason and frequently the issue was that they did not store the source code in a git repository.

It is good to encourage developers to use best practices, such as version control, but making the build fail if they build from a non-version-controlled repository was unnecessarily strong measure.

This commit changes the behavior so that if an extension is built from a non-git folder then the build succeeds, just a warning is displayed during project configuration step and `NA` is used as the extension's WC revision.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
