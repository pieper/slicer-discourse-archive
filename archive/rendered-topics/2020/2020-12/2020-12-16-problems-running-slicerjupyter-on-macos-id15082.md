---
topic_id: 15082
title: "Problems Running Slicerjupyter On Macos"
date: 2020-12-16
url: https://discourse.slicer.org/t/15082
---

# Problems running SlicerJupyter on MacOS

**Topic ID**: 15082
**Date**: 2020-12-16
**URL**: https://discourse.slicer.org/t/problems-running-slicerjupyter-on-macos/15082

---

## Post #1 by @jsalas424 (2020-12-16 03:11 UTC)

<p>I was trying to get the app working by following the instructions here: <a href="https://github.com/Slicer/SlicerJupyter" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/SlicerJupyter: Extension for 3D Slicer that allows the application to be used from Jupyter notebook</a></p>
<p>I started the Jupyter Server from within the app:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/020037b755449d44e8863a97a6c8a2fd923e4163.png" data-download-href="/uploads/short-url/hHq7e5SocPayIhz6dbOOw5XjO3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/020037b755449d44e8863a97a6c8a2fd923e4163_2_690x431.png" alt="image" data-base62-sha1="hHq7e5SocPayIhz6dbOOw5XjO3" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/020037b755449d44e8863a97a6c8a2fd923e4163_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/020037b755449d44e8863a97a6c8a2fd923e4163_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/020037b755449d44e8863a97a6c8a2fd923e4163_2_1380x862.png 2x" data-dominant-color="545568"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2880×1800 283 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I installed node.js, moved both node and npm files from /usr/local/bin to Slicer.app/contents/MacOS where the “Slicer” executable is located (when I click the file it opens 3DSlicer).</p>
<p>I ran pip_install(‘jupyterlab’) in the python console but got the error “name ‘pip_install’ is not defined”. I can access pip through my terminal but these commands still fail:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/3131b93ae177725b030729485752ab23dcf57c17.jpeg" data-download-href="/uploads/short-url/71bVyijisznaaexe8CigHlmS7tB.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3131b93ae177725b030729485752ab23dcf57c17_2_690x431.jpeg" alt="image" data-base62-sha1="71bVyijisznaaexe8CigHlmS7tB" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3131b93ae177725b030729485752ab23dcf57c17_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3131b93ae177725b030729485752ab23dcf57c17_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3131b93ae177725b030729485752ab23dcf57c17_2_1380x862.jpeg 2x" data-dominant-color="A5A6A9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2880×1800 744 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<blockquote>
<p>Last login: Tue Dec 15 22:07:32 on ttys000<br>
jon@Jonathans-MBP ~ % python3<br>
Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23)<br>
[Clang 6.0 (clang-600.0.57)] on darwin<br>
Type “help”, “copyright”, “credits” or “license” for more information.<br>
pip_install(‘jupyterlab’)<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
NameError: name ‘pip_install’ is not defined</p>
</blockquote>

---

## Post #2 by @lassoan (2020-12-16 03:51 UTC)

<p>Do you only have problems with JupyterLab? Does classic Jupyter work well if you click “Start Jupyter server” button (server starts correctly and Jupyter GUI starts in your web browser)?</p>
<p><code>pip_install('jupyterlab')</code> command must be run from Slicer’s Python console (Ctrl-3). To use SlicerJupyter, you don’t even need to have Python installed on your computer.</p>

---

## Post #3 by @jsalas424 (2020-12-17 03:07 UTC)

<p>Thanks for clarifying about the slicer’s python console. This fails at the<br>
slicer.util._executePythonModule command, here’s the logs:</p>
<pre><code class="lang-auto">Python 3.6.7 (default, Sep 30 2020, 16:04:14) 
[GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)] on darwin
&gt;&gt;&gt; 
Collecting pillow
  Using cached Pillow-8.0.1-cp36-cp36m-macosx_10_10_x86_64.whl (2.2 MB)
Installing collected packages: pillow
  Attempting uninstall: pillow
    Found existing installation: Pillow 8.0.1
    Uninstalling Pillow-8.0.1:
      Successfully uninstalled Pillow-8.0.1
Successfully installed pillow-8.0.1
WARNING: You are using pip version 20.1.1; however, version 20.3.3 is available.
You should consider upgrading via the '/Applications/Slicer.app/Contents/bin/./python-real -m pip install --upgrade pip' command.
Collecting jupyter
  Using cached jupyter-1.0.0-py2.py3-none-any.whl (2.7 kB)
Collecting ipywidgets
  Using cached ipywidgets-7.5.1-py2.py3-none-any.whl (121 kB)
Collecting pandas
  Using cached pandas-1.1.5-cp36-cp36m-macosx_10_9_x86_64.whl (10.2 MB)
Collecting ipyevents
  Using cached ipyevents-0.8.1-py2.py3-none-any.whl (150 kB)
Collecting ipycanvas
  Using cached ipycanvas-0.7.0-py2.py3-none-any.whl (247 kB)
Collecting nbconvert
  Using cached nbconvert-6.0.7-py3-none-any.whl (552 kB)
Collecting jupyter-console
  Using cached jupyter_console-6.2.0-py3-none-any.whl (22 kB)
Collecting qtconsoleCollecting traitlets&gt;=4.3.1
  Using cached traitlets-4.3.3-py2.py3-none-any.whl (75 kB)
Collecting nbformat&gt;=4.2.0
  Using cached nbformat-5.0.8-py3-none-any.whl (172 kB)
Collecting ipython&gt;=4.0.0; python_version &gt;= "3.3"
  Using cached ipython-7.16.1-py3-none-any.whl (785 kB)
Collecting widgetsnbextension~=3.5.0
  Using cached widgetsnbextension-3.5.1-py2.py3-none-any.whl (2.2 MB)
Collecting python-dateutil&gt;=2.7.3
  Using cached python_dateutil-2.8.1-py2.py3-none-any.whl (227 kB)
Requirement already satisfied: numpy&gt;=1.15.4 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from pandas) (1.19.1)
Collecting pytz&gt;=2017.2
  Using cached pytz-2020.4-py2.py3-none-any.whl (509 kB)
Collecting orjson
  Using cached orjson-3.4.6-cp36-cp36m-macosx_10_7_x86_64.whl (231 kB)
Requirement already satisfied: pillow&gt;=6.0 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from ipycanvas) (8.0.1)
Collecting defusedxml
  Using cached defusedxml-0.6.0-py2.py3-none-any.whl (23 kB)
Collecting jinja2&gt;=2.4
  Using cached Jinja2-2.11.2-py2.py3-none-any.whl (125 kB)
Collecting jupyterlab-pygments
  Using cached jupyterlab_pygments-0.1.2-py2.py3-none-any.whl (4.6 kB)
Processing /Users/jon/Library/Caches/pip/wheels/12/12/89/fe63ac4d6ee6440daab4db77b78c63f7f192b700f844b6639f/pandocfilters-1.4.3-py3-none-any.whl
Collecting testpath
  Using cached testpath-0.4.4-py2.py3-none-any.whl (163 kB)
Collecting jupyter-core
  Using cached jupyter_core-4.7.0-py3-none-any.whl (82 kB)
Collecting nbclient&lt;0.6.0,&gt;=0.5.0
  Using cached nbclient-0.5.1-py3-none-any.whl (65 kB)
Requirement already satisfied: pygments&gt;=2.4.1 in ./Slicer.app/Contents/Extensions-29402/SlicerJupyter/lib/python3.6/site-packages (from nbconvert-&gt;jupyter) (2.4.1)
Collecting entrypoints&gt;=0.2.2
  Using cached entrypoints-0.3-py2.py3-none-any.whl (11 kB)
Collecting mistune&lt;2,&gt;=0.8.1
  Using cached mistune-0.8.4-py2.py3-none-any.whl (16 kB)
