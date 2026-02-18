# Many extensions are not getting updates for Slicer Stable Release

**Topic ID**: 34343
**Date**: 2024-02-15
**URL**: https://discourse.slicer.org/t/many-extensions-are-not-getting-updates-for-slicer-stable-release/34343

---

## Post #1 by @lassoan (2024-02-15 15:10 UTC)

<p>Nightly build of many extensions for Slicer-5.6 have build errors on Windows and macOS. The errors started to show up a few weeks ago.</p>
<p>For example, SlicerHeart extension failures:</p>
<p><a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;begin=2024-01-01&amp;end=2024-02-15&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=SlicerHeart" class="onebox" target="_blank" rel="noopener">https://slicer.cdash.org/index.php?project=SlicerStable&amp;begin=2024-01-01&amp;end=2024-02-15&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=SlicerHeart</a></p>
<p>We did not modify anything in SlicerHeart extension’s main branch, so most likely something has changed on the factory machines.</p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/jcfr">@jcfr</a> could you please have a look?</p>

---

## Post #2 by @jamesobutler (2024-02-16 16:45 UTC)

<p>It appears that around Tuesday January 30th, during Slicer Project week, there were some changes to the factory build machines.</p>
<p>Based on the Slicer Stable cDash configure errors, my guess is that Slicer 5.6.1 stable was built with MSVC 14.35.32215 (Visual Studio 17.5). Then Visual Studio was updated to 17.8 which brought in MSVC 14.38.33130 and resulted in compiled Slicer extensions complaining about a mismatch when trying to build against the Slicer Stable build tree.</p>

---

## Post #3 by @jcfr (2024-02-16 17:03 UTC)

<h3><a name="p-107027-build-of-macos-stable-extensions-1" class="anchor" href="#p-107027-build-of-macos-stable-extensions-1" aria-label="Heading link"></a>Build of macOS Stable extensions</h3>
<p>The macOS Stable extension build starting to fail after January 9th.</p>
<p>We are working on addressing this and will follow-up shortly.</p>
<h3><a name="p-107027-slicerheart-2" class="anchor" href="#p-107027-slicerheart-2" aria-label="Heading link"></a>SlicerHeart</h3>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be805d9155ad1cf89b7de271718ef280141a785b.jpeg" data-download-href="/uploads/short-url/rbfJXaiUGkeQJ1uhs6nAJaG993B.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be805d9155ad1cf89b7de271718ef280141a785b_2_517x247.jpeg" alt="image" data-base62-sha1="rbfJXaiUGkeQJ1uhs6nAJaG993B" width="517" height="247" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be805d9155ad1cf89b7de271718ef280141a785b_2_517x247.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be805d9155ad1cf89b7de271718ef280141a785b_2_775x370.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be805d9155ad1cf89b7de271718ef280141a785b_2_1034x494.jpeg 2x" data-dominant-color="DAD6CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×921 195 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Link: <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;begin=2023-12-01&amp;end=2024-02-15&amp;filtercount=2&amp;showfilters=1&amp;filtercombine=and&amp;field1=buildname&amp;compare1=63&amp;value1=SlicerHeart&amp;field2=site&amp;compare2=63&amp;value2=computron" class="inline-onebox">SlicerStable</a></p>
<h3><a name="p-107027-slicerrt-3" class="anchor" href="#p-107027-slicerrt-3" aria-label="Heading link"></a>SlicerRT</h3>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f9ae81ba1ac254792e05cafc30774141917badd.jpeg" data-download-href="/uploads/short-url/dDLfeuBZYbxrFr7zg0k9m0KOoWx.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f9ae81ba1ac254792e05cafc30774141917badd_2_517x261.jpeg" alt="image" data-base62-sha1="dDLfeuBZYbxrFr7zg0k9m0KOoWx" width="517" height="261" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f9ae81ba1ac254792e05cafc30774141917badd_2_517x261.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f9ae81ba1ac254792e05cafc30774141917badd_2_775x391.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f9ae81ba1ac254792e05cafc30774141917badd_2_1034x522.jpeg 2x" data-dominant-color="DDDAD0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×969 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Link: <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;begin=2023-12-01&amp;end=2024-02-15&amp;filtercount=2&amp;showfilters=1&amp;filtercombine=and&amp;field1=buildname&amp;compare1=63&amp;value1=SlicerRT&amp;field2=site&amp;compare2=63&amp;value2=computron" class="inline-onebox">SlicerStable</a></p>

---

## Post #4 by @jcfr (2024-02-16 21:46 UTC)

