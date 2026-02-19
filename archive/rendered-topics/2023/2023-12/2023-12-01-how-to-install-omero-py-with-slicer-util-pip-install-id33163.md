---
topic_id: 33163
title: "How To Install Omero Py With Slicer Util Pip Install"
date: 2023-12-01
url: https://discourse.slicer.org/t/33163
---

# How to install omero-py with slicer.util.pip_install

**Topic ID**: 33163
**Date**: 2023-12-01
**URL**: https://discourse.slicer.org/t/how-to-install-omero-py-with-slicer-util-pip-install/33163

---

## Post #1 by @borjafernanruiz (2023-12-01 16:50 UTC)

<p>Hi all,</p>
<p>I am working with 3D Slicer on a Ubuntu 20.0.4 docker. I am trying to install the <code>omero-py</code> Python library. It needs to install <code>zero-ice==3.6.5</code>. Additionally, you have to install the following libraries in Ubuntu:</p>
<pre><code class="lang-auto">apt-get install libssl-dev
apt-get install libbz2-dev
apt-get install build-essential
apt-get install python3.9-dev
</code></pre>
<p>Pip doesn’t intall these.</p>
<p>However, the slicer.util.pip_install(“zeroc-ice==‘3.6.5’”) command doesn’t work.<br>
Error:</p>
<pre><code class="lang-auto">creating build/temp.linux-x86_64-cpython-39/src/ice/mcpp
 
      /opt/rh/devtoolset-7/root/usr/bin/gcc -pthread -std=c99 -Wall -Wstrict-prototypes -fno-strict-aliasing -fwrapv -g -fPIC -DICE_STATIC_LIBS -Isrc -Isrc/ice/cpp/include -Isrc/ice/cpp/src -I/work/Stable/Slicer-0-build/python-install/include/python3.9 -c src/BatchRequestInterceptor.cpp -o build/temp.linux-x86_64-cpython-39/src/BatchRequestInterceptor.o -w
 
      error: command '/opt/rh/devtoolset-7/root/usr/bin/gcc' failed: No such file or directory
 
      [end of output]
  note: This error originates from a subprocess, and is likely not a problem with pip.
 
error: legacy-install-failure
× Encountered error while trying to install package.
 
╰─&gt; zeroc-ice
note: This is an issue with the package mentioned above, not pip.
 
hint: See above for output from the failure.
[notice] A new release of pip is available: 23.0 -&gt; 23.3.1
 
[notice] To update, run: python-real -m pip install --upgrade pip
 
Traceback (most recent call last):
 
  File "&lt;console&gt;", line 1, in &lt;module&gt;
 
  File "/slicer/bin/Python/slicer/util.py", line 3578, in pip_install
 
    _executePythonModule('pip', args)
 
  File "/slicer/bin/Python/slicer/util.py", line 3540, in _executePythonModule
 
    logProcessOutput(proc)
 
  File "/slicer/bin/Python/slicer/util.py", line 3509, in logProcessOutput
 
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
 
subprocess.CalledProcessError: Command '['/slicer/bin/../bin/PythonSlicer', '-m', 'pip', 'install', 'omero-py']' returned non-zero exit status 1.
</code></pre>
<p>In order for it to work, I need to install python 3.9 and its pip with:</p>
<pre><code class="lang-auto">apt-get install python3.9
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.9 get-pip.py
</code></pre>
<p>Then, I install zeroc-ice library:<br>
<code>pip install zeroc-ice=='3.6.5'`` If I then execute </code>slicer.util.pip_install(“zeroc-ice==‘3.6.5’”)`, it succeeds.</p>
<p>Does anyone know why? Is there any way to make the pip install work in Slicer without installing the other python as described above?</p>
<p>Thanks a lot for the help!</p>

---

## Post #2 by @lassoan (2023-12-01 18:12 UTC)

<p>ZeroC-ICE 3.6.5 does does not have wheels for Python-3.9: <a href="https://pypi.org/project/zeroc-ice/3.6.5/#files" class="inline-onebox">zeroc-ice · PyPI</a></p>
<p>You can use a more recent version that supports Python-3.9 (that has wheels with <code>-cp39-</code> in its name).</p>

---
