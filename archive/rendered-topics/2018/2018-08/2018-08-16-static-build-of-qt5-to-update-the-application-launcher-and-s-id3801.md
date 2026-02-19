---
topic_id: 3801
title: "Static Build Of Qt5 To Update The Application Launcher And S"
date: 2018-08-16
url: https://discourse.slicer.org/t/3801
---

# Static build of Qt5 to update the application launcher and support interactive process

**Topic ID**: 3801
**Date**: 2018-08-16
**URL**: https://discourse.slicer.org/t/static-build-of-qt5-to-update-the-application-launcher-and-support-interactive-process/3801

---

## Post #1 by @jcfr (2018-08-16 15:59 UTC)

<h2>Short version</h2>
<p>Help is needed to do a 32-bit static build of Qt5 on Windows. See <strong>link error</strong> at the end of this post.</p>
<p>Indeed, building against a static build of Qt4 is not sufficient anymore because the function <a href="https://doc.qt.io/qt-5/qprocess.html#setInputChannelMode">QProcess::setInputChannelMode</a> added in Qt 5.2 is <a href="https://github.com/commontk/AppLauncher/pull/101/commits/c12cd6e0bc950c80bb7e54d1eaf22327cfe1d715">needed on Windows</a> by the applauncher.</p>
<h2>Long version</h2>
<h3>What is this “interactive support”  ?</h3>
<p>Thanks to the suggestion of <a class="mention" href="/u/ihnorton">@ihnorton</a> and help from <a class="mention" href="/u/lassoan">@lassoan</a>, we recently improved the launcher to support interactive process.</p>
<p>It basically makes the following possible:</p>
<p>before</p>
<pre><code class="lang-auto">macbook-pro:bin inorton$ ./SlicerPython
                              ---&gt; nothing happens, no display or response
^CTraceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
KeyboardInterrupt
</code></pre>
<p>after:</p>
<pre><code class="lang-auto">macbook-pro:bin inorton$ ./SlicerPython
Python 2.7.13 (default, Apr  5 2018, 16:41:55)
[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt;
</code></pre>
<h3>What is the launcher ?</h3>
<p>The launcher is statically built executable allowing to prepare the environment before starting the “real” Slicer executable.</p>
<p>The associated source code is maintained at <a href="https://github.com/commontk/AppLauncher">https://github.com/commontk/AppLauncher</a></p>
<h3>How do you build the launcher ?</h3>
<p>Each time we integrate changes to the <code>master</code> branch or <a href="https://github.com/commontk/AppLauncher#maintainers-how-to-make-a-release-">tag a new release</a>, binaries for Linux, macOS and Windows are automatically uploaded <a href="https://github.com/commontk/AppLauncher/releases">here</a>.</p>
<p>To efficiently support building the launcher statically against a static build of Qt4, we have pre-packaged build tree for the three operating system we support. See <a href="https://github.com/jcfr/qt-static-build">https://github.com/jcfr/qt-static-build</a></p>
<p>We now need to update these and have Qt5 build tree starting with Windows. But we have issue doing so.</p>
<h3>Problem building statically Qt5 on windows ?</h3>
<p>References:</p>
<ul>
<li><a href="https://doc.qt.io/qt-5/windows-requirements.html">https://doc.qt.io/qt-5/windows-requirements.html</a></li>
<li><a href="https://doc.qt.io/qt-5/windows-building.html">https://doc.qt.io/qt-5/windows-building.html</a></li>
</ul>
<p>Step by step</p>
<h4>Step 1: Install Perl to <code>C:\Perl64</code>
</h4>
<ul>
<li>Download from <a href="http://www.activestate.com/activeperl">http://www.activestate.com/activeperl</a>
</li>
<li>Custom install:
<ul>
<li>Disable example and documentation components</li>
<li>Do not create Perl file association</li>
<li>Do not add perl to PATH</li>
</ul>
</li>
</ul>
<h4>Step 2: Open Git Bash and download sources</h4>
<p>Note: we should probably only download <code>qtbase</code> module</p>
<pre><code class="lang-auto">mkdir /c/Qt-static
cd /c/Qt-static
git clone git://github.com/qt/qt5/ --branch v5.11.1 --depth 1 --recursive 5.11.1
</code></pre>
<h4>Step 3: Create <code>C:\Qt-static\qt5vars.cmd</code> and associated desktop shortcut</h4>
<p>Note: we on purpose selected <code>x86</code> so that we have a 32-bit build tree that will allow to create binaries working on both 32-bit and 64-bit windows install.</p>
<pre><code class="lang-auto">REM Set up \Microsoft Visual Studio 2017, where &lt;arch&gt; is \c amd64, \c x86, etc.
REM CALL "C:\Program Files (x86)\Microsoft Visual Studio\2017\Professional\VC\Auxiliary\Build\vcvarsall.bat" x86
CALL "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall.bat" x86
SET _ROOT=C:\Qt-static\5.11.1
SET PATH=%_ROOT%\qtbase\bin;%_ROOT%\gnuwin32\bin;%PATH%
REM Uncomment the below line when using a git checkout of the source repository
SET PATH=%_ROOT%\qtrepotools\bin;%PATH%
SET _ROOT=

SET PATH=C:\Perl64\bin;%PATH%
SET PATH=C:\Python37-x64;%PATH%
</code></pre>
<p>In <code>C:\Qt-static\</code>, create a shortcut link named <code>qt5-shell</code> by specifying the command <code>%SystemRoot%\system32\cmd.exe /E:ON /V:ON /k C:\Qt-static\qt5vars.cmd</code> as application and <code>C:\Qt-static</code> as working directory.</p>
<h4>Step 4: Download jom</h4>
<p>Download <a href="http://download.qt.io/official_releases/jom/jom.zip">http://download.qt.io/official_releases/jom/jom.zip</a> and copy the <code>jom.exe</code> into <code>C:\Qt-static\5.11.1</code></p>
<h4>Step 5: Start terminal using the Desktop link created in a previous step and configure Qt</h4>
<pre><code class="lang-auto">cd C:\Qt-static\5.11.1
configure.bat -platform win32-msvc -release ^
-nomake examples ^
-nomake tests ^
-opensource ^
-confirm-license ^
-static ^
-qt-zlib ^
-qt-pcre ^
-qt-libpng ^
-qt-libjpeg ^
-qt-freetype ^
-no-ssl ^
-no-opengl ^
-skip qt3d ^
-skip qtactiveqt ^
-skip qtandroidextras ^
-skip qtcanvas3d ^
-skip qtcharts ^
-skip qtconnectivity ^
-skip qtdatavis3d ^
-skip qtdeclarative ^
-skip qtdoc ^
-skip qtdocgallery ^
-skip qtenginio ^
-skip qtfeedback ^
-skip qtgamepad ^
-skip qtgraphicaleffects ^
-skip qtimageformats ^
-skip qtlocation ^
-skip qtmacextras ^
-skip qtmultimedia ^
-skip qtnetworkauth ^
-skip qtpim ^
-skip qtpurchasing ^
-skip qtqa ^
-skip qtquickcontrols ^
-skip qtquickcontrols2 ^
-skip qtremoteobjects ^
-skip qtrepotools ^
-skip qtscript ^
-skip qtscxml ^
-skip qtsensors ^
-skip qtserialbus ^
-skip qtserialport ^
-skip qtspeech ^
-skip qtsvg ^
-skip qtsystems ^
-skip qttools ^
-skip qttranslations ^
-skip qtvirtualkeyboard ^
-skip qtwayland ^
-skip qtwebchannel ^
-skip qtwebengine ^
-skip qtwebglplugin ^
-skip qtwebsockets ^
-skip qtwebview ^
-skip qtwinextras ^
-skip qtx11extras ^
-skip qtxmlpatterns

</code></pre>
<h4>Step 6: Build</h4>
<pre><code class="lang-auto">C:\Qt-static\5.11.1&gt; jom

jom 1.1.2 - empower your cores

        cd qtbase\ &amp;&amp; ( if not exist Makefile C:\Qt-static\5.11.1\qtbase\bin\qmake.exe -o Makefile C
:\Qt-static\5.11.1\qtbase\qtbase.pro ) &amp;&amp; C:\Qt-static\5.11.1\jom.exe -f Makefile
        cd src\ &amp;&amp; ( if not exist Makefile C:\Qt-static\5.11.1\qtbase\bin\qmake.exe -o Makefile C:\Q
t-static\5.11.1\qtbase\src\src.pro ) &amp;&amp; C:\Qt-static\5.11.1\jom.exe -f Makefile
        cd corelib\ &amp;&amp; ( if not exist Makefile.qtzlib C:\Qt-static\5.11.1\qtbase\bin\qmake.exe -o Ma
kefile.qtzlib C:\Qt-static\5.11.1\qtbase\src\corelib\qtzlib.pro ) &amp;&amp; C:\Qt-static\5.11.1\jom.exe -f
Makefile.qtzlib

[...]

        C:\Qt-static\5.11.1\jom.exe -f Makefile.Release
        cd sql\ &amp;&amp; ( if not exist Makefile C:\Qt-static\5.11.1\qtbase\bin\qmake.exe -o Makefile C:\Q
t-static\5.11.1\qtbase\src\sql\sql.pro ) &amp;&amp; C:\Qt-static\5.11.1\jom.exe -f Makefile
        C:\Qt-static\5.11.1\jom.exe -f Makefile.Release
        cd 3rdparty\harfbuzz-ng\ &amp;&amp; ( if not exist Makefile C:\Qt-static\5.11.1\qtbase\bin\qmake.exe
 -o Makefile C:\Qt-static\5.11.1\qtbase\src\3rdparty\harfbuzz-ng\harfbuzz-ng.pro ) &amp;&amp; C:\Qt-static\5
.11.1\jom.exe -f Makefile
        C:\Qt-static\5.11.1\jom.exe -f Makefile.Release
        cd tools\uic\ &amp;&amp; ( if not exist Makefile C:\Qt-static\5.11.1\qtbase\bin\qmake.exe -o Makefil
e C:\Qt-static\5.11.1\qtbase\src\tools\uic\uic.pro ) &amp;&amp; C:\Qt-static\5.11.1\jom.exe -f Makefile
        C:\Qt-static\5.11.1\jom.exe -f Makefile.Release
        cd network\ &amp;&amp; ( if not exist Makefile C:\Qt-static\5.11.1\qtbase\bin\qmake.exe -o Makefile
C:\Qt-static\5.11.1\qtbase\src\network\network.pro ) &amp;&amp; C:\Qt-static\5.11.1\jom.exe -f Makefile
        C:\Qt-static\5.11.1\jom.exe -f Makefile.Release
        cd dbus\ &amp;&amp; ( if not exist Makefile C:\Qt-static\5.11.1\qtbase\bin\qmake.exe -o Makefile C:\
Qt-static\5.11.1\qtbase\src\dbus\dbus.pro ) &amp;&amp; C:\Qt-static\5.11.1\jom.exe -f Makefile
        C:\Qt-static\5.11.1\jom.exe -f Makefile.Release
Qt5Core.lib(qstring.obj) : error LNK2019: unresolved external symbol "public: class QFlags&lt;enum QReg
ularExpression::PatternOption&gt; __thiscall QRegularExpression::patternOptions(void)const " (?patternO
ptions@QRegularExpression@@QBE?AV?$QFlags@W4PatternOption@QRegularExpression@@@@XZ) referenced in fu
nction "public: class QString __thiscall QString::section(class QRegularExpression const &amp;,int,int,c
lass QFlags&lt;enum QString::SectionFlag&gt;)const " (?section@QString@@QBE?AV1@ABVQRegularExpression@@HHV
?$QFlags@W4SectionFlag@QString@@@@@Z)
Qt5Core.lib(qstringlist.obj) : error LNK2001: unresolved external symbol "public: class QFlags&lt;enum
QRegularExpression::PatternOption&gt; __thiscall QRegularExpression::patternOptions(void)const " (?patt
ernOptions@QRegularExpression@@QBE?AV?$QFlags@W4PatternOption@QRegularExpression@@@@XZ)
Qt5Core.lib(qstring.obj) : error LNK2019: unresolved external symbol "public: void __thiscall QRegul
arExpression::setPatternOptions(class QFlags&lt;enum QRegularExpression::PatternOption&gt;)" (?setPatternO
ptions@QRegularExpression@@QAEXV?$QFlags@W4PatternOption@QRegularExpression@@@@@Z) referenced in fun
ction "public: class QString __thiscall QString::section(class QRegularExpression const &amp;,int,int,cl
ass QFlags&lt;enum QString::SectionFlag&gt;)const " (?section@QString@@QBE?AV1@ABVQRegularExpression@@HHV?
$QFlags@W4SectionFlag@QString@@@@@Z)
Qt5Core.lib(qstring.obj) : error LNK2019: unresolved external symbol "public: __thiscall QRegularExp
ression::QRegularExpression(class QRegularExpression const &amp;)" (??0QRegularExpression@@QAE@ABV0@@Z)
referenced in function "public: class QString __thiscall QString::section(class QRegularExpression c
onst &amp;,int,int,class QFlags&lt;enum QString::SectionFlag&gt;)const " (?section@QString@@QBE?AV1@ABVQRegula
rExpression@@HHV?$QFlags@W4SectionFlag@QString@@@@@Z)
[...]
</code></pre>
<h2>FAQ</h2>
<h3>How do you create the list of <code>-skip option</code> to give to <code>configure.bat</code> ?</h3>
<p>Copy list of modules from <a href="https://github.com/qt/qt5">https://github.com/qt/qt5</a> into a text file (e.g <code>/tmp/qt-modules.txt</code>):</p>
<pre><code class="lang-auto"> 	qt3d @ 3a3fa5d 	Update submodules on '5.11' in qt5 	a day ago
	qtactiveqt @ e977cfd 	Update submodules on '5.11' in qt5 	13 days ago
