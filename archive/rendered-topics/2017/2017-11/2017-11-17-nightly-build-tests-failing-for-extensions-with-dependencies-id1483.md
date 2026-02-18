# Nightly build TESTS failing for extensions with dependencies to other scriptable modules

**Topic ID**: 1483
**Date**: 2017-11-17
**URL**: https://discourse.slicer.org/t/nightly-build-tests-failing-for-extensions-with-dependencies-to-other-scriptable-modules/1483

---

## Post #1 by @che85 (2017-11-17 19:45 UTC)

<p>Hi there,</p>
<p>today I noticed that (for a long time) our extension tests has been failing (generic, but also our custom tests)</p>
<p>e.g. <a href="http://slicer.cdash.org/testDetails.php?test=8407693&amp;build=1124707" rel="nofollow noopener">http://slicer.cdash.org/testDetails.php?test=8407693&amp;build=1124707</a></p>
<p>Our mpReview extension has a dependency to ‘SlicerDevelopmentToolbox’</p>
<p>As you will notice, there are no dependencies loaded as additional-module-paths in the following cli command:</p>
<pre><code>   /Users/kitware/Dashboards/Nightly/Slicer-0-build/Slicer-build/Slicer \"--no-splash\" \"--testing\" 
\"--launcher-additional-settings\" \"/Users/kitware/Dashboards/Nightly/S-0-E-b/mpReview-build/AdditionalLauncherSettings.ini\" 
\"--no-main-window\" \"--disable-cli-modules\" \"--additional-module-path\" 
\"/Users/kitware/Dashboards/Nightly/S-0-E-b/mpReview-build/lib/Slicer-4.9/qt-scripted-modules\" 
\"--additional-module-paths\" \"/Users/kitware/Dashboards/Nightly/S-0-E-b/mpReview-build/lib/Slicer-4.9/qt-scripted-modules\" 
\"/Users/kitware/Dashboards/Nightly/S-0-E-b/mpReview-build/lib/Slicer-4.9/cli-modules\" 
\"/Users/kitware/Dashboards/Nightly/S-0-E-b/mpReview-build/\" 
\"--python-code\" \"import slicer.testing; slicer.testing.runUnitTest([\'/Users/kitware/Dashboards/Nightly/S-0-E-b/mpReview-build\', 
\'/Users/kitware/Dashboards/Nightly/S-0-E-b/mpReview\'], \'qSlicermpReviewModuleGenericTest\')\"
</code></pre>
<p>Solution:<br>
Slicer nightly tests just needs to have those additional dependencies loaded for running tests. Otherwise this doesn’t mirror the real world where I need to install an extension from the ExtensionManager where the downloaded extensions (dependencies) automatically get added to the Slicer “Additional module paths”. And after restarting the extension (optimally) works like a charm!</p>
<p>Hope we can find a simple and quick solution for that.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2017-11-17 20:32 UTC)

<p>Does your additional launcher settings file contain all the necessary paths?</p>

---

## Post #3 by @che85 (2017-11-17 20:48 UTC)

<p>SlicerDevelopmentToolbox is definitely missing. When building an extension, would this file automatically get extended by the missing dependencies? That’s what I would expect.</p>
<p>The AdditionalLauncherSettings.ini of my local mpReview build looks like the following:</p>
<pre><code>[General]
additionalPathVariables=PYTHONPATH

[LibraryPaths]
1\path=/Users/christian/sources/py/mpReview/Build/lib/Slicer-4.7/cli-modules/.
2\path=/Users/christian/sources/py/mpReview/Build/lib/Slicer-4.7/qt-loadable-modules/.
size=2

[Paths]
1\path=/Users/christian/sources/py/mpReview/Build/lib/Slicer-4.7/cli-modules/.
2\path=/Users/christian/sources/py/mpReview/Build/bin/.
size=2

[EnvironmentVariables]

[PYTHONPATH]
1\path=/Users/christian/sources/py/mpReview/Build/lib/Slicer-4.7/qt-scripted-modules
2\path=/Users/christian/sources/py/mpReview/Build/lib/Slicer-4.7/qt-loadable-modules/.
3\path=/Users/christian/sources/py/mpReview/Build/lib/Slicer-4.7/qt-loadable-modules/Python
size=3</code></pre>

---

## Post #4 by @cpinter (2017-11-17 20:51 UTC)

<p>For reference I added a Mantis issue about the same thing<br>
<a href="https://issues.slicer.org/view.php?id=4472" class="onebox" target="_blank">https://issues.slicer.org/view.php?id=4472</a><br>
I haven’t figured it out yet either.</p>

---

## Post #5 by @che85 (2017-11-17 20:53 UTC)

<p>Oh yeah. When building an extension which depends on other extensions I would assume the AdditionalLauncherSettings.ini to be extended by the dependencies, which probably would fix that issue.</p>

---

## Post #6 by @cpinter (2017-11-17 20:57 UTC)

<p>In my case the extension GelDosimetryAnalysis depends on SlicerRT. The problem locally is that the SlicerRT_DIR CMake variable is not set. Instead it gives me this</p>
<details>
<summary>
CMake warning message</summary>
<p>CMake Warning at C:/d/Slicer4/Extensions/CMake/SlicerBlockAdditionalLauncherSettings.cmake:48 (MESSAGE):<br>
Dependent extension SlicerRT cannot be found by CMake find_package(),<br>
therefore paths variables cannot be imported from this extension.  The<br>
problem can be resolved by generating SlicerRTConfig.cmake by adding<br>
include(${Slicer_EXTENSION_GENERATE_CONFIG}) to the top-level<br>
CMakeLists.txt of the dependent exension.<br>
Call Stack (most recent call first):<br>
C:/d/S4R/Slicer-build/UseSlicer.cmake:281 (include)<br>
CMakeLists.txt:24 (include)</p>
</details>
<p>However include(${Slicer_EXTENSION_GENERATE_CONFIG}) is in the top-level CMakeLists, and SlicerRT does generate a SlicerRTConfig.cmake.</p>
<p>If I define SlicerRT_DIR manually, then it works nicely. It’s not done on the factory unfortunately, and this is where I am stuck now. We have a factory machine and was going to take a look at the issue on it, but I haven’t gotten to that point yet.</p>

---

## Post #7 by @che85 (2017-11-17 21:00 UTC)

