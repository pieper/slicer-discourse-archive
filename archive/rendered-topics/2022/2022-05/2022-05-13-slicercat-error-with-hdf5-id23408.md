---
topic_id: 23408
title: "Slicercat Error With Hdf5"
date: 2022-05-13
url: https://discourse.slicer.org/t/23408
---

# SlicerCAT error with hdf5

**Topic ID**: 23408
**Date**: 2022-05-13
**URL**: https://discourse.slicer.org/t/slicercat-error-with-hdf5/23408

---

## Post #1 by @fbordignon (2022-05-13 12:59 UTC)

<p>Hello everyone<br>
I am having an issue with my custom app on linux that I am not sure if it is something related with my modifications or SlicerCAT in general.</p>
<p>Can someone test the following on a custom app on linux with python 3.9, please?</p>
<p>Slicer(custom app) console:</p>
<pre><code class="lang-python">pip_install("h5py")
pip_install("netcdf4")
import h5py
import netCDF4
</code></pre>
<p>it is crashing upon import on libhdf5.so which both packages carry as dependencies. On Slicer 5.1 this is fine and properly handled, i.e. both packages install and load ok. I don’t even know how to handle it. One thing that comes to mind is building both packages with the same libhdf5, but if it is something wrong with the build I want to try and fix it. Thanks</p>

---

## Post #2 by @cpinter (2022-05-13 13:10 UTC)

<p>I tested it with a custom app (it uses Slicer 4.11) and the last line made it crash for me as well on Ubuntu 20.04.4.</p>

---

## Post #3 by @fbordignon (2022-05-13 13:17 UTC)

<p>Thanks <a class="mention" href="/u/cpinter">@cpinter</a>. Mine is using Slicer 4.11 as well but with python 3.9. Which version is your python?<br>
Just to be sure, the crash you are talking about is Slicer exiting completely, right? Thanks</p>

---

## Post #4 by @jamesobutler (2022-05-13 13:56 UTC)

<p>On Windows, using a Slicer custom app based on Slicer 4.13 (commit just prior to 5.0 tag) the following installs and import were successful. This Slicer version is using Python 3.9.</p>

---

## Post #5 by @jamesobutler (2022-05-13 14:07 UTC)

<p>Note that Slicer 4.11.20210226 was using ITK 5.1.2 which specifies HDF5 1.10.4 (see <a href="https://github.com/InsightSoftwareConsortium/ITK/tree/v5.1.2/Modules/ThirdParty/HDF5/src/itkhdf5" rel="noopener nofollow ugc">here</a>), while latest Slicer uses ITK 5.3rc03 which specifies HDF5 1.12.1 (see <a href="https://github.com/InsightSoftwareConsortium/ITK/tree/v5.3rc03/Modules/ThirdParty/HDF5/src/itkhdf5" rel="noopener nofollow ugc">here</a>).</p>
<p>On Windows it appears the latest version of h5py whls (3.6.0) build against HDF5 1.12.1 (see <a href="https://github.com/h5py/h5py/blob/3.6.0/azure-pipelines.yml#L43" rel="noopener nofollow ugc">here</a>).</p>

---

## Post #6 by @cpinter (2022-05-13 14:34 UTC)

<p>Python version is 3.6.7. Yes it exits completely: <code>error: [/home/...App-real] exit abnormally - Report the problem.</code></p>

---

## Post #7 by @lassoan (2022-05-15 12:37 UTC)

<p>ITK and VTK use custom prefix in the HDF shared library name and symbols, so there should not be any conflicts (ABI compatibility issues) with system HDF or any other HDF versions installed by Python packages.</p>
<p>Have you configured your custom Slicer build to use system HDF? That could break this isolation.</p>
<p>If Python packages include HDF as shared library then it may lead to conflicts, too.</p>

---

## Post #8 by @fbordignon (2022-05-16 12:57 UTC)