<h2><a name="p-107043-build-of-macos-stable-extensions-1" class="anchor" href="#p-107043-build-of-macos-stable-extensions-1" aria-label="Heading link"></a>Build of macOS Stable extensions</h2>
<p>The build of macOS stable extensions has been restored <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></p>
<p>The fixes applied should address errors like the following:</p>
<pre><code class="lang-auto">CMake Error in KretzFileReader/Logic/CMakeLists.txt:
  Imported target "qSlicerBaseQTCLI" includes non-existent path
    "/Applications/Xcode-14.2.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX14.0.sdk/System/Library/Frameworks/OpenGL.framework"
  in its INTERFACE_INCLUDE_DIRECTORIES.  Possible reasons include:
  * The path was deleted, renamed, or moved to another location.
  * An install or uninstall procedure did not complete successfully.
  * The installation package was faulty and references files it does not
  provide.
</code></pre>
<h3><a name="p-107043-fix-applied-2" class="anchor" href="#p-107043-fix-applied-2" aria-label="Heading link"></a>Fix applied</h3>
<pre><code class="lang-auto">% pushd /Applications/Xcode-14.2.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/

% sudo ln -s MacOSX.sdk MacOSX14.0.sdk
</code></pre>
<table>
<tbody><tr><th>Before</th><th>After</th></tr>
<tr>
<td>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4efc1ff64e40feb9619104d8ecd1fd95aa141ff6.png" data-download-href="/uploads/short-url/bgJpTDrMLdplofdns4EAIu1o51k.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4efc1ff64e40feb9619104d8ecd1fd95aa141ff6_2_690x128.png" alt="image" data-base62-sha1="bgJpTDrMLdplofdns4EAIu1o51k" width="690" height="128" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4efc1ff64e40feb9619104d8ecd1fd95aa141ff6_2_690x128.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4efc1ff64e40feb9619104d8ecd1fd95aa141ff6_2_1035x192.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4efc1ff64e40feb9619104d8ecd1fd95aa141ff6_2_1380x256.png 2x" data-dominant-color="0E0E0E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1410×262 53.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</td><td>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/feee631dc0daf3780bdd935b89e3f6d5695c3a9a.png" data-download-href="/uploads/short-url/Ane1dyC0gLo8eRqOZ3YI9TAQaPo.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/feee631dc0daf3780bdd935b89e3f6d5695c3a9a_2_690x143.png" alt="image" data-base62-sha1="Ane1dyC0gLo8eRqOZ3YI9TAQaPo" width="690" height="143" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/feee631dc0daf3780bdd935b89e3f6d5695c3a9a_2_690x143.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/feee631dc0daf3780bdd935b89e3f6d5695c3a9a_2_1035x214.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/feee631dc0daf3780bdd935b89e3f6d5695c3a9a_2_1380x286.png 2x" data-dominant-color="100F0F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1433×298 66.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</td>
</tr>
</tbody></table>
<h3><a name="p-107043-analysis-3" class="anchor" href="#p-107043-analysis-3" aria-label="Heading link"></a>Analysis</h3>
<p>Inspecting <code>/Library/Receipts/InstallHistory.plist</code> indicated that XCode was updated to <code>15.2</code> on January 9th, this is consistent with the release date<sup class="footnote-ref"><a href="#footnote-107043-1" id="footnote-ref-107043-1">[1]</a></sup> of XCode 15.2 being January 8th 2024.</p>
<p>Looking at the content of the directory <code>/Applications/Xcode-14.2.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/</code>, we could see that the date at which the symlinks were updated was also <code>January 9th</code>:</p>
<pre><code class="lang-auto">% pushd /Applications/Xcode-14.2.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/

% ls -aslh
total 0
0 drwxr-xr-x  5 root  wheel   160B Jan  9 13:27 .
0 drwxr-xr-x  6 root  wheel   192B Dec 10 23:33 ..
0 drwxr-xr-x  7 root  wheel   224B Nov 13 13:25 MacOSX.sdk
0 lrwxr-xr-x  1 root  wheel    10B Jan  9 13:24 MacOSX14.2.sdk -&gt; MacOSX.sdk
0 lrwxr-xr-x  1 root  wheel    10B Jan  9 13:24 MacOSX14.sdk -&gt; MacOSX.sdk
</code></pre>
<p>We fixed it by creating a new symlink <code>MacOSX14.2.sdk</code> → <code>MacOSX.sdk</code></p>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-107043-1" class="footnote-item"><p><a href="https://xcodereleases.com/">https://xcodereleases.com/</a> <a href="#footnote-ref-107043-1" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---

## Post #5 by @jcfr (2024-02-16 22:45 UTC)

