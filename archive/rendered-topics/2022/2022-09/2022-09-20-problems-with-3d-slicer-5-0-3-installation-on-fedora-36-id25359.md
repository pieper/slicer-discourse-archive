# Problems with 3D Slicer 5.0.3 Installation on Fedora 36

**Topic ID**: 25359
**Date**: 2022-09-20
**URL**: https://discourse.slicer.org/t/problems-with-3d-slicer-5-0-3-installation-on-fedora-36/25359

---

## Post #1 by @cnot (2022-09-20 15:20 UTC)

<p>Hello all! I am running into some issues when trying to run Slicer 5.0.3 on my Fedora 36 workstation.</p>
<p>I followed the instructions given here (<a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#installing-3d-slicer" class="inline-onebox" rel="noopener nofollow ugc">Getting Started — 3D Slicer documentation</a>), making sure to install the necessary dependencies and removing the included libcrypto files.</p>
<p>When I try to run the Slicer executable, I get the following error:</p>
<p>Found metadata in lib /usr/img/Slicer503/lib/QtPlugins/platforms/libqxcb.so, metadata=<br>
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
QFactoryLoader::QFactoryLoader() checking directory path “/usr/img/Slicer503/bin/platforms” …<br>
Cannot load library /usr/img/Slicer503/lib/QtPlugins/platforms/libqxcb.so: (libxcb-icccm.so.4: cannot open shared object file: No such file or directory)<br>
QLibraryPrivate::loadPlugin failed on “/usr/img/Slicer503/lib/QtPlugins/platforms/libqxcb.so” : “Cannot load library /usr/img/Slicer503/lib/QtPlugins/platforms/libqxcb.so: (libxcb-icccm.so.4: cannot open shared object file: No such file or directory)”<br>
qt.qpa.plugin: Could not load the Qt platform plugin “xcb” in “” even though it was found.<br>
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.</p>
<p>Available platform plugins are: xcb.</p>
<p>error: [/usr/img/Slicer503/bin/SlicerApp-real] exit abnormally - Report the problem.</p>
<p><em>I tried:</em><br>
dnf install libxcb-icccm.so.4<br>
<em>I got:</em><br>
No match for argument: lixcb-icccm.so.4<br>
Error: Unable to find a match: lixcb-icccm.so.4</p>
<p><em>I tried:</em><br>
dnf list libxcb<br>
<em>I got:</em><br>
Installed Packages<br>
libxcb.i686                         1.13.1-9.fc36                        <span class="mention">@fedora</span><br>
libxcb.x86_64                       1.13.1-9.fc36                        <span class="mention">@fedora</span></p>
<p>I tried reinstalling libxcb, to no avail.</p>
<p>Any ideas of where to go from here would be greatly appreciated, thank you!</p>

---

## Post #2 by @pieper (2022-10-04 13:47 UTC)

<p>Were you able to resolve this?</p>

---

## Post #3 by @cnot (2022-10-14 07:02 UTC)

<p>I followed the advice suggested on: <a href="https://discourse.slicer.org/t/install-fail-slicer-5-0-3-on-ubuntu-22-04-1/25155/8" class="inline-onebox">Install fail Slicer-5.0.3 on Ubuntu-22.04.1 - #8 by muratmaga</a>, and then restarted my machine. This seemed to fix it!</p>

---
