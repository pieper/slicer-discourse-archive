# Transition of nightly build to Qt5, VTK9, CMake 3.9 and C++11

**Topic ID**: 1918
**Date**: 2018-01-24
**URL**: https://discourse.slicer.org/t/transition-of-nightly-build-to-qt5-vtk9-cmake-3-9-and-c-11/1918

---

## Post #1 by @jcfr (2018-01-24 00:32 UTC)

<p>Hi All,</p>
<p>Now that we have released Slicer 4.8.1 and also addressed a lot of issues with Qt5 and VTK9, the time has come to transition our nightly builds.</p>
<p><strong>IMPORTANT</strong>: Time the nightly builds are stabilized, you should <strong>expect  disruption and build failures</strong> until the end of next week.</p>
<h3>Transition Plan</h3>
<p>Later this week and the following one, we will:</p>
<ul>
<li>
<p>Update <a href="https://github.com/Slicer/DashboardScripts/blob/4efec4e330f4e79da9d9eef3ac445a350bde4618/overload-vs2013-slicer_release_nightly.cmake">window nightly build script</a> to use VS2015, Qt5 and VTK9</p>
</li>
<li>
<p>Add a new <a href="https://github.com/Slicer/DashboardScripts">dashboard scripts</a> to build on the more recent macOS machine:</p>
<ul>
<li>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory#factory-south.kitware">factory-south.kitware</a> running macOS 10.11.6.</li>
<li>compiler is <code>Apple LLVM version 8.0.0 (clang-800.0.42.1)</code>
</li>
<li>We will most likely target macOS 10.7 or 10.8.</li>
</ul>
</li>
<li>
<p>Disable build on the older machine <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory#factory.kitware">factory.kitware</a> that was running macOS 10.6.8.</p>
</li>
<li>
<p>Update the default values in <a href="https://github.com/Slicer/Slicer/blob/09d0f4bebc51ff3794ba4045b25faf44c52f0fa6/CMakeLists.txt">Slicer/CMakeLists.txt</a></p>
</li>
<li>
<p>Update minimum required version of CMake to 3.9.5. See <a href="https://discourse.slicer.org/t/updating-minimum-required-version-of-cmake-to-3-9-5/1873">this topic</a> for more details.</p>
</li>
</ul>
<h3>Important remarks</h3>
<ul>
<li>waiting we transition Linux build from Ubuntu 10.04 VM running on <code>factory-south.kitware</code> to docker or VM based build running on <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory#overload.kitware_and_metroplex.kitware">metroplex.kitware</a> dashboard, we will <strong>keep linux build with Qt4 and VTK7</strong>. This will happen later.</li>
</ul>

---

## Post #2 by @hjmjohnson (2018-01-24 03:05 UTC)

<p>Very Exciting!  You may want to speak with Matt McCormick regarding minimum OSX versions.  He just completed an investigation into this regarding ITK and python.</p>

---

## Post #3 by @JoostJM (2018-01-24 10:12 UTC)

<p>Very exciting indeed! With the transition to VS2015, will the python version also be changed to 3.5 or will this be done at a later date?</p>

---

## Post #4 by @lassoan (2018-01-24 13:49 UTC)

<p>Python 3 migration is planned, too. As far as I know, most or all Slicer dependencies support Python 3 already, so the switch could probably happen later this year, once Slicer is stabilized after VTK, Qt, and compiler updates.</p>

---

## Post #5 by @jcfr (2018-01-24 17:30 UTC)

<aside class="quote no-group" data-username="JoostJM" data-post="3" data-topic="1918">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/joostjm/48/1091_2.png" class="avatar"> JoostJM:</div>
<blockquote>
<p>will the python version also be changed to 3.5</p>
</blockquote>
</aside>
<p>To complement <a class="mention" href="/u/lassoan">@lassoan</a> answer, during the past few years we worked hard to update VTK and ITK to work nicely with  Python 3. Now that PythonQt also support it. The remaining part will be to update CTK and Slicer to work with Python 3.</p>
<p>If this is something important for your project and you have resources to allocate for this, do not hesitate to reach out to me.</p>

