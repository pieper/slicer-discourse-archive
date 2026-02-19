---
topic_id: 41707
title: "Slicer Extension Manager Build Error Missing Photogrammetry"
date: 2025-02-14
url: https://discourse.slicer.org/t/41707
---

# Slicer Extension Manager build error: Missing Photogrammetry.json on CDash

**Topic ID**: 41707
**Date**: 2025-02-14
**URL**: https://discourse.slicer.org/t/slicer-extension-manager-build-error-missing-photogrammetry-json-on-cdash/41707

---

## Post #1 by @oothomas (2025-02-14 18:43 UTC)

<p>Hello everyone,</p>
<p>I’m having trouble with my <strong>SlicerPhotogrammetry</strong> extension on the <strong>Slicer Preview</strong> dashboard. This is not a personal/local build; it’s built on the official dashboard (CDash). Despite the build itself completing successfully, packaging fails with this error:</p>
<pre><code class="lang-auto">CMake Error at /work/Preview/Slicer-0/Extensions/CMake/SlicerFunctionExtractExtensionDescription.cmake:135 (message):
  error: EXTENSION_FILE CMake variable points to a nonexistent file or directory:
  /.../SlicerPhotogrammetry-build/./Photogrammetry.json

Call Stack (most recent call first):
  /work/Preview/Slicer-0/Extensions/CMake/SlicerExtensionPackageAndUploadTarget.cmake:206 (slicerFunctionExtractExtensionDescriptionFromJson)
</code></pre>
<p>Is Photogrammetry.json being references because of the module name or the extension index .json file having the wrong name?</p>
<p>The extension includes two scripted modules (Photogrammetry and ClusterPhotos) and a standard CMakeLists.txt that sets EXTENSION_NAME, EXTENSION_DESCRIPTION, etc. I do see a .s4ext file generated, but I don’t see a corresponding .json file in the build directory. For some reason, the build system references Photogrammetry.json yet never seems to generate it.</p>
<p>Has anyone encountered a similar issue or know how to ensure the .json file is properly created and recognized? Any guidance on what might be missing in my extension’s configuration to keep CDash from throwing this error would be greatly appreciated.</p>
<p>Thanks so much!</p>

---

## Post #2 by @jamesobutler (2025-02-15 14:29 UTC)

<p><a class="mention" href="/u/oothomas">@oothomas</a> Check the extensions manager tomorrow following the change I pushed at:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/ExtensionsIndex/commit/3bc301f73afc53eb280d3f317e3d7df0c970e6f5">
  <header class="source">

      <a href="https://github.com/Slicer/ExtensionsIndex/commit/3bc301f73afc53eb280d3f317e3d7df0c970e6f5" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/ExtensionsIndex</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/ExtensionsIndex/commit/3bc301f73afc53eb280d3f317e3d7df0c970e6f5" target="_blank" rel="noopener nofollow ugc">Fix mismatch of Photogrammetry extensions json and extension name</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2025-02-15" data-time="14:29:08" data-timezone="UTC">02:29PM - 15 Feb 25 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="changed 1 files with 1 additions and 2 deletions">
        <a href="https://github.com/Slicer/ExtensionsIndex/commit/3bc301f73afc53eb280d3f317e3d7df0c970e6f5" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+1</span>
          <span class="removed">-2</span>
        </a>
      </div>
    </div>
  </div>
</div>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @muratmaga (2025-02-16 19:07 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> thanks for the fixes. Looks like it is built for preview but is not listed for Stable? Any idea why that might be the case?</p>

---

## Post #4 by @jamesobutler (2025-02-16 19:37 UTC)

<p>The Photogrammetry was only submitted to the <code>main</code> branch of the extensions index making it available for Slicer Preview builds.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/Slicer/ExtensionsIndex/tree/main">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/ExtensionsIndex/tree/main" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/Slicer/ExtensionsIndex/tree/main" target="_blank" rel="noopener nofollow ugc">GitHub - Slicer/ExtensionsIndex: Slicer extensions index</a></h3>

  <p><a href="https://github.com/Slicer/ExtensionsIndex/tree/main" target="_blank" rel="noopener nofollow ugc">main</a></p>

  <p><span class="label1">Slicer extensions index. Contribute to Slicer/ExtensionsIndex development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>A PR has to be submitted to the <code>5.8</code> branch to make it available for the Slicer 5.8.x stable releases.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/Slicer/ExtensionsIndex/tree/5.8">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/ExtensionsIndex/tree/5.8" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/Slicer/ExtensionsIndex/tree/5.8" target="_blank" rel="noopener nofollow ugc">GitHub - Slicer/ExtensionsIndex at 5.8</a></h3>

  <p><a href="https://github.com/Slicer/ExtensionsIndex/tree/5.8" target="_blank" rel="noopener nofollow ugc">5.8</a></p>

  <p><span class="label1">Slicer extensions index. Contribute to Slicer/ExtensionsIndex development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @muratmaga (2025-02-16 20:03 UTC)

<p>Got it thanks for the pointer.</p>

---
