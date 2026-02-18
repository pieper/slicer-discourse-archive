# Slicer Build Environment Upgraded to `qt5-almalinux8-gcc14`

**Topic ID**: 43802
**Date**: 2025-07-22
**URL**: https://discourse.slicer.org/t/slicer-build-environment-upgraded-to-qt5-almalinux8-gcc14/43802

---

## Post #1 by @jcfr (2025-07-22 05:19 UTC)

<p>The build environment used for generating Slicer Preview and its extensions has been upgraded from <code>qt5-centos7-gcc7</code> to <code>qt5-almalinux8-gcc14</code>.</p>
<p>This update brings improved C++ standards support, better compatibility with modern systems, and eliminates complications related to the <em>Dual ABI</em> issue previously discussed <a href="https://discourse.slicer.org/t/temporary-disabling-of-stable-extension-builds-in-preparation-for-slicer-5-8-release-visual-studio-update/41207/7">here</a>.</p>
<h3><a name="p-126953-comparison-of-build-environments-1" class="anchor" href="#p-126953-comparison-of-build-environments-1" aria-label="Heading link"></a>Comparison of Build Environments</h3>
<div class="md-table">
<table>
<thead>
<tr>
<th>Build Environment</th>
<th>Minimum Required <code>glibc</code></th>
<th>Manylinux Policy</th>
<th>GCC Version</th>
<th>Compatible Systems</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>qt5-centos7-gcc7</code></td>
<td>2.17</td>
<td><code>manylinux2014</code>, <code>manylinux_2_17</code></td>
<td>GCC 7</td>
<td>Debian 8+<br>Ubuntu 13.10+<br>Fedora 19+<br>RHEL 7+</td>
</tr>
<tr>
<td><code>qt5-almalinux8-gcc14</code></td>
<td>2.28</td>
<td><code>manylinux_2_28</code></td>
<td>GCC 14</td>
<td>Debian 10+<br>Ubuntu 18.10+<br>Fedora 29+<br>RHEL 8+</td>
</tr>
</tbody>
</table>
</div><h3><a name="p-126953-important-note-for-extension-developers-2" class="anchor" href="#p-126953-important-note-for-extension-developers-2" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/warning.png?v=15" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> Important Note for Extension Developers <img src="https://emoji.discourse-cdn.com/twitter/warning.png?v=15" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"></h3>
<p>Due to <em>Dual ABI</em> issue referenced above, the extensions containing compiled C++ code (e.g., Loadable or CLI modules) <strong>built before July 23, 2025</strong> using the older environment <strong>are not compatible</strong> with the updated Slicer Preview. Please rebuild your extensions to ensure compatibility.</p>

---

## Post #2 by @jcfr (2025-07-24 13:32 UTC)

<p><strong>Update:</strong></p>
<p>To address remaining test failures on Linux systems using non-system Qt installations, the <code>krb5-gssapi-stub</code> project and its associated build option <code>Slicer_BUILD_KRB5_GSSAPI_STUB</code> have been introduced.</p>
<p>When enabled, this project builds a minimal <code>libgssapi_krb5.so.2</code> stub library that exports only the <code>GSS_C_NT_HOSTBASED_SERVICE</code> symbol. This satisfies Qt5Network’s GSSAPI linkage requirements without introducing full Kerberos or OpenSSL system dependencies, which may conflict with those bundled with Slicer.</p>
<p>By default, the stub is <strong>automatically built only when</strong>:</p>
<ul>
<li>The platform is Linux (i.e., <code>UNIX AND NOT APPLE</code>)</li>
<li><code>Slicer_USE_SYSTEM_QT</code> is <code>OFF</code> (i.e., using a non-system Qt installation)</li>
<li>The <code>Qt5::Network</code> target reports <code>gssapi</code> as an enabled feature</li>
</ul>
<p>This logic avoids building the stub unnecessarily and ensures compatibility when Qt has been installed via the Qt online installer or a custom prefix (which often links against Kerberos).</p>
<p>To override the default detection logic, developers can explicitly set the option:</p>
<pre data-code-wrap="bash"><code class="lang-bash">-D Slicer_BUILD_KRB5_GSSAPI_STUB:BOOL=ON  # force build
-D Slicer_BUILD_KRB5_GSSAPI_STUB:BOOL=OFF # disable build
</code></pre>
<p>See <a href="https://github.com/Slicer/Slicer/pull/8598">PR-8598</a> (BUG: Add krb5-gssapi-stub to avoid GSSAPI runtime linkage issues on Linux)</p>

---

