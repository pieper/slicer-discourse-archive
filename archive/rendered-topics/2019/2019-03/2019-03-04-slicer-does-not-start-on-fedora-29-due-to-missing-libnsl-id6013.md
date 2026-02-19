---
topic_id: 6013
title: "Slicer Does Not Start On Fedora 29 Due To Missing Libnsl"
date: 2019-03-04
url: https://discourse.slicer.org/t/6013
---

# Slicer does not start on Fedora 29 due to missing libnsl

**Topic ID**: 6013
**Date**: 2019-03-04
**URL**: https://discourse.slicer.org/t/slicer-does-not-start-on-fedora-29-due-to-missing-libnsl/6013

---

## Post #1 by @Kevin_Santi (2019-03-04 18:55 UTC)

<p>Operating system:fedora 29<br>
Slicer version:4.11 and 4.10<br>
Expected behavior:work as mentioned in linux guidelines installation<br>
Actual behavior:not working<br>
error while loading shared libraries: libnsl.so.1: cannot open shared object file: No such file or directory</p>
<p>libnsl already installed</p>
<p>Big thanks in advance!</p>

---

## Post #2 by @fedorov (2019-03-05 16:02 UTC)

<p>Did you try installing <code>libnsl</code> package?</p>
<p>From a quick search, this seemed to work for some users of other applications where this caused problem (e.g. see <a href="https://github.com/AppImage/pkg2appimage/issues/336#issuecomment-419797608" rel="nofollow noopener">https://github.com/AppImage/pkg2appimage/issues/336#issuecomment-419797608</a>).</p>

---
