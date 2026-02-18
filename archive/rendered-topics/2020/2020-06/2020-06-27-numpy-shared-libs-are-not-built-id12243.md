# Numpy shared libs are not built

**Topic ID**: 12243
**Date**: 2020-06-27
**URL**: https://discourse.slicer.org/t/numpy-shared-libs-are-not-built/12243

---

## Post #1 by @chir.set (2020-06-27 15:18 UTC)

<p>I am trying to build at 04a58a9005. The built package misses all numpy shared libs, like _multiarray_umath.cpython-36m-x86_64-linux-gnu.so. This results in exceptions like</p>
<blockquote>
<p>ModuleNotFoundError: No module named ‘numpy.core._multiarray_umath’</p>
</blockquote>
<p>on start-up. These shared libs are simply not built at all, i.e, they are not excluded on packaging. I don’t have any clue about this.</p>
<p>Building on Arch Linux with clang 10 and cmake 3.17.3.</p>
<p>Can you advise for a fix ?</p>
<p>Thanks.</p>

---

## Post #2 by @chir.set (2020-06-27 15:31 UTC)

<p>Directory python-numpy is just empty in the superbuild tree, and python-numpy-prefix lists as follows :</p>
<pre><code>ls -l python-numpy-prefix/src/python-numpy-stamp/python-numpy-*
-rw-r--r-- 1 arc arc    0 27 juin  17:16 python-numpy-prefix/src/python-numpy-stamp/python-numpy-build
-rw-r--r-- 1 arc arc    0 27 juin  17:16 python-numpy-prefix/src/python-numpy-stamp/python-numpy-configure
-rw-r--r-- 1 arc arc    0 27 juin  17:16 python-numpy-prefix/src/python-numpy-stamp/python-numpy-done
-rw-r--r-- 1 arc arc    0 27 juin  16:20 python-numpy-prefix/src/python-numpy-stamp/python-numpy-download
-rw-r--r-- 1 arc arc    0 27 juin  16:20 python-numpy-prefix/src/python-numpy-stamp/python-numpy-generate_project_description
-rw-r--r-- 1 arc arc    0 27 juin  17:16 python-numpy-prefix/src/python-numpy-stamp/python-numpy-install
-rw-r--r-- 1 arc arc  223 27 juin  17:16 python-numpy-prefix/src/python-numpy-stamp/python-numpy-install-err.log
-rw-r--r-- 1 arc arc  447 27 juin  17:16 python-numpy-prefix/src/python-numpy-stamp/python-numpy-install-out.log
-rw-r--r-- 1 arc arc 2241 27 juin  16:17 python-numpy-prefix/src/python-numpy-stamp/python-numpy-install-Release.cmake
-rw-r--r-- 1 arc arc    0 27 juin  16:20 python-numpy-prefix/src/python-numpy-stamp/python-numpy-mkdir
-rw-r--r-- 1 arc arc    0 27 juin  16:20 python-numpy-prefix/src/python-numpy-stamp/python-numpy-patch
-rw-r--r-- 1 arc arc    0 27 juin  16:20 python-numpy-prefix/src/python-numpy-stamp/python-numpy-update
</code></pre>
<p>Most files are empty !</p>

---

## Post #4 by @lassoan (2020-06-27 15:35 UTC)

<p>Are you building in debug mode?</p>
<p>What command has triggered ModuleNotFound error? A simple <code>import numpy</code>?</p>

---

## Post #5 by @chir.set (2020-06-27 16:00 UTC)

<p>It’s a release build actually.</p>
<p>The ModuleNotFoundError is in console when starting Slicer itself.</p>
<p>Here is the content of numpy/core :</p>
<pre><code>ls programs/Slicer-4.11.0-2020-06-26-linux-amd64/lib/Python/lib/python3.6/site-packages/numpy/core/
_add_newdocs.py  _dtype_ctypes.py  function_base.py       _internal.py  multiarray.py    records.py          tests
arrayprint.py    _dtype.py         generate_numpy_api.py  lib           numeric.py       setup_common.py     _type_aliases.py
_asarray.py      einsumfunc.py     getlimits.py           machar.py     numerictypes.py  setup.py            _ufunc_config.py
cversions.py     _exceptions.py    include                memmap.py     overrides.py     shape_base.py       umath.py
defchararray.py  fromnumeric.py    __init__.py            _methods.py   __pycache__      _string_helpers.py  umath_tests.py
</code></pre>
<p>while there are many shared libs there in a normal build :</p>
<pre><code>cd programs/Slicer-4.11.0-2020-06-19-linux-amd64/lib/Python/lib/python3.6/site-packages/numpy/core/
#user@localhost core[0]$ ls *.so
_multiarray_tests.cpython-36m-x86_64-linux-gnu.so    _rational_tests.cpython-36m-x86_64-linux-gnu.so
_multiarray_umath.cpython-36m-x86_64-linux-gnu.so    _struct_ufunc_tests.cpython-36m-x86_64-linux-gnu.so
_operand_flag_tests.cpython-36m-x86_64-linux-gnu.so  _umath_tests.cpython-36m-x86_64-linux-gnu.so
</code></pre>
<p>None of these shared libs get built.</p>
<p>Thanks for considering.</p>

---

## Post #6 by @lassoan (2020-06-27 16:41 UTC)

<p>Linux build was successful a few days ago but there are no test results available on the dashboard, because of some network error: <a href="http://slicer.cdash.org/index.php?project=SlicerPreview">http://slicer.cdash.org/index.php?project=SlicerPreview</a></p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <span class="mention">@sjh26</span> could you have a look? The Linux build has been having this “build error” for a while now.</p>
<p><a class="mention" href="/u/chir.set">@chir.set</a> Do latest factory builds work correctly? If yes, then you can check out what exact built tools are used and how they differ from your configuration:</p>
<ul>
<li><a href="https://github.com/Slicer/DashboardScripts#maintenance-guides">https://github.com/Slicer/DashboardScripts#maintenance-guides</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory</a></li>
</ul>

---

## Post #7 by @chir.set (2020-06-27 17:41 UTC)

<p>Factory build works correctly at least. It means more complexity to install loadable extensions, like VMTK,  every time I unpack a factory build.</p>

---