<p>There is also something wrong here. The attribute name is not split into three depending extensions</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db1fa2c460acb7fd6656f253d7ac2b3835322d58.png" data-download-href="/uploads/short-url/vgslpRbKIoMydujuqXtLokWHGyI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db1fa2c460acb7fd6656f253d7ac2b3835322d58_2_690x97.png" alt="image" data-base62-sha1="vgslpRbKIoMydujuqXtLokWHGyI" width="690" height="97" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db1fa2c460acb7fd6656f253d7ac2b3835322d58_2_690x97.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db1fa2c460acb7fd6656f253d7ac2b3835322d58_2_1035x145.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db1fa2c460acb7fd6656f253d7ac2b3835322d58_2_1380x194.png 2x" data-dominant-color="EED7D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3104×440 68.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @che85 (2017-11-17 21:12 UTC)

<p>Having more than one dependency was causing issues since I didn’t add those dependencies correctly within the CMakeLists.txt.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee5cfe909fdc9f1159cfd8cf0517761f5916bbb6.png" data-download-href="/uploads/short-url/y0ESpfOTpm0Je435sqUB4mZgVAa.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee5cfe909fdc9f1159cfd8cf0517761f5916bbb6_2_690x125.png" alt="image" data-base62-sha1="y0ESpfOTpm0Je435sqUB4mZgVAa" width="690" height="125" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee5cfe909fdc9f1159cfd8cf0517761f5916bbb6_2_690x125.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee5cfe909fdc9f1159cfd8cf0517761f5916bbb6_2_1035x187.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee5cfe909fdc9f1159cfd8cf0517761f5916bbb6_2_1380x250.png 2x" data-dominant-color="F06060"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2114×386 79.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The following at leasts splits the dependencies into separate CMake attributes</p>
<pre><code>set(EXTENSION_DEPENDS SlicerDevelopmentToolbox DCMQI PETDICOMExtension)
</code></pre>
<p>instead of</p>
<pre><code>set(EXTENSION_DEPENDS "SlicerDevelopmentToolbox DCMQI PETDICOMExtension")
</code></pre>
<p>My mistake. But it still doesn’t resolve the dependencies. Not sure where find_package() is looking</p>

---

## Post #9 by @cpinter (2017-11-17 21:15 UTC)

<p>Yep <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> I reported the same thing to <a class="mention" href="/u/jcfr">@jcfr</a> but haven’t added a Mantis issue for this one. See screenshot</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f0adb3426b259a70c2b4baee152ece4d68eaaca.png" data-download-href="/uploads/short-url/294q8elfk6Xbs0xrl3hBW8civ4C.png?dl=1" title="20171027_MultipleExtensionDependencies"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f0adb3426b259a70c2b4baee152ece4d68eaaca_2_690x399.png" alt="20171027_MultipleExtensionDependencies" data-base62-sha1="294q8elfk6Xbs0xrl3hBW8civ4C" width="690" height="399" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f0adb3426b259a70c2b4baee152ece4d68eaaca_2_690x399.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f0adb3426b259a70c2b4baee152ece4d68eaaca_2_1035x598.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f0adb3426b259a70c2b4baee152ece4d68eaaca_2_1380x798.png 2x" data-dominant-color="ECECEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20171027_MultipleExtensionDependencies</span><span class="informations">1689×978 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @cpinter (2017-11-17 21:16 UTC)

<p>Oh so if you don’t put them between quotation marks then it works? Thanks!!</p>

---

## Post #11 by @che85 (2017-11-17 21:20 UTC)

<p>Don’t put it in quotation marks or separate it with semicolon:</p>
<p>Both work for me:</p>
<pre><code>set(EXTENSION_DEPENDS dependency1 dependency2 dependency3)

set(EXTENSION_DEPENDS "dependency1;dependency2;dependency3")</code></pre>

---

## Post #12 by @cpinter (2017-11-17 21:23 UTC)

<p>Right. The <a href="https://github.com/Slicer/Slicer/blob/836639490e2257a2ba485b440ba05d850f14736a/Utilities/Templates/Extensions/SuperBuild/CMakeLists.txt#L13">template</a> mentions the space separation, so that was fine. However the example “NA” is within quotes, and that made me put them between quotes. Maybe if we remove the quotes from the template or explain this in the same comment, then it’s less error-prone.</p>

---

## Post #13 by @lassoan (2017-11-17 22:01 UTC)

<p>Additional directories are collected recursively from all extensions that your extension depends on, and added to the additional launcher settings. Does it work until this point?</p>

---

## Post #14 by @cpinter (2017-11-17 22:12 UTC)

<p>Without manually specifying SlicerRT_DIR in the GelDosimetryAnalysis CMake, it is not found, see explanation in earlier <a href="https://discourse.slicer.org/t/nightly-build-tests-failing-for-extensions-with-dependencies-to-other-scriptable-modules/1483/6?u=cpinter">comment</a></p>

---

## Post #15 by @lassoan (2017-11-18 02:21 UTC)

