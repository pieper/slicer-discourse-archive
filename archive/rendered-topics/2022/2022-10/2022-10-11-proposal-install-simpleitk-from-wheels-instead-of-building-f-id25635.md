# Proposal: Install SimpleITK from wheels instead of building from source

**Topic ID**: 25635
**Date**: 2022-10-11
**URL**: https://discourse.slicer.org/t/proposal-install-simpleitk-from-wheels-instead-of-building-from-source/25635

---

## Post #1 by @jcfr (2022-10-11 04:31 UTC)

<p>Now that Slicer <a href="https://github.com/Slicer/Slicer/pull/6564">PR-6564</a> adding support for building ITK with a custom namespace has been integrated, installing SimpleITK from wheels should be possible.</p>
<p>Pros:</p>
<ol>
<li>Reduced build time by a factor x2 (and probably more on windows)</li>
<li>Version of SimpleITK bundled in Slicer may be update-able using <code>pip</code>, this would allow to install a newer SimpleITK in a released Slicer distribution.</li>
<li>Reduced build-system complexity by removing external projects <code>Swig</code>, <code>PCRE</code> and <code>SimpleITK</code> and introducing <code>python-SimpleITK</code></li>
</ol>
<p>Cons:</p>
<ol>
<li>Fixes integrated in ITK C++ that is used to build Slicer may not be immediately be available in the nightly build,  they may only be available once new SimpleITK wheels are released.</li>
</ol>
<h2><a name="p-84382-questions-1" class="anchor" href="#p-84382-questions-1" aria-label="Heading link"></a>Questions</h2>
<p>Assuming SimpleITK wheels can be used, should we move forward with this proposal ?</p>
<p>Should we distribute <a href="https://github.com/SimpleITK/SlicerSimpleFilters">SimpleFilters</a> as a standalone extension and further reduce the size of the main Slicer package ?</p>
<ul>
<li><code>_SimpleITK.cpython-39-x86_64-linux-gnu.so</code> is <code>259M</code> on Linux</li>
<li><code>_SimpleITK.cpython-39-darwin.so</code> is <code>201M</code> on macOS</li>
<li><code>_SimpleITK.cp39-win_amd64.pyd</code> is <code>10M</code> on Windows</li>
</ul>
<p>Rational for smaller library on Windows:</p>
<blockquote>
<pre><code class="lang-auto"># SimpleITK has large internal libraries, which take an extremely long
# time to link on windows when they are static. Creating shared
# SimpleITK internal libraries can reduce linking time. Also the size
# of the debug libraries are monstrous. Using shared libraries for
# debug, reduce disc requirements, and can improve linking
# times. However, these shared libraries take longer to load than the
# monolithic target from static libraries.
</code></pre>
</blockquote>
<p><em>Source: <a href="https://github.com/Slicer/Slicer/commit/ff8f546e4d88db793f8d8a8973625a0c6da91598">Slicer@ff8f546e4</a> (COMP: Adding option for SimpleITK as a shared library)</em></p>
<h2><a name="p-84382-preliminary-testing-2" class="anchor" href="#p-84382-preliminary-testing-2" aria-label="Heading link"></a>Preliminary testing</h2>
<p>After removing <code>ITK_AUTOLOAD_PATH</code> from the environment, the SimpleITK package could successfully be installed &amp; imported  on Linux (Ubuntu 20.04.4).</p>
<pre data-code-wrap="python"><code class="lang-python">import os
del os.environ["ITK_AUTOLOAD_PATH"]
import SimpleITK
</code></pre>
<p>That said, attempting to apply a filter by leveraging the <code>SlicerSimpleFilter</code> module failed with the following error:</p>
<pre data-code-wrap="python"><code class="lang-python">Exception thrown in SimpleITK ImageFileReader_Execute: /tmp/SimpleITK/Code/IO/src/sitkImageReaderBase.cxx:97:

sitk::ERROR: The file "slicer:0x561741d91310#vtkMRMLScalarVolumeNode1" does not exist.
</code></pre>
<p>This means that we should revisit how the <code>SlicerSimpleFilter</code> module access volume node information by instead passing numpy array by leveraging <code>vtk.util.numpy_support</code> like what is done in <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/4fd5ea0005e81a473eb12460e607ba76f0e382e1/Wrapping/Generators/Python/itk/support/extras.py#L626-L727">itk.vtk_image_from_image/itk.image_from_vtk_image</a> or  <a href="https://github.com/dave3d/dicom2stl/blob/main/utils/sitk2vtk.py">sitk2vtk.py</a>/<a href="https://github.com/dave3d/dicom2stl/blob/main/utils/vtk2sitk.py">vtk2sitk.py</a></p>

