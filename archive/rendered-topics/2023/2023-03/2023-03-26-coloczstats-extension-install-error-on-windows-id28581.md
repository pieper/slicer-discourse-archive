# 'ColocZStats' extension install error on Windows

**Topic ID**: 28581
**Date**: 2023-03-26
**URL**: https://discourse.slicer.org/t/coloczstats-extension-install-error-on-windows/28581

---

## Post #1 by @CharlesChen (2023-03-26 03:26 UTC)

<p>OS: Win 10<br>
Version: 3D Slicer Stable 5.2.2</p>
<p>Hi there,<br>
I downloaded and installed the 3D Slicer stable version 5.2.2 on my windows for the first time.</p>
<p>After installing the ‘ColocZStats’ extension through its built-in ‘Extension Manager’ and restarting Slicer. The ‘ColocZStats’ can’t be found by searching in the ‘Module finder’.</p>
<p>Meanwhile, I got the following error messages in the Python Console:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
File "C:/Users/xiang/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/ColocZStats/lib/Slicer-5.2/qt-scripted-modules/ColocZStats.py", line 62, in &lt;module&gt;
  from skimage import morphology
ModuleNotFoundError: No module named 'skimage'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
File "&lt;string&gt;", line 1, in &lt;module&gt;
File "C:\Users\xiang\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\imp.py", line 169, in load_source
  module = _exec(spec, sys.modules[name])
File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
File "C:/Users/xiang/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/ColocZStats/lib/Slicer-5.2/qt-scripted-modules/ColocZStats.py", line 64, in &lt;module&gt;
  slicer.util.pip_install("scikit-image")
File "C:\Users\xiang\AppData\Local\NA-MIC\Slicer 5.2.2\bin\Python\slicer\util.py", line 3578, in pip_install
  _executePythonModule('pip', args)
File "C:\Users\xiang\AppData\Local\NA-MIC\Slicer 5.2.2\bin\Python\slicer\util.py", line 3540, in _executePythonModule
  logProcessOutput(proc)
File "C:\Users\xiang\AppData\Local\NA-MIC\Slicer 5.2.2\bin\Python\slicer\util.py", line 3509, in logProcessOutput
  raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Users/xiang/AppData/Local/NA-MIC/Slicer 5.2.2/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'scikit-image']' returned non-zero exit status 1.
[Qt] loadSourceAsModule - Failed to load file "C:/Users/xiang/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/ColocZStats/lib/Slicer-5.2/qt-scripted-modules/ColocZStats.py"  as module "ColocZStats" !
[Qt] Fail to instantiate module  "ColocZStats"
[Qt] The following modules failed to be instantiated:
[Qt]    ColocZStats
</code></pre>
<p>The reason seems to be the unsuccessful install/import of ‘skimage’ and ‘morphology’.</p>
<p>Here is how the ‘skimage’ and ‘morphology’ are installed/imported in ColocZStats.py:</p>
<pre><code class="lang-auto">try:
    from skimage import morphology
except ModuleNotFoundError:
    slicer.util.pip_install("scikit-image")
    from skimage import morphology
</code></pre>
<p>However, when I restart Slicer again, the ‘ColocZStats’ extension can be searched in the ‘Modules finder’ and works normally.</p>
<p>I checked the SlicerStable dashboard,  the test output of ColocZStats on Windows seems to show the same information as above:  <a href="https://slicer.cdash.org/test/24353596" rel="noopener nofollow ugc">https://slicer.cdash.org/test/24353596</a></p>
<pre><code class="lang-auto">Collecting matplotlib
  Using cached matplotlib-3.7.1-cp39-cp39-win_amd64.whl (7.6 MB)
Requirement already satisfied: pillow&gt;=6.2.0 in d:\d\s\s-0-build\python-install\lib\site-packages (from matplotlib) (9.4.0)
Collecting importlib-resources&gt;=3.2.0
  Using cached importlib_resources-5.12.0-py3-none-any.whl (36 kB)
Requirement already satisfied: numpy&gt;=1.20 in d:\d\s\s-0-build\python-install\lib\site-packages (from matplotlib) (1.23.4)
Collecting contourpy&gt;=1.0.1
  Using cached contourpy-1.0.7-cp39-cp39-win_amd64.whl (160 kB)
Requirement already satisfied: pyparsing&gt;=2.3.1 in d:\d\s\s-0-build\python-install\lib\site-packages (from matplotlib) (3.0.9)
Requirement already satisfied: packaging&gt;=20.0 in d:\d\s\s-0-build\python-install\lib\site-packages (from matplotlib) (23.0)
Collecting cycler&gt;=0.10
  Using cached cycler-0.11.0-py3-none-any.whl (6.4 kB)
Collecting kiwisolver&gt;=1.0.1
  Using cached kiwisolver-1.4.4-cp39-cp39-win_amd64.whl (55 kB)
