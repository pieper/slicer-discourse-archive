# Opening extension manager makes Slicer crash on Linux

**Topic ID**: 7589
**Date**: 2019-07-15
**URL**: https://discourse.slicer.org/t/opening-extension-manager-makes-slicer-crash-on-linux/7589

---

## Post #1 by @APF (2019-07-15 13:27 UTC)

<p>Operating system: Linux 4.15.0-50-generic <span class="hashtag">#54-Ubuntu</span> SMP Mon May 6 18:46:08 UTC 2019<br>
Slicer version: Slicer-4.10.2-linux-amd64</p>
<p>This problem occurs when I try to open the extension manager by clicking the button “Install Slicer Extensions”</p>
<p>Expected behavior: Be able to browse and install extensions within the extension manager<br>
Actual behavior: Opens a new window named “Extension Manager” loading a bunch of things, then all windows close.</p>
<p>Note: This only happens when connected to internet. When not connected. The window “Extension Manager” shows up written “No internet connection” and remains. No crash.</p>
<p>What I’ve tried: Reinstalling the same version of Slicer. No difference. Tried messing with my connection, but it seems that no matter what I do I cannot have an internet connection and the extension manager open with other than “No internet connection” screen. I’ve looked at this : <a href="https://discourse.slicer.org/t/nightly-slicer-crashes-trying-to-open-extension-manager/4005/2" class="inline-onebox">Nightly Slicer crashes trying to open Extension Manager</a> but haven’t found any file named <code>Slicer.ini</code> in my install.</p>
<p>Stack trace:</p>
<pre><code class="lang-auto">soft/Slicer-4.10.2-linux-amd64/Slicer 
Switch to module:  "Welcome"
An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.
[0715/111643.154822:WARNING:stack_trace_posix.cc(699)] Failed to open file: /home/apfauwadel/#16654149 (deleted)
  Error: No such file or directory
