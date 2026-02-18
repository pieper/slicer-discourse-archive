# Build fails in vtkExodus on Linux

**Topic ID**: 12018
**Date**: 2020-06-14
**URL**: https://discourse.slicer.org/t/build-fails-in-vtkexodus-on-linux/12018

---

## Post #1 by @chir.set (2020-06-14 12:42 UTC)

<p>Hello,</p>
<p>After today’s pull, build fails on Linux with these messages :</p>
<blockquote>
<p>/usr/bin/ld: CMakeFiles/vtkexodusII.dir/src/ex_open_par.c.o:(.rodata+0x0): multiple definition of `exodus_unused_symbol_dummy_1’; CMakeFiles/vtkexodusII.dir/src/ex_create_par.c.o:(.rodata+0x0): first defined here<br>
collect2: error: ld returned 1 exit status<br>
make[6]: *** [ThirdParty/exodusII/vtkexodusII/CMakeFiles/vtkexodusII.dir/build.make:4172: lib/libvtkexodusII-8.2.so.1] Error 1<br>
make[5]: *** [CMakeFiles/Makefile2:8028: ThirdParty/exodusII/vtkexodusII/CMakeFiles/vtkexodusII.dir/all] Error 2<br>
make[5]: *** Waiting for unfinished jobs…<br>
make[4]: *** [Makefile:150: all] Error 2<br>
make[3]: *** [CMakeFiles/VTK.dir/build.make:137: VTK-prefix/src/VTK-stamp/VTK-build] Error 2<br>
make[2]: *** [CMakeFiles/Makefile2:1115: CMakeFiles/VTK.dir/all] Error 2<br>
make[1]: *** [CMakeFiles/Makefile2:224: CMakeFiles/Slicer.dir/rule] Error 2</p>
</blockquote>
<p>In hope of a fix,</p>
<p>Regards.</p>

---

## Post #2 by @lassoan (2020-06-14 15:03 UTC)

<p>If this was not a completely clear build (you updated an existing build tree) then please delete the entire top-level build directory of Slicer and start a new build.</p>

---

## Post #3 by @chir.set (2020-06-14 15:41 UTC)

<p>It was indeed a clean build, I forgot this important detail.</p>
<p>Configured and built as such :</p>
<blockquote>
<p>export CFLAGS=“-I/usr/include/tirpc”<br>
export CXXFLAGS=“-I/usr/include/tirpc”<br>
cmake -DSlicer_VTK_VERSION_MAJOR:INT=8 -DQt5_DIR:PATH=/usr/lib/cmake/Qt5 -DBUILD_TESTING:BOOL=OFF -DCMAKE_BUILD_TYPE:STRING=Release -DADDITIONAL_CXX_FLAGS:STRING=-I/usr/include/tirpc …/Slicer<br>
export LANG=C<br>
export LC_ALL=C<br>
make -j6</p>
</blockquote>
<p>The ‘tirpc’ path is specific to Arch.<br>
Using GCC 10.1.0, Qt 5.15.0.</p>

---

## Post #4 by @lassoan (2020-06-14 16:07 UTC)

<p>It looks like an error caused by gcc tightening some restrictions - <a href="https://gitlab.kitware.com/vtk/vtk/-/issues/17774">https://gitlab.kitware.com/vtk/vtk/-/issues/17774</a></p>
<p>We plan to upgrade to latest VTK soon. That version will contain the fix. <a class="mention" href="/u/jcfr">@jcfr</a> do you have an estimation of when the update may happen?</p>
<p>In the meantime, you may backport the fix to Slicer’s VTK or use an older gcc version.</p>

---

## Post #5 by @chir.set (2020-06-14 20:41 UTC)

<p>After backporting the available patch to Slicer’s VTK, the build process completes successfully.</p>
<p>For the record, it fails to build after downgrading GCC to 9.2; I suppose it’s related to the GCC version that built Arch’s  currently installed libraries.</p>
<p>Thanks.</p>
<p>-************************************************************************-</p>
<blockquote>
<p>/usr/bin/ld: /usr/lib/libQt5Widgets.so.5.15.0: undefined reference to <code>std::pmr::monotonic_buffer_resource::~monotonic_buffer_resource()@GLIBCXX_3.4.28' /usr/bin/ld: /usr/lib/libQt5Widgets.so.5.15.0: undefined reference to </code>vtable for std::pmr::monotonic_buffer_resource@GLIBCXX_3.4.28’<br>
collect2: error: ld returned 1 exit status<br>
make[6]: *** [CMakeFiles/CTKAppLauncher.dir/build.make:109: bin/CTKAppLauncher] Error 1<br>
make[5]: *** [CMakeFiles/Makefile2:227: CMakeFiles/CTKAppLauncher.dir/all] Error 2<br>
make[4]: *** [Makefile:172: all] Error 2<br>
make[3]: *** [CMakeFiles/CTKAppLauncherLib.dir/build.make:134: CTKAppLauncherLib-prefix/src/CTKAppLauncherLib-stamp/CTKAppLauncherLib-build] Error 2<br>
make[2]: *** [CMakeFiles/Makefile2:493: CMakeFiles/CTKAppLauncherLib.dir/all] Error 2<br>
make[2]: *** Waiting for unfinished jobs…<br>
Note: switching to ‘3.30.1’.</p>
</blockquote>

---

## Post #6 by @lassoan (2020-06-14 21:26 UTC)

<p>Great, thanks for the update. Could you send a pull request to Slicer’s VTK with the backported fix?</p>

---

## Post #7 by @chir.set (2020-06-14 21:50 UTC)

<p>This diff is easily obtained, but never did a pull request anywhere. Anyway, I 'll investigate ASAP, in daylight.</p>

---

## Post #8 by @chir.set (2020-06-15 10:40 UTC)

<p>The PR process is too heavy for such a trivial patch, I’m posting it here. Anyway, it follows the one you <a href="https://gitlab.kitware.com/vtk/vtk/-/issues/17774" rel="nofollow noopener">mentioned</a>.</p>
<pre><code>diff --git a/ThirdParty/exodusII/update.sh b/ThirdParty/exodusII/update.sh
index 21b1098191..db2450250a 100755
--- a/ThirdParty/exodusII/update.sh
+++ b/ThirdParty/exodusII/update.sh
@@ -8,7 +8,7 @@ readonly name="exodusII"
 readonly ownership="Seacas Upstream &lt;kwrobot@kitware.com&gt;"
 readonly subtree="ThirdParty/$name/vtk$name"
 readonly repo="https://gitlab.kitware.com/third-party/seacas.git"
-readonly tag="for/vtk-old"
+readonly tag="for/vtk-20200128-7.24f-v2019-12-18"
 readonly paths="
 packages/seacas/libraries/exodus/CMakeLists.vtk.txt
 packages/seacas/libraries/exodus/cmake/exodus_config.h.in
diff --git a/ThirdParty/exodusII/vtkexodusII/src/ex_create_par.c b/ThirdParty/exodusII/vtkexodusII/src/ex_create_par.c
index bf5bb44711..1286074fac 100644
--- a/ThirdParty/exodusII/vtkexodusII/src/ex_create_par.c
+++ b/ThirdParty/exodusII/vtkexodusII/src/ex_create_par.c
@@ -614,5 +614,5 @@ int ex_create_par_int(const char *path, int cmode, int *comp_ws, int *io_ws, MPI
  * Prevent warning in some versions of ranlib(1) because the object
  * file has no symbols.
  */
-const char exodus_unused_symbol_dummy_1;
+const char exodus_unused_symbol_dummy_ex_create_par;
 #endif
diff --git a/ThirdParty/exodusII/vtkexodusII/src/ex_open_par.c b/ThirdParty/exodusII/vtkexodusII/src/ex_open_par.c
index f379fc3496..c568353f52 100644
--- a/ThirdParty/exodusII/vtkexodusII/src/ex_open_par.c
+++ b/ThirdParty/exodusII/vtkexodusII/src/ex_open_par.c
@@ -474,5 +474,5 @@ int ex_open_par_int(const char *path, int mode, int *comp_ws, int *io_ws, float
  * Prevent warning in some versions of ranlib(1) because the object
  * file has no symbols.
  */
-const char exodus_unused_symbol_dummy_1;
+const char exodus_unused_symbol_dummy_ex_open_par;
 #endif</code></pre>

---

## Post #9 by @jcfr (2020-06-15 21:47 UTC)

<p>Thanks for the patch.</p>
<p>In fact, this is much simpler.</p>
<p>Could you fork <a href="https://github.com/Slicer/VTK">https://github.com/Slicer/VTK</a> ? And publish a Pull Request against the Slicer fork that based on <a href="https://github.com/Slicer/VTK/tree/slicer-v8.2.0-2018-10-02-74d9488523">https://github.com/Slicer/VTK/tree/slicer-v8.2.0-2018-10-02-74d9488523</a> adding the commit ?  Once this is done, we will take care of integrating it and updating Slicer.</p>
<p>Thanks for your help <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=9" title=":pray:" class="emoji" alt=":pray:"></p>
<p>To learn more about the Slicer fork, read here: <a href="https://github.com/Slicer/VTK">https://github.com/Slicer/VTK</a></p>

---

## Post #10 by @lassoan (2020-06-16 02:42 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> I find the process described here quite complicated, too. My impression is that a new branch has to be created for each pull request, but it is not clear why or how exactly it should be named.</p>

---

## Post #11 by @jcfr (2020-06-16 13:05 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Here is a pull request adding “How to backport changes to a specific branch ?”  section to the README. See <a href="https://github.com/Slicer/VTK/pull/27" class="inline-onebox">README: Add "How to backport changes to a specific branch ?" by jcfr · Pull Request #27 · Slicer/VTK · GitHub</a></p>
<blockquote>
<p>My impression is that a new branch has to be created for each pull request</p>
</blockquote>
<p>The introduction of this new README entry should help clarify</p>
<blockquote>
<p>it is not clear why or how exactly it should be named</p>
</blockquote>
<p>The branch is named after the commit common to both the upstream project and the Slicer fork. It allows to clearly identify the divergence point.</p>

---

## Post #12 by @chir.set (2020-06-16 15:07 UTC)

<p>The pull request is <a href="https://github.com/Slicer/VTK/pull/28" rel="nofollow noopener">visible</a>. I hope it’s rightly done, for something new to me.</p>

---

## Post #13 by @jcfr (2020-06-17 02:47 UTC)

<p>Thanks. Both Slicer/VTK fork and Slicer have been updated.<br>
For reference, see <a href="https://github.com/Slicer/Slicer/pull/4990">https://github.com/Slicer/Slicer/pull/4990</a></p>

---

## Post #14 by @chir.set (2020-06-22 17:46 UTC)

<p>Amongst the many <a href="https://gcc.gnu.org/gcc-10/changes.html" rel="nofollow noopener">changes</a> in GCC 10, the use of -fno-common by default explains this behaviour. The fix is therefore valid, moreover explained <a href="https://wiki.gentoo.org/wiki/Gcc_10_porting_notes/fno_common" rel="nofollow noopener">here</a>; except that I don’t know the effect of the ‘tags’ change in the patch.</p>
<p>I am seeing linking issues with GCC 10, despite the patch now, reported <a href="https://discourse.slicer.org/t/build-fails-in-vtk-many-undefined-references/12150">here</a>. Going with clang for now.</p>

---
