---
topic_id: 2576
title: "Compile Errors Pop Os Ubuntu With Qt 5 10"
date: 2018-04-13
url: https://discourse.slicer.org/t/2576
---

# Compile errors Pop!_OS/Ubuntu with Qt 5.10

**Topic ID**: 2576
**Date**: 2018-04-13
**URL**: https://discourse.slicer.org/t/compile-errors-pop-os-ubuntu-with-qt-5-10/2576

---

## Post #1 by @tavaughan (2018-04-13 02:52 UTC)

<p>I built Qt 5.10 as per <a href="https://github.com/jcfr/qt-easy-build/tree/5.10.0#readme" class="inline-onebox" rel="noopener nofollow ugc">GitHub - jcfr/qt-easy-build at 5.10.0</a></p>
<p>I’m now trying to build Slicer, but I get the following compile error:</p>
<blockquote>
<p>[  0%] Generating ui_pqPlayBackEventsDialog.h<br>
/media/vaughan/workspace/lnx/devel/Support/qt-everywhere-build-5.10.0/bin/uic: /usr/lib/x86_64-linux-gnu/libQt5Core.so.5: version `Qt_5.10’ not found (required by /media/vaughan/workspace/lnx/devel/Support/qt-everywhere-build-5.10.0/bin/uic)<br>
CMakeFiles/QtTesting.dir/build.make:257: recipe for target ‘ui_pqPlayBackEventsDialog.h’ failed<br>
make[8]: *** [ui_pqPlayBackEventsDialog.h] Error 1<br>
CMakeFiles/Makefile2:67: recipe for target ‘CMakeFiles/QtTesting.dir/all’ failed<br>
make[7]: *** [CMakeFiles/QtTesting.dir/all] Error 2<br>
Makefile:129: recipe for target ‘all’ failed<br>
make[6]: *** [all] Error 2<br>
CMakeFiles/QtTesting.dir/build.make:110: recipe for target ‘QtTesting-cmake/src/QtTesting-stamp/QtTesting-build’ failed<br>
make[5]: *** [QtTesting-cmake/src/QtTesting-stamp/QtTesting-build] Error 2<br>
CMakeFiles/Makefile2:256: recipe for target ‘CMakeFiles/QtTesting.dir/all’ failed<br>
make[4]: *** [CMakeFiles/QtTesting.dir/all] Error 2<br>
Makefile:129: recipe for target ‘all’ failed<br>
make[3]: *** [all] Error 2<br>
CMakeFiles/CTK.dir/build.make:115: recipe for target ‘CTK-prefix/src/CTK-stamp/CTK-build’ failed<br>
make[2]: *** [CTK-prefix/src/CTK-stamp/CTK-build] Error 2<br>
CMakeFiles/Makefile2:1794: recipe for target ‘CMakeFiles/CTK.dir/all’ failed<br>
make[1]: *** [CMakeFiles/CTK.dir/all] Error 2<br>
Makefile:94: recipe for target ‘all’ failed<br>
make: *** [all] Error 2</p>
</blockquote>
<p>If I had to guess, I’d say that something didn’t build correctly when I built Qt? I can see the file</p>
<blockquote>
<p>/media/vaughan/workspace/lnx/devel/Support/qt-everywhere-build-5.10.0/bin/uic</p>
</blockquote>
<p>I am otherwise confused by</p>
<blockquote>
<p>version `Qt_5.10’ not found</p>
</blockquote>
<p>Any ideas?</p>
<p>–</p>
<p>Clarification: I’m running cmake with:</p>
<blockquote>
<p>cmake -DCMAKE_BUILD_TYPE:STRING=Debug -DQt5_DIR:Path=/media/vaughan/workspace/lnx/devel/Support/qt-everywhere-build-5.10.0/lib/cmake/Qt5 …/S4</p>
</blockquote>

---

## Post #2 by @ihnorton (2018-04-13 13:09 UTC)

<aside class="quote no-group" data-username="tavaughan" data-post="1" data-topic="2576">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tavaughan/48/1475_2.png" class="avatar"> tavaughan:</div>
<blockquote>
<p>/usr/lib/x86_64-linux-gnu/libQt5Core.so.5:</p>
</blockquote>
</aside>
<p>It looks like you are picking up a system Qt installation.</p>

