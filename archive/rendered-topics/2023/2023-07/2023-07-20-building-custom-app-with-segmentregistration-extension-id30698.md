# Building custom app with SegmentRegistration extension

**Topic ID**: 30698
**Date**: 2023-07-20
**URL**: https://discourse.slicer.org/t/building-custom-app-with-segmentregistration-extension/30698

---

## Post #1 by @darabi (2023-07-20 07:56 UTC)

<p>Hello,<br>
I have successfully created and built a skeleton custom app and would now like to add the extensions which I need for the application. For this, I have added the necessary <code>FetchContent_Populate</code> sections to <code>CMakeLists.txt</code> (cf. <a href="https://pastebin.com/70yFsart" class="inline-onebox" rel="noopener nofollow ugc">Extension configuration - Pastebin.com</a>).</p>
<p>SegmentRegistration has a dependency on SlicerProstate, which contains the DistanceMapBasedRegistration module, but SlicerProstate is not found by cmake:</p>
<pre><code class="lang-auto">-- Checking EXTENSION_NAME variable
-- Checking EXTENSION_NAME variable - SegmentRegistration
CMake Error at .../build/SegmentRegistration/CMakeLists.txt:27 (find_package):
  By not providing "FindSlicerProstate.cmake" in CMAKE_MODULE_PATH this
  project has asked CMake to find a package configuration file provided by
  "SlicerProstate", but CMake did not find one.

  Could not find a package configuration file provided by "SlicerProstate"
  with any of the following names:

    SlicerProstateConfig.cmake
    slicerprostate-config.cmake

  Add the installation prefix of "SlicerProstate" to CMAKE_PREFIX_PATH or set
  "SlicerProstate_DIR" to a directory containing one of the above files.  If
  "SlicerProstate" provides a separate development package or SDK, be sure it
  has been installed.


-- Configuring incomplete, errors occurred!
</code></pre>
<p>Any hint on what I should change is highly appreciated.</p>
<p>Thank you</p>
<p>Kambiz</p>

---

## Post #2 by @lassoan (2023-07-22 02:17 UTC)

<p>When an extension depends on extension then usually the one with dependencies calls <code>find_package(...)</code> for each dependent extensions. However, when extensions are bundled then they are incorporated directly into the Slicer project and don’t appear as separate projects, therefore <code>find_package(...)</code> would fail.</p>
<p>The solution is to only use <code>find_package(...)</code> for the extension name if the extension is not bundled. This can be determined by checking if <code>Slicer_EXTENSION_SOURCE_DIRS</code> is empty. See for example how it is done in SlicerIGT extension:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerIGT/SlicerIGT/blob/245fa92ec7e4533253d1f25f076f9d9026b8692a/CMakeLists.txt#L24-L29">
  <header class="source">

      <a href="https://github.com/SlicerIGT/SlicerIGT/blob/245fa92ec7e4533253d1f25f076f9d9026b8692a/CMakeLists.txt#L24-L29" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/SlicerIGT/blob/245fa92ec7e4533253d1f25f076f9d9026b8692a/CMakeLists.txt#L24-L29" target="_blank" rel="noopener">SlicerIGT/SlicerIGT/blob/245fa92ec7e4533253d1f25f076f9d9026b8692a/CMakeLists.txt#L24-L29</a></h4>



    <pre class="onebox"><code class="lang-txt">
      <ol class="start lines" start="24" style="counter-reset: li-counter 23 ;">
          <li>if (NOT DEFINED Slicer_EXTENSION_SOURCE_DIRS)
</li>
          <li>  find_package(SlicerIGSIO REQUIRED) 
</li>
          <li>else()
</li>
          <li>  # Allow usage if dependent extension is bundled
</li>
          <li>  find_package(IGSIO REQUIRED) 
</li>
          <li>endif()
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Note that a different <code>find_package(...)</code> may be needed if the dependent extension is a suprerbuild-type extension that includes some additional libraries (SlicerIGSIO extension is a superbuild-type extension that included the <code>IGSIO</code> library).</p>
<p>In your case the fix is probably to change the top-level CMakeLists.txt file in SegmentRegistration extension from this:</p>
<pre><code class="lang-auto">find_package(SlicerProstate REQUIRED)
find_package(SlicerRT REQUIRED)
</code></pre>
<p>to this:</p>
<pre><code class="lang-auto">if (NOT DEFINED Slicer_EXTENSION_SOURCE_DIRS)
  find_package(SlicerProstate REQUIRED)
  find_package(SlicerRT REQUIRED)
else()
  # Allow usage if dependent extension is bundled
  #find_package(IGSIO REQUIRED) 
endif()
</code></pre>
<p>You may also need to do it for SlicerRT or other extensions that are bundled. If you confirmed that the changes fix the bundling issue on your computer then you can submit pull requests to the repositories.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Do you have any comments? Do you find the recommended changes to be a good solution?</p>

---

## Post #3 by @darabi (2023-07-28 07:24 UTC)

<p>I can confirm that the proposed change fixes my issue. I haven’t attempted a Slicer full build with this change.</p>
<p>The pull request is here:</p><aside class="onebox githubpullrequest" data-onebox-src="https://github.com/SlicerRt/SegmentRegistration/pull/8">
  <header class="source">

      <a href="https://github.com/SlicerRt/SegmentRegistration/pull/8" target="_blank" rel="noopener nofollow ugc">github.com/SlicerRt/SegmentRegistration</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/SlicerRt/SegmentRegistration/pull/8" target="_blank" rel="noopener nofollow ugc">ENH: allow build of extensions which depend on this one</a>
      </h4>

    <div class="branches">
      <code>SlicerRt:master</code> ← <code>darabi:fix-cmake-find-package</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-07-28" data-time="07:19:45" data-timezone="UTC">07:19AM - 28 Jul 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/darabi" target="_blank" rel="noopener nofollow ugc">
            <img alt="darabi" src="https://avatars.githubusercontent.com/u/473055?v=4" class="onebox-avatar-inline" width="20" height="20">
            darabi
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 6 additions and 2 deletions">
          <a href="https://github.com/SlicerRt/SegmentRegistration/pull/8/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+6</span>
            <span class="removed">-2</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The unconditional use of find_package leads to an error during the build process<span class="show-more-container"><a href="https://github.com/SlicerRt/SegmentRegistration/pull/8" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden"> of dependent extensions. See

https://discourse.slicer.org/t/30698</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Thank you for your help!</p>

---
