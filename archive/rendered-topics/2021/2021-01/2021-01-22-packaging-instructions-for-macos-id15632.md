# Packaging instructions for macOS

**Topic ID**: 15632
**Date**: 2021-01-22
**URL**: https://discourse.slicer.org/t/packaging-instructions-for-macos/15632

---

## Post #1 by @pll_llq (2021-01-22 15:08 UTC)

<p>Hi,</p>
<p>I’ve successfully built Slicer from source on macOS 11.1 but I am having trouble packaging the app. I’ve tried building with Qt installed from a web-installer and from homebrew.</p>
<p>When I try to package Slicer build with Qt from the web-installer the log shows lots of <code>@rpath</code> errors like</p>
<pre><code class="lang-auto">warning: target '@rpath/QtGui.framework/Versions/5/QtGui' is not absolute...
warning: target '@rpath/QtGui.framework/Versions/5/QtGui' does not exist...
error: /Applications/DevelopmentTools/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/otool-classic: can't open file: @rpath/QtGui.framework/Versions/5/QtGui (No such file or directory)
</code></pre>
<p>and the packaged app doesn’t run on the machine it was built.</p>
<p>When I do the same with the Qt that’s installed from homebrew there are no errors and the app launches on the machine it was built on but when I try to launch the app on a different machine the app crashes with an error saying a library was not loaded/found</p>
<pre><code class="lang-auto">Dyld Error Message:\
  dyld: Using shared cache: 467A83CB-BA86-3F07-B652-B9256C74080A\
Library not loaded: /usr/local/opt/lz4/lib/liblz4.1.dylib\
  Referenced from: /Applications/Slicer.app/Contents/lib/Slicer-4.13/libarchive.17.dylib\
  Reason: image not found\
</code></pre>
<p>The <code>rpath</code> issue was discussed in a number of posts here, like <a href="https://discourse.slicer.org/t/slicer-packaging-qt5-libraries-link/3583">this one</a> and <a href="https://discourse.slicer.org/t/build-error-on-macosx-and-linux-with-itkpython-enabled/3277/18">this one</a> and most important <a href="https://discourse.slicer.org/t/osx-slicer-qt5-packaging-error/1468/6">this one</a></p>
<p>From the forum posts it appears that the only way to create a Slicer (or a Slicelet) for distribution to end-users is to build Qt from source. Is it the only option? Might there be another solution that involves an extra step between building Slicer and running <code>make package</code> in the <code>Slicer-build</code> folder?</p>
<p>Any advice is appreciated.</p>

---

## Post #2 by @lassoan (2021-01-22 15:32 UTC)

<p>Your understanding is correct, it is not practically feasible to create standalone installation packages if you use homebrew. You need to build Qt from source. This is described in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/macos.html#prerequisites">build instructions</a>, but apparently te instructions are not clear enough. Please send a pull request with suggestions for wording changes, which will make things more clear for future developers.</p>

---

## Post #3 by @pll_llq (2021-01-22 17:28 UTC)

<p>Thanks for clarifying this, <a class="mention" href="/u/lassoan">@lassoan</a><br>
I hoped there might be an easier solution like setting some <code>DYLD</code> path or using <code>install_name_tool</code> before packaging.</p>
<hr>
<p>Also, can you explain the following line from the instructions:</p>
<blockquote>
<p>If <code>using Qt from the system</code> , do not forget to add the following CMake variable to your configuration command line: <code>-DSlicer_USE_SYSTEM_QT:BOOL=ON</code></p>
</blockquote>
<p>Does <code>using Qt from the system</code> relate to the use case when Qt was built from source?</p>

---

## Post #4 by @lassoan (2021-01-22 17:55 UTC)

<p>If you want to create installation packages then you need to build Qt yourself and set <code>Slicer_USE_SYSTEM_QT:BOOL=OFF</code>.</p>

---

## Post #5 by @pll_llq (2021-01-22 18:07 UTC)

<p>Thank you very much <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---