<p>Hey <a class="mention" href="/u/lassoan">@lassoan</a> thanks for the tips. I will check the build configs but I can see the HDF libs with custom prefixes on the package (libiktIO and libvtk). One thing to notice is that If I use the console (PythonSlicer) it is fine importing h5py and netCDF4. So it must be something that Slicer imports/does.</p>
<p>I’ve built the <a href="https://github.com/KitwareMedical/SlicerCAT" rel="noopener nofollow ugc">SlicerCAT example</a> with Slicer <a href="https://github.com/Slicer/Slicer/commit/260478f415f50d377c5df076340fbf3e82c5a709" rel="noopener nofollow ugc">260478f</a> (Slicer 5) and the problems I am reporting here are solved.</p>
<p>I am on a crossroads now. Slicer 4.11 is still the supported version but I understand that we are on the verge on changing to v5. I will spend a little more time on this if no easy solution is found I will abandon it in favor of using Slicer v5.</p>

---

## Post #9 by @keri (2022-05-16 15:20 UTC)

<p>To exclude the doubts whether it is because of your modification or not I would try to run SlicerCAT without modules:</p>
<pre><code class="lang-auto">./SlicerCAT --disable-modules
</code></pre>
<p>If without modules the SlicerCAT runs fine with h5py I would try to disable only some suspicious modules:</p>
<pre><code class="lang-auto">./SlicerCAT --modules-to-ignore qSlicerModule1,qSlicerModule2
</code></pre>

---

## Post #10 by @fbordignon (2022-05-16 16:30 UTC)

<p>Good tip, thanks! Unfortunately I had the same crash.</p>

---

## Post #11 by @keri (2022-05-16 17:00 UTC)

<p>I can see that in Slicer (4 I think) both VTK and ITK have compiled HDF5 libs.<br>
Also as I remember (worse to check) <code>h5py</code> uses native C hdf5 library (not a high level <code>_hl</code>).</p>
<p>Thus I can find:</p>
<pre><code class="lang-auto">/home/kerim/Documents/Slicer/d/VTK-build/lib/libvtkhdf5-9.1.so
/home/kerim/Documents/Slicer/d/ITK-build/lib/libitkhdf5-shared-5.3_debug.so
and also I expect there should be `site-packages/h5py/libhdf5.so`
</code></pre>
<p>As you said there is no problem to import <code>h5py</code> to python without Slicer. It might be because you don’t import VTK’s HDF5 and ITK’s hdf5 along with h5py’s hdf5.</p>
<p>As HDF5 is a pure C library I would try to import them to PythonSlicer and then to Slicer directly. I haven’t done this before but <a href="https://stackoverflow.com/questions/145270/calling-c-c-from-python#:~:text=from%20ctypes%20import%20cdll%0Alib%20%3D%20cdll.LoadLibrary(%27./libfoo.so%27)" rel="noopener nofollow ugc">google</a> tells me that it may be done via:</p>
<pre><code class="lang-auto">from ctypes import cdll
itkhdf5 = cdll.LoadLibrary('/path/to/itkhdf5.so')
vtkhdf5 = cdll.LoadLibrary('/path/to/vtkhdf5.so')
pyhdf5 = cdll.LoadLibrary('/path/to/h5pyhdf5.so')
</code></pre>
<p>I hope an exception is raised.</p>

---

## Post #12 by @keri (2022-05-16 18:00 UTC)

<p><a class="mention" href="/u/fbordignon">@fbordignon</a> sorry, my previous post didn’t work.<br>
I tested it on pure Slicer 4 LTS.</p>
<p>I discovered that if I import <code>netCDF4</code> first and then <code>import h5py</code> then the app fails at the <a href="https://github.com/h5py/h5py/blob/8b40fbb29b9551a0e6751405283886582585738a/h5py/__init__.py#L25" rel="noopener nofollow ugc">h5py.<strong>init</strong> line</a> when importing <code>_errors.cpython-36m-x86_64-linux-gnu.so</code> lib (you can set <code>print()</code> in it to check)</p>
<p>And <code>_errors</code> lib contains <code>H5E_</code> functions (exceptions). I got this with <code>nm -gD  _errors.cpython-36m-x86_64-linux-gnu.so</code></p>

