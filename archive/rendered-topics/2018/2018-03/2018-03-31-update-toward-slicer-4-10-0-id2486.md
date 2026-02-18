# Update: Toward Slicer 4.10.0

**Topic ID**: 2486
**Date**: 2018-03-31
**URL**: https://discourse.slicer.org/t/update-toward-slicer-4-10-0/2486

---

## Post #1 by @jcfr (2018-03-31 08:16 UTC)

<h3><a name="p-10117-release-status-1" class="anchor" href="#p-10117-release-status-1" aria-label="Heading link"></a>release status</h3>
<p>We are getting close ! Thanks you everyone <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=15" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>But considering that:</p>
<ul>
<li>
<p><s>the last VTK update addressing the <a href="https://issues.slicer.org/view.php?id=4510">#4510</a> (<em>Cropping is broken with GPU Volume rendering if depth peeling is enabled</em>), also introduced a  <a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4071#note_395250">regression</a>.</s></p>
</li>
<li>
<p>there are still issues with the <a href="https://discourse.slicer.org/t/extension-not-built-by-build-system/2462">extension build system</a>. - <strong>will be addressed in 4.10.0</strong></p>
</li>
<li>
<p><s>issue <a href="https://issues.slicer.org/view.php?id=4511">#4511</a> (<em>Large camera view angle (used in OpenVR) not properly handled with GPU Volume Rendering</em>) is not yet resolved. That seriously limits the usability of the SlicerVirtualReality extension.</s></p>
</li>
<li>
<p>Pre-built and Locally-built 3dSlicer under Ubuntu 16.04 <a href="https://discourse.slicer.org/t/pre-build-or-locally-build-3dslicer-under-ubuntu-16-04-does-not-start-failed-to-obtain-launcher-executable-name/2322">do NOT start</a> - <strong>will be addressed in 4.10.0</strong></p>
</li>
<li>
<p><s><a href="https://issues.slicer.org/view.php?id=4530">#4530</a> Slice viewer are too small after switching to conventional layout</s></p>
</li>
<li>
<p><s><a href="https://issues.slicer.org/view.php?id=4517">#4517</a> macOS: Slicer dmg installer and Slicer app do not have the icon</s>. Now fixed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27123">r27123</a></p>
</li>
<li>
<p><s>and <a href="https://issues.slicer.org/search.php?project_id=3&amp;status%5B%5D=10&amp;status%5B%5D=30&amp;status%5B%5D=40&amp;status%5B%5D=50&amp;sticky=on&amp;target_version=Slicer%204.9.0&amp;sort=last_updated&amp;dir=DESC&amp;hide_status=-2&amp;match_type=0">few other ones</a>,</s></p>
</li>
</ul>
<p>I suggest we delay the release <s>by few days/s&gt;.</s></p><s>
<p>That should enable us to address the most critical issues and transition into their own extension: BRAINSTools, EMSegment, and SimpleITK. And ExpertAutomatedRegistration module into the existing <a href="https://github.com/Slicer/SlicerLegacyModules">LegacyModules</a> extension.</p>
<h3><a name="p-10117-infrastructure-updates-2" class="anchor" href="#p-10117-infrastructure-updates-2" aria-label="Heading link"></a>infrastructure updates</h3>
<p>The past few days were spent updating the CI and build infrastructure so that we have Linux build done with Qt5. And here it is:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66aae1fe2f437edac348d89a49939359cae58b58.png" data-download-href="/uploads/short-url/eEeODfPJ74e0Xqu6cQd8G3gh5nq.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66aae1fe2f437edac348d89a49939359cae58b58_2_690x70.png" alt="image" data-base62-sha1="eEeODfPJ74e0Xqu6cQd8G3gh5nq" width="690" height="70" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66aae1fe2f437edac348d89a49939359cae58b58_2_690x70.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66aae1fe2f437edac348d89a49939359cae58b58_2_1035x105.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66aae1fe2f437edac348d89a49939359cae58b58_2_1380x140.png 2x" data-dominant-color="BCCDD5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1794×183 25.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Since our server <code>metroplex</code> doesn’t have a host operating system suitable to generate distributable packages, it is using the build environment <a href="https://github.com/Slicer/SlicerBuildEnvironment">slicer/buildenv-qt5-centos7</a> (itself built on top of the <a href="https://github.com/dockbuild/dockbuild">dockbuild/centos7-devtoolset4-gcc5</a> dockbuild image)</p>
<p>Here is the section of the night script responsible for driving the Slicer Preview build and packaging. Note that <code>run_ctest_with_test</code> default to <code>FALSE</code>.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/DashboardScripts/blob/ab2f81bbab5ff720e25b5b1ac131d436169f7728/metroplex.sh#L4-L15">
  <header class="source">

      <a href="https://github.com/Slicer/DashboardScripts/blob/ab2f81bbab5ff720e25b5b1ac131d436169f7728/metroplex.sh#L4-L15" target="_blank" rel="noopener">github.com/Slicer/DashboardScripts</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/DashboardScripts/blob/ab2f81bbab5ff720e25b5b1ac131d436169f7728/metroplex.sh#L4-L15" target="_blank" rel="noopener">metroplex.sh</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/DashboardScripts/blob/ab2f81bbab5ff720e25b5b1ac131d436169f7728/metroplex.sh#L4-L15" rel="noopener"><code>ab2f81bba</code></a>
