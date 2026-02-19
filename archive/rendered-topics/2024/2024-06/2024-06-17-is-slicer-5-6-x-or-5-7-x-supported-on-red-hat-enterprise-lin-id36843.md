---
topic_id: 36843
title: "Is Slicer 5 6 X Or 5 7 X Supported On Red Hat Enterprise Lin"
date: 2024-06-17
url: https://discourse.slicer.org/t/36843
---

# Is slicer 5.6.x or 5.7.x supported on Red Hat Enterprise Linux release 8.10 (Ootpa)

**Topic ID**: 36843
**Date**: 2024-06-17
**URL**: https://discourse.slicer.org/t/is-slicer-5-6-x-or-5-7-x-supported-on-red-hat-enterprise-linux-release-8-10-ootpa/36843

---

## Post #1 by @RonK (2024-06-17 19:01 UTC)

<p>Receiving the following error for both 5.6.2 and 5.7.0</p>
<pre><code class="lang-auto"># export QT_DEBUG_PLUGINS=1
# ./Slicer
 Error: BadAccess (attempt to access private resource denied) 10
  Extension:    131 (MIT-SHM)
  Minor opcode: 1 (X_ShmAttach)
  Resource id:  0x106
X Error: BadShmSeg (invalid shared segment parameter) 128
  Extension:    131 (MIT-SHM)
  Minor opcode: 5 (X_ShmCreatePixmap)
  Resource id:  0x2e0000c
X Error: BadDrawable (invalid Pixmap or Window parameter) 9
  Major opcode: 62 (X_CopyArea)
  Resource id:  0x2e0000d
/usr/local/Slicer-5.6.2-linux-amd64/bin/SlicerApp-real: symbol lookup error: /lib64/libk5crypto.so.3: undefined symbol: EVP_KDF_ctrl, version OPENSSL_1_1_1b
X Error: BadPixmap (invalid Pixmap parameter) 4
  Major opcode: 54 (X_FreePixmap)
  Resource id:  0x2e0000d
X Error: BadShmSeg (invalid shared segment parameter) 128
  Extension:    131 (MIT-SHM)
  Minor opcode: 2 (X_ShmDetach)
  Resource id:  0x2e0000c
</code></pre>

---

## Post #2 by @lassoan (2024-06-17 19:14 UTC)

<p>It seems that your system has some problem with the MIT-SHM (MIT Shared Memory Extension) X11 extension. You may need to disable this X11 extensions to use Qt applications, such as Slicer. See for example <a href="https://stackoverflow.com/questions/50605433/running-pyqt-with-root-privilege">this page</a> for details.</p>
<p>Let us know if this launches Slicer correctly on your system:</p>
<pre><code class="lang-auto">export QT_X11_NO_MITSHM=1
./Slicer
</code></pre>

---

## Post #3 by @RonK (2024-06-17 19:28 UTC)

<pre><code class="lang-auto"># export QT_X11_NO_MITSHM=1
# export QT_DEBUG_PLUGINS=1
[root@fchredhattst01 Slicer-5.6.2-linux-amd64]# ls
bin  include  lib  libexec  resources  share  Slicer
[root@fchredhattst01 Slicer-5.6.2-linux-amd64]# ./Slicer
QFactoryLoader::QFactoryLoader() ignoring "com.trolltech.Qt.QInputContextFactoryInterface" since plugins are disabled in static builds 
QFactoryLoader::QFactoryLoader() ignoring "com.trolltech.Qt.QStyleFactoryInterface" since plugins are disabled in static builds 
QFactoryLoader::QFactoryLoader() ignoring "com.trolltech.Qt.QImageIOHandlerFactoryInterface" since plugins are disabled in static builds 
/usr/local/Slicer-5.6.2-linux-amd64/bin/SlicerApp-real: symbol lookup error: /lib64/libk5crypto.so.3: undefined symbol: EVP_KDF_ctrl, version OPENSSL_1_1_1b
</code></pre>

---

## Post #4 by @lassoan (2024-06-17 19:37 UTC)

<p>It seems that you have run into this issue: <a href="https://github.com/Slicer/Slicer/issues/5663" class="inline-onebox">Crash on Fedora 33 due to OpenSSL/Kerberos incompatibility · Issue #5663 · Slicer/Slicer · GitHub</a></p>
<p>Please follow the suggestions described on that page and let us know what solution ended up working for you.</p>
<p>You probably don’t need <code>QT_DEBUG_PLUGINS=1</code>. You can remove it to avoid noise.</p>

---
