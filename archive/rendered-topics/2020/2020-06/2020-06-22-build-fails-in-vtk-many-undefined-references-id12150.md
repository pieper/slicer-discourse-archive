# Build fails in VTK : many undefined references

**Topic ID**: 12150
**Date**: 2020-06-22
**URL**: https://discourse.slicer.org/t/build-fails-in-vtk-many-undefined-references/12150

---

## Post #1 by @chir.set (2020-06-22 09:26 UTC)

<p>Hello,</p>
<p>Sorry to bother you again. Slicer (128fb86dd18) build fails in VTK on Arch Linux as such :</p>
<blockquote>
<p>/usr/bin/ld: CMakeFiles/vtkProbeOpenGLVersion.dir/vtkProbeOpenGLVersion.cxx.o: in function <code>main': vtkProbeOpenGLVersion.cxx:(.text.startup+0x25): undefined reference to </code>vtkRenderer::New()’<br>
/usr/bin/ld: vtkProbeOpenGLVersion.cxx:(.text.startup+0x2d): undefined reference to <code>vtkRenderWindow::New()' /usr/bin/ld: vtkProbeOpenGLVersion.cxx:(.text.startup+0x68): undefined reference to </code>vtkObjectBase::GetClassName() const’<br>
/usr/bin/ld: vtkProbeOpenGLVersion.cxx:(.text.startup+0x172): undefined reference to <code>vtkOutputWindow::GetInstance()' /usr/bin/ld: vtkProbeOpenGLVersion.cxx:(.text.startup+0x183): undefined reference to </code>vtkOutputWindow::GetInstance()’<br>
… many other undefined references</p>
</blockquote>
<p>It’s configured as follows :</p>
<blockquote>
<p>export LANG=C<br>
export LC_ALL=C<br>
export CFLAGS=“-I/usr/include/tirpc”<br>
export CXXFLAGS=“-I/usr/include/tirpc”<br>
cmake -DSlicer_VTK_VERSION_MAJOR:INT=8 -DQt5_DIR:PATH=/usr/lib/cmake/Qt5 -DBUILD_TESTING:BOOL=OFF -DCMAKE_BUILD_TYPE:STRING=Release -DADDITIONAL_CXX_FLAGS:STRING=-I/usr/include/tirpc …/Slicer</p>
</blockquote>
<p>I suppose libvtkCommon is not found during linking.</p>
<p>Reporting it in hope of a fix.</p>
<p>Regards.</p>

---

## Post #2 by @chir.set (2020-06-22 17:43 UTC)