---

## Post #6 by @JoostJM (2018-01-25 08:56 UTC)

<p>No rush, more of a personal interest <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=5" title=":wink:" class="emoji" alt=":wink:"></p>

---

## Post #7 by @Davide_Punzo (2018-01-26 10:57 UTC)

<p>ok, great! waiting for the Linux transition as well <img src="https://emoji.discourse-cdn.com/twitter/yum.png?v=5" title=":yum:" class="emoji" alt=":yum:"><img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=5" title=":smile:" class="emoji" alt=":smile:"></p>

---

## Post #8 by @jcfr (2018-01-26 11:13 UTC)

<aside class="quote no-group" data-username="Davide_Punzo" data-post="7" data-topic="1918">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar"> Davide_Punzo:</div>
<blockquote>
<p>waiting for the Linux transition as well</p>
</blockquote>
</aside>
<p>That will come last but we will make sure to keep you posted of the progress.</p>
<p>xref <a href="https://github.com/Punzo/SlicerAstro/issues/72" class="inline-onebox">COMP: update gcc compiler linux kitware factory machine · Issue #72 · Punzo/SlicerAstro · GitHub</a></p>

---

## Post #9 by @jcfr (2018-01-31 02:53 UTC)

<p>Windows nightly build for Slicer application and extensions have been updated to use VS2015.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/DashboardScripts/commit/59b15e63b1571212e2262f390cc6e629447323cf">
  <header class="source">

      <a href="https://github.com/Slicer/DashboardScripts/commit/59b15e63b1571212e2262f390cc6e629447323cf" target="_blank" rel="noopener">github.com/Slicer/DashboardScripts</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/DashboardScripts/commit/59b15e63b1571212e2262f390cc6e629447323cf" target="_blank" rel="noopener">overload: Add script to build Slicer nightly app and extensions using VS2015</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2018-01-31" data-time="02:48:08" data-timezone="UTC">02:48AM - 31 Jan 18 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="changed 3 files with 280 additions and 8 deletions">
        <a href="https://github.com/Slicer/DashboardScripts/commit/59b15e63b1571212e2262f390cc6e629447323cf" target="_blank" rel="noopener">
          <span class="added">+280</span>
          <span class="removed">-8</span>
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

<p>Tomorrow, we will update the windows script to use Qt5 and VTK9 (as well as OpenGL2)</p>

---

## Post #10 by @jcfr (2018-02-01 14:17 UTC)

<p>Update:</p>
<ul>
<li>Windows build machine (named overload) has been updated two days ago but Slicer build failed because the dashboard script wasn’t setting <code>Qt5_DIR</code>. This was <strong>fixed yesterday</strong> in <a href="https://github.com/Slicer/DashboardScripts/commit/3d50b85c7659a40932d6fb75556ed710fa31b5a6">Slicer/DashboardScripts@3d50b85</a>.</li>
<li>On that same machine, StrawberryPerl was also installed yesterday to generate archives of pre-built libraries for a recent version of OpenSSL and upload them on <a href="https://github.com/Slicer/Slicer-OpenSSL" class="inline-onebox">GitHub - Slicer/Slicer-OpenSSL: OpenSSL sources and builds used in Slicer-based projects.</a>
<ul>
<li>This caused the last nightly build to fail (see below) because the <code>patch.exe</code> provided by StrawberryPerl failed to be used to patch NUMPY.</li>
<li>This <strong>was addressed</strong> by removing the extra path</li>
<li>Note  that corresponding CDash entry was removed, and nightly build was restarted.</li>
</ul>
</li>
</ul>
<p>Error that was reported on the dashboard:</p>
<pre><code class="lang-auto">Program: C:\StrawberryPerl-x64\c\bin\patch.exe

File: .\src\patch\2.5.9\patch-2.5.9-src\patch.c, Line 354
         
