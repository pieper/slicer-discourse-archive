# Import SimpleITK fails

**Topic ID**: 36735
**Date**: 2024-06-12
**URL**: https://discourse.slicer.org/t/import-simpleitk-fails/36735

---

## Post #1 by @smrolfe (2024-06-12 20:19 UTC)

<p>Import of SimpleITK is failing using the latest Preview version on a Windows OS. Mac OS seems to work fine. The error I’m getting is:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\Users\srolfe\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-10\lib\Python\Lib\site-packages\SimpleITK\__init__.py", line 18, in &lt;module&gt;
    from SimpleITK.SimpleITK import *
  File "C:\Users\srolfe\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-10\lib\Python\Lib\site-packages\SimpleITK\SimpleITK.py", line 13, in &lt;module&gt;
    from . import _SimpleITK
ImportError: DLL load failed while importing _SimpleITK: The specified module could not be found.
</code></pre>

---

## Post #2 by @lassoan (2024-06-13 01:38 UTC)

<p>Thanks for reporting. It seems that <a href="https://slicer.cdash.org/viewTest.php?buildid=3415654&amp;onlyfailed">SimpleITK tests in Slicer core has been failing</a> since <a href="https://github.com/Slicer/Slicer/commit/acf3dd47940665869765584564b38439f73ff1d5">ITK was updated last week</a> (2024-06-04).</p>
<p><a class="mention" href="/u/dzenanz">@dzenanz</a> <a class="mention" href="/u/jcfr">@jcfr</a> Could you please have a look?</p>

---

## Post #3 by @jamesobutler (2024-06-13 03:32 UTC)

<p>What is odd is that these results are different from my local build, package and testing that I reported in my <a href="https://github.com/Slicer/Slicer/pull/7771#pullrequestreview-2094047926" rel="noopener nofollow ugc">review comment</a>. With my installed package the import of SimpleITK is successful:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7234aa4831e2155fe28fe8be6e4f95d218ffdc4.png" data-download-href="/uploads/short-url/uHcgCa6CK1fWBWMslGFTPioL3fe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7234aa4831e2155fe28fe8be6e4f95d218ffdc4.png" alt="image" data-base62-sha1="uHcgCa6CK1fWBWMslGFTPioL3fe" width="690" height="185" data-dominant-color="DCDCDE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">695×187 4.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However I do see the reported import error when using the Slicer factory built versions. When viewing the <a href="https://slicer.cdash.org/builds/3424065/configure" rel="noopener nofollow ugc">configure command</a> of recent Slicer preview builds I see that it is using</p>
<ul>
<li>CMake 3.22.1 (released December 7th 2021)</li>
<li>Visual Studio 2022 &gt;=17.9.6, &lt;17.10</li>
</ul>
<p>My successful build was with:</p>
<ul>
<li>CMake 3.28.3 (released February 5th 2024)</li>
<li>Visual Studio 2022 17.9.5.</li>
</ul>
<p>I wouldn’t be surprised if the older CMake version may be having issues with this latest SimpleITK.</p>

---

## Post #4 by @blowekamp (2024-06-13 12:59 UTC)

<p>A recent change to the building of SimpleITK was to enable the Python Limited or Stable API:</p><aside class="onebox githubpullrequest" data-onebox-src="https://github.com/SimpleITK/SimpleITK/pull/2121/files">
  <header class="source">

      <a href="https://github.com/SimpleITK/SimpleITK/pull/2121/files" target="_blank" rel="noopener nofollow ugc">github.com/SimpleITK/SimpleITK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/SimpleITK/SimpleITK/pull/2121/files" target="_blank" rel="noopener nofollow ugc">Add SimpleITK_PYTHON_USE_USE_LIMITED_API option</a>
      </h4>

    <div class="branches">
      <code>SimpleITK:master</code> ← <code>blowekamp:add_python_stable_api</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-05-20" data-time="19:56:17" data-timezone="UTC">07:56PM - 20 May 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/blowekamp" target="_blank" rel="noopener nofollow ugc">
            <img alt="blowekamp" src="https://avatars.githubusercontent.com/u/321061?v=4" class="onebox-avatar-inline" width="20" height="20">
            blowekamp
          </a>
        </div>

        <div class="lines" title="5 commits changed 13 files with 96 additions and 13 deletions">
          <a href="https://github.com/SimpleITK/SimpleITK/pull/2121/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+96</span>
            <span class="removed">-13</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">More information on the Python Stable API:
https://docs.python.org/3/c-api/stab<span class="show-more-container"><a href="https://github.com/SimpleITK/SimpleITK/pull/2121" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">le.html

Requires Python 3.11+, SWIG 4.2+, and CMake 3.26+.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>There is some conditional logic on the version of CMake, SWIG and Python to enable this feature. It may be a good place to start looking at the configuration output of SimpleITK and it’s Python configuration.</p>

