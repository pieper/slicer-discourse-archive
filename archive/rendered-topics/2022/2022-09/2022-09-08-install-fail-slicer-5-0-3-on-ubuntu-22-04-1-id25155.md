# Install fail Slicer-5.0.3 on Ubuntu-22.04.1

**Topic ID**: 25155
**Date**: 2022-09-08
**URL**: https://discourse.slicer.org/t/install-fail-slicer-5-0-3-on-ubuntu-22-04-1/25155

---

## Post #1 by @JSteinJ (2022-09-08 13:11 UTC)

<p>Hi &amp; greetings. I have the following problem:<br>
when I try to start my new 3D Slicer on Linux there is a flash of the “welcome screen” &amp; the following error message:</p>
<pre><code class="lang-auto">Qt: Session management error: Could not open network socket
Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.
</code></pre>
<p>I found some fixes here used for other versions:</p>
<blockquote>
<p>Debian / Ubuntu<br>
The following may be needed on fresh debian or ubuntu:</p>
<pre><code class="lang-auto">sudo apt-get install libpulse-dev libnss3 libglu1-mesa
sudo apt-get install --reinstall libxcb-xinerama0
</code></pre>
</blockquote>
<blockquote>
<pre><code class="lang-auto">Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: xcb.
</code></pre>
<p>The solution is to create symlink:</p>
<pre><code class="lang-auto">sudo ln -s /usr/lib/x86_64-linux-gnu/libxcb-util.so /usr/lib/x86_64-linux-gnu/libxcb-util.so.1
</code></pre>
</blockquote>
<p>Did not work, same error…<br>
???<br>
Greetings jsteinj</p>

---

## Post #2 by @cnot (2022-09-21 12:27 UTC)

<p>I am having the exact same issue trying to install Slicer 5.0.3 on Fedora 36… Did you happen to find a solution?</p>
<p>Cheers</p>

---

## Post #3 by @lassoan (2022-09-21 14:00 UTC)

<p><a class="mention" href="/u/cnot">@cnot</a> Please follow <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#linux">these instructions</a> and let us know if it fixed the problem.</p>
<p><a class="mention" href="/u/jsteinj">@JSteinJ</a> Slicer uses Qt as GUI toolkit and right now many (all?) such applications seem to be broken if Wayland is used (see for example <a href="https://www.reddit.com/r/swaywm/comments/s6bpc2/a_lot_of_packages_dont_work_under_wayland/?utm_source=BD&amp;utm_medium=Search&amp;utm_name=Bing&amp;utm_content=PSR1">1</a> and <a href="https://bugreports.qt.io/browse/QTBUG-105921">2</a>). Please try solutions that you can find on the web about running Qt applications on Ubuntu-22 with Wayland and let us know if you found any solution (or if disabling Wayland fixes the issue).</p>

---

## Post #4 by @cnot (2022-09-21 16:10 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Those are the instructions I followed originally, see <a href="https://discourse.slicer.org/t/problems-with-3d-slicer-5-0-3-installation-on-fedora-36/25359" class="inline-onebox">Problems with 3D Slicer 5.0.3 Installation on Fedora 36</a> for the full results. Unfortunately, it is still not running…</p>

---

## Post #5 by @lassoan (2022-09-21 16:18 UTC)

<p><a class="mention" href="/u/cnot">@cnot</a> thank you for trying those instructions<br>
If those did not help then probably your system is configured to use Wayland. Please see tips that I gave to <a class="mention" href="/u/jsteinj">@JSteinJ</a> above.</p>

---

## Post #7 by @cnot (2022-09-21 17:06 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> , it actually does not appear as if my system is configured to use Wayland. The output of</p>
<p><code>echo $XDG_SESSION_TYPE</code></p>
<p>is</p>
<p><code>x11</code></p>
<p>…Is there another possible explanation?</p>

---

## Post #8 by @muratmaga (2022-09-21 17:25 UTC)

<p>Try the QT_DEBUG_PLUGIN=1 as explained in here <a href="https://discourse.slicer.org/t/cant-start-latest-stable-on-ubuntu-20-04/14029/2" class="inline-onebox">Can't start latest stable on ubuntu 20.04 - #2 by muratmaga</a></p>
<p>and see which other QT plugin you are missing from your system (the ones we included in the documentation are the most common ones for most common install options, they are not necessarily the only ones, say if you did a minimal install).</p>

