---
topic_id: 43236
title: "Issue With Hdbrainextraction Tool Not Completing Error Messa"
date: 2025-06-05
url: https://discourse.slicer.org/t/43236
---

# Issue with HDBrainExtraction Tool Not Completing – Error Message Appears

**Topic ID**: 43236
**Date**: 2025-06-05
**URL**: https://discourse.slicer.org/t/issue-with-hdbrainextraction-tool-not-completing-error-message-appears/43236

---

## Post #1 by @MZA (2025-06-05 15:25 UTC)

<p>Hi everyone,</p>
<p>I’m encountering an issue while using the <strong>HDBrainExtraction</strong> tool. After selecting the source and output volume and clicking <strong>Apply</strong>, the process fails to complete. Instead, I get the pop-up error message shown in the attached screenshot.</p>
<p>I’m also posting two texts for reference:</p>
<ul>
<li>The next one contains the output shown when clicking the <strong>“Show details”</strong> button in the error message:</li>
</ul>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "C:\Users\mrasf\AppData\Local\slicer.org\Slicer 5.8.1\bin\Python\slicer\util.py", line 3303, in tryWithErrorDisplay
    yield
  File "C:/Users/mrasf/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/HDBrainExtraction/lib/Slicer-5.8/qt-scripted-modules/HDBrainExtractionTool.py", line 227, in onApplyButton
    self.logic.setupPythonRequirements()
  File "C:/Users/mrasf/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/HDBrainExtraction/lib/Slicer-5.8/qt-scripted-modules/HDBrainExtractionTool.py", line 308, in setupPythonRequirements
    slicer.util.pip_install('batchgenerators')
  File "C:\Users\mrasf\AppData\Local\slicer.org\Slicer 5.8.1\bin\Python\slicer\util.py", line 3942, in pip_install
    _executePythonModule("pip", args)
  File "C:\Users\mrasf\AppData\Local\slicer.org\Slicer 5.8.1\bin\Python\slicer\util.py", line 3896, in _executePythonModule
    logProcessOutput(proc)
  File "C:\Users\mrasf\AppData\Local\slicer.org\Slicer 5.8.1\bin\Python\slicer\util.py", line 3862, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Users/mrasf/AppData/Local/slicer.org/Slicer 5.8.1/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'batchgenerators']' returned non-zero exit status 1.