Expression: hunk
</code></pre>
<p>It was originally available at <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1190922" class="inline-onebox">CDash</a> but corresponding entry was deleted, and build was manually restarted.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/2036eb9718403491ba933aee18ae24c1d0312e7c.png" data-download-href="/uploads/short-url/4AYWBlsRsnkkxJugzKm43wDqwna.png?dl=1" title="Screenshot%20from%202018-02-01%2009-18-03"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/2036eb9718403491ba933aee18ae24c1d0312e7c_2_690x66.png" alt="Screenshot%20from%202018-02-01%2009-18-03" data-base62-sha1="4AYWBlsRsnkkxJugzKm43wDqwna" width="690" height="66" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/2036eb9718403491ba933aee18ae24c1d0312e7c_2_690x66.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/2036eb9718403491ba933aee18ae24c1d0312e7c_2_1035x99.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/2036eb9718403491ba933aee18ae24c1d0312e7c_2_1380x132.png 2x" data-dominant-color="B5C2C1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202018-02-01%2009-18-03</span><span class="informations">1846×177 32 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @cpinter (2018-02-01 14:47 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> Will the official Qt version be 5.10.0, or it hasn’t been fixed yet?</p>

---

## Post #12 by @jcfr (2018-02-01 15:13 UTC)

<p>Since Qt 5.10.0 addresses issues (especially with WebEngine), I think we should go with it for the current release cycle. We could then revisit after Slicer 5.0 is out.</p>

---

## Post #13 by @jcfr (2018-02-01 22:57 UTC)

<p>Updates:</p>
<ul>
<li>Starting today, Slicer packages for windows are available for download and built against Qt5 and VTK9 with OpenGL2 enabled.</li>
<li>The startup warnings related to the extension manager are already captured in <a href="https://issues.slicer.org/view.php?id=4446">https://issues.slicer.org/view.php?id=4446</a>  (assigned to <a class="mention" href="/u/jcfr">@jcfr</a>  )</li>
<li>The extra popup showing up is also captured in <a href="https://issues.slicer.org/view.php?id=4505">https://issues.slicer.org/view.php?id=4505</a> (assigned to <a class="mention" href="/u/johan_andruejol">@Johan_Andruejol</a> )</li>
<li>The issue with icon size is being worked by to <a class="mention" href="/u/johan_andruejol">@Johan_Andruejol</a>. This was captured in issue <a href="https://issues.slicer.org/view.php?id=4501">4501</a> and was addressed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26976">r26976</a>
</li>
</ul>

---

## Post #14 by @cpinter (2018-02-02 14:08 UTC)

<p>FYI the popup problem already had an issue: <a href="https://issues.slicer.org/view.php?id=4503">https://issues.slicer.org/view.php?id=4503</a></p>
<p>It’s great that the official Slicer at least for windows is now Qt5. Thanks for working on this!</p>

---

## Post #15 by @jcfr (2018-02-02 22:00 UTC)