Received signal 11 SEGV_MAPERR 7fdc00000000
#0 0x7fddee93d52f &lt;unknown&gt;
#1 0x7fdded36eb1d &lt;unknown&gt;
#2 0x7fddee93da3e &lt;unknown&gt;
#3 0x7fdde2949890 &lt;unknown&gt;
#4 0x7fddccee7207 __libc_malloc
#5 0x7fddcd4ec258 operator new()
#6 0x7fddeddcae8e &lt;unknown&gt;
#7 0x7fddf3dec731 QtWebEngineCore::RenderWidgetHostViewQtDelegateWidget::resizeEvent()
#8 0x7fddd897be22 QWidget::event()
#9 0x7fddcc2b7b2b QQuickWidget::event()
#10 0x7fddf3dec946 QtWebEngineCore::RenderWidgetHostViewQtDelegateWidget::event()
#11 0x7fddd893ee2c QApplicationPrivate::notify_helper()
#12 0x7fddd8945f60 QApplication::notify()
#13 0x7fddf65eb9dc qSlicerApplication::notify()
#14 0x7fddd7aef2d8 QCoreApplication::notifyInternal2()
#15 0x7fddd897340e QWidgetPrivate::setGeometry_sys()
#16 0x7fddd89740d0 QWidget::setGeometry()
#17 0x7fddd895df2c QWidgetItem::setGeometry()
#18 0x7fddd8954278 QBoxLayout::setGeometry()
#19 0x7fddd895a48b QLayoutPrivate::doResize()
#20 0x7fddd893edfa QApplicationPrivate::notify_helper()
#21 0x7fddd8945f60 QApplication::notify()
#22 0x7fddf65eb9dc qSlicerApplication::notify()
#23 0x7fddd7aef2d8 QCoreApplication::notifyInternal2()
#24 0x7fddd897340e QWidgetPrivate::setGeometry_sys()
#25 0x7fddd89740d0 QWidget::setGeometry()
#26 0x7fddd895df2c QWidgetItem::setGeometry()
#27 0x7fddd8954278 QBoxLayout::setGeometry()
#28 0x7fddd895a48b QLayoutPrivate::doResize()
#29 0x7fddd895b4a0 QLayout::activate()
#30 0x7fddd893edfa QApplicationPrivate::notify_helper()
#31 0x7fddd8945f60 QApplication::notify()
#32 0x7fddf65eb9dc qSlicerApplication::notify()
#33 0x7fddd7aef2d8 QCoreApplication::notifyInternal2()
#34 0x7fddd7af1ceb QCoreApplicationPrivate::sendPostedEvents()
#35 0x7fddd7b43d93 postEventSourceDispatch()
#36 0x7fddcc726417 g_main_context_dispatch
#37 0x7fddcc726650 &lt;unknown&gt;
#38 0x7fddcc7266dc g_main_context_iteration
#39 0x7fddd7b433ff QEventDispatcherGlib::processEvents()
#40 0x7fddc27c00d1 QPAEventDispatcherGlib::processEvents()
#41 0x7fddd7aedc3a QEventLoop::exec()
#42 0x7fddd8b1bb37 QDialog::exec()
#43 0x7fddf65ec084 qSlicerApplication::openExtensionsManagerDialog()
#44 0x7fddf6680c85 qSlicerApplication::qt_static_metacall()
#45 0x7fddd7b1a189 QMetaObject::activate()
#46 0x7fddd8a233a2 QAbstractButton::clicked()
#47 0x7fddd8a235a4 QAbstractButtonPrivate::emitClicked()
#48 0x7fddd8a2513e QAbstractButtonPrivate::click()
#49 0x7fddd8a25295 QAbstractButton::mouseReleaseEvent()
#50 0x7fddd897b688 QWidget::event()
#51 0x7fddd893ee2c QApplicationPrivate::notify_helper()
#52 0x7fddd8946a13 QApplication::notify()
#53 0x7fddf65eb9dc qSlicerApplication::notify()
#54 0x7fddd7aef2d8 QCoreApplication::notifyInternal2()
#55 0x7fddd894550f QApplicationPrivate::sendMouseEvent()
#56 0x7fddd89951dd QWidgetWindow::handleMouseEvent()
#57 0x7fddd8997ae3 QWidgetWindow::event()
#58 0x7fddd893ee2c QApplicationPrivate::notify_helper()
#59 0x7fddd8945f60 QApplication::notify()
#60 0x7fddf65eb9dc qSlicerApplication::notify()
#61 0x7fddd7aef2d8 QCoreApplication::notifyInternal2()
</code></pre>

---

## Post #2 by @APF (2019-07-15 14:37 UTC)

<p>(can’t find the edit button anymore)</p>
<p>I’ve tried with Slicer <code>4.11.0-2019-07-13-linux-amd64</code> as well, with no success.</p>

---

## Post #3 by @pieper (2019-07-15 14:55 UTC)

<p>Interesting - thanks for the report.  I suspect this is some kind of Qt/Linux interaction.  On my linux machine I get the same warning about the Core Profile not supported and the same stack_trace_posix warning, but then I do not get the crash (the Extension Manager window and everything else works as expected).</p>
<p>I tested both 4.10.2 and today’s nightly on ubuntu 18.04.</p>

---

## Post #4 by @lassoan (2019-07-15 15:03 UTC)

<aside class="quote no-group" data-username="APF" data-post="1" data-topic="7589">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/3da27b/48.png" class="avatar"> APF:</div>
<blockquote>
<p>haven’t found any file named <code>Slicer.ini</code> in my install</p>
</blockquote>
</aside>
<p>Slicer.ini is in your profile folder. You can get your Slicer.ini path by running:</p>
<pre><code>./Slicer --settings-path
</code></pre>
<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="7589">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I get the same warning about the Core Profile not supported</p>
</blockquote>
</aside>
<p>We had to enable compatibility profile for Windows by default. Maybe we would need to enable it for Linux, too. Could you please try if things improve if you enable compatibility profile by setting <code>SLICER_OPENGL_PROFILE</code> environment variable to <code>compatibility</code> before launching Slicer? Does the warning still appear? Does the web browser still crash?</p>
<p>If all else fails, you can download extensions and install them manually (with internet disconnected) as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager">here</a>.</p>
<aside class="quote no-group" data-username="APF" data-post="2" data-topic="7589">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/3da27b/48.png" class="avatar"> APF:</div>
<blockquote>
<p>(can’t find the edit button anymore)</p>
</blockquote>
</aside>
<p>Editing of forum posts is limited to a certain time limit to avoid spammers to inject malicious URLs into their posts after discussion is no longer active.</p>