<p>Built with clang 10.0 successfully at 76a41991e.</p>
<p>With commit 128fb86dd, there were linking errors as below :</p>
<blockquote>
<p>/usr/bin/ld: …/…/…/bin/libRemoteIO.so: undefined reference to <code>libssh2_init' /usr/bin/ld: ../../../bin/libRemoteIO.so: undefined reference to </code>libssh2_knownhost_free’<br>
/usr/bin/ld: …/…/…/bin/libRemoteIO.so: undefined reference to <code>libssh2_knownhost_get' /usr/bin/ld: ../../../bin/libRemoteIO.so: undefined reference to </code>libssh2_sftp_open_ex’<br>
/usr/bin/ld: …/…/…/bin/libRemoteIO.so: undefined reference to <code>libssh2_channel_wait_eof' /usr/bin/ld: ../../../bin/libRemoteIO.so: undefined reference to </code>libssh2_session_method_pref’<br>
/usr/bin/ld: …/…/…/bin/libRemoteIO.so: undefined reference to <code>libssh2_channel_wait_closed' /usr/bin/ld: ../../../bin/libRemoteIO.so: undefined reference to </code>libssh2_agent_init’<br>
/usr/bin/ld: …/…/…/bin/libRemoteIO.so: undefined reference to <code>libssh2_agent_list_identities' /usr/bin/ld: ../../../bin/libRemoteIO.so: undefined reference to </code>libssh2_agent_connect’<br>
/usr/bin/ld: …/…/…/bin/libRemoteIO.so: undefined reference to <code>libssh2_channel_send_eof' /usr/bin/ld: ../../../bin/libRemoteIO.so: undefined reference to </code>libssh2_userauth_keyboard_interactive_ex’<br>
/usr/bin/ld: …/…/…/bin/libRemoteIO.so: undefined reference to <code>libssh2_agent_disconnect' /usr/bin/ld: ../../../bin/libRemoteIO.so: undefined reference to </code>libssh2_scp_recv2’<br>
/usr/bin/ld: …/…/…/bin/libRemoteIO.so: undefined reference to `libssh2_hostkey_hash’</p>
</blockquote>
<p>With gcc 10.1, on top of VTK linking errors, numpy didn’t build, i.e, no *.so file was found.</p>
<p>Will continue with clang then.</p>

---

## Post #3 by @chir.set (2020-06-28 11:29 UTC)

<p>It turns out that the root cause is with the pull request I submitted <a href="https://github.com/Slicer/VTK/pull/28" rel="nofollow noopener">recently</a>. The ‘tags’ entry should not have been modified. It is set back to the previous value of ‘vtk-old’ in this <a href="https://github.com/Slicer/VTK/pull/29" rel="nofollow noopener">corrective</a> pull request.</p>
<p>This allows VTK to compile in a clean build, both with gcc 10.1 and clang 10.0. Moreover, no numpy errors are encountered.</p>
<p>However, this patch was necessary, to allow RemoteIO to link to ssh2.</p>
<pre><code>diff --git a/Libs/RemoteIO/CMakeLists.txt b/Libs/RemoteIO/CMakeLists.txt
index 65bd1b6183..23ca01b092 100644
--- a/Libs/RemoteIO/CMakeLists.txt
+++ b/Libs/RemoteIO/CMakeLists.txt
@@ -95,6 +95,7 @@ add_library(${lib_name} ${srcs})
 set(libs
   ${CURL_LIBRARIES}
   MRMLCore
+  ssh2
   )
 if(Slicer_USE_PYTHONQT_WITH_OPENSSL)
   list(APPEND libs
</code></pre>
<p>I hope the <a href="https://github.com/Slicer/VTK/pull/29" rel="nofollow noopener">corrective</a> request is merged in the Slicer/VTK tree.</p>

---

## Post #4 by @lassoan (2020-06-28 14:19 UTC)

<p>Thank you very much for working on this. We can merge the Slicer/VTK pull request if you touch it up a bit based on <a href="https://github.com/Slicer/VTK/pull/29#issuecomment-650766976">comments</a>. After that, please submit a pull request to Slicer/Slicer that uses the new Slicer/VTK hash and includes all other proposed changes (RemoteIO and anything else that you find necessary).</p>

---

## Post #5 by @chir.set (2020-06-28 16:16 UTC)

<p>I <a href="https://github.com/Slicer/VTK/commit/54838c2ac8f5f8521d4aa1d24988fb9ed1c715b4" rel="noopener nofollow ugc">amended</a> the last comment on the fork to be more explicit, and did a forced push. But I am not being able to create a new pull request; no command is available for this, and I am logged in.</p>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="4" data-topic="12150">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>please submit a pull request to Slicer/Slicer that uses the new Slicer/VTK hash and includes all other proposed changes (RemoteIO…</p>
</blockquote>
</aside>
<p>My first ever pull request has not been a success, so I’m somehow hesitant now.</p>

---

## Post #6 by @lassoan (2020-06-28 19:02 UTC)

<p>No need to create a new pull request, it is enough to change the content of the branch that the pull request was created for.</p>
<p>Maybe you forgot to rebase your branch on the latest version of the target branch.</p>

---

## Post #7 by @jcfr (2020-06-28 21:44 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="3" data-topic="12150">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>It turns out that the root cause is with the pull request I submitted <a href="https://github.com/Slicer/VTK/pull/28">recently </a>. The ‘tags’ entry should not have been modified. It is set back to the previous value of ‘vtk-old’ in this <a href="https://github.com/Slicer/VTK/pull/29">corrective </a> pull request.</p>
</blockquote>
</aside>
<p>Update to <code>update.sh</code> associated with commit  <a href="https://github.com/Slicer/VTK/commit/b4a181566f8510103333d32d19a567cd5a455a34">Slicer/VTK@b4a1815</a> (added to branch <a href="https://github.com/Slicer/VTK/commits/slicer-v8.2.0-2018-10-02-74d9488523">slicer-v8.2.0-2018-10-02-74d9488523</a>) is unlikely to be the source of the problem.</p>
<p>Indeed, we are not running this script while building VTK or Slicer.</p>
<p>I suggest we spend a little bit more time understanding the root cause of the problem. Since we do not call function  like <code>libssh2_agent_disconnect</code> in Slicer code, adding a dependency to <code>ssh2</code> does not seem to be the “right” fix.</p>

---

## Post #8 by @chir.set (2020-06-29 06:24 UTC)

<p>Well these are observational findings, perhaps related to Arch’s specifics, being so called ‘bleeding edge’ by nature.</p>
<p>I report these findings in case it’s known to you and a fix can be pointed to, or in case these findings might be useful in the future. I am well aware your build infrastructure is quite different and well described in your factory pages. I am not an IT pro, and won’t ever have such knowledge to venture in advanced tasks like a new pull request.</p>
<p>So in all, I’ll maintain locally a few tweaks that allow me to build Slicer.</p>
<p>As for the ssh2 issue, the new curl pulled in has much to do with ssh2 :</p>
<pre><code>LANG=C LC_ALL=C readelf -hs src/Slicer-SuperBuild/curl-build/lib/libcurl.a |grep ssh 
    30: 0000000000000000     0 NOTYPE  GLOBAL DEFAULT  UND Curl_ssh_init
    35: 0000000000000000     0 NOTYPE  GLOBAL DEFAULT  UND Curl_ssh_cleanup
     9: 0000000000000000    80 OBJECT  LOCAL  DEFAULT    4 ssh_buffer.0
    24: 0000000000000000     0 NOTYPE  GLOBAL DEFAULT  UND Curl_ssh_version
File: src/Slicer-SuperBuild/curl-build/lib/libcurl.a(libssh.c.o)
     1: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS libssh.c
File: src/Slicer-SuperBuild/curl-build/lib/libcurl.a(libssh2.c.o)
     1: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS libssh2.c
     5: 0000000000000000     9 FUNC    LOCAL  DEFAULT    1 my_libssh2_malloc
     6: 0000000000000010     9 FUNC    LOCAL  DEFAULT    1 my_libssh2_realloc
     7: 0000000000000020    17 FUNC    LOCAL  DEFAULT    1 my_libssh2_free
</code></pre>
<p>… …</p>
<p>May be I don’t interpret it rightly. I may of course give you more information you may need.</p>

---

## Post #9 by @hherhold (2020-07-07 16:35 UTC)

<p>Is there an update on this? I have the same problem building on MacOS 10.15.5 (undefined libssh references).</p>

---

## Post #10 by @hherhold (2020-07-10 17:25 UTC)

<p>Does anyone have a workaround to get MacOS builds going? I’ve installed libssh2, but I seem to be unable to tell CMake where to find it. I’ve added the ssh2 library line for RemoteIO (I realize this may be sub-optimal), but make is unable to find libssh2 in /usr/local - I checked link.txt and it does not have -L/usr/local/lib (where libssh2 is located). I’ve tried to add -L/usr/local/lib to what look like CMake LD flag settings, but make still doesn’t look in /usr/local/lib.</p>
<p>How do I add /usr/local/lib to the linker flags for RemoteIO?</p>
<p>Thanks!!</p>

---

## Post #11 by @hherhold (2020-07-15 13:27 UTC)

<p>OK, I think I figured this out. ssh2 is required for RemoteIO, but just adding ssh2 to CMakeLists.txt wasn’t sufficient for my setup - it didn’t know where to find libssh2.dylib. To tell it to get ssh2 from /usr/local (version 1.9.0_1 installed via HomeBrew), I had to add a call to find_library() and tell it to look in /usr/local/lib.</p>
<pre><code>diff --git a/Libs/RemoteIO/CMakeLists.txt b/Libs/RemoteIO/CMakeLists.txt
index 65bd1b618..a11163e9c 100644
--- a/Libs/RemoteIO/CMakeLists.txt
+++ b/Libs/RemoteIO/CMakeLists.txt
@@ -92,9 +92,12 @@ set(srcs ${RemoteIO_SRCS})

 add_library(${lib_name} ${srcs})

+find_library(SSH2_LIBRARY NAMES ssh2 PATHS /usr/local/lib)
+
 set(libs
   ${CURL_LIBRARIES}
   MRMLCore
+  ${SSH2_LIBRARY}
   )
 if(Slicer_USE_PYTHONQT_WITH_OPENSSL)
   list(APPEND libs
</code></pre>
<p>Now, I have no idea if this is the <em>right</em> solution, as <a class="mention" href="/u/jcfr">@jcfr</a> mentioned above. But at least it got the build going.</p>
<p>Any comments?</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #12 by @RafaelPalomar (2020-09-29 18:51 UTC)

<p>Hello,</p>
<p>I left a PR in here: <a href="https://github.com/Slicer/Slicer/pull/5209" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/pull/5209</a>. My solution is to disable libssh and libssh2 in curl; as pointed out by <a class="mention" href="/u/jcfr">@jcfr</a>, these are not used by Slicer.</p>
<p>I hope this is an ok solution.</p>
<p>Best,<br>
Rafael.</p>

---
