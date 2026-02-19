---
topic_id: 40686
title: "Developing For Slicer On Apple Silicon Build Targeting X86 6"
date: 2024-12-13
url: https://discourse.slicer.org/t/40686
---

# Developing for Slicer on Apple Silicon (build targeting x86_64)

**Topic ID**: 40686
**Date**: 2024-12-13
**URL**: https://discourse.slicer.org/t/developing-for-slicer-on-apple-silicon-build-targeting-x86-64/40686

---

## Post #1 by @arhowe00 (2024-12-13 22:44 UTC)

<p>The <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/macos.html" rel="noopener nofollow ugc">developer docs</a> may need a minor update addressing development on the newer Macs (M-series chips). Here is a sufficient-for-development build from source on arm64 MacOS without requiring niche workarounds for specific libraries. The following steps explain how to build Slicer from source on M-chip computers. Note that the Slicer build still targets x86_64 (i.e. run through Rosetta 2), but native arm64 builds may be rolled out at a future date. To summarize the steps:</p>
<ol>
<li>Install Qt5 with x86_64 <code>brew</code></li>
<li>Use x86_64 <code>bash</code> to build Slicer</li>
<li>Turn off SimpleITK</li>
<li>There were a few libraries which could not compile using later versions of clang. This discussion post is coupled with <a href="https://github.com/Slicer/Slicer/pull/8097" rel="noopener nofollow ugc">PR#8097</a>, which cherry picks a few patches in files within <a href="https://github.com/libarchive/libarchive" rel="noopener nofollow ugc">libarchive</a>.</li>
</ol>
<p>This is an attempt to partially address <a href="https://github.com/Slicer/Slicer/issues/6811" rel="noopener nofollow ugc">#6811</a>.</p>
<h2><a name="p-120512-step-by-step-1" class="anchor" href="#p-120512-step-by-step-1" aria-label="Heading link"></a>Step-by-step:</h2>
<ol>
<li>
<p>Install the latest Xcode SDKs:</p>
<pre data-code-wrap="sh"><code class="lang-sh">xcode-select --install 
</code></pre>
</li>
<li>
<p>Checkout Slicer source files</p>
<pre data-code-wrap="sh"><code class="lang-sh">git clone https://github.com/Slicer/Slicer.git
</code></pre>
</li>
<li>
<p>Setup the development environment</p>
<pre><code class="lang-auto">cd Slicer
./Utilities/SetupForDevelopment.sh
</code></pre>
</li>
<li>
<p>Install x86_64 Homebrew.  You can install “x86_64 Homebrew” if you run the shell with Rosetta 2:</p>
<pre data-code-wrap="sh"><code class="lang-sh">arch -x86_64 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
</code></pre>
</li>
<li>
<p>Launch <code>/bin/bash</code> with Rosetta 2. x86_64 Homebrew is in <code>/usr/local/bin/brew</code>, and it installs binaries in <code>/usr/local/bin</code>. <code>/usr/local/bin</code> is added to <code>PATH</code> by default on MacOS, so all binaries are accessible without any custom profiles (e.g. <code>.bash_profile</code>, <code>.bashrc</code>). <strong>You should remain in the x86_64 <code>/bin/bash</code> for the rest of the build.</strong></p>
<pre data-code-wrap="sh"><code class="lang-sh">exec /usr/bin/arch -x86_64 /bin/bash --norc --noprofile
</code></pre>
<pre data-code-wrap="bash"><code class="lang-bash">export PATH="/usr/local/bin:$PATH"
brew install qt5
</code></pre>
<blockquote>
<p>Be aware: On MacOS, <code>/etc/paths</code> configures your <code>PATH</code> such that binaries installed by Homebrew will be preferred over those in <code>/bin</code>. For example, if you install an x86_64 bash with <code>/usr/local/bin/brew install bash</code>, Homebrew-installed x86_64 <code>/usr/local/bin/bash</code> will be resolved when typing <code>bash</code>, <em>not</em> <code>/bin/bash</code>. For native arm64 Homebrew, be careful to set <code>PATH=/opt/homebrew/bin:$PATH</code> in custom profiles, or x86_64 binaries will always be resolved first, including <code>brew</code>.</p>
</blockquote>
</li>
<li>
<p>Configure and build Slicer (from x86_64 <code>/bin/bash</code>). Note that arm64 <code>cmake</code> here is permissible:</p>
<pre data-code-wrap="bash"><code class="lang-bash">cd ..