---

## Post #13 by @fbordignon (2022-05-16 18:37 UTC)

<p><a class="mention" href="/u/keri">@keri</a> thanks for your suggestions, but when doing <code>cdll.LoadLibrary</code> no functions from the libraries are called.<br>
I believe there is something wrong with the initialization of the library that is issuing a segfault.<br>
These are the backtraces I am having. The error always occur on the last lib imported. i.e if I import netCDF4 and then h5py, the error is on h5py and vice-versa.</p>
<p>This error is on the interactive python console of the custom app. If I issue these commands on a PythonSlicer console they import both libs fine. i.e. they are somewhat isolated from each other.</p>
<details>
<summary>
Error netCDF4</summary>
<p>Thread 2.1 “GeoSlicerApp-re” received signal SIGSEGV, Segmentation fault.<br>
[Switching to Thread 0x7fffbafbd540 (LWP 3789)]<br>
0x00007ffe4661d91d in ?? () from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/lib/Python/lib/python3.9/site-packages/netCDF4/…/netCDF4.libs/libhdf5-02fc656b.so.200.0.0<br>
(gdb) bt<br>
<span class="hashtag">#0</span>  0x00007ffe4661d91d in ?? ()<br>
from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/lib/Python/lib/python3.9/site-packages/netCDF4/…/netCDF4.libs/libhdf5-02fc656b.so.200.0.0<br>
<span class="hashtag">#1</span>  0x00007ffe466221f8 in H5SL_create ()<br>
from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/lib/Python/lib/python3.9/site-packages/netCDF4/…/netCDF4.libs/libhdf5-02fc656b.so.200.0.0<br>
<span class="hashtag">#2</span>  0x00007ffe464f2989 in H5I_register_type ()<br>
from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/lib/Python/lib/python3.9/site-packages/netCDF4/…/netCDF4.libs/libhdf5-02fc656b.so.200.0.0<br>
<span class="hashtag">#3</span>  0x00007ffe46721aa2 in H5VL__init_package ()<br>
from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/lib/Python/lib/python3.9/site-packages/netCDF4/…/netCDF4.libs/libhdf5-02fc656b.so.200.0.0<br>
<span class="hashtag">#4</span>  0x00007ffe46721b9a in H5VL_init_phase1 ()<br>
from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/lib/Python/lib/python3.9/site-packages/netCDF4/…/netCDF4.libs/libhdf5-02fc656b.so.200.0.0<br>
<span class="hashtag">#5</span>  0x00007ffe4630d43e in H5_init_library ()<br>
from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/lib/Python/lib/python3.9/site-packages/netCDF4/…/netCDF4.libs/libhdf5-02fc656b.so.200.0.0<br>
<span class="hashtag">#6</span>  0x00007ffe4630dedf in H5get_libversion ()<br>
from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/lib/Python/lib/python3.9/site-packages/netCDF4/…/netCDF4.libs/libhdf5-02fc656b.so.200.0.0<br>
<span class="hashtag">#7</span>  0x00007ffe46a8bbe1 in ?? ()<br>
from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/lib/Python/lib/python3.9/site-packages/netCDF4/_netCDF4.cpython-39-x86_64-linux-gnu.so<br>
<span class="hashtag">#8</span>  0x00007ffe46a85b86 in ?? ()<br>
from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/lib/Python/lib/python3.9/site-packages/netCDF4/_netCDF4.cpython-39-x86_64-linux-gnu.so<br>
<span class="hashtag">#9</span>  0x00007ffe46a777d6 in ?? ()<br>
from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/lib/Python/lib/python3.9/site-packages/netCDF4/_netCDF4.cpython-39-x86_64-linux-gnu.so<br>
<span class="hashtag">#10</span> 0x00007fffe18bf33a in PyModule_ExecDef ()<br>
from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/bin/…/lib/Python/lib/libpython3.9.so<br>
<span class="hashtag">#11</span> 0x00007fffe19a386b in ?? () from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/bin/…/lib/Python/lib/libpython3.9.so<br>
<span class="hashtag">#12</span> 0x00007fffe18bdcf3 in ?? () from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/bin/…/lib/Python/lib/libpython3.9.so<br>
<span class="hashtag">#13</span> 0x00007fffe1852954 in PyVectorcall_Call ()<br>
from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/bin/…/lib/Python/lib/libpython3.9.so</p>
</details>
<p>//////////////////////////////////////////////////////</p>
<details>
<summary>
Error h5py</summary>
<p>Thread 2.1 “GeoSlicerApp-re” received signal SIGSEGV, Segmentation fault.<br>
[Switching to Thread 0x7fffbafbd540 (LWP 3848)]<br>
0x00007fffbf9178b1 in __vfprintf_internal (s=s@entry=0x7fffff7ff450, format=format@entry=0x7ffe47dd8bb5 “can’t locate ID”, ap=ap@entry=0x7fffff7ff5a8, mode_flags=mode_flags@entry=0) at vfprintf-internal.c:1289<br>
1289	vfprintf-internal.c: No such file or directory.<br>
(gdb) bt<br>
<span class="hashtag">#0</span>  0x00007fffbf9178b1 in __vfprintf_internal (s=s@entry=0x7fffff7ff450, format=format@entry=0x7ffe47dd8bb5 “can’t locate ID”,<br>
ap=ap@entry=0x7fffff7ff5a8, mode_flags=mode_flags@entry=0) at vfprintf-internal.c:1289<br>
<span class="hashtag">#1</span>  0x00007fffbf92cbfa in __vasprintf_internal (result_ptr=0x7fffff7ff5a0, format=0x7ffe47dd8bb5 “can’t locate ID”, args=0x7fffff7ff5a8, mode_flags=0)<br>
at vasprintf.c:57<br>
<span class="hashtag">#2</span>  0x00007ffe47b55417 in H5E_printf_stack ()<br>
from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/lib/Python/lib/python3.9/site-packages/h5py/…/h5py.libs/libhdf5-346dbfc8.so.200.1.0<br>
<span class="hashtag">#3</span>  0x00007ffe47be470c in H5I_inc_ref ()<br>
from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/lib/Python/lib/python3.9/site-packages/h5py/…/h5py.libs/libhdf5-346dbfc8.so.200.1.0<br>
<span class="hashtag">#4</span>  0x00007ffe47b55243 in H5E__push_stack ()<br>
from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/lib/Python/lib/python3.9/site-packages/h5py/…/h5py.libs/libhdf5-346dbfc8.so.200.1.0<br>
<span class="hashtag">#5</span>  0x00007ffe47b55444 in H5E_printf_stack ()<br>
from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/lib/Python/lib/python3.9/site-packages/h5py/…/h5py.libs/libhdf5-346dbfc8.so.200.1.0<br>
<span class="hashtag">#6</span>  0x00007ffe47be470c in H5I_inc_ref ()<br>
from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/lib/Python/lib/python3.9/site-packages/h5py/…/h5py.libs/libhdf5-346dbfc8.so.200.1.0<br>
<span class="hashtag">#7</span>  0x00007ffe47b55243 in H5E__push_stack ()<br>
from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/lib/Python/lib/python3.9/site-packages/h5py/…/h5py.libs/libhdf5-346dbfc8.so.200.1.0<br>
<span class="hashtag">#8</span>  0x00007ffe47b55444 in H5E_printf_stack ()<br>
from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/lib/Python/lib/python3.9/site-packages/h5py/…/h5py.libs/libhdf5-346dbfc8.so.200.1.0<br>
<span class="hashtag">#9</span>  0x00007ffe47be470c in H5I_inc_ref ()<br>
from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/lib/Python/lib/python3.9/site-packages/h5py/…/h5py.libs/libhdf5-346dbfc8.so.200.1.0<br>
<span class="hashtag">#10</span> 0x00007ffe47b55243 in H5E__push_stack ()<br>
from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/lib/Python/lib/python3.9/site-packages/h5py/…/h5py.libs/libhdf5-346dbfc8.so.200.1.0<br>
<span class="hashtag">#11</span> 0x00007ffe47b55444 in H5E_printf_stack ()<br>
from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/lib/Python/lib/python3.9/site-packages/h5py/…/h5py.libs/libhdf5-346dbfc8.so.200.1.0<br>
<span class="hashtag">#12</span> 0x00007ffe47be470c in H5I_inc_ref ()<br>
from /home/fernando/Downloads/GeoSlicer-1.6.0-2022-05-11-linux-amd64/lib/Python/lib/python3.9/site-packages/h5py/…/h5py.libs/libhdf5-346dbfc8.so.20</p>
</details>
<p>I’ve updated my custom Slicer app to the latest ITK v5.3rc something and it did not solve the issue.<br>
I noticed that on Linux and Windows if I issue <code>import sitkUtils</code> it crashes the custom app.</p>

