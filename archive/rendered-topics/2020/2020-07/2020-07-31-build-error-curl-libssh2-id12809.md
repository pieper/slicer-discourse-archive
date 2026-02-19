---
topic_id: 12809
title: "Build Error Curl Libssh2"
date: 2020-07-31
url: https://discourse.slicer.org/t/12809
---

# Build error curl/libssh2

**Topic ID**: 12809
**Date**: 2020-07-31
**URL**: https://discourse.slicer.org/t/build-error-curl-libssh2/12809

---

## Post #1 by @gcsharp (2020-07-31 17:20 UTC)

<p>Hi, I am getting the following build error:</p>
<pre><code>[ 23%] Linking CXX shared library ../../bin/libRemoteIO.so
/usr/bin/ld: /PHShome/gcs6/build/slicer-4/Slicer-build/curl-install/lib/libcurl.a(libssh2.c.o): in function `ssh_statemach_act':
libssh2.c:(.text+0x322): undefined reference to `libssh2_session_handshake'
/usr/bin/ld: libssh2.c:(.text+0x363): undefined reference to `libssh2_hostkey_hash'
/usr/bin/ld: libssh2.c:(.text+0x40b): undefined reference to `libssh2_session_hostkey'
&lt;and many more&gt;
</code></pre>
<p>Missing symbols are defined in /usr/lib/x86_64-linux-gnu/libssh2.so, but libssh2 is not specified in the link command for building target libRemoteIO.  Any idea how to fix?</p>

---

## Post #2 by @hherhold (2020-07-31 18:14 UTC)

<p>This was mentioned in <a href="https://discourse.slicer.org/t/build-fails-in-vtk-many-undefined-references/12150" class="inline-onebox">Build fails in VTK : many undefined references</a>. You can see my fix at the bottom, as discussed in the thread, I’m not sure it’s the <em>correct</em> fix.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> - any update/opinions on this?</p>
<p>Thanks!!</p>

---

## Post #3 by @lassoan (2020-07-31 18:33 UTC)

<p><a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> does your <a href="https://github.com/Slicer/Slicer/pull/5050">new linux build instructions page</a> include description of this solution/workaround? It would be great if you could add it and finalize the page soon (we can always improve it as needed). Thank you!</p>

---

## Post #4 by @hherhold (2020-07-31 18:47 UTC)

<p>Is the addition of ssh2 as a library a reasonable fix? or just a workaround?</p>
<p>I’m happy to submit a pull request if it’s an actual fix.</p>

---

## Post #5 by @gcsharp (2020-07-31 20:27 UTC)

<p>Thanks HH.  This works great!  (Slicer crashes, but it does compile.)</p>

---
