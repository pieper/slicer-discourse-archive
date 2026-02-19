---
topic_id: 43442
title: "Monailabel Numpy Bool Version Conflict"
date: 2025-06-20
url: https://discourse.slicer.org/t/43442
---

# Monailabel numpy.bool version conflict

**Topic ID**: 43442
**Date**: 2025-06-20
**URL**: https://discourse.slicer.org/t/monailabel-numpy-bool-version-conflict/43442

---

## Post #1 by @chz31 (2025-06-20 22:02 UTC)

<p>Hi,</p>
<p>I installed monailabel in a conda environment using <code>pip install -U monailabel</code> following instructions: <code>https://github.com/Project-MONAI/MONAILabel</code>. My pytorch version is 2.6.0 with cu124. Python version is 3.9.</p>
<p>However, it reported a numpy version issue. It appears that “numpy.bool” is deprecated and replaced with just ‘bool’</p>
<pre><code class="lang-auto">In the future `np.bool` will be defined as the corresponding NumPy scalar.
In the future `np.bool` will be defined as the corresponding NumPy scalar.
In the future `np.bool` will be defined as the corresponding NumPy scalar.
[2025-06-20 16:05:56,791] [441716] [MainThread] [INFO] (__main__:285) - USING:: version = False
[2025-06-20 16:05:56,791] [441716] [MainThread] [INFO] (__main__:285) - USING:: app = /home/zhang/apps/radiology
[2025-06-20 16:05:56,791] [441716] [MainThread] [INFO] (__main__:285) - USING:: studies = /home/zhang/datasets/Task09_Spleen/imagesTr
[2025-06-20 16:05:56,791] [441716] [MainThread] [INFO] (__main__:285) - USING:: verbose = INFO
[2025-06-20 16:05:56,791] [441716] [MainThread] [INFO] (__main__:285) - USING:: conf = [['models', 'deepedit']]
[2025-06-20 16:05:56,791] [441716] [MainThread] [INFO] (__main__:285) - USING:: host = 0.0.0.0
[2025-06-20 16:05:56,791] [441716] [MainThread] [INFO] (__main__:285) - USING:: port = 8000
[2025-06-20 16:05:56,791] [441716] [MainThread] [INFO] (__main__:285) - USING:: uvicorn_app = monailabel.app:app
[2025-06-20 16:05:56,791] [441716] [MainThread] [INFO] (__main__:285) - USING:: ssl_keyfile = None
[2025-06-20 16:05:56,791] [441716] [MainThread] [INFO] (__main__:285) - USING:: ssl_certfile = None
[2025-06-20 16:05:56,791] [441716] [MainThread] [INFO] (__main__:285) - USING:: ssl_keyfile_password = None
[2025-06-20 16:05:56,791] [441716] [MainThread] [INFO] (__main__:285) - USING:: ssl_ca_certs = None
[2025-06-20 16:05:56,791] [441716] [MainThread] [INFO] (__main__:285) - USING:: workers = None
[2025-06-20 16:05:56,791] [441716] [MainThread] [INFO] (__main__:285) - USING:: limit_concurrency = None
[2025-06-20 16:05:56,791] [441716] [MainThread] [INFO] (__main__:285) - USING:: access_log = False
[2025-06-20 16:05:56,791] [441716] [MainThread] [INFO] (__main__:285) - USING:: root_path = 
[2025-06-20 16:05:56,791] [441716] [MainThread] [INFO] (__main__:285) - USING:: log_level = info
[2025-06-20 16:05:56,791] [441716] [MainThread] [INFO] (__main__:285) - USING:: log_config = None
[2025-06-20 16:05:56,791] [441716] [MainThread] [INFO] (__main__:285) - USING:: dryrun = False
[2025-06-20 16:05:56,791] [441716] [MainThread] [INFO] (__main__:285) - USING:: action = start_server
[2025-06-20 16:05:56,792] [441716] [MainThread] [INFO] (__main__:296) - 
In the future `np.bool` will be defined as the corresponding NumPy scalar.
Traceback (most recent call last):
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/site-packages/monailabel/main.py", line 356, in &lt;module&gt;
    Main().run()
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/site-packages/monailabel/main.py", line 135, in run
    self.action_start_server(args)
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/site-packages/monailabel/main.py", line 242, in action_start_server
    uvicorn.run(
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/site-packages/uvicorn/main.py", line 580, in run
    server.run()
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/asyncio/base_events.py", line 647, in run_until_complete
    return future.result()
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "&lt;frozen importlib._bootstrap&gt;", line 1030, in _gcd_import
  File "&lt;frozen importlib._bootstrap&gt;", line 1007, in _find_and_load
  File "&lt;frozen importlib._bootstrap&gt;", line 986, in _find_and_load_unlocked
  File "&lt;frozen importlib._bootstrap&gt;", line 680, in _load_unlocked
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/site-packages/monailabel/app.py", line 24, in &lt;module&gt;
    from monailabel.endpoints import (
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/site-packages/monailabel/endpoints/activelearning.py", line 20, in &lt;module&gt;
    from monailabel.interfaces.app import MONAILabelApp
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/site-packages/monailabel/interfaces/app.py", line 37, in &lt;module&gt;
    from monailabel.datastore.dicom import DICOMwebClientX, DICOMWebDatastore
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/site-packages/monailabel/datastore/dicom.py", line 25, in &lt;module&gt;
    from monailabel.datastore.utils.convert import binary_to_image, dicom_to_nifti, nifti_to_dicom_seg
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/site-packages/monailabel/datastore/utils/convert.py", line 27, in &lt;module&gt;
    from monailabel.transform.writer import write_itk
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/site-packages/monailabel/transform/writer.py", line 16, in &lt;module&gt;
    import itk
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/site-packages/itk/__init__.py", line 28, in &lt;module&gt;
    from itk.support.extras import *
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/site-packages/itk/support/extras.py", line 37, in &lt;module&gt;
    import itk.support.types as itkt
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/site-packages/itk/support/types.py", line 178, in &lt;module&gt;
    ) = itkCType.initialize_c_types_once()
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/site-packages/itk/support/types.py", line 143, in initialize_c_types_once
    _B: "itkCType" = itkCType("bool", "B", np.dtype(np.bool))
  File "/home/zhang/anaconda3/envs/moani/lib/python3.9/site-packages/numpy/__init__.py", line 324, in __getattr__
    raise AttributeError(__former_attrs__[attr])
AttributeError: module 'numpy' has no attribute 'bool'.
`np.bool` was a deprecated alias for the builtin `bool`. To avoid this error in existing code, use `bool` by itself. Doing this will not modify any behavior and is safe. If you specifically wanted the numpy scalar type, use `np.bool_` here.
The aliases was originally deprecated in NumPy 1.20; for more details and guidance see the original release note at:
    https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations
(moani) zhang@23-1BPKQ54:~$ python -c "import torch;print(torch.__version__)
</code></pre>
<p>I tried to downgrade numpy to 1.23.5, however, it led to further conflict:</p>
<pre><code class="lang-auto">ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
monai 1.5.0 requires numpy&lt;3.0,&gt;=1.24, but you have numpy 1.23.5 which is incompatible.
numpymaxflow 0.0.7 requires numpy&lt;2.0.0,&gt;=1.26.0, but you have numpy 1.23.5 which is incompatible.
</code></pre>
<p>Does anyone encounter this issue? Thanks!</p>

---