<h2><a name="p-107045-build-of-windows-stable-extensions-1" class="anchor" href="#p-107045-build-of-windows-stable-extensions-1" aria-label="Heading link"></a>Build of Windows Stable extensions</h2>
<p>The build of Windows stable extensions has been restored <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></p>
<p>The fixes applied should address errors like the following:</p>
<pre><code class="lang-auto">7&gt;-- Configuring Scripted module: ValveView
7&gt;-- Configuring Scripted module: Philips4dUsDicomPatcher
7&gt;CMake Error at KretzFileReader/Logic/CMakeLists.txt:1 (project):
7&gt;  The CMAKE_C_COMPILER:
7&gt;
7&gt;    C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.35.32215/bin/Hostx64/x64/cl.exe
7&gt;
7&gt;  is not a full path to an existing compiler tool.
7&gt;
7&gt;CMake Error at KretzFileReader/Logic/CMakeLists.txt:1 (project):
7&gt;  The CMAKE_CXX_COMPILER:
7&gt;
7&gt;    C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.35.32215/bin/Hostx64/x64/cl.exe
7&gt;
7&gt;  is not a full path to an existing compiler tool.
7&gt;
7&gt;-- Configuring incomplete, errors occurred!

</code></pre>
<h3><a name="p-107045-fix-applied-2" class="anchor" href="#p-107045-fix-applied-2" aria-label="Heading link"></a>Fix applied</h3>
<p>Updated the file <code>SlicerConfig.cmake</code> associated with the Stable Slicer build tree applying the following patch:</p>
<pre data-code-wrap="diff"><code class="lang-diff">-set(Slicer_CMAKE_CXX_COMPILER "C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.35.32215/bin/Hostx64/x64/cl.exe")
+set(Slicer_CMAKE_CXX_COMPILER "C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.38.33130/bin/Hostx64/x64/cl.exe")
-set(Slicer_CMAKE_C_COMPILER   "C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.35.32215/bin/Hostx64/x64/cl.exe")
+set(Slicer_CMAKE_C_COMPILER   "C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.38.33130/bin/Hostx64/x64/cl.exe")
[...]
-slicer_config_set_compiler_ep( CMAKE_C_COMPILER   "C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.35.32215/bin/Hostx64/x64/cl.exe"
+slicer_config_set_compiler_ep( CMAKE_C_COMPILER   "C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.38.33130/bin/Hostx64/x64/cl.exe"
   CACHE PATH "Path to C compiler used in Slicer build" FORCE )
-slicer_config_set_compiler_ep( CMAKE_CXX_COMPILER "C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.35.32215/bin/Hostx64/x64/cl.exe"
+slicer_config_set_compiler_ep( CMAKE_CXX_COMPILER "C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.38.33130/bin/Hostx64/x64/cl.exe"
   CACHE PATH "Path to CXX compiler used in Slicer build" FORCE )
</code></pre>
<h3><a name="p-107045-analysis-3" class="anchor" href="#p-107045-analysis-3" aria-label="Heading link"></a>Analysis</h3>
<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="34343">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>It appears that around Tuesday January 30th, during Slicer Project week, there were some changes to the factory build machines.</p>
</blockquote>
</aside>
<p>While attending the 40th Project week, while working on <code>BUG: Ensure packaging of the latest d3dcompiler_47.dll for SlicerVirtualReality</code> (<a href="https://github.com/Slicer/Slicer/pull/7571">PR-7571</a>), on January 30th, we indeed updated Visual Studio.</p>
<p>This is confirmed by the following:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th><code>#ar-in-slicer</code> discord entry</th>
<th>Modified date of directories with installed VS 2022 compilers</th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/eda295d69bc73be657cafc6aed19cac38cb166b6.png" data-download-href="/uploads/short-url/xUduRXnturpfvKc8KgQuz53afqK.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/eda295d69bc73be657cafc6aed19cac38cb166b6_2_690x197.png" alt="image" data-base62-sha1="xUduRXnturpfvKc8KgQuz53afqK" width="690" height="197" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/eda295d69bc73be657cafc6aed19cac38cb166b6_2_690x197.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/eda295d69bc73be657cafc6aed19cac38cb166b6_2_1035x295.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/eda295d69bc73be657cafc6aed19cac38cb166b6.png 2x" data-dominant-color="F7F7F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1132×324 53.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86bce629558574906f383f5704fb690284085f2b.png" data-download-href="/uploads/short-url/jdWH7dNeClWza2JaXDmVhMSO2eL.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86bce629558574906f383f5704fb690284085f2b_2_690x165.png" alt="image" data-base62-sha1="jdWH7dNeClWza2JaXDmVhMSO2eL" width="690" height="165" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86bce629558574906f383f5704fb690284085f2b_2_690x165.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86bce629558574906f383f5704fb690284085f2b_2_1035x247.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86bce629558574906f383f5704fb690284085f2b_2_1380x330.png 2x" data-dominant-color="393941"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2670×642 93 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td>
</tr>
</tbody>
</table>
</div>

---

## Post #6 by @lassoan (2024-02-17 02:55 UTC)

<p>Great, thanks a lot!</p>

---

## Post #7 by @jcfr (2024-02-17 20:45 UTC)

<p>Inspecting <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2024-02-17&amp;filtercount=0&amp;showfilters=1">today’s results</a> confirmed the Stable extensions are built <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></p>

---