---

## Post #3 by @Davide_Punzo (2018-04-13 13:11 UTC)

<p>Hi Thomas,</p>
<p>I have no issue in compiling in ubuntu 17.10. I don’t know the reason of your error, but I can share my configuration (it may help):</p>
<ol>
<li>I compile with gcc 6.4.0</li>
<li>I used Qt5.10 compiled with the Jc’s qt-easy-build script.</li>
<li>this is the string that I used to configure Slicer:<br>
cmake -DCMAKE_BUILD_TYPE:STRING=Debug -DQt5_DIR=/home/davide/Slicer/Support/qt-everywhere-build-5.10.0/lib/cmake/Qt5 …/Slicer</li>
</ol>
<p>In general I noticed that if you miss -DQt5_DIR variable (and you setup the Qt5 paths later on, e.g. in ccmake), you can have issue.<br>
I hope helps</p>

---

## Post #4 by @Davide_Punzo (2018-04-13 13:17 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="2" data-topic="2576">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>It looks like you are picking up a system Qt installation.</p>
</blockquote>
</aside>
<p>ah yes, I didn’t noticed the paths. Thomas, most likely you need to setup the Qt5 varibale in the cmake</p>

---

## Post #5 by @Leon (2018-04-13 13:18 UTC)

<p>Hi Thomas,</p>
<p>Why should you try to build it on Ubuntu. I just unpacked the tar-file and the I could run Slicer rightaway just from the slicer-file in the folder. Created a extra quicklauncher in the menu.<br>
Done!</p>
<p>p.s. I use LinuxMint (ubuntubased)</p>
<p>Greetings<br>
Léon</p>

---

## Post #6 by @tavaughan (2018-04-13 13:44 UTC)

<p>Thank you Davide and Isaiah,</p>
<p>Good catch. I’m not sure why it would be picking up a system installation. I am running Slicer build with:</p>
<blockquote>
<p>cmake -DCMAKE_BUILD_TYPE:STRING=Debug -DQt5_DIR:Path=/media/vaughan/workspace/lnx/devel/Support/qt-everywhere-build-5.10.0/lib/cmake/Qt5 …/S4<br>
make</p>
</blockquote>
<p>This <em>should</em> work, no?</p>

---

## Post #7 by @Davide_Punzo (2018-04-13 13:47 UTC)