</code></pre>
<ul>
<li>The other is the Python Console log at the time of the error:</li>
</ul>
<pre><code class="lang-auto">Collecting batchgenerators
  Using cached batchgenerators-0.25.1.tar.gz (76 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Requirement already satisfied: pillow&gt;=7.1.2 in c:\users\mrasf\appdata\local\slicer.org\slicer 5.8.1\lib\python\lib\site-packages (from batchgenerators) (10.3.0)
Requirement already satisfied: numpy&gt;=1.10.2 in c:\users\mrasf\appdata\local\slicer.org\slicer 5.8.1\lib\python\lib\site-packages (from batchgenerators) (1.26.4)
Requirement already satisfied: scipy in c:\users\mrasf\appdata\local\slicer.org\slicer 5.8.1\lib\python\lib\site-packages (from batchgenerators) (1.13.1)
Collecting scikit-image (from batchgenerators)
  Using cached scikit_image-0.24.0-cp39-cp39-win_amd64.whl.metadata (14 kB)
Collecting scikit-learn (from batchgenerators)
  Using cached scikit_learn-1.6.1-cp39-cp39-win_amd64.whl.metadata (15 kB)
Collecting future (from batchgenerators)
  Using cached future-1.0.0-py3-none-any.whl.metadata (4.0 kB)
Collecting pandas (from batchgenerators)
  Using cached pandas-2.3.0.tar.gz (4.5 MB)
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Installing backend dependencies: started
  Installing backend dependencies: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'error'
  error: subprocess-exited-with-error

  Preparing metadata (pyproject.toml) did not run successfully.
  exit code: 1

  [10 lines of output]
  + meson setup C:\Users\mrasf\AppData\Local\Temp\pip-install-0i038abm\pandas_a4d32aa1603d435e9c1558c96e77e301 C:\Users\mrasf\AppData\Local\Temp\pip-install-0i038abm\pandas_a4d32aa1603d435e9c1558c96e77e301\.mesonpy-6sv7bkf5 -Dbuildtype=release -Db_ndebug=if-release -Db_vscrt=md --vsenv --native-file=C:\Users\mrasf\AppData\Local\Temp\pip-install-0i038abm\pandas_a4d32aa1603d435e9c1558c96e77e301\.mesonpy-6sv7bkf5\meson-python-native-file.ini
  The Meson build system
  Version: 1.8.1
  Source dir: C:\Users\mrasf\AppData\Local\Temp\pip-install-0i038abm\pandas_a4d32aa1603d435e9c1558c96e77e301
  Build dir: C:\Users\mrasf\AppData\Local\Temp\pip-install-0i038abm\pandas_a4d32aa1603d435e9c1558c96e77e301\.mesonpy-6sv7bkf5
  Build type: native build

  ..\meson.build:2:0: ERROR: Could not find C:\Program Files (x86)\Microsoft Visual Studio\Installer\vswhere.exe

  A full log can be found at C:\Users\mrasf\AppData\Local\Temp\pip-install-0i038abm\pandas_a4d32aa1603d435e9c1558c96e77e301\.mesonpy-6sv7bkf5\meson-logs\meson-log.txt
  [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

Encountered error while generating package metadata.

See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.
[Python] Failed to compute results.
[Python] Command '['C:/Users/mrasf/AppData/Local/slicer.org/Slicer 5.8.1/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'batchgenerators']' returned non-zero exit status 1.
Traceback (most recent call last):
  File "C:/Users/mrasf/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/HDBrainExtraction/lib/Slicer-5.8/qt-scripted-modules/HDBrainExtractionTool.py", line 227, in onApplyButton
    self.logic.setupPythonRequirements()
  File "C:/Users/mrasf/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/HDBrainExtraction/lib/Slicer-5.8/qt-scripted-modules/HDBrainExtractionTool.py", line 308, in setupPythonRequirements
    slicer.util.pip_install('batchgenerators')
  File "C:\Users\mrasf\AppData\Local\slicer.org\Slicer 5.8.1\bin\Python\slicer\util.py", line 3942, in pip_install
    _executePythonModule("pip", args)
  File "C:\Users\mrasf\AppData\Local\slicer.org\Slicer 5.8.1\bin\Python\slicer\util.py", line 3896, in _executePythonModule
    logProcessOutput(proc)
  File "C:\Users\mrasf\AppData\Local\slicer.org\Slicer 5.8.1\bin\Python\slicer\util.py", line 3862, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Users/mrasf/AppData/Local/slicer.org/Slicer 5.8.1/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'batchgenerators']' returned non-zero exit status 1.
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c92aec51a54d84eb6f2cc25790170ce5b058a16a.jpeg" data-download-href="/uploads/short-url/sHBVTZSlQxpPQAZFHSKH2UfW8FY.jpeg?dl=1" title="hdbrainextractionerror" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c92aec51a54d84eb6f2cc25790170ce5b058a16a.jpeg" alt="hdbrainextractionerror" data-base62-sha1="sHBVTZSlQxpPQAZFHSKH2UfW8FY" width="668" height="146"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">hdbrainextractionerror</span><span class="informations">668×146 22.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Any suggestions for resolving this?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @jamesobutler (2025-06-05 18:36 UTC)

<p>It is trying to install latest <code>pandas</code>, but the <code>pandas</code> maintainers made a mistake in their most recent 2.3.0 release that came out yesterday (see issue linked below). The release notes specify that their intention was for this release to require Python 3.10 or newer, but their configuration stated that it was still Python 3.9 or newer. There are no Python 3.9 wheels for pandas <code>2.3.0</code> based on their intention to not support this python version.</p>
<p>For Slicer 5.8.1 you can instead call <code>slicer.util.pip_install("pandas&lt;2.3.0")</code> to resolve this issue with HDBrainExtraction.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/pandas-dev/pandas/issues/61563">
  <header class="source">

      <a href="https://github.com/pandas-dev/pandas/issues/61563" target="_blank" rel="noopener nofollow ugc">github.com/pandas-dev/pandas</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/pandas-dev/pandas/issues/61563" target="_blank" rel="noopener nofollow ugc">Failed to install pandas==2.3.0 with Python 3.9</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-06-05" data-time="04:11:02" data-timezone="UTC">04:11AM - 05 Jun 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/ryanchao2012" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/7628311?v=4" class="onebox-avatar-inline" width="20" height="20">
          ryanchao2012
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Build
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Needs Triage
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">### Installation check

