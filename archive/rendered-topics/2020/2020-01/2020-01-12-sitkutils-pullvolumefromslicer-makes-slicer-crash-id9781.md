# sitkUtils.PullVolumeFromSlicer makes Slicer crash

**Topic ID**: 9781
**Date**: 2020-01-12
**URL**: https://discourse.slicer.org/t/sitkutils-pullvolumefromslicer-makes-slicer-crash/9781

---

## Post #1 by @Fernando (2020-01-12 13:11 UTC)

<p>Hi all,</p>
<p>Snippet to reproduce:</p>
<pre><code class="lang-python">import SampleData
import sitkUtils as su
sampleDataLogic = SampleData.SampleDataLogic()
node = sampleDataLogic.downloadMRHead()
su.PullVolumeFromSlicer(node)

</code></pre>
<p>Tried on latest nightly for macOS: <code>r28728</code>.</p>

---

## Post #2 by @Fernando (2020-01-12 13:22 UTC)

<aside class="quote no-group" data-username="Fernando" data-post="1" data-topic="9781">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>import SampleData import sitkUtils as su sampleDataLogic = SampleData.SampleDataLogic() node = sampleDataLogic.downloadMRHead()</p>
</blockquote>
</aside>
<p>Actually, it seems to be a problem with SimpleITK, as <code>sitk.ReadImage()</code> makes Slicer crash as well.</p>
<p><a class="mention" href="/u/blowekamp">@blowekamp</a></p>

---

## Post #3 by @jamesobutler (2020-01-12 20:44 UTC)

<p>Yes, it appears that py_nomainwindow_test_sitkUtils <a href="http://slicer.cdash.org/testDetails.php?test=9875240&amp;build=1797177" rel="nofollow noopener">is failing</a> as you have also reported here. This is likely due to recent updates to ITK and SimpleITK in <a href="https://github.com/Slicer/Slicer/commit/15fda09332c42bf185958ffbc14c9c18b7715a5a" rel="nofollow noopener">28727</a>. That SimpleITK version specifies to use ITK 5.1rc01 which is what we switched to so there in theory shouldn’t be an incompatibility between the two. There had to be a fix to Mac to fix an ITK compile error in the commit after the updated ITK one. Maybe <a class="mention" href="/u/pieper">@pieper</a> can look into this on Mac?</p>
<p>I’ll have to test on Windows to see if it is across platforms, but the test appears to be passing on the Windows build machine.</p>

---

## Post #4 by @pieper (2020-01-12 22:39 UTC)

<p>That code works for me on my local mac build.</p>

---

## Post #5 by @jamesobutler (2020-01-12 22:51 UTC)

<p>Maybe <a class="mention" href="/u/pieper">@pieper</a> you can try to install the package from the nightly build machine to see if it is an issue specific to that package? The tests are showing some Slicer crash using that build.</p>

---

## Post #6 by @pieper (2020-01-12 23:13 UTC)

<p>Yes, you are right - the 2020-01-10 build crashes with that input.</p>
<p>I am able to attach Xcode to the release build but there’s not much stack info (maybe it gets trashed) but it says this is the function where the crash occurs:</p>
<pre><code class="lang-auto">#0	0x000000013a916aaa in itk::ImageFileReader&lt;itk::Image&lt;short, 3u&gt;, itk::DefaultConvertPixelTraits&lt;short&gt; &gt;::EnlargeOutputRequestedRegion(itk::DataObject*) ()
</code></pre>

---

## Post #7 by @lassoan (2020-02-01 16:19 UTC)

<p>This is a very serious limitation of Slicer on MacOS. I don’t have easy access to a Mac and not know much about MacOS anyway, so someone else has to investigate this.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> what do you think? Can you investigate yourself or do you need help from <a class="mention" href="/u/blowekamp">@blowekamp</a> with SimpleITK or <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> with accessing the factory machine?</p>

---

## Post #8 by @pieper (2020-02-01 16:45 UTC)

<p>I agree it’s a blocker for the slicer5 release. (for reference also see <a href="https://discourse.slicer.org/t/fast-marching-gone-for-good/10059/4">this post</a>).</p>
<p>I’m not seeing a lot of clues to suggest a course of action.  I guess I could try making a release build locally and see if I can replicate.</p>
<p>Yes, input from <a class="mention" href="/u/blowekamp">@blowekamp</a> and <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> would be appreciated.</p>

---

## Post #9 by @blowekamp (2020-02-03 16:18 UTC)

