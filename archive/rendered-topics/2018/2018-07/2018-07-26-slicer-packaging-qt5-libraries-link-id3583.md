# Slicer packaging Qt5 libraries link

**Topic ID**: 3583
**Date**: 2018-07-26
**URL**: https://discourse.slicer.org/t/slicer-packaging-qt5-libraries-link/3583

---

## Post #1 by @juanprietob (2018-07-26 13:37 UTC)

<p>Operating system: MACOS 10.13.5<br>
Slicer version: 27287<br>
Expected behavior: Launch Slicer<br>
Actual behavior:</p>
<p>I have compiled Slicer r 27287 successfully on MACOS high Sierra 10.13.5<br>
The packaging seems to be working after the following fixes are introduced, otherwise errors such as appear for Qt libraries:</p>
<pre><code>warning: cannot resolve item '@rpath/QtMultimedia.framework/Versions/5/QtMultimedia'

  possible problems:
    need more directories?
    need to use InstallRequiredSystemLibraries?
    run in install tree instead of build tree?
</code></pre>
<p>The fixes are<br>
Before calling configure_file in SlicerCPack.cmake line 140 (this is to get the location of Qt5 libraries):</p>
<pre><code>  get_target_property(Qt5_location Qt5::Widgets LOCATION)
  string(FIND ${Qt5_location} "/QtWidgets" length)
  string(SUBSTRING ${Qt5_location} 0 ${length} Qt5_location)

configure_file(
    "${Slicer_SOURCE_DIR}/CMake/SlicerCPackBundleFixup.cmake.in"
    "${slicer_cpack_bundle_fixup_directory}/SlicerCPackBundleFixup.cmake"
    @ONLY)
</code></pre>
<p>And in the SlicerCPackBundleFixup.cmake.in in line 314 (This is to add the location):</p>
<pre><code>set(libs_path ${libs_path} @Qt5_location@)

fixup_bundle(
    "${app_dir}"
    "${libs}"
    "${libs_path}"
    )
</code></pre>
<p>The following error appears now:</p>
<pre><code>dyld: Library not loaded: @rpath/Frameworks/QtMultimedia.framework/Versions/5/QtMultimedia
  Referenced from: /Users/aaaa/Slicer/Slicer-install/Slicer.app/Contents/MacOS/Slicer
  Reason: no suitable image found.  Did find:
    /Users/aaaa/Slicer/Slicer-install/Slicer.app/Contents/MacOS/../Frameworks/QtMultimedia.framework/Versions/5/QtMultimedia: file too short
[1]    9262 abort      /Users/aaaa/Slicer/Slicer-install/Slicer.app/Contents/MacOS/Slicer
</code></pre>
<p>Does any body know how to fix the packaging?</p>
<p>Thank you in advance.</p>

---

## Post #2 by @Alex_Vergara (2018-07-26 13:51 UTC)

<p>Try this <a href="https://discourse.slicer.org/t/build-error-on-macosx-and-linux-with-itkpython-enabled/3277/19?u=alex_vergara">solution</a></p>

---

## Post #3 by @ihnorton (2018-07-26 14:12 UTC)

<p><a class="mention" href="/u/juanprietob">@juanprietob</a> Qt5 needs to be built with <code>-no-rpath</code> right now. See <a href="https://github.com/jcfr/qt-easy-build/blob/5.10.0/Build-qt.sh#L359-L363">this build script</a>.</p>
<aside class="quote no-group" data-username="Alex_Vergara" data-post="2" data-topic="3583">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>Try this <a href="https://discourse.slicer.org/t/build-error-on-macosx-and-linux-with-itkpython-enabled/3277/19">solution</a></p>
</blockquote>
</aside>
<p>That may work locally, but it is not a solution for packaging; users should not need to set any environment variables.</p>

---