<p>Adding of _DIR for all required extensions is implemented in SlicerBlockBuildPackageAndUploadExtensions.cmake:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/4edfa38fe94abf5b8c88ea336682e55efbf906a6/Extensions/CMake/SlicerBlockBuildPackageAndUploadExtensions.cmake#L103" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/4edfa38fe94abf5b8c88ea336682e55efbf906a6/Extensions/CMake/SlicerBlockBuildPackageAndUploadExtensions.cmake#L103" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/4edfa38fe94abf5b8c88ea336682e55efbf906a6/Extensions/CMake/SlicerBlockBuildPackageAndUploadExtensions.cmake#L103</a></h4>
<pre class="onebox"><code class="lang-cmake"><ol class="start lines" start="93" style="counter-reset: li-counter 92 ;">
<li>set(EXTENSION_ICONURL ${EXTENSION_EXT_ICONURL})</li>
<li>set(EXTENSION_CONTRIBUTORS ${EXTENSION_EXT_CONTRIBUTORS})</li>
<li>set(EXTENSION_DESCRIPTION ${EXTENSION_EXT_DESCRIPTION})</li>
<li>set(EXTENSION_HOMEPAGE ${EXTENSION_EXT_HOMEPAGE})</li>
<li>set(EXTENSION_SCREENSHOTURLS ${EXTENSION_EXT_SCREENSHOTURLS})</li>
<li>set(EXTENSION_ENABLED ${EXTENSION_EXT_ENABLED})</li>
<li>set(EXTENSION_DEPENDS ${EXTENSION_EXT_DEPENDS})</li>
<li>
</li>
<li># Ensure extensions depending on this extension can lookup the corresponding</li>
<li># _DIR and _BUILD_SUBDIRECTORY variables.</li>
<li class="selected">set(${EXTENSION_NAME}_BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR}/${EXTENSION_NAME}-build)</li>
<li>set(${EXTENSION_NAME}_BUILD_SUBDIRECTORY ${EXTENSION_EXT_BUILD_SUBDIRECTORY})</li>
<li>
</li>
<li>message(STATUS "Configuring extension: ${EXTENSION_NAME}")</li>
<li>if("${EXTENSION_EXT_SCM}" STREQUAL "" AND "${EXTENSION_EXT_SCMURL}" STREQUAL "")</li>
<li>  message(WARNING "Failed to extract extension information associated to file: ${file}")</li>
<li>  continue()</li>
<li>endif()</li>
<li>
</li>
<li># Set convenience variable</li>
<li>set(proj ${EXTENSION_NAME})</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Maybe you could add a couple of MESSAGE prints in this file to see where things go wrong. If everything looks fine then you can go one step further and check if the generated CMake cache file content is correct (contains _DIR and the value is correct). If not, you can add some MESSAGE prints here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/4edfa38fe94abf5b8c88ea336682e55efbf906a6/Extensions/CMake/SlicerBlockBuildPackageAndUploadExtension.cmake#L159-L164" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/4edfa38fe94abf5b8c88ea336682e55efbf906a6/Extensions/CMake/SlicerBlockBuildPackageAndUploadExtension.cmake#L159-L164" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/4edfa38fe94abf5b8c88ea336682e55efbf906a6/Extensions/CMake/SlicerBlockBuildPackageAndUploadExtension.cmake#L159-L164</a></h4>
<pre class="onebox"><code class="lang-cmake"><ol class="start lines" start="159" style="counter-reset: li-counter 158 ;">
<li>foreach(dep ${EXTENSION_DEPENDS})</li>
<li>set(cmakecache_content "${cmakecache_content}</li>
<li>${dep}_BINARY_DIR:PATH=${${dep}_BINARY_DIR}</li>
<li>${dep}_BUILD_SUBDIRECTORY:STRING=${${dep}_BUILD_SUBDIRECTORY}</li>
<li>${dep}_DIR:PATH=${${dep}_BINARY_DIR}/${${dep}_BUILD_SUBDIRECTORY}")</li>
<li>endforeach()</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #16 by @jcfr (2017-11-18 19:16 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="6" data-topic="1483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>If I define SlicerRT_DIR manually, then it works nicely. It’s not done on the factory unfortunately, and this is where I am stuck now. We have a factory machine and was going to take a look at the issue on it, but I haven’t gotten to that point yet.</p>
</blockquote>
</aside>
<p>As mentioned in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#Can_an_extension_depend_on_other_extensions_.3F">Developer FAQ / Extensions / Can an extension depend on other extensions ?</a>, the build system should build extensions with the expected <code>&lt;ExtensionName&gt;_DIR</code> variables.</p>
<p>This is implemented here:</p>
<p><a href="https://github.com/Slicer/Slicer/blob/4edfa38fe94abf5b8c88ea336682e55efbf906a6/Extensions/CMake/SlicerBlockUploadExtension.cmake#L100-L105" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/4edfa38fe94abf5b8c88ea336682e55efbf906a6/Extensions/CMake/SlicerBlockUploadExtension.cmake#L100-L105</a></p>
<p>and here:</p>
<p><a href="https://github.com/Slicer/Slicer/blob/4edfa38fe94abf5b8c88ea336682e55efbf906a6/Extensions/CMake/SlicerBlockBuildPackageAndUploadExtension.cmake#L159-L164" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/4edfa38fe94abf5b8c88ea336682e55efbf906a6/Extensions/CMake/SlicerBlockBuildPackageAndUploadExtension.cmake#L159-L164</a></p>
<blockquote>
<p>mpReview extension has a dependency to ‘SlicerDevelopmentToolbox’</p>
</blockquote>
<p>Looking at the <a href="https://github.com/Slicer/ExtensionsIndex/blob/55645f9f4b67495b6cd326545943e5af7eaf28ab/mpReview.s4ext#L15">description file</a> confirms that.</p>
<blockquote>
<p>GelDosimetry dependencies - See <a href="https://issues.slicer.org/view.php?id=4472" class="inline-onebox">Automatic test for extension cannot find dependency on factory · Issue #4472 · Slicer/Slicer · GitHub</a></p>
</blockquote>
<p>As we can see in the <a href="https://github.com/SlicerRt/GelDosimetryAnalysis/blob/b2ee130bd93e766822eed4371219877184ea9847/CMakeLists.txt#L19">CMakeLists.txt</a>, the dependency is specified as <code>SlicerRT</code></p>
<p>But looking at the <code>CMakeCache.txt</code> of both extension, the path is not properly set:</p>
<pre><code class="lang-auto">kitware@factory-south-ubuntu:~/Dashboards/Nightly/S-0-E-b/mpReview-build$ cat CMakeCache.txt | grep SlicerDevelopmentToolbox_DIR
SlicerDevelopmentToolbox_DIR:PATH=SlicerDevelopmentToolbox_DIR-NOTFOUND
</code></pre>
<pre><code class="lang-auto">kitware@factory-south-ubuntu:~/Dashboards/Nightly/S-0-E-b/GelDosimetryAnalysis-build$ cat CMakeCache.txt | grep SlicerRT_DIR
SlicerRT_DIR:PATH=SlicerRT_DIR-NOTFOUND
</code></pre>
<p>There is definitively a problem.</p>

---

## Post #17 by @jcfr (2017-11-18 20:01 UTC)

<p>Also worth noting that the current test check that <code>_DIR</code> variables are effectively set:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/63218815d127d2828e4806f43cc3a50163a0c6c5/Extensions/CMake/Testing/SlicerExtensionBuildSystemTest.py#L547-L575" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/63218815d127d2828e4806f43cc3a50163a0c6c5/Extensions/CMake/Testing/SlicerExtensionBuildSystemTest.py#L547-L575" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/63218815d127d2828e4806f43cc3a50163a0c6c5/Extensions/CMake/Testing/SlicerExtensionBuildSystemTest.py#L547-L575</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="547" style="counter-reset: li-counter 546 ;">
<li>def _check_caches(self, test_binary_dir):</li>
<li>
</li>
<li>  # Check extension caches</li>
<li>  for extensionName in ['TestExtA', 'TestExtB', 'TestExtC']:</li>
<li>
</li>
<li>    # Read cache</li>
<li>    varname = '%s_BUILD_SLICER_EXTENSION' % extensionName</li>
<li>    cmakecache = test_binary_dir + '/' + extensionName + '-build/CMakeCache.txt'</li>
<li>    cache_values = get_cmakecache_values(cmakecache, [varname])</li>
<li>
</li>
<li>    # Check &lt;ExtensionName&gt;_BUILD_SLICER_EXTENSION variable</li>
<li>    self.assertIn(cache_values[varname], ['1', 'ON', 'TRUE'])</li>
<li>
</li>
<li>  # Read TestExtC cache</li>
<li>  cmakecache = test_binary_dir + '/TestExtC-build/CMakeCache.txt'</li>
<li>  cache_values = get_cmakecache_values(cmakecache, [</li>
<li>    'EXTENSION_DEPENDS',</li>
<li>    'TestExtA_DIR',</li>
<li>    'TestExtB_DIR',</li>
<li>    ])</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/63218815d127d2828e4806f43cc3a50163a0c6c5/Extensions/CMake/Testing/SlicerExtensionBuildSystemTest.py#L547-L575" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #18 by @jcfr (2017-11-18 20:36 UTC)

<p>The issue are the following:</p>
<ul>
<li>
<p>For <code>SlicerRT</code>, the config file is located in the top-level directory but the extension  build system set <code>SlicerRT_DIR</code>  using</p>
<pre><code class="lang-auto">${dep}_DIR:PATH=${${dep}_BINARY_DIR}/${${dep}_BUILD_SUBDIRECTORY}")
</code></pre>
<p>This means the call to <code>find_package(SlicerRT)</code> fails because it can’t find a config file and reset the variable <code>SlicerRT_DIR</code></p>
</li>
<li>
<p>For <code>SlicerDevelopmentToolbox</code>, there is no <code>SlicerDevelopmentToolboxConfig.cmake</code> file and as <a class="mention" href="/u/lassoan">@lassoan</a> suggested, it can easily be fixed adding  <code>include(${Slicer_EXTENSION_GENERATE_CONFIG})</code> in <a href="https://github.com/fbudin69500/SlicerDeveloperToolsForExtensions/blob/5ceceabbb3ae35a669309389aa34e596699ca058/CMakeLists.txt#L26">https://github.com/fbudin69500/SlicerDeveloperToolsForExtensions/blob/5ceceabbb3ae35a669309389aa34e596699ca058/CMakeLists.txt#L26</a></p>
</li>
</ul>

---

## Post #19 by @lassoan (2017-11-19 00:25 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="18" data-topic="1483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>This means the call to find_package(SlicerRT) fails because it can’t find a config file and reset the variable SlicerRT_DIR</p>
</blockquote>
</aside>
<p>I’ve fixed this already earlier today (<a href="https://github.com/Slicer/Slicer/commit/9d4634fada0d428e698de7c4a68d43db25d242ef">https://github.com/Slicer/Slicer/commit/9d4634fada0d428e698de7c4a68d43db25d242ef</a>).</p>

---

## Post #20 by @lassoan (2017-11-19 00:35 UTC)

<p>Also pushed a fix to SlicerRT (<a href="https://github.com/SlicerRt/SlicerRT/commit/eb5995488eeddcc9fb1a6be789dc63ac0e2448fa">https://github.com/SlicerRt/SlicerRT/commit/eb5995488eeddcc9fb1a6be789dc63ac0e2448fa</a>). SlicerRTConfig.cmake was generated too early (before any modules were configured), so no module paths were added to SlicerRT’s AdditionalLauncherSettings.ini file.</p>

---

## Post #21 by @cpinter (2017-11-19 00:56 UTC)

<p>Thanks for the fix, Andras!</p>

---

## Post #22 by @che85 (2017-11-19 19:52 UTC)

<p>Seems like mpReviews CMake can now find SlicerDevelopmentToobox, after I added the line yesterday, but the tests are still failing</p>
<p><a href="http://slicer.cdash.org/testDetails.php?test=8435164&amp;build=1133229" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/testDetails.php?test=8435164&amp;build=1133229</a></p>
<pre><code>When loading module  "mpReview" , the dependency "SlicerDevelopmentToolbox" failed to be loaded.</code></pre>

---

## Post #23 by @jcfr (2017-11-19 22:44 UTC)

<aside class="quote no-group" data-username="che85" data-post="22" data-topic="1483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/che85/48/636_2.png" class="avatar"> che85:</div>
<blockquote>
<p>after I added the line yesterday, but the tests are still failing</p>
</blockquote>
</aside>
<p>Look like the edit you are mentioning are not yet integrated: <a href="https://github.com/fbudin69500/SlicerDeveloperToolsForExtensions/blob/master/CMakeLists.txt" class="inline-onebox">SlicerDeveloperToolsForExtensions/CMakeLists.txt at master · Slicer/SlicerDeveloperToolsForExtensions · GitHub</a></p>
<p>i suggest you submit a PR against SlicerDeveloperToolsForExtensions and then update the Extension index.</p>

---

## Post #24 by @che85 (2017-11-19 23:03 UTC)

<p>I was not talking about the repository that you were mentioning. I am talking about SlicerDevelopmentToolbox and not about SlicerDeveloperToolsForExtensions</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/QIICR/SlicerDevelopmentToolbox">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/QIICR/SlicerDevelopmentToolbox" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/b946b6a7e5e5b048a3cd945ccd8d32a4bc2ae0e59b407973b4157a7bbeac957d/QIICR/SlicerDevelopmentToolbox" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/QIICR/SlicerDevelopmentToolbox" target="_blank" rel="noopener nofollow ugc">GitHub - QIICR/SlicerDevelopmentToolbox: API for 3D Slicer extension...</a></h3>

  <p>API for 3D Slicer extension development providing widgets, mixins, helpers, decorators etc. - GitHub - QIICR/SlicerDevelopmentToolbox: API for 3D Slicer extension development providing widgets, mix...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #25 by @jcfr (2017-11-20 02:05 UTC)

<p>Sorry for the confusion.</p>
<p>Good new is that the additional settings contain the dependent extension paths.</p>
<p>That said, we still need to investigate the remaining issues.</p>
<pre><code class="lang-auto">kitware@factory-south-ubuntu:~/Dashboards/Nightly/S-0-E-b/mpReview-build$ cat AdditionalLauncherSettings.ini
[General]
additionalPathVariables=PYTHONPATH

[LibraryPaths]
1\path=/home/kitware/Dashboards/Nightly/S-0-E-b/mpReview-build/lib/Slicer-4.9/cli-modules/.
2\path=/home/kitware/Dashboards/Nightly/S-0-E-b/mpReview-build/lib/Slicer-4.9/qt-loadable-modules/.
3\path=/home/kitware/Dashboards/Nightly/S-0-E-b/SlicerDevelopmentToolbox-build/lib/Slicer-4.9/cli-modules/.
4\path=/home/kitware/Dashboards/Nightly/S-0-E-b/SlicerDevelopmentToolbox-build/lib/Slicer-4.9/qt-loadable-modules/.
size=4

[Paths]
1\path=/home/kitware/Dashboards/Nightly/S-0-E-b/mpReview-build/lib/Slicer-4.9/cli-modules/.
2\path=/home/kitware/Dashboards/Nightly/S-0-E-b/mpReview-build/bin/.
3\path=/home/kitware/Dashboards/Nightly/S-0-E-b/SlicerDevelopmentToolbox-build/lib/Slicer-4.9/cli-modules/.
4\path=/home/kitware/Dashboards/Nightly/S-0-E-b/SlicerDevelopmentToolbox-build/bin/.
size=4

[EnvironmentVariables]




[PYTHONPATH]
1\path=/home/kitware/Dashboards/Nightly/S-0-E-b/mpReview-build/lib/Slicer-4.9/qt-scripted-modules
2\path=/home/kitware/Dashboards/Nightly/S-0-E-b/mpReview-build/lib/Slicer-4.9/qt-loadable-modules/.
3\path=/home/kitware/Dashboards/Nightly/S-0-E-b/mpReview-build/lib/Slicer-4.9/qt-loadable-modules/Python
4\path=/home/kitware/Dashboards/Nightly/S-0-E-b/SlicerDevelopmentToolbox-build/lib/Slicer-4.9/qt-scripted-modules
5\path=/home/kitware/Dashboards/Nightly/S-0-E-b/SlicerDevelopmentToolbox-build/lib/Slicer-4.9/qt-loadable-modules/.
6\path=/home/kitware/Dashboards/Nightly/S-0-E-b/SlicerDevelopmentToolbox-build/lib/Slicer-4.9/qt-loadable-modules/Python
size=6
</code></pre>

---

## Post #26 by @che85 (2017-11-20 05:36 UTC)

<p>Is there a specific order in which the paths are loaded into Slicer from the AdditionalLauncherSettings.ini?</p>
<p>If it’s loaded in the same order, then the missing dependency makes sense to me since mpReview is would be loaded first.</p>

---

## Post #27 by @lassoan (2017-11-20 17:51 UTC)

<p>Order of module class instantiation is random. Order of module widget and logic creation is based on the order determined from module dependencies.</p>

---

## Post #28 by @jcfr (2017-11-20 18:04 UTC)

<p>And to clarify, currently the “GenericTest” are executed without loading any dependencies are expected to pass independently of this.</p>

---

## Post #29 by @che85 (2017-11-20 18:14 UTC)

<p>How can it pass the generic tests without dependencies to be loaded? I an extension depends on other extensions, it won’t be available in slicer.modules unless the dependencies are available, right?</p>

---

## Post #30 by @che85 (2017-11-21 15:23 UTC)

<p>I just tried to join the weekly developer hangout but there was no response.</p>
<p>Is there any progress regarding this issue? Looking at today’s dashboard [1] all Tests are failing.</p>
<p>[1] <a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;display=project&amp;filtercombine=and&amp;filtercombine=and&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercount=4&amp;showfilters=1&amp;filtercombine=or&amp;field1=buildname&amp;compare1=63&amp;value1=SliceTracker&amp;field2=buildname&amp;compare2=63&amp;value2=SlicerDevelopmentToolbox&amp;field3=buildname&amp;compare3=63&amp;value3=mpReview&amp;field4=buildname&amp;compare4=63&amp;value4=QuantitativeReporting" rel="nofollow noopener">http://slicer.cdash.org/index.php?project=Slicer4&amp;display=project&amp;filtercombine=and&amp;filtercombine=and&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercount=4&amp;showfilters=1&amp;filtercombine=or&amp;field1=buildname&amp;compare1=63&amp;value1=SliceTracker&amp;field2=buildname&amp;compare2=63&amp;value2=SlicerDevelopmentToolbox&amp;field3=buildname&amp;compare3=63&amp;value3=mpReview&amp;field4=buildname&amp;compare4=63&amp;value4=QuantitativeReporting</a></p>

---

## Post #31 by @pieper (2017-11-21 15:50 UTC)

<p>Today is a project week discussion during the developer hangout.  It’s going on now but the topics aren’t currently addressing development (more about coordinating projects).</p>
<p><a href="https://meet.google.com/wzh-syuy-otj" class="onebox" target="_blank">https://meet.google.com/wzh-syuy-otj</a></p>

---

## Post #32 by @cpinter (2017-11-21 16:04 UTC)

<p>The single dependency issue seems to have been resolved. I still have failing tests, but it’s not because of dependencies (see GelDosimetry).<br>
Multiple dependencies still don’t work (see SegmentRegistration - interestingly the passing tests are the real failures).<br>
Here’s the <a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;display=project&amp;filtercombine=and&amp;filtercombine=and&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercount=4&amp;showfilters=1&amp;filtercombine=or&amp;field1=label&amp;compare1=63&amp;value1=SlicerRT&amp;field2=label&amp;compare2=63&amp;value2=GelDosimetry&amp;field3=label&amp;compare3=63&amp;value3=FilmDosimetry&amp;field4=label&amp;compare4=63&amp;value4=SegmentRegistration">filtered dashboard</a>.</p>

---

## Post #33 by @cpinter (2017-11-21 16:22 UTC)

<p>(Hang on, I didn’t commit the stripped quotes from around the extension dependencies)</p>

---

## Post #34 by @cpinter (2017-11-22 13:58 UTC)

<p>Update: Same thing after applying the fix</p>

---

## Post #35 by @che85 (2017-11-22 15:55 UTC)

<p>Is there a way to simulate the build server locally on my system, so that I can just test that locally? Making some tiny changes and waiting 24hours to it failing again doesn’t sound very productive <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=5" title=":wink:" class="emoji" alt=":wink:"></p>

---

## Post #36 by @lassoan (2017-11-22 16:16 UTC)

<p>Yes. It’s very simple to set up extension build on your computer. See instructions here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_ExtensionsIndex">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_ExtensionsIndex</a></p>

---

## Post #37 by @che85 (2017-11-22 19:45 UTC)

<p>Ok same thing is happening when I run the extension build locally. (see <a href="http://slicer.cdash.org/testDetails.php?test=8443330&amp;build=1135723" rel="nofollow noopener">http://slicer.cdash.org/testDetails.php?test=8443330&amp;build=1135723</a>)</p>

---

## Post #38 by @cpinter (2017-11-22 20:02 UTC)

<p>I managed to run the tests with multiple dependencies by adding the dependencies to the tests, see</p><aside class="onebox githubcommit" data-onebox-src="https://github.com/SlicerRt/SegmentRegistration/commit/a6a710d44faaf0dc5761eec4680755fb10672906">
  <header class="source">

      <a href="https://github.com/SlicerRt/SegmentRegistration/commit/a6a710d44faaf0dc5761eec4680755fb10672906" target="_blank" rel="noopener">github.com/SlicerRt/SegmentRegistration</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerRt/SegmentRegistration/commit/a6a710d44faaf0dc5761eec4680755fb10672906" target="_blank" rel="noopener">BUG: Added dependent module paths to tests</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2017-11-22" data-time="14:43:10" data-timezone="UTC">02:43PM - 22 Nov 17 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/cpinter" target="_blank" rel="noopener">
          <img alt="cpinter" src="https://avatars.githubusercontent.com/u/1325980?v=4" class="onebox-avatar-inline" width="20" height="20">
          cpinter
        </a>
      </div>

      <div class="lines" title="changed 3 files with 39 additions and 6 deletions">
        <a href="https://github.com/SlicerRt/SegmentRegistration/commit/a6a710d44faaf0dc5761eec4680755fb10672906" target="_blank" rel="noopener">
          <span class="added">+39</span>
          <span class="removed">-6</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The test now run and pass locally (except for the generic tests which have been <span class="show-more-container"><a href="https://github.com/SlicerRt/SegmentRegistration/commit/a6a710d44faaf0dc5761eec4680755fb10672906" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">disabled), so there is a chance they will work on the factory as well</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
and</p><aside class="onebox githubcommit" data-onebox-src="https://github.com/SlicerRt/SegmentRegistration/commit/08716b9e69a9ad2915d5a0c55001ebdfab890ab8">
  <header class="source">

      <a href="https://github.com/SlicerRt/SegmentRegistration/commit/08716b9e69a9ad2915d5a0c55001ebdfab890ab8" target="_blank" rel="noopener">github.com/SlicerRt/SegmentRegistration</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerRt/SegmentRegistration/commit/08716b9e69a9ad2915d5a0c55001ebdfab890ab8" target="_blank" rel="noopener">BUG: Added SlicerProstate dependency CLI path for Mac and Linux</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2017-11-22" data-time="20:03:18" data-timezone="UTC">08:03PM - 22 Nov 17 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/cpinter" target="_blank" rel="noopener">
          <img alt="cpinter" src="https://avatars.githubusercontent.com/u/1325980?v=4" class="onebox-avatar-inline" width="20" height="20">
          cpinter
        </a>
      </div>

      <div class="lines" title="changed 1 files with 1 additions and 0 deletions">
        <a href="https://github.com/SlicerRt/SegmentRegistration/commit/08716b9e69a9ad2915d5a0c55001ebdfab890ab8" target="_blank" rel="noopener">
          <span class="added">+1</span>
          <span class="removed">-0</span>
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

<p>If the Xyz_DIR variables are correctly set (you can check it on your local factory build), then the tests should run if you add these too.</p>

---

## Post #39 by @lassoan (2017-11-22 20:17 UTC)

<aside class="quote no-group" data-username="che85" data-post="37" data-topic="1483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/che85/48/636_2.png" class="avatar"> che85:</div>
<blockquote>
<p>Ok same thing is happening when I run the extension build locally</p>
</blockquote>
</aside>
<p>This error</p>
<pre><code>/Users/christian/sources/cpp/Builds/Slicer/Release/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/./libvtkSlicerMarkupsModuleMRMLDisplayableManagerPythonD.dylib: malformed mach-o: load commands size (32840) &gt; 32768
</code></pre>
<p>seems to be due to the limit on total size of all the load commands in the dynamic library in the MacOS loader.</p>
<p>I guess using a shorter build directory path would solve the issue. For example, instead of <code>/Users/christian/sources/cpp/Builds/Slicer/Release</code>, you could try <code>/Users/christian/D/S4R</code>.</p>

---

## Post #40 by @fedorov (2017-11-22 20:41 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="27" data-topic="1483" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Order of module class instantiation is random. Order of module widget and logic creation is based on the order determined from module dependencies.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> so does this mean that the way things work, developers cannot have python modules that are independent from Slicer? Python modules must have Slicer widget/logic in order to establish module class instantiation?</p>

---

## Post #41 by @lassoan (2017-11-22 20:55 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="40" data-topic="1483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>developers cannot have python modules that are independent from Slicer</p>
</blockquote>
</aside>
<p>By “module” I mean Slicer scripted module. You can use any Python packages that are independent from Slicer, in any way you want. You just have to place them in a subdirectory of any Slicer module directory so that Python can find it.</p>

---

## Post #42 by @fedorov (2017-11-22 21:07 UTC)

<p>I think in the case of <a class="mention" href="/u/che85">@che85</a>, the issue comes from the dependency on a Slicer extension, SlicerDevelopmentToolbox, that contains a set of python packages to reuse from multiple Slicer modules, and it is not loaded when it is needed. It sounds like we would need to add “fake” widget/logic to the classes from that extension to make it loaded in order. Christian, please correct me if I am wrong.</p>

---

## Post #43 by @cpinter (2017-11-22 21:11 UTC)

<p>It doesn’t need to be an actual module, the only thing that needs to be ensured is that the python files are deployed to the proper location, which is recognized by the extension. An example can be DICOMLib or Modules/Loadable/Segmentations/EditorEffects/Python.</p>
<p>If the files are deployed to the right place, the dependencies need to be added (at least this is how I managed to get it to work). See the git commits I referenced <a href="https://discourse.slicer.org/t/nightly-build-tests-failing-for-extensions-with-dependencies-to-other-scriptable-modules/1483/38?u=cpinter">above</a>.</p>

---

## Post #44 by @che85 (2017-11-22 22:34 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> It would be great if that works. In my opinion Slicer should set those in a generic manner instead of having those attributes set within the extensions CMakeLists. I think otherwise it would be very error prone and a lot of overhead.</p>
<p>No idea if that can be done in Slicer itself.</p>

---

## Post #45 by @jcfr (2017-11-22 23:36 UTC)

<p>Hi,</p>
<p>You can build the project Slicer/extensions/Cmake.</p>
<p>Look for “build extensionindex” on the devel FAQ.</p>
<p>Hth<br>
Jc</p>

---

## Post #46 by @che85 (2017-11-22 23:54 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> That’s what I did and those are the results: <a href="http://slicer.cdash.org/testDetails.php?test=8443330&amp;build=11357232" rel="nofollow noopener">http://slicer.cdash.org/testDetails.php?test=8443330&amp;build=11357232</a></p>

---

## Post #47 by @ihnorton (2017-11-23 02:11 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="39" data-topic="1483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>seems to be due to the limit on total size of all the load commands in the dynamic library in the MacOS loader.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/che85">@che85</a> you can confirm this with <code>otool -l LIBRARYNAME</code>.</p>
<p>There is a <a href="https://github.com/NixOS/nixpkgs/pull/27536">hack</a> we could use, essentially to daisy-chain dependencies, but at that level of effort we’re better off reducing the number of shared libraries.</p>
<p>(last time I looked at the slow startup issue on macOS – especially debug build – I think there were over 600 shared libraries loaded, and majority of them were ours. IIRC there were something like 30 million <code>strcmp</code>s during startup while sorting symbols).</p>

---

## Post #48 by @jcfr (2017-11-23 02:32 UTC)

<p>FWIW, a patch is being integrated into VTK to get ride of the PythonD<br>
library and remove the number of libraries.</p>
<p>We could backport it.</p>
<p>Jc</p>

---

## Post #49 by @che85 (2017-11-23 04:24 UTC)

<p><a class="mention" href="/u/ihnorton">@ihnorton</a> Here is the output of otool<br>
<aside class="onebox githubgist">
  <header class="source">
      <a href="https://gist.github.com/che85/5f767b593cfce938a475fa813830e83f" target="_blank" rel="nofollow noopener">gist.github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://gist.github.com/che85/5f767b593cfce938a475fa813830e83f" target="_blank" rel="nofollow noopener">https://gist.github.com/che85/5f767b593cfce938a475fa813830e83f</a></h4>

<p>
</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #50 by @cpinter (2017-11-23 13:32 UTC)

<p>Update: Those path additions that enabled the tests to run locally didn’t do the trick on the factory.<br>
<a href="http://slicer.cdash.org/testDetails.php?test=8445508&amp;build=1136268" class="onebox" target="_blank">http://slicer.cdash.org/testDetails.php?test=8445508&amp;build=1136268</a><br>
The only reason I can see is that the *_DIR paths are not correct. I’ll check on our factory machine.</p>

---

## Post #51 by @che85 (2018-01-19 21:37 UTC)

<p>Hi guys,</p>
<p>are there any updates/ideas for solving this issue?</p>

---

## Post #52 by @fedorov (2018-01-19 21:50 UTC)

<p>Considering the switch to Qt5 and other dramatic changes in the core, it is unfortunate that we don’t have a reliable way to test extensions to identify regressions associated with that process.</p>

---

## Post #53 by @jcfr (2018-01-19 22:04 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="52" data-topic="1483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>unfortunate that we don’t have a reliable way to test extensions to identify regressions associated with that process</p>
</blockquote>
</aside>
<p>To clarify, extensions are still build and tested nightly. It means you will be able to look at the build report every day.</p>

---

## Post #54 by @fedorov (2018-01-19 22:40 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="53" data-topic="1483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>To clarify, extensions are still build and tested nightly. It means you will be able to look at the build report every day.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/jcfr">@jcfr</a> not sure I understand. My understanding was that the issue is “Nightly build TESTS failing for extensions with dependencies to other scriptable modules”, which means we have false alarms instead of actually checking for regressions in the code. Am I missing something?</p>

---

## Post #55 by @fedorov (2018-01-20 04:10 UTC)

<p><a class="mention" href="/u/che85">@che85</a> is there a bug report that documents the problem? If not, can you submit one?</p>

---

## Post #56 by @che85 (2018-01-22 16:18 UTC)

<p>I created a bug report for this issue. See <a href="https://issues.slicer.org/view.php?id=4498" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4498</a></p>

---

## Post #57 by @che85 (2018-02-05 07:00 UTC)

<p>Seems like the tests are running now. I added the following lines to CMakeLists.txt</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/QIICR/QuantitativeReporting/blob/450ac0437ef77172349d72b347af2a854d5f4ce3/CMakeLists.txt#L21-L38" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/QIICR/QuantitativeReporting/blob/450ac0437ef77172349d72b347af2a854d5f4ce3/CMakeLists.txt#L21-L38" target="_blank" rel="nofollow noopener">QIICR/QuantitativeReporting/blob/450ac0437ef77172349d72b347af2a854d5f4ce3/CMakeLists.txt#L21-L38</a></h4>
<pre class="onebox"><code class="lang-txt"><ol class="start lines" start="21" style="counter-reset: li-counter 20 ;">
<li>#find_package(SlicerDevelopmentToolbox REQUIRED)</li>
<li>#find_package(DCMQI REQUIRED)</li>
<li>#find_package(PETDICOMExtension REQUIRED)</li>
<li>
</li>
<li>set(DEPENDENCY_BUILD_DIRS</li>
<li>${SlicerDevelopmentToolbox_DIR}/${Slicer_QTLOADABLEMODULES_LIB_DIR}</li>
<li>${SlicerDevelopmentToolbox_DIR}/${Slicer_CLIMODULES_LIB_DIR}</li>
<li>${PETDICOMExtension_DIR}/${Slicer_QTLOADABLEMODULES_LIB_DIR}</li>
<li>${PETDICOMExtension_DIR}/${Slicer_CLIMODULES_LIB_DIR}</li>
<li>${DCMQI_DIR}/dcmqi-build/bin</li>
<li>)</li>
<li>
</li>
<li>message("DEPENDENCY_BUILD_DIRS: ${DEPENDENCY_BUILD_DIRS}")</li>
<li>
</li>
<li>set(DEPENDENCIES_ADDITIONAL_MODULE_PATHS</li>
<li>${DEPENDENCY_BUILD_DIRS}</li>
<li>${SlicerDevelopmentToolbox_DIR}/${Slicer_QTSCRIPTEDMODULES_LIB_DIR}</li>
<li>)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>and</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/QIICR/QuantitativeReporting/blob/450ac0437ef77172349d72b347af2a854d5f4ce3/Testing/CMakeLists.txt#L1-L6" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/QIICR/QuantitativeReporting/blob/450ac0437ef77172349d72b347af2a854d5f4ce3/Testing/CMakeLists.txt#L1-L6" target="_blank" rel="nofollow noopener">QIICR/QuantitativeReporting/blob/450ac0437ef77172349d72b347af2a854d5f4ce3/Testing/CMakeLists.txt#L1-L6</a></h4>
<pre class="onebox"><code class="lang-txt"><ol class="start lines" start="1" style="counter-reset: li-counter 0 ;">
<li>slicer_add_python_unittest(</li>
<li>SCRIPT ${MODULE_NAME}Tests.py</li>
<li>SLICER_ARGS --additional-module-paths</li>
<li>  ${CMAKE_BINARY_DIR}/${Slicer_QTSCRIPTEDMODULES_LIB_DIR}</li>
<li>  ${DEPENDENCIES_ADDITIONAL_MODULE_PATHS}</li>
<li>)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p><a href="http://slicer.cdash.org/testDetails.php?test=8625898&amp;build=1194275" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/testDetails.php?test=8625898&amp;build=1194275</a></p>
<p>The <code>find_package</code> commands are commented out because they caused CMake configure errors, which in my opinion is giving misleading information to the developer:</p>
<p><a href="http://slicer.cdash.org/viewConfigure.php?buildid=1193166" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/viewConfigure.php?buildid=1193166</a></p>
<p>For any reason when using those find_package commands, DCMQI is not found. <a class="mention" href="/u/jcfr">@jcfr</a> I feel like the following warnings are always displayed. Is that correct?</p>
<pre><code class="lang-auto">CMake Warning at /home/kitware/Dashboards/Nightly/Slicer-0/Extensions/CMake/SlicerBlockAdditionalLauncherSettings.cmake:48 (message):
  Dependent extension PETDICOMExtension cannot be found by CMake
  find_package(), therefore paths variables cannot be imported from this
  extension.  The problem can be resolved by generating
  PETDICOMExtensionConfig.cmake by adding
  include(${Slicer_EXTENSION_GENERATE_CONFIG}) to the top-level
  CMakeLists.txt of the dependent exension.
</code></pre>

---

## Post #58 by @che85 (2018-02-05 16:06 UTC)

<p>Looking at the command line of [1] I am also wondering, why <code>${SlicerDevelopmentToolbox_DIR}</code> could be resolved to <code>/Users/kitware/Dashboards/Nightly/S-481-E-b/SlicerDevelopmentToolbox-build/</code>, but neither<code>${PETDICOMExtension_DIR}</code> could be resolved --&gt;  <code>PETDICOMExtension_DIR-NOTFOUND</code> nor <code>${DCMQI_DIR}</code> could be resolved --&gt; <code>DCMQI_DIR-NOTFOUND</code>.</p>
<p>I will run some more tests.</p>
<p>[1] <a href="http://slicer.cdash.org/testDetails.php?test=8625898&amp;build=1194275" rel="nofollow noopener">http://slicer.cdash.org/testDetails.php?test=8625898&amp;build=1194275</a></p>

---

## Post #59 by @che85 (2018-02-05 16:21 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a> Can you explain why those messages still appear even though I included the mentioned files for every single project and built each one on its own? Am I missing something? Configuring only works, if I specify the directories manually.</p>
<pre><code class="lang-auto">CMake Warning at /Users/christian/sources/cpp/Slicer/Extensions/CMake/SlicerBlockAdditionalLauncherSettings.cmake:48 (message):
  Dependent extension SlicerDevelopmentToolbox cannot be found by CMake
  find_package(), therefore paths variables cannot be imported from this
  extension.  The problem can be resolved by generating
  SlicerDevelopmentToolboxConfig.cmake by adding
  include(${Slicer_EXTENSION_GENERATE_CONFIG}) to the top-level
  CMakeLists.txt of the dependent exension.
Call Stack (most recent call first):
  /Users/christian/D/S4R/Slicer-build/UseSlicer.cmake:281 (include)
  CMakeLists.txt:19 (include)


CMake Warning at /Users/christian/sources/cpp/Slicer/Extensions/CMake/SlicerBlockAdditionalLauncherSettings.cmake:48 (message):
  Dependent extension DCMQI cannot be found by CMake find_package(),
  therefore paths variables cannot be imported from this extension.  The
  problem can be resolved by generating DCMQIConfig.cmake by adding
  include(${Slicer_EXTENSION_GENERATE_CONFIG}) to the top-level
  CMakeLists.txt of the dependent exension.
Call Stack (most recent call first):
  /Users/christian/D/S4R/Slicer-build/UseSlicer.cmake:281 (include)
  CMakeLists.txt:19 (include)


CMake Warning at /Users/christian/sources/cpp/Slicer/Extensions/CMake/SlicerBlockAdditionalLauncherSettings.cmake:48 (message):
  Dependent extension PETDICOMExtension cannot be found by CMake
  find_package(), therefore paths variables cannot be imported from this
  extension.  The problem can be resolved by generating
  PETDICOMExtensionConfig.cmake by adding
  include(${Slicer_EXTENSION_GENERATE_CONFIG}) to the top-level
  CMakeLists.txt of the dependent exension.
Call Stack (most recent call first):
  /Users/christian/D/S4R/Slicer-build/UseSlicer.cmake:281 (include)
  CMakeLists.txt:19 (include)
</code></pre>

---

## Post #60 by @jcfr (2018-02-07 07:02 UTC)

<p>To summarize, this last issue was due to missing dependencies and missing config files generation in the extensions. The following commits address the problem: <a href="https://github.com/Slicer/ExtensionsIndex/commit/34a08966493d756e344a0a42471ebcb9ef8f2e7f">Slicer/ExtensionsIndex@34a0896</a> and <a href="https://github.com/Slicer/ExtensionsIndex/commit/3bdb20a7df2c931ecde9f50b682df34c3dbe127c">Slicer/ExtensionsIndex@3bdb20a</a></p>

---

## Post #61 by @che85 (2018-02-14 16:59 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> I just noticed that it’s still not working. See <a href="http://slicer.cdash.org/viewConfigure.php?buildid=1202036" rel="nofollow noopener">http://slicer.cdash.org/viewConfigure.php?buildid=1202036</a></p>
<p>For any reason, PETDICOMExtension[1,2] cannot be found by CMake.</p>
<p>[1] <a href="https://github.com/Slicer/ExtensionsIndex/blob/master/PETDICOMExtension.s4ext#L9-L10" rel="nofollow noopener">https://github.com/Slicer/ExtensionsIndex/blob/master/PETDICOMExtension.s4ext#L9-L10</a><br>
[2] <a href="https://github.com/QIICR/Slicer-PETDICOMExtension/blob/master/CMakeLists.txt#L34-L35" rel="nofollow noopener">https://github.com/QIICR/Slicer-PETDICOMExtension/blob/master/CMakeLists.txt#L34-L35</a></p>

---

## Post #62 by @fedorov (2018-02-16 23:17 UTC)

<p><a class="mention" href="/u/che85">@che85</a> can you please plan to join the Slicer hangout on the coming Tuesday to follow up on this issue? Thank you</p>

---