</div>



    <pre class="onebox"><code class="lang-sh">
      <ol class="start lines" start="4" style="counter-reset: li-counter 3 ;">
          <li># Changing directory is required by slicer-buildenv-qt5-centos7-latest</li>
          <li>cd  /home/kitware/Dashboards/Slicer</li>
          <li></li>
          <li># Slicer dashboard settings</li>
          <li>docker_args="-e run_ctest_with_disable_clean=${run_ctest_with_disable_clean-FALSE}"</li>
          <li>docker_args+=" -e run_ctest_with_update=${run_ctest_with_update-TRUE}"</li>
          <li>docker_args+=" -e run_ctest_with_test=${run_ctest_with_test-FALSE}" # XXX Re-enable testing after slicer/slicer-test images have been updated</li>
          <li></li>
          <li># Slicer 'Preview' release</li>
          <li>slicer-buildenv-qt5-centos7-latest \</li>
          <li>  --args "${docker_args}" \</li>
          <li>  ctest -S /work/DashboardScripts/metroplex-slicer_preview_nightly.cmake -VV -O /work/Logs/metroplex-slicer_preview_nightly.log</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The build itself uses the latest version of CMake (v3.11.0) and a <a href="https://github.com/dockbuild/ninja-jobserver">modified version</a> of ninja generator that supports  GNU make jobserver. This ensures the child processes spawn within each external projects communicate with the top-level process.</p>
<p>To control the number of overall processes, the <a href="https://discourse.slicer.org/t/ninja-build-using-too-many-cores/2304">CMAKE_JOB_* options</a> are particularly useful. In our case, we configure the compile and the link pool with different values. Considering <code>metroplex</code> has 32 cores and 32GB of memory, the settings are currently the following:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/DashboardScripts/blob/ab2f81bbab5ff720e25b5b1ac131d436169f7728/metroplex-slicer_preview_nightly.cmake#L47-L51">
  <header class="source">

      <a href="https://github.com/Slicer/DashboardScripts/blob/ab2f81bbab5ff720e25b5b1ac131d436169f7728/metroplex-slicer_preview_nightly.cmake#L47-L51" target="_blank" rel="noopener">github.com/Slicer/DashboardScripts</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/DashboardScripts/blob/ab2f81bbab5ff720e25b5b1ac131d436169f7728/metroplex-slicer_preview_nightly.cmake#L47-L51" target="_blank" rel="noopener">metroplex-slicer_preview_nightly.cmake</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/DashboardScripts/blob/ab2f81bbab5ff720e25b5b1ac131d436169f7728/metroplex-slicer_preview_nightly.cmake#L47-L51" rel="noopener"><code>ab2f81bba</code></a>
</div>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="47" style="counter-reset: li-counter 46 ;">
          <li>set(ADDITIONAL_CMAKECACHE_OPTION "</li>
          <li>-DCMAKE_JOB_POOLS:STRING=compile=16;link=8</li>
          <li>-DCMAKE_JOB_POOL_COMPILE:STRING=compile</li>
          <li>-DCMAKE_JOB_POOL_LINK:STRING=link</li>
          <li>")</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Given the highly templated nature of some of our code (SimpleITK, ITK, vtkITK, …), the link jobs require a <a href="https://stackoverflow.com/questions/26415909/how-can-i-reduce-the-compile-time-memory-footprint-of-large-templates">lot of memory</a>, for that reason we set a smaller maximum number of link job.</p>
<p>This will also be particularly useful on CircleCi where there is also 32core but <em>only</em> <a href="https://circleci.com/docs/2.0/configuration-reference/#resource_class">4GB</a> (by default), we will be able to leverage the number of core while drastically limiting the number of parallel link job.</p></s>

---

## Post #2 by @pieper (2018-04-03 14:53 UTC)

<p>Thanks for pulling this together Jc!</p>
<p>I’d add this slice rendering performance issue to the short list of issues that we should resolve before the release: <a href="https://issues.slicer.org/view.php?id=4496">https://issues.slicer.org/view.php?id=4496</a></p>
<p>Reslicing is a core function and I think people will be disappointed if we have a release with a major regression.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> have you done any further testing or debugging on this?</p>

---

## Post #3 by @lassoan (2018-04-04 05:58 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="2486">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p><a class="mention" href="/u/lassoan">@lassoan</a> have you done any further testing or debugging on this?</p>
</blockquote>
</aside>
<p>Yes, and I have a solution that makes slice browsing very fast (60-90fps now, instead of 10fps) on fast computers, with NVidia GPUs. I have some other attempts to improve performance, but those don’t seem to make much difference. See details here: <a href="https://github.com/Slicer/Slicer/pull/930" class="inline-onebox">Screen Freezing · Issue #930 · Slicer/Slicer · GitHub</a>.</p>

---

## Post #4 by @jamesobutler (2018-06-19 15:19 UTC)

<p>Out of curiosity, are there any new updates about when the next Slicer version is expected for release?  I saw this post is about 12 weeks old and couldn’t find any new information indicating a new timeline for release.</p>

---

## Post #5 by @lassoan (2018-06-19 22:53 UTC)

<p>There are still 19 open issues for 4.9 that must be addressed. My estimation would be a few more weeks.</p>

---

## Post #6 by @jcfr (2018-10-17 17:52 UTC)

<p>To follow up, all Slicer 4.9 issues have been addressed: <a href="https://issues.slicer.org/view_all_bug_page.php?filter=51308" class="inline-onebox">Issues · Slicer/Slicer · GitHub</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e740787a8d7d0ae6db2906f98fcdbeb160d6213a.png" data-download-href="/uploads/short-url/wZKqfjMTMppQPNtc2iKIrvzdTMm.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e740787a8d7d0ae6db2906f98fcdbeb160d6213a.png" alt="image" data-base62-sha1="wZKqfjMTMppQPNtc2iKIrvzdTMm" width="690" height="114" data-dominant-color="C0D6D7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">854×142 4.57 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