Collecting bleach
  Using cached bleach-3.2.1-py2.py3-none-any.whl (145 kB)
Collecting jupyter-client
  Using cached jupyter_client-6.1.7-py3-none-any.whl (108 kB)
Collecting prompt-toolkit!=3.0.0,!=3.0.1,&lt;3.1.0,&gt;=2.0.0
  Using cached prompt_toolkit-3.0.8-py3-none-any.whl (355 kB)
Collecting qtpy
  Using cached QtPy-1.9.0-py2.py3-none-any.whl (54 kB)
Collecting ipython-genutils
  Using cached ipython_genutils-0.2.0-py2.py3-none-any.whl (26 kB)
Collecting pyzmq&gt;=17.1
  Using cached pyzmq-20.0.0-cp36-cp36m-macosx_10_9_intel.whl (1.4 MB)
Collecting tornado&gt;=4.2
  Using cached tornado-6.1-cp36-cp36m-macosx_10_9_x86_64.whl (416 kB)
Collecting appnope; platform_system == "Darwin"
  Using cached appnope-0.1.2-py2.py3-none-any.whl (4.3 kB)
Collecting terminado&gt;=0.8.3
  Using cached terminado-0.9.1-py3-none-any.whl (13 kB)
Collecting Send2Trash
  Using cached Send2Trash-1.5.0-py3-none-any.whl (12 kB)
Collecting prometheus-client
  Using cached prometheus_client-0.9.0-py2.py3-none-any.whl (53 kB)
Collecting argon2-cffi
  Using cached argon2-cffi-20.1.0.tar.gz (1.8 MB)
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
    Preparing wheel metadata: started
    Preparing wheel metadata: finished with status 'done'
Collecting decorator
  Using cached decorator-4.4.2-py2.py3-none-any.whl (9.2 kB)
Requirement already satisfied: six in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from traitlets&gt;=4.3.1-&gt;ipywidgets) (1.15.0)
Collecting jsonschema!=2.5.0,&gt;=2.4
  Using cached jsonschema-3.2.0-py2.py3-none-any.whl (56 kB)
Collecting backcall
  Using cached backcall-0.2.0-py2.py3-none-any.whl (11 kB)
Collecting pexpect; sys_platform != "win32"
  Using cached pexpect-4.8.0-py2.py3-none-any.whl (59 kB)
Requirement already satisfied: jedi&gt;=0.10 in ./Slicer.app/Contents/Extensions-29402/SlicerJupyter/lib/python3.6/site-packages (from ipython&gt;=4.0.0; python_version &gt;= "3.3"-&gt;ipywidgets) (0.17.0)
Collecting pickleshare
  Using cached pickleshare-0.7.5-py2.py3-none-any.whl (6.9 kB)
Requirement already satisfied: setuptools&gt;=18.5 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from ipython&gt;=4.0.0; python_version &gt;= "3.3"-&gt;ipywidgets) (49.2.0)
Collecting MarkupSafe&gt;=0.23
  Using cached MarkupSafe-1.1.1-cp36-cp36m-macosx_10_6_intel.whl (18 kB)
Collecting async-generator
  Using cached async_generator-1.10-py3-none-any.whl (18 kB)
Collecting nest-asyncio
  Using cached nest_asyncio-1.4.3-py3-none-any.whl (5.3 kB)
Requirement already satisfied: packaging in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from bleach-&gt;nbconvert-&gt;jupyter) (20.4)
Collecting webencodings
  Using cached webencodings-0.5.1-py2.py3-none-any.whl (11 kB)
Collecting wcwidth
  Using cached wcwidth-0.2.5-py2.py3-none-any.whl (30 kB)
Collecting ptyprocess; os_name != "nt"
  Using cached ptyprocess-0.6.0-py2.py3-none-any.whl (39 kB)
Collecting cffi&gt;=1.0.0
  Using cached cffi-1.14.4-cp36-cp36m-macosx_10_9_x86_64.whl (176 kB)
Collecting attrs&gt;=17.4.0
  Using cached attrs-20.3.0-py2.py3-none-any.whl (49 kB)
Processing /Users/jon/Library/Caches/pip/wheels/34/13/19/294da8e11bce7e563afee51251b9fa878185e14f4b5caf00cb/pyrsistent-0.17.3-cp36-cp36m-macosx_10_13_x86_64.whl
Collecting importlib-metadata; python_version &lt; "3.8"
  Using cached importlib_metadata-3.3.0-py3-none-any.whl (10 kB)
Requirement already satisfied: parso&gt;=0.7.0 in ./Slicer.app/Contents/Extensions-29402/SlicerJupyter/lib/python3.6/site-packages (from jedi&gt;=0.10-&gt;ipython&gt;=4.0.0; python_version &gt;= "3.3"-&gt;ipywidgets) (0.7.1)
Requirement already satisfied: pyparsing&gt;=2.0.2 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from packaging-&gt;bleach-&gt;nbconvert-&gt;jupyter) (2.4.7)
Collecting pycparser
  Using cached pycparser-2.20-py2.py3-none-any.whl (112 kB)
Collecting zipp&gt;=0.5
  Using cached zipp-3.4.0-py3-none-any.whl (5.2 kB)
Collecting typing-extensions&gt;=3.6.4; python_version &lt; "3.8"
  Using cached typing_extensions-3.7.4.3-py3-none-any.whl (22 kB)
Building wheels for collected packages: argon2-cffi
  Building wheel for argon2-cffi (PEP 517): started
  Building wheel for argon2-cffi (PEP 517): finished with status 'error'
  ERROR: Command errored out with exit status 1:
   command: /Applications/Slicer.app/Contents/bin/./python-real /Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_vendor/pep517/_in_process.py build_wheel /var/folders/gk/xk6mdq_d7m7db3_6d4_6sg5w0000gn/T/tmpj7paas7y
       cwd: /private/var/folders/gk/xk6mdq_d7m7db3_6d4_6sg5w0000gn/T/pip-install-j5wn1lco/argon2-cffi
  Complete output (29 lines):
  running bdist_wheel
  running build
  running build_py
  creating build
  creating build/lib.macosx-10.13-x86_64-3.6
  creating build/lib.macosx-10.13-x86_64-3.6/argon2
  copying src/argon2/__init__.py -&gt; build/lib.macosx-10.13-x86_64-3.6/argon2
  copying src/argon2/low_level.py -&gt; build/lib.macosx-10.13-x86_64-3.6/argon2
  copying src/argon2/_ffi_build.py -&gt; build/lib.macosx-10.13-x86_64-3.6/argon2
  copying src/argon2/_password_hasher.py -&gt; build/lib.macosx-10.13-x86_64-3.6/argon2
  copying src/argon2/exceptions.py -&gt; build/lib.macosx-10.13-x86_64-3.6/argon2
  copying src/argon2/_legacy.py -&gt; build/lib.macosx-10.13-x86_64-3.6/argon2
  copying src/argon2/__main__.py -&gt; build/lib.macosx-10.13-x86_64-3.6/argon2
  copying src/argon2/_utils.py -&gt; build/lib.macosx-10.13-x86_64-3.6/argon2
  running build_clib
  building 'argon2' library
  creating build/temp.macosx-10.13-x86_64-3.6
  creating build/temp.macosx-10.13-x86_64-3.6/extras
  creating build/temp.macosx-10.13-x86_64-3.6/extras/libargon2
  creating build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src
  creating build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/blake2
  /usr/bin/clang -pthread -Wall -g -fPIC -msse2 -Iextras/libargon2/src/../include -Iextras/libargon2/src/blake2 -c extras/libargon2/src/argon2.c -o build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/argon2.o
  /usr/bin/clang -pthread -Wall -g -fPIC -msse2 -Iextras/libargon2/src/../include -Iextras/libargon2/src/blake2 -c extras/libargon2/src/blake2/blake2b.c -o build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/blake2/blake2b.o
  /usr/bin/clang -pthread -Wall -g -fPIC -msse2 -Iextras/libargon2/src/../include -Iextras/libargon2/src/blake2 -c extras/libargon2/src/core.c -o build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/core.o
  /usr/bin/clang -pthread -Wall -g -fPIC -msse2 -Iextras/libargon2/src/../include -Iextras/libargon2/src/blake2 -c extras/libargon2/src/encoding.c -o build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/encoding.o
  /usr/bin/clang -pthread -Wall -g -fPIC -msse2 -Iextras/libargon2/src/../include -Iextras/libargon2/src/blake2 -c extras/libargon2/src/opt.c -o build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/opt.o
  /usr/bin/clang -pthread -Wall -g -fPIC -msse2 -Iextras/libargon2/src/../include -Iextras/libargon2/src/blake2 -c extras/libargon2/src/thread.c -o build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/thread.o
  /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ar rc build/temp.macosx-10.13-x86_64-3.6/libargon2.a build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/argon2.o build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/blake2/blake2b.o build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/core.o build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/encoding.o build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/opt.o build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/thread.o
  error: command '/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ar' failed with exit status 1
  ----------------------------------------
  ERROR: Failed building wheel for argon2-cffi