<h3>Updates</h3>
<ul>
<li>
<p>Thanks to <a class="mention" href="/u/hina-shah">@hina-shah</a>  , Slicer issue <a href="https://issues.slicer.org/view.php?id=4503">#4503</a> is now fixed.</p>
</li>
<li>
<p>macOS:</p>
<ul>
<li>Starting today, Slicer packages for macOS will be done on <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory#factory-south.kitware">factory-south.kitware</a> using  Qt5 and VTK9 with OpenGL2 enabled.</li>
<li>Deployment target will be <code>10.9</code>, this means Slicer nightly package will <strong>NOT</strong> run on older operating system.</li>
<li>
<a href="https://github.com/jcfr/qt-easy-build">qt-easy-build scripts</a> for macOS and Linux have been updated to support building Qt 5.10.0 without rpath. (Corresponding CircleCI and TravisCI are green)</li>
</ul>
</li>
<li>
<p>windows:</p>
<ul>
<li>today’s Windows packages have successfully been built using VS2015, VTK9, Qt5 and C++11</li>
</ul>
</li>
</ul>
<h3>Next Steps</h3>
<p><em>Listed in no particular order</em></p>
<ul>
<li>Fixes for the startup warnings related to the extension manager (<a href="https://issues.slicer.org/view.php?id=4446">https://issues.slicer.org/view.php?id=4446</a>) should be integrated later today.</li>
<li>Address remaining styling issues (thanks to <a class="mention" href="/u/hjmjohnson">@hjmjohnson</a> )  and warnings</li>
<li>Update of the wiki (Note that I already have screenshot documenting the step to install Qt 5.10.0 on Windows)</li>
<li>Setup Linux build</li>
<li>Tag sources and integrate changes in project like <a href="https://github.com/Slicer/itkMGHImageIO">Slicer/itkMGHImageIO</a> (thanks to <a class="mention" href="/u/hjmjohnson">@hjmjohnson</a>)</li>
<li>Update minimum version of CMake to 3.9.5</li>
</ul>
<h3>More details</h3>
<h4>Why Qt5 needs to build without rpath on macOS ?</h4>
<p>This is required to work well with the current implementation of the packaging system.</p>
<p>The good news is that <a class="mention" href="/u/ihnorton">@ihnorton</a> is working on creating a python script that will greatly speed up the packaging process and also allow <em>repackaging</em> of Qt libraries installed using official installer.</p>
<h4>Was the build of Slicer against Qt 5.10.0 and VTK9 tested on macOS ?</h4>
<p>During the past year, a lot of people contributed to testing and stabilizing the build.</p>
<p>Last night, new dashboard scripts were added to support building on <code>factory-south-macos</code>:</p>
<ul>
<li><a href="https://github.com/Slicer/DashboardScripts/blob/master/factory-south-macos-slicer_release_nightly.cmake">factory-south-macos-slicer_release_nightly.cmake</a></li>
<li><a href="https://github.com/Slicer/DashboardScripts/blob/master/factory-south-macos-slicerextensions_release_nightly.cmake">factory-south-macos-slicerextensions_release_nightly.cmake</a></li>
</ul>
<p>Build of the Slicer application was manually started (with packaging disabled), it failed with an error related to Swig installation that should be fixed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26877">r26877</a></p>
<p>Later today, the build was manually restarted and it completed. Packaging is now in progress, and I think it will succeed. If not, that will give us the opportunity to fix problem before the nightly start.</p>

---

## Post #16 by @jcfr (2018-02-02 23:21 UTC)

<h3>Update</h3>
<ul>
<li>
<p>macOS packaging</p>
<ul>
<li>local packaging of Slicer (built with Qt5 and VTK9) completed.</li>
<li>there is one issue <a href="https://issues.slicer.org/view.php?id=4506">#4506</a> related to missing <code>libqcocoa.dylib</code> that will be addressed shortly.</li>
<li>I uploaded the corresponding installer here: <a href="https://github.com/jcfr/sandbox/releases/tag/Slicer">https://github.com/jcfr/sandbox/releases/tag/Slicer</a> Could someone try it ? <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/fedorov">@fedorov</a> <a class="mention" href="/u/ihnorton">@ihnorton</a>
</li>
</ul>
</li>
</ul>

---

## Post #17 by @pieper (2018-02-02 23:39 UTC)

<p>Alas no, it crashed on startup; log below.</p>
<p>Process:               Slicer [58842]<br>
Path:                  /private/var/folders/*/Slicer.app/Contents/MacOS/Slicer<br>
Identifier:            Slicer<br>
Version:               ???<br>
Code Type:             X86-64 (Native)<br>
Parent Process:        ??? [1]<br>
Responsible:           Slicer [58842]<br>
User ID:               501</p>
<p>Date/Time:             2018-02-02 18:34:05.285 -0500<br>
OS Version:            Mac OS X 10.13.3 (17D47)<br>
Report Version:        12<br>
Anonymous UUID:        AE9D173E-A1E8-E500-62F7-C31D0E540E6E</p>
<p>Time Awake Since Boot: 260000 seconds</p>
<p>System Integrity Protection: enabled</p>
<p>Notes:                 Translocated Process</p>
<p>Crashed Thread:        0  Dispatch queue: com.apple.main-thread</p>
<p>Exception Type:        EXC_CRASH (SIGABRT)<br>
Exception Codes:       0x0000000000000000, 0x0000000000000000<br>
Exception Note:        EXC_CORPSE_NOTIFY</p>
<p>Application Specific Information:<br>
abort() called</p>
<p>Thread 0 Crashed:: Dispatch queue: com.apple.main-thread<br>
0   libsystem_kernel.dylib        	0x00007fff6eb8ce3e __pthread_kill + 10<br>
1   libsystem_pthread.dylib       	0x00007fff6eccb150 pthread_kill + 333<br>
2   libsystem_c.dylib             	0x00007fff6eae9312 abort + 127<br>
3   org.qt-project.QtCore         	0x000000011999d9a9 0x119987000 + 92585<br>
4   org.qt-project.QtCore         	0x000000011999f239 QMessageLogger::fatal(char const*, …) const + 233<br>
5   org.qt-project.QtGui          	0x000000011949e866 QGuiApplicationPrivate::createPlatformIntegration() + 5670<br>
6   org.qt-project.QtGui          	0x000000011949e88b QGuiApplicationPrivate::createEventDispatcher() + 27<br>
7   org.qt-project.QtCore         	0x0000000119b7fbd5 QCoreApplicationPrivate::init() + 2069<br>
8   org.qt-project.QtGui          	0x000000011949a320 QGuiApplicationPrivate::init() + 64<br>
9   org.qt-project.QtWidgets      	0x0000000118ed585a QApplicationPrivate::init() + 26<br>
10  libqSlicerBaseQTCore.dylib    	0x000000010abec7f0 qSlicerCoreApplication::qSlicerCoreApplication(qSlicerCoreApplicationPrivate*, int&amp;, char**) + 32<br>
11  libqSlicerBaseQTGUI.dylib     	0x000000010a2f8188 qSlicerApplication::qSlicerApplication(int&amp;, char**) + 200<br>
12                                	0x0000000109f980f3 (anonymous namespace)::SlicerAppMain(int, char**) + 803<br>
13  libdyld.dylib                 	0x00007fff6ea3d115 start + 1</p>
<p>Also there’s no slicer icon.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c82ee83c042f4814cd20332347175e79caa81a22.png" alt="image" data-base62-sha1="syTZw7X13jIAFKJhGdgjwUCbxFE" width="597" height="128"></p>

---

## Post #18 by @pieper (2018-02-03 18:33 UTC)

<p>When I try opening from the console I get this message that indicates it’s not finding the platform library in spite of it being installed by <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26882">r26882</a>.  Odd that it says it can’t find “cocoa” but also says that “cocoa” is available.  Is it maybe the wrong version of the platform library file?</p>
<pre><code class="lang-auto">$ /Volumes/Slicer-4.9.0-2018-01-28-macosx-amd64/Slicer.app/Contents/MacOS/Slicer 
This application failed to start because it could not find or load the Qt platform plugin "cocoa"
in "".

Available platform plugins are: cocoa.

Reinstalling the application may fix this problem.
Abort trap: 6

</code></pre>

---

## Post #19 by @ihnorton (2018-02-03 19:05 UTC)

<p>There a number of RPATH problems masked behind the qt plugin loader.</p>
<pre><code class="lang-auto">Slicer.app inorton$ QT_DEBUG_PLUGINS=1 ./Contents/MacOS/Slicer
QFactoryLoader::QFactoryLoader() checking directory path "/private/tmp/Slicer.app/Contents/lib/QtPlugins/platforms" ...
QFactoryLoader::QFactoryLoader() looking at "/private/tmp/Slicer.app/Contents/lib/QtPlugins/platforms/libqcocoa.dylib"
Found metadata in lib /private/tmp/Slicer.app/Contents/lib/QtPlugins/platforms/libqcocoa.dylib, metadata=
{
    "IID": "org.qt-project.Qt.QPA.QPlatformIntegrationFactoryInterface.5.3",
    "MetaData": {
        "Keys": [
            "cocoa"
        ]
    },
    "className": "QCocoaIntegrationPlugin",
    "debug": false,
    "version": 330240
}


Got keys from plugin meta data ("cocoa")
QFactoryLoader::QFactoryLoader() checking directory path "/private/tmp/Slicer.app/Contents/MacOS/platforms" ...
Cannot load library /private/tmp/Slicer.app/Contents/lib/QtPlugins/platforms/libqcocoa.dylib: (dlopen(/private/tmp/Slicer.app/Contents/lib/QtPlugins/platforms/libqcocoa.dylib, 133): Library not loaded: /Volumes/Dashboards/Support/qt-everywhere-build-5.10.0/lib/QtGui.framework/Versions/5/QtGui
  Referenced from: /private/tmp/Slicer.app/Contents/lib/QtPlugins/platforms/libqcocoa.dylib
  Reason: image not found)
QLibraryPrivate::loadPlugin failed on "/private/tmp/Slicer.app/Contents/lib/QtPlugins/platforms/libqcocoa.dylib" : "Cannot load library /private/tmp/Slicer.app/Contents/lib/QtPlugins/platforms/libqcocoa.dylib: (dlopen(/private/tmp/Slicer.app/Contents/lib/QtPlugins/platforms/libqcocoa.dylib, 133): Library not loaded: /Volumes/Dashboards/Support/qt-everywhere-build-5.10.0/lib/QtGui.framework/Versions/5/QtGui\n  Referenced from: /private/tmp/Slicer.app/Contents/lib/QtPlugins/platforms/libqcocoa.dylib\n  Reason: image not found)"
This application failed to start because it could not find or load the Qt platform plugin "cocoa"
in "".

Available platform plugins are: cocoa.

Reinstalling the application may fix this problem.
Abort trap: 6
</code></pre>

---

## Post #20 by @jcfr (2018-02-03 19:26 UTC)

<p>Could try the latest nightly for macos. I manually fixed and triggered the<br>
upload this morning.</p>

---

## Post #21 by @pieper (2018-02-03 22:18 UTC)

<p>Looks like the package was built but couldn’t upload.  Getting closer…</p>
<p>From <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1192626">the log</a>:</p>
<pre><code class="lang-auto">CPack: - package: /Volumes/Dashboards/Nightly/Slicer-0-build/Slicer-build/Slicer-4.9.0-2018-02-02-macosx-amd64.dmg generated.

Uploading [Slicer-4.9.0-2018-02-02-macosx-amd64.dmg] on [http://slicer.kitware.com/midas3]
CMake Warning at /Volumes/Dashboards/Nightly/Slicer-0/CMake/MIDASAPILogin.cmake:69 (message):
  Failed to login to MIDAS server

    url: http://slicer.kitware.com/midas3
    email: MIDAS_PACKAGE_EMAIL-NOTDEFINED
    apikey: MIDAS_PACKAGE_API_KEY-NOTDEFINED
    response: {"stat":"fail","message":"Unable to authenticate. Please check credentials.","code":"-150"}
Call Stack (most recent call first):
  /Volumes/Dashboards/Nightly/Slicer-0/CMake/MIDASAPIUploadPackage.cmake:59 (midas_api_login)
  /Volumes/Dashboards/Nightly/Slicer-0/CMake/SlicerPackageAndUploadTarget.cmake:234 (midas_api_upload_package)


CMake Error at /Volumes/Dashboards/Nightly/Slicer-0/CMake/SlicerPackageAndUploadTarget.cmake:250 (message):
  Upload of [Slicer-4.9.0-2018-02-02-macosx-amd64.dmg] failed !

  Check that:

  (1) you have been granted permission to upload

  (2) your email and api key are correct
</code></pre>

---

## Post #22 by @jcfr (2018-02-04 01:03 UTC)

<aside class="quote no-group" data-username="pieper" data-post="21" data-topic="1918">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Looks like the package was built but couldn’t upload.  Getting closer…</p>
</blockquote>
</aside>
<p>This was <a href="https://github.com/Slicer/DashboardScripts/commit/a4b631f3e9b819dbc47acf8a4794cb33b62b8cf0">fixed</a> this morning</p>
<p>I also manually triggered the upload and the latest package can be found here: <a href="http://slicer.kitware.com/midas3/item/341826">http://slicer.kitware.com/midas3/item/341826</a>  (But for some reason, it didn’t show up on  the download  website … )</p>
<p>This package also includes a fix for the cocoa packaging. See <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26882">r26882</a></p>

---

## Post #23 by @pieper (2018-02-04 19:48 UTC)

<p>Getting even closer…  But a new issue:</p>
<pre><code class="lang-auto">$ /Volumes/Slicer-4.9.0-2018-02-03-macosx-amd64/Slicer.app/Contents/MacOS/Slicer 
Could not find QtWebEngineProcess
Abort trap: 6
</code></pre>
<pre><code class="lang-auto">Application Specific Information:
abort() called

Thread 0 Crashed:: Dispatch queue: com.apple.main-thread
0   libsystem_kernel.dylib        	0x00007fff6eb8ce3e __pthread_kill + 10
1   libsystem_pthread.dylib       	0x00007fff6eccb150 pthread_kill + 333
2   libsystem_c.dylib             	0x00007fff6eae9312 abort + 127
3   org.qt-project.QtCore         	0x000000011b8909a9 0x11b87a000 + 92585
4   org.qt-project.QtCore         	0x000000011b892239 QMessageLogger::fatal(char const*, ...) const + 233
5   org.qt-project.Qt.QtWebEngineCore	0x000000010e209b57 0x10e197000 + 469847
6   org.qt-project.Qt.QtWebEngineCore	0x000000010e2066c8 0x10e197000 + 456392
7   org.qt-project.Qt.QtWebEngineCore	0x000000010e205d7b 0x10e197000 + 454011
8   org.qt-project.Qt.QtWebEngineCore	0x000000010e1aa0c8 QtWebEngineCore::BrowserContextAdapter::BrowserContextAdapter(QString const&amp;) + 248
9   org.qt-project.QtWebEngineWidgets	0x000000010d2a493c 0x10d290000 + 84284
10  org.qt-project.QtWebEngineWidgets	0x000000010d2a4887 QWebEngineProfile::QWebEngineProfile(QString const&amp;, QObject*) + 71
11  libqSlicerBaseQTGUI.dylib     	0x000000010c386d6f qSlicerWebWidgetPrivate::init() + 111
12  libqSlicerBaseQTGUI.dylib     	0x000000010c38798a qSlicerWebWidget::qSlicerWebWidget(QWidget*) + 74
13  libqSlicerBaseQTGUI.dylib     	0x000000010c38a25f qSlicerExtensionsInstallWidget::qSlicerExtensionsInstallWidget(QWidget*) + 15
14  libqSlicerBaseQTGUI.dylib     	0x000000010c399ede Ui_qSlicerExtensionsManagerWidget::setupUi(QWidget*) + 878
15  libqSlicerBaseQTGUI.dylib     	0x000000010c399073 qSlicerExtensionsManagerWidgetPrivate::init() + 35
16  libqSlicerBaseQTGUI.dylib     	0x000000010c39aa4b qSlicerExtensionsManagerWidget::qSlicerExtensionsManagerWidget(QWidget*) + 91
17  libqSlicerBaseQTGUI.dylib     	0x000000010c397c81 Ui_qSlicerExtensionsManagerDialog::setupUi(QDialog*) + 417
18  libqSlicerBaseQTGUI.dylib     	0x000000010c397353 qSlicerExtensionsManagerDialogPrivate::init() + 35
19  libqSlicerBaseQTGUI.dylib     	0x000000010c398173 qSlicerExtensionsManagerDialog::qSlicerExtensionsManagerDialog(QWidget*) + 99
20  libqSlicerBaseQTGUI.dylib     	0x000000010c325998 qSlicerApplicationPrivate::init() + 2408
21  libqSlicerBaseQTGUI.dylib     	0x000000010c32718c qSlicerApplication::qSlicerApplication(int&amp;, char**) + 220
22                                	0x000000010bfc50f3 (anonymous namespace)::SlicerAppMain(int, char**) + 803
23  libdyld.dylib                 	0x00007fff6ea3d115 start + 1
</code></pre>

---

## Post #24 by @jcfr (2018-02-04 20:13 UTC)

<p>Great. I already addressed this for Linux. Will work on fix for macOS on Monday or sooner if<br>
possible.</p>

---

## Post #25 by @jcfr (2018-02-05 23:23 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="24" data-topic="1918">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>on fix for macOS</p>
</blockquote>
</aside>
<p>Here is a work in progress topic: <a href="https://github.com/Slicer/Slicer/compare/master...jcfr:macos-qt5-fixup-qtwebengineprocess">https://github.com/Slicer/Slicer/compare/master...jcfr:macos-qt5-fixup-qtwebengineprocess</a></p>
<p>I plan on finalizing later tonight.</p>

---

## Post #26 by @jcfr (2018-02-07 04:51 UTC)

<p>Packaging of <code>QtWebEngineProcess</code> on macOS should now be addressed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26892">r26892</a></p>
<p>Since I already disabled the regular nightly build on macOS for this evening, I will manually trigger it after:</p>
<ul>
<li>running <code>svn update</code>
</li>
<li>disabling the source updates setting env variable <a href="https://github.com/Slicer/Slicer/blob/203b10f584ec2758e1af52f8109c6e4cd1a327ee/CMake/SlicerDashboardDriverScript.cmake#L121">run_ctest_with_update</a>
</li>
<li>manually running <a href="https://github.com/Slicer/DashboardScripts/blob/a4b631f3e9b819dbc47acf8a4794cb33b62b8cf0/factory-south-macos.sh">factory-south-macos.sh</a>
</li>
</ul>
<p>Before doing so, I will have a look at <a href="https://discourse.slicer.org/t/launch-error-message-in-qt5-debug-build/2039/3">Launch error message in Qt5 debug build</a></p>

---

## Post #27 by @jcfr (2018-02-07 06:56 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="26" data-topic="1918">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Before doing so, I will have a look at Launch error message in Qt5 debug build</p>
</blockquote>
</aside>
<p>As already summarized in the corresponding topic,  <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26893">r26893</a> addresses this problem.</p>
<p>Next step will be to address the <code>FloatingPointExceptions are not supported on this platform.</code> error reported when running CLI tests.</p>

---

## Post #28 by @jcfr (2018-02-08 03:28 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="27" data-topic="1918">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Next step will be to address the FloatingPointExceptions are not supported on this platform. error reported when running CLI tests.</p>
</blockquote>
</aside>
<p>This should be fixed by <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26894">r26894</a>. Waiting the <a href="http://review.source.kitware.com/#/c/23159">topic proposed</a> to upstream ITK is integrated, <a href="https://github.com/Slicer/ITK/compare/906a0f8...Slicer:slicer-v4.13.0-2017-12-20-d92873e">changes specific</a> to the Slicer fork of ITK were pushed.</p>

---

## Post #29 by @pieper (2018-02-08 14:23 UTC)

<p>Mac nightly is working today <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=5" title=":+1:" class="emoji" alt=":+1:"></p>

---
