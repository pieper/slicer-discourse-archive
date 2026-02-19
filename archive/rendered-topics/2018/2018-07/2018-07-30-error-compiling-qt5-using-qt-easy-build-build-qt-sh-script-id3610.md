---
topic_id: 3610
title: "Error Compiling Qt5 Using Qt Easy Build Build Qt Sh Script"
date: 2018-07-30
url: https://discourse.slicer.org/t/3610
---

# Error compiling Qt5 using qt-easy-build/Build-qt.sh script

**Topic ID**: 3610
**Date**: 2018-07-30
**URL**: https://discourse.slicer.org/t/error-compiling-qt5-using-qt-easy-build-build-qt-sh-script/3610

---

## Post #1 by @mschumaker (2018-07-30 15:01 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a><br>
I’m attempting to build Qt5.10.0 using the qt-easy-build/Build-qt.sh script to deal with the rpath issue with packaging Slicer on Mac, but it fails. Help?<br>
Operating system is MacOS 10.12. Xcode 9.2<br>
The Xcode installation doesn’t have the 10.12 sdk, it has 10.13.</p>
<p>Command line: ./Build-qt.sh -d 10.12 -s macosx10.13 -j 4</p>
<p>Error:</p>
<blockquote>
<p>compiling qwebview_darwin.mm<br>
qwebview_darwin.mm:261:24: error: ‘loadFileURL:allowingReadAccessToURL:’ is only available on macOS 10.11 or newer<br>
[-Werror,-Wunguarded-availability]<br>
[wkWebView loadFileURL:url.toNSURL()<br>
^~~~~~~~~~~~~~~~~~~~~~~~~<br>
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk/System/Library/Frameworks/WebKit.framework/Headers/WKWebView.h:102:1: note:<br>
‘loadFileURL:allowingReadAccessToURL:’ has been explicitly marked partial here<br>
- (nullable WKNavigation *)loadFileURL:(NSURL *)URL allowingReadAccessToURL:(NSURL *)readAccessURL API_AVAILABLE(macosx…<br>
^<br>
qwebview_darwin.mm:261:24: note: enclose ‘loadFileURL:allowingReadAccessToURL:’ in an <span class="mention">@available</span> check to silence this warning<br>
[wkWebView loadFileURL:url.toNSURL()<br>
^~~~~~~~~~~~~~~~~~~~~~~~~<br>
1 error generated.<br>
make[3]: *** [.obj/qwebview_darwin.o] Error 1<br>
make[2]: *** [sub-webview-make_first] Error 2<br>
make[1]: *** [sub-src-make_first] Error 2<br>
make: *** [module-qtwebview-make_first] Error 2</p>
</blockquote>
<p>Thanks for any assistance.</p>

---

## Post #2 by @ihnorton (2018-07-30 16:10 UTC)

<p>That’s supposed to be fixed in 5.10.1, see: <a href="https://bugreports.qt.io/browse/QTBUG-65075">https://bugreports.qt.io/browse/QTBUG-65075</a><br>
5.10.1 should be a clean upgrade in qt-easy-build, just change the version and the MD5 sum.</p>
<p>(<s>or, alternatively and less than ideal: remove <code>-Werror</code> in the compiler command line options</s> actually, that’s buried in the qt build scripts, which are fairly confusing. It will probably be much easier to upgrade the version)</p>

---

## Post #3 by @mschumaker (2018-07-30 16:21 UTC)

<p>Ok, thanks. Has it been tested for 5.11?</p>

---

## Post #4 by @ihnorton (2018-07-30 17:56 UTC)

<aside class="quote no-group" data-username="mschumaker" data-post="3" data-topic="3610">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p>Has it been tested for 5.11?</p>
</blockquote>
</aside>
<p>Slicer is known to build against 5.11, as that’s the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Linux">recommendation on Linux</a>. I don’t know if qt-easy-build has been tested against 5.11.</p>

---

## Post #5 by @mschumaker (2018-07-30 19:33 UTC)

<p>Ok, 5.11.1 didn’t compile. I’ll try 5.10.1.<br>
The error:</p>
<blockquote>
<p>In file included from main.cpp:19:<br>
In file included from …/…/3rdparty/chromium/base/at_exit.h:9:<br>
In file included from …/…/3rdparty/chromium/base/callback.h:9:<br>
In file included from …/…/3rdparty/chromium/base/callback_internal.h:14:<br>
…/…/3rdparty/chromium/base/memory/ref_counted.h:155:5: warning: use of this statement in a constexpr constructor is a C++14<br>
extension [-Wc++14-extensions]<br>
needs_adopt_ref_ = true;<br>
^<br>
linking …/…/lib/QtWebEngineCore.framework/Versions/5/Helpers/QtWebEngineProcess.app/Contents/MacOS/QtWebEngineProcess<br>
In file included from main.cpp:20:<br>
In file included from …/…/3rdparty/chromium/base/files/file_path.h:115:<br>
…/…/3rdparty/chromium/base/strings/string_piece.h:226:18: warning: ‘constexpr’ non-static member function will not be<br>
implicitly ‘const’ in C++14; add ‘const’ to avoid a change in behavior [-Wconstexpr-not-const]<br>
constexpr void remove_prefix(size_type n) {<br>
^<br>
const<br>
…/…/3rdparty/chromium/base/strings/string_piece.h:231:18: warning: ‘constexpr’ non-static member function will not be<br>
implicitly ‘const’ in C++14; add ‘const’ to avoid a change in behavior [-Wconstexpr-not-const]<br>
constexpr void remove_suffix(size_type n) { length_ -= n; }<br>
^<br>
const<br>
…/…/3rdparty/chromium/base/strings/string_piece.h:226:18: error: constexpr function’s return type ‘void’ is not a literal<br>
type<br>
constexpr void remove_prefix(size_type n) {<br>
^<br>
…/…/3rdparty/chromium/base/strings/string_piece.h:231:18: error: constexpr function’s return type ‘void’ is not a literal<br>
type<br>
constexpr void remove_suffix(size_type n) { length_ -= n; }<br>
^<br>
compiling …/…/include/QtWebEngine/QtWebEngineDepends<br>
143 warnings and 7 errors generated.<br>
make[3]: *** [.obj/main.o] Error 1<br>
make[2]: *** [sub-tools-qwebengine_convert_dict-make_first] Error 2</p>
</blockquote>

---

## Post #6 by @mschumaker (2018-07-30 21:51 UTC)

<p>Qt 5.10.1 compiled successfully using the script.<br>
For reference, the MD5sum for Qt 5.10.1 is 7e167b9617e7bd64012daaacb85477af</p>
<p>Thanks!</p>

---

## Post #7 by @jcfr (2018-07-31 03:05 UTC)

<p>Thanks <a class="mention" href="/u/mschumaker">@mschumaker</a></p>
<p>Could you submit a PR to update <a href="https://github.com/jcfr/qt-easy-build/tree/5.10.0">https://github.com/jcfr/qt-easy-build/tree/5.10.0</a> ?</p>

---
