---
topic_id: 3185
title: "4 9 0 Nightly Build Cannot Be Run On A Vnc Server Due To Qt5"
date: 2018-06-14
url: https://discourse.slicer.org/t/3185
---

# 4.9.0 nightly build cannot be run on a VNC server due to Qt5-GLX problem

**Topic ID**: 3185
**Date**: 2018-06-14
**URL**: https://discourse.slicer.org/t/4-9-0-nightly-build-cannot-be-run-on-a-vnc-server-due-to-qt5-glx-problem/3185

---

## Post #1 by @ferhue (2018-06-14 20:02 UTC)

<p>I am using a VNCviewer to connect to a remote Ubuntu 16 server, where I have installed 3DSlicer.</p>
<p>I downloaded the stable release and run it without problems as:</p>
<blockquote>
<p>user@pgdev:~$ /opt/Slicer-4.8.1-linux-amd64/Slicer<br>
Number of registered modules: 161<br>
Number of instantiated modules: 161<br>
Number of loaded modules: 161<br>
Switch to module:  “Welcome”<br>
Loaded volume from file: /home/user/.config/NA-MIC/Extensions-26813/SlicerVMTK/lib/Slicer-4.8/qt-scripted-modules/Resources/Vesselness.png. Dimensions: 65x50x1. Number of components: 3. Pixel type: unsigned char.</p>
</blockquote>
<p>However, with the nightly build 4.9.0, it does not work any more, thus I report the problem.</p>
<blockquote>
<p>user@pgdev:~$ /opt/Slicer-4.9.0-2018-06-11-linux-amd64/Slicer<br>
QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to ‘/tmp/runtime-user’<br>
QXcbConnection: Failed to initialize XRandr<br>
Qt: XKEYBOARD extension not present on the X server.<br>
Could not initialize GLX<br>
error: [/opt/Slicer-4.9.0-2018-06-11-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.</p>
</blockquote>
<p>Seems to be a Qt5 issue. I tried the solutions posted here, but to no avail: <a href="https://github.com/spyder-ide/spyder/issues/3713" class="inline-onebox" rel="noopener nofollow ugc">No keyboard responding for Spyder when started through VNC · Issue #3713 · spyder-ide/spyder · GitHub</a></p>
<p>Here my system info:</p>
<blockquote>
<p>user@pgdev:~$ uname -a<br>
Linux pgdev 4.4.0-127-generic <span class="hashtag-raw">#153-Ubuntu</span> SMP Sat May 19 10:58:46 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux<br>
user@pgdev:~$ cat /etc/os-release<br>
NAME=“Ubuntu”<br>
VERSION=“16.04.4 LTS (Xenial Xerus)”<br>
ID=ubuntu<br>
ID_LIKE=debian<br>
PRETTY_NAME=“Ubuntu 16.04.4 LTS”<br>
VERSION_ID=“16.04”<br>
HOME_URL=“<a href="http://www.ubuntu.com/" rel="noopener nofollow ugc">http://www.ubuntu.com/</a>”<br>
SUPPORT_URL=“<a href="http://help.ubuntu.com/" rel="noopener nofollow ugc">http://help.ubuntu.com/</a>”<br>
BUG_REPORT_URL=“<a href="http://bugs.launchpad.net/ubuntu/" class="inline-onebox" rel="noopener nofollow ugc">Bugs : Ubuntu</a>”<br>
VERSION_CODENAME=xenial<br>
UBUNTU_CODENAME=xenial</p>
</blockquote>

---

## Post #2 by @ihnorton (2018-06-14 21:49 UTC)

<p>You could try <code>export LIBGL_ALWAYS_INDIRECT=1</code>, in the shell, before launching Slicer.</p>

---

## Post #3 by @ferhue (2018-06-14 21:58 UTC)

<p>Thanks, but does not work, I get the exact same error message.</p>

---

## Post #4 by @muratmaga (2018-06-16 02:12 UTC)

<p>As an alternative solution, you can use virtualgl on your vncserver. You will need to execute the slicer through vglrun command.</p>
<p><a href="https://virtualgl.org/vgldoc/2_1_1/" rel="nofollow noopener">https://virtualgl.org/vgldoc/2_1_1/</a></p>

---

## Post #5 by @fedorov (2020-03-19 20:14 UTC)

<p><a class="mention" href="/u/ferhue">@ferhue</a> another user reported this problem.  Can you let us know what worked for you? Were you able to figure this out?</p>

---

## Post #6 by @ferhue (2020-03-19 21:51 UTC)

<p>I never solved it, I just used it with grdesktop instead of VNC viewer.</p>
<p>I just tried again with Ubuntu 18 and Slicer 4.10.1 and it does not crash, however I get a black screen.</p>
<p>Below the errors printed in terminal:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bcad818cdb5093ff2ee3f16a2f0ea3aa2ed81018.png" data-download-href="/uploads/short-url/qV7uXTSpOqhuOsKGiHgp61DpsO4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bcad818cdb5093ff2ee3f16a2f0ea3aa2ed81018_2_690x281.png" alt="image" data-base62-sha1="qV7uXTSpOqhuOsKGiHgp61DpsO4" width="690" height="281" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bcad818cdb5093ff2ee3f16a2f0ea3aa2ed81018_2_690x281.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bcad818cdb5093ff2ee3f16a2f0ea3aa2ed81018.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bcad818cdb5093ff2ee3f16a2f0ea3aa2ed81018.png 2x" data-dominant-color="EEEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1030×420 63.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