- [x] I have read the [installation guide](https://panda<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">s.pydata.org/pandas-docs/stable/getting_started/install.html#installing-pandas).


### Platform

Linux-5.10.195-1.20230921.el7.x86_64-x86_64-with-glibc2.17

### Installation Method

pip install

### pandas Version

2.3.0

### Python Version

3.9.15

### Installation Logs

&lt;details&gt;
(base) [root@64bf929a621d7dafeb18b348 ~]# python -c 'import platform; print(platform.platform())'
Linux-5.10.195-1.20230921.el7.x86_64-x86_64-with-glibc2.17

(base) [root@64bf929a621d7dafeb18b348 ~]# pip install pandas -U
Requirement already satisfied: pandas in /opt/conda/lib/python3.9/site-packages (1.5.0)
Collecting pandas
  Downloading pandas-2.3.0.tar.gz (4.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/4.5 MB 90.9 MB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... error
  error: subprocess-exited-with-error

  × Preparing metadata (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─&gt; [152 lines of output]
      + meson setup /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86 /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/.mesonpy-lsu89q1a -Dbuildtype=release -Db_ndebug=if-release -Db_vscrt=md --vsenv --native-file=/tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/.mesonpy-lsu89q1a/meson-python-native-file.ini
      The Meson build system
      Version: 1.8.1
      Source dir: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86
      Build dir: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/.mesonpy-lsu89q1a
      Build type: native build
      Project name: pandas
      Project version: 2.3.0
      C compiler for the host machine: cc (gcc 4.8.5 "cc (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44)")
      C linker for the host machine: cc ld.bfd 2.27-44
      C++ compiler for the host machine: c++ (gcc 4.8.5 "c++ (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44)")
      C++ linker for the host machine: c++ ld.bfd 2.27-44
      Cython compiler for the host machine: cython (cython 3.1.1)
      Host machine cpu family: x86_64
      Host machine cpu: x86_64
      Program python found: YES (/opt/conda/bin/python)
      Found pkg-config: YES (/usr/bin/pkg-config) 0.27.1
      Run-time dependency python found: YES 3.9
      Build targets in project: 53

      pandas 2.3.0

        User defined options
          Native files: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/.mesonpy-lsu89q1a/meson-python-native-file.ini
          b_ndebug    : if-release
          b_vscrt     : md
          buildtype   : release
          vsenv       : true

      Found ninja-1.11.1.git.kitware.jobserver-1 at /tmp/pip-build-env-ltjugjgm/normal/bin/ninja

      Visual Studio environment is needed to run Ninja. It is recommended to use Meson wrapper:
      /tmp/pip-build-env-ltjugjgm/overlay/bin/meson compile -C .
      + /tmp/pip-build-env-ltjugjgm/normal/bin/ninja
      [1/151] Generating pandas/_libs/intervaltree_helper_pxi with a custom command
      [2/151] Generating pandas/_libs/hashtable_func_helper_pxi with a custom command
      [3/151] Generating pandas/_libs/algos_common_helper_pxi with a custom command
      [4/151] Generating pandas/_libs/khash_primitive_helper_pxi with a custom command
      [5/151] Generating pandas/_libs/index_class_helper_pxi with a custom command
      [6/151] Generating pandas/_libs/algos_take_helper_pxi with a custom command
      [7/151] Generating pandas/_libs/hashtable_class_helper_pxi with a custom command
      [8/151] Copying file pandas/__init__.py
      [9/151] Generating pandas/_libs/sparse_op_helper_pxi with a custom command
      [10/151] Compiling C object pandas/_libs/json.cpython-39-x86_64-linux-gnu.so.p/src_vendored_ujson_lib_ultrajsonenc.c.o
      FAILED: pandas/_libs/json.cpython-39-x86_64-linux-gnu.so.p/src_vendored_ujson_lib_ultrajsonenc.c.o
      cc -Ipandas/_libs/json.cpython-39-x86_64-linux-gnu.so.p -Ipandas/_libs -I../pandas/_libs -I../../../pip-build-env-ltjugjgm/overlay/lib/python3.9/site-packages/numpy/_core/include -I../pandas/_libs/include -I/opt/conda/include/python3.9 -fvisibility=hidden -DNDEBUG -D_FILE_OFFSET_BITS=64 -Wall -Winvalid-pch -Wextra -std=c11 -O3 -DNPY_NO_DEPRECATED_API=0 -DNPY_TARGET_VERSION=NPY_1_21_API_VERSION -fPIC -MD -MQ pandas/_libs/json.cpython-39-x86_64-linux-gnu.so.p/src_vendored_ujson_lib_ultrajsonenc.c.o -MF pandas/_libs/json.cpython-39-x86_64-linux-gnu.so.p/src_vendored_ujson_lib_ultrajsonenc.c.o.d -o pandas/_libs/json.cpython-39-x86_64-linux-gnu.so.p/src_vendored_ujson_lib_ultrajsonenc.c.o -c ../pandas/_libs/src/vendored/ujson/lib/ultrajsonenc.c
      In file included from ../pandas/_libs/src/vendored/ujson/lib/ultrajsonenc.c:43:0:
      ../pandas/_libs/include/pandas/portable.h:31:22: error: missing binary operator before token "("
       #elif __has_attribute(__fallthrough__)
                            ^
      [11/151] Compiling C object pandas/_libs/pandas_parser.cpython-39-x86_64-linux-gnu.so.p/src_parser_io.c.o
      [12/151] Compiling C object pandas/_libs/pandas_datetime.cpython-39-x86_64-linux-gnu.so.p/src_vendored_numpy_datetime_np_datetime.c.o
      FAILED: pandas/_libs/pandas_datetime.cpython-39-x86_64-linux-gnu.so.p/src_vendored_numpy_datetime_np_datetime.c.o
      cc -Ipandas/_libs/pandas_datetime.cpython-39-x86_64-linux-gnu.so.p -Ipandas/_libs -I../pandas/_libs -I../../../pip-build-env-ltjugjgm/overlay/lib/python3.9/site-packages/numpy/_core/include -I../pandas/_libs/include -I/opt/conda/include/python3.9 -fvisibility=hidden -DNDEBUG -D_FILE_OFFSET_BITS=64 -Wall -Winvalid-pch -Wextra -std=c11 -O3 -DNPY_NO_DEPRECATED_API=0 -DNPY_TARGET_VERSION=NPY_1_21_API_VERSION -fPIC -MD -MQ pandas/_libs/pandas_datetime.cpython-39-x86_64-linux-gnu.so.p/src_vendored_numpy_datetime_np_datetime.c.o -MF pandas/_libs/pandas_datetime.cpython-39-x86_64-linux-gnu.so.p/src_vendored_numpy_datetime_np_datetime.c.o.d -o pandas/_libs/pandas_datetime.cpython-39-x86_64-linux-gnu.so.p/src_vendored_numpy_datetime_np_datetime.c.o -c ../pandas/_libs/src/vendored/numpy/datetime/np_datetime.c
      ../pandas/_libs/src/vendored/numpy/datetime/np_datetime.c:57:1: error: static assertion failed: "__has_builtin not detected; please try a newer compiler"
       _Static_assert(0, "__has_builtin not detected; please try a newer compiler");
       ^
      ../pandas/_libs/src/vendored/numpy/datetime/np_datetime.c: In function ‘scaleYearToEpoch’:
      ../pandas/_libs/src/vendored/numpy/datetime/np_datetime.c:343:3: warning: implicit declaration of function ‘checked_int64_sub’ [-Wimplicit-function-declaration]
         return checked_int64_sub(year, 1970, result);
         ^
      ../pandas/_libs/src/vendored/numpy/datetime/np_datetime.c: In function ‘scaleYearsToMonths’:
      ../pandas/_libs/src/vendored/numpy/datetime/np_datetime.c:347:3: warning: implicit declaration of function ‘checked_int64_mul’ [-Wimplicit-function-declaration]
         return checked_int64_mul(years, 12, result);
         ^
      ../pandas/_libs/src/vendored/numpy/datetime/np_datetime.c: In function ‘npy_datetimestruct_to_datetime’:
      ../pandas/_libs/src/vendored/numpy/datetime/np_datetime.c:425:5: warning: implicit declaration of function ‘checked_int64_add’ [-Wimplicit-function-declaration]
           PD_CHECK_OVERFLOW(checked_int64_add(months, months_adder, &amp;months));
           ^
      [13/151] Compiling C object pandas/_libs/pandas_parser.cpython-39-x86_64-linux-gnu.so.p/src_parser_pd_parser.c.o
      [14/151] Compiling C object pandas/_libs/pandas_datetime.cpython-39-x86_64-linux-gnu.so.p/src_datetime_date_conversions.c.o
      [15/151] Compiling C object pandas/_libs/json.cpython-39-x86_64-linux-gnu.so.p/src_vendored_ujson_python_JSONtoObj.c.o
      [16/151] Compiling C object pandas/_libs/pandas_datetime.cpython-39-x86_64-linux-gnu.so.p/src_datetime_pd_datetime.c.o
      [17/151] Compiling C object pandas/_libs/json.cpython-39-x86_64-linux-gnu.so.p/src_vendored_ujson_python_ujson.c.o
      [18/151] Compiling C object pandas/_libs/pandas_datetime.cpython-39-x86_64-linux-gnu.so.p/src_vendored_numpy_datetime_np_datetime_strings.c.o
      [19/151] Compiling C object pandas/_libs/json.cpython-39-x86_64-linux-gnu.so.p/src_vendored_ujson_python_objToJSON.c.o
      [20/151] Compiling C object pandas/_libs/tslibs/parsing.cpython-39-x86_64-linux-gnu.so.p/.._src_parser_tokenizer.c.o
      [21/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/indexing.pyx
      [22/151] Compiling C object pandas/_libs/pandas_parser.cpython-39-x86_64-linux-gnu.so.p/src_parser_tokenizer.c.o
      [23/151] Compiling C object pandas/_libs/lib.cpython-39-x86_64-linux-gnu.so.p/src_parser_tokenizer.c.o
      [24/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/ccalendar.pyx
      [25/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/base.pyx
      [26/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/np_datetime.pyx
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:188:38: noexcept clause is ignored for function returning Python object
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:193:40: noexcept clause is ignored for function returning Python object
      [27/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/missing.pyx
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:188:38: noexcept clause is ignored for function returning Python object
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:193:40: noexcept clause is ignored for function returning Python object
      [28/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/dtypes.pyx
      [29/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/arrays.pyx
      [30/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/hashing.pyx
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:188:38: noexcept clause is ignored for function returning Python object
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:193:40: noexcept clause is ignored for function returning Python object
      [31/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/nattype.pyx
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:188:38: noexcept clause is ignored for function returning Python object
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:193:40: noexcept clause is ignored for function returning Python object
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/nattype.pyx:79:0: Global name __nat_unpickle matched from within class scope in contradiction to to Python 'class private name' rules. This may change in a future release.
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/nattype.pyx:79:0: Global name __nat_unpickle matched from within class scope in contradiction to to Python 'class private name' rules. This may change in a future release.
      [32/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/vectorized.pyx
      [33/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/fields.pyx
      [34/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/internals.pyx
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:188:38: noexcept clause is ignored for function returning Python object
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:193:40: noexcept clause is ignored for function returning Python object
      [35/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/conversion.pyx
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:188:38: noexcept clause is ignored for function returning Python object
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:193:40: noexcept clause is ignored for function returning Python object
      [36/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/parsing.pyx
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:188:38: noexcept clause is ignored for function returning Python object
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:193:40: noexcept clause is ignored for function returning Python object
      [37/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/timezones.pyx
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:188:38: noexcept clause is ignored for function returning Python object
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:193:40: noexcept clause is ignored for function returning Python object
      [38/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/tzconversion.pyx
      [39/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/strptime.pyx
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:188:38: noexcept clause is ignored for function returning Python object
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:193:40: noexcept clause is ignored for function returning Python object
      [40/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/parsers.pyx
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:188:38: noexcept clause is ignored for function returning Python object
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:193:40: noexcept clause is ignored for function returning Python object
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/parsers.pyx:1605:18: noexcept clause is ignored for function returning Python object
      [41/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/timestamps.pyx
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:188:38: noexcept clause is ignored for function returning Python object
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:193:40: noexcept clause is ignored for function returning Python object
      [42/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/period.pyx
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:188:38: noexcept clause is ignored for function returning Python object
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:193:40: noexcept clause is ignored for function returning Python object
      [43/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/timedeltas.pyx
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:188:38: noexcept clause is ignored for function returning Python object
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:193:40: noexcept clause is ignored for function returning Python object
      [44/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/offsets.pyx
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:188:38: noexcept clause is ignored for function returning Python object
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:193:40: noexcept clause is ignored for function returning Python object
      [45/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/lib.pyx
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:188:38: noexcept clause is ignored for function returning Python object
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:193:40: noexcept clause is ignored for function returning Python object
      [46/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/index.pyx
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:188:38: noexcept clause is ignored for function returning Python object
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:193:40: noexcept clause is ignored for function returning Python object
      [47/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/interval.pyx
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:188:38: noexcept clause is ignored for function returning Python object
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:193:40: noexcept clause is ignored for function returning Python object
      [48/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/join.pyx
      [49/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/hashtable.pyx
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:188:38: noexcept clause is ignored for function returning Python object
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:193:40: noexcept clause is ignored for function returning Python object
      [50/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/algos.pyx
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:188:38: noexcept clause is ignored for function returning Python object
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:193:40: noexcept clause is ignored for function returning Python object
      [51/151] Compiling Cython source /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/groupby.pyx
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:188:38: noexcept clause is ignored for function returning Python object
      warning: /tmp/pip-install-gp_gpioe/pandas_8608342ddb164d0e8725d2463640de86/pandas/_libs/tslibs/util.pxd:193:40: noexcept clause is ignored for function returning Python object
      ninja: build stopped: subcommand failed.
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─&gt; See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.


&lt;/details&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It seems like <code>pandas</code> may ultimately provide Python 3.9 wheels for version 2.3.0 since their own testing seemed to pass on Python 3.9. You could monitor the following PR. Maybe they will release a 2.3.1 soon that states that will still support Python 3.9 for one last time.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/pandas-dev/pandas/pull/61569">
  <header class="source">

      <a href="https://github.com/pandas-dev/pandas/pull/61569" target="_blank" rel="noopener nofollow ugc">github.com/pandas-dev/pandas</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/pandas-dev/pandas/pull/61569" target="_blank" rel="noopener nofollow ugc">BLD: Build wheels for 3.9</a>
      </h4>

    <div class="branches">
      <code>2.3.x</code> ← <code>mroeschke:ci/wheels/39</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-06-05" data-time="17:29:26" data-timezone="UTC">05:29PM - 05 Jun 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/mroeschke" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://avatars.githubusercontent.com/u/10647082?v=4" class="onebox-avatar-inline" width="20" height="20">
            mroeschke
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 1 additions and 1 deletions">
          <a href="https://github.com/pandas-dev/pandas/pull/61569/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+1</span>
            <span class="removed">-1</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">@lithomas1 would I need to re-tag the 2.3.x branch if/when we merge this?

xre<span class="show-more-container"><a href="https://github.com/pandas-dev/pandas/pull/61569" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">f https://github.com/pandas-dev/pandas/issues/61563</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>For Slicer Preview, you will soon not have to do this workaround as Slicer is moving from using Python 3.9 to Python 3.12 (see PR below). It is not the first time that some python packages have dropped Python 3.9 support, but then did not appropriately update their configurations to state this as well.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8466">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8466" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8466" target="_blank" rel="noopener nofollow ugc">ENH: Upgrade from python 3.9.10 to 3.12.10</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>jcfr:transition-from-python-3.9-to-3.12-repushed</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-06-05" data-time="01:32:23" data-timezone="UTC">01:32AM - 05 Jun 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jcfr" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
            jcfr
          </a>
        </div>

        <div class="lines" title="1 commits changed 9 files with 97 additions and 97 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8466/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+97</span>
            <span class="removed">-97</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This pull request was created to include the changes originally integrated throu<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8466" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">gh this pull requests:
* https://github.com/Slicer/Slicer/pull/8456

For the sake of having a clean history and considering the updated `main` branch has not been referenced externally, `main` was forced push to https://github.com/Slicer/Slicer/commit/4b1666ec317ab1885f1b02354ac2f78708cb29f4

---- 

&gt; [!IMPORTANT]
&gt; This pull request should be rebased &amp; integrated *only* after the pull requests referenced below are themselves reviewed &amp; integrated:
&gt; * https://github.com/Slicer/Slicer/pull/8454
&gt; * https://github.com/Slicer/Slicer/pull/8457
&gt; * https://github.com/Slicer/Slicer/pull/8459
&gt; * https://github.com/Slicer/Slicer/pull/8461
&gt; * https://github.com/Slicer/Slicer/pull/8467</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @MZA (2025-06-06 21:08 UTC)

<p>Thanks James, it’s working now!</p>

---

## Post #4 by @jamesobutler (2025-06-07 00:03 UTC)

<p>Looks like the <code>pandas</code> developers have now uploaded the Python 3.9 whls for version <code>2.3.0</code> even though they originally intended not to for this version. Therefore the workaround of forcing a earlier version is no longer needed.</p>

---