---

## Post #2 by @lassoan (2022-10-19 06:20 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="1" data-topic="25635">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Assuming SimpleITK wheels can be used, should we move forward with this proposal ?</p>
</blockquote>
</aside>
<p>Yes! (due to the reasons you described above)</p>
<aside class="quote no-group" data-username="jcfr" data-post="1" data-topic="25635">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Should we distribute <a href="https://github.com/SimpleITK/SlicerSimpleFilters">SimpleFilters</a> as a standalone extension and further reduce the size of the main Slicer package ?</p>
</blockquote>
</aside>
<p>Yes, because reducing the installer size (and maybe reducing startup time?) would be very useful. Especially because ITKPython wrapping is kept being improved so developers may choose to use that instead of SimpleITK. For extensions in Slicer-5.3 and later we could add SimpleITK extension as a dependency if the extension uses SimpleITK.</p>

---

## Post #3 by @blowekamp (2022-10-21 12:43 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="1" data-topic="25635">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<ol>
<li>Fixes integrated in ITK C++ that is used to build Slicer may not be immediately be available in the nightly build, they may only be available once new SimpleITK wheels are released.</li>
</ol>
</blockquote>
</aside>
<p>SimpleITK rebuild builds packages for most of the common wheels each night when there has been a source code change in the master branch. Currently these are just uploaded to Github for the “latest” release, and discarded when the next latest package is created. Discussions have occurred if it would be useful to upload these packages to an S3 bucket or some other place to be archived for some period ( total size / time limit ). This could enabled fixes and contributions to SimpleITK to be readily available to the Slicer community.</p>

---

## Post #4 by @jamesobutler (2023-01-13 04:07 UTC)

<p>Things have observed to break down when Slicer’s SimpleITK is uninstalled a SimpleITK upstream version is installed from whl. <a href="https://github.com/Slicer/Slicer/issues/6711" class="inline-onebox" rel="noopener nofollow ugc">Slicer's embedded SimpleITK can be removed by pip · Issue #6711 · Slicer/Slicer · GitHub</a></p>
<p>As of right now it seems that proceeding with using SimpleITK whl files is not possible within Slicer due to requiring the fixes made in <a href="https://github.com/Slicer/Slicer/pull/6606" class="inline-onebox" rel="noopener nofollow ugc">BUG: Update SimpleITK to fix test_sitkUtils by jcfr · Pull Request #6606 · Slicer/Slicer · GitHub</a> which are not in SimpleITK upstream.</p>

---

## Post #5 by @jamesobutler (2025-12-26 22:51 UTC)

<p>This proposal has been completed with the integration of the following commits:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/3c72591d38fa22e8496864eed6805e8e7dcf08db">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/3c72591d38fa22e8496864eed6805e8e7dcf08db" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/3c72591d38fa22e8496864eed6805e8e7dcf08db" target="_blank" rel="noopener nofollow ugc">ENH: Replace usage of custom SimpleITK in sitkUtils</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2025-12-26" data-time="22:50:02" data-timezone="UTC">10:50PM - 26 Dec 25 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="changed 1 files with 85 additions and 127 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/3c72591d38fa22e8496864eed6805e8e7dcf08db" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+85</span>
          <span class="removed">-127</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This updates PullVolumeFromSlicer and PushVolumeToSlicer to utilize the vtk2sitk<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/3c72591d38fa22e8496864eed6805e8e7dcf08db" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden"> and sitk2vtk methods that do not rely on the existing custom SimpleITK for image conversion.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/f87c977465f3b63219456186b7673f5c12e8b514">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/f87c977465f3b63219456186b7673f5c12e8b514" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/f87c977465f3b63219456186b7673f5c12e8b514" target="_blank" rel="noopener nofollow ugc">COMP: Switch building SimpleITK from source to using pre-built Whl</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2025-12-26" data-time="22:50:02" data-timezone="UTC">10:50PM - 26 Dec 25 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="changed 10 files with 100 additions and 495 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/f87c977465f3b63219456186b7673f5c12e8b514" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+100</span>
          <span class="removed">-495</span>
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
