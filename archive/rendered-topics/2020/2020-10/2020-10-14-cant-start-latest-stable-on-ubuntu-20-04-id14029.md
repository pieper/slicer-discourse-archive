# Can't start latest stable on ubuntu 20.04

**Topic ID**: 14029
**Date**: 2020-10-14
**URL**: https://discourse.slicer.org/t/cant-start-latest-stable-on-ubuntu-20-04/14029

---

## Post #1 by @muratmaga (2020-10-14 03:58 UTC)

<p>Due to the issues we had with Centos 7 and latest stable, I  just recently installed Ubuntu 20.04 on a spare machine. This is just a default install, and nothing more (or less). Latest stable doesn’t start with this error:</p>
<pre><code>&gt; maga@magalab-ubuntu:~/Downloads/Slicer-4.11.20200930-linux-amd64$ ./Slicer 
&gt; qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
&gt; This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.
&gt; 
&gt;     Available platform plugins are: xcb.
&gt; 
&gt;     error: [/home/maga/Downloads/Slicer-4.11.20200930-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.`</code></pre>

---

## Post #2 by @muratmaga (2020-10-14 04:05 UTC)

<p>OK. As per <a href="https://askubuntu.com/questions/308128/failed-to-load-platform-plugin-xcb-while-launching-qt5-app-on-linux-without" rel="noopener nofollow ugc">this thread,</a> setting:<br>
export QT_DEBUG_PLUGINS=1</p>
<p>revealed missing library  libxcb-xinerama0. Installing it fixed the problem.</p>
<pre><code>maga@magalab-ubuntu:~/Downloads/Slicer-4.11.20200930-linux-amd64$ export QT_DEBUG_PLUGINS=1
maga@magalab-ubuntu:~/Downloads/Slicer-4.11.20200930-linux-amd64$ ./Slicer 
QFactoryLoader::QFactoryLoader() ignoring "com.nokia.qt.QGuiPlatformPluginInterface" since plugins are disabled in static builds 
QFactoryLoader::QFactoryLoader() ignoring "com.trolltech.Qt.QStyleFactoryInterface" since plugins are disabled in static builds 
QFactoryLoader::QFactoryLoader() ignoring "com.trolltech.Qt.QInputContextFactoryInterface" since plugins are disabled in static builds 
QFactoryLoader::QFactoryLoader() ignoring "com.trolltech.Qt.QImageIOHandlerFactoryInterface" since plugins are disabled in static builds 
QFactoryLoader::QFactoryLoader() checking directory path "/home/maga/Downloads/Slicer-4.11.20200930-linux-amd64/lib/QtPlugins/platforms" ...
QFactoryLoader::QFactoryLoader() looking at "/home/maga/Downloads/Slicer-4.11.20200930-linux-amd64/lib/QtPlugins/platforms/libqxcb.so"
Found metadata in lib /home/maga/Downloads/Slicer-4.11.20200930-linux-amd64/lib/QtPlugins/platforms/libqxcb.so, metadata=
{
    "IID": "org.qt-project.Qt.QPA.QPlatformIntegrationFactoryInterface.5.3",
    "MetaData": {
        "Keys": [
            "xcb"
        ]
    },
    "archreq": 0,
    "className": "QXcbIntegrationPlugin",
    "debug": false,
    "version": 331520
}


Got keys from plugin meta data ("xcb")
QFactoryLoader::QFactoryLoader() checking directory path "/home/maga/Downloads/Slicer-4.11.20200930-linux-amd64/bin/platforms" ...
Cannot load library /home/maga/Downloads/Slicer-4.11.20200930-linux-amd64/lib/QtPlugins/platforms/libqxcb.so: (libxcb-xinerama.so.0: cannot open shared object file: No such file or directory)
QLibraryPrivate::loadPlugin failed on "/home/maga/Downloads/Slicer-4.11.20200930-linux-amd64/lib/QtPlugins/platforms/libqxcb.so" : "Cannot load library /home/maga/Downloads/Slicer-4.11.20200930-linux-amd64/lib/QtPlugins/platforms/libqxcb.so: (libxcb-xinerama.so.0: cannot open shared object file: No such file or directory)"
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: xcb.

error: [/home/maga/Downloads/Slicer-4.11.20200930-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.</code></pre>

---

## Post #3 by @pieper (2020-10-14 19:07 UTC)

<p>Thanks for the report <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>
<p>So we should add <code>libxcb-xinerama0</code> to the install line here?<br>
</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#linux" target="_blank" rel="noopener">slicer.readthedocs.io</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="20" height="20">

<h3><a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#linux" target="_blank" rel="noopener">Getting Started — 3D Slicer  documentation</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>or is there a different package name?</p>

---

## Post #4 by @lassoan (2020-10-15 03:19 UTC)

<p>If you search for Qt an xinerama then you find lots of unhappy users complaining about this:</p>
<ul>
<li><a href="https://forum.qt.io/topic/75701/qt-static-compile-linux-error-loading-libxcb-xinerama-so/7">https://forum.qt.io/topic/75701/qt-static-compile-linux-error-loading-libxcb-xinerama-so/7</a></li>
<li><a href="https://bugreports.qt.io/browse/QTBUG-84749">https://bugreports.qt.io/browse/QTBUG-84749</a></li>
<li><a href="https://bugreports.qt.io/browse/QTBUG-69411">https://bugreports.qt.io/browse/QTBUG-69411</a></li>
</ul>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> Could you try to build Qt with <code>-no-xinerama</code> option to see if it fixes the issue? (see <a href="https://doc.qt.io/qt-5/linux-deployment.html">https://doc.qt.io/qt-5/linux-deployment.html</a>)</p>
<p>We can continue the discussion here, but I also added a ticket to make sure we implement a good solution before releasing Slicer5: <a href="https://github.com/Slicer/Slicer/issues/5251">https://github.com/Slicer/Slicer/issues/5251</a></p>

---

## Post #5 by @JanWitowski (2020-10-15 19:45 UTC)

<p>Just wanted to report that I have encountered the exact error, latest stable and Ubuntu 16.04.</p>

---

## Post #6 by @muratmaga (2020-10-15 19:51 UTC)

<p>I wonder what is different about the latest stable in the way it is built. We still couldn’t figure out why open3d 0.8.0 that worked until the 9/25 version of Linux is now causing a crash in the current stable.</p>

---

## Post #7 by @lassoan (2020-10-15 20:35 UTC)

<p>Open3d does not seem to be related to this problem and it is discussed <a href="https://discourse.slicer.org/t/open3d-worked-within-slicer-until-revision-29392/13870/10">here</a>).</p>
<p>Requiring xinerama extension on linux seems to be a very widespread problem. Qt says it is not a bug, as they <a href="https://doc.qt.io/qt-5/linux-deployment.html#application-dependencies">document what X11 extensions are required</a>, but since Ubuntu does not come with xinerama installed by default (maybe earlier ir did), this causing users some pain. Development of xinerama stopped more than a decade ago, and it seems that is being weeded out from more and more places, but its removal from Qt is only scheduled for Qt6. Until then, we either need to build our Qt with xinerama disabled or add a note to the Slicer installation instructions.</p>

---

## Post #8 by @jcfr (2020-10-15 20:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="14029">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Until then, we either need to build our Qt with xinerama disabled</p>
</blockquote>
</aside>
<p>Here is a pull request updating the build scripts: <a href="https://github.com/jcfr/qt-easy-build/pull/60" class="inline-onebox">[5.15.1] Build Qt for linux with xinerama disabled by jcfr · Pull Request #60 · jcfr/qt-easy-build · GitHub</a></p>
<p>That said, we currently do not build Qt and instead rely on the official binary to include Qt in the docker image used to build the official installers. See <a href="https://github.com/Slicer/SlicerBuildEnvironment/blob/master/Docker/qt5-centos7/qt-installer-noninteractive.qs">here</a></p>
<blockquote>
<p>Until then, we either need to build our Qt with xinerama disabled or add a note to the Slicer installation instructions.</p>
</blockquote>
<p>An third approach could be to update <a href="https://github.com/commontk/AppLauncher">the launcher</a> so that it checks for requirements and provide a friendly message to the user.</p>
<p>In the meantime, updating the install instructions is a sensible solution.</p>

---

## Post #9 by @lassoan (2020-11-03 20:34 UTC)

<p>A post was split to a new topic: <a href="/t/problem-running-slicer-on-centos8/14413">Problem running Slicer on CentOS8</a></p>

---

## Post #10 by @tbillah (2020-11-04 15:44 UTC)

<p>[CentOS 7]</p>
<p>Same problem:</p>
<pre><code class="lang-auto">Cannot load library Slicer-4.11.20200930-linux-amd64/lib/QtPlugins/platforms/libqxcb.so: (libxcb-icccm.so.4: cannot open shared object file: No such file or directory)
QLibraryPrivate::loadPlugin failed on "Slicer-4.11.20200930-linux-amd64/lib/QtPlugins/platforms/libqxcb.so" : "Cannot load library Slicer-4.11.20200930-linux-amd64/lib/QtPlugins/platforms/libqxcb.so: (libxcb-icccm.so.4: cannot open shared object file: No such file or directory)"
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.
</code></pre>
<p>I wonder why Slicer-4.11 fails to load <code>libqxcb.so</code> although it is found. I could try <code>yum install libxcb-devel</code> but do not have the privilege to do so. Any other bright ideas?</p>

---

## Post #11 by @pieper (2020-11-04 15:46 UTC)

<p>Are you able to request that the xcb package be installed?</p>
<p>If not, can you use singularity on that system for programs needing X and opengl?</p>

---

## Post #12 by @tbillah (2020-11-04 15:49 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>,</p>
<blockquote>
<p>Are you able to request that the xcb package be installed?</p>
</blockquote>
<p>If it has come down to having them available through the system, I should.</p>
<blockquote>
<p>If not, can you use singularity on that system for programs needing X and opengl?</p>
</blockquote>
<p>News for me, is Slicer available as a Singularity container now?</p>

---

## Post #13 by @pieper (2020-11-04 16:06 UTC)

<p>I think yes, from what I’ve seen xcb is going to be required, or at least for now that’s a reasonable workaround.</p>
<p>Regarding Singularity, I haven’t done that myself, but <a href="https://github.com/pieper/SlicerDockers">Docker works with Slicer</a> (at least older Slicers) and perhaps Singularity would too.  I ask, since you indicated Singularity is available to you for the trako project, but I don’t know if it will work for this too.</p>

---

## Post #14 by @PaoloZaffino (2020-12-02 15:46 UTC)

<p>Hi all,<br>
I think we are facing the same problem here.</p>
<p>The environment is:</p>
<ul>
<li>OS: Ubuntu 20.10 64bit, GNOME 3.38.1</li>
<li>CPU: AMD A10-9600p</li>
<li>GPU: Radeon R5 (embedded) plus Radeon R6 M435DX</li>
<li>RAM: 16GB DDR4</li>
<li>xinerama, openssl and xcb installed.</li>
<li>Slicer preview release (2020-11-30).</li>
</ul>
<p>That’s what we get:</p>
<blockquote>
<p>ciro@ciro:~/Slicer-4.13.0-2020-11-30-linux-amd64$ export QT_DEBUG_PLUGINS=1<br>
ciro@ciro:~/Slicer-4.13.0-2020-11-30-linux-amd64$ ./Slicer<br>
QFactoryLoader::QFactoryLoader() ignoring “com.nokia.qt.QGuiPlatformPluginInterface” since plugins are disabled in static builds<br>
QFactoryLoader::QFactoryLoader() ignoring “com.trolltech.Qt.QStyleFactoryInterface” since plugins are disabled in static builds<br>
QFactoryLoader::QFactoryLoader() ignoring “com.trolltech.Qt.QInputContextFactoryInterface” since plugins are disabled in static builds<br>
QFactoryLoader::QFactoryLoader() ignoring “com.trolltech.Qt.QImageIOHandlerFactoryInterface” since plugins are disabled in static builds<br>
QFactoryLoader::QFactoryLoader() checking directory path “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/platforms” …<br>
QFactoryLoader::QFactoryLoader() looking at “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/platforms/libqxcb.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/platforms/libqxcb.so, metadata=<br>
{<br>
“IID”: “org.qt-project.Qt.QPA.QPlatformIntegrationFactoryInterface.5.3”,<br>
“MetaData”: {<br>
“Keys”: [<br>
“xcb”<br>
]<br>
},<br>
“archreq”: 0,<br>
“className”: “QXcbIntegrationPlugin”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>Got keys from plugin meta data (“xcb”)<br>
QFactoryLoader::QFactoryLoader() checking directory path “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/bin/platforms” …<br>
loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/platforms/libqxcb.so”<br>
loaded library “Xcursor”<br>
QFactoryLoader::QFactoryLoader() checking directory path “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/platformthemes” …<br>
QFactoryLoader::QFactoryLoader() checking directory path “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/bin/platformthemes” …<br>
QFactoryLoader::QFactoryLoader() checking directory path “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/platforminputcontexts” …<br>
QFactoryLoader::QFactoryLoader() checking directory path “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/bin/platforminputcontexts” …<br>
QFactoryLoader::QFactoryLoader() checking directory path “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/xcbglintegrations” …<br>
QFactoryLoader::QFactoryLoader() looking at “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/xcbglintegrations/libqxcb-glx-integration.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/xcbglintegrations/libqxcb-glx-integration.so, metadata=<br>
{<br>
“IID”: “org.qt-project.Qt.QPA.Xcb.QXcbGlIntegrationFactoryInterface.5.5”,<br>
“MetaData”: {<br>
“Keys”: [<br>
“xcb_glx”<br>
]<br>
},<br>
“archreq”: 0,<br>
“className”: “QXcbGlxIntegrationPlugin”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>Got keys from plugin meta data (“xcb_glx”)<br>
QFactoryLoader::QFactoryLoader() checking directory path “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/bin/xcbglintegrations” …<br>
loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/xcbglintegrations/libqxcb-glx-integration.so”<br>
QFactoryLoader::QFactoryLoader() checking directory path “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/iconengines” …<br>
QFactoryLoader::QFactoryLoader() looking at “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/iconengines/libqSlicerIconEnginePlugin.so”<br>
“Failed to extract plugin meta data from ‘/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/iconengines/libqSlicerIconEnginePlugin.so’”<br>
not a plugin<br>
QFactoryLoader::QFactoryLoader() checking directory path “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/bin/iconengines” …<br>
QFactoryLoader::QFactoryLoader() checking directory path “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats” …<br>
QFactoryLoader::QFactoryLoader() looking at “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqgif.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqgif.so, metadata=<br>
{<br>
“IID”: “org.qt-project.Qt.QImageIOHandlerFactoryInterface”,<br>
“MetaData”: {<br>
“Keys”: [<br>
“gif”<br>
],<br>
“MimeTypes”: [<br>
“image/gif”<br>
]<br>
},<br>
“archreq”: 0,<br>
“className”: “QGifPlugin”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>Got keys from plugin meta data (“gif”)<br>
QFactoryLoader::QFactoryLoader() looking at “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqicns.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqicns.so, metadata=<br>
{<br>
“IID”: “org.qt-project.Qt.QImageIOHandlerFactoryInterface”,<br>
“MetaData”: {<br>
“Keys”: [<br>
“icns”<br>
],<br>
“MimeTypes”: [<br>
“image/x-icns”<br>
]<br>
},<br>
“archreq”: 0,<br>
“className”: “QICNSPlugin”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>Got keys from plugin meta data (“icns”)<br>
QFactoryLoader::QFactoryLoader() looking at “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqico.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqico.so, metadata=<br>
{<br>
“IID”: “org.qt-project.Qt.QImageIOHandlerFactoryInterface”,<br>
“MetaData”: {<br>
“Keys”: [<br>
“ico”,<br>
“cur”<br>
],<br>
“MimeTypes”: [<br>
“image/vnd.microsoft.icon”,<br>
“image/vnd.microsoft.icon”<br>
]<br>
},<br>
“archreq”: 0,<br>
“className”: “QICOPlugin”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>Got keys from plugin meta data (“ico”, “cur”)<br>
QFactoryLoader::QFactoryLoader() looking at “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqjpeg.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqjpeg.so, metadata=<br>
{<br>
“IID”: “org.qt-project.Qt.QImageIOHandlerFactoryInterface”,<br>
“MetaData”: {<br>
“Keys”: [<br>
“jpg”,<br>
“jpeg”<br>
],<br>
“MimeTypes”: [<br>
“image/jpeg”,<br>
“image/jpeg”<br>
]<br>
},<br>
“archreq”: 0,<br>
“className”: “QJpegPlugin”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>Got keys from plugin meta data (“jpg”, “jpeg”)<br>
QFactoryLoader::QFactoryLoader() looking at “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqsvg.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqsvg.so, metadata=<br>
{<br>
“IID”: “org.qt-project.Qt.QImageIOHandlerFactoryInterface”,<br>
“MetaData”: {<br>
“Keys”: [<br>
“svg”,<br>
“svgz”<br>
],<br>
“MimeTypes”: [<br>
“image/svg+xml”,<br>
“image/svg+xml-compressed”<br>
]<br>
},<br>
“archreq”: 0,<br>
“className”: “QSvgPlugin”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>Got keys from plugin meta data (“svg”, “svgz”)<br>
QFactoryLoader::QFactoryLoader() looking at “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqtga.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqtga.so, metadata=<br>
{<br>
“IID”: “org.qt-project.Qt.QImageIOHandlerFactoryInterface”,<br>
“MetaData”: {<br>
“Keys”: [<br>
“tga”<br>
],<br>
“MimeTypes”: [<br>
“image/x-tga”<br>
]<br>
},<br>
“archreq”: 0,<br>
“className”: “QTgaPlugin”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>Got keys from plugin meta data (“tga”)<br>
QFactoryLoader::QFactoryLoader() looking at “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqtiff.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqtiff.so, metadata=<br>
{<br>
“IID”: “org.qt-project.Qt.QImageIOHandlerFactoryInterface”,<br>
“MetaData”: {<br>
“Keys”: [<br>
“tiff”,<br>
“tif”<br>
],<br>
“MimeTypes”: [<br>
“image/tiff”,<br>
“image/tiff”<br>
]<br>
},<br>
“archreq”: 0,<br>
“className”: “QTiffPlugin”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>Got keys from plugin meta data (“tiff”, “tif”)<br>
QFactoryLoader::QFactoryLoader() looking at “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqwbmp.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqwbmp.so, metadata=<br>
{<br>
“IID”: “org.qt-project.Qt.QImageIOHandlerFactoryInterface”,<br>
“MetaData”: {<br>
“Keys”: [<br>
“wbmp”<br>
],<br>
“MimeTypes”: [<br>
“image/vnd.wap.wbmp”<br>
]<br>
},<br>
“archreq”: 0,<br>
“className”: “QWbmpPlugin”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>Got keys from plugin meta data (“wbmp”)<br>
QFactoryLoader::QFactoryLoader() looking at “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqwebp.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqwebp.so, metadata=<br>
{<br>
“IID”: “org.qt-project.Qt.QImageIOHandlerFactoryInterface”,<br>
“MetaData”: {<br>
“Keys”: [<br>
“webp”<br>
],<br>
“MimeTypes”: [<br>
“image/webp”<br>
]<br>
},<br>
“archreq”: 0,<br>
“className”: “QWebpPlugin”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>Got keys from plugin meta data (“webp”)<br>
QFactoryLoader::QFactoryLoader() checking directory path “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/bin/imageformats” …<br>
loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqgif.so”<br>
loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqicns.so”<br>
loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqico.so”<br>
loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqjpeg.so”<br>
loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqsvg.so”<br>
loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqtga.so”<br>
loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqtiff.so”<br>
loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqwbmp.so”<br>
loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/imageformats/libqwebp.so”<br>
QFactoryLoader::QFactoryLoader() checking directory path “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/accessible” …<br>
QFactoryLoader::QFactoryLoader() checking directory path “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/bin/accessible” …<br>
loaded library “crypto”<br>
loaded library “ssl”<br>
QFactoryLoader::QFactoryLoader() checking directory path “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/bearer” …<br>
QFactoryLoader::QFactoryLoader() checking directory path “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/bin/bearer” …<br>
QFactoryLoader::QFactoryLoader() checking directory path “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/styles” …<br>
QFactoryLoader::QFactoryLoader() looking at “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/styles/libqSlicerBaseQTGUIStylePlugins.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/QtPlugins/styles/libqSlicerBaseQTGUIStylePlugins.so, metadata=<br>
{<br>
“IID”: “org.qt-project.Qt.QStyleFactoryInterface”,<br>
“MetaData”: {<br>
“Keys”: [<br>
“slicer”,<br>
“light slicer”,<br>
“dark slicer”<br>
]<br>
},<br>
“archreq”: 0,<br>
“className”: “qSlicerStylePlugin”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>Got keys from plugin meta data (“slicer”, “light slicer”, “dark slicer”)<br>
QFactoryLoader::QFactoryLoader() checking directory path “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/bin/styles” …<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerAnnotationsModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerAnnotationsModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerAnnotationsModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerCamerasModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerCamerasModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerCamerasModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerColorsModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerColorsModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerColorsModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerCropVolumeModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerCropVolumeModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerCropVolumeModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerDataModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerDataModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerDataModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerDataStoreModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerDataStoreModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerDataStoreModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerDoubleArraysModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerDoubleArraysModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerDoubleArraysModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerDynamicModelerModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerDynamicModelerModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerDynamicModelerModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerMarkupsModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerMarkupsModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerMarkupsModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerModelsModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerModelsModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerModelsModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerMultiVolumeExplorerModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerMultiVolumeExplorerModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerMultiVolumeExplorerModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerPlotsModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerPlotsModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerPlotsModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerReformatModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerReformatModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerReformatModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerSceneViewsModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerSceneViewsModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerSceneViewsModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerSegmentationsModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerSegmentationsModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerSegmentationsModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerSequencesModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerSequencesModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerSequencesModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerSubjectHierarchyModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerSubjectHierarchyModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerSubjectHierarchyModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerTablesModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerTablesModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerTablesModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerTerminologiesModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerTerminologiesModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerTerminologiesModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerTextsModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerTextsModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerTextsModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerTransformsModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerTransformsModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerTransformsModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerUnitsModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerUnitsModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerUnitsModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerViewControllersModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerViewControllersModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerViewControllersModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerVolumeRenderingModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerVolumeRenderingModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerVolumeRenderingModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerVolumesModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerVolumesModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerVolumesModule.so”<br>
Found metadata in lib /home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerWelcomeModule.so, metadata=<br>
{<br>
“IID”: “org.slicer.modules.loadable.qSlicerLoadableModule/1.0”,<br>
“archreq”: 0,<br>
“className”: “qSlicerWelcomeModule”,<br>
“debug”: false,<br>
“version”: 331520<br>
}</p>
<p>loaded library “/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/lib/Slicer-4.13/qt-loadable-modules/libqSlicerWelcomeModule.so”<br>
error: [/home/ciro/Slicer-4.13.0-2020-11-30-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.</p>
</blockquote>
<p>Any idea of what is going on?</p>
<p>Thanks a lot.</p>
<p>Paolo</p>

---

## Post #15 by @pieper (2020-12-02 16:10 UTC)

<p>Hi <a class="mention" href="/u/paolozaffino">@PaoloZaffino</a> - yes, I see the same sort of thing with 20.10 and <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> says he sees it too on other linux and hopes to investigate.  I guess it’s a Qt platform issue so maybe just a build system update is enough.  Looks like you are on a good track to debug but I don’t know how to interpret that output.  Anyone else know?  Also does. local build work for you?</p>

---

## Post #16 by @PaoloZaffino (2020-12-02 16:32 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a><br>
This is a student of mine machine, I have no access to it to try to build Slicer from source.</p>
<p>If we can provide additional information we will be glad.</p>
<p>Paolo</p>

---

## Post #17 by @pieper (2020-12-02 16:34 UTC)

<p>Thanks <a class="mention" href="/u/paolozaffino">@PaoloZaffino</a> for now the suggestion is to use 20.04 which doesn’t have this issue.</p>

---

## Post #18 by @manjula (2020-12-02 19:46 UTC)

<p>Just to report PoP OS Pop!_OS 20.10 which is based on ubuntu 20.10 is working fine with Slicer both stable and unstable versions! and Build works with CMAKE GUI. I have not tried CLI .</p>

---

## Post #19 by @RafaelPalomar (2020-12-03 19:49 UTC)

<p>Hello,</p>
<p>I have been having a look at the problems using Slicer 4.11.20200930 in Ubuntu 20.10. Here are my findings:</p>
<ul>
<li>
<p>[Error 1] On a fresh installation of Ubuntu 20.10 <code>libxcb-xinerama0</code> needs to be installed to avoid an error related to qt and xcb when starting Slicer. Installing <code>qt5dxcb-plugin</code> will include <code>libxcb-xinerama0</code> and remove some other warnings during the execution of Slicer.</p>
</li>
<li>
<p>[Error 2] Slicer crashes with a segmentation fault on application launch. It seems the crash produces on the interaction of python (ctypes extension) with libffi (<code>/usr/lib/x86_64-linux-gnu/libffi.so.8</code>). In Ubuntu 20.10 libffi is packaged in its 3.4 version, while in other distributions not having this problem the version is 3.3. This would suggest incompatibility between the python deployed in Slicer and libffi installed in Ubuntu 20.10; <a class="mention" href="/u/manjula">@manjula</a>, could you check the version of libffi in PoP OS 20.10 just to discard this end?</p>
</li>
<li>
<p>[Workaround] The python version built in Slicer seems to come with its own libffi that can be built and included in libpython (statically) when <code>BUILTIN_CTYPES=ON</code> (in the python external project). Buiding the Slicer Python that way, Slicer seems to work properly. <a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/jcfr">@jcfr</a>, <a class="mention" href="/u/lassoan">@lassoan</a>, my suggestion would be to check whether setting <code>BUILTIN_CTYPES=ON</code> breaks anyting for other OSs (Windows, different versions of Linux) and set it <code>ON</code> for the superbuild.</p>
</li>
</ul>

---

## Post #20 by @pieper (2020-12-03 20:06 UTC)

<p>Very helpful debugging Rafael!</p>
<aside class="quote no-group" data-username="RafaelPalomar" data-post="19" data-topic="14029">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p>Installing <code>qt5dxcb-plugin</code> will include <code>libxcb-xinerama0</code> and remove some other warnings during the execution of</p>
</blockquote>
</aside>
<p>You mean this is something we can include in the slicer packaging?  Sounds much better than making the user install it.</p>
<aside class="quote no-group" data-username="RafaelPalomar" data-post="19" data-topic="14029">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p>check whether setting <code>BUILTIN_CTYPES=ON</code> breaks anyting for other OSs (Windows, different versions of Linux) and set it <code>ON</code> for the superbuild.</p>
</blockquote>
</aside>
<p>This sounds promising enough that we should probably enable it for the preview builds and see if it resolves the issue.  It sounds like the correct answer.</p>

---

## Post #21 by @RafaelPalomar (2020-12-03 20:33 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <code>qt5dxcb-plugin</code> seems to be a component of QtGui that can be built with the <code>-qt-xcb</code> flag (<a href="https://doc.qt.io/qt-5.9/qtgui-attribution-xcb.html" rel="noopener nofollow ugc">Qt XCB</a>). I guess to include this in the slicer packaging QT should be included as a whole? I’m with you on avoiding the user installing packages to use the packaged binaries, but we need to be careful not ending up packaging all the way to the Linux kernel <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"></p>

---

## Post #22 by @manjula (2020-12-03 20:39 UTC)

<aside class="quote no-group" data-username="RafaelPalomar" data-post="19" data-topic="14029">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<ul>
<li>[Error 2] Slicer crashes with a segmentation fault on application launch. It seems the crash produces on the interaction of python (ctypes extension) with libffi ( <code>/usr/lib/x86_64-linux-gnu/libffi.so.8</code> ). In Ubuntu 20.10 libffi is packaged in its 3.4 version, while in other distributions not having this problem the version is 3.3. This would suggest incompatibility between the python deployed in Slicer and libffi installed in Ubuntu 20.10; <a class="mention" href="/u/manjula">@manjula</a>, could you check the version of libffi in PoP OS 20.10 just to discard this end?</li>
</ul>
</blockquote>
</aside>
<p>3.4~20200819gead65ca871-0ubuntu3</p>

---

## Post #23 by @RafaelPalomar (2020-12-03 21:13 UTC)

<p>thanks <a class="mention" href="/u/manjula">@manjula</a>. It is exactly the same version as in Ubuntu 20.10. We may not be hitting the right diagnostic here with the compatibility. Would you mind to paste a list of your installed packages in <a href="https://dpaste.org" rel="noopener nofollow ugc">dpaste</a>?</p>
<p>to do this you can install <code>xclip</code>:</p>
<pre><code class="lang-auto">sudo apt install xclip
</code></pre>
<p>and then copy the list of packages in the clipboard</p>
<pre><code class="lang-auto">sudo apt list --installed | xclip -selection c
</code></pre>
<p>thenk you can go to <a href="https://dpaste.org" rel="noopener nofollow ugc">dpaste</a>, paste (Ctrl+V) the results and post here the link. If PoP is almost Ubuntu, maybe we find the difference.</p>
<p>Thanks in advance.</p>

---

## Post #24 by @manjula (2020-12-03 21:24 UTC)

<p>Please note that most of my packages i have is in flatpak but here is the link.</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <a href="https://dpaste.org/sNOh" target="_blank" rel="noopener nofollow ugc">dpaste.org</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="" height="">

<h3><a href="https://dpaste.org/sNOh" target="_blank" rel="noopener nofollow ugc">dpaste/sNOh (Python)</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #25 by @manjula (2020-12-03 21:28 UTC)

<p>I mentioned about flatpak because when I was figuring out what was going wrong with  linkSlicerBlender the deb version of the Blender was giving error in importing numpy, Apparently it was a know issue with blender but when i switch to flatpak it went away.</p>

---

## Post #26 by @RafaelPalomar (2020-12-06 06:54 UTC)

<p>I have installed PopOS 20.10 (also the packages from <a class="mention" href="/u/manjula">@manjula</a>) and got the same results as with Ubuntu 20.10:</p>
<ul>
<li>Error due to missing <code>libxcb-xinerama0</code> on Slicer stable (<code>4.11.20200930</code>). When <code>libxcb-xinerama0</code> is installed, segmentation fault is produced on startup.</li>
<li>Segmentation fault is removed by compiling python with <code>BUILTIN_CTYPES=ON</code>.</li>
</ul>
<p>I still think the problem is leaning towards a compatibility problem between python and libffi 3.4.</p>

---

## Post #27 by @kotloski (2020-12-08 15:54 UTC)

<p>I think I am experiencing the same issue with Ubuntu 20.10.  Can you tell me how to use the BUILTIN_CTYPES=ON work-around? I have not been able to figure it out from the online documentation. Thanks!</p>

---

## Post #28 by @jcfr (2020-12-08 19:04 UTC)

<aside class="quote no-group" data-username="kotloski" data-post="27" data-topic="14029">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kotloski/48/9115_2.png" class="avatar"> kotloski:</div>
<blockquote>
<p>Can you tell me how to use the BUILTIN_CTYPES=ON work-around?</p>
</blockquote>
</aside>
<p>This is a build option for the <code>cpython-cmake-buildsystem</code> project, you can enable this option adding</p>
<pre><code class="lang-auto">-DBUILTIN_CTYPES=ON
</code></pre>
<p>under <code>CMAKE_CACHE_ARGS</code> in this file:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/de2e43a7271b2f72d5537ea0a9af1288beb44055/SuperBuild/External_python.cmake#L138">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/de2e43a7271b2f72d5537ea0a9af1288beb44055/SuperBuild/External_python.cmake#L138" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/de2e43a7271b2f72d5537ea0a9af1288beb44055/SuperBuild/External_python.cmake#L138" target="_blank" rel="noopener">Slicer/Slicer/blob/de2e43a7271b2f72d5537ea0a9af1288beb44055/SuperBuild/External_python.cmake#L138</a></h4>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="128" style="counter-reset: li-counter 127 ;">
          <li>    CMAKE_ARGS</li>
          <li>    ${EXTERNAL_PROJECT_OPTIONAL_CMAKE_ARGS})</li>
          <li>endif()</li>
          <li></li>
          <li>ExternalProject_Add(${proj}</li>
          <li>  ${${proj}_EP_ARGS}</li>
          <li>  GIT_REPOSITORY "${Slicer_${proj}_GIT_REPOSITORY}"</li>
          <li>  GIT_TAG "${Slicer_${proj}_GIT_TAG}"</li>
          <li>  SOURCE_DIR ${EP_SOURCE_DIR}</li>
          <li>  BINARY_DIR ${EP_BINARY_DIR}</li>
          <li class="selected">  CMAKE_CACHE_ARGS</li>
          <li>    -DCMAKE_CXX_COMPILER:FILEPATH=${CMAKE_CXX_COMPILER}</li>
          <li>    #-DCMAKE_CXX_FLAGS:STRING=${ep_common_cxx_flags} # Not used</li>
          <li>    -DCMAKE_C_COMPILER:FILEPATH=${CMAKE_C_COMPILER}</li>
          <li>    -DCMAKE_C_FLAGS:STRING=${ep_common_c_flags}</li>
          <li>    -DCMAKE_INSTALL_PREFIX:PATH=${EP_INSTALL_DIR}</li>
          <li>    #-DBUILD_TESTING:BOOL=OFF</li>
          <li>    -DBUILD_LIBPYTHON_SHARED:BOOL=ON</li>
          <li>    -DUSE_SYSTEM_LIBRARIES:BOOL=OFF</li>
          <li>    -DSRC_DIR:PATH=${python_SOURCE_DIR}</li>
          <li>    -DDOWNLOAD_SOURCES:BOOL=OFF</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Then, you would have to re-build Slicer from the top-level.</p>

---

## Post #29 by @kotloski (2020-12-10 14:17 UTC)

<p>Thanks! Adding <strong>-DBUILTIN_CTYPES:BOOL=ON</strong> worked. Though the extension I need doesn’t won’t run in the latest build. Oh well, it’s been that kind of year.</p>

---

## Post #30 by @jcfr (2020-12-10 15:51 UTC)

<aside class="quote no-group" data-username="kotloski" data-post="29" data-topic="14029">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kotloski/48/9115_2.png" class="avatar"> kotloski:</div>
<blockquote>
<p>Though the extension I need doesn’t won’t run in the latest build.</p>
</blockquote>
</aside>
<p>Which extension it is ?</p>

---

## Post #31 by @kotloski (2020-12-10 16:29 UTC)

<p>Segmentation Wizard. It last worked for me in 4.10.2. The extension seems to install OK and I can see it in the Extensions manager window, but I can not find it under modules in the main program and it is listed as “not loaded” when I search using Module finder. Thanks for any help; I just need to finish up a little bit of old data.</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://www.slicer.org/w/img_auth.php/6/64/Favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SegmentationWizard" target="_blank" rel="noopener nofollow ugc">slicer.org</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SegmentationWizard" target="_blank" rel="noopener nofollow ugc">Documentation/Nightly/Extensions/SegmentationWizard - Slicer Wiki</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #32 by @lassoan (2020-12-10 19:59 UTC)

<p>Yes. Your system is not compatible with the precompiled binaries that we provide.</p>

---

## Post #33 by @manjula (2020-12-14 13:24 UTC)

<p>I today tried building Slicer in Manjaro Linux on a fresh install. it failed,  with the following errors.</p>
<p>This is the output from the finals parts</p>
<p><a href="https://pastebin.com/0gAANfae" class="onebox" target="_blank" rel="noopener nofollow ugc">https://pastebin.com/0gAANfae</a></p>
<p>As <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> said i checked the version  of libffi</p>
<blockquote>
<p>core/libffi 3.3-4 [installed]<br>
Portable foreign function interface library<br>
community/haskell-libffi 0.1-20<br>
A binding to libffi<br>
multilib/lib32-libffi 3.3-2 [installed]<br>
A portable, high level programming interface to various calling conventions (32-bit)</p>
</blockquote>

---

## Post #34 by @RafaelPalomar (2020-12-14 15:51 UTC)

<p><a class="mention" href="/u/manjula">@manjula</a>, I think your problem is not related to the issue discussed in this thread.  This thread is starting to be a mix of different issues and is becoming difficult to follow. I suggest that you open a new thread for discussing it.</p>
<p>Regards,<br>
Rafael</p>

---

## Post #35 by @lassoan (2020-12-14 16:00 UTC)

<p>It may be better to keep this thread as general discussion topic here and create separate issues in the issue tracker to discuss technical details there.</p>

---

## Post #36 by @fuentesdt (2020-12-29 04:01 UTC)

<p>apt-get install libxcb-xinerama0-dev</p>
<p>seemed to work for me on ubuntu 16.04</p>

---

## Post #37 by @Karam_AbuGhalieh (2021-02-09 17:09 UTC)

<p>I found this solution <a href="https://askubuntu.com/questions/308128/failed-to-load-platform-plugin-xcb-while-launching-qt5-app-on-linux-without" rel="noopener nofollow ugc">here</a> and worked fine for me:</p>
<pre><code class="lang-auto">sudo apt-get install --reinstall libxcb-xinerama0
</code></pre>

---

## Post #38 by @lassoan (2021-02-09 17:47 UTC)

<p>Thank you. This is also described in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#linux">Slicer install instructions</a>.</p>
<p><a class="mention" href="/u/karam_abughalieh">@Karam_AbuGhalieh</a> Do you have a suggestion how to make the instructions easier to find?</p>

---

## Post #39 by @Karam_AbuGhalieh (2021-02-09 19:22 UTC)

<p>I was there before facing the problem, now I am surprised the solution is there!</p>
<p>I think what I did is just reading the Linux section and ignoring the next Debian/Ubuntu one!!</p>

---

## Post #40 by @pieper (2021-12-18 16:49 UTC)

<p>Note that for another machine where I started from a fresh unbuntu 20.04 that wasn’t configured as a desktop workstation I also needed to add this package to get past the xcb startup issue: <code>sudo apt-get install libxcb-shape0</code></p>
<p>I also installed these packages to get xvfb-run to work with Slicer:</p>
<p><code>sudo apt-get install libxcb-icccm4-dev libxcb-image0-dev libxcb-keysyms1-dev libxcb-randr0 libxcb-render-util0 libxcb-xkb-dev libxkbcommon-x11-dev</code></p>

---

## Post #41 by @tbillah (2022-04-25 20:29 UTC)

<blockquote>
<p>libxcb-icccm4-dev libxcb-image0-dev libxcb-keysyms1-dev libxcb-randr0 libxcb-render-util0 libxcb-xkb-dev libxkbcommon-x11-dev</p>
</blockquote>
<p>Hi <a class="mention" href="/u/pieper">@pieper</a> , do you happen to remember the CentOS equivalent package names for these?</p>

---

## Post #42 by @tbillah (2022-04-25 20:37 UTC)

<p>For NDA Amazon workspace, I needed to install the following packages to be able to launch a pre-built Slicer:</p>
<blockquote>
<p>yum -y install xcb-util-wm xcb-util-image xcb-util-keysyms xcb-util-renderutil libxkbcommon-x11</p>
</blockquote>

---

## Post #43 by @lassoan (2022-04-26 03:14 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> should we add this to the Linux install instructions?</p>

---

## Post #44 by @pieper (2022-04-26 12:12 UTC)

<p>Yes, I was thinking of suggesting that.  I didn’t have a chance to do it myself.</p>

---

## Post #45 by @tbillah (2022-04-26 14:16 UTC)

<p>By the way, don’t forget to document <a href="https://discourse.slicer.org/t/error-glsl-1-50-is-not-supported/10083/7">export MESA_GL_VERSION_OVERRIDE=3.3</a> .</p>

---

## Post #46 by @pieper (2022-04-26 14:23 UTC)

<p>It would be good if someone who uses the platforms in question could craft the PR with all the needed instructions.  I don’t use these platforms.</p>

---

## Post #47 by @VSTVR (2022-07-22 08:47 UTC)

<p>Yes indeed.<br>
sudo apt-get install libxcb-xinerama0</p>

---

## Post #48 by @nagy.attila (2023-06-28 08:47 UTC)

<p>Just a quick note:</p>
<p>I downloaded and installed 5.2.2 on an Ubuntu 220.04 LTS.<br>
I just have upgraded from 20.04 LTS the other day.</p>
<p>This is an almost vanilla install (I have no knowledge about previous package additions on this pc, but  I am almost sure there weren’t too many)</p>
<p>I had to apt install t5dxcb-plugin because until then Slicer stopped during start:</p>
<pre><code class="lang-auto">./Slicer 
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: xcb.

error: [/home/attila/Downloads/Slicer-5.2.2-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.
</code></pre>

---

## Post #49 by @RafaelPalomar (2023-06-28 12:37 UTC)

<p>Hello <a class="mention" href="/u/nagy.attila">@nagy.attila</a>, have you had a look at the documented requirements for linux?</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#linux" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#linux</a></p>
<p>On a VirtualBox fresh installation of Ubuntu 22.04 i just had to install:</p>
<pre><code class="lang-auto">sudo apt-get install libpulse-dev libnss3 libglu1-mesa
sudo apt-get install --reinstall libxcb-xinerama0
</code></pre>
<p>The binary re-distributable for both stable and preview launches without problems. I hope this helps.</p>

---

## Post #50 by @swang.jislee (2023-10-13 17:19 UTC)

<p>I got the same problem as <a class="mention" href="/u/paolozaffino">@PaoloZaffino</a> reported.<br>
There is a missing dependency for debian:</p>
<p>libxkbcommon-x11-0</p>
<p>You need to install it by:<br>
sudo apt install libxkbcommon-x11-0</p>

---

## Post #51 by @nagy.attila (2024-06-04 12:32 UTC)

<p>Hi <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> , sorry, it is very unkind of me not to follow up <img src="https://emoji.discourse-cdn.com/twitter/innocent.png?v=12" title=":innocent:" class="emoji" alt=":innocent:" loading="lazy" width="20" height="20"></p>
<p>The solution worked!</p>
<p>It seems though, that the issue still persists: I faced the same problem on a vanilla Ubuntu 24.04 LTS with Slicer 5.6.2.<br>
Interestingly (for me) ldd didn’t reveal the missing dependency, I had to set the QT_DEBUG_PLUGINS=1 variable to reveal the missing library.</p>
<p>This time I installed qt5dxcb-plugin, and it fixed the issue, even though it might have been a bit overkill <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Best,<br>
Attila</p>

---

## Post #52 by @lassoan (2024-06-04 15:55 UTC)

<p>Thanks for the update <a class="mention" href="/u/nagy.attila">@nagy.attila</a></p>
<p><a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> could you have a look at the <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#linux">linux install instructions</a> and see if we need to update? Should we add <code>libxkbcommon-x11-0</code> and <code>qt5dxcb-plugin</code>?</p>

---

## Post #53 by @RafaelPalomar (2024-06-04 19:29 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, yes, I can give it a review</p>

---

## Post #54 by @nagy.attila (2024-06-05 06:40 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> , <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a></p>
<p>It seems that this is the culprit:</p>
<pre><code class="lang-auto">Got keys from plugin meta data ("xcb")
QFactoryLoader::QFactoryLoader() checking directory path "/home/attila/Downloads/Slicer-5.6.2-linux-amd64/bin/platforms" ...
Cannot load library /home/attila/Downloads/Slicer-5.6.2-linux-amd64/lib/QtPlugins/platforms/libqxcb.so: (libxcb-xinerama.so.0: cannot open shared object file: No such file or directory)
</code></pre>
<p>According to apt-file find, libxcb-xinerama.so.0 is provided by<br>
apt-file find libxcb-xinerama.so.0<br>
libxcb-xinerama0: /usr/lib/x86_64-linux-gnu/libxcb-xinerama.so.0<br>
libxcb-xinerama0: /usr/lib/x86_64-linux-gnu/libxcb-xinerama.so.0.0.0</p>
<p>And that dependency was installed by qt5dxcb-plugin:</p>
<pre><code class="lang-auto">sudo apt install qt5dxcb-plugin
[sudo] password for attila: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  libdouble-conversion3 libmd4c0 libpcre2-16-0 libqt5core5t64 libqt5dbus5t64 libqt5gui5t64
  libqt5network5t64 libqt5qml5 libqt5qmlmodels5 libqt5quick5 libqt5svg5 libqt5waylandclient5
  libqt5waylandcompositor5 libqt5widgets5t64 libqt5x11extras5 libxcb-composite0
  libxcb-xinerama0 libxcb-xinput0 qt5-gtk-platformtheme qttranslations5-l10n qtwayland5
Suggested packages:
  qgnomeplatform-qt5 qt5-image-formats-plugins qt5-qmltooling-plugins
The following NEW packages will be installed:
  libdouble-conversion3 libmd4c0 libpcre2-16-0 libqt5core5t64 libqt5dbus5t64 libqt5gui5t64
  libqt5network5t64 libqt5qml5 libqt5qmlmodels5 libqt5quick5 libqt5svg5 libqt5waylandclient5
  libqt5waylandcompositor5 libqt5widgets5t64 libqt5x11extras5 libxcb-composite0
  libxcb-xinerama0 libxcb-xinput0 qt5-gtk-platformtheme qt5dxcb-plugin qttranslations5-l10n
  qtwayland5
0 upgraded, 22 newly installed, 0 to remove and 28 not upgraded.
</code></pre>
<p>libxkbcommon-x11-0 seems to be part of the base install:</p>
<pre><code class="lang-auto">apt list | grep libxkbcommon

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

libxkbcommon-dev/noble 1.6.0-1build1 amd64
libxkbcommon-dev/noble 1.6.0-1build1 i386
libxkbcommon-doc/noble,noble 1.6.0-1build1 all
libxkbcommon-tools/noble 1.6.0-1build1 amd64
libxkbcommon-tools/noble 1.6.0-1build1 i386
libxkbcommon-x11-0/noble,now 1.6.0-1build1 amd64 [installed,automatic]
libxkbcommon-x11-0/noble 1.6.0-1build1 i386
libxkbcommon-x11-dev/noble 1.6.0-1build1 amd64
libxkbcommon-x11-dev/noble 1.6.0-1build1 i386
libxkbcommon0/noble,now 1.6.0-1build1 amd64 [installed,automatic]
libxkbcommon0/noble 1.6.0-1build1 i386

</code></pre>
<p>According to this manifest:<br>
<a href="http://releases.ubuntu.com/noble/ubuntu-24.04-desktop-amd64.manifest" class="onebox" target="_blank" rel="noopener nofollow ugc">http://releases.ubuntu.com/noble/ubuntu-24.04-desktop-amd64.manifest</a></p>
<p>Best,<br>
Attila</p>

---
