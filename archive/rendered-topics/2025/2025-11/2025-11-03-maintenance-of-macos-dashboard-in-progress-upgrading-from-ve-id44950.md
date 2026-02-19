---
topic_id: 44950
title: "Maintenance Of Macos Dashboard In Progress Upgrading From Ve"
date: 2025-11-03
url: https://discourse.slicer.org/t/44950
---

# Maintenance of macOS dashboard in progress - upgrading from Ventura to Sequoia

**Topic ID**: 44950
**Date**: 2025-11-03
**URL**: https://discourse.slicer.org/t/maintenance-of-macos-dashboard-in-progress-upgrading-from-ventura-to-sequoia/44950

---

## Post #1 by @jcfr (2025-11-03 16:49 UTC)

<p>The macOS system named “computron” has been upgraded from <code>13.7.5</code> (Ventura) to <code>15.7.1</code> (Sequoia).</p>
<p>While we finish updating the build tools and Qt dependencies , <strong>macOS builds of Slicer and extensions are temporarily unavailable.</strong></p>
<h2><a name="p-129600-impacted-macos-builds-1" class="anchor" href="#p-129600-impacted-macos-builds-1" aria-label="Heading link"></a>Impacted macOS builds</h2>
<div class="md-table">
<table>
<thead>
<tr>
<th></th>
<th>Slicer Stable (5.8)</th>
<th>Slicer Preview</th>
</tr>
</thead>
<tbody>
<tr>
<td>Slicer Application</td>
<td>NA</td>
<td><img src="https://emoji.discourse-cdn.com/twitter/pause_button.png?v=15" title=":pause_button:" class="emoji only-emoji" alt=":pause_button:" loading="lazy" width="20" height="20"></td>
</tr>
<tr>
<td>Slicer Extensions</td>
<td><img src="https://emoji.discourse-cdn.com/twitter/pause_button.png?v=15" title=":pause_button:" class="emoji only-emoji" alt=":pause_button:" loading="lazy" width="20" height="20"></td>
<td><img src="https://emoji.discourse-cdn.com/twitter/pause_button.png?v=15" title=":pause_button:" class="emoji only-emoji" alt=":pause_button:" loading="lazy" width="20" height="20"></td>
</tr>
</tbody>
</table>
</div><p><em>Linux and Windows dashboards are unaffected.</em></p>
<h2><a name="p-129600-near-term-plan-2" class="anchor" href="#p-129600-near-term-plan-2" aria-label="Heading link"></a>Near-term plan</h2>
<ul>
<li>We’re targeting the <strong>Slicer 5.10</strong> release later this week (week of <strong>Nov 3, 2025</strong>).</li>
<li>To stay focused on that, we will <strong>not</strong> restore builds of <strong>Stable macOS extensions for Slicer 5.8</strong>.</li>
<li>Stable macOS extensions will resume <strong>after Slicer 5.10 is released</strong>.</li>
</ul>
<hr>
<p>Thanks for your patience and understanding <img src="https://emoji.discourse-cdn.com/twitter/folded_hands.png?v=15" title=":folded_hands:" class="emoji" alt=":folded_hands:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @jamesobutler (2025-11-03 21:55 UTC)

<p>As part of this upgrade, the XCode version has also been updated? The clang version is used in the build name when viewing entries on the Slicer cDash. Computron may possibly be using clang 17?</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/DashboardScripts/blob/359b580c0b448eedb3cd0db3d5de9a069f63564f/computron-slicer_preview_nightly.cmake#L21">
  <header class="source">

      <a href="https://github.com/Slicer/DashboardScripts/blob/359b580c0b448eedb3cd0db3d5de9a069f63564f/computron-slicer_preview_nightly.cmake#L21" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/DashboardScripts</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/DashboardScripts/blob/359b580c0b448eedb3cd0db3d5de9a069f63564f/computron-slicer_preview_nightly.cmake#L21" target="_blank" rel="noopener nofollow ugc">computron-slicer_preview_nightly.cmake</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/DashboardScripts/blob/359b580c0b448eedb3cd0db3d5de9a069f63564f/computron-slicer_preview_nightly.cmake#L21" rel="noopener nofollow ugc"><code>359b580c0</code></a>
</div>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="11" style="counter-reset: li-counter 10 ;">
          <li>dashboard_set(OPERATING_SYSTEM      "macOS")</li>
          <li>dashboard_set(SCRIPT_MODE           "Nightly")        # Experimental, Continuous or Nightly</li>
          <li>dashboard_set(Slicer_RELEASE_TYPE   "P")              # (E)xperimental, (P)review or (S)table</li>
          <li>dashboard_set(WITH_PACKAGES         TRUE)             # Enable to generate packages</li>
          <li>dashboard_set(GIT_TAG               "main")         # Specify a tag for Stable release</li>
          <li></li>
          <li>if(APPLE)</li>
          <li>  dashboard_set(CMAKE_OSX_DEPLOYMENT_TARGET "13.0")</li>
          <li>endif()</li>
          <li>dashboard_set(CTEST_CMAKE_GENERATOR "Unix Makefiles")</li>
          <li class="selected">dashboard_set(COMPILER              "clang-14.0.6")    # Used only to set the build name</li>
          <li>dashboard_set(CTEST_BUILD_FLAGS     "-j9 -l8")        # Use multiple CPU cores to build. For example "-j -l4" on unix</li>
          <li># By default, CMake auto-discovers the compilers</li>
          <li>#dashboard_set(CMAKE_C_COMPILER      "/path/to/c/compiler")</li>
          <li>#dashboard_set(CMAKE_CXX_COMPILER    "/path/to/cxx/compiler")</li>
          <li>dashboard_set(CTEST_BUILD_CONFIGURATION "Release")</li>
          <li>dashboard_set(WITH_MEMCHECK       FALSE)</li>
          <li>dashboard_set(WITH_COVERAGE       FALSE)</li>
          <li>dashboard_set(WITH_DOCUMENTATION  FALSE)</li>
          <li>dashboard_set(Slicer_BUILD_CLI    ON)</li>
          <li>dashboard_set(Slicer_USE_PYTHONQT ON)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @jcfr (2025-11-04 08:56 UTC)

<blockquote>
<p>As part of this upgrade, the XCode version has also been updated</p>
</blockquote>
<p>Not yet. Once this is done, we will evaluate if a workaround like the one required when updating from 10.13 (High Sierra) to 13 (Ventura) is needed.</p>
<p>See <a href="https://discourse.slicer.org/t/transition-of-macos-preview-build-from-host-10-13-high-sierra-to-13-ventura/28668/3" class="inline-onebox">Transition of macOS Preview build from host 10.13 (High Sierra) to 13 (Ventura) - #3 by jcfr</a></p>

---

## Post #4 by @jcfr (2025-11-08 05:28 UTC)

<p><strong>Updates:</strong></p>
<ul>
<li>
<p>XCode has been updated to <code>26.1</code> and clang version is now <code>17.0.0</code>.</p>
</li>
<li>
<p>Issue related to the build of Qt <code>5.15.18</code> should now all be sorted our and the build is in progress <img src="https://emoji.discourse-cdn.com/twitter/rocket.png?v=15" title=":rocket:" class="emoji" alt=":rocket:" loading="lazy" width="20" height="20"></p>
<p>For more details: <a href="https://github.com/commontk/qt-easy-build/pull/80" class="inline-onebox">[5.15.18] Fix detection of OpenGL Qt backend and OpenSSL linkage on macOS by jcfr · Pull Request #80 · commontk/qt-easy-build · GitHub</a></p>
</li>
</ul>

---