[...]
</code></pre>
<p>then run the following command:</p>
<pre><code class="lang-auto">for module in $(cat /tmp/qt-modules.txt  | cut -d"@" -f1 | tr -d "\t" | tr -d " "); do echo "-skip $module ^"; done
</code></pre>
<p>In the command we used, we removed <code>-skip qtbase</code></p>

---

## Post #2 by @lassoan (2018-08-16 16:41 UTC)

<p>Have you tried to build with default options (not skipping any packages)? I’ve noticed that you skipped pcre package and you have an unresolved symbol related to regular expressions - maybe they are related.</p>

---

## Post #3 by @dzenanz (2018-08-16 17:49 UTC)

<p>I have built static Qt in the past, I don’t remember it being much different from regular build.</p>
<p>As <a class="mention" href="/u/lassoan">@lassoan</a> pointed out, you are skipping a whole lot of components. To check whether it is disabling of components or the static build that is causing the error, you could try the same build command except you now remove the <code>-static</code> option.</p>
<p><strong>Edit</strong>: it might also be a consequence of using parallel build tool, which might not honor all inter-module dependencies. I remember running into problems building Qt with <code>/MP</code> option.</p>

---

## Post #4 by @jamesobutler (2018-08-16 22:14 UTC)

<blockquote>
<p>Have you tried to build with default options (not skipping any packages)?</p>
</blockquote>
<p>You actually will have to skip some modules like QtWebEngine if python 3 is being used in the build process as indicated.</p>
<blockquote>
<p>SET PATH=C:\Python37-x64;%PATH%</p>
</blockquote>
<p>QtWebengine requires python &gt;2.7.5 but not python 3.  Unsure if there are any other modules like that.<br>
Plus static builds aren’t supported either.</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://doc.qt.io/qt-5/qtwebengine-platform-notes.html">
  <header class="source">
      <img src="https://d33sqmjvzgs8hq.cloudfront.net/wp-content/themes/oneqt/assets/images/favicon.ico.gzip" class="site-icon" width="" height="">

      <a href="https://doc.qt.io/qt-5/qtwebengine-platform-notes.html" target="_blank" rel="noopener nofollow ugc">doc.qt.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://doc.qt.io/qt-5/qtwebengine-platform-notes.html" target="_blank" rel="noopener nofollow ugc">Qt WebEngine Platform Notes | Qt WebEngine 6.6.1</a></h3>

  <p>Contains information about issues that are specific to the Qt WebEngine module.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @lassoan (2018-08-30 17:07 UTC)

