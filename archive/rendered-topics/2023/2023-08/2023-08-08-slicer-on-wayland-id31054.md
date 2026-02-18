# Slicer on Wayland

**Topic ID**: 31054
**Date**: 2023-08-08
**URL**: https://discourse.slicer.org/t/slicer-on-wayland/31054

---

## Post #1 by @d-vogel (2023-08-08 20:44 UTC)

<p>Hey everyone,<br>
I’ve been messing around a bit today with Slicer due to performance issues and noticed it’s actually running in XWayland on my openSuse TW + KDE plasma Wayland system.<br>
Upon starting from the commandline:</p>
<pre><code class="lang-bash">➜  ~ /opt/slicer/Slicer-5.3.0-2023-08-01-linux-amd64/Slicer
qt.qpa.plugin: Could not find the Qt platform plugin "wayland" in ""
Switch to module:  "Welcome"
</code></pre>
<p>indeed, the platform plugins shipped in the binary download are the following:</p>
<pre><code class="lang-bash">➜  ~ ls /opt/slicer/Slicer-5.3.0-2023-08-01-linux-amd64/lib/QtPlugins/platforms/           
libqxcb.so
</code></pre>
<p>While the ones available on my system:</p>
<pre><code class="lang-bash">➜  ~ ls /usr/lib64/qt5/plugins/platforms 
libqeglfs.so       libqminimal.so    libqwayland-egl.so             libqwayland-xcomposite-glx.so
libqlinuxfb.so     libqoffscreen.so  libqwayland-generic.so         libqxcb.so
libqminimalegl.so  libqvnc.so        libqwayland-xcomposite-egl.so
</code></pre>
<p>and unfortunately symlinking any of the files from the latter to the former is unsuccessful, Qt finds and correctly identifies the lib, but stops with version incompatibility.</p>
<p>If my understanding is right, would it be imaginable to have the platform plugins shipped with Slicer?</p>

---

## Post #2 by @lassoan (2023-08-09 20:16 UTC)