## Post #3 by @fedorov (2025-08-05 02:16 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> could this update be the cause of this error “Error: could not load cache” on Linux for dcmqi, which started on Jul 22? <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;begin=2025-07-11&amp;end=2025-08-01&amp;filtercount=2&amp;showfilters=1&amp;filtercombine=and&amp;field1=buildname&amp;compare1=63&amp;value1=dcmqi&amp;field2=buildname&amp;compare2=63&amp;value2=-g%2B%2B" class="inline-onebox">SlicerPreview</a></p>
<p>I am not sure dcmqi is the only extension affected - SlicerRT started failing on Jul 22 as well: <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;begin=2025-07-11&amp;end=2025-08-01&amp;filtercount=2&amp;showfilters=1&amp;filtercombine=and&amp;field1=buildname&amp;compare1=63&amp;value1=-g%2B%2B&amp;field2=buildname&amp;compare2=63&amp;value2=slicerrt" class="inline-onebox">SlicerPreview</a></p>
<p>cc: <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #4 by @Davide_Punzo (2025-08-05 08:14 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> I just wanted to report that I have the following issue on:</p>
<ul>
<li>
<p>OS: Ubuntu 25.04</p>
</li>
<li>
<p>Compiler: GCC 14.2.0</p>
</li>
<li>
<p>CMake: 3.31.8</p>
</li>
<li>
<p>Qt: 5.15.2 (from online installer)</p>
</li>
</ul>
<p>Problem: When launching Slicer, the following error occurs:</p>
<p>./Slicer /home/davide/Development/Slicer/Slicer-SuperBuild-Debug/Slicer-build/bin/./SlicerApp-real: symbol lookup error: /lib/x86_64-linux-gnu/libtirpc.so.3: undefined symbol: GSS_C_NT_USER_NAME, version gssapi_krb5_2_MIT</p>
<p>Root Cause: The system’s libtirpc.so.3 library conflicts with Slicer’s built-in GSS/Kerberos libraries, causing a symbol version mismatch.</p>
<p>Working Solutions:</p>
<ol>
<li>
<p>Remove Slicer’s GSS library (allows fallback to system library): rm /path/to/Slicer-build/bin/libgssapi_krb5.so*</p>
</li>
<li>
<p>Disable GSS API stub during build: cmake -D Slicer_BUILD_KRB5_GSSAPI_STUB:BOOL=OFF …</p>
</li>
</ol>
<p>Since there’s a working solution for the GSS_C_NT_USER_NAME symbol lookup error on Ubuntu 25.04, this isn’t a high-priority issue. However, it might be worth documenting this known compatibility issue and its workarounds in the official Slicer build instructions to help other users who encounter the same problem.</p>

---

## Post #5 by @RafaelPalomar (2025-08-08 08:02 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="3" data-topic="43802">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p><a class="mention" href="/u/jcfr">@jcfr</a> could this update be the cause of this error “Error: could not load cache” on Linux for dcmqi, which started on Jul 22? <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;begin=2025-07-11&amp;end=2025-08-01&amp;filtercount=2&amp;showfilters=1&amp;filtercombine=and&amp;field1=buildname&amp;compare1=63&amp;value1=dcmqi&amp;field2=buildname&amp;compare2=63&amp;value2=-g%2B%2B" rel="noopener nofollow ugc">SlicerPreview</a></p>
</blockquote>
</aside>
<p><a class="mention" href="/u/fedorov">@fedorov</a>, <a class="mention" href="/u/jcfr">@jcfr</a>, SlicerSOFA on Linux is also having the same issue. What sets these extensions apart is that they are Superbuild extensions. I have done a quick scan and found errors starting on July 22nd for other superbuild extensions (not the same error, though):</p>
<ul>
<li>SlicerVMTK: <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;begin=2025-07-11&amp;end=2025-08-01&amp;filtercount=2&amp;showfilters=1&amp;filtercombine=and&amp;field1=buildname&amp;compare1=63&amp;value1=vmtk&amp;field2=buildname&amp;compare2=63&amp;value2=-g%252B%252B" rel="noopener nofollow ugc">SlicerPreview</a></li>
<li>SlicerOpenIGTLink: <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;begin=2025-07-11&amp;end=2025-08-01&amp;filtercount=2&amp;showfilters=1&amp;filtercombine=and&amp;field1=buildname&amp;compare1=63&amp;value1=OpenIGTLink&amp;field2=buildname&amp;compare2=63&amp;value2=-g%252B%252B" rel="noopener nofollow ugc">SlicerPreview</a></li>
</ul>

---

## Post #6 by @fedorov (2025-08-08 15:10 UTC)

<p>Can someone at Kitware confirm that the issue is not in some cache or something else leftover on the factory machines that need to be reset?</p>
<p>It is not the first time we have mysterious errors, and I think in the past there were cases when those were fixed by some magic by factory machines maintainers.</p>

---

## Post #7 by @jcfr (2025-08-08 15:25 UTC)