---

## Post #5 by @APF (2019-07-15 15:16 UTC)

<p>Thank you for your replies.</p>
<p>After deleting the Slicer.ini file, I get pretty much the same error again :</p>
<pre><code class="lang-auto">~/soft/Slicer-4.10.2-linux-amd64$ ./Slicer
Switch to module:  "Welcome"
An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.
[0715/171141.426489:WARNING:stack_trace_posix.cc(699)] Failed to open file: /home/apfauwadel/#16654229 (deleted)
  Error: No such file or directory
nouveau: kernel rejected pushbuf: No such file or directory
nouveau: ch8: krec 0 pushes 0 bufs 1 relocs 0
nouveau: ch8: buf 00000000 00000002 00000004 00000004 00000000
SlicerApp-real: ../nouveau/pushbuf.c:723: nouveau_pushbuf_data: Assertion `kref' failed.
Received signal 6
#0 0x7f341476952f &lt;unknown&gt;
#1 0x7f341319ab1d &lt;unknown&gt;
#2 0x7f3414769a3e &lt;unknown&gt;
#3 0x7f3408775890 &lt;unknown&gt;
#4 0x7f33f2cbae97 gsignal
#5 0x7f33f2cbc801 abort
#6 0x7f33f2cac39a &lt;unknown&gt;
#7 0x7f33f2cac412 __assert_fail
#8 0x7f33e4fdb9ad nouveau_pushbuf_data
#9 0x7f33e4fdb966 nouveau_pushbuf_data
#10 0x7f33e4fdba3f &lt;unknown&gt;
#11 0x7f33e4fdbeaf &lt;unknown&gt;
#12 0x7f33e4fdca40 nouveau_pushbuf_kick
#13 0x7f33e5a85186 &lt;unknown&gt;
#14 0x7f33e568bb8b &lt;unknown&gt;
#15 0x7f33e585020a &lt;unknown&gt;
#16 0x7f33e7422d88 &lt;unknown&gt;
#17 0x7f33e7874db2 QGLXContext::swapBuffers()
#18 0x7f33fdf83b3c QOpenGLContext::swapBuffers()
#19 0x7f33fe1eebeb QPlatformBackingStore::composeAndFlush()
#20 0x7f33e856fd0f QXcbBackingStore::composeAndFlush()
#21 0x7f33fe776faa QWidgetBackingStore::qt_flush()
#22 0x7f33fe7783c1 QWidgetBackingStore::flush()
#23 0x7f33fe77a0d0 QWidgetBackingStore::doSync()
#24 0x7f33fe77a300 QWidgetBackingStore::sync()
#25 0x7f33fe7908df QWidgetPrivate::syncBackingStore()
#26 0x7f33fe7a7790 QWidget::event()
#27 0x7f33fe76ae2c QApplicationPrivate::notify_helper()
#28 0x7f33fe771f60 QApplication::notify()
#29 0x7f341c4179dc qSlicerApplication::notify()
#30 0x7f33fd91b2d8 QCoreApplication::notifyInternal2()
#31 0x7f33fe77aa5d QWidgetBackin
</code></pre>

---

## Post #6 by @lassoan (2019-07-15 15:27 UTC)

<aside class="quote no-group" data-username="APF" data-post="5" data-topic="7589">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/3da27b/48.png" class="avatar"> APF:</div>
<blockquote>
<p>nouveau: kernel rejected pushbuf: No such file or directory</p>
</blockquote>
</aside>
<p>This seems to be a crash in Nouveau display driver (see for example <a href="https://bugs.launchpad.net/oxide/+bug/1499419">here</a>, but there are many other similar reports). Could you try to switch graphic driver (e.g., to one provided by nVidia)?</p>
<p>Does setting of <code>SLICER_OPENGL_PROFILE</code> to <code>compatibility</code> make any difference?</p>

---

## Post #7 by @APF (2019-07-16 09:35 UTC)

<p>Setting of <code>SLICER_OPENGL_PROFILE</code> to <code>compatibility</code> does not seem to make any difference. Actually, the last stack trace I’ve provided is with <code>SLICER_OPENGL_PROFILE</code> set to <code>compatibility</code>, and without <code>Slicer.ini</code> as well. I’ve tried just setting the variable to <code>compatibility</code> without deleting <code>Slicer.ini</code>, it didn’t change anything either.</p>
<p>I’m working on the display driver switch.</p>

---

## Post #8 by @PaoloZaffino (2019-07-16 10:16 UTC)

<p>Same problem here (Arch linux)</p>

---

## Post #9 by @lassoan (2019-07-16 11:53 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Does setting <code>SLICER_OPENGL_PROFILE</code> to <code>compatibility</code> make the core profile warning disappear for you?</p>
<aside class="quote no-group" data-username="PaoloZaffino" data-post="8" data-topic="7589" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/paolozaffino/48/81052_2.png" class="avatar"> PaoloZaffino:</div>
<blockquote>
<p>Same problem here (Arch linux)</p>
</blockquote>
</aside>
<p>Do you mean that you have OpenGL core profile warning on application startup, or extension manager crash (potentially due to incompatible display driver)?</p>

---

## Post #10 by @pieper (2019-07-16 13:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="7589">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Does setting <code>SLICER_OPENGL_PROFILE</code> to <code>compatibility</code> make the core profile warning disappear for you?</p>
</blockquote>
</aside>
<p>No difference.  I also tried the <code>no</code> and <code>core</code> options but always get the same result.  (Something else is odd today with those <code>Operation canceled</code> messages, but they also appear on mac so probably unrelated to this issue).  The extension manager operates normally for me in spite of these messages.</p>
<pre><code class="lang-auto">$ SLICER_OPENGL_PROFILE=compatibility ./Slicer-4.10.2-linux-amd64/Slicer 
Switch to module:  "Welcome"
Loading Slicer RC file [/home/pieper/.slicerrc.py]
Segmentation nodes will be stored uncompressed by default
An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.
[0716/091617.790781:WARNING:stack_trace_posix.cc(699)] Failed to open file: /home/pieper/#29148638 (deleted)
  Error: No such file or directory

DevTools listening on ws://127.0.0.1:1337/devtools/browser/2271ba07-bbe5-4039-83e1-d0ea424e8e40
Remote debugging server started successfully. Try pointing a Chromium-based browser to http://127.0.0.1:1337
"{6bb547eb-0a4f-4952-bd43-c66ca0631563}: 5: Operation canceled"
"{9c2f679b-863d-425f-ba5d-a3c9aaf41bac}: 5: Operation canceled"
"{1f692201-84bc-420d-b312-1bb68b2b24bd}: 5: Operation canceled"
"{5f96d5e8-fc98-40d3-8d23-8d64541ce9c9}: 5: Operation canceled"
"{12ddc7e1-0382-495c-89ff-389a21e866d8}: 5: Operation canceled"
"{eac26abb-1e9f-4d82-90cd-a3f8ef1419a0}: 5: Operation canceled"
[1843:2193:0716/091756.735071:ERROR:nss_ocsp.cc(614)] No URLRequestContext for NSS HTTP handler. host: ocsp.digicert.com
[1843:2193:0716/091756.735092:ERROR:nss_ocsp.cc(614)] No URLRequestContext for NSS HTTP handler. host: ocsp.digicert.com
[1843:2193:0716/091756.735108:ERROR:nss_ocsp.cc(614)] No URLRequestContext for NSS HTTP handler. host: crl4.digicert.com
[1843:2193:0716/091756.736059:ERROR:nss_ocsp.cc(614)] No URLRequestContext for NSS HTTP handler. host: ocsp.digicert.com
[1843:2193:0716/091756.736068:ERROR:nss_ocsp.cc(614)] No URLRequestContext for NSS HTTP handler. host: ocsp.digicert.com
[1843:2193:0716/091756.736081:ERROR:nss_ocsp.cc(614)] No URLRequestContext for NSS HTTP handler. host: crl4.digicert.com
</code></pre>

---

## Post #11 by @lassoan (2019-07-16 14:23 UTC)

<aside class="quote no-group" data-username="pieper" data-post="10" data-topic="7589">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I also tried the <code>no</code> and <code>core</code> options but always get the same result.</p>
</blockquote>
</aside>
<p>Selection of profile was introduced after 4.10.2. Could you try with a recent nightly?</p>
<aside class="quote no-group" data-username="pieper" data-post="10" data-topic="7589">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Something else is odd today with those <code>Operation canceled</code> messages</p>
</blockquote>
</aside>
<p>I often get those on Windows, too, especially on my desktop where I have many extensions installed. I suspect that it indicates the querying of available updates for installed extensions is timing out.</p>

---

## Post #12 by @pieper (2019-07-16 20:19 UTC)

<aside class="quote no-group">
<blockquote>
<blockquote>
<p>I also tried the <code>no</code> and <code>core</code> options but always get the same result.</p>
</blockquote>
<p>Selection of profile was introduced after 4.10.2. Could you try with a recent nightly?</p>
</blockquote>
</aside>
<p>Same result with the current nightly, the environment variable has no effect.</p>
<p>Oddly my local (debug) build on the same linux system doesn’t have the error message.  Extension manager dialog works for all combinations.</p>

---

## Post #13 by @lassoan (2019-07-16 20:48 UTC)

<aside class="quote no-group" data-username="pieper" data-post="12" data-topic="7589">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Same result with the current nightly, the environment variable has no effect.</p>
</blockquote>
</aside>
<p>Is the reported profile changing in the application log? There should be a log line like this:</p>
<pre><code>Qt configuration .........: version 5.10.1, with SSL, requested OpenGL 3.2 (compatibility profile)
</code></pre>
<p>If it is not changing then maybe the environment variable is not checked correctly (I’ve only tested it on Windows).</p>

---

## Post #14 by @pieper (2019-07-16 21:02 UTC)

<p>Yes, the log shows the environment variable worked.</p>
<p><code>[DEBUG][Qt] 16.07.2019 16:15:19 [] (unknown:0) - Qt configuration .........: version 5.11.2, with SSL, requested OpenGL 3.2 (compatibility profile)</code></p>

---

## Post #15 by @lassoan (2019-07-16 21:43 UTC)

<p>For this log entry, we check value in <code>QSurfaceFormat::defaultFormat()</code>, so it really is the surface format that Slicer uses. Maybe the log entry is generated by the webengine process. What Qt version do you use in your local build that does not generate the error?</p>
<p>This error seems to be very common on linux systems. Upgrading from Qt 5.10 to 5.12 fixed this linux crash for some projects <a href="https://github.com/CBICA/CaPTk/issues/277" rel="nofollow noopener">https://github.com/CBICA/CaPTk/issues/277</a>).</p>

---

## Post #16 by @pieper (2019-07-16 21:57 UTC)

<p>My local build is 5.8.0.  Maybe too old for the problem.</p>

---

## Post #17 by @tbillah (2019-07-22 21:34 UTC)

<p>I have the same issue with <a href="https://download.slicer.org/bitstream/1023242" rel="nofollow noopener">Slicer-4.10.2-linux-amd64</a>. When I try to launch the ExtensionManager, Slicer crashes:</p>
<pre><code class="lang-auto">$ ./Slicer
Switch to module:  "Welcome"
An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.
[0722/172516.028558:WARNING:stack_trace_posix.cc(699)] Failed to open file: /tmp/ffiAUn5xo (deleted)
  Error: No such file or directory
[16503:17205:0722/172516.706419:ERROR:gl_surface_glx_qt.cpp(186)] glXCreatePbuffer failed.
Received signal 11 SEGV_MAPERR 000000000000
#0 0x7f4a25c7b52f &lt;unknown&gt;
#1 0x7f4a246acb1d &lt;unknown&gt;
#2 0x7f4a25c7ba3e &lt;unknown&gt;
#3 0x7f4a19c876d0 &lt;unknown&gt;
#4 0x7f4a2470e34d &lt;unknown&gt;
#5 0x7f4a246f9ae8 &lt;unknown&gt;
#6 0x7f4a267b769d &lt;unknown&gt;
#7 0x7f4a249fd6d1 &lt;unknown&gt;
#8 0x7f4a249feec5 &lt;unknown&gt;
#9 0x7f4a26c6da67 &lt;unknown&gt;
#10 0x7f4a28487605 &lt;unknown&gt;
#11 0x7f4a25ce3ee5 &lt;unknown&gt;
#12 0x7f4a25cdf280 &lt;unknown&gt;
#13 0x7f4a19c7fe25 start_thread
#14 0x7f4a04cbcbad __clone
</code></pre>
<p>In case it is helpful, I have the following OpenGL configuration:</p>
<pre><code class="lang-auto">$ glxinfo | grep version
server glx version string: 1.4 Mesa 18.1.1
client glx version string: 1.4 Mesa 18.1.1
GLX version: 1.4
OpenGL core profile version string: 3.3 (Core Profile) Mesa 18.1.1
OpenGL core profile shading language version string: 3.30
OpenGL version string: 3.1 Mesa 18.1.1
OpenGL shading language version string: 1.40
OpenGL ES profile version string: OpenGL ES 3.0 Mesa 18.1.1
OpenGL ES profile shading language version string: OpenGL ES GLSL ES 3.00
</code></pre>
<p>Like <a class="mention" href="/u/pieper">@pieper</a>, falling back to other profiles didn’t help either.</p>

---

## Post #18 by @tbillah (2019-07-22 21:37 UTC)

<p>Question, is there a way to install extensions without using Extension Manager on the GUI?<br>
<a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p>Obviously building Slicer is an option, but not the most preferred one on ERIS cluster nodes with no sudo access.</p>

---

## Post #19 by @pieper (2019-07-22 21:51 UTC)

<p>Yes, as a workaround you can download and open the archive outside Slicer, then just set the paths so the modules are discovered (either via the settings or with --additional-module-paths on the command line)</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#How_to_manually_install_an_extension_package.3F" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#How_to_manually_install_an_extension_package.3F</a></p>

---

## Post #20 by @tbillah (2019-07-23 04:36 UTC)

<p>This is a good suggestion, except <a href="http://slicer.kitware.com/midas3/slicerappstore" rel="nofollow noopener">http://slicer.kitware.com/midas3/slicerappstore</a> is taking forever to load. Is the link active?</p>

---

## Post #21 by @jamesobutler (2019-07-23 10:20 UTC)

<p><a class="mention" href="/u/tbillah">@tbillah</a> Use the method to get to the slicerappstore as described in this linked post:</p><aside class="quote" data-post="2" data-topic="7550">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/extension-app-store-not-accessible-http-slicer-kitware-com-midas3-slicerappstore/7550/2">Extension app store not accessible (http://slicer.kitware.com/midas3/slicerappstore)</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Short answer: Use this link and enter relevant information. See <a href="http://slicer.kitware.com/midas3/slicerappstore/?os=win&amp;arch=amd64&amp;revision=&amp;search=&amp;layout=layout" rel="noopener nofollow ugc">http://slicer.kitware.com/midas3/slicerappstore/?os=win&amp;arch=amd64&amp;revision=&amp;search=&amp;layout=layout</a> 
Long answer: 

The landing page is trying to find the most recent Slicer revision … but this is not done efficiently.
We have plan to modernize the infrastructure and address issue like the one you reported. See <a href="https://www.slicer.org/wiki/Documentation/Labs/ExtensionsServer" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Labs/ExtensionsServer</a>
  </blockquote>
</aside>


---

## Post #22 by @lassoan (2019-07-23 12:41 UTC)

<p>The <a href="http://slicer.kitware.com/midas3/slicerappstore" rel="nofollow noopener">Slicer appstore site</a> is indeed very slow to load (if it loads at all).</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> could you please have a look at the server? Thanks!</p>

---

## Post #23 by @jamesobutler (2019-07-23 12:50 UTC)

<p>It’s very fast to load for me when you prepopulate the search fields. Here’s a link when searching Windows/x64/revision 28257 (Slicer.4.10.2)<br>
<a href="http://slicer.kitware.com/midas3/slicerappstore/?os=win&amp;arch=amd64&amp;revision=28257&amp;category=&amp;search=&amp;layout=layout" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.kitware.com/midas3/slicerappstore/?os=win&amp;arch=amd64&amp;revision=28257&amp;category=&amp;search=&amp;layout=layout</a></p>

---

## Post #24 by @lassoan (2019-07-23 13:16 UTC)

<p>Thank you, I confirm that pre-populating the fields make it load immediately. Probably auto-detection of latest version is slow because many preview release files piled up. I guess cleaning up older preview release files or switching to Girder will address this.</p>

---

## Post #25 by @tbillah (2019-07-23 14:14 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a>, I used the link from <a class="mention" href="/u/jcfr">@jcfr</a>’s post:</p>
<p><a href="http://slicer.kitware.com/midas3/slicerappstore/?os=win&amp;arch=amd64&amp;revision=&amp;search=&amp;layout=layout" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.kitware.com/midas3/slicerappstore/?os=win&amp;arch=amd64&amp;revision=&amp;search=&amp;layout=layout</a></p>
<p>Plugged in Linux, 64 bit, 28257, it’s still taking forever.</p>
<p>Even tried clicking <code>Diffusion</code>, <code>Process</code> etc on the left, didn’t help either. This is opposite to what <a class="mention" href="/u/lassoan">@lassoan</a> confirmed.</p>

---

## Post #26 by @lassoan (2019-07-23 16:22 UTC)

<aside class="quote no-group" data-username="tbillah" data-post="25" data-topic="7589">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tbillah/48/4139_2.png" class="avatar"> tbillah:</div>
<blockquote>
<p>Plugged in Linux, 64 bit, 28257, it’s still taking forever.</p>
</blockquote>
</aside>
<p>For me, this page loads immediately:<br>
<a href="http://slicer.kitware.com/midas3/slicerappstore/?os=linux&amp;arch=amd64&amp;revision=28257&amp;category=&amp;search=&amp;layout=layout" class="onebox" target="_blank" rel="noopener">http://slicer.kitware.com/midas3/slicerappstore/?os=linux&amp;arch=amd64&amp;revision=28257&amp;category=&amp;search=&amp;layout=layout</a></p>
<p>For Preview Releases, extensions may not be built for every platform for every revision, because there is only one build per night and if there is any error then there will be no extensions for that night. You can see on the <a href="http://slicer.cdash.org/index.php?project=SlicerPreview">dashboard</a> what is built each night and any build and test warnings and errors.</p>

---

## Post #27 by @PaoloZaffino (2019-10-01 17:02 UTC)

<p>Hi all,<br>
I have still problem with extension manager and data store too.<br>
If I try to open a new windows, it crashes.</p>
<p>I’m using Arch Linux and Slicer 4.11.0-2019-09-30.</p>
<p>Let me know if I can provide further information.<br>
Thanks a lot!</p>
<p>Paolo</p>

---

## Post #28 by @PaoloZaffino (2019-10-01 17:08 UTC)

<p>Sorry, my fault!<br>
I got that error if I use it via X2go, if I use the “real” desktop it works without problem.</p>
<p>Sorry for the noise!</p>
<p>Paolo</p>

---
