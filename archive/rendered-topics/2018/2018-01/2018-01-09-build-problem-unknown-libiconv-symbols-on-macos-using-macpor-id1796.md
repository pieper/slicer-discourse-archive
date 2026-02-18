# Build problem (unknown _libiconv symbols) on macOS (using MacPorts)

**Topic ID**: 1796
**Date**: 2018-01-09
**URL**: https://discourse.slicer.org/t/build-problem-unknown-libiconv-symbols-on-macos-using-macports/1796

---

## Post #1 by @hmeine (2018-01-09 15:49 UTC)

<p>I am trying to compile Slicer on macOS 10.12.6 with XCode 9.1.  Homebrew is <em>not</em> installed, I am using MacPorts.</p>
<p>My SuperBuild fails in <code>DCMTK-build</code>, with</p>
<blockquote>
<p>[  2%] Linking CXX shared library …/…/lib/libofstd.dylib<br>
Undefined symbols for architecture x86_64:<br>
“_libiconv”, referenced from:<br>
OFCharacterEncoding::Implementation::convert(OFString&amp;, char const*, unsigned long) in ofchrenc.cc.o<br>
“_libiconv_close”, referenced from:<br>
OFCharacterEncoding::Implementation::~Implementation() in ofchrenc.cc.o<br>
“_libiconv_open”, referenced from:<br>
OFCharacterEncoding::Implementation::create(OFString const&amp;, OFString const&amp;, OFCondition&amp;) in ofchrenc.cc.o<br>
“_libiconvctl”, referenced from:<br>
OFCharacterEncoding::Implementation::getConversionFlags() const in ofchrenc.cc.o<br>
OFCharacterEncoding::Implementation::setConversionFlags(unsigned int) in ofchrenc.cc.o<br>
“_locale_charset”, referenced from:<br>
OFCharacterEncoding::Implementation::getLocaleEncoding() in ofchrenc.cc.o<br>
ld: symbol(s) not found for architecture x86_64<br>
clang: error: linker command failed with exit code 1 (use -v to see invocation)<br>
make[5]: *** [lib/libofstd.3.6.2.dylib] Error 1<br>
make[4]: *** [ofstd/libsrc/CMakeFiles/ofstd.dir/all] Error 2<br>
make[3]: *** [all] Error 2<br>
make[2]: *** [DCMTK-prefix/src/DCMTK-stamp/DCMTK-build] Error 2<br>
make[1]: *** [CMakeFiles/DCMTK.dir/all] Error 2</p>
</blockquote>
<p>Does that look familiar to anyone?</p>

---

## Post #2 by @hmeine (2018-01-09 16:08 UTC)

<p><a class="mention" href="/u/ihnorton">@ihnorton</a> suggested that it could be the wrong libiconv (probably from MacPorts) being picked up – that sounds reasonable. I’m investigating.</p>

---

## Post #3 by @hmeine (2018-01-09 16:43 UTC)

<p>Ok, so from <a href="https://issues.slicer.org/view.php?id=2006" rel="nofollow noopener">https://issues.slicer.org/view.php?id=2006</a> I thought that libiconv would not be needed and deactivated.  In CMake, I can see that <code>DCMTK_WITH_ICONV</code> is disabled.</p>
<p>Still, I tried to <code>port deactivate libiconv</code>, confirming that I want to do that despite ~40 packages depend on it, but then CMake was one of these… <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=5" title=":wink:" class="emoji" alt=":wink:"></p>
<p>There’s also a libiconv in /usr (macOS-provided, I assume), which gets picked up first when I enable <code>DCMTK_WITH_ICONV</code>.  Building with <code>DCMTK_WITH_ICONV</code> and either the /usr or the /opt/local (MacPorts) version did not work, either.  (Leading to the exact same linker error.)</p>
<p>So, back to square one: Why am I getting these missing symbols when <code>DCMTK_WITH_ICONV</code> is disabled, as it should be, in the first place?</p>

---

## Post #4 by @hmeine (2018-01-09 18:16 UTC)

<p>More info: I started the SuperBuild with</p>
<blockquote>
<p>cmake \<br>
-DCMAKE_OSX_DEPLOYMENT_TARGET=10.12 \<br>
-DQT_QMAKE_EXECUTABLE=/opt/local/libexec/qt4/bin/qmake \<br>
-DSlicer_USE_PYTHONQT_WITH_TCL=false \<br>
$SRC_DIR</p>
</blockquote>
<p>and Qt is version 4.8.7_5 (although that shouldn’t make a difference for dcmtk, AFAICS).  I also tried a fresh build with <code>CMAKE_OSX_DEPLOYMENT_TARGET=10.11</code>, FWIW.  CMake is 3.10.1.</p>
<p>On <a class="mention" href="/u/che85">@che85</a>’s machine with Sierra, but HomeBrew instead of MacPorts, we managed to compile the same code.</p>

---

## Post #5 by @hmeine (2018-01-10 20:32 UTC)

<p><a class="mention" href="/u/ihnorton">@ihnorton</a> and I debugged this further and ultimately found the culprit:</p>
<p>In the out-of-source build of <code>DCMTK/ofstd/libsrc/ofchrenc.cc</code>, the line</p>
<pre><code class="lang-auto">#include "dcmtk/config/osconfig.h"
</code></pre>
<p>picks up the wrong <code>osconfig.h</code> from <code>/opt/local/include</code> (MacPorts) which has ICONV enabled.</p>
<p>Now one solution would be to disable / remove that dcmtk.  However, I wonder where the include path comes from, which is defined like this:</p>
<pre><code class="lang-auto">set(CMAKE_CXX_TARGET_INCLUDE_PATH
  "/opt/local/include"
  "config/include"
  "/Users/hmeine/Developer/MIC_OSS/Slicer/Slicer-SuperBuild-Debug/DCMTK/ofstd/include"
  "/Users/hmeine/Developer/MIC_OSS/Slicer/Slicer-SuperBuild-Debug/DCMTK/oflog/include"
  "/Users/hmeine/Developer/MIC_OSS/Slicer/Slicer-SuperBuild-Debug/DCMTK/dcmdata/include"
  "/Users/hmeine/Developer/MIC_OSS/Slicer/Slicer-SuperBuild-Debug/DCMTK/dcmimgle/include"
...
</code></pre>
<p>As you can see, the dcmtk build &amp; source directories immediately follow the culprit, so why is that one in front?</p>
<p>Got it! <code>DCMTK_WITH_ICU</code> was enabled! Now I can build. Still, I wonder why this flag leads to the include path being <em>prepended</em> instead of appended after the superbuild-paths.  Maybe someone subscribed to dcmtk lists or involved in dcmtk and its CMake system would like to fix this?</p>

---

## Post #6 by @ihnorton (2018-09-13 14:33 UTC)

<p>Dropping a breadcrumb here so I can find this again next time I need it. Here is the explanation why ICU is not used:</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/pull/976#issuecomment-405286985">https://github.com/Slicer/Slicer/pull/976#issuecomment-405286985</a></li>
<li><a href="https://github.com/commontk/CTK/issues/178">https://github.com/commontk/CTK/issues/178</a></li>
</ul>

---