Collecting fonttools&gt;=4.22.0
  Using cached fonttools-4.39.2-py3-none-any.whl (1.0 MB)
Collecting python-dateutil&gt;=2.7
  Using cached python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
Collecting zipp&gt;=3.1.0
  Using cached zipp-3.15.0-py3-none-any.whl (6.8 kB)
Requirement already satisfied: six&gt;=1.5 in d:\d\s\s-0-build\python-install\lib\site-packages (from python-dateutil&gt;=2.7-&gt;matplotlib) (1.16.0)
Installing collected packages: zipp, python-dateutil, kiwisolver, fonttools, cycler, contourpy, importlib-resources, matplotlib
  WARNING: The scripts fonttools.exe, pyftmerge.exe, pyftsubset.exe and ttx.exe are installed in 'D:\D\S\S-0-build\python-install\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed contourpy-1.0.7 cycler-0.11.0 fonttools-4.39.2 importlib-resources-5.12.0 kiwisolver-1.4.4 matplotlib-3.7.1 python-dateutil-2.8.2 zipp-3.15.0

[notice] A new release of pip is available: 23.0 -&gt; 23.0.1
[notice] To update, run: python.exe -m pip install --upgrade pip
Collecting pandas
  Using cached pandas-1.5.3-cp39-cp39-win_amd64.whl (10.9 MB)
Requirement already satisfied: python-dateutil&gt;=2.8.1 in d:\d\s\s-0-build\python-install\lib\site-packages (from pandas) (2.8.2)
Requirement already satisfied: numpy&gt;=1.20.3 in d:\d\s\s-0-build\python-install\lib\site-packages (from pandas) (1.23.4)
Collecting pytz&gt;=2020.1
  Downloading pytz-2023.2-py2.py3-none-any.whl (502 kB)
     ------------------------------------- 502.1/502.1 kB 10.5 MB/s eta 0:00:00
Requirement already satisfied: six&gt;=1.5 in d:\d\s\s-0-build\python-install\lib\site-packages (from python-dateutil&gt;=2.8.1-&gt;pandas) (1.16.0)
Installing collected packages: pytz, pandas
Successfully installed pandas-1.5.3 pytz-2023.2

[notice] A new release of pip is available: 23.0 -&gt; 23.0.1
[notice] To update, run: python.exe -m pip install --upgrade pip
Collecting xlsxwriter
  Using cached XlsxWriter-3.0.9-py3-none-any.whl (152 kB)
Installing collected packages: xlsxwriter
Successfully installed xlsxwriter-3.0.9

[notice] A new release of pip is available: 23.0 -&gt; 23.0.1
[notice] To update, run: python.exe -m pip install --upgrade pip
Collecting tifffile
  Using cached tifffile-2023.3.21-py3-none-any.whl (218 kB)
Requirement already satisfied: numpy in d:\d\s\s-0-build\python-install\lib\site-packages (from tifffile) (1.23.4)
Installing collected packages: tifffile
  WARNING: The scripts lsm2bin.exe, tiff2fsspec.exe, tiffcomment.exe and tifffile.exe are installed in 'D:\D\S\S-0-build\python-install\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed tifffile-2023.3.21

[notice] A new release of pip is available: 23.0 -&gt; 23.0.1
[notice] To update, run: python.exe -m pip install --upgrade pip
Collecting scikit-image
  Using cached scikit_image-0.20.0-cp39-cp39-win_amd64.whl (23.9 MB)
Requirement already satisfied: packaging&gt;=20.0 in d:\d\s\s-0-build\python-install\lib\site-packages (from scikit-image) (23.0)
Requirement already satisfied: tifffile&gt;=2019.7.26 in d:\d\s\s-0-build\python-install\lib\site-packages (from scikit-image) (2023.3.21)
Collecting networkx&gt;=2.8
  Using cached networkx-3.0-py3-none-any.whl (2.0 MB)
Collecting lazy_loader&gt;=0.1
  Using cached lazy_loader-0.2-py3-none-any.whl (8.6 kB)
Collecting imageio&gt;=2.4.1
  Using cached imageio-2.26.1-py3-none-any.whl (3.4 MB)
Collecting scipy&lt;1.9.2,&gt;=1.8
  Using cached scipy-1.9.1-cp39-cp39-win_amd64.whl (38.6 MB)
Requirement already satisfied: pillow&gt;=9.0.1 in d:\d\s\s-0-build\python-install\lib\site-packages (from scikit-image) (9.4.0)
Collecting PyWavelets&gt;=1.1.1
  Using cached PyWavelets-1.4.1-cp39-cp39-win_amd64.whl (4.2 MB)