<p>yes, hopefully (<img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"> .<br>
(however, I don’t use the :Path in front of the Qt5_DIR variable)</p>
<p>P.S.: you can also use the -j option with make to speed up.<br>
e.g.: make -j 8</p>

---

## Post #8 by @tavaughan (2018-04-13 13:57 UTC)

<p>Thanks. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> I usually use -j flag, I didn’t use it this time because I want to see the output one line at a time before the build stops.</p>
<p>To be clear, the issue is that I’m running this command:</p>
<blockquote>
<p>cmake -DCMAKE_BUILD_TYPE:STRING=Debug -DQt5_DIR:Path=/media/vaughan/workspace/lnx/devel/Support/qt-everywhere-build-5.10.0/lib/cmake/Qt5 …/S4</p>
</blockquote>
<p>Then make, and the build fails.</p>
<p>Correction: I’m not sure why I wrote Ubuntu 17.10 in the title. I’m actually running Pop!_OS. I think it’s based on Ubuntu 17.10, but it might not be the exact same thing. I’ll correct the title.</p>

---

## Post #9 by @Davide_Punzo (2018-04-13 14:00 UTC)

<p>have you cleaned the previous build?</p>

---

## Post #10 by @tavaughan (2018-04-13 18:18 UTC)

<p>Yes. I deleted everything in the Slicer build directory and ran these commands again to be 100% sure:</p>
<blockquote>
<p>cd S4D<br>
cmake -DCMAKE_BUILD_TYPE:STRING=Debug -DQt5_DIR=/media/vaughan/workspace/lnx/devel/Support/qt-everywhere-build-5.10.0/lib/cmake/Qt5 …/S4<br>
make -j7</p>
</blockquote>
<p>I got the same result.</p>
<p>All the Qt definitions I see in ccmake refer to my Qt build (in /media/vaughan/workspace/lnx/devel/Support/). So I’m not sure what’s going on… whether it’s a configuration problem or something gone weird when I built Qt5. As far as I can tell I haven’t deviated from the usual process.</p>
<p>In case it’s relevant here are the versions of various packages/builds I’m using:</p>
<ul>
<li>GCC: 7.2.0 installed through package manager</li>
<li>Git: 2.14.1</li>
<li>CMake: 3.11.0, built from source with openssl support</li>
<li>Qt: 5.10.0, built using qt-easy-build</li>
<li>Slicer: checked out commit <a href="https://github.com/Slicer/Slicer/commit/6b1f058de4082c920f1ddf3abd61fee01e0b07c9" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/commit/6b1f058de4082c920f1ddf3abd61fee01e0b07c9</a></li>
</ul>

---

## Post #11 by @Davide_Punzo (2018-04-15 12:02 UTC)

<p>sorry no idea, I had not these path issues. Here are my building differences:</p>
<p>gcc 6.4<br>
cmake 3.9.1 from ubuntu repository</p>

---

## Post #12 by @lassoan (2018-04-15 14:32 UTC)

<aside class="quote no-group" data-username="tavaughan" data-post="1" data-topic="2576">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tavaughan/48/1475_2.png" class="avatar"> tavaughan:</div>
<blockquote>
<p>version `Qt_5.10’ not found</p>
</blockquote>
</aside>
<p>These kind of issues seems to be due to ldd picking up system Qt. See for example <a href="https://stackoverflow.com/questions/36128645/error-on-execution-version-qt-5-not-found-required-by" class="inline-onebox">linux - Error on execution -version `Qt_5' not found required by - Stack Overflow</a>.</p>
<p>You can find build script that Slicer nightly builds use here: <a href="https://github.com/Slicer/DashboardScripts" class="inline-onebox">GitHub - Slicer/DashboardScripts: Collection of scripts used to configure/build/test/package 3D Slicer and associated extensions</a></p>

---

## Post #13 by @tavaughan (2018-04-16 01:23 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"> !</p>
<p>I’m not sure where I am supposed to find the build script in the second link you sent. But the links still helped. I can get Slicer to compile now. I ran the following:</p>
<blockquote>
<p>cd S4D<br>
export LD_LIBRARY_PATH=/media/vaughan/workspace/lnx/devel/Support/qt-everywhere-build-5.10.0/lib<br>
export PKG_CONFIG_PATH=/media/vaughan/workspace/lnx/devel/Support/qt-everywhere-build-5.10.0/lib/pkgconfig<br>
export PATH=/media/vaughan/workspace/lnx/devel/Support/qt-everywhere-build-5.10.0/bin:$PATH<br>
cmake -DCMAKE_BUILD_TYPE:STRING=Debug -DQt5_DIR=/media/vaughan/workspace/lnx/devel/Support/qt-everywhere-build-5.10.0/lib/cmake/Qt5 …/S4</p>
</blockquote>
<p>And the rest of the build was ok. <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"> Edit: Though inconvenience that I have to export the LD_LIBRARY_PATH to run Slicer from Terminal.</p>
<p>Normally setting the Qt5_DIR in CMake should be enough though… no?</p>
<p>Edit again: I’m going to try setting the path variable similar to <a href="https://discourse.slicer.org/t/build-failing-in-ctk-on-macos-10-12-slicer-nightly-qt-5-9/2551/17">here</a>.</p>

---

## Post #14 by @Davide_Punzo (2018-04-16 10:05 UTC)

<aside class="quote no-group" data-username="tavaughan" data-post="13" data-topic="2576">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tavaughan/48/1475_2.png" class="avatar"> tavaughan:</div>
<blockquote>
<p>Normally setting the Qt5_DIR in CMake should be enough though… no?</p>
</blockquote>
</aside>
<p>in my experience, yes</p>

---

## Post #15 by @ihnorton (2018-04-16 14:21 UTC)

<aside class="quote no-group" data-username="tavaughan" data-post="13" data-topic="2576">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tavaughan/48/1475_2.png" class="avatar"> tavaughan:</div>
<blockquote>
<p>Normally setting the Qt5_DIR in CMake should be enough though… no?</p>
</blockquote>
</aside>
<p>From the first message, it seems like the problem is higher, at the Qt build level: the <code>uic</code> program is linked against system Qt libraries rather than against the libraries in its build tree:</p>
<blockquote>
<p>/media/vaughan/workspace/lnx/devel/Support/qt-everywhere-build-5.10.0/bin/uic: /usr/lib/x86_64-linux-gnu/libQt5Core.so.5: version `Qt_5.10’ not found (required by <strong>/media/vaughan/workspace/lnx/devel/Support/qt-everywhere-build-5.10.0/bin/uic</strong>)</p>
</blockquote>
<p>So the problem is potentially with Qt or the qt-easy-build discovery process rather than Slicer per se. (but the only thing I can think of is maybe you have LD_LIBRARY_PATH set already, for a Nix or multi-arch configuration? then ld might defer to those during build as in the link from Andras).</p>

---

## Post #16 by @Davide_Punzo (2018-04-17 11:31 UTC)

<p><a class="mention" href="/u/tavaughan">@tavaughan</a>  I just upgraded to ubuntu 18.04 (completely clean installation) and I had the same issue.</p>
<p>Config:</p>
<ul>
<li>GCC 7.3.0</li>
<li>cmake 3.10.2</li>
<li>git 2.17</li>
<li>qt from Jc’s script</li>
</ul>
<p>If I have time I’ll try to donwgrade gcc and see if the linker will work properly.<br>
Setting manually the paths fix the issue as well.</p>

---

## Post #17 by @ihnorton (2018-04-18 02:30 UTC)

<p><a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> <a class="mention" href="/u/tavaughan">@tavaughan</a> when you build with qt-easy-build, do you get QtWebEngine? Did you install anything other than the Slicer prerequisites?</p>
<p>I’ve built on two different systems, and didn’t get QtWebEngine either time. From <a href="https://wiki.qt.io/Building_Qt_5_from_Git#Linux.2FX11">this list</a> it seems I was missing bison, flex, and gperf (at least)… trying again after installing.</p>

---

## Post #18 by @Davide_Punzo (2018-04-18 10:29 UTC)

<p><a class="mention" href="/u/ihnorton">@ihnorton</a>, I had the same issue. I ended up with this post <a href="https://www.ics.com/blog/how-compile-qt-source-code-linux" rel="nofollow noopener">https://www.ics.com/blog/how-compile-qt-source-code-linux</a>. For ubutnu 18.04 I had to change a couple of libraries, but then worked.</p>
<p>In addition, I noticed that I had to do a clean installation to get to compile the webengine (i.e., this workflow was not working: tried to compile, error, installing additional libraries, trying again to compile). It looked like the configuration script was not really looking again.</p>
<p>P.S.: at a cetain point the script print out the configuration building. This is mine after installing all the libraries in the post (and maybe few others) and doing again a clean building of Qt:</p>
<p>Configure summary:</p>
<p>Build type: linux-g++ (x86_64, CPU features: mmx sse sse2)<br>
Configuration: use_gold_linker sse2 aesni sse3 ssse3 sse4_1 sse4_2 avx avx2 avx512f avx512bw avx512cd avx512dq avx512er avx512ifma avx512pf avx512vbmi avx512vl compile_examples enable_new_dtags f16c largefile precompile_header rdrnd shani silent shared release c++11 concurrent dbus reduce_exports reduce_relocations stl<br>
Build options:<br>
Mode … release<br>
Optimize release build for size … no<br>
Building shared libraries … yes<br>
Using C++ standard … C++11<br>
Using ccache … no<br>
Using gold linker … yes<br>
Using new DTAGS … yes<br>
Using precompiled headers … yes<br>
Using LTCG … no<br>
Target compiler supports:<br>
SSE … SSE2 SSE3 SSSE3 SSE4.1 SSE4.2<br>
AVX … AVX AVX2<br>
AVX512 … F ER CD PF DQ BW VL IFMA VBMI<br>
Other x86 … AES F16C RDRAND SHA<br>
Build parts … libs tools<br>
Qt modules and options:<br>
Qt Concurrent … yes<br>
Qt D-Bus … yes<br>
Qt D-Bus directly linked to libdbus … yes<br>
Qt Gui … yes<br>
Qt Network … yes<br>
Qt Sql … yes<br>
Qt Testlib … yes<br>
Qt Widgets … yes<br>
Qt Xml … yes<br>
Support enabled for:<br>
Using pkg-config … yes<br>
QML debugging … yes<br>
udev … yes<br>
Using system zlib … yes<br>
Qt Core:<br>
DoubleConversion … yes<br>
Using system DoubleConversion … no<br>
GLib … yes<br>
iconv … no<br>
ICU … yes<br>
Logging backends:<br>
journald … no<br>
syslog … no<br>
slog2 … no<br>
Using system PCRE2 … no<br>
Qt Network:<br>
getifaddrs() … yes<br>
IPv6 ifname … yes<br>
libproxy … no<br>
OpenSSL … yes<br>
Qt directly linked to OpenSSL … no<br>
SCTP … no<br>
Use system proxies … yes<br>
Qt Gui:<br>
Accessibility … yes<br>
FreeType … yes<br>
Using system FreeType … yes<br>
HarfBuzz … yes<br>
Using system HarfBuzz … yes<br>
Fontconfig … yes<br>
Image formats:<br>
GIF … yes<br>
ICO … yes<br>
JPEG … yes<br>
Using system libjpeg … yes<br>
PNG … yes<br>
Using system libpng … yes<br>
EGL … yes<br>
OpenVG … no<br>
OpenGL:<br>
Desktop OpenGL … yes<br>
OpenGL ES 2.0 … no<br>
OpenGL ES 3.0 … no<br>
OpenGL ES 3.1 … no<br>
OpenGL ES 3.2 … no<br>
Vulkan … no<br>
Session Management … yes<br>
Features used by QPA backends:<br>
evdev … yes<br>
libinput … no<br>
INTEGRITY HID … no<br>
mtdev … no<br>
tslib … no<br>
xkbcommon-evdev … no<br>
QPA backends:<br>
DirectFB … no<br>
EGLFS … yes<br>
EGLFS details:<br>
EGLFS i.Mx6 … no<br>
EGLFS i.Mx6 Wayland … no<br>
EGLFS EGLDevice … yes<br>
EGLFS GBM … no<br>
EGLFS Mali … no<br>
EGLFS Raspberry Pi … no<br>
EGL on X11 … yes<br>
LinuxFB … yes<br>
VNC … yes<br>
Mir client … no<br>
X11:<br>
Using system-provided XCB libraries … yes<br>
EGL on X11 … yes<br>
Xinput2 … yes<br>
XCB XKB … yes<br>
XLib … yes<br>
XCB render … yes<br>
XCB GLX … yes<br>
XCB Xlib … yes<br>
Using system-provided xkbcommon … no<br>
Native painting (experimental) … yes<br>
Qt Widgets:<br>
GTK+ … no<br>
Styles … Fusion Windows<br>
Qt PrintSupport:<br>
CUPS … yes<br>
Qt Sql:<br>
DB2 (IBM) … no<br>
InterBase … no<br>
MySql … no<br>
OCI (Oracle) … no<br>
ODBC … no<br>
PostgreSQL … no<br>
SQLite2 … no<br>
SQLite … yes<br>
Using system provided SQLite … no<br>
TDS (Sybase) … no<br>
Qt SerialBus:<br>
Socket CAN … yes<br>
Socket CAN FD … yes<br>
QtXmlPatterns:<br>
XML schema support … yes<br>
Qt QML:<br>
QML interpreter … yes<br>
QML network support … yes<br>
Qt Quick:<br>
Direct3D 12 … no<br>
AnimatedImage item … yes<br>
Canvas item … yes<br>
Support for Qt Quick Designer … yes<br>
Flipable item … yes<br>
GridView item … yes<br>
ListView item … yes<br>
Path support … yes<br>
PathView item … yes<br>
Positioner items … yes<br>
ShaderEffect item … yes<br>
Sprite item … yes<br>
Qt Gamepad:<br>
SDL2 … no<br>
Qt 3D:<br>
Assimp … yes<br>
System Assimp … no<br>
Output Qt3D Job traces … no<br>
Output Qt3D GL traces … no<br>
Use SSE2 instructions … yes<br>
Use AVX2 instructions … no<br>
Aspects:<br>
Render aspect … yes<br>
Input aspect … yes<br>
Logic aspect … yes<br>
Animation aspect … yes<br>
Extras aspect … yes<br>
Qt 3D GeometryLoaders:<br>
Autodesk FBX … no<br>
Qt Wayland Drivers:<br>
EGL … yes<br>
Raspberry Pi … no<br>
XComposite EGL … yes<br>
XComposite GLX … yes<br>
DRM EGL … yes<br>
libhybris EGL … no<br>
Qt Wayland Client … yes<br>
Qt Wayland Compositor … yes<br>
Qt Bluetooth:<br>
BlueZ … no<br>
BlueZ Low Energy … no<br>
Linux Crypto API … no<br>
WinRT Bluetooth API (desktop &amp; UWP) … no<br>
Qt Sensors:<br>
sensorfw … no<br>
Qt Quick Controls 2:<br>
Styles … Default Fusion Imagine Material Universal<br>
Qt Quick Templates 2:<br>
Hover support … yes<br>
Multi-touch support … yes<br>
Qt Positioning:<br>
Gypsy GPS Daemon … no<br>
WinRT Geolocation API … no<br>
Qt Location:<br>
Geoservice plugins:<br>
OpenStreetMap … yes<br>
HERE … yes<br>
Esri … yes<br>
Mapbox … yes<br>
MapboxGL … no<br>
Itemsoverlay … yes<br>
Qt Multimedia:<br>
ALSA … yes<br>
GStreamer 1.0 … yes<br>
GStreamer 0.10 … no<br>
Video for Linux … yes<br>
OpenAL … no<br>
PulseAudio … yes<br>
Resource Policy (libresourceqt5) … no<br>
Windows Audio Services … no<br>
DirectShow … no<br>
Windows Media Foundation … no<br>
Qt WebEngine:<br>
Embedded build … no<br>
Pepper Plugins … yes<br>
Printing and PDF … yes<br>
Proprietary Codecs … no<br>
Spellchecker … yes<br>
Native Spellchecker … no<br>
WebRTC … yes<br>
Use System Ninja … yes<br>
Geolocation … yes<br>
Use ALSA … yes<br>
Use PulseAudio … yes<br>
Optional system libraries used:<br>
re2 … no<br>
icu … no<br>
libwebp, libwebpmux and libwebpdemux . yes<br>
opus … yes<br>
ffmpeg … no<br>
libvpx … no<br>
snappy … no<br>
libsrtp … no<br>
glib … yes<br>
zlib … yes<br>
minizip … yes<br>
libevent … yes<br>
jsoncpp … yes<br>
protobuf … no<br>
libxml2 and libxslt … yes<br>
lcms2 … no<br>
png … yes<br>
harfbuzz … yes<br>
Required system libraries:<br>
fontconfig … yes<br>
dbus … yes<br>
nss … yes<br>
khr … yes<br>
glibc … yes<br>
Required system libraries for qpa-xcb:<br>
libdrm … yes<br>
xcomposite … yes<br>
xcursor … yes<br>
xi … yes<br>
xrandr … yes<br>
xtst … yes</p>

---

## Post #19 by @Davide_Punzo (2018-04-18 10:30 UTC)

<p>I guess that for Webengine these are the important ones:</p>
<aside class="quote no-group" data-username="Davide_Punzo" data-post="18" data-topic="2576">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar"> Davide_Punzo:</div>
<blockquote>
<p>Required system libraries:</p>
<p>fontconfig … yes</p>
<p>dbus … yes</p>
<p>nss … yes</p>
<p>khr … yes</p>
<p>glibc … yes</p>
<p>Required system libraries for qpa-xcb:</p>
<p>libdrm … yes</p>
<p>xcomposite … yes</p>
<p>xcursor … yes</p>
<p>xi … yes</p>
<p>xrandr … yes</p>
<p>xtst … yes</p>
</blockquote>
</aside>

---

## Post #20 by @ihnorton (2018-04-18 14:36 UTC)

<p>Thanks. The set of dependencies from the ICS link seems to have done it. Now I get a listing for WebEngine in the configure output. Unfortunately as far as I can tell there is no way to make ./configure fail fast if webengine won’t be built (<a href="https://github.com/jcfr/qt-easy-build/issues/40">https://github.com/jcfr/qt-easy-build/issues/40</a>).</p>

---

## Post #21 by @tavaughan (2018-04-19 05:56 UTC)

<p>I now have Slicer building and running without fiddling with LD_LIBRARY_PATH. I think the issue was with the Build-qt.sh script.</p>
<p>Steps:</p>
<ol>
<li>Install Qt dependencies (for QtWebEngine-specific dependencies I referred to this page <a href="https://wiki.qt.io/QtWebEngine/How_to_Try" class="inline-onebox" rel="noopener nofollow ugc">QtWebEngine/How to Try - Qt Wiki</a> )</li>
<li>Download the Qt-build script as per <a href="https://github.com/jcfr/qt-easy-build/tree/5.10.0#readme" class="inline-onebox" rel="noopener nofollow ugc">GitHub - jcfr/qt-easy-build at 5.10.0</a></li>
<li>Open the script in a text editor. Scroll to the configure step near the end of the file (line 365 at time of writing). Change the -no-rpath option to -rpath. I changed:</li>
</ol>
<blockquote>
<p>./configure $qt_install_dir_options <br>
[stuff]<br>
-no-rpath \</p>
</blockquote>
<p>to:</p>
<blockquote>
<p>./configure $qt_install_dir_options <br>
[stuff]<br>
-rpath \</p>
</blockquote>
<p><em>Note: I suspect simply removing the -rpath line would have the same result as removing it completely. I am not 100% sure of this though.</em></p>
<ol start="4">
<li>Run the Qt-build script. It takes a while so I just left it overnight.</li>
<li>Download and install Slicer dependencies as indicated on build instructions page: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Ubuntu" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/Build Instructions - Slicer Wiki</a></li>
<li>Download Slicer source files.</li>
<li>Create a script that has contents like the following:</li>
</ol>
<blockquote>
<p>cd S4D<br>
cmake <br>
-DQT_QMAKE_EXECUTABLE:FILEPATH=/media/vaughan/workspace/lnx/devel/Support/qt-everywhere-build-5.10.0/bin/qmake <br>
-DQt5_DIR=/media/vaughan/workspace/lnx/devel/Support/qt-everywhere-build-5.10.0/lib/cmake/Qt5 <br>
-DCMAKE_BUILD_TYPE:STRING=Debug <br>
-DCMAKE_PREFIX_PATH:PATH=/media/vaughan/workspace/lnx/devel/Support/qt-everywhere-build-5.10.0/bin/ <br>
-DSlicer_USE_PYTHONQT_WITH_TCL:BOOL=OFF <br>
-DSlicer_USE_SimpleITK:BOOL=OFF <br>
-DSlicer_USE_QtTesting:BOOL=OFF <br>
-DSlicer_VTK_VERSION_MAJOR:STRING=9 <br>
-DSlicer_VTK_RENDERING_BACKEND:STRING=OpenGL2 <br>
-DSlicer_BUILD_DataStore:BOOL=OFF <br>
…/S4<br>
make -j7</p>
</blockquote>
<p>Make sure to set your Qt directories to wherever you built it.</p>
<ol start="8">
<li>Run script. Like Qt, this will take a while.</li>
</ol>
<p>With any luck, Slicer should build correctly. After doing these steps I do not need to run any export LD_LIBRARY_PATH commands.</p>
<p>I created an issue on GitHub for discussion: <a href="https://github.com/jcfr/qt-easy-build/issues/42" class="inline-onebox" rel="noopener nofollow ugc">Ld trying to use system install of Qt5 · Issue #42 · jcfr/qt-easy-build · GitHub</a></p>

---