---

## Post #5 by @dzenanz (2024-06-13 13:11 UTC)

<p>I have already spent ~10 hours on this update. It would be good if someone else hunted this down. Maybe even someone more familiar with SimpleITK than me?</p>

---

## Post #6 by @blowekamp (2024-06-17 15:25 UTC)

<p><a class="mention" href="/u/dzenanz">@dzenanz</a>  Was the update to SimpleITK required?</p>
<p>I am just noticing that Slicer is using a forked version of SimpleITK. And looking into why… There is a lit for me to catch up on the help out. Let me know how I can help.</p>

---

## Post #7 by @dzenanz (2024-06-17 15:35 UTC)

<p>Slicer adds <a href="https://github.com/Slicer/ITK/commit/aacaefd6366bb09e09faefd173d4d3797f386ad0" rel="noopener nofollow ugc">this commit</a> which adds support for customizing ITK’s namespace. Correspondingly, <a href="https://github.com/Slicer/SimpleITK/commits/slicer-v2.3.1-2024-05-20-bc4449e/" rel="noopener nofollow ugc">a few commits</a> are added to SimpleITK. Updating ITK without also updating SimpleITK runs into errors (I did this a month ago so I don’t remember exactly what compiler complained about).</p>

---

## Post #8 by @jamesobutler (2024-06-17 15:40 UTC)

<p>Some links to refresh the memory regarding the Slicer SimpleITK fork and thoughts to reconsider using PyPI whl.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6606#issuecomment-1286278137">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6606#issuecomment-1286278137" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">

    <div class="github-icon-container" title="Comment">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 2.75a.25.25 0 01.25-.25h8.5a.25.25 0 01.25.25v5.5a.25.25 0 01-.25.25h-3.5a.75.75 0 00-.53.22L3.5 11.44V9.25a.75.75 0 00-.75-.75h-1a.25.25 0 01-.25-.25v-5.5zM1.75 1A1.75 1.75 0 000 2.75v5.5C0 9.216.784 10 1.75 10H2v1.543a1.457 1.457 0 002.487 1.03L7.061 10h3.189A1.75 1.75 0 0012 8.25v-5.5A1.75 1.75 0 0010.25 1h-8.5zM14.5 4.75a.25.25 0 00-.25-.25h-.5a.75.75 0 110-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0114.25 12H14v1.543a1.457 1.457 0 01-2.487 1.03L9.22 12.28a.75.75 0 111.06-1.06l2.22 2.22v-2.19a.75.75 0 01.75-.75h1a.25.25 0 00.25-.25v-5.5z"></path></svg>
    </div>



  <div class="github-info-container">

      <h4>
        Comment by
        <a href="https://github.com/jcfr" target="_blank" rel="noopener nofollow ugc">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?u=fdc648b09ebb3203e6cffa04dd160b0bd6e4f139&amp;v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a> - <a href="https://github.com/Slicer/Slicer/pull/6606#issuecomment-1286278137" target="_blank" rel="noopener nofollow ugc">BUG: Update SimpleITK to fix test_sitkUtils</a>
      </h4>



    <div class="branches">
      <code>Slicer:main</code> ← <code>jcfr:update-SimpleITK-to-fix-regression-introduced-by-custom-namespace-support</code>
    </div>

  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">&gt; going to be necessary in a Slicer SimpleITK fork moving forward or is there a <span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6606" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">diff that is flexible enough for integration into the SimpleITK upstream?

I started to discuss this with @blowekamp  in https://github.com/Slicer/SimpleITK/commit/ca0c09386219dfff61975437b7ea32b246adb724#r87443367

Also worth noting that building SimpleITK may not be required in the future, see https://discourse.slicer.org/t/proposal-install-simpleitk-from-wheels-instead-of-building-from-source/25635</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote" data-post="4" data-topic="25635">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/proposal-install-simpleitk-from-wheels-instead-of-building-from-source/25635/4">Proposal: Install SimpleITK from wheels instead of building from source</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Things have observed to break down when Slicer’s SimpleITK is uninstalled a SimpleITK upstream version is installed from whl. <a href="https://github.com/Slicer/Slicer/issues/6711" class="inline-onebox" rel="noopener nofollow ugc">Slicer's embedded SimpleITK can be removed by pip · Issue #6711 · Slicer/Slicer · GitHub</a> 
As of right now it seems that proceeding with using SimpleITK whl files is not possible within Slicer due to requiring the fixes made in <a href="https://github.com/Slicer/Slicer/pull/6606" class="inline-onebox" rel="noopener nofollow ugc">BUG: Update SimpleITK to fix test_sitkUtils by jcfr · Pull Request #6606 · Slicer/Slicer · GitHub</a> which are not in SimpleITK upstream.
  </blockquote>
</aside>


---