cmake_build_type=Debug

cmake \
  -DQt5_DIR:PATH=/usr/local/opt/qt@5/lib/cmake/Qt5 \
  -DCMAKE_OSX_ARCHITECTURES:STRING=x86_64 \
  -DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=13.0 \
  -DCMAKE_BUILD_TYPE:STRING=$cmake_build_type \
  -DSlicer_USE_SYSTEM_QT:BOOL=ON \
  -DSlicer_USE_SimpleITK:BOOL=OFF \
  -B ./Slicer-$cmake_build_type \
  -S ./Slicer

cmake --build ./Slicer-$cmake_build_type
</code></pre>
</li>
</ol>
<h2><a name="p-120512-happy-developing-2" class="anchor" href="#p-120512-happy-developing-2" aria-label="Heading link"></a>Happy developing!</h2>
<p>Not all the tests pass, but you should be able to launch Slicer with <code>./Slicer-Debug/Slicer-build/Slicer</code>. This should make it easier to develop and iterate over 3DSlicer on Apple Silicon devices. Thank you to <a class="mention" href="/u/jared_vicory">@Jared_Vicory</a> for helpful input and <a class="mention" href="/u/jcfr">@jcfr</a> for the invaluable support.</p>

---

## Post #3 by @arhowe00 (2025-06-09 00:21 UTC)

<p>It appears that this build guide no longer works with the latest Xcode SDKs.</p>
<p>Instead, a downgrade is required due to the latest macOS SDK versions deprecating or excluding <code>fp.h</code>, among other things, in newer releases. Build issues were seen when installing VTK dependencies. I did not try bumping the VTK version used by Slicer or see whether later versions of VTK bump the VTK dependencies to versions that might fix build issues.</p>
<p>I have found that for Slicer v5.8.1 (11eaf62), downgrading the macOS SDK to 15.1, which is released with Xcode 16.1, I was able to build Slicer. To do this:</p>
<ol>
<li>Download <a href="https://developer.apple.com/services-account/download?path=/Developer_Tools/Xcode_16.1/Xcode_16.1.xip" rel="noopener nofollow ugc">Xcode 16.1</a> from <a href="http://xcodereleases.com" rel="noopener nofollow ugc">xcodereleases.com</a>.</li>
<li>Extract <code>Xcode_16.1.xip</code> and move it to <code>/Applications</code>.
<blockquote>
<p>Note: This extracts to <code>/Downloads/Xcode.app</code>, but you should rename it to  <code>Xcode_16.1.app</code>, as you will likely have multiple installations of <code>Xcode</code> on your system.</p>
</blockquote>
</li>
<li>Follow all steps from the guide above, except replace the configuration step with the following:<pre data-code-wrap="sh"><code class="lang-sh">cmake \
  -DQt5_DIR:PATH=/usr/local/opt/qt@5/lib/cmake/Qt5 \
  -DCMAKE_OSX_ARCHITECTURES:STRING=x86_64 \
  -DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=13.0 \
  -DCMAKE_OSX_SYSROOT:PATH=/Applications/Xcode_16.1.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.1.sdk \
  -DCMAKE_BUILD_TYPE:STRING=$cmake_build_type \
  -DSlicer_USE_SYSTEM_QT:BOOL=ON \
  -DSlicer_USE_SimpleITK:BOOL=OFF \
  -B ./Slicer-$cmake_build_type \
  -S ./Slicer
</code></pre>
</li>
<li>Follow all steps from above as usual.</li>
</ol>

---

## Post #4 by @jamesobutler (2025-06-09 00:32 UTC)

