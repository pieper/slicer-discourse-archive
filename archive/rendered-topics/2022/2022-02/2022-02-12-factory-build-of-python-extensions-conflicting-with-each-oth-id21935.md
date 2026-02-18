# Factory build of python extensions conflicting with each other

**Topic ID**: 21935
**Date**: 2022-02-12
**URL**: https://discourse.slicer.org/t/factory-build-of-python-extensions-conflicting-with-each-other/21935

---

## Post #1 by @jamesobutler (2022-02-12 15:07 UTC)

<p>I noticed an issue occurring during the factory build of python extensions where an extension may be installing new python packages which results in Slicer core python packages having their installed version modified. This may be with general tools like <code>pip</code>, <code>setuptools</code>, etc.</p>
<p>When this happens if impacts all extensions built afterwards which have to use modified versions of these packages. This makes it difficult to make sure a Slicer extension that includes additional python packages is going to be successful because it can’t expect that it will be using the same versions of the tools like <code>pip</code> and <code>setuptools</code> from Slicer core.</p>
<p>For example SlicerRadiomics was built after SlicerJupyter. SlicerJupyter installs a large set of python packages (<a href="https://slicer.cdash.org/viewBuildError.php?type=1&amp;buildid=2588996" class="inline-onebox" rel="noopener nofollow ugc">CDash</a>) where the build process says to install to a special location.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerJupyter/blob/4c69a34746a273290f977a9823c8171498da865f/SuperBuild/External_python-packages.cmake#L42-L68">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerJupyter/blob/4c69a34746a273290f977a9823c8171498da865f/SuperBuild/External_python-packages.cmake#L42-L68" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerJupyter/blob/4c69a34746a273290f977a9823c8171498da865f/SuperBuild/External_python-packages.cmake#L42-L68" target="_blank" rel="noopener nofollow ugc">Slicer/SlicerJupyter/blob/4c69a34746a273290f977a9823c8171498da865f/SuperBuild/External_python-packages.cmake#L42-L68</a></h4>



    <pre class="onebox">      <code class="lang-cmake">
        <ol class="start lines" start="42" style="counter-reset: li-counter 41 ;">
            <li># Alternative python prefix for installing extension python packages</li>
            <li>set(python_packages_DIR "${CMAKE_BINARY_DIR}/python-packages-install")</li>
            <li>file(TO_NATIVE_PATH ${python_packages_DIR} python_packages_DIR_NATIVE_DIR)</li>
            <li>
            </li>
<li>set(python_sitepackages_DIR "${CMAKE_BINARY_DIR}/python-packages-install/${PYTHON_SITE_PACKAGES_SUBDIR}")</li>
            <li>file(TO_NATIVE_PATH ${python_sitepackages_DIR} python_sitepackages_DIR_NATIVE_DIR)</li>
            <li>
            </li>
<li>
            </li>
<li>set(_no_binary "")</li>
            <li>
            </li>
<li># Install jedi and requirements</li>
            <li># note: --force-reinstall ensures the python dependency is installed within</li>
            <li>#       this library's prefix for packaging.</li>
            <li>set(_install_jedi COMMAND ${CMAKE_COMMAND}</li>
            <li>    -E env</li>
            <li>      PYTHONNOUSERSITE=1</li>
            <li>      CC=${CMAKE_C_COMPILER}</li>
            <li>      PYTHONPATH=${python_sitepackages_DIR}</li>
            <li>      ${wrapper_script} ${PYTHON_EXECUTABLE} -m pip install</li>
            <li>        jedi==${${CMAKE_PROJECT_NAME}_jedi_VERSION}</li>
        </ol>
      </code>
    </pre>


  This file has been truncated. <a href="https://github.com/Slicer/SlicerJupyter/blob/4c69a34746a273290f977a9823c8171498da865f/SuperBuild/External_python-packages.cmake#L42-L68" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>During the process it appears that <code>setuptools</code> is uninstalled but not reinstalled in the expected Slicer core location. This results in a SlicerRadiomics build error seemingly saying that there is no <code>setuptools</code> available to use (<a href="https://slicer.cdash.org/viewBuildError.php?buildid=2589004" class="inline-onebox" rel="noopener nofollow ugc">CDash</a>)</p>
<p>I wonder if Slicer core external python projects should be re-run after each extension is built to make sure the extension is built against the expected versions in Slicer core. Or some other method to make sure that factory built extensions are not modifying the Slicer core build tree so that each subsequent factory built extension is built against the same version of the build tree.</p>

---

## Post #2 by @pieper (2022-02-12 15:57 UTC)

<p>This is a really important point <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, thanks for bringing it up.  A clean solution could be to copy the Slicer tree to a fresh directory so that each extension is installed and tested independently.</p>

---

## Post #3 by @lassoan (2022-02-13 14:13 UTC)

<p>When an extension is built then it may rely on all extension that it depends on (recursively), so if we save the state then it may need to be a stack where we can push the state of the folder and then pop that state (instead of always just resetting the original state).</p>
<p>This may not require entire folder copying because <code>pip</code> can store all package versions in a string and then restore that state.</p>

---

## Post #4 by @jcfr (2022-04-29 08:34 UTC)

<p>To follow-up on this, the SlicerJupyter extension has been updated to remove the use of <code>--force-reinstall</code>.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/SlicerJupyter/pull/71">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerJupyter/pull/71" target="_blank" rel="noopener">github.com/Slicer/SlicerJupyter</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/SlicerJupyter/pull/71" target="_blank" rel="noopener">COMP: Fix python install to prevent main site-packages corruption</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>jcfr:fix-python-package-install</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-04-29" data-time="08:32:37" data-timezone="UTC">08:32AM - 29 Apr 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 0 additions and 3 deletions">
        <a href="https://github.com/Slicer/SlicerJupyter/pull/71/files" target="_blank" rel="noopener">
          <span class="added">+0</span>
          <span class="removed">-3</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This commit reverts use of `--force-reinstall` originally introduced in c59b08fa<span class="show-more-container"><a href="https://github.com/Slicer/SlicerJupyter/pull/71" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">9 (Fix python package installation).

The use of `--force-reinstall` led to removal of package like `setuptools` from the `site-packages` directory associated with the application and was causing the build of following extension (e.g SlicerRadiomics) to fail.

See https://discourse.slicer.org/t/factory-build-of-python-extensions-conflicting-with-each-other/21935</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
