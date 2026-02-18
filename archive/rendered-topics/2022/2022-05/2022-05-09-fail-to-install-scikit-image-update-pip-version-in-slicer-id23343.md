# Fail to install `scikit-image` - update pip version in Slicer

**Topic ID**: 23343
**Date**: 2022-05-09
**URL**: https://discourse.slicer.org/t/fail-to-install-scikit-image-update-pip-version-in-slicer/23343

---

## Post #1 by @S_Arbabi (2022-05-09 12:52 UTC)

<p>I wanted to install scikit-image library using pip_install(“scikit-image”), when I got the warning:</p>
<pre><code class="lang-auto">WARNING: You are using pip version 21.1.2; however, version 21.3.1 is available.
You should consider upgrading via the 'C:\Users\saeed\AppData\Local\NA-MIC\Slicer 4.13.0-2021-09-07\bin\python-real.exe -m pip install --upgrade pip' command.
</code></pre>
<p>and then error:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\Users\saeed\AppData\Local\NA-MIC\Slicer 4.13.0-2021-09-07\bin\Python\slicer\util.py", line 2925, in pip_install
    _executePythonModule('pip', args)
  File "C:\Users\saeed\AppData\Local\NA-MIC\Slicer 4.13.0-2021-09-07\bin\Python\slicer\util.py", line 2900, in _executePythonModule
    logProcessOutput(proc)
  File "C:\Users\saeed\AppData\Local\NA-MIC\Slicer 4.13.0-2021-09-07\bin\Python\slicer\util.py", line 2869, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Users/saeed/AppData/Local/NA-MIC/Slicer 4.13.0-2021-09-07/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', '--upgrade']' returned non-zero exit status 1.
</code></pre>
<p>I was wondering how could I update pip in slicer, so I can install scikit-image?</p>

---

## Post #2 by @jamesobutler (2022-05-09 13:53 UTC)

<p>The update pip version is likely not the issue here, but an issue with the python package versions related to scikit-image. Slicer 4.13.0-2021-09-07 was using Python 3.6 which is no longer supported by the latest version of scikit-image and the latest versions of its dependencies. Slicer was updated to use Python 3.9 earlier this year so my recommendation is to download the most recent Slicer Preview version which uses Python 3.9. Shown below is my output installing scikit-image and it being successful.</p>
<pre><code class="lang-auto">Python 3.9.10 (main, May  8 2022, 23:28:56) [MSC v.1930 64 bit (AMD64)] on win32
&gt;&gt;&gt; pip_install("scikit-image")
Collecting scikit-image
  Using cached scikit_image-0.19.2-cp39-cp39-win_amd64.whl (12.6 MB)
Collecting tifffile&gt;=2019.7.26
  Downloading tifffile-2022.5.4-py3-none-any.whl (195 kB)
     -------------------------------------- 195.6/195.6 KB 2.9 MB/s eta 0:00:00
Requirement already satisfied: numpy&gt;=1.17.0 in c:\users\jamesbutler\appdata\local\na-mic\slicer 5.1.0-2022-05-08\lib\python\lib\site-packages (from scikit-image) (1.22.1)
Requirement already satisfied: scipy&gt;=1.4.1 in c:\users\jamesbutler\appdata\local\na-mic\slicer 5.1.0-2022-05-08\lib\python\lib\site-packages (from scikit-image) (1.8.0)
Collecting PyWavelets&gt;=1.1.1
  Using cached PyWavelets-1.3.0-cp39-cp39-win_amd64.whl (4.2 MB)
Collecting networkx&gt;=2.2
  Downloading networkx-2.8-py3-none-any.whl (2.0 MB)
     ---------------------------------------- 2.0/2.0 MB 15.9 MB/s eta 0:00:00
Requirement already satisfied: pillow!=7.1.0,!=7.1.1,!=8.3.0,&gt;=6.1.0 in c:\users\jamesbutler\appdata\local\na-mic\slicer 5.1.0-2022-05-08\lib\python\lib\site-packages (from scikit-image) (9.0.1)
Collecting imageio&gt;=2.4.1
  Downloading imageio-2.19.1-py3-none-any.whl (3.4 MB)
     ---------------------------------------- 3.4/3.4 MB 23.7 MB/s eta 0:00:00
Requirement already satisfied: packaging&gt;=20.0 in c:\users\jamesbutler\appdata\local\na-mic\slicer 5.1.0-2022-05-08\lib\python\lib\site-packages (from scikit-image) (21.3)
Requirement already satisfied: pyparsing!=3.0.5,&gt;=2.0.2 in c:\users\jamesbutler\appdata\local\na-mic\slicer 5.1.0-2022-05-08\lib\python\lib\site-packages (from packaging&gt;=20.0-&gt;scikit-image) (3.0.7)
Installing collected packages: tifffile, PyWavelets, networkx, imageio, scikit-image
  WARNING: The scripts lsm2bin.exe, tiff2fsspec.exe, tiffcomment.exe and tifffile.exe are installed in 'C:\Users\JamesButler\AppData\Local\NA-MIC\Slicer 5.1.0-2022-05-08\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts imageio_download_bin.exe and imageio_remove_bin.exe are installed in 'C:\Users\JamesButler\AppData\Local\NA-MIC\Slicer 5.1.0-2022-05-08\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script skivi.exe is installed in 'C:\Users\JamesButler\AppData\Local\NA-MIC\Slicer 5.1.0-2022-05-08\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed PyWavelets-1.3.0 imageio-2.19.1 networkx-2.8 scikit-image-0.19.2 tifffile-2022.5.4
WARNING: You are using pip version 22.0.3; however, version 22.0.4 is available.
You should consider upgrading via the 'C:\Users\JamesButler\AppData\Local\NA-MIC\Slicer 5.1.0-2022-05-08\bin\python-real.exe -m pip install --upgrade pip' command.
&gt;&gt;&gt; import skimage
&gt;&gt;&gt; skimage.__version__
'0.19.2'
</code></pre>

---

## Post #3 by @ruili (2024-02-03 00:28 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="23343">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>ear so my recommendation is to download the most recent Slicer Preview version which uses Python 3.9. Shown below is my output installing scikit-image and it being successful.</p>
</blockquote>
</aside>
<p>Hi! Thanks for the answer. I was wondering if you did anything regarding those warning about <code>C:\Users\JamesButler\AppData\Local\NA-MIC\Slicer 5.1.0-2022-05-08\lib\Python\Scripts</code> not in PATH?</p>

---