<aside class="quote no-group quote-modified" data-username="arhowe00" data-post="2" data-topic="40686">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/arhowe00/48/80367_2.png" class="avatar"> arhowe00:</div>
<blockquote>
<p>I did not try bumping the VTK version used by Slicer or see whether later versions of VTK bump the VTK dependencies to versions that might fix build issues.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/arhowe00">@arhowe00</a> I think this very well may fix the build issues. See for example the following thread with Xcode 16.3 where a specific build fix was included in VTK 9.4. Slicer 5.8.1 was based on a VTK 9.2 version while latest Slicer Preview is based on VTK 9.4, so I would definitely try building latest Slicer Preview with a newer Xcode.</p>
<aside class="onebox discoursetopic" data-onebox-src="https://discourse.vtk.org/t/compile-error-building-vtk-9-3-0-rc1-on-macos-sequoia/15528">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.vtk.org/t/compile-error-building-vtk-9-3-0-rc1-on-macos-sequoia/15528" target="_blank" rel="noopener nofollow ugc" title="11:44PM - 21 April 2025">VTK – 21 Apr 25</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/369;"><img src="https://discourse.vtk.org/uploads/default/original/1X/b7d45ff6520965c4fbd148f8d0b1f7720956fa24.png" class="thumbnail" width="690" height="369"></div>

<div class="title-wrapper">
  <h3><a href="https://discourse.vtk.org/t/compile-error-building-vtk-9-3-0-rc1-on-macos-sequoia/15528" target="_blank" rel="noopener nofollow ugc">Compile error building VTK-9.3.0.rc1 on MacOS sequoia</a></h3>
  <div class="topic-category">
      <span class="badge-wrapper bullet">
        <span class="badge-category-bg" style="background-color: #F7941D;"></span>
        <span class="badge-category clear-badge">
          <span class="category-name">Support</span>
        </span>
      </span>
  </div>
</div>

  <p>Building VTK-9.3.0.rc1 on MacOS Sequoia, running xcode Version 16.3 (16E140). Following compile error occurs:  [  1%] Building C object ThirdParty/zlib/vtkzlib/CMakeFiles/zlib.dir/zutil.c.o cd...</p>

  <p>
    <span class="label1">Reading time: 1 mins 🕑</span>
      <span class="label2">Likes: 2 ❤</span>
  </p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @jamesobutler (2025-06-09 00:38 UTC)

<p><a class="mention" href="/u/arhowe00">@arhowe00</a> You may also find helpful the instructions I added to the qt-easy-build project regarding building Slicer (x86_64) on Apple Silicon. I successfully built Qt 5.15.16 from source on an Apple silicon machine using the macOS 15.2 SDK. Building Qt from source allowed me to build a macOS package for distribution.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/jcfr/qt-easy-build/tree/5.15.16?tab=readme-ov-file#build-for-x86_64-on-apple-silicon-arm64">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/jcfr/qt-easy-build/tree/5.15.16?tab=readme-ov-file#build-for-x86_64-on-apple-silicon-arm64" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/jcfr/qt-easy-build/tree/5.15.16?tab=readme-ov-file#build-for-x86_64-on-apple-silicon-arm64" target="_blank" rel="noopener nofollow ugc">GitHub - jcfr/qt-easy-build at 5.15.16</a></h3>

  <p><a href="https://github.com/jcfr/qt-easy-build/tree/5.15.16?tab=readme-ov-file#build-for-x86_64-on-apple-silicon-arm64" target="_blank" rel="noopener nofollow ugc">5.15.16</a></p>

  <p><span class="label1">Scripts allowing to easily build Qt with OpenSSL support on Linux, macOS or Windows</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>With this branch I added patches for clang 16 compatibility, but I haven’t checked the status of things if using clang 17 which was released in Xcode 16.3. It is unclear why Apple bumped clang in a minor release of Xcode this time around.</p>

---

## Post #6 by @arhowe00 (2025-06-09 03:28 UTC)

<p>This is really helpful <a class="mention" href="/u/jamesobutler">@jamesobutler</a> , kudos!</p>

---

## Post #7 by @arhowe00 (2025-06-09 03:31 UTC)

<p>The fix in this reply is only needed if trying to build Slicer v5.8.1. If you need to build Slicer v5.8.1 or older and are having trouble using the macOS SDKs &gt;15.2, Xcode &gt;16.3, see the comment above.</p>

---