---

## Post #14 by @fbordignon (2022-05-16 18:55 UTC)

<p>Sorry, I assumed at first that this was a problem related to SlicerCAT but it is related to Slicer 4.11<br>
Download <a href="https://download.slicer.org/bitstream/60add706ae4540bf6a89bf98" rel="noopener nofollow ugc">Slicer version 4.11.20210226 revision 29738 built 2021-02-27</a> for linux<br>
On the interactive console:</p>
<pre><code class="lang-python">pip_install("--upgrade pip")
pip_install("h5py netcdf4")
import h5py, netCDF4
</code></pre>
<p>crashes</p>
<p>On PythonSlicer executable after the above commands were executed:</p>
<pre><code class="lang-python">import h5py, netCDF4
</code></pre>
<p>runs fine.</p>
<p>EDIT: maybe it is related with <a href="https://gitlab.kitware.com/vtk/vtk/-/issues/18514" class="inline-onebox" rel="noopener nofollow ugc">libvtkhdf5 contains unmangled symbols (#18514) · Issues · VTK / VTK · GitLab</a></p>

---

## Post #15 by @keri (2022-05-16 19:40 UTC)

<p>I think the problem is that there are too many HDF5 libs (ITK, VTK, h5py, netCDF4)</p>
<p>In my SlicerCAT I build HDF5 as external project and set it to VTK and ITK. So my system has only one instance of HDF5.<br>
I just reproduced your “fail” steps on my SlicerCAT on clean Ubuntu 22.04:</p>
<pre><code class="lang-auto">pip_install("h5py")
pip_install("netcdf4")
import h5py
import netCDF4
</code></pre>
<p>and it didn’t crash:</p>
<p>SlicerCAT is built upon Slicer <a href="https://github.com/Slicer/Slicer/tree/564ccb319c099d3772a74aea974d6e29075c7593" rel="noopener nofollow ugc">564ccb319c099d3772a74aea974d6e29075c7593</a> (14 may 2022)</p>
<p>Lately <a href="https://discourse.slicer.org/t/simpleitk-install-fails-on-windows/23373/8">we had a conversation</a> with <a class="mention" href="/u/lassoan">@lassoan</a> that it would be good to build HDF5 as an external project.<br>
It is not a problem but don’t have time for this now.</p>
<p>In the future I will add a PR.</p>
<p>If you can’t wait (one-two months I think) you can take a look how I <a href="https://discourse.slicer.org/t/simpleitk-install-fails-on-windows/23373/9">configured External_VTK.cmake and External_ITK.cmake</a>. And there you can find External_HDF5.cmake but it probably should be modified to allow building against specific HDF5 version (probably you would want h5py to work with the same HDF5 version)</p>

---

## Post #16 by @lassoan (2022-05-16 21:12 UTC)

<aside class="quote no-group" data-username="keri" data-post="15" data-topic="23408">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>I think the problem is that there are too many HDF5 libs (ITK, VTK, h5py, netCDF4)</p>
</blockquote>
</aside>
<p>This is only a problem if an application or library brings its own HDF5 as a shared library, without shared library name or symbol mangling.</p>
<p><strong>ITK and VTK behave well</strong> - their HDF5 will not clash with anything (other than potentially another ITK and VTK), unless you force using “system” HDF5. If you force ITK or VTK to use "system HDF5 then it is entirely up to you to manage version conflicts.</p>
<p>I’ve checked the wheel files of netcdf4 and h5py.</p>
<p><strong>netcdf4 behaves well</strong> - it links HDF5 staticallly, so there are no conflicts.</p>
<p><strong>h5py is messed up</strong> - it includes shared libraries with non-mangled names (<code>hdf5.dll</code>, <code>hdf5_hl.dll</code>, and even a <code>zlib.dll</code>). This can crash any application that uses HDF5 or zlib. An application or the system may provide a common shared library without name and symbol mangling, but a Python package must never do this (they must not dictate an application what HDF5 it may use). I would recommend not to use this package (or maybe build it yourself, as a static build, if that is supported).</p>

---

## Post #17 by @keri (2022-05-16 22:38 UTC)

<p>Thank you for explanation,</p>
<p>I don’t understand why non-mangled <code>hdf5</code> may crash the app in that sutiation.</p>
<p>This is how I understand this:<br>
VTK and ITK have completely “separeted” name mangled HDF5. That means they use only their own HDF5: instead of <code>H5D_close</code> ITK uses <code>itk_H5D_close</code>.</p>
<p>Then <code>h5py</code> uses unmangled HDF5: it uses <code>H5D_close</code>.</p>
<p>if <code>netCDF4</code> links to HDF5 statically then does that mean that it can’t use <code>h5py</code>’s HDF5? I don’t know that, but the app crashes after <code>h5py</code> and <code>netCDF4</code> imported together (along with ITK and VTK).</p>
<p>I can see two hints why this may happen:</p>
<ol>
<li>If I try to look in HDF5 lib object names (I believe this could be done with <code>nm -gD libitkhdf5-shared-5.3_debug.so</code>) I can see that most function names are prefixed with <code>itk_</code> but there are also some of them without name mangling:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/329faeab7cbe7f67968fecc1ec1a5d408fbb23d2.jpeg" alt="image" data-base62-sha1="7dPZsu6eEsy0BnDKb37WGCvclSq" width="495" height="325">
</li>
<li>may two HDF5 libs of the same version without name mangling be loaded together or this is impossible or that leads to crash?</li>
<li>probably these two unmangled HDF5 libs are of different version or compiled with different compilers (compiler flags)</li>
</ol>
<p>I don’t have enough of theoretical knowledge so I’m not sure about it.<br>
But:<br>
VTK+ITK+h5py = OK<br>
VTK+ITK+netCDF4 = OK<br>
h5py+netCDF4  = OK<br>
VTK+ITK+h5py+netCDF4 = CRASH <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>(ITK and VTK here are meant as VTK’s and ITK’s HDF5)</p>
<p>I tested on my SlicerCAT where ITK=VTK=HDF5 v1.12 and h5py and netCDF4 are installed with <code>pip_install</code> then:<br>
VTK+ITK+h5py+netCDF4 = OK <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>I thought that it would be better to build HDF5 externally and set it as a VTK and ITK dependency with the ability to set desired HDF5 version so that if <code>h5py</code> is intented to be used then it was possible to prepare needed version.</p>

---

## Post #18 by @lassoan (2022-05-16 23:20 UTC)

<aside class="quote no-group" data-username="keri" data-post="17" data-topic="23408">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>I don’t understand why non-mangled <code>hdf5</code> may crash the app in that sutiation.</p>
<p>This is how I understand this:<br>
VTK and ITK have completely “separeted” name mangled HDF5. That means they use only their own HDF5: instead of <code>H5D_close</code> ITK uses <code>itk_H5D_close</code> .</p>
</blockquote>
</aside>
<p>VTK’s and ITK’s HDF5 are only isolated if you don’t force them to use your own (“system”) HDF5.</p>
<aside class="quote no-group quote-modified" data-username="keri" data-post="17" data-topic="23408">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>if <code>netCDF4</code> links to HDF5 statically then does that mean that it can’t use <code>h5py</code> 's HDF5?</p>
</blockquote>
</aside>
<p>It means netCDF is self-contained, it does not rely on a shared library. It does not use or interfere with any HDF5 shared libraries.</p>
<aside class="quote no-group" data-username="keri" data-post="17" data-topic="23408">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>I thought that it would be better to build HDF5 externally and set it as a VTK and ITK dependency</p>
</blockquote>
</aside>
<p>If you build HDF5 externally and want to use that in ITK and VTK then it is up to you to ensure that your custom HDF5 does not clash with h5py’s HDF5. You either have to use the exact same version, built with the same options, or build your HDF5 with library name and symbol mangling.</p>
<aside class="quote no-group" data-username="keri" data-post="17" data-topic="23408">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>I can see that most function names are prefixed with <code>itk_</code> but there are also some of them without name mangling:</p>
</blockquote>
</aside>
<p>These seem to be some private/debug functions. It may be normal that they are not name-mangled, but maybe it is an error. Mixing libraries built in debug and release mode (or built with slightly different options) may cause crashes, too.</p>
<aside class="quote no-group" data-username="keri" data-post="17" data-topic="23408">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>may two HDF5 libs of the same version without name mangling be loaded together or this is impossible or that leads to crash?</p>
</blockquote>
</aside>
<p>Even if you build the same HDF5 version, there may be compiler or library build option differences between your build and the third-party-built binary that can cause crash. It is safer to isolate your binaries.</p>
<aside class="quote no-group" data-username="keri" data-post="17" data-topic="23408">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>h5py+netCDF4 = OK<br>
VTK+ITK+h5py+netCDF4 = CRASH</p>
</blockquote>
</aside>
<p>It seems that netCDF4 uses a HDF5 shared library on linux. So, unless you are lucky (they all happen to use the same HDF5 version, built with the same options) you cannot use both h5py and netCDF wheels at the same time on linux. You should be able to build both from source though, forcing both of them to use some common HDF5 version.</p>

---

## Post #19 by @fbordignon (2022-05-17 14:18 UTC)

<p>From what I looked up recently, the wheels distributed under manylinux tags are compatible with various standards using <a href="https://github.com/pypa/auditwheel" rel="noopener nofollow ugc">auditwheel</a> to rename the .so libs and allow for various wheels to use dependencies that would otherwise clash. This <a href="https://github.com/pypa/auditwheel/issues/79" rel="noopener nofollow ugc">issue</a> discusses some problems with this approach. It seems like if a thirdparty lib loads the symbol globally, then the mechanism implemented in auditwheel does not work, i.e. something loads global hdf5 symbols, then the python wheels will call that symbols and crash.<br>
It seems to me that even though the symbols of netCDF4 and h5py are not mangled, they can work together because of the auditwheel steps that are also present on macOS via delocate.</p>
<p>if I issue:</p>
<pre><code class="lang-auto">nm -gD lib/GeoSlicer-4.11/libvtkhdf5-8.2.so.1 | grep -v vtk
</code></pre>
<p>There are some symbols without the prefix vtk</p>
<details>
<summary>
unmangled symbols</summary>
<p>00000000005dd0be B H5AC_init_g<br>
00000000005dd0bc B H5A_init_g<br>
00000000005dcc46 B H5_api_entered_g<br>
00000000005dd0c0 B H5B2_init_g<br>
00000000005dd0bf B H5B_init_g<br>
00000000005dd0c1 B H5C_init_g<br>
00000000005dee00 B H5D_def_dxpl_cache<br>
00000000005decc0 B H5_debug_g<br>
00000000005dd0c2 B H5D_init_g<br>
00000000005de331 B H5EA_init_g<br>
00000000005de330 B H5E_init_g<br>
00000000005dee60 B H5E_stack_g<br>
00000000005de340 B H5FA_init_g<br>
00000000005de348 B H5FD_init_g<br>
00000000005de332 B H5F_init_g<br>
00000000005de3b0 B H5FL_init_g<br>
00000000005de338 B H5F_sfile_head_g<br>
00000000005de400 B H5FS_init_g<br>
00000000005de401 B H5G_init_g<br>
00000000005de403 B H5HF_init_g<br>
00000000005de404 B H5HG_init_g<br>
00000000005de405 B H5HL_init_g<br>
00000000005de420 B H5I_init_g<br>
00000000005dcc45 B H5_libinit_g<br>
00000000005dcc44 B H5_libterm_g<br>
00000000005de838 B H5L_init_g<br>
00000000005de858 B H5MF_init_g<br>
00000000005de859 B H5MP_init_g<br>
00000000005de85a B H5O_init_g<br>
00000000005de948 B H5PB_init_g</p>
</details>
<p>on Slicer 5</p>
<pre><code class="lang-auto">nm -gD lib/libvtkhdf5-9.1.so.1 | grep -v vtk
</code></pre>
<p>no H5* symbols appear at the output.<br>
This corroborates with my thesis that vtk is loading those symbols in some manner and it is corrected in Slicer 5 via the new vtk version which has the fix <a href="https://gitlab.kitware.com/vtk/vtk/-/issues/18514" rel="noopener nofollow ugc">linked before</a>. I am trying to update hdf5 for vtk on Slicer 4.11 to see if it is really the case.</p>

---

## Post #20 by @fbordignon (2022-05-17 19:16 UTC)

<p>Updating the hdf5 lib inside VTK was proving to be difficult because it needs a big jump so I’ve forked VTK from the commit hash of Slicer 4.11 and only added the mangling defines from VTK 9.1. It works! <a href="https://github.com/fbordignon/VTK/commit/757ae364f70f6ff9dba741a359eb0ccfa349bee0" rel="noopener nofollow ugc">This commit</a> made it work fine, no more symbols are unmangled on libvtkhdf5. I’ve merged the defines from vtk 8 and 9 so probably there are some that are not needed, but I figure it does not hurt.<br>
I don’t know if Slicer 4 will be given maintenance after Slicer 5 is released but it is a small enough fix. Now I can import h5py and netCDF4 without crashing <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #21 by @keri (2022-06-07 23:43 UTC)

<p><a href="https://github.com/Slicer/Slicer/pull/6415" rel="noopener nofollow ugc">PR is ready</a><br>
It builds HDF5 as external project that is used by both VTK and ITK</p>

---

## Post #22 by @jamesobutler (2022-06-07 23:53 UTC)

<p><a class="mention" href="/u/fbordignon">@fbordignon</a> I wanted to point out to you that VTK8 support has now been removed from latest Slicer. I know you’ve been piecing together older Slicer with newer Python and other mixing of new and old stuff. Did you get around to updating your application to use latest version of Slicer? There won’t be maintenance of Slicer 4 branches now that Slicer 5 is officially released and available to download.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/b9ac6ed61cae9de90986eaf8766c0e8b1b4461c1">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/b9ac6ed61cae9de90986eaf8766c0e8b1b4461c1" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/b9ac6ed61cae9de90986eaf8766c0e8b1b4461c1" target="_blank" rel="noopener nofollow ugc">COMP: Remove support for VTK8</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2022-06-07" data-time="21:10:35" data-timezone="UTC">09:10PM - 07 Jun 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="changed 58 files with 36 additions and 670 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/b9ac6ed61cae9de90986eaf8766c0e8b1b4461c1" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+36</span>
          <span class="removed">-670</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Build support for VTK8 or VTK9 was introduced in October 2020 in https://github.<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/b9ac6ed61cae9de90986eaf8766c0e8b1b4461c1" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">com/Slicer/Slicer/commit/c658b7b428a37d6f4e925664099ee30fd4ca408c when VTK9 support was added.

To streamline maintenance, VTK8 support is now being removed.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