Failed to build argon2-cffi
ERROR: Could not build wheels for argon2-cffi which use PEP 517 and cannot be installed directly
WARNING: You are using pip version 20.1.1; however, version 20.3.3 is available.
You should consider upgrading via the '/Applications/Slicer.app/Contents/bin/./python-real -m pip install --upgrade pip' command.
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer.app/Contents/Extensions-29402/SlicerJupyter/lib/Slicer-4.11/qt-scripted-modules/JupyterNotebooks.py", line 53, in installRequiredPackages
    slicer.util.pip_install("jupyter ipywidgets pandas ipyevents ipycanvas --no-warn-script-location")
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 2569, in pip_install
    _executePythonModule('pip', args)
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 2545, in _executePythonModule
    logProcessOutput(proc)
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 2517, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['/Applications/Slicer.app/Contents/bin/../bin/PythonSlicer', '-m', 'pip', 'install', 'jupyter', 'ipywidgets', 'pandas', 'ipyevents', 'ipycanvas', '--no-warn-script-location']' returned non-zero exit status 1.

  Using cached qtconsole-5.0.1-py3-none-any.whl (118 kB)
Collecting ipykernel
  Using cached ipykernel-5.4.2-py3-none-any.whl (119 kB)
Collecting notebook
  Using cached notebook-6.1.5-py3-none-any.whl (9.5 MB)
&gt;&gt;&gt; pip_install('jupyterlab')
Collecting jupyterlab  Using cached jupyterlab-2.2.9-py3-none-any.whl (7.9 MB)
Collecting jupyterlab-server&lt;2.0,&gt;=1.1.5
  Using cached jupyterlab_server-1.2.0-py3-none-any.whl (29 kB)
Collecting jinja2&gt;=2.10
  Using cached Jinja2-2.11.2-py2.py3-none-any.whl (125 kB)
Collecting notebook&gt;=4.3.1
  Using cached notebook-6.1.5-py3-none-any.whl (9.5 MB)
Collecting tornado!=6.0.0,!=6.0.1,!=6.0.2
  Using cached tornado-6.1-cp36-cp36m-macosx_10_9_x86_64.whl (416 kB)
Collecting jsonschema&gt;=3.0.1
  Using cached jsonschema-3.2.0-py2.py3-none-any.whl (56 kB)
Collecting json5
  Using cached json5-0.9.5-py2.py3-none-any.whl (17 kB)
Requirement already satisfied: requests in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from jupyterlab-server&lt;2.0,&gt;=1.1.5-&gt;jupyterlab) (2.24.0)
Collecting MarkupSafe&gt;=0.23
  Using cached MarkupSafe-1.1.1-cp36-cp36m-macosx_10_6_intel.whl (18 kB)
Collecting jupyter-core&gt;=4.6.1
  Using cached jupyter_core-4.7.0-py3-none-any.whl (82 kB)
Collecting traitlets&gt;=4.2.1
  Using cached traitlets-4.3.3-py2.py3-none-any.whl (75 kB)
Collecting jupyter-client&gt;=5.3.4
  Using cached jupyter_client-6.1.7-py3-none-any.whl (108 kB)
Collecting ipython-genutils
  Using cached ipython_genutils-0.2.0-py2.py3-none-any.whl (26 kB)
Collecting pyzmq&gt;=17
  Using cached pyzmq-20.0.0-cp36-cp36m-macosx_10_9_intel.whl (1.4 MB)
Collecting nbconvert
  Using cached nbconvert-6.0.7-py3-none-any.whl (552 kB)
Collecting Send2Trash
  Using cached Send2Trash-1.5.0-py3-none-any.whl (12 kB)
Collecting prometheus-client
  Using cached prometheus_client-0.9.0-py2.py3-none-any.whl (53 kB)
Collecting terminado&gt;=0.8.3
  Using cached terminado-0.9.1-py3-none-any.whl (13 kB)
Collecting argon2-cffi
  Using cached argon2-cffi-20.1.0.tar.gz (1.8 MB)
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
    Preparing wheel metadata: started
    Preparing wheel metadata: finished with status 'done'
Collecting nbformat
  Using cached nbformat-5.0.8-py3-none-any.whl (172 kB)
Collecting ipykernel
  Using cached ipykernel-5.4.2-py3-none-any.whl (119 kB)
Processing /Users/jon/Library/Caches/pip/wheels/34/13/19/294da8e11bce7e563afee51251b9fa878185e14f4b5caf00cb/pyrsistent-0.17.3-cp36-cp36m-macosx_10_13_x86_64.whl
Requirement already satisfied: six&gt;=1.11.0 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from jsonschema&gt;=3.0.1-&gt;jupyterlab-server&lt;2.0,&gt;=1.1.5-&gt;jupyterlab) (1.15.0)
Collecting attrs&gt;=17.4.0
  Using cached attrs-20.3.0-py2.py3-none-any.whl (49 kB)
Requirement already satisfied: setuptools in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from jsonschema&gt;=3.0.1-&gt;jupyterlab-server&lt;2.0,&gt;=1.1.5-&gt;jupyterlab) (49.2.0)
Collecting importlib-metadata; python_version &lt; "3.8"
  Using cached importlib_metadata-3.3.0-py3-none-any.whl (10 kB)
Requirement already satisfied: certifi&gt;=2017.4.17 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from requests-&gt;jupyterlab-server&lt;2.0,&gt;=1.1.5-&gt;jupyterlab) (2020.6.20)
Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,&lt;1.26,&gt;=1.21.1 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from requests-&gt;jupyterlab-server&lt;2.0,&gt;=1.1.5-&gt;jupyterlab) (1.25.10)
Requirement already satisfied: chardet&lt;4,&gt;=3.0.2 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from requests-&gt;jupyterlab-server&lt;2.0,&gt;=1.1.5-&gt;jupyterlab) (3.0.4)
Requirement already satisfied: idna&lt;3,&gt;=2.5 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from requests-&gt;jupyterlab-server&lt;2.0,&gt;=1.1.5-&gt;jupyterlab) (2.10)
Collecting decorator
  Using cached decorator-4.4.2-py2.py3-none-any.whl (9.2 kB)
Collecting python-dateutil&gt;=2.1
  Using cached python_dateutil-2.8.1-py2.py3-none-any.whl (227 kB)
Processing /Users/jon/Library/Caches/pip/wheels/12/12/89/fe63ac4d6ee6440daab4db77b78c63f7f192b700f844b6639f/pandocfilters-1.4.3-py3-none-any.whl
Collecting defusedxml
  Using cached defusedxml-0.6.0-py2.py3-none-any.whl (23 kB)