<p>Could we just use a static pre-built Qt, such as this one?</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/martinrotter/qt-minimalistic-builds/releases">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/martinrotter/qt-minimalistic-builds/releases" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/5236277b0b5a657824edcfa9ffd50cb1e718a13ef7a5b8a68fdf3f29621d7cf9/martinrotter/qt-minimalistic-builds" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/martinrotter/qt-minimalistic-builds/releases" target="_blank" rel="noopener">Releases · martinrotter/qt-minimalistic-builds</a></h3>

  <p>Precompiled x64 Qt 5/6 library in minimalistic configuration for Windows. - martinrotter/qt-minimalistic-builds</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @jcfr (2018-08-30 17:24 UTC)

<p>That looks great.</p>
<p>And it seems there are no script to build Qt 5.11 in static with msvc, only Qt 5.10.1 … that is probably why it failed.</p>
<p>Would appreciate if someone could test this script: <a href="https://github.com/martinrotter/qt5-minimalistic-builds/blob/master/msvc-build5101-static.ps1">https://github.com/martinrotter/qt5-minimalistic-builds/blob/master/msvc-build5101-static.ps1</a>  (ideally with VS2015 … which is the version we have available on the factory)</p>

---

## Post #7 by @cpinter (2018-08-30 17:32 UTC)

