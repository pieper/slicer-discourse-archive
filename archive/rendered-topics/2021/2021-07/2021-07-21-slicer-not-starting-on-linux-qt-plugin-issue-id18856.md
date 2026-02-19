---
topic_id: 18856
title: "Slicer Not Starting On Linux Qt Plugin Issue"
date: 2021-07-21
url: https://discourse.slicer.org/t/18856
---

# Slicer not starting on Linux (Qt plugin issue)

**Topic ID**: 18856
**Date**: 2021-07-21
**URL**: https://discourse.slicer.org/t/slicer-not-starting-on-linux-qt-plugin-issue/18856

---

## Post #1 by @perecanals (2021-07-21 12:44 UTC)

<p>Hi,</p>
<p>OS: Linux (Ubuntu 20.04)<br>
Slicer version (current stable release): Slicer-4.11.20210226-linux-amd64</p>
<p>I am trying to start Slicer after the usual download and extraction process and this error appears:</p>
<pre><code class="lang-auto">qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: xcb.
</code></pre>
<p>I found this topic <a href="https://discourse.slicer.org/t/error-executing-version-slicer-4-11-0-2020-06-01-linux-amd64-tar-gz-on-ubuntu-16-04/11834">https://discourse.slicer.org/t/error-executing-version-slicer-4-11-0-2020-06-01-linux-amd64-tar-gz-on-ubuntu-16-04/11834</a> in the forums, and installing that version works well, but I am using a more recent version of the VMTK module that is not compatible tith that version of Slicer and my Python scripts do not work. I tried installing the Nightly build (Slicer-4.13.0-2021-07-17-linux-amd64) and I run into the same error as the current stable version. Any help?</p>

---

## Post #2 by @perecanals (2021-07-21 12:56 UTC)

<p>To add more info, I tried running the <code>./Slicer</code> command (stable release) with <code>export QT_DEBUG_PLUGINS=1</code>, and this was output:</p>
<pre><code class="lang-auto">QFactoryLoader::QFactoryLoader() ignoring "com.nokia.qt.QGuiPlatformPluginInterface" since plugins are disabled in static builds 
QFactoryLoader::QFactoryLoader() ignoring "com.trolltech.Qt.QStyleFactoryInterface" since plugins are disabled in static builds 
QFactoryLoader::QFactoryLoader() ignoring "com.trolltech.Qt.QInputContextFactoryInterface" since plugins are disabled in static builds 
QFactoryLoader::QFactoryLoader() ignoring "com.trolltech.Qt.QImageIOHandlerFactoryInterface" since plugins are disabled in static builds 
QFactoryLoader::QFactoryLoader() checking directory path "/home/perecanals/Applications/Slicer-4.11.20210226-linux-amd64/lib/QtPlugins/platforms" ...
QFactoryLoader::QFactoryLoader() looking at "/home/perecanals/Applications/Slicer-4.11.20210226-linux-amd64/lib/QtPlugins/platforms/libqxcb.so"
Found metadata in lib /home/perecanals/Applications/Slicer-4.11.20210226-linux-amd64/lib/QtPlugins/platforms/libqxcb.so, metadata=
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
QFactoryLoader::QFactoryLoader() checking directory path "/home/perecanals/Applications/Slicer-4.11.20210226-linux-amd64/bin/platforms" ...
Cannot load library /home/perecanals/Applications/Slicer-4.11.20210226-linux-amd64/lib/QtPlugins/platforms/libqxcb.so: (libxcb-xinerama.so.0: cannot open shared object file: No such file or directory)
QLibraryPrivate::loadPlugin failed on "/home/perecanals/Applications/Slicer-4.11.20210226-linux-amd64/lib/QtPlugins/platforms/libqxcb.so" : "Cannot load library /home/perecanals/Applications/Slicer-4.11.20210226-linux-amd64/lib/QtPlugins/platforms/libqxcb.so: (libxcb-xinerama.so.0: cannot open shared object file: No such file or directory)"
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: xcb.
</code></pre>
<p>From this, together with what I gathered online, it seems that the problem has to do with that <code>libxcb-xinerama.so.0</code> file, but I don’t know how to fix it.</p>

---

## Post #3 by @pieper (2021-07-21 13:20 UTC)

<p>Did you find this thread?  That solution should work.</p>
<aside class="quote quote-modified" data-post="1" data-topic="14029">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/cant-start-latest-stable-on-ubuntu-20-04/14029">Can't start latest stable on ubuntu 20.04</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Due to the issues we had with Centos 7 and latest stable, I  just recently installed Ubuntu 20.04 on a spare machine. This is just a default install, and nothing more (or less). Latest stable doesn’t start with this error: 
&gt; maga@magalab-ubuntu:~/Downloads/Slicer-4.11.20200930-linux-amd64$ ./Slicer 
&gt; qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
&gt; This application failed to start because no Qt platform plugin could be initialized. Reinstalling the a…
  </blockquote>
</aside>


---

## Post #4 by @perecanals (2021-07-21 13:31 UTC)

<p>Just found it a minute before you posted the response! Gonna try to follow it, thanks and sorry! Maybe I wasn’t specific enough but I could not find it before posting the issue. Thank you!</p>

---
