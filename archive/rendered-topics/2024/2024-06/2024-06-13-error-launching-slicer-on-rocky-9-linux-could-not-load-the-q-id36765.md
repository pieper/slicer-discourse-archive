# Error launching Slicer on Rocky 9 linux: `Could not load the Qt platform plugin "xcb" in "" even though it was found`

**Topic ID**: 36765
**Date**: 2024-06-13
**URL**: https://discourse.slicer.org/t/error-launching-slicer-on-rocky-9-linux-could-not-load-the-qt-platform-plugin-xcb-in-even-though-it-was-found/36765

---

## Post #1 by @113992 (2024-06-13 19:10 UTC)

<p>Hello, I am having some issues when launching the Slicer program. This is the output with export QT_DEBUG_PLUGINS=1. I am on Rocky Linux 9:</p>
<blockquote>
<p>QFactoryLoader::QFactoryLoader() ignoring “com.trolltech.Qt.QInputContextFactoryInterface” since plugins are disabled in static builds<br>
QFactoryLoader::QFactoryLoader() ignoring “com.trolltech.Qt.QStyleFactoryInterface” since plugins are disabled in static builds<br>
QFactoryLoader::QFactoryLoader() ignoring “com.trolltech.Qt.QImageIOHandlerFactoryInterface” since plugins are disabled in static builds<br>
QFactoryLoader::QFactoryLoader() checking directory path “/opt/3Dslicer/5.6.2/lib/QtPlugins/platforms” …<br>
QFactoryLoader::QFactoryLoader() looking at “/opt/3Dslicer/5.6.2/lib/QtPlugins/platforms/libqxcb.so”<br>
Found metadata in lib /opt/3Dslicer/5.6.2/lib/QtPlugins/platforms/libqxcb.so, metadata=<br>
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
QFactoryLoader::QFactoryLoader() checking directory path “/opt/3Dslicer/5.6.2/bin/platforms” …<br>
Cannot load library /opt/3Dslicer/5.6.2/lib/QtPlugins/platforms/libqxcb.so: (libxcb-icccm.so.4: cannot open shared object file: No such file or directory)<br>
QLibraryPrivate::loadPlugin failed on “/opt/3Dslicer/5.6.2/lib/QtPlugins/platforms/libqxcb.so” : “Cannot load library /opt/3Dslicer/5.6.2/lib/QtPlugins/platforms/libqxcb.so: (libxcb-icccm.so.4: cannot open shared object file: No such file or directory)”<br>
qt.qpa.plugin: Could not load the Qt platform plugin “xcb” in “” even though it was found.<br>
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.</p>
<p>Available platform plugins are: xcb.</p>
<p>error: [/opt/3Dslicer/5.6.2/bin/SlicerApp-real] exit abnormally - Report the problem.</p>
</blockquote>
<p>I have seen this error mentioned on Ubuntu/Debian but not Rocky and admittedly I am a little stumped.</p>
<p>I yum installed the prerequisites: mesa-libGLU libnsl.</p>
<p>Am I missing an additional list of dependencies for Rocky 9?</p>

---

## Post #2 by @RafaelPalomar (2024-06-13 19:28 UTC)

<p>Hello. Yesterday, I went through some Linux distributions and updated the documentation in this PR (not yet merged): <a href="https://github.com/Slicer/Slicer/pull/7798" class="inline-onebox" rel="noopener nofollow ugc">DOC: Update Linux documentation by RafaelPalomar · Pull Request #7798 · Slicer/Slicer · GitHub</a>. Rocky is not in the list, but maybe some of the other distros can be used as inspiration for the dependencies.</p>

---