<p>I started the script but the first issue it runs into is SSL/TLS secure download. I’m investigating</p>

---

## Post #8 by @cpinter (2018-08-30 17:35 UTC)

<p>Update: Had to add</p>
<pre><code>[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
</code></pre>
<p>before line <a href="https://github.com/martinrotter/qt5-minimalistic-builds/blob/master/msvc-build5101-static.ps1#L26">https://github.com/martinrotter/qt5-minimalistic-builds/blob/master/msvc-build5101-static.ps1#L26</a><br>
Now the download is running.</p>

---

## Post #9 by @jcfr (2018-08-30 17:45 UTC)

<p>Nice.</p>
<p>In scikit-ci-addons, we set the following:</p>
<pre><code class="lang-auto">[System.Net.ServicePointManager]::SecurityProtocol = 3072 -bor 768 -bor 192 -bor 48
</code></pre>
<p>See <a href="https://scikit-ci-addons.readthedocs.io/en/latest/addons.html#addressing-the-underlying-connection-was-closed-error">https://scikit-ci-addons.readthedocs.io/en/latest/addons.html#addressing-the-underlying-connection-was-closed-error</a></p>

---

## Post #10 by @cpinter (2018-08-30 18:59 UTC)

<p>The security protocol you mention also works here.</p>
<p>Apparently the script doesn’t run with VS2015. <a class="mention" href="/u/lassoan">@lassoan</a> has VS2017, he’s running it now.</p>

---

## Post #11 by @jcfr (2018-08-30 19:29 UTC)

<p>Thanks for the help.</p>
<p>I also forgot to mention:</p>
<ul>
<li>the build should be done in a 32-bit console. That way we can use the libraries to build a launcher working for both platform and easily support 32-bit tablets.</li>
<li>since usually the archived build tree is not relocatable, the build directory should be something generic enough. Here is what I used for the last build tree <code>C:\D\Support\qt-static-release-i386-4.8.6</code>
</li>
</ul>
<p>After the build is done, it would be ideal to create a release like this one: <a href="https://github.com/jcfr/qt-static-build/releases/tag/4.8.6-vs2008">https://github.com/jcfr/qt-static-build/releases/tag/4.8.6-vs2008</a></p>

---

## Post #12 by @lassoan (2018-08-30 19:58 UTC)

<p>There have been some issues with the build:</p>
<ul>
<li>need to apply Qt patch due to this <a href="https://bugreports.qt.io/browse/QTBUG-69957">bug</a> that affects latest<br>
VS2017 with older Qt versions =&gt; this <a href="https://github.com/qt/qtbase/commit/0ef66e98ccf4946a0e4513ab5fc157df0f0aca4e">patch</a> fixed it</li>
<li>OpenSSL was not detected (even though it was installed at the specified location) =&gt; removing -openssl -openssl-linked flags from msvc-build5101-static.ps1 fixed it</li>
</ul>
<p>The build is still in progress.</p>
<p>Note that <a href="https://github.com/martinrotter/qt5-minimalistic-builds/releases">pre-built static binaries are already available</a>, although it is 64-bit only.</p>

---

## Post #13 by @jcfr (2018-08-30 20:02 UTC)

<blockquote>
<p>need to apply Qt patch</p>
</blockquote>
<p>Good catch</p>
<blockquote>
<p>OpenSSL was not detected</p>
</blockquote>
<p>We don’t need OpenSSL for the launcher. simpler is better</p>
<blockquote>
<p>Note that <a href="https://github.com/martinrotter/qt5-minimalistic-builds/releases">pre-built static binaries are already available</a>, although it is 64-bit only</p>
</blockquote>
<p>Considering we use these launcher for commercial projects, the associated library binaries need to come from a trusted and known party.</p>
<p>Thanks for the help</p>

---

## Post #14 by @lassoan (2018-08-31 04:57 UTC)

<p>I’ve managed to build static Qt 5.10.1 and use it to build a launcher (64-bit, VS2017 toolset) with a couple of changes to <a href="https://github.com/lassoan/qt5-minimalistic-builds/commit/5d170c7ed9273cd5f2c81e7f0c2e75938235d3a5">Qt build</a> and <a href="https://github.com/lassoan/AppLauncher/commit/15ead3cc2a378d496326a1832d8c7ece5f0f5e58">AppLauncher</a>. There were many test errors but Slicer started successfully using this launcher. I haven’t tried to build a 32-bit launcher. It would be great if somebody could take over from here (reproduce the build, determine what is causing test failures, replacing hardcoded paths in CMakeLists.txt, etc).</p>

---

## Post #15 by @lassoan (2018-08-31 14:55 UTC)

<p>I’ve uploaded <a href="https://github.com/lassoan/qt5-minimalistic-builds/commit/1e0a127c4af46fac410c2097d3def4cc5d93c80e">build script and additional patch</a> for building 32-bit static Qt5 launcher using MSVC 2017.</p>
<p>App launcher build completes and the launcher seemingly works but there are many test errors. Maybe there are issues in the test application.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Can you take it over from here? I’m happy to help out but don’t have time to properly work out all the details.</p>

---

## Post #16 by @jcfr (2018-08-31 21:56 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="3801">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Can you take it over from here?</p>
</blockquote>
</aside>
<p>Will do. Thanks a lot for your help, this was very helpful <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #17 by @jcfr (2018-10-13 08:19 UTC)

<p>To follow up on this, updated launcher is available at <a href="https://github.com/commontk/AppLauncher/releases/tag/v0.1.25">https://github.com/commontk/AppLauncher/releases/tag/v0.1.25</a></p>
<p>Script used to generate the 32-bit Qt5 static build used for building the launcher is here: <a href="https://github.com/jcfr/qt5-minimalistic-builds/compare/master...jcfr:add-msvc-build5112-static-x86-applauncher">https://github.com/jcfr/qt5-minimalistic-builds/compare/master...jcfr:add-msvc-build5112-static-x86-applauncher</a></p>
<p>Associated archive is available at <a href="https://github.com/jcfr/qt-static-build/releases/tag/applauncher-5.11.2-vs2017">https://github.com/jcfr/qt-static-build/releases/tag/applauncher-5.11.2-vs2017</a></p>
<p>Finally, the set of flags and list of libraries to specify to ensure the launcher is statically built and the universal C runtime and the C++ standard library are included in the executable is here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/commontk/AppLauncher/blob/68b0ecdb66a90f91b695107aff43a7ddb67a2b95/msvc-static-configure.cmake#L72-L120" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/AppLauncher/blob/68b0ecdb66a90f91b695107aff43a7ddb67a2b95/msvc-static-configure.cmake#L72-L120" target="_blank">commontk/AppLauncher/blob/68b0ecdb66a90f91b695107aff43a7ddb67a2b95/msvc-static-configure.cmake#L72-L120</a></h4>
<pre class="onebox"><code class="lang-cmake"><ol class="start lines" start="72" style="counter-reset: li-counter 71 ;">
<li># Dependencies of QPA plugin needed for running GUI based application</li>
<li># and avoid runtime error: qt.qpa.plugin: Could not find the Qt platform plugin "windows" in ""</li>
<li>set(qt_qpa_plugin_static_libraries</li>
<li>${QT_PREFIX_DIR}/lib/Qt5EventDispatcherSupport.lib</li>
<li>${QT_PREFIX_DIR}/lib/Qt5FontDatabaseSupport.lib</li>
<li>${QT_PREFIX_DIR}/lib/Qt5ThemeSupport.lib</li>
<li>${QT_PREFIX_DIR}/lib/Qt5WindowsUIAutomationSupport.lib</li>
<li>Dwmapi.lib</li>
<li>Imm32.lib</li>
<li>)</li>
<li>set(qt_static_libraries</li>
<li># Qt</li>
<li>${QT_PREFIX_DIR}/lib/qtharfbuzz.lib</li>
<li>${QT_PREFIX_DIR}/lib/qtlibpng.lib</li>
<li>${QT_PREFIX_DIR}/lib/qtpcre2.lib</li>
<li>${QT_PREFIX_DIR}/plugins/platforms/qwindows.lib</li>
<li>${qt_qpa_plugin_static_libraries}</li>
<li># Windows API</li>
<li>Netapi32.lib</li>
<li>OLDNAMES.LIB</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/commontk/AppLauncher/blob/68b0ecdb66a90f91b695107aff43a7ddb67a2b95/msvc-static-configure.cmake#L72-L120" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Useful references are:</p>
<ul>
<li>CRT Library Features: <a href="https://msdn.microsoft.com/en-us/library/abx4dbyh.aspx">https://msdn.microsoft.com/en-us/library/abx4dbyh.aspx</a>
</li>
<li><a href="https://support.microsoft.com/en-us/help/2999226/update-for-universal-c-runtime-in-windows">https://support.microsoft.com/en-us/help/2999226/update-for-universal-c-runtime-in-windows</a></li>
</ul>

---
