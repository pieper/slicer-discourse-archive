---
topic_id: 40241
title: "Cdash Build Error Json Not Found"
date: 2024-11-18
url: https://discourse.slicer.org/t/40241
---

# CDash build error: JSON not found

**Topic ID**: 40241
**Date**: 2024-11-18
**URL**: https://discourse.slicer.org/t/cdash-build-error-json-not-found/40241

---

## Post #1 by @acsenrafilho (2024-11-18 12:43 UTC)

<p>Hi Slicers,</p>
<p>I have uploaded some projects to the Slicer Extension Index. Some of them presented the following build error:</p>
<pre data-code-wrap="bash"><code class="lang-bash">error: EXTENSION_FILE CMake variable points to a inexistent file or
  directory: /.../SlicerDTIALPS-build/./Slicer-DTI-ALPS.json
Call Stack (most recent call first):
  /work/Preview/Slicer-0/Extensions/CMake/SlicerExtensionPackageAndUploadTarget.cmake:206 (slicerFunctionExtractExtensionDescriptionFromJson)
</code></pre>
<p>This example was for the extension: <code>Slicer-DTI-ALPS</code><br>
Link for the <code>.json</code> file in the SlicerExtensionIndex: <a href="https://github.com/Slicer/ExtensionsIndex/blob/main/SlicerDTIALPS.json" class="inline-onebox" rel="noopener nofollow ugc">ExtensionsIndex/SlicerDTIALPS.json at main · Slicer/ExtensionsIndex · GitHub</a></p>
<p>However, a problem occurred to me before uploading this <code>.json</code> file. In fact, the building process (I followed the steps in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#linux-and-macos" rel="noopener nofollow ugc">Slicer documentation</a>) did not create a <code>.json</code> file but the old <code>.s4ext</code> text file.</p>
<p>I manually created the <code>.json</code> file to upload to the Slicer Extension Index.</p>
<p>How can I update the build folder to automatically generate the <code>.json</code> file? I believe that is the problem to CDash build error…</p>
<p>Note: A strange thing happens to another Slicer Extension (<a href="https://slicer.cdash.org/viewBuildError.php?buildid=3593901" rel="noopener nofollow ugc">Brain Volume Refinement</a>) that does all the building process normally, but it has the same building instructions (as far as I know). Hence, the <code>.json</code> file was not the problem here… <img src="https://emoji.discourse-cdn.com/twitter/thinking.png?v=12" title=":thinking:" class="emoji" alt=":thinking:" loading="lazy" width="20" height="20"></p>
<p>Thank you in advance for the assistance!</p>

---

## Post #2 by @acsenrafilho (2024-11-19 20:14 UTC)

<p>As an additional test, I made a brand new Slicer Extension (using the Extension Wizard module) to verify whether the Slicer 5.x version had updated the Extension creation from the previous Slicer 4.x extension pattern (which is the most cases for my previous Slicer extensions codes).</p>
<p>However, after the build had been done (as given at <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#linux-and-macos" class="inline-onebox" rel="noopener nofollow ugc">Extensions — 3D Slicer documentation</a>), the exported file is still a <code>.s4ext</code> text file, and I did not found a <code>.json</code> instead.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> can someone give some help here, please?</p>

---

## Post #3 by @lassoan (2024-11-19 22:09 UTC)

<p>Good point, we missed this. Would you give it a try and update the exrension description generation in Slicer to create a json file instead?</p>

---

## Post #4 by @acsenrafilho (2024-11-21 18:35 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I was trying to understand the Extension Description file writing process through the Slicer code, but I confess that it was a bit confusing to me…</p>
<p>I have compared the git tag <code>5.6</code> (which is the stable version at the moment) to the <code>main</code> code, however the <code>ExtensionDescription.py</code> script is already updated to <code>json</code> in the most recent commit.<br>
<a href="https://github.com/Slicer/Slicer/blob/f10cd8c229b50e4d96e55743385f17482214433a/Utilities/Scripts/SlicerWizard/ExtensionDescription.py#L256" rel="noopener nofollow ugc">See the line of code</a> (comparing the tag <code>5.6</code> and <code>main</code>)</p>
<p>What is a possible adjustment in this case? In my understanding, the Slicer stable version (<code>5.6</code> and below) has the old <code>.s4ext</code> format as default. Then, after <a href="https://github.com/Slicer/Slicer/commit/437e33804ded22e813a76f81d79f56cbbdcd184b" rel="noopener nofollow ugc">commit</a> <code>437e338</code> the new <code>json</code> file structure is introduced, which is the case for the <code>slicer preview</code> building process.</p>
<p>How can I give a different building procedure on each <code>slicer preview</code> and <code>slicer stable</code> stages?</p>
<p>I am sorry for the long explanation, but I am puzzled about how to help here…</p>

---

## Post #5 by @acsenrafilho (2024-11-22 12:05 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> , I think that I narrowed the point to adjustment…</p>
<p>After I rebuilt the Slicer version to <code>nightly</code>, using the <code>main</code> branch, I noticed that the <code>Slicer/Utilities/Scripts/SlicerWizard/ExtensionDescription.py</code> file is already updated to <code>json</code> description file formatting.<br>
However, the extension building process continues to generate the old <code>.s4ext</code> file instead. I used the common cmake building command as described in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#build-an-extension" rel="noopener nofollow ugc">Slicer documentation</a>.</p>
<p>Then I started to check it out the CMake files to find where it has the mention to <code>s4ext</code> and located the <code>SlicerExtensionCPack.cmake</code>, <a href="https://github.com/Slicer/Slicer/blob/45366c6d4d6a769c87a4fc8552c50f8c5c3c428d/CMake/SlicerExtensionCPack.cmake#L79" rel="noopener nofollow ugc">line 79</a></p>
<p>I think that this maintains the same <code>s4ext</code> extension description, even with the <code>json</code> being delegated to the <code>ExtensionDescription.py</code>.</p>
<p>Unfortunately, my knowledge of CMake does not allow me to fix this, but I hope I assisted you in checking where it could be fixed in the Slicer code.</p>
<p>Is this correct? Can I help is something else?</p>

---

## Post #6 by @Thibault_Pelletier (2025-08-08 05:55 UTC)

<p>Hi everyone,</p>
<p>I know this post is old, but as I was confronted with the same problem and tumbled here, I thought I would post the solution.</p>
<p>The problem comes from a mismatch between the CMake project name and the .json file present on the Slicer Extension Index.</p>
<p>For the packageupload target to work, both names need to be strictly the same.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> or <a class="mention" href="/u/jcfr">@jcfr</a> is this information already available in a doc somewhere or should I add an entry to document this behavior for further reference?</p>
<p>Best,</p>
<p>Thibault</p>

---

## Post #7 by @lassoan (2025-08-09 21:40 UTC)

<p>It was documented in the extension checklist. It was only enforced by manual review, but now I added an automatic check:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/ExtensionsIndex/pull/2194">
  <header class="source">

      <a href="https://github.com/Slicer/ExtensionsIndex/pull/2194" target="_blank" rel="noopener">github.com/Slicer/ExtensionsIndex</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/ExtensionsIndex/pull/2194" target="_blank" rel="noopener">ENH: Add more automatic tests</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>lassoan:add-more-automatic-tests</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-08-09" data-time="18:49:19" data-timezone="UTC">06:49PM - 09 Aug 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 7 files with 750 additions and 135 deletions">
          <a href="https://github.com/Slicer/ExtensionsIndex/pull/2194/files" target="_blank" rel="noopener">
            <span class="added">+750</span>
            <span class="removed">-135</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Move filename checks from bash script executed by CircleCI to Python script exec<span class="show-more-container"><a href="https://github.com/Slicer/ExtensionsIndex/pull/2194" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">uted by GitHub actions for consistency and to be able to run on Windows. Moved the unstable pre-commit json file schema check to the other extension validation checks.

Added tests:
- check that the extension description file name matches the project name in the `CMakeLists.txt` file
- check that the extension can be git cloned
- check that a license file can be found in the extension's repository
- check that extension category is in the allowed list
- check that the extension icon and screenshot URLs are valid image files

Show repository URL, `CMakeLists.txt`, license file in a report in the pull request. This makes quick review of extension submissions a bit easier.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
