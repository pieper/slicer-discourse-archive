# Slicer crashes when creating h5 file

**Topic ID**: 19733
**Date**: 2021-09-18
**URL**: https://discourse.slicer.org/t/slicer-crashes-when-creating-h5-file/19733

---

## Post #1 by @szymswiat (2021-09-18 00:10 UTC)

<p>Problem report for Slicer 4.13.0-2021-09-13 linux-amd64:</p>
<p>When I’m trying to create h5 file in scripted module using h5py package, Slicer 4.13 crashes without any error (even in attached debugger). File appears in filesystem without content (0 bytes).<br>
Does not occur on Slicer 4.11.</p>

---

## Post #2 by @lassoan (2021-09-18 00:22 UTC)

<p>Can you provide a short script that reproduces the issue?</p>
<p>What Linux are you using?</p>

---

## Post #3 by @szymswiat (2021-09-18 18:51 UTC)

<p>My OS: Ubuntu 20.04.3 LTS (Focal Fossa)<br>
Kernel version: 5.9.0-050900-generic</p>
<p>Just type in console:</p>
<pre><code class="lang-python">import h5py
f = h5py.File('new_file.h5', 'w')
</code></pre>

---

## Post #4 by @lassoan (2021-09-20 01:21 UTC)

<p>I was able to reproduce the issue.</p>
<p>It seems that HDF5 that is shipped with ITK-5.2 conflicts with HDF in h5py.</p>
<details>
<summary>
gdb traceback result</summary>
<p>Program terminated with signal SIGSEGV, Segmentation fault.</p>
<p><span class="hashtag">#0</span>  0x00007f6c491e0e54 in itk_H5F_get_intent () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Slicer-4.13/libitkhdf5-shared-5.2.so.1</p>
<p>[Current thread is 1 (Thread 0x7f6c47622540 (LWP 586093))]</p>
<p>(gdb) backtrace</p>
<p><span class="hashtag">#0</span>  0x00007f6c491e0e54 in itk_H5F_get_intent () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Slicer-4.13/libitkhdf5-shared-5.2.so.1</p>
<p><span class="hashtag">#1</span>  0x00007f6c4929241e in H5O__create_ohdr () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Slicer-4.13/libitkhdf5-shared-5.2.so.1</p>
<p><span class="hashtag">#2</span>  0x00007f6bfc4ac53c in H5O_create () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/lib/Python/lib/python3.6/site-packages/h5py/…/h5py.libs/libhdf5-00e8fae8.so.200.0.0</p>
<p><span class="hashtag">#3</span>  0x00007f6bfc43caeb in H5G__obj_create_real () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/lib/Python/lib/python3.6/site-packages/h5py/…/h5py.libs/libhdf5-00e8fae8.so.200.0.0</p>
<p><span class="hashtag">#4</span>  0x00007f6bfc43cce1 in H5G__obj_create () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/lib/Python/lib/python3.6/site-packages/h5py/…/h5py.libs/libhdf5-00e8fae8.so.200.0.0</p>
<p><span class="hashtag">#5</span>  0x00007f6bfc43f6c9 in H5G_mkroot () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/lib/Python/lib/python3.6/site-packages/h5py/…/h5py.libs/libhdf5-00e8fae8.so.200.0.0</p>
<p><span class="hashtag">#6</span>  0x00007f6bfc3f8e5e in H5F_open () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/lib/Python/lib/python3.6/site-packages/h5py/…/h5py.libs/libhdf5-00e8fae8.so.200.0.0</p>
<p><span class="hashtag">#7</span>  0x00007f6bfc6006a5 in H5VL__native_file_create () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/lib/Python/lib/python3.6/site-packages/h5py/…/h5py.libs/libhdf5-00e8fae8.so.200.0.0</p>
<p><span class="hashtag">#8</span>  0x00007f6bfc5ed287 in H5VL_file_create () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/lib/Python/lib/python3.6/site-packages/h5py/…/h5py.libs/libhdf5-00e8fae8.so.200.0.0</p>
<p><span class="hashtag">#9</span>  0x00007f6bfc3ea9ab in H5Fcreate () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/lib/Python/lib/python3.6/site-packages/h5py/…/h5py.libs/libhdf5-00e8fae8.so.200.0.0</p>
<p><span class="hashtag">#10</span> 0x00007f6bfaf3219b in __pyx_f_4h5py_4defs_H5Fcreate () at /tmp/pip-req-build-sxro7y2n/h5py/defs.c:11009</p>
<p><span class="hashtag">#11</span> 0x00007f6b8f790fc9 in __pyx_pf_4h5py_3h5f_2create () at /tmp/pip-req-build-sxro7y2n/h5py/h5f.c:2787</p>
<p><span class="hashtag">#12</span> __pyx_pw_4h5py_3h5f_3create () at /tmp/pip-req-build-sxro7y2n/h5py/h5f.c:2749</p>
<p><span class="hashtag">#13</span> 0x00007f6c56c1ed49 in PyCFunction_Call () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#14</span> 0x00007f6bfacf5a0c in __Pyx_PyObject_Call () at /tmp/pip-req-build-sxro7y2n/h5py/_objects.c:12946</p>
<p><span class="hashtag">#15</span> 0x00007f6bfad00162 in __pyx_pf_4h5py_8_objects_9with_phil_wrapper () at /tmp/pip-req-build-sxro7y2n/h5py/_objects.c:4118</p>
<p><span class="hashtag">#16</span> __pyx_pw_4h5py_8_objects_9with_phil_1wrapper () at /tmp/pip-req-build-sxro7y2n/h5py/_objects.c:4039</p>
<p><span class="hashtag">#17</span> 0x00007f6c56bd18ca in _PyObject_FastCallDict () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#18</span> 0x00007f6c56bd1d30 in _PyObject_FastCallKeywords () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#19</span> 0x00007f6c56ca5f2b in ?? () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#20</span> 0x00007f6c56caad28 in _PyEval_EvalFrameDefault () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#21</span> 0x00007f6c56ca5ddd in ?? () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#22</span> 0x00007f6c56ca6076 in ?? () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#23</span> 0x00007f6c56caad28 in _PyEval_EvalFrameDefault () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#24</span> 0x00007f6c56ca5ddd in ?? () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#25</span> 0x00007f6c56cae675 in _PyFunction_FastCallDict () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#26</span> 0x00007f6c56bd19a6 in _PyObject_FastCallDict () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#27</span> 0x00007f6c56bd1a9d in _PyObject_Call_Prepend () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#28</span> 0x00007f6c56bd176a in PyObject_Call () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#29</span> 0x00007f6c56c3aef9 in ?? () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#30</span> 0x00007f6c56c35fe3 in ?? () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#31</span> 0x00007f6c56bd18ca in _PyObject_FastCallDict () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#32</span> 0x00007f6c56ca5f2b in ?? () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#33</span> 0x00007f6c56ca9c8d in _PyEval_EvalFrameDefault () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#34</span> 0x00007f6c56ca5ddd in ?? () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#35</span> 0x00007f6c56ca639e in PyEval_EvalCodeEx () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#36</span> 0x00007f6c56ca63cb in PyEval_EvalCode () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#37</span> 0x00007f6c56ca355d in ?? () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#38</span> 0x00007f6c56c1eba9 in _PyCFunction_FastCallDict () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#39</span> 0x00007f6c56ca615f in ?? () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#40</span> 0x00007f6c56ca9c8d in _PyEval_EvalFrameDefault () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#41</span> 0x00007f6c56ca5423 in ?? () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#42</span> 0x00007f6c56ca6341 in ?? () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#43</span> 0x00007f6c56ca9c8d in _PyEval_EvalFrameDefault () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#44</span> 0x00007f6c56ca5ddd in ?? () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#45</span> 0x00007f6c56ca6076 in ?? () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#46</span> 0x00007f6c56ca9c8d in _PyEval_EvalFrameDefault () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#47</span> 0x00007f6c56ca5423 in ?? () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#48</span> 0x00007f6c56cae7e7 in _PyFunction_FastCallDict () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#49</span> 0x00007f6c56bd19a6 in _PyObject_FastCallDict () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#50</span> 0x00007f6c56bd1a9d in _PyObject_Call_Prepend () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#51</span> 0x00007f6c56bd18ca in _PyObject_FastCallDict () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#52</span> 0x00007f6c56bd2234 in PyObject_CallMethod () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Python/lib/libpython3.6m.so</p>
<p><span class="hashtag">#53</span> 0x00007f6c7e1433a2 in ?? () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Slicer-4.13/libCTKScriptingPythonWidgets.so.0.1</p>
<p><span class="hashtag">#54</span> 0x00007f6c7e143a81 in ctkPythonConsole::executeCommand(QString const&amp;) () from /home/perklab/Slicer/Slicer-4.13.0-2021-09-10-linux-amd64/bin/…/lib/Slicer-4.13/libCTKScriptingPythonWidgets.so.0.1</p>
</details>
<p>I’ve tried a quick ugly workaround of copying libitkhdf* libraries (renaming them with <code>-shared-5.2</code> suffix) from Slicer-4.11.20210226:</p>
<ul>
<li>libitkhdf5_cpp-shared-5.2.so</li>
<li>libitkhdf5_cpp-shared-5.2.so.1</li>
<li>libitkhdf5-shared-5.2.so</li>
<li>libitkhdf5-shared-5.2.so.1</li>
</ul>
<p>After this, Slicer did not crash when opened the h5 file, but I did not go any further with the testing.</p>
<p>You may ask ITK developers about this, but HDF5 very often has such problems.</p>
<p>Maybe you can use the more modern and Pythonic Zarr container instead.</p>

---

## Post #5 by @szymswiat (2021-09-21 19:21 UTC)

<p>Thanks for suggestion, I switched to zarr ;).</p>

---