<p>Thanks for bringing this up <img src="https://emoji.discourse-cdn.com/twitter/folded_hands.png?v=14" title=":folded_hands:" class="emoji" alt=":folded_hands:" loading="lazy" width="20" height="20">, we will review <img src="https://emoji.discourse-cdn.com/twitter/rocket.png?v=14" title=":rocket:" class="emoji" alt=":rocket:" loading="lazy" width="20" height="20"> and follow-up.</p>
<p>For additional context, extension builds are orchestrated running the scripts maintained at <a href="https://github.com/Slicer/DashboardScripts">Slicer/DashboardScripts</a></p>
<p>Beside of building the stable extensions against the existing Slicer Stable build tree having its <code>site-packages</code> directory restored daily, there is no additional <em>caching</em>.</p>

---

## Post #8 by @lassoan (2025-08-26 18:03 UTC)

<p>Several projects (<a href="https://slicer.cdash.org/viewBuildError.php?buildid=3907129">SlicerIGSIO</a>, <a href="https://slicer.cdash.org/viewBuildError.php?buildid=3907036">SlicerOpenIGTLink</a>, <a href="https://slicer.cdash.org/viewBuildError.php?buildid=3907177">SlicerANTs</a>, <a href="https://slicer.cdash.org/viewBuildError.php?buildid=3907125">SlicerRadiomics</a>) have this error: <code>gmake[5]: *** read jobs pipe: Bad file descriptor.  Stop.</code>.</p>
<p>This seems to be related to the toolchain, as these packages have no problems on Windows and macOS and did not have issues with previous Linux versions.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> Could you have a look? Thank you!</p>

---

## Post #9 by @jcfr (2025-08-26 21:29 UTC)

<p>The underlying image is being updated to include GNU Make 4.4 instead of GNU Make 4.2. We expect this to be completed either this evening or tomorrow.</p>

---

## Post #10 by @jcfr (2025-08-27 22:07 UTC)

<p>The build environment has been updated to include GNU Make 4.4:</p>
<pre><code class="lang-auto">$ slicer-buildenv-qt5-almalinux8-gcc14-latest make --version
GNU Make 4.4
Built for x86_64-pc-linux-gnu
</code></pre>
<p>In addition of these updates, the following ones have been integrated:</p>
<ul>
<li>ninja: <code>1.11.1.g95dee.kitware.jobserver-1</code> → <code>1.13.1</code></li>
<li>automake <code>1.16</code> → <code>1.17</code></li>
<li>libtool <code>2.4.6</code> → <code>2.5.3</code></li>
</ul>

---

## Post #11 by @jcfr (2025-08-28 13:04 UTC)

<p>To follow-up, the issue has not been fixed by the update of GNU Make, we will further investigate and report back.</p>

---

## Post #12 by @jcfr (2025-09-03 22:25 UTC)

<p>Thanks to the insights of <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> and input of others during the last Slicer weekly meeting, we were able to identify the issues.</p>
<p>This should be fixed after integration the following pull request:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8691">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8691" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8691" target="_blank" rel="noopener">COMP: Ensure BUILD_JOB_SERVER_AWARE is set for external projects</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>jcfr:fix-make-jobserver-support-with-newer-cmake</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-09-03" data-time="22:21:29" data-timezone="UTC">10:21PM - 03 Sep 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jcfr" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
            jcfr
          </a>
        </div>

        <div class="lines" title="3 commits changed 3 files with 17 additions and 1 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8691/files" target="_blank" rel="noopener">
            <span class="added">+17</span>
            <span class="removed">-1</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This pull request updates the build system to ensure the `BUILD_JOB_SERVER_AWARE<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8691" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">` option is set for external projects when using CMake &gt;= 3.28. It addresses the `gmake[N]: *** read jobs  pipe: Bad file descriptor.` issue associated with the build command.

1. Modify `ExternalProjectDependency.cmake` to set `BUILD_JOB_SERVER_AWARE`.
2. Update CTK configuration to ensure `BUILD_JOB_SERVER_AWARE` is set.
3. Ensure this option is also set for extensions external projects

See https://discourse.slicer.org/t/slicer-build-environment-upgraded-to-qt5-almalinux8-gcc14/43802/8?u=jcfr</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>For more details:</p>
<ul>
<li><a href="https://gitlab.kitware.com/cmake/cmake/-/issues/26398" class="inline-onebox">ExternalProject: CMake 3.28.0 regressed INSTALL_COMMAND+LOG_INSTALL with GNU make (#26398) · Issues · CMake / CMake · GitLab</a></li>
<li><a href="https://gitlab.kitware.com/cmake/cmake/-/merge_requests/8667" class="inline-onebox">ExternalProject: Enable make job server with explicit build command (!8667) · Merge requests · CMake / CMake · GitLab</a></li>
<li><a href="https://gitlab.kitware.com/cmake/cmake/-/merge_requests/10014" class="inline-onebox">execute_process: Restore CLOEXEC on OUTPUT_FILE and ERROR_FILE descriptors (!10014) · Merge requests · CMake / CMake · GitLab</a></li>
</ul>

---

## Post #13 by @lkcl (2025-12-16 16:05 UTC)

<p>still present in Slicer-5.11.0-2025-12-15-linux-amd64</p>

---