<p>I was able to reproduce this on Slicer-4.11.0-2020-1-30 and Slicer-4.11.0-2020-01-12 ( which was be for <a href="https://github.com/Slicer/Slicer/commit/506754f1becd5df717464e320c154142ccd701cb" rel="noopener nofollow ugc">this</a> change with regards to the SITK explicit instantiation library.</p>
<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="9781">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I am able to attach Xcode to the release build but there’s not much stack info (maybe it gets trashed) but it says this is the function where the crash occurs:</p>
<pre><code class="lang-auto">#0	0x000000013a916aaa in itk::ImageFileReader&lt;itk::Image&lt;short, 3u&gt;, itk::DefaultConvertPixelTraits&lt;short&gt; &gt;::EnlargeOutputRequestedRegion(itk::DataObject*) ()
</code></pre>
</blockquote>
</aside>
<p>The lack of symbols is due to the SimpleITK libraries being <a href="https://github.com/SimpleITK/SimpleITK/blob/master/CMake/sitkStripOption.cmake" rel="noopener nofollow ugc">explicitly striped</a>. This greatly reduces the size of the libraries. Without further clues it may be worth it to set “SimpleITK_BUILD_STRIP=OFF” for the nightly Mac build.</p>
<p>This sounds like it’s a problem only with the nightly builds. What is the current OS, Xcode, and OS SDK used for those builds?</p>
<p>This may be some type of miss match with between flags or libraries between the ITK libraries and the SimpleITK libraries. Slicer is using the [“Superbuild” configuration](<a href="https://github.com/Slicer/Slicer/commit/506754f1becd5df717464e320c154142ccd701cb" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix SimpleITK failure to convert between SimpleITK and ITK image… · Slicer/Slicer@506754f · GitHub</a><br>
<span class="hashtag-raw">#diff-109aeb3808fbb9cd5a014863e7556a16R72</span>) for SimpleITK which tries to do more intelligent or user friendly automatic configuration of required flags and libraries.</p>

---

## Post #10 by @Sam_Horvath (2020-02-03 16:31 UTC)

<p>Factory Details:</p>
<p>OS: 10.11.6<br>
XCode: 8.2 (but we aren’t building with Xcode. We are building with Clang  - clang-800.0.42.1)<br>
XCode SDK: Xcode 8.2.1 Build version 8C1002</p>

---

## Post #11 by @blowekamp (2020-02-03 16:34 UTC)

<aside class="quote no-group" data-username="Sam_Horvath" data-post="10" data-topic="9781">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar"> Sam_Horvath:</div>
<blockquote>
<p>XCode SDK: Xcode 8.2.1 Build version 8C1002</p>
</blockquote>
</aside>
<p>More specifically what is <code>CMAKE_OSX_SYSROOT</code> and <code>CMAKE_OSX_DEPLOYMENT_TARGET</code>?</p>

---

## Post #12 by @Sam_Horvath (2020-02-03 16:36 UTC)

<p>From top level build cache:</p>
<pre><code class="lang-auto">//Build architectures for OSX
CMAKE_OSX_ARCHITECTURES:STRING=

CMAKE_OSX_DEPLOYMENT_TARGET:STRING=10.11

//The product will be built against the headers and libraries located
// inside the indicated SDK.
CMAKE_OSX_SYSROOT:PATH=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.12.sdk
</code></pre>

---

## Post #13 by @blowekamp (2020-02-03 17:52 UTC)

<p>How do these variable get propagated to the Superbuild’s External Projects?</p>

---

## Post #14 by @Sam_Horvath (2020-02-03 17:58 UTC)

<p>They are provided in the initial cache when configuring external projects.</p>
<p>I have checked, and the cache variables for ITK and SimpleITK match the top level.</p>

---

## Post #15 by @blowekamp (2020-02-03 22:38 UTC)

<p>Thanks for checking.</p>
<p>I am able to use the PythonSlicer executable successfully:</p>
<pre><code class="lang-auto">./Slicer-4.11.0-2020-01-30.app/Contents/bin/PythonSlicer -c \
  "import SimpleITK as sitk; sitk.ReadImage('/Users/blowekamp/cthead1.png')"
</code></pre>
<p>But if the same commands are execute in the 3D Slicer REPL, then the program termination occurs.</p>
<p>I wonder if this <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/master/Modules/IO/ImageBase/include/itkImageFileReader.hxx#L296" rel="nofollow noopener">dynamic_cast</a> is failing.</p>

---

## Post #16 by @Sam_Horvath (2020-02-04 15:09 UTC)

<p>Interesting.  According to a current failing test( <a href="http://slicer.cdash.org/testDetails.php?test=9874258&amp;build=1815371" rel="nofollow noopener">http://slicer.cdash.org/testDetails.php?test=9874258&amp;build=1815371</a>),</p>
<pre><code class="lang-auto">/Volumes/Dashboards/Preview/Slicer-0-build/Slicer-build/Slicer "--no-splash" "--testing" "--no-main-window" "--additional-module-paths" "/Volumes/Dashboards/Preview/Slicer-0-build/Slicer-build/lib/Slicer-4.11/qt-scripted-modules" "/Volumes/Dashboards/Preview/Slicer-0-build/Slicer-build/lib/Slicer-4.11/cli-modules" "/Volumes/Dashboards/Preview/Slicer-0-build/Slicer-build/lib/Slicer-4.11/qt-loadable-modules" "--python-code" "import slicer.testing; slicer.testing.runUnitTest(['/Volumes/Dashboards/Preview/Slicer-0-build/Slicer-build/Applications/SlicerApp/Testing/Python', '/Volumes/Dashboards/Preview/Slicer-0/Base/Python/tests'], 'test_sitkUtils')"

</code></pre>
<p>also generates the error.</p>
<p>So it looks like we are failing when we are specifically in the full Slicer environment, but not the Slicer python interpreter.</p>

---

## Post #17 by @blowekamp (2020-02-04 16:04 UTC)

<p>The following fails with a verbose message on the nightly build too:</p>
<pre><code class="lang-auto">&gt; import SimpleITK as sitk
&gt; img = sitk.Image(10,10,sitk.sitkUInt8)
&gt; sitk.SmoothingRecursiveGaussian(img)

Traceback (most recent call last):

File "&lt;console&gt;", line 1, in &lt;module&gt;

File "/Users/blowekamp/Desktop/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/SimpleITK-1.3.0.dev527-py3.6-macosx-10.11-x86_64.egg/SimpleITK/SimpleITK.py", line 64305, in SmoothingRecursiveGaussian

return _SimpleITK.SmoothingRecursiveGaussian(*args)

RuntimeError: Exception thrown in SimpleITK SmoothingRecursiveGaussian: /Volumes/Dashboards/Preview/Slicer-0-build/ITK/Modules/Core/Common/include/itkImage.hxx:131:

itk::ERROR: Image(0x7f8224cf4a50): itk::Image::Graft() cannot cast PKN3itk10DataObjectE to PKN3itk5ImageIfLj2EEE
</code></pre>
<p>This confirms is an OSX symbol/dynamic_cast issue.</p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> That further confirms that the Slicer’s runtime is polluting SimpleITK with different ITK symbols than what is expected in the SimpleITK library.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> Are you compiling Slicer with SimpleITK shared or static libraries on OSX?</p>

---

## Post #18 by @Sam_Horvath (2020-02-04 16:12 UTC)

<p>They appear to be static for macOS release:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/4db181a73e03b3a2c8044ffd4e4174d873b267c3/CMakeLists.txt#L341" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/4db181a73e03b3a2c8044ffd4e4174d873b267c3/CMakeLists.txt#L341" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/4db181a73e03b3a2c8044ffd4e4174d873b267c3/CMakeLists.txt#L341</a></h4>
<pre class="onebox"><code class="lang-txt"><ol class="start lines" start="331" style="counter-reset: li-counter 330 ;">
<li>
</li>
<li>#</li>
<li># SimpleITK has large internal libraries, which take an extremely long</li>
<li># time to link on windows when they are static. Creating shared</li>
<li># SimpleITK internal libraries can reduce linking time. Also the size</li>
<li># of the debug libraries are monstrous. Using shared libraries for</li>
<li># debug, reduce disc requirements, and can improve linking</li>
<li># times. However, these shared libraries take longer to load than the</li>
<li># monolithic target from static libraries.</li>
<li>#</li>
<li class="selected">set( Slicer_USE_SimpleITK_SHARED_DEFAULT OFF)</li>
<li>string(TOUPPER "${CMAKE_BUILD_TYPE}" _CMAKE_BUILD_TYPE)</li>
<li>if(MSVC OR _CMAKE_BUILD_TYPE MATCHES "DEBUG")</li>
<li>  set(Slicer_USE_SimpleITK_SHARED_DEFAULT ON)</li>
<li>endif()</li>
<li>CMAKE_DEPENDENT_OPTION(Slicer_USE_SimpleITK_SHARED "Build SimpleITK with shared libraries. Reduces linking time, increases run-time load time." ${Slicer_USE_SimpleITK_SHARED_DEFAULT} "Slicer_USE_SimpleITK" OFF )</li>
<li>mark_as_superbuild(Slicer_USE_SimpleITK_SHARED)</li>
<li>
</li>
<li>#-----------------------------------------------------------------------------</li>
<li># Install no development files by default, but allow the user to get</li>
<li># them installed by setting Slicer_INSTALL_DEVELOPMENT to true.</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>From SimpleITK build cache on factory:</p>
<pre><code class="lang-auto">//Build SimpleITK ITK with shared libraries. This does not effect
// wrapped languages.
BUILD_SHARED_LIBS:BOOL=OFF
</code></pre>

---

## Post #19 by @blowekamp (2020-02-04 16:32 UTC)

<p>I recall Steve being a fan of compline Slicer in Debug mode. If so then line 343 would have made the libraries be shared by default.</p>
<p>I have not set up a Slicer build environment, and I need to know the requirements for a system setup to reproduce the issue. The nightly build system seems a little exotic with its custom clang compiler.</p>

---

## Post #20 by @pieper (2020-02-04 16:36 UTC)

<p>Yes, my local build is <code>Debug</code> and my CMakeCache.txt says:</p>
<p><code>Slicer_USE_SimpleITK_SHARED:BOOL=ON</code></p>
<p>My compiler is the one that comes with Xcode.</p>

---

## Post #21 by @blowekamp (2020-02-04 16:40 UTC)

<p>Has anyone else compiled Slicer with SimpleITK on OSX? Does it have this same casting problem?</p>
<aside class="quote no-group" data-username="pieper" data-post="20" data-topic="9781" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Yes, my local build is <code>Debug</code> and my CMakeCache.txt says:</p>
<p><code>Slicer_USE_SimpleITK_SHARED:BOOL=ON</code></p>
</blockquote>
</aside>
<p>And your build does not exhibit this issue. Could you delete all the SITK build stuff and try with <code>Slicer_USE_SimpleITK_SHARED:BOOL=OFF</code>?</p>
<p>I wonder if anyone else has a local build of Slicer with SimpleITK enabled on OSX to check if they have this same issue?</p>

---

## Post #22 by @Sam_Horvath (2020-02-04 16:41 UTC)

<p>I am actually not sure how to reproduce the factory setup (wiki info is out of date).  <a class="mention" href="/u/jcfr">@jcfr</a> !!</p>
<p>I can set up up debug build on the factory.  Steve, you posted earlier that your local (debug) build wasn’t crashing?</p>

---

## Post #23 by @pieper (2020-02-04 17:30 UTC)

<p>Right, my debug build with shared libraries does not crash.  I’ll try non-shared as Brad suggested and report back.</p>

---

## Post #24 by @jcfr (2020-02-04 17:46 UTC)

<aside class="quote no-group" data-username="Sam_Horvath" data-post="22" data-topic="9781">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar"> Sam_Horvath:</div>
<blockquote>
<p>I am actually not sure how to reproduce the factory setup (wiki info is out of date).</p>
</blockquote>
</aside>
<p>Which information is not up-to-date ? See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory#factory-south.kitware" class="inline-onebox">Documentation/Nightly/Developers/Factory - Slicer Wiki</a></p>
<p>What are you trying to do ?</p>

---

## Post #25 by @Sam_Horvath (2020-02-04 17:58 UTC)

<p>I am not familiar with mac, and so I am not sure how the clang compiler interacts with the XCode setup (cmake finds the compiler through the xcode toolchain).  I don’t know how the compiler is installed or from where.</p>
<p>The factory notes includes details about VMs on the mac machine which is very out of date for our current setup.</p>

---

## Post #26 by @pieper (2020-02-04 18:41 UTC)

<p>I can replicate the crash when I build in Debug with <code>Slicer_USE_SimpleITK_SHARED:BOOL=OFF</code></p>
<p>Here’s the stack trace.  As suspected the dynamic case results in a null pointer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a69749504d6e5269f387988dcc33dd0dfaf02d4.jpeg" data-download-href="/uploads/short-url/fbmy2qgPwoMntFb66Ufj1dMi1Ks.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a69749504d6e5269f387988dcc33dd0dfaf02d4_2_690x256.jpeg" alt="image" data-base62-sha1="fbmy2qgPwoMntFb66Ufj1dMi1Ks" width="690" height="256" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a69749504d6e5269f387988dcc33dd0dfaf02d4_2_690x256.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a69749504d6e5269f387988dcc33dd0dfaf02d4_2_1035x384.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a69749504d6e5269f387988dcc33dd0dfaf02d4_2_1380x512.jpeg 2x" data-dominant-color="EEEDED"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2168×805 412 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Here’s some more info on the object it’s trying to convert:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05b9e0cedb780d64141ff4edec21a9b3f1816e8f.jpeg" data-download-href="/uploads/short-url/OED1FhPhdNftXzFAkHuMvE5R5d.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/05b9e0cedb780d64141ff4edec21a9b3f1816e8f_2_690x217.jpeg" alt="image" data-base62-sha1="OED1FhPhdNftXzFAkHuMvE5R5d" width="690" height="217" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/05b9e0cedb780d64141ff4edec21a9b3f1816e8f_2_690x217.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05b9e0cedb780d64141ff4edec21a9b3f1816e8f.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05b9e0cedb780d64141ff4edec21a9b3f1816e8f.jpeg 2x" data-dominant-color="E8E7E7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">861×271 77.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #27 by @jcfr (2020-02-04 19:06 UTC)

<aside class="quote no-group" data-username="Sam_Horvath" data-post="25" data-topic="9781">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar"> Sam_Horvath:</div>
<blockquote>
<p>clang compiler interacts with the XCode setup</p>
</blockquote>
</aside>
<p>This is the compiler provided by XCode installed on the machine. I updated the page.</p>

---

## Post #28 by @blowekamp (2020-02-05 21:38 UTC)

<p>Thanks for testing Steve! That was a big help to help reproduce the issue.</p>
<p>I believe the following correction is needed, but my build has not finished the clean rebuild. The partial rebuild failed but the nm inspection of the _SimpleITK.so library indicated the symbols were exported as the prior working version.</p>
<pre><code class="lang-auto">diff --git a/SuperBuild/External_SimpleITK.cmake b/SuperBuild/External_SimpleITK.cmake
index 2e8f20106..cb3cd4710 100644
--- a/SuperBuild/External_SimpleITK.cmake
+++ b/SuperBuild/External_SimpleITK.cmake
@@ -88,7 +88,7 @@ ExternalProject_Execute(${proj} \"install\" \"${PYTHON_EXECUTABLE}\" Packaging/s
       -DSimpleITK_INSTALL_ARCHIVE_DIR:PATH=${Slicer_INSTALL_LIB_DIR}
       -DSimpleITK_INSTALL_LIBRARY_DIR:PATH=${Slicer_INSTALL_LIB_DIR}
       -DSimpleITK_INT64_PIXELIDS:BOOL=OFF
-      -DSimpleITK_EXPLICIT_INSTATIATION_DEFAULT:BOOL=ON
+      -DSimpleITK_EXPLICIT_INSTANTIATION:BOOL=ON
       -DCMAKE_INSTALL_PREFIX:PATH=&lt;INSTALL_DIR&gt;
       -DSimpleITK_USE_SYSTEM_ITK:BOOL=ON
       -DITK_DIR:PATH=${ITK_DIR}
</code></pre>

---

## Post #29 by @pieper (2020-02-05 22:34 UTC)

<p>Just changing the flag and rebuilding didn’t work, so I’m deleting all my Simple* directories from the build tree and retrying.</p>

---

## Post #30 by @pieper (2020-02-05 23:06 UTC)

<p>Unfortunately setting <code>-DSimpleITK_EXPLICIT_INSTATIATION:BOOL=ON</code> didn’t work even after rebuilding all the SimpleITK code.  It still crashes when I try to run a command in SimpleFilters.</p>
<p>Anything else to try?</p>

---

## Post #31 by @blowekamp (2020-02-06 13:55 UTC)

<p>Let us verify this build and installation as we have had problems getting a clear re-build of SimpleITK before.</p>
<p>To check the build SimpleITK library got install correctly and the symbols are as expected, please in the build directory run:</p>
<pre><code class="lang-auto">for f in $(find ./ -name _SimpleITK.\*.so); do nm -C $f | grep vtable\ for\ itk::ImageBase; echo "==&gt;$f"; done
</code></pre>
<p>This should find the library in the SimpleITK-build directory and the one installed in Python’s site-packages.</p>
<p>This distinguishes between the working Slicers and the broken ones:</p>
<pre><code class="lang-auto">$ for f in $(find ./ -name _SimpleITK.\*.so); do nm -C $f | grep vtable\ for\ itk::ImageBase; echo "==&gt;$f"; done
==&gt;.//Slicer-2020-01-15.app/Contents/lib/Python/lib/python3.6/site-packages/SimpleITK-1.3.0.dev527-py3.6-macosx-10.11-x86_64.egg/SimpleITK/_SimpleITK.cpython-36m-darwin.so

00000000078234d8 D **vtable for itk::ImageBase** &lt;1u&gt;

0000000007823728 D **vtable for itk::ImageBase** &lt;2u&gt;

0000000007823978 D **vtable for itk::ImageBase** &lt;3u&gt;

==&gt;.//Slicer-2019-12-28.app/Contents/lib/Python/lib/python3.6/site-packages/SimpleITK-1.3.0rc2.dev260-py3.6-macosx-10.11-x86_64.egg/SimpleITK/_SimpleITK.cpython-36m-darwin.so

==&gt;.//Slicer-2020-01-30.app/Contents/lib/Python/lib/python3.6/site-packages/SimpleITK-1.3.0.dev527-py3.6-macosx-10.11-x86_64.egg/SimpleITK/_SimpleITK.cpython-36m-darwin.so

==&gt;.//Slicer-2020-01-30.app/Contents/lib/Python/lib/python3.6/site-packages/SimpleITK-1.3.0.dev527-py3.6-macosx-10.11-x86_64.egg/SimpleITK/_SimpleITK.cpython-36m-darwin.so

</code></pre>

---

## Post #32 by @lassoan (2020-02-06 17:45 UTC)

<aside class="quote no-group" data-username="pieper" data-post="30" data-topic="9781">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p><code>-DSimpleITK_EXPLICIT_INSTATIATION:BOOL=ON</code></p>
</blockquote>
</aside>
<p>SHould we just change this in the nightly build and see if it fixes the issue? (worst case it does not fix the problem on Mac and breaks Windows builds, too - but these should be OK for one day)</p>

---

## Post #33 by @pieper (2020-02-06 18:59 UTC)

<aside class="quote no-group quote-modified" data-username="blowekamp" data-post="31" data-topic="9781">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/blowekamp/48/1386_2.png" class="avatar"> blowekamp:</div>
<blockquote>
<p>for f in $(find ./ -name _SimpleITK.*.so); do nm -C $f | grep vtable\ for\ itk::ImageBase; echo “==&gt;$f”; done</p>
</blockquote>
</aside>
<p>Here are my results.  I’ll try deleting these python installation versions and rebuild using the same settings (non-shared, with explicit instantiation).</p>
<pre><code class="lang-auto">rock:s pieper$ for f in $(find ./ -name _SimpleITK.\*.so); do nm -C $f | grep vtable\ for\ itk::ImageBase; echo "==&gt;$f"; done
000000000e683328 s vtable for itk::ImageBase&lt;1u&gt;
000000000e02f0d0 s vtable for itk::ImageBase&lt;2u&gt;
000000000e02c5f0 s vtable for itk::ImageBase&lt;3u&gt;
000000000e279818 s vtable for itk::ImageBase&lt;4u&gt;
000000000df04660 s vtable for itk::ImageBase&lt;5u&gt;
==&gt;.//python-install/lib/python3.6/site-packages/SimpleITK-1.3.0.dev527-py3.6-macosx-10.14-x86_64.egg/SimpleITK/_SimpleITK.cpython-36m-darwin.so
==&gt;.//python-install/lib/python3.6/site-packages/SimpleITK-1.3.0rc2.dev260-py3.6-macosx-10.14-x86_64.egg/SimpleITK/_SimpleITK.cpython-36m-darwin.so
000000000e683328 s vtable for itk::ImageBase&lt;1u&gt;
000000000e02f0d0 s vtable for itk::ImageBase&lt;2u&gt;
000000000e02c5f0 s vtable for itk::ImageBase&lt;3u&gt;
000000000e279818 s vtable for itk::ImageBase&lt;4u&gt;
000000000df04660 s vtable for itk::ImageBase&lt;5u&gt;
==&gt;.//SimpleITK-build/SimpleITK-build/Wrapping/Python/build/lib.macosx-10.14-x86_64-3.6/SimpleITK/_SimpleITK.cpython-36m-darwin.so
</code></pre>

---

## Post #34 by @pieper (2020-02-06 19:00 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="32" data-topic="9781">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>SHould we just change this in the nightly build and see if it fixes the issue?</p>
</blockquote>
</aside>
<p>I would say yes, or we can wait until my build finishes.</p>

---

## Post #35 by @pieper (2020-02-06 22:54 UTC)

<p>I deleted and regenerated the files and this is what I get (slicer still crashes when I try to run a SimpleFilters operation).</p>
<pre><code class="lang-auto">rock:s pieper$ for f in $(find ./ -name _SimpleITK.\*.so); do nm -C $f | grep vtable\ for\ itk::ImageBase; echo "==&gt;$f"; done
000000000e683328 s vtable for itk::ImageBase&lt;1u&gt;
000000000e02f0d0 s vtable for itk::ImageBase&lt;2u&gt;
000000000e02c5f0 s vtable for itk::ImageBase&lt;3u&gt;
000000000e279818 s vtable for itk::ImageBase&lt;4u&gt;
000000000df04660 s vtable for itk::ImageBase&lt;5u&gt;
==&gt;.//python-install/lib/python3.6/site-packages/SimpleITK-1.3.0.dev527-py3.6-macosx-10.14-x86_64.egg/SimpleITK/_SimpleITK.cpython-36m-darwin.so
000000000e683328 s vtable for itk::ImageBase&lt;1u&gt;
000000000e02f0d0 s vtable for itk::ImageBase&lt;2u&gt;
000000000e02c5f0 s vtable for itk::ImageBase&lt;3u&gt;
000000000e279818 s vtable for itk::ImageBase&lt;4u&gt;
000000000df04660 s vtable for itk::ImageBase&lt;5u&gt;
==&gt;.//SimpleITK-build/SimpleITK-build/Wrapping/Python/build/lib.macosx-10.14-x86_64-3.6/SimpleITK/_SimpleITK.cpython-36m-darwin.so
</code></pre>

---

## Post #36 by @blowekamp (2020-02-07 15:09 UTC)

<p>I was able to get back to my build. The symbols of the library are as expected and match that of the working Slicer distribution:</p>
<pre><code class="lang-auto">Slicer]$ for f in $(find ./ -name _SimpleITK.\*.so); do nm -C $f | grep vtable\ for\ itk::ImageBase; echo "==&gt;$f"; done
00000000114cf1b0 D vtable for itk::ImageBase&lt;1u&gt;
00000000114cf400 D vtable for itk::ImageBase&lt;2u&gt;
00000000114cf650 D vtable for itk::ImageBase&lt;3u&gt;
0000000010d2d280 d vtable for itk::ImageBase&lt;4u&gt;
0000000010a15170 d vtable for itk::ImageBase&lt;5u&gt;
==&gt;.//python-install/lib/python3.6/site-packages/SimpleITK-1.3.0.dev527-py3.6-macosx-10.13-x86_64.egg/SimpleITK/_SimpleITK.cpython-36m-darwin.so
00000000114cf1b0 D vtable for itk::ImageBase&lt;1u&gt;
00000000114cf400 D vtable for itk::ImageBase&lt;2u&gt;
00000000114cf650 D vtable for itk::ImageBase&lt;3u&gt;
0000000010d2d280 d vtable for itk::ImageBase&lt;4u&gt;
0000000010a15170 d vtable for itk::ImageBase&lt;5u&gt;
==&gt;.//SimpleITK-build/SimpleITK-build/Wrapping/Python/build/lib.macosx-10.13-x86_64-3.6/SimpleITK/_SimpleITK.cpython-36m-darwin.so
</code></pre>
<p>Now, the from the GUI the python fails on `sitk.Image(10,10,sitk.sitkUInt8);</p>
<p><em>corrected</em><br>
From the command line with <code>PythonSlicer</code> there are unresolved sysmbols, which I guess is expected:</p>
<pre><code class="lang-auto"> .//python-install/bin/PythonSlicer  -c  "import SimpleITK as sitk; sitk.Image(10,10,sitk.sitkUInt8);"
dyld: lazy symbol binding failed: Symbol not found: __ZN3itk11ImageRegionILj2EEC1Ev
  Referenced from: /scratch/blowekamp/Slicer/python-install/lib/python3.6/site-packages/SimpleITK-1.3.0.dev527-py3.6-macosx-10.13-x86_64.egg/SimpleITK/_SimpleITK.cpython-36m-darwin.so
  Expected in: flat namespace

dyld: Symbol not found: __ZN3itk11ImageRegionILj2EEC1Ev
  Referenced from: /scratch/blowekamp/Slicer/python-install/lib/python3.6/site-packages/SimpleITK-1.3.0.dev527-py3.6-macosx-10.13-x86_64.egg/SimpleITK/_SimpleITK.cpython-36m-darwin.so
  Expected in: flat namespace

error: [/scratch/blowekamp/Slicer/python-install/bin/./python] exit abnormally - Report the problem.
</code></pre>

---

## Post #37 by @blowekamp (2020-02-07 17:03 UTC)

<p>I compiled SimpleITK v1.2.4 with the currently Slicer environment. I got simular terminations as before.</p>
<p>I did attach lldb to a running Slicer process and entered <code>sitk.Image(10,10,sitk.sitkUInt8)</code>:</p>
<p>This is the top of the stack trace I got:</p>
<pre><code class="lang-auto"> thread #1, queue = 'com.apple.main-thread', stop reason = signal SIGABRT
  * frame #0: 0x00000001063553ba dyld`__abort_with_payload + 10
    frame #1: 0x0000000106354bac dyld`abort_with_payload_wrapper_internal + 82
    frame #2: 0x0000000106354bde dyld`abort_with_payload + 9
    frame #3: 0x0000000106314a9d dyld`dyld::halt(char const*) + 343
    frame #4: 0x0000000106314bc7 dyld`dyld::fastBindLazySymbol(ImageLoader**, unsigned long) + 167
    frame #5: 0x00007fff7b20532e libdyld.dylib`dyld_stub_binder + 282
    frame #6: 0x000000016233f3c8 _SimpleITK.cpython-36m-darwin.so
    frame #7: 0x0000000152bd2c1a _SimpleITK.cpython-36m-darwin.so`void std::__1::__invoke_void_return_wrapper&lt;void&gt;::__call&lt;std::__1::__bind&lt;void (itk::simple::Image::*&amp;)(unsigned int, unsigned int, unsigned int, unsigned int, unsigned int), itk::simple::Image*&amp;, std::__1::placeholders::__ph&lt;1&gt; const&amp;, std::__1::placeholders::__ph&lt;2&gt; const&amp;, std::__1::placeholders::__ph&lt;3&gt; const&amp;, std::__1::placeholders::__ph&lt;4&gt; const&amp;, std::__1::placeholders::__ph&lt;5&gt; const&amp;&gt;&amp;, unsigned int, unsigned int, unsigned int, unsigned int, unsigned int&gt;(std::__1::__bind&lt;void (itk::simple::Image::*&amp;)(unsigned int, unsigned int, unsigned int, unsigned int, unsigned int), itk::simple::Image*&amp;, std::__1::placeholders::__ph&lt;1&gt; const&amp;, std::__1::placeholders::__ph&lt;2&gt; const&amp;, std::__1::placeholders::__ph&lt;3&gt; const&amp;, std::__1::placeholders::__ph&lt;4&gt; const&amp;, std::__1::placeholders::__ph&lt;5&gt; const&amp;&gt;&amp;&amp;&amp;, unsigned int&amp;&amp;, unsigned int&amp;&amp;, unsigned int&amp;&amp;, unsigned int&amp;&amp;, unsigned int&amp;&amp;) [inlined] decltype(__f=0x00007ffeebeec2a8, __a0=0x00007ffeebeec2b8, __args=0x00007ffeebeebcfc, __args=0x00007ffeebeebcf8, __args=0x00007ffeebeebcf4, __args=0x00007ffeebeebcf0, __args=0x00007ffeebeebcec)).*fp(std::__1::forward&lt;unsigned int, unsigned int, unsigned int, unsigned int, unsigned int&gt;(fp1))) std::__1::__invoke&lt;void (itk::simple::Image::*&amp;)(unsigned int, unsigned int, unsigned int, unsigned int, unsigned int), itk::simple::Image*&amp;, unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, void&gt;(void (itk::simple::Image::*&amp;&amp;&amp;)(unsigned int, unsigned int, unsigned int, unsigned int, unsigned int), itk::simple::Image*&amp;&amp;&amp;, unsigned int&amp;&amp;, unsigned int&amp;&amp;, unsigned int&amp;&amp;, unsigned int&amp;&amp;, unsigned int&amp;&amp;) at type_traits:4264
</code></pre>
<p>From googling, I believe this is due to missing symbols.</p>

---

## Post #38 by @blowekamp (2020-02-07 20:56 UTC)

<p>I was able to get the library working by setting “CMAKE_CXX_VISIBILITY_PRESET=default” and disabling the SimpleITK’s explicit ITK library. This <a href="https://github.com/SimpleITK/SimpleITK/pull/968" rel="nofollow noopener">SimpleITK PR</a> will be required.</p>
<p>Because all the ITK symbols are at the library interface now the size is much larger:</p>
<p>483M .//python-install/lib/python3.6/site-packages/SimpleITK-1.2.4-py3.6-macosx-10.13-x86_64.egg/SimpleITK/_SimpleITK.cpython-36m-darwin.so</p>
<p>After <code>strip -x</code>:<br>
296M .//python-install/lib/python3.6/site-packages/SimpleITK-1.2.4-py3.6-macosx-10.13-x86_64.egg/SimpleITK/_SimpleITK.cpython-36m-darwin.so</p>
<p>By comparison the SimpleITK pypi binary contains all ITK IO, but doesn’t expose any symbols. The library is much smaller:<br>
179M .//lib/python3.6/site-packages/SimpleITK/_SimpleITK.cpython-36m-darwin.so</p>

---

## Post #39 by @pieper (2020-02-07 21:21 UTC)

<p>Nice Brad <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>
<p>Looks like that PR has been merged, so I’ll try a local build.</p>

---

## Post #40 by @blowekamp (2020-02-07 21:37 UTC)

<p>This is what I am working on compiling locally:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://github.com/blowekamp/Slicer/tree/SimpleITKUseDefaultVisibility" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars1.githubusercontent.com/u/321061?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/blowekamp/Slicer/tree/SimpleITKUseDefaultVisibility" target="_blank" rel="nofollow noopener">blowekamp/Slicer</a></h3>

<p>Multi-platform, free open source software for visualization and image computing. - blowekamp/Slicer</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>The change of visibility likely is not needed on Linux and Windows ( Have we verified SimpleITK is working on them currently?), so to minimize size it may be best to only change the visibility on OSX.</p>

---

## Post #41 by @pieper (2020-02-07 22:34 UTC)

<p>Hmm, well I rebuilt with the referenced ITK and SimpleITK and didn’t get any build errors, but when I try to run it says I can’t import SimpleITK.  I used the same build flags as before.</p>
<pre><code class="lang-auto">Switch to module:  "SimpleFilters"
Traceback (most recent call last):
  File "/s/python-install/lib/python3.6/site-packages/SimpleITK/SimpleITK.py", line 14, in swig_import_helper
    return importlib.import_module(mname)
  File "/s/python-install/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "&lt;frozen importlib._bootstrap&gt;", line 994, in _gcd_import
  File "&lt;frozen importlib._bootstrap&gt;", line 971, in _find_and_load
  File "&lt;frozen importlib._bootstrap&gt;", line 953, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'SimpleITK._SimpleITK'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/s/Slicer-build/lib/Slicer-4.11/qt-scripted-modules/SimpleFilters.py", line 83, in __init__
    import SimpleITK as sitk
  File "/s/python-install/lib/python3.6/site-packages/SimpleITK/__init__.py", line 1, in &lt;module&gt;
    from .SimpleITK import *
  File "/s/python-install/lib/python3.6/site-packages/SimpleITK/SimpleITK.py", line 17, in &lt;module&gt;
    _SimpleITK = swig_import_helper()
  File "/s/python-install/lib/python3.6/site-packages/SimpleITK/SimpleITK.py", line 16, in swig_import_helper
    return importlib.import_module('_SimpleITK')
  File "/s/python-install/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
ModuleNotFoundError: No module named '_SimpleITK'
qSlicerPythonCppAPI::instantiateClass  - [ "SimpleFiltersWidget" ] - Failed to instantiate scripted pythonqt class "SimpleFiltersWidget" 0x7fcc110eae68

</code></pre>

---

## Post #42 by @blowekamp (2020-02-11 15:05 UTC)

<aside class="quote no-group" data-username="pieper" data-post="41" data-topic="9781">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I used the same build flags as before</p>
</blockquote>
</aside>
<p>I am not sure what additional changes you had.</p>
<p>I have done a clean build in Debug and Release, and SimpleITK with SimpleFilters, and the test pass for me.</p>
<p>When I cleanly built <a href="https://github.com/blowekamp/Slicer/tree/SimpleITKUseDefaultVisibility" rel="noopener nofollow ugc">the branch</a> in Debug mode (with SimpleITK shared libraries the default options), initially I got an ITK compilation error:</p>
<pre><code class="lang-auto">Undefined symbols for architecture x86_64:
  "itk::TransformBaseTemplate&lt;double&gt;::TransformBaseTemplate()", referenced from:
      itk::Transform&lt;double, 4u, 4u&gt;::Transform(unsigned long) in itkTransformFactoryBaseRegisterDoubleParameters.cxx.o
      itk::Transform&lt;double, 3u, 3u&gt;::Transform(unsigned long) in itkTransformFactoryBaseRegisterDoubleParameters.cxx.o
      itk::Transform&lt;double, 2u, 2u&gt;::Transform(unsigned long) in itkTransformFactoryBaseRegisterDoubleParameters.cxx.o
      itk::Transform&lt;double, 3u, 2u&gt;::Transform(unsigned long) in itkTransformFactoryBaseRegisterDoubleParameters.cxx.o
  "itk::TransformBaseTemplate&lt;double&gt;::~TransformBaseTemplate()", referenced from:
      itk::Transform&lt;double, 4u, 4u&gt;::Transform(unsigned long) in itkTransformFactoryBaseRegisterDoubleParameters.cxx.o
      itk::Transform&lt;double, 4u, 4u&gt;::~Transform() in itkTransformFactoryBaseRegisterDoubleParameters.cxx.o
      itk::Transform&lt;double, 3u, 3u&gt;::Transform(unsigned long) in itkTransformFactoryBaseRegisterDoubleParameters.cxx.o
      itk::Transform&lt;double, 3u, 3u&gt;::~Transform() in itkTransformFactoryBaseRegisterDoubleParameters.cxx.o
      itk::Transform&lt;double, 2u, 2u&gt;::Transform(unsigned long) in itkTransformFactoryBaseRegisterDoubleParameters.cxx.o
      itk::Transform&lt;double, 2u, 2u&gt;::~Transform() in itkTransformFactoryBaseRegisterDoubleParameters.cxx.o
      itk::Transform&lt;double, 3u, 2u&gt;::Transform(unsigned long) in itkTransformFactoryBaseRegisterDoubleParameters.cxx.o
      ...

</code></pre>
<p>But then I reverted to the current ITK branch ( and removed the MeanImageFilter from SimpleITK). And the build completed OK.</p>
<p>I believe this is the solution, we just need to get ITK and SimpleITK in sync.</p>

---

## Post #43 by @pieper (2020-02-11 18:38 UTC)

<aside class="quote no-group" data-username="blowekamp" data-post="42" data-topic="9781">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/blowekamp/48/1386_2.png" class="avatar"> blowekamp:</div>
<blockquote>
<p>I am not sure what additional changes you had.</p>
</blockquote>
</aside>
<p>I was referring to the instantiation and visibility flags we’d been discussing above.</p>
<aside class="quote no-group" data-username="blowekamp" data-post="42" data-topic="9781">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/blowekamp/48/1386_2.png" class="avatar"> blowekamp:</div>
<blockquote>
<p>I believe this is the solution, we just need to get ITK and SimpleITK in sync.</p>
</blockquote>
</aside>
<p>So that means this PR then: <a href="https://github.com/Slicer/Slicer/pull/1324" class="inline-onebox">modfying opacity in the listing of models does not work · Issue #1324 · Slicer/Slicer · GitHub</a></p>
<p>I agree with the comment from <a class="mention" href="/u/lassoan">@lassoan</a> that it would be cleaner and less confusing if the changes could be in a tagged ITK version.  (Could it be ITK  v5.1rc02?).</p>

---

## Post #44 by @blowekamp (2020-02-11 18:59 UTC)

<p>The ITK version does not need to be updated.</p>
<p>I have a dangling branch of SimpleITK which cherry picked the needed change in SimpleITK to get it working with Slicer.</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="32" height="32">
      <a href="https://github.com/blowekamp/SimpleITK/tree/slicer-vv1.2.4-2020-02-07-777520bd" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars1.githubusercontent.com/u/321061?s=400&amp;v=4" class="thumbnail onebox-avatar" width="420" height="420">

<h3><a href="https://github.com/blowekamp/SimpleITK/tree/slicer-vv1.2.4-2020-02-07-777520bd" target="_blank" rel="nofollow noopener">blowekamp/SimpleITK</a></h3>

<p>Contribute to blowekamp/SimpleITK development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>The branch just needs to be in <a href="https://github.com/Slicer/SimpleITK" rel="nofollow noopener">Slicer’s SimpleITK fork</a>. Then we will not need to change the current ITK in Slicer is using.</p>

---

## Post #45 by @blowekamp (2020-02-13 16:16 UTC)

<p>This patch was merged, and the SimpleFilters module works in the current Slicer nightly build.</p>

---

## Post #46 by @pieper (2020-02-13 16:31 UTC)

<p>Confirmed SimpleFilters is also working now on my local build <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:">  Thanks <a class="mention" href="/u/blowekamp">@blowekamp</a>!</p>

---