---

## Post #9 by @cnot (2022-09-21 17:44 UTC)

<p>Thank you very much for your reply, <a class="mention" href="/u/muratmaga">@muratmaga</a> . When running it with QT_DEBUG_PLUGIN, this is the output:</p>
<pre><code class="lang-auto">Found metadata in lib /usr/img/Slicer503/lib/QtPlugins/platforms/libqxcb.so, metadata=
{
“IID”: “org.qt-project.Qt.QPA.QPlatformIntegrationFactoryInterface.5.3”,
“MetaData”: {
“Keys”: [
“xcb”
]
},
“archreq”: 0,
“className”: “QXcbIntegrationPlugin”,
“debug”: false,
“version”: 331520
}

Got keys from plugin meta data (“xcb”)
QFactoryLoader::QFactoryLoader() checking directory path “/usr/img/Slicer503/bin/platforms” …
Cannot load library /usr/img/Slicer503/lib/QtPlugins/platforms/libqxcb.so: (libxcb-icccm.so.4: cannot open shared object file: No such file or directory)
QLibraryPrivate::loadPlugin failed on “/usr/img/Slicer503/lib/QtPlugins/platforms/libqxcb.so” : “Cannot load library /usr/img/Slicer503/lib/QtPlugins/platforms/libqxcb.so: (libxcb-icccm.so.4: cannot open shared object file: No such file or directory)”
qt.qpa.plugin: Could not load the Qt platform plugin “xcb” in “” even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: xcb.

error: [/usr/img/Slicer503/bin/SlicerApp-real] exit abnormally - Report the problem.
</code></pre>
<p><em>I tried:</em><br>
<code>dnf install libxcb-icccm.so.4</code></p>
<p><em>Result:</em></p>
<pre><code class="lang-auto">No match for argument: lixcb-icccm.so.4
Error: Unable to find a match: lixcb-icccm.so.4
</code></pre>
<p>I then tried<br>
<code>dnf list libxcb</code></p>
<p>To see if I was missing anything, but the result was</p>
<pre><code class="lang-auto">Installed Packages
libxcb.i686 1.13.1-9.fc36 @fedora
libxcb.x86_64 1.13.1-9.fc36 @fedora
</code></pre>
<p>So I am now not sure how to proceed!</p>

---

## Post #10 by @muratmaga (2022-09-21 17:47 UTC)

<aside class="quote no-group" data-username="cnot" data-post="9" data-topic="25155">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cnot/48/16719_2.png" class="avatar"> cnot:</div>
<blockquote>
<p><code>lixcb-icccm.so.4</code></p>
</blockquote>
</aside>
<p>did you try the wm-util package? I am not a fedora user, but it seems to provide<br>
<a href="https://rpmfind.net/linux/RPM/fedora/devel/rawhide/aarch64/x/xcb-util-wm-0.4.1-23.fc37.aarch64.html" class="onebox" target="_blank" rel="noopener">https://rpmfind.net/linux/RPM/fedora/devel/rawhide/aarch64/x/xcb-util-wm-0.4.1-23.fc37.aarch64.html</a></p>

---

## Post #11 by @cnot (2022-09-22 07:24 UTC)

<p>Thank you for your suggestion! Yes, I already have xcb-util-wm-0.4.1-12.el8.x86_64.rpm installed…</p>

---

## Post #12 by @muratmaga (2022-09-22 17:52 UTC)

<p>Then somehow QT is not finding the that. Perhaps you are simply missing the symbolic link. For example on my ubuntu it shows like this:</p>
<pre><code class="lang-auto">/usr/lib/x86_64-linux-gnu$ ls -l libxcb-ic*
lrwxrwxrwx 1 root root    21 Nov  4  2021 libxcb-icccm.so.4 -&gt; libxcb-icccm.so.4.0.0
-rw-r--r-- 1 root root 22464 Dec  4  2018 libxcb-icccm.so.4.0.0
</code></pre>
<p>or it is not on a path that QT looks… Sorry that’s as far as I can help…</p>

---
