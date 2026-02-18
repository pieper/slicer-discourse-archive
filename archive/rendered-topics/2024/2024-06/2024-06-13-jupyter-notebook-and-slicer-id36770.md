# Jupyter notebook and Slicer

**Topic ID**: 36770
**Date**: 2024-06-13
**URL**: https://discourse.slicer.org/t/jupyter-notebook-and-slicer/36770

---

## Post #1 by @Sharada (2024-06-13 22:37 UTC)

<p>Hello,</p>
<p>I’m posting on behalf on another user. This is about trying to use Slicer through jupyter notebook. The version they are using is 4.11.20210226. They were able to install the ‘SlicerJupyter’ module without any errors. But when they hit ‘StartJupyterServer’ under the ‘JupyterKernel’ module, there is the error shown below. However, we did not encounter this error while using the latest version of Slicer. We need to use the 4.11 version as some of the code we have isn’t compatible with the latest version. Any help on how to fix this error would be appreciated! Thank you.</p>
<p>Error message:<br>
Cargo, the Rust package manager, is not installed or is not on PATH.</p>
<p>This package requires Rust and Cargo to compile extensions. Install it through</p>
<p>the system’s package manager or via <a href="https://rustup.rs/" rel="noopener nofollow ugc">https://rustup.rs/</a></p>
<p>Checking for Rust toolchain…</p>
<hr>
<p>ERROR: Command errored out with exit status 1: ‘D:\Documents\Slicer 4.11.20210226\bin\python-real.exe’ ‘D:\Documents\Slicer 4.11.20210226\lib\Python\Lib\site-packages\pip_vendor\pep517_in_process.py’ prepare_metadata_for_build_wheel ‘C:\Users\subbu\AppData\Local\Temp\tmp9087_1f2’ Check the logs for full command output.</p>
<p>WARNING: You are using pip version 20.3.3; however, version 21.3.1 is available.</p>
<p>You should consider upgrading via the ‘D:\Documents\Slicer 4.11.20210226\bin\python-real.exe -m pip install --upgrade pip’ command.</p>
<p>Traceback (most recent call last):</p>
<p>File “”, line 1, in </p>
<p>File “D:/Documents/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerJupyter/lib/Slicer-4.11/qt-scripted-modules/JupyterNotebooks.py”, line 54, in installRequiredPackages</p>
<p>slicer.util.pip_install(“jupyter jupyterlab ipywidgets pandas ipyevents ipycanvas --no-warn-script-location”)</p>
<p>File “D:\Documents\Slicer 4.11.20210226\bin\Python\slicer\util.py”, line 2876, in pip_install</p>
<p>_executePythonModule(‘pip’, args)</p>
<p>File “D:\Documents\Slicer 4.11.20210226\bin\Python\slicer\util.py”, line 2851, in _executePythonModule</p>
<p>logProcessOutput(proc)</p>
<p>File “D:\Documents\Slicer 4.11.20210226\bin\Python\slicer\util.py”, line 2820, in logProcessOutput</p>
<p>raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)</p>
<p>subprocess.CalledProcessError: Command ‘[‘D:/Documents/Slicer 4.11.20210226/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘jupyter’, ‘jupyterlab’, ‘ipywidgets’, ‘pandas’, ‘ipyevents’, ‘ipycanvas’, ‘–no-warn-script-location’]’ returned non-zero exit status 1.</p>

---

## Post #2 by @Saladi (2024-12-30 08:28 UTC)

<p>You need to install rust: <a href="https://www.rust-lang.org/tools/install" class="inline-onebox" rel="noopener nofollow ugc">Install Rust - Rust Programming Language</a><br>
This worked for me for the same version of Slicer.</p>

---