<p>Thank you for the investigation and sharing the results.</p>
<p>I’ve tried to set up a linux box with wayland a couple of months ago and found that basically none of the commonly used remote desktop software supported it yet, so it did not look like that wayland is really ready for replacing X protocol. Do you find that wayland is actually practically usable? (for me, no standard remote desktop software</p>
<p>If yes, and you think that it is time for Slicer to support it, too, then we could use some of your experience and help with this. Could you build Slicer as described <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html">here</a> and see if it works? Then try to make a package (<code>make package</code>) and see if the wayland platform plugin files are included in the created package.</p>
<ul>
<li>If the wayland plugin files are not included then <code>SlicerBlockInstallQtPlugins.cmake</code> may need to be modified.</li>
<li>If the wayland plugin files are included it means that the Qt that is used on factory machines need to be <a href="https://github.com/jcfr/qt-easy-build/tree/5.15.2#readme">built</a> with wayland enabled.</li>
</ul>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/jcfr">@jcfr</a> please chime in if you have some suggestions or have experience with wayland support.</p>

---

## Post #3 by @jcfr (2023-08-09 23:38 UTC)

<p>Looking at  the Slicer sources, we can indeed observe that we are only packaging <code>xcb</code> plugins</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/1e656d9bf0ea8a23e1f87e52f06f4cd82c0cb754/CMake/SlicerCPack.cmake#L48-L52">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/1e656d9bf0ea8a23e1f87e52f06f4cd82c0cb754/CMake/SlicerCPack.cmake#L48-L52" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/1e656d9bf0ea8a23e1f87e52f06f4cd82c0cb754/CMake/SlicerCPack.cmake#L48-L52" target="_blank" rel="noopener">CMake/SlicerCPack.cmake</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/1e656d9bf0ea8a23e1f87e52f06f4cd82c0cb754/CMake/SlicerCPack.cmake#L48-L52" rel="noopener"><code>1e656d9bf</code></a>
</div>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="48" style="counter-reset: li-counter 47 ;">
          <li>elseif(UNIX)</li>
          <li>  list(APPEND SlicerBlockInstallQtPlugins_subdirectories</li>
          <li>    platforms:xcb</li>
          <li>    xcbglintegrations:xcb-glx-integration</li>
          <li>    )</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<blockquote>
<p>means that the Qt that is used on factory machines need to be <a href="https://github.com/jcfr/qt-easy-build/tree/5.15.2#readme">built</a> with wayland enabled.</p>
</blockquote>
<p>Since on Linux, we are re-packaging the official binaries, addressing this should not require to build Qt from source.</p>
<h3><a name="p-98886-wayland-plugins-1" class="anchor" href="#p-98886-wayland-plugins-1" aria-label="Heading link"></a>Wayland plugins</h3>
<p>The plugins available in Qt 5.15.2 are the following:</p>
<pre><code class="lang-auto">$ cd /opt/qt/5.15.2/gcc_64/plugins

$ ls -1 wayland-decoration-client/
libbradient.so

$ ls -1 wayland-graphics-integration-client/
libdmabuf-server.so
libdrm-egl-server.so
libqt-plugin-wayland-egl.so
libshm-emulation-server.so
libvulkan-server.so
libxcomposite-egl.so
libxcomposite-glx.so

$ ls -1 wayland-shell-integration/
libfullscreen-shell-v1.so
libivi-shell.so
libwl-shell.so
libxdg-shell.so
libxdg-shell-v5.so
libxdg-shell-v6.so
</code></pre>
<h3><a name="p-98886-distributing-wayland-plugins-2" class="anchor" href="#p-98886-distributing-wayland-plugins-2" aria-label="Heading link"></a>Distributing Wayland plugins</h3>
<p>It would be straightforward to distribute additional plugins.</p>
<p><a class="mention" href="/u/d-vogel">@d-vogel</a> Could you help use evaluate which ones ?</p>
<p>Without recompiling, you should be able to simply copy the missing plugins found after installing Qt 5.15.2 following <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#any-distribution">these instructions</a></p>
<h3><a name="p-98886-documentation-3" class="anchor" href="#p-98886-documentation-3" aria-label="Heading link"></a>Documentation</h3>
<ul>
<li><a href="https://doc.qt.io/qt-5/wayland-and-qt.html" class="inline-onebox">Wayland and Qt | Qt 5.15</a></li>
<li><a href="https://doc.qt.io/qt-6/wayland-and-qt.html" class="inline-onebox">Wayland and Qt | Qt 6.10</a></li>
<li><a href="https://wiki.qt.io/QtWayland#How_do_I_use_QtWayland.3F" class="inline-onebox">QtWayland - Qt Wiki</a></li>
</ul>

---

## Post #4 by @d-vogel (2023-08-10 06:31 UTC)

<p>Well wayland is now default on quite a few distributions (Fedora and openSuse at least), KDE has stated Wayland is their default target for Plasmashell and I think Gnome is also very much focused on Wayland.</p>
<p>I’ve been running  plasmashell with wayland for around two years now and I think all apps installed from the distro repo are using wayland (including Paraview with better performance with Wayland). The last apps that don’t are apps installed via flatpack (MS Teams) and Electron apps (VSCode, Slack, Spotify, Obsidian) both require adding a flag manually, I applied them for Teams and VSCode and again the animations are smoother.</p>
<p>As for the source build, it might be challenging in terms of time, I will first investigate the direction provided by <a class="mention" href="/u/jcfr">@jcfr</a>.</p>

---

## Post #5 by @chir.set (2023-08-10 08:45 UTC)

<aside class="quote no-group" data-username="d-vogel" data-post="4" data-topic="31054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/b782af/48.png" class="avatar"> d-vogel:</div>
<blockquote>
<p>plasmashell with wayland</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="d-vogel" data-post="4" data-topic="31054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/b782af/48.png" class="avatar"> d-vogel:</div>
<blockquote>
<p>all apps installed from the distro repo are using wayland</p>
</blockquote>
</aside>
<p>To my understanding, apps in plasmashell-wayland are in fact using xwayland, and won’t start without X libraries. Last time I tried with a pure Wayland desktop like Weston, even kcalc did not launch. Will try again, it’s just doubtful that the plethora of applicaions in a Linux distribution have been ported to pure Wayland.</p>

---

## Post #6 by @d-vogel (2023-08-10 12:01 UTC)

<p>XWayland apps get listed by <code>xlsclients</code>, only those I talked about in my previous message pop up in the list.</p>

---

## Post #7 by @pieper (2023-08-10 12:53 UTC)

<p>There’s no reason Wayland shouldn’t be supportable either via the methods Jc suggested if someone has the time to invest in it, or by waiting for the Qt6 port.  I’m not particularly motivated since X works fine for my use cases and remote desktop support in Wayland seems to be lagging.</p>

---

## Post #8 by @jcfr (2023-08-10 13:31 UTC)

<blockquote>
<p>I will first investigate the direction provided by <a class="mention" href="/u/jcfr">@jcfr</a></p>
</blockquote>
<p><a class="mention" href="/u/d-vogel">@d-vogel</a>  Thanks for working on that. The idea would be to understand how to update variable <code>SlicerBlockInstallQtPlugins_subdirectories</code> referenced above.</p>
<p>In addition of the libraries listed above, there are also:</p>
<pre><code class="lang-auto">$ cd /opt/qt/5.15.2/gcc_64/plugins

$ ls -1 platforms/libqwayland-*so
platforms/libqwayland-egl.so
platforms/libqwayland-generic.so
platforms/libqwayland-xcomposite-egl.so
platforms/libqwayland-xcomposite-glx.so
</code></pre>
<p>Reading this page is informative:</p>
<ul>
<li><a href="https://github.com/qt/qtwayland/tree/5.15">https://github.com/qt/qtwayland/tree/5.15</a></li>
</ul>
<p>After we understand which plugins are required and how to env. variable  like these ones:</p>
<ul>
<li><code>QT_XCB_GL_INTEGRATION</code></li>
<li><code>QT_WAYLAND_CLIENT_BUFFER_INTEGRATION</code></li>
</ul>
<p>we will understand how to update the list of plugins to package and provide guidance.</p>
<p>The env. variable should be set in a way for also compatible with how Qt and VTK are integrated.</p>
<p>Additional resources:</p>
<ul>
<li><a href="https://github.com/qt/qtwayland/tree/5.15">https://github.com/qt/qtwayland/tree/5.15</a></li>
<li><a href="https://doc.qt.io/qt-5/license-changes.html#qt-wayland-compositor">https://doc.qt.io/qt-5/license-changes.html#qt-wayland-compositor</a></li>
<li><a href="https://doc.qt.io/qt-6/license-changes.html#qt-wayland-module">https://doc.qt.io/qt-6/license-changes.html#qt-wayland-module</a></li>
</ul>

---