Requirement already satisfied: pygments&gt;=2.4.1 in ./Slicer.app/Contents/Extensions-29402/SlicerJupyter/lib/python3.6/site-packages (from nbconvert-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (2.4.1)
Collecting testpath
  Using cached testpath-0.4.4-py2.py3-none-any.whl (163 kB)
Collecting mistune&lt;2,&gt;=0.8.1
  Using cached mistune-0.8.4-py2.py3-none-any.whl (16 kB)
Collecting entrypoints&gt;=0.2.2
  Using cached entrypoints-0.3-py2.py3-none-any.whl (11 kB)
Collecting jupyterlab-pygments
  Using cached jupyterlab_pygments-0.1.2-py2.py3-none-any.whl (4.6 kB)
Collecting nbclient&lt;0.6.0,&gt;=0.5.0
  Using cached nbclient-0.5.1-py3-none-any.whl (65 kB)
Collecting bleach
  Using cached bleach-3.2.1-py2.py3-none-any.whl (145 kB)
Collecting ptyprocess; os_name != "nt"
  Using cached ptyprocess-0.6.0-py2.py3-none-any.whl (39 kB)
Collecting cffi&gt;=1.0.0
  Using cached cffi-1.14.4-cp36-cp36m-macosx_10_9_x86_64.whl (176 kB)
Collecting appnope; platform_system == "Darwin"
  Using cached appnope-0.1.2-py2.py3-none-any.whl (4.3 kB)
Collecting ipython&gt;=5.0.0
  Using cached ipython-7.16.1-py3-none-any.whl (785 kB)
Collecting typing-extensions&gt;=3.6.4; python_version &lt; "3.8"
  Using cached typing_extensions-3.7.4.3-py3-none-any.whl (22 kB)
Collecting zipp&gt;=0.5
  Using cached zipp-3.4.0-py3-none-any.whl (5.2 kB)
Collecting nest-asyncio
  Using cached nest_asyncio-1.4.3-py3-none-any.whl (5.3 kB)
Collecting async-generator
  Using cached async_generator-1.10-py3-none-any.whl (18 kB)
Collecting webencodings
  Using cached webencodings-0.5.1-py2.py3-none-any.whl (11 kB)
Requirement already satisfied: packaging in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from bleach-&gt;nbconvert-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (20.4)
Collecting pycparser
  Using cached pycparser-2.20-py2.py3-none-any.whl (112 kB)
Collecting backcall
  Using cached backcall-0.2.0-py2.py3-none-any.whl (11 kB)
Requirement already satisfied: jedi&gt;=0.10 in ./Slicer.app/Contents/Extensions-29402/SlicerJupyter/lib/python3.6/site-packages (from ipython&gt;=5.0.0-&gt;ipykernel-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (0.17.0)
Collecting pexpect; sys_platform != "win32"
  Using cached pexpect-4.8.0-py2.py3-none-any.whl (59 kB)
Collecting pickleshare
  Using cached pickleshare-0.7.5-py2.py3-none-any.whl (6.9 kB)
Collecting prompt-toolkit!=3.0.0,!=3.0.1,&lt;3.1.0,&gt;=2.0.0
  Using cached prompt_toolkit-3.0.8-py3-none-any.whl (355 kB)
Requirement already satisfied: pyparsing&gt;=2.0.2 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from packaging-&gt;bleach-&gt;nbconvert-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (2.4.7)
Requirement already satisfied: parso&gt;=0.7.0 in ./Slicer.app/Contents/Extensions-29402/SlicerJupyter/lib/python3.6/site-packages (from jedi&gt;=0.10-&gt;ipython&gt;=5.0.0-&gt;ipykernel-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (0.7.1)
Collecting wcwidth
  Using cached wcwidth-0.2.5-py2.py3-none-any.whl (30 kB)
Building wheels for collected packages: argon2-cffi
  Building wheel for argon2-cffi (PEP 517): started
  Building wheel for argon2-cffi (PEP 517): finished with status 'error'
  ERROR: Command errored out with exit status 1:
   command: /Applications/Slicer.app/Contents/bin/./python-real /Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_vendor/pep517/_in_process.py build_wheel /var/folders/gk/xk6mdq_d7m7db3_6d4_6sg5w0000gn/T/tmpkye11kzt
       cwd: /private/var/folders/gk/xk6mdq_d7m7db3_6d4_6sg5w0000gn/T/pip-install-efqdzjlq/argon2-cffi
  Complete output (29 lines):
  running bdist_wheel
  running build
  running build_py
  creating build
  creating build/lib.macosx-10.13-x86_64-3.6
  creating build/lib.macosx-10.13-x86_64-3.6/argon2
  copying src/argon2/__init__.py -&gt; build/lib.macosx-10.13-x86_64-3.6/argon2
  copying src/argon2/low_level.py -&gt; build/lib.macosx-10.13-x86_64-3.6/argon2
  copying src/argon2/_ffi_build.py -&gt; build/lib.macosx-10.13-x86_64-3.6/argon2

  copying src/argon2/_password_hasher.py -&gt; build/lib.macosx-10.13-x86_64-3.6/argon2
  copying src/argon2/exceptions.py -&gt; build/lib.macosx-10.13-x86_64-3.6/argon2
  copying src/argon2/_legacy.py -&gt; build/lib.macosx-10.13-x86_64-3.6/argon2
  copying src/argon2/__main__.py -&gt; build/lib.macosx-10.13-x86_64-3.6/argon2
  copying src/argon2/_utils.py -&gt; build/lib.macosx-10.13-x86_64-3.6/argon2
  running build_clib
  building 'argon2' library
  creating build/temp.macosx-10.13-x86_64-3.6
  creating build/temp.macosx-10.13-x86_64-3.6/extras
  creating build/temp.macosx-10.13-x86_64-3.6/extras/libargon2
  creating build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src
  creating build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/blake2
  /usr/bin/clang -pthread -Wall -g -fPIC -msse2 -Iextras/libargon2/src/../include -Iextras/libargon2/src/blake2 -c extras/libargon2/src/argon2.c -o build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/argon2.o
  /usr/bin/clang -pthread -Wall -g -fPIC -msse2 -Iextras/libargon2/src/../include -Iextras/libargon2/src/blake2 -c extras/libargon2/src/blake2/blake2b.c -o build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/blake2/blake2b.o
  /usr/bin/clang -pthread -Wall -g -fPIC -msse2 -Iextras/libargon2/src/../include -Iextras/libargon2/src/blake2 -c extras/libargon2/src/core.c -o build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/core.o
  /usr/bin/clang -pthread -Wall -g -fPIC -msse2 -Iextras/libargon2/src/../include -Iextras/libargon2/src/blake2 -c extras/libargon2/src/encoding.c -o build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/encoding.o
  /usr/bin/clang -pthread -Wall -g -fPIC -msse2 -Iextras/libargon2/src/../include -Iextras/libargon2/src/blake2 -c extras/libargon2/src/opt.c -o build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/opt.o
  /usr/bin/clang -pthread -Wall -g -fPIC -msse2 -Iextras/libargon2/src/../include -Iextras/libargon2/src/blake2 -c extras/libargon2/src/thread.c -o build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/thread.o
  /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ar rc build/temp.macosx-10.13-x86_64-3.6/libargon2.a build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/argon2.o build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/blake2/blake2b.o build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/core.o build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/encoding.o build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/opt.o build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/thread.o
  error: command '/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ar' failed with exit status 1
  ----------------------------------------
  ERROR: Failed building wheel for argon2-cffi
Failed to build argon2-cffi
ERROR: Could not build wheels for argon2-cffi which use PEP 517 and cannot be installed directly
WARNING: You are using pip version 20.1.1; however, version 20.3.3 is available.
You should consider upgrading via the '/Applications/Slicer.app/Contents/bin/./python-real -m pip install --upgrade pip' command.
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 2569, in pip_install
    _executePythonModule('pip', args)
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 2545, in _executePythonModule
    logProcessOutput(proc)
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 2517, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['/Applications/Slicer.app/Contents/bin/../bin/PythonSlicer', '-m', 'pip', 'install', 'jupyterlab']' returned non-zero exit status 1.
&gt;&gt;&gt; 
&gt;&gt;&gt; slicer.util._executePythonModule('jupyter',['labextension','install','@jupyter-widgets/jupyterlab-manager','ipycanvas','ipyevents'])
/Applications/Slicer.app/Contents/bin/./python-real: No module named jupyter
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 2545, in _executePythonModule
    logProcessOutput(proc)
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 2517, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['/Applications/Slicer.app/Contents/bin/../bin/PythonSlicer', '-m', 'jupyter', 'labextension', 'install', '@jupyter-widgets/jupyterlab-manager', 'ipycanvas', 'ipyevents']' returned non-zero exit status 1.
</code></pre>

---

## Post #4 by @jsalas424 (2020-12-17 03:09 UTC)

<aside class="quote no-group" data-username="jsalas424" data-post="3" data-topic="15082">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a87d85/48.png" class="avatar"> jsalas424:</div>
<blockquote>
<p><code>/Applications/Slicer.app/Contents/bin/./python-real -m pip install --upgrade pip</code></p>
</blockquote>
</aside>
<p>I also tried to upgrade pip as per the log output but that didn’t work either</p>
<pre><code class="lang-auto">jon@Jonathans-MBP ~ % /Applications/Slicer.app/Contents/bin/./python-real -m pip install --upgrade pip
Could not find platform independent libraries &lt;prefix&gt;
Could not find platform dependent libraries &lt;exec_prefix&gt;
Consider setting $PYTHONHOME to &lt;prefix&gt;[:&lt;exec_prefix&gt;]
Fatal Python error: Py_Initialize: unable to load the file system codec
ModuleNotFoundError: No module named 'encodings'

Current thread 0x000000011a8a6dc0 (most recent call first):
zsh: abort      /Applications/Slicer.app/Contents/bin/./python-real -m pip install --upgrade 
jon@Jonathans-MBP ~ % 
</code></pre>

---

## Post #5 by @lassoan (2020-12-17 05:47 UTC)

<p>You got the error because Jupyter server uses argon2-cffi package, which does not have wheels for macOS for Python-3.6.7. I’ve updated SlicerJupyter to bundle this package with the extension, so it is not necessary to build it during installation. Please try it again tomorrow (uninstall and install SlicerJupyter).</p>
<p>Updating pip is not necessary (but if you do that then probably it does not cause any problem either).</p>
<p>You got the error when you executed python-real because the virtual python environment was not set up. Instead of running python-real directly, you can use PythonSlicer executable, which sets up the virtual python environment and launches python-real.</p>

---

## Post #6 by @jsalas424 (2020-12-21 15:38 UTC)

<p>Solved! I reinstalled and it launched right into the localhost webpage for Jupyter notebook. I was also able to update pip by calling PythonSlicer instead of python-real. Perhaps this warrants an update of the warning output?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/650e77a78c8b4ad4a9308ae6927c09212bfa5bd5.jpeg" data-download-href="/uploads/short-url/epZdGFuAxCaDJ4uXOyMGNVBe0wl.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/650e77a78c8b4ad4a9308ae6927c09212bfa5bd5_2_690x431.jpeg" alt="image" data-base62-sha1="epZdGFuAxCaDJ4uXOyMGNVBe0wl" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/650e77a78c8b4ad4a9308ae6927c09212bfa5bd5_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/650e77a78c8b4ad4a9308ae6927c09212bfa5bd5_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/650e77a78c8b4ad4a9308ae6927c09212bfa5bd5_2_1380x862.jpeg 2x" data-dominant-color="DCDCDE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2880×1800 329 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<blockquote>
<p>Collecting pillow</p>
<p>Using cached Pillow-8.0.1-cp36-cp36m-macosx_10_10_x86_64.whl (2.2 MB)</p>
<p>Installing collected packages: pillow</p>
<p>Attempting uninstall: pillow</p>
<p>Found existing installation: Pillow 8.0.1</p>
<p>Uninstalling Pillow-8.0.1:</p>
<p>Successfully uninstalled Pillow-8.0.1</p>
<p>Successfully installed pillow-8.0.1</p>
<p>WARNING: You are using pip version 20.1.1; however, version 20.3.3 is available.</p>
<p>You should consider upgrading via the ‘/Applications/Slicer.app/Contents/bin/./python-real -m pip install --upgrade pip’ command.</p>
<p>Collecting jupyter</p>
<p>Using cached jupyter-1.0.0-py2.py3-none-any.whl (2.7 kB)</p>
<p>Collecting ipywidgets</p>
<p>Using cached ipywidgets-7.5.1-py2.py3-none-any.whl (121 kB)</p>
<p>Collecting pandas</p>
<p>Using cached pandas-1.1.5-cp36-cp36m-macosx_10_9_x86_64.whl (10.2 MB)</p>
<p>Collecting ipyevents</p>
<p>Using cached ipyevents-0.8.1-py2.py3-none-any.whl (150 kB)</p>
<p>Collecting ipycanvas</p>
<p>Downloading ipycanvas-0.8.0-py2.py3-none-any.whl (257 kB)</p>
<p>Collecting notebook</p>
<p>Using cached notebook-6.1.5-py3-none-any.whl (9.5 MB)</p>
<p>Collecting ipykernel</p>
<p>Using cached ipykernel-5.4.2-py3-none-any.whl (119 kB)</p>
<p>Collecting jupyter-console</p>
<p>Using cached jupyter_console-6.2.0-py3-none-any.whl (22 kB)</p>
<p>Collecting nbconvert</p>
<p>Using cached nbconvert-6.0.7-py3-none-any.whl (552 kB)</p>
<p>Collecting qtconsole</p>
<p>Using cached qtconsole-5.0.1-py3-none-any.whl (118 kB)</p>
<p>Collecting nbformat&gt;=4.2.0</p>
<p>Using cached nbformat-5.0.8-py3-none-any.whl (172 kB)</p>
<p>Collecting traitlets&gt;=4.3.1</p>
<p>Using cached traitlets-4.3.3-py2.py3-none-any.whl (75 kB)</p>
<p>Collecting ipython&gt;=4.0.0; python_version &gt;= “3.3”</p>
<p>Using cached ipython-7.16.1-py3-none-any.whl (785 kB)</p>
<p>Collecting widgetsnbextension~=3.5.0</p>
<p>Using cached widgetsnbextension-3.5.1-py2.py3-none-any.whl (2.2 MB)</p>
<p>Requirement already satisfied: numpy&gt;=1.15.4 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from pandas) (1.19.1)</p>
<p>Collecting pytz&gt;=2017.2</p>
<p>Using cached pytz-2020.4-py2.py3-none-any.whl (509 kB)</p>
<p>Collecting python-dateutil&gt;=2.7.3</p>
<p>Using cached python_dateutil-2.8.1-py2.py3-none-any.whl (227 kB)</p>
<p>Collecting orjson</p>
<p>Using cached orjson-3.4.6-cp36-cp36m-macosx_10_7_x86_64.whl (231 kB)</p>
<p>Requirement already satisfied: pillow&gt;=6.0 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from ipycanvas) (8.0.1)</p>
<p>Collecting Send2Trash</p>
<p>Using cached Send2Trash-1.5.0-py3-none-any.whl (12 kB)</p>
<p>Collecting terminado&gt;=0.8.3</p>
<p>Using cached terminado-0.9.1-py3-none-any.whl (13 kB)</p>
<p>Collecting pyzmq&gt;=17</p>
<p>Using cached pyzmq-20.0.0-cp36-cp36m-macosx_10_9_intel.whl (1.4 MB)</p>
<p>Collecting jupyter-client&gt;=5.3.4</p>
<p>Using cached jupyter_client-6.1.7-py3-none-any.whl (108 kB)</p>
<p>Requirement already satisfied: argon2-cffi in ./Slicer.app/Contents/Extensions-29402/SlicerJupyter/lib/python3.6/site-packages (from notebook-&gt;jupyter) (20.1.0)</p>
<p>Collecting tornado&gt;=5.0</p>
<p>Using cached tornado-6.1-cp36-cp36m-macosx_10_9_x86_64.whl (416 kB)</p>
<p>Collecting ipython-genutils</p>
<p>Using cached ipython_genutils-0.2.0-py2.py3-none-any.whl (26 kB)</p>
<p>Collecting prometheus-client</p>
<p>Using cached prometheus_client-0.9.0-py2.py3-none-any.whl (53 kB)</p>
<p>Collecting jinja2</p>
<p>Using cached Jinja2-2.11.2-py2.py3-none-any.whl (125 kB)</p>
<p>Collecting jupyter-core&gt;=4.6.1</p>
<p>Using cached jupyter_core-4.7.0-py3-none-any.whl (82 kB)</p>
<p>Collecting appnope; platform_system == “Darwin”</p>
<p>Using cached appnope-0.1.2-py2.py3-none-any.whl (4.3 kB)</p>
<p>Collecting prompt-toolkit!=3.0.0,!=3.0.1,&lt;3.1.0,&gt;=2.0.0</p>
<p>Using cached prompt_toolkit-3.0.8-py3-none-any.whl (355 kB)</p>
<p>Requirement already satisfied: pygments in ./Slicer.app/Contents/Extensions-29402/SlicerJupyter/lib/python3.6/site-packages (from jupyter-console-&gt;jupyter) (2.4.1)</p>
<p>Processing /Users/jon/Library/Caches/pip/wheels/12/12/89/fe63ac4d6ee6440daab4db77b78c63f7f192b700f844b6639f/pandocfilters-1.4.3-py3-none-any.whl</p>
<p>Collecting nbclient&lt;0.6.0,&gt;=0.5.0</p>
<p>Using cached nbclient-0.5.1-py3-none-any.whl (65 kB)</p>
<p>Collecting testpath</p>
<p>Using cached testpath-0.4.4-py2.py3-none-any.whl (163 kB)</p>
<p>Collecting jupyterlab-pygments</p>
<p>Using cached jupyterlab_pygments-0.1.2-py2.py3-none-any.whl (4.6 kB)</p>
<p>Collecting defusedxml</p>
<p>Using cached defusedxml-0.6.0-py2.py3-none-any.whl (23 kB)</p>
<p>Collecting entrypoints&gt;=0.2.2</p>
<p>Using cached entrypoints-0.3-py2.py3-none-any.whl (11 kB)</p>
<p>Collecting bleach</p>
<p>Using cached bleach-3.2.1-py2.py3-none-any.whl (145 kB)</p>
<p>Collecting mistune&lt;2,&gt;=0.8.1</p>
<p>Using cached mistune-0.8.4-py2.py3-none-any.whl (16 kB)</p>
<p>Collecting qtpy</p>
<p>Using cached QtPy-1.9.0-py2.py3-none-any.whl (54 kB)</p>
<p>Collecting jsonschema!=2.5.0,&gt;=2.4</p>
<p>Using cached jsonschema-3.2.0-py2.py3-none-any.whl (56 kB)</p>
<p>Collecting decorator</p>
<p>Using cached decorator-4.4.2-py2.py3-none-any.whl (9.2 kB)</p>
<p>Requirement already satisfied: six in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from traitlets&gt;=4.3.1-&gt;ipywidgets) (1.15.0)</p>
<p>Collecting pexpect; sys_platform != “win32”</p>
<p>Using cached pexpect-4.8.0-py2.py3-none-any.whl (59 kB)</p>
<p>Collecting pickleshare</p>
<p>Using cached pickleshare-0.7.5-py2.py3-none-any.whl (6.9 kB)</p>
<p>Collecting backcall</p>
<p>Using cached backcall-0.2.0-py2.py3-none-any.whl (11 kB)</p>
<p>Requirement already satisfied: jedi&gt;=0.10 in ./Slicer.app/Contents/Extensions-29402/SlicerJupyter/lib/python3.6/site-packages (from ipython&gt;=4.0.0; python_version &gt;= “3.3”-&gt;ipywidgets) (0.17.0)</p>
<p>Requirement already satisfied: setuptools&gt;=18.5 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from ipython&gt;=4.0.0; python_version &gt;= “3.3”-&gt;ipywidgets) (49.2.0)</p>
<p>Collecting ptyprocess; os_name != “nt”</p>
<p>Using cached ptyprocess-0.6.0-py2.py3-none-any.whl (39 kB)</p>
<p>Requirement already satisfied: cffi&gt;=1.0.0 in ./Slicer.app/Contents/Extensions-29402/SlicerJupyter/lib/python3.6/site-packages (from argon2-cffi-&gt;notebook-&gt;jupyter) (1.14.4)</p>
<p>Collecting MarkupSafe&gt;=0.23</p>
<p>Using cached MarkupSafe-1.1.1-cp36-cp36m-macosx_10_6_intel.whl (18 kB)</p>
<p>Collecting wcwidth</p>
<p>Using cached wcwidth-0.2.5-py2.py3-none-any.whl (30 kB)</p>
<p>Collecting nest-asyncio</p>
<p>Using cached nest_asyncio-1.4.3-py3-none-any.whl (5.3 kB)</p>
<p>Collecting async-generator</p>
<p>Using cached async_generator-1.10-py3-none-any.whl (18 kB)</p>
<p>Requirement already satisfied: packaging in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from bleach-&gt;nbconvert-&gt;jupyter) (20.4)</p>
<p>Collecting webencodings</p>
<p>Using cached webencodings-0.5.1-py2.py3-none-any.whl (11 kB)</p>
<p>Collecting attrs&gt;=17.4.0</p>
<p>Using cached attrs-20.3.0-py2.py3-none-any.whl (49 kB)</p>
<p>Collecting importlib-metadata; python_version &lt; “3.8”</p>
<p>Using cached importlib_metadata-3.3.0-py3-none-any.whl (10 kB)</p>
<p>Processing /Users/jon/Library/Caches/pip/wheels/34/13/19/294da8e11bce7e563afee51251b9fa878185e14f4b5caf00cb/pyrsistent-0.17.3-cp36-cp36m-macosx_10_13_x86_64.whl</p>
<p>Requirement already satisfied: parso&gt;=0.7.0 in ./Slicer.app/Contents/Extensions-29402/SlicerJupyter/lib/python3.6/site-packages (from jedi&gt;=0.10-&gt;ipython&gt;=4.0.0; python_version &gt;= “3.3”-&gt;ipywidgets) (0.7.1)</p>
<p>Requirement already satisfied: pycparser in ./Slicer.app/Contents/Extensions-29402/SlicerJupyter/lib/python3.6/site-packages (from cffi&gt;=1.0.0-&gt;argon2-cffi-&gt;notebook-&gt;jupyter) (2.20)</p>
<p>Requirement already satisfied: pyparsing&gt;=2.0.2 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from packaging-&gt;bleach-&gt;nbconvert-&gt;jupyter) (2.4.7)</p>
<p>Collecting zipp&gt;=0.5</p>
<p>Using cached zipp-3.4.0-py3-none-any.whl (5.2 kB)</p>
<p>Collecting typing-extensions&gt;=3.6.4; python_version &lt; “3.8”</p>
<p>Using cached typing_extensions-3.7.4.3-py3-none-any.whl (22 kB)</p>
<p>Installing collected packages: Send2Trash, ptyprocess, tornado, terminado, pyzmq, python-dateutil, decorator, ipython-genutils, traitlets, jupyter-core, jupyter-client, appnope, wcwidth, prompt-toolkit, pexpect, pickleshare, backcall, ipython, ipykernel, pandocfilters, attrs, zipp, typing-extensions, importlib-metadata, pyrsistent, jsonschema, nbformat, nest-asyncio, async-generator, nbclient, testpath, jupyterlab-pygments, defusedxml, MarkupSafe, jinja2, entrypoints, webencodings, bleach, mistune, nbconvert, prometheus-client, notebook, jupyter-console, widgetsnbextension, ipywidgets, qtpy, qtconsole, jupyter, pytz, pandas, ipyevents, orjson, ipycanvas</p>
<p>Successfully installed MarkupSafe-1.1.1 Send2Trash-1.5.0 appnope-0.1.2 async-generator-1.10 attrs-20.3.0 backcall-0.2.0 bleach-3.2.1 decorator-4.4.2 defusedxml-0.6.0 entrypoints-0.3 importlib-metadata-3.3.0 ipycanvas-0.8.0 ipyevents-0.8.1 ipykernel-5.4.2 ipython-7.16.1 ipython-genutils-0.2.0 ipywidgets-7.5.1 jinja2-2.11.2 jsonschema-3.2.0 jupyter-1.0.0 jupyter-client-6.1.7 jupyter-console-6.2.0 jupyter-core-4.7.0 jupyterlab-pygments-0.1.2 mistune-0.8.4 nbclient-0.5.1 nbconvert-6.0.7 nbformat-5.0.8 nest-asyncio-1.4.3 notebook-6.1.5 orjson-3.4.6 pandas-1.1.5 pandocfilters-1.4.3 pexpect-4.8.0 pickleshare-0.7.5 prometheus-client-0.9.0 prompt-toolkit-3.0.8 ptyprocess-0.6.0 pyrsistent-0.17.3 python-dateutil-2.8.1 pytz-2020.4 pyzmq-20.0.0 qtconsole-5.0.1 qtpy-1.9.0 terminado-0.9.1 testpath-0.4.4 tornado-6.1 traitlets-4.3.3 typing-extensions-3.7.4.3 wcwidth-0.2.5 webencodings-0.5.1 widgetsnbextension-3.5.1 zipp-3.4.0</p>
<p>WARNING: You are using pip version 20.1.1; however, version 20.3.3 is available.</p>
<p>You should consider upgrading via the ‘/Applications/Slicer.app/Contents/bin/./python-real -m pip install --upgrade pip’ command.</p>
<p>Enabling notebook extension jupyter-js-widgets/extension…</p>
<ul>
<li>Validating: e[32mOKe[0m</li>
</ul>
<p>Enabling notebook extension ipyevents/extension…</p>
<ul>
<li>Validating: e[32mOKe[0m</li>
</ul>
<p>Installed kernelspec slicer-4.11 in /Users/jon/Library/Jupyter/kernels/slicer-4.11</p>
<blockquote>
<blockquote>
<blockquote>
<p>pip_install(‘jupyterlab’)</p>
</blockquote>
</blockquote>
</blockquote>
<p>Collecting jupyterlab Using cached jupyterlab-2.2.9-py3-none-any.whl (7.9 MB)</p>
<p>Collecting jupyterlab-server&lt;2.0,&gt;=1.1.5</p>
<p>Using cached jupyterlab_server-1.2.0-py3-none-any.whl (29 kB)</p>
<p>Requirement already satisfied: tornado!=6.0.0,!=6.0.1,!=6.0.2 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from jupyterlab) (6.1)</p>
<p>Requirement already satisfied: jinja2&gt;=2.10 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from jupyterlab) (2.11.2)</p>
<p>Requirement already satisfied: notebook&gt;=4.3.1 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from jupyterlab) (6.1.5)</p>
<p>Requirement already satisfied: jsonschema&gt;=3.0.1 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from jupyterlab-server&lt;2.0,&gt;=1.1.5-&gt;jupyterlab) (3.2.0)</p>
<p>Collecting json5</p>
<p>Using cached json5-0.9.5-py2.py3-none-any.whl (17 kB)</p>
<p>Requirement already satisfied: requests in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from jupyterlab-server&lt;2.0,&gt;=1.1.5-&gt;jupyterlab) (2.24.0)</p>
<p>Requirement already satisfied: MarkupSafe&gt;=0.23 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from jinja2&gt;=2.10-&gt;jupyterlab) (1.1.1)</p>
<p>Requirement already satisfied: nbformat in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from notebook&gt;=4.3.1-&gt;jupyterlab) (5.0.8)</p>
<p>Requirement already satisfied: pyzmq&gt;=17 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from notebook&gt;=4.3.1-&gt;jupyterlab) (20.0.0)</p>
<p>Requirement already satisfied: ipython-genutils in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from notebook&gt;=4.3.1-&gt;jupyterlab) (0.2.0)</p>
<p>Requirement already satisfied: nbconvert in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from notebook&gt;=4.3.1-&gt;jupyterlab) (6.0.7)</p>
<p>Requirement already satisfied: ipykernel in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from notebook&gt;=4.3.1-&gt;jupyterlab) (5.4.2)</p>
<p>Requirement already satisfied: jupyter-client&gt;=5.3.4 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from notebook&gt;=4.3.1-&gt;jupyterlab) (6.1.7)</p>
<p>Requirement already satisfied: Send2Trash in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from notebook&gt;=4.3.1-&gt;jupyterlab) (1.5.0)</p>
<p>Requirement already satisfied: argon2-cffi in ./Slicer.app/Contents/Extensions-29402/SlicerJupyter/lib/python3.6/site-packages (from notebook&gt;=4.3.1-&gt;jupyterlab) (20.1.0)</p>
<p>Requirement already satisfied: prometheus-client in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from notebook&gt;=4.3.1-&gt;jupyterlab) (0.9.0)</p>
<p>Requirement already satisfied: terminado&gt;=0.8.3 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from notebook&gt;=4.3.1-&gt;jupyterlab) (0.9.1)</p>
<p>Requirement already satisfied: traitlets&gt;=4.2.1 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from notebook&gt;=4.3.1-&gt;jupyterlab) (4.3.3)</p>
<p>Requirement already satisfied: jupyter-core&gt;=4.6.1 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from notebook&gt;=4.3.1-&gt;jupyterlab) (4.7.0)</p>
<p>Requirement already satisfied: pyrsistent&gt;=0.14.0 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from jsonschema&gt;=3.0.1-&gt;jupyterlab-server&lt;2.0,&gt;=1.1.5-&gt;jupyterlab) (0.17.3)</p>
<p>Requirement already satisfied: six&gt;=1.11.0 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from jsonschema&gt;=3.0.1-&gt;jupyterlab-server&lt;2.0,&gt;=1.1.5-&gt;jupyterlab) (1.15.0)</p>
<p>Requirement already satisfied: importlib-metadata; python_version &lt; “3.8” in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from jsonschema&gt;=3.0.1-&gt;jupyterlab-server&lt;2.0,&gt;=1.1.5-&gt;jupyterlab) (3.3.0)</p>
<p>Requirement already satisfied: setuptools in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from jsonschema&gt;=3.0.1-&gt;jupyterlab-server&lt;2.0,&gt;=1.1.5-&gt;jupyterlab) (49.2.0)</p>
<p>Requirement already satisfied: attrs&gt;=17.4.0 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from jsonschema&gt;=3.0.1-&gt;jupyterlab-server&lt;2.0,&gt;=1.1.5-&gt;jupyterlab) (20.3.0)</p>
<p>Requirement already satisfied: certifi&gt;=2017.4.17 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from requests-&gt;jupyterlab-server&lt;2.0,&gt;=1.1.5-&gt;jupyterlab) (2020.6.20)</p>
<p>Requirement already satisfied: chardet&lt;4,&gt;=3.0.2 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from requests-&gt;jupyterlab-server&lt;2.0,&gt;=1.1.5-&gt;jupyterlab) (3.0.4)</p>
<p>Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,&lt;1.26,&gt;=1.21.1 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from requests-&gt;jupyterlab-server&lt;2.0,&gt;=1.1.5-&gt;jupyterlab) (1.25.10)</p>
<p>Requirement already satisfied: idna&lt;3,&gt;=2.5 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from requests-&gt;jupyterlab-server&lt;2.0,&gt;=1.1.5-&gt;jupyterlab) (2.10)</p>
<p>Requirement already satisfied: bleach in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from nbconvert-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (3.2.1)</p>
<p>Requirement already satisfied: pandocfilters&gt;=1.4.1 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from nbconvert-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (1.4.3)</p>
<p>Requirement already satisfied: mistune&lt;2,&gt;=0.8.1 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from nbconvert-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (0.8.4)</p>
<p>Requirement already satisfied: jupyterlab-pygments in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from nbconvert-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (0.1.2)</p>
<p>Requirement already satisfied: pygments&gt;=2.4.1 in ./Slicer.app/Contents/Extensions-29402/SlicerJupyter/lib/python3.6/site-packages (from nbconvert-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (2.4.1)</p>
<p>Requirement already satisfied: entrypoints&gt;=0.2.2 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from nbconvert-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (0.3)</p>
<p>Requirement already satisfied: defusedxml in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from nbconvert-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (0.6.0)</p>
<p>Requirement already satisfied: nbclient&lt;0.6.0,&gt;=0.5.0 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from nbconvert-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (0.5.1)</p>
<p>Requirement already satisfied: testpath in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from nbconvert-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (0.4.4)</p>
<p>Requirement already satisfied: appnope; platform_system == “Darwin” in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from ipykernel-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (0.1.2)</p>
<p>Requirement already satisfied: ipython&gt;=5.0.0 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from ipykernel-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (7.16.1)</p>
<p>Requirement already satisfied: python-dateutil&gt;=2.1 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from jupyter-client&gt;=5.3.4-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (2.8.1)</p>
<p>Requirement already satisfied: cffi&gt;=1.0.0 in ./Slicer.app/Contents/Extensions-29402/SlicerJupyter/lib/python3.6/site-packages (from argon2-cffi-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (1.14.4)</p>
<p>Requirement already satisfied: ptyprocess; os_name != “nt” in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from terminado&gt;=0.8.3-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (0.6.0)</p>
<p>Requirement already satisfied: decorator in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from traitlets&gt;=4.2.1-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (4.4.2)</p>
<p>Requirement already satisfied: typing-extensions&gt;=3.6.4; python_version &lt; “3.8” in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from importlib-metadata; python_version &lt; “3.8”-&gt;jsonschema&gt;=3.0.1-&gt;jupyterlab-server&lt;2.0,&gt;=1.1.5-&gt;jupyterlab) (3.7.4.3)</p>
<p>Requirement already satisfied: zipp&gt;=0.5 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from importlib-metadata; python_version &lt; “3.8”-&gt;jsonschema&gt;=3.0.1-&gt;jupyterlab-server&lt;2.0,&gt;=1.1.5-&gt;jupyterlab) (3.4.0)</p>
<p>Requirement already satisfied: packaging in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from bleach-&gt;nbconvert-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (20.4)</p>
<p>Requirement already satisfied: webencodings in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from bleach-&gt;nbconvert-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (0.5.1)</p>
<p>Requirement already satisfied: async-generator in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from nbclient&lt;0.6.0,&gt;=0.5.0-&gt;nbconvert-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (1.10)</p>
<p>Requirement already satisfied: nest-asyncio in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from nbclient&lt;0.6.0,&gt;=0.5.0-&gt;nbconvert-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (1.4.3)</p>
<p>Requirement already satisfied: backcall in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from ipython&gt;=5.0.0-&gt;ipykernel-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (0.2.0)</p>
<p>Requirement already satisfied: pexpect; sys_platform != “win32” in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from ipython&gt;=5.0.0-&gt;ipykernel-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (4.8.0)</p>
<p>Requirement already satisfied: jedi&gt;=0.10 in ./Slicer.app/Contents/Extensions-29402/SlicerJupyter/lib/python3.6/site-packages (from ipython&gt;=5.0.0-&gt;ipykernel-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (0.17.0)</p>
<p>Requirement already satisfied: pickleshare in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from ipython&gt;=5.0.0-&gt;ipykernel-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (0.7.5)</p>
<p>Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,&lt;3.1.0,&gt;=2.0.0 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from ipython&gt;=5.0.0-&gt;ipykernel-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (3.0.8)</p>
<p>Requirement already satisfied: pycparser in ./Slicer.app/Contents/Extensions-29402/SlicerJupyter/lib/python3.6/site-packages (from cffi&gt;=1.0.0-&gt;argon2-cffi-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (2.20)</p>
<p>Requirement already satisfied: pyparsing&gt;=2.0.2 in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from packaging-&gt;bleach-&gt;nbconvert-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (2.4.7)</p>
<p>Requirement already satisfied: parso&gt;=0.7.0 in ./Slicer.app/Contents/Extensions-29402/SlicerJupyter/lib/python3.6/site-packages (from jedi&gt;=0.10-&gt;ipython&gt;=5.0.0-&gt;ipykernel-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (0.7.1)</p>
<p>Requirement already satisfied: wcwidth in ./Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,&lt;3.1.0,&gt;=2.0.0-&gt;ipython&gt;=5.0.0-&gt;ipykernel-&gt;notebook&gt;=4.3.1-&gt;jupyterlab) (0.2.5)</p>
<p>Installing collected packages: json5, jupyterlab-server, jupyterlab</p>
<p>WARNING: The script pyjson5 is installed in ‘/Applications/Slicer.app/Contents/lib/Python/bin’ which is not on PATH.</p>
<p>Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.</p>
<p>WARNING: The scripts jlpm, jupyter-lab, jupyter-labextension and jupyter-labhub are installed in ‘/Applications/Slicer.app/Contents/lib/Python/bin’ which is not on PATH.</p>
<p>Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.</p>
<p>Successfully installed json5-0.9.5 jupyterlab-2.2.9 jupyterlab-server-1.2.0</p>
<p>WARNING: You are using pip version 20.1.1; however, version 20.3.3 is available.</p>
<p>You should consider upgrading via the ‘/Applications/Slicer.app/Contents/bin/./python-real -m pip install --upgrade pip’ command.</p>
</blockquote>
<blockquote>
<p>jon@Jonathans-MBP ~ % /Applications/Slicer.app/Contents/bin/./PythonSlicer -m pip install --upgrade pip<br>
Collecting pip<br>
Downloading pip-20.3.3-py2.py3-none-any.whl (1.5 MB)<br>
|████████████████████████████████| 1.5 MB 3.5 MB/s<br>
Installing collected packages: pip<br>
Attempting uninstall: pip<br>
Found existing installation: pip 20.1.1<br>
Uninstalling pip-20.1.1:<br>
Successfully uninstalled pip-20.1.1<br>
WARNING: The scripts pip, pip3 and pip3.6 are installed in ‘/Applications/Slicer.app/Contents/lib/Python/bin’ which is not on PATH.<br>
Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.<br>
Successfully installed pip-20.3.3</p>
</blockquote>

---

## Post #7 by @lassoan (2020-12-21 16:11 UTC)

<p>Thanks for the feedback. It’s good to know that the fix worked. I’ve added some notes on the warnings to the <a href="https://github.com/Slicer/SlicerJupyter/blob/master/README.md#notes">module documentation</a>.</p>

---