Requirement already satisfied: numpy&gt;=1.21.1 in d:\d\s\s-0-build\python-install\lib\site-packages (from scikit-image) (1.23.4)
Installing collected packages: scipy, PyWavelets, networkx, lazy_loader, imageio, scikit-image
  Attempting uninstall: scipy
    Found existing installation: scipy 1.9.2
    Uninstalling scipy-1.9.2:
      Successfully uninstalled scipy-1.9.2
ERROR: Could not install packages due to an OSError: [WinError 5] Access is denied: 'D:\\D\\S\\S-0-build\\python-install\\Lib\\site-packages\\~cipy\\_lib\\_ccallback_c.cp39-win_amd64.pyd'
Consider using the `--user` option or check the permissions.


[notice] A new release of pip is available: 23.0 -&gt; 23.0.1
[notice] To update, run: python.exe -m pip install --upgrade pip
Traceback (most recent call last):
  File "D:/D/S/S-0-E-b/ColocZStats-build/lib/Slicer-5.2/qt-scripted-modules/ColocZStats.py", line 62, in &lt;module&gt;
    from skimage import morphology
ModuleNotFoundError: No module named 'skimage'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "D:\D\S\S-0-build\python-install\Lib\imp.py", line 169, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "D:/D/S/S-0-E-b/ColocZStats-build/lib/Slicer-5.2/qt-scripted-modules/ColocZStats.py", line 64, in &lt;module&gt;
    slicer.util.pip_install("scikit-image")
  File "D:\D\S\S-0-build\Slicer-build\bin\Python\slicer\util.py", line 3578, in pip_install
    _executePythonModule('pip', args)
  File "D:\D\S\S-0-build\Slicer-build\bin\Python\slicer\util.py", line 3540, in _executePythonModule
    logProcessOutput(proc)
  File "D:\D\S\S-0-build\Slicer-build\bin\Python\slicer\util.py", line 3509, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['D:/D/S/S-0-build/python-install/bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'scikit-image']' returned non-zero exit status 1.
loadSourceAsModule - Failed to load file "D:/D/S/S-0-E-b/ColocZStats-build/lib/Slicer-5.2/qt-scripted-modules/ColocZStats.py"  as module "ColocZStats" !
Fail to instantiate module  "ColocZStats"
The following modules failed to be instantiated:
   ColocZStats
</code></pre>
<p>What exactly should I do to fix it?</p>
<p>In addition, according to the SlicerStable dashboard, there are two tests of ColocZStats on MacoOS failed. The ‘Details’ shows ‘Timeout’, and the ‘Summary’ shows ‘Unstable’. The following are the test outputs: <a href="https://slicer.cdash.org/viewTest.php?onlyfailed&amp;buildid=2979269" rel="noopener nofollow ugc">https://slicer.cdash.org/viewTest.php?onlyfailed&amp;buildid=2979269</a></p>
<p>py_ColocZStats:</p>
<pre><code class="lang-auto">Collecting pandas
</code></pre>
<p>py_nomainwindow_qSlicerColocZStatsModuleGenericTest:</p>
<pre><code class="lang-auto">Collecting matplotlib
</code></pre>
<p>What is the specific meaning of these outputs? Does it have any impact on how the extension works?</p>
<p>Thank you in advance for your help, I appreciate it!</p>

---

## Post #2 by @lassoan (2023-03-26 04:07 UTC)

<p>The module is implemented incorrectly. It uses <code>pip_install</code> to install many Python packages in the global scope (when the module is loaded). Instead, packages should be installed as late as possible, i.e., when they are actually used.</p>
<p>Installation of the <code>skimage</code> package fails due to the recent rename, which prevents the package from loading.</p>
<p>Please send a pull request to the <a href="https://github.com/ChenXiang96/SlicerColoc-Z-Stats">extension’s repository</a> with the proposed fix. If you don’t get a response within 1-2 weeks then let us know and we’ll see what we can do.</p>

---

## Post #4 by @CharlesChen (2023-04-12 03:31 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<blockquote>
<p>It uses <code>pip_install</code> to install many Python packages in the global scope (when the module is loaded). Instead, packages should be installed as late as possible, i.e., when they are actually used.</p>
</blockquote>
<p>Thank you for your kind reminder. I’m the developer of the module, and I have made the necessary changes to it by relocating the installation of most Python packages from the global scope to where they are actually used.</p>
<p>And I have avoided the error I mentioned by simply removing the unnecessary code related with <code>skimage</code>, cause I think for now I don’t need it anymore.</p>
<p>However, could you please provide more details about the reseason for the <code>skimage</code> package installation failure you mentioned earlier? :</p>
<blockquote>
<p>Installation of the <code>skimage</code> package fails due to the recent rename, which prevents the package from loading.</p>
</blockquote>
<p>This would be helpful in case I need to use it in the future.<br>
Thank you very much for your assistance!</p>

---
