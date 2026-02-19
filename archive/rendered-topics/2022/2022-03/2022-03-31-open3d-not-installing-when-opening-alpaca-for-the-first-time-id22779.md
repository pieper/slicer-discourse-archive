---
topic_id: 22779
title: "Open3D Not Installing When Opening Alpaca For The First Time"
date: 2022-03-31
url: https://discourse.slicer.org/t/22779
---

# open3D not installing when opening ALPACA for the first time

**Topic ID**: 22779
**Date**: 2022-03-31
**URL**: https://discourse.slicer.org/t/open3d-not-installing-when-opening-alpaca-for-the-first-time/22779

---

## Post #1 by @Erik.Meilak (2022-03-31 13:58 UTC)

<p>I have Slicer 4.11.20210226 on Windows 10. When trying to use ALPACA for the first time, the software attempts to upgrade open3d however never manages to. I am met with the following errors.</p>
<pre><code class="lang-auto">Requirement already satisfied: cpdalp in c:\users\meilake\appdata\local\na-mic\slicer 4.11.20210226\lib\python\lib\site-packages (1.2.0)
Requirement already satisfied: numpy in c:\users\meilake\appdata\local\na-mic\slicer 4.11.20210226\lib\python\lib\site-packages (from cpdalp) (1.19.2)
WARNING: You are using pip version 20.3.3; however, version 21.3.1 is available.
You should consider upgrading via the 'C:\Users\meilake\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\python-real.exe -m pip install --upgrade pip' command.
ERROR: open3d-0.14.1+816263b-cp39-cp39-win_amd64.whl is not a supported wheel on this platform.
WARNING: You are using pip version 20.3.3; however, version 21.3.1 is available.
You should consider upgrading via the 'C:\Users\meilake\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\python-real.exe -m pip install --upgrade pip' command.
Traceback (most recent call last):
  File "C:/Users/meilake/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerMorph/lib/Slicer-4.11/qt-scripted-modules/ALPACA.py", line 146, in __init__
    slicer.util.pip_install(wheelPath)
  File "C:\Users\meilake\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\Python\slicer\util.py", line 2876, in pip_install
    _executePythonModule('pip', args)
  File "C:\Users\meilake\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\Python\slicer\util.py", line 2851, in _executePythonModule
    logProcessOutput(proc)
  File "C:\Users\meilake\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\Python\slicer\util.py", line 2820, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Users/meilake/AppData/Local/NA-MIC/Slicer 4.11.20210226/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'C:/Users/meilake/AppData/Local/NA-MIC/Slicer/cache/SlicerIO/open3d-0.14.1+816263b-cp39-cp39-win_amd64.whl']' returned non-zero exit status 1.
</code></pre>
<p>When I try to apply the fixed posted on a related forum post:</p><aside class="quote quote-modified" data-post="1" data-topic="22512">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/khanine/48/14672_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/unable-to-download-open3d-library-for-alpaca/22512">Unable to download open3d library for ALPACA</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi all, 
I am trying to run some 3D morphometrics on ALPACA (a program within slicermorph) and every time I try to run it, it tells me “ALPACA requires open3d library. Installation will take a few minutes” then a whole installation sequence takes place in python. However, I keep running into this error and I am not sure how to remedy it. 
"ERROR: Command errored out with exit status 1: ‘C:\Users\blakk\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\python-real.exe’ ‘C:\Users\blakk\AppData\Local\NA…
  </blockquote>
</aside>

<p>Then I get further messages and the problem is not resolved:</p>
<pre><code class="lang-auto">Requirement already satisfied: pywinpty==1.1.6 in c:\users\meilake\appdata\local\na-mic\slicer 4.11.20210226\lib\python\lib\site-packages (1.1.6)

WARNING: You are using pip version 20.3.3; however, version 21.3.1 is available.

You should consider upgrading via the 'C:\Users\meilake\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\python-real.exe -m pip install --upgrade pip' command.
</code></pre>
<p>Any help you could give me would be much appreciated.</p>

---

## Post #2 by @jamesobutler (2022-03-31 14:38 UTC)

<aside class="quote no-group" data-username="Erik.Meilak" data-post="1" data-topic="22779">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/fbc32d/48.png" class="avatar"> Erik.Meilak:</div>
<blockquote>
<p>ERROR: open3d-0.14.1+816263b-cp39-cp39-win_amd64.whl</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/smrolfe">@smrolfe</a> <a class="mention" href="/u/muratmaga">@muratmaga</a> Are you all providing a Python 3.9 whl for Slicer 4.11.20210226 which is using Python 3.6?</p>

---

## Post #3 by @muratmaga (2022-03-31 15:56 UTC)

<p>It is a bit complicated.</p>
<p>There are a lot of complications with getting open3d working particularly on Linux and maintaining different python versions between stable and preview and meanwhile making ALPACA consistently run on all platforms (there is some sort of a bug in their ransac implementation in certain open3d releases in mac and linux). Given the release of 5.0 stable is imminent, we put our efforts in making the preview version working reliably.</p>
<p><a class="mention" href="/u/erik.meilak">@Erik.Meilak</a> If you have to use that version, please download a prepackaged Slicer installation with ALPACA and open3d installed and ready to go from here:</p>
<p><a href="https://app.box.com/shared/static/xziombnoti3jbrc8hqp236v95ghcz2c2.zip" class="onebox" target="_blank" rel="noopener nofollow ugc">https://app.box.com/shared/static/xziombnoti3jbrc8hqp236v95ghcz2c2.zip</a></p>
<p>Do not update SlicerMorph or any of the extensions, unzip and use them as is.</p>

---

## Post #4 by @smrolfe (2022-03-31 18:00 UTC)

<p>Although we may not continue supporting the Stable version, we have just pushed a fix to correct this issue.</p>
<p><a class="mention" href="/u/erik.meilak">@Erik.Meilak</a> this error can also be fixed manually by running the following lines in the Python interactor:</p>
<pre><code class="lang-auto">slicer.util.pip_install('pywinpty==1.1.6')
slicer.util.pip_install('notebook==6.0.3')
slicer.util.pip_install('open3d==0.10.0')
slicer.util.pip_install('cpdalp')
</code></pre>

---

## Post #5 by @Erik.Meilak (2022-04-01 12:32 UTC)

<p>Thank you all for your swift replies, I followed Sara’s instructions and it now works!</p>

---

## Post #6 by @lili-yu22 (2022-06-03 01:23 UTC)

<p>l have try all the methods in this topic，downlod the slicer5.1.0，but ALPACA can’t open，could you help me</p>

---

## Post #7 by @muratmaga (2022-06-03 04:07 UTC)

<p>Can you tell us your on what OS you are running, and what error message are you seeing if you expand the python console?</p>

---

## Post #8 by @muratmaga (2022-06-03 04:13 UTC)

<p>I just tried with the fresh install of the latest preview on windows (r30987). It takes about 1 minute for open3d to install on a new system, and then ALPACA is available:</p>
<pre><code class="lang-auto">Collecting cpdalp
  Using cached cpdalp-1.2.0-py3-none-any.whl (18 kB)
Requirement already satisfied: numpy in c:\users\murat\appdata\local\na-mic\slicer 5.1.0-2022-06-01\lib\python\lib\site-packages (from cpdalp) (1.22.1)
Installing collected packages: cpdalp
Successfully installed cpdalp-1.2.0
WARNING: You are using pip version 22.0.3; however, version 22.1.2 is available.
You should consider upgrading via the 'C:\Users\murat\AppData\Local\NA-MIC\Slicer 5.1.0-2022-06-01\bin\python-real.exe -m pip install --upgrade pip' command.
Processing c:\users\murat\desktop\open3d-0.14.1+816263b-cp39-cp39-win_amd64.whl
Collecting ipywidgets&gt;=7.6.0
  Using cached ipywidgets-7.7.0-py2.py3-none-any.whl (123 kB)
Collecting jupyter-packaging~=0.10
  Downloading jupyter_packaging-0.12.1-py3-none-any.whl (15 kB)
Collecting pygments&gt;=2.7.4
  Using cached Pygments-2.12.0-py3-none-any.whl (1.1 MB)
Requirement already satisfied: numpy&gt;=1.18.0 in c:\users\murat\appdata\local\na-mic\slicer 5.1.0-2022-06-01\lib\python\lib\site-packages (from open3d==0.14.1+816263b) (1.22.1)
Collecting jupyterlab==3.*,&gt;=3.0.0
  Using cached jupyterlab-3.4.2-py3-none-any.whl (8.8 MB)
Requirement already satisfied: setuptools&gt;=40.8.0 in c:\users\murat\appdata\local\na-mic\slicer 5.1.0-2022-06-01\lib\python\lib\site-packages (from open3d==0.14.1+816263b) (60.9.3)
Requirement already satisfied: wheel&gt;=0.36.0 in c:\users\murat\appdata\local\na-mic\slicer 5.1.0-2022-06-01\lib\python\lib\site-packages (from open3d==0.14.1+816263b) (0.37.1)
Collecting jupyter-server~=1.16
  Using cached jupyter_server-1.17.0-py3-none-any.whl (342 kB)
Requirement already satisfied: packaging in c:\users\murat\appdata\local\na-mic\slicer 5.1.0-2022-06-01\lib\python\lib\site-packages (from jupyterlab==3.*,&gt;=3.0.0-&gt;open3d==0.14.1+816263b) (21.3)
Collecting nbclassic~=0.2
  Using cached nbclassic-0.3.7-py3-none-any.whl (13 kB)
Collecting jupyterlab-server~=2.10
  Using cached jupyterlab_server-2.14.0-py3-none-any.whl (54 kB)
Collecting ipython
  Downloading ipython-8.4.0-py3-none-any.whl (750 kB)
     ------------------------------------- 750.8/750.8 KB 15.8 MB/s eta 0:00:00
Collecting tornado&gt;=6.1.0
  Using cached tornado-6.1-cp39-cp39-win_amd64.whl (422 kB)
Collecting jupyter-core
  Using cached jupyter_core-4.10.0-py3-none-any.whl (87 kB)
Collecting jinja2&gt;=2.1
  Using cached Jinja2-3.1.2-py3-none-any.whl (133 kB)
Collecting traitlets&gt;=4.3.1
  Downloading traitlets-5.2.2.post1-py3-none-any.whl (106 kB)
     -------------------------------------- 106.8/106.8 KB 6.0 MB/s eta 0:00:00
Collecting nbformat&gt;=4.2.0
  Using cached nbformat-5.4.0-py3-none-any.whl (73 kB)
Collecting ipykernel&gt;=4.5.1
  Using cached ipykernel-6.13.0-py3-none-any.whl (131 kB)
Collecting ipython-genutils~=0.2.0
  Using cached ipython_genutils-0.2.0-py2.py3-none-any.whl (26 kB)
Collecting jupyterlab-widgets&gt;=1.0.0
  Using cached jupyterlab_widgets-1.1.0-py3-none-any.whl (245 kB)
Collecting widgetsnbextension~=3.6.0
  Using cached widgetsnbextension-3.6.0-py2.py3-none-any.whl (1.6 MB)
Collecting deprecation
  Using cached deprecation-2.1.0-py2.py3-none-any.whl (11 kB)
Collecting tomlkit
  Downloading tomlkit-0.11.0-py3-none-any.whl (34 kB)
Collecting jupyter-client&gt;=6.1.12
  Using cached jupyter_client-7.3.1-py3-none-any.whl (130 kB)
Collecting debugpy&gt;=1.0
  Using cached debugpy-1.6.0-cp39-cp39-win_amd64.whl (4.3 MB)
Collecting psutil
  Downloading psutil-5.9.1-cp39-cp39-win_amd64.whl (245 kB)
     ------------------------------------- 245.9/245.9 KB 14.7 MB/s eta 0:00:00
Collecting matplotlib-inline&gt;=0.1
  Using cached matplotlib_inline-0.1.3-py3-none-any.whl (8.2 kB)
Collecting nest-asyncio
  Using cached nest_asyncio-1.5.5-py3-none-any.whl (5.2 kB)
Collecting pickleshare
  Using cached pickleshare-0.7.5-py2.py3-none-any.whl (6.9 kB)
Collecting decorator
  Using cached decorator-5.1.1-py3-none-any.whl (9.1 kB)
Collecting prompt-toolkit!=3.0.0,!=3.0.1,&lt;3.1.0,&gt;=2.0.0
  Using cached prompt_toolkit-3.0.29-py3-none-any.whl (381 kB)
Collecting backcall
  Using cached backcall-0.2.0-py2.py3-none-any.whl (11 kB)
Collecting stack-data
  Using cached stack_data-0.2.0-py3-none-any.whl (21 kB)
Collecting colorama
  Using cached colorama-0.4.4-py2.py3-none-any.whl (16 kB)
Collecting jedi&gt;=0.16
  Using cached jedi-0.18.1-py2.py3-none-any.whl (1.6 MB)
Collecting MarkupSafe&gt;=2.0
  Using cached MarkupSafe-2.1.1-cp39-cp39-win_amd64.whl (17 kB)
Collecting pyzmq&gt;=17
  Downloading pyzmq-23.1.0-cp39-cp39-win_amd64.whl (991 kB)
     ------------------------------------- 992.0/992.0 KB 31.7 MB/s eta 0:00:00
Collecting Send2Trash
  Using cached Send2Trash-1.8.0-py3-none-any.whl (18 kB)
Collecting anyio&lt;4,&gt;=3.1.0
  Using cached anyio-3.6.1-py3-none-any.whl (80 kB)
Collecting argon2-cffi
  Using cached argon2_cffi-21.3.0-py3-none-any.whl (14 kB)
Collecting terminado&gt;=0.8.3
  Using cached terminado-0.15.0-py3-none-any.whl (16 kB)
Collecting websocket-client
  Using cached websocket_client-1.3.2-py3-none-any.whl (54 kB)
Collecting pywinpty
  Using cached pywinpty-2.0.5-cp39-none-win_amd64.whl (1.4 MB)
Collecting nbconvert&gt;=6.4.4
  Using cached nbconvert-6.5.0-py3-none-any.whl (561 kB)
Collecting prometheus-client
  Using cached prometheus_client-0.14.1-py3-none-any.whl (59 kB)
Collecting pywin32&gt;=1.0
  Using cached pywin32-304-cp39-cp39-win_amd64.whl (12.2 MB)
Collecting importlib-metadata&gt;=3.6
  Downloading importlib_metadata-4.11.4-py3-none-any.whl (18 kB)
Collecting babel
  Using cached Babel-2.10.1-py3-none-any.whl (9.5 MB)
Collecting jsonschema&gt;=3.0.1
  Downloading jsonschema-4.6.0-py3-none-any.whl (80 kB)
     ---------------------------------------- 80.4/80.4 KB ? eta 0:00:00
Collecting json5
  Using cached json5-0.9.8-py2.py3-none-any.whl
Requirement already satisfied: requests in c:\users\murat\appdata\local\na-mic\slicer 5.1.0-2022-06-01\lib\python\lib\site-packages (from jupyterlab-server~=2.10-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d==0.14.1+816263b) (2.27.1)
Collecting notebook&lt;7
  Using cached notebook-6.4.11-py3-none-any.whl (9.9 MB)
Collecting notebook-shim&gt;=0.1.0
  Using cached notebook_shim-0.1.0-py3-none-any.whl (13 kB)
Collecting fastjsonschema
  Using cached fastjsonschema-2.15.3-py3-none-any.whl (22 kB)
Requirement already satisfied: pyparsing!=3.0.5,&gt;=2.0.2 in c:\users\murat\appdata\local\na-mic\slicer 5.1.0-2022-06-01\lib\python\lib\site-packages (from packaging-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d==0.14.1+816263b) (3.0.7)
Requirement already satisfied: idna&gt;=2.8 in c:\users\murat\appdata\local\na-mic\slicer 5.1.0-2022-06-01\lib\python\lib\site-packages (from anyio&lt;4,&gt;=3.1.0-&gt;jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d==0.14.1+816263b) (3.3)
Collecting sniffio&gt;=1.1
  Using cached sniffio-1.2.0-py3-none-any.whl (10 kB)
Collecting zipp&gt;=0.5
  Using cached zipp-3.8.0-py3-none-any.whl (5.4 kB)
Collecting parso&lt;0.9.0,&gt;=0.8.0
  Using cached parso-0.8.3-py2.py3-none-any.whl (100 kB)
Collecting attrs&gt;=17.4.0
  Using cached attrs-21.4.0-py2.py3-none-any.whl (60 kB)
Collecting pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,&gt;=0.14.0
  Using cached pyrsistent-0.18.1-cp39-cp39-win_amd64.whl (61 kB)
Requirement already satisfied: python-dateutil&gt;=2.8.2 in c:\users\murat\appdata\local\na-mic\slicer 5.1.0-2022-06-01\lib\python\lib\site-packages (from jupyter-client&gt;=6.1.12-&gt;ipykernel&gt;=4.5.1-&gt;ipywidgets&gt;=7.6.0-&gt;open3d==0.14.1+816263b) (2.8.2)
Collecting entrypoints
  Using cached entrypoints-0.4-py3-none-any.whl (5.3 kB)
Collecting bleach
  Using cached bleach-5.0.0-py3-none-any.whl (160 kB)
Collecting tinycss2
  Using cached tinycss2-1.1.1-py3-none-any.whl (21 kB)
Collecting beautifulsoup4
  Using cached beautifulsoup4-4.11.1-py3-none-any.whl (128 kB)
Collecting defusedxml
  Using cached defusedxml-0.7.1-py2.py3-none-any.whl (25 kB)
Collecting mistune&lt;2,&gt;=0.8.1
  Using cached mistune-0.8.4-py2.py3-none-any.whl (16 kB)
Collecting nbclient&gt;=0.5.0
  Downloading nbclient-0.6.4-py3-none-any.whl (71 kB)
     ---------------------------------------- 71.8/71.8 KB ? eta 0:00:00
Collecting jupyterlab-pygments
  Using cached jupyterlab_pygments-0.2.2-py2.py3-none-any.whl (21 kB)
Collecting pandocfilters&gt;=1.4.1
  Using cached pandocfilters-1.5.0-py2.py3-none-any.whl (8.7 kB)
Collecting wcwidth
  Using cached wcwidth-0.2.5-py2.py3-none-any.whl (30 kB)
Collecting argon2-cffi-bindings
  Using cached argon2_cffi_bindings-21.2.0-cp36-abi3-win_amd64.whl (30 kB)
Requirement already satisfied: pytz&gt;=2015.7 in c:\users\murat\appdata\local\na-mic\slicer 5.1.0-2022-06-01\lib\python\lib\site-packages (from babel-&gt;jupyterlab-server~=2.10-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d==0.14.1+816263b) (2022.1)
Requirement already satisfied: certifi&gt;=2017.4.17 in c:\users\murat\appdata\local\na-mic\slicer 5.1.0-2022-06-01\lib\python\lib\site-packages (from requests-&gt;jupyterlab-server~=2.10-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d==0.14.1+816263b) (2021.10.8)
Requirement already satisfied: urllib3&lt;1.27,&gt;=1.21.1 in c:\users\murat\appdata\local\na-mic\slicer 5.1.0-2022-06-01\lib\python\lib\site-packages (from requests-&gt;jupyterlab-server~=2.10-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d==0.14.1+816263b) (1.26.8)
Requirement already satisfied: charset-normalizer~=2.0.0 in c:\users\murat\appdata\local\na-mic\slicer 5.1.0-2022-06-01\lib\python\lib\site-packages (from requests-&gt;jupyterlab-server~=2.10-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d==0.14.1+816263b) (2.0.12)
Collecting pure-eval
  Using cached pure_eval-0.2.2-py3-none-any.whl (11 kB)
Collecting executing
  Using cached executing-0.8.3-py2.py3-none-any.whl (16 kB)
Collecting asttokens
  Using cached asttokens-2.0.5-py2.py3-none-any.whl (20 kB)
Requirement already satisfied: six&gt;=1.5 in c:\users\murat\appdata\local\na-mic\slicer 5.1.0-2022-06-01\lib\python\lib\site-packages (from python-dateutil&gt;=2.8.2-&gt;jupyter-client&gt;=6.1.12-&gt;ipykernel&gt;=4.5.1-&gt;ipywidgets&gt;=7.6.0-&gt;open3d==0.14.1+816263b) (1.16.0)
Requirement already satisfied: cffi&gt;=1.0.1 in c:\users\murat\appdata\local\na-mic\slicer 5.1.0-2022-06-01\lib\python\lib\site-packages (from argon2-cffi-bindings-&gt;argon2-cffi-&gt;jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d==0.14.1+816263b) (1.15.0)
Collecting soupsieve&gt;1.2
  Using cached soupsieve-2.3.2.post1-py3-none-any.whl (37 kB)
Collecting webencodings
  Using cached webencodings-0.5.1-py2.py3-none-any.whl (11 kB)
Requirement already satisfied: pycparser in c:\users\murat\appdata\local\na-mic\slicer 5.1.0-2022-06-01\lib\python\lib\site-packages (from cffi&gt;=1.0.1-&gt;argon2-cffi-bindings-&gt;argon2-cffi-&gt;jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d==0.14.1+816263b) (2.21)
Installing collected packages: webencodings, wcwidth, Send2Trash, pywin32, pure-eval, pickleshare, mistune, json5, ipython-genutils, fastjsonschema, executing, backcall, zipp, websocket-client, traitlets, tornado, tomlkit, tinycss2, soupsieve, sniffio, pyzmq, pywinpty, pyrsistent, pygments, psutil, prompt-toolkit, prometheus-client, parso, pandocfilters, nest-asyncio, MarkupSafe, jupyterlab-widgets, jupyterlab-pygments, entrypoints, defusedxml, decorator, debugpy, colorama, bleach, babel, attrs, asttokens, terminado, stack-data, matplotlib-inline, jupyter-core, jsonschema, jinja2, jedi, importlib-metadata, deprecation, beautifulsoup4, argon2-cffi-bindings, anyio, nbformat, jupyter-packaging, jupyter-client, ipython, argon2-cffi, nbclient, ipykernel, nbconvert, notebook, jupyter-server, widgetsnbextension, notebook-shim, jupyterlab-server, nbclassic, ipywidgets, jupyterlab, open3d
  WARNING: The script send2trash.exe is installed in 'C:\Users\murat\AppData\Local\NA-MIC\Slicer 5.1.0-2022-06-01\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script pyjson5.exe is installed in 'C:\Users\murat\AppData\Local\NA-MIC\Slicer 5.1.0-2022-06-01\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script wsdump.exe is installed in 'C:\Users\murat\AppData\Local\NA-MIC\Slicer 5.1.0-2022-06-01\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script pygmentize.exe is installed in 'C:\Users\murat\AppData\Local\NA-MIC\Slicer 5.1.0-2022-06-01\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script pybabel.exe is installed in 'C:\Users\murat\AppData\Local\NA-MIC\Slicer 5.1.0-2022-06-01\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts jupyter-migrate.exe, jupyter-troubleshoot.exe and jupyter.exe are installed in 'C:\Users\murat\AppData\Local\NA-MIC\Slicer 5.1.0-2022-06-01\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script jsonschema.exe is installed in 'C:\Users\murat\AppData\Local\NA-MIC\Slicer 5.1.0-2022-06-01\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script jupyter-trust.exe is installed in 'C:\Users\murat\AppData\Local\NA-MIC\Slicer 5.1.0-2022-06-01\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts jupyter-kernel.exe, jupyter-kernelspec.exe and jupyter-run.exe are installed in 'C:\Users\murat\AppData\Local\NA-MIC\Slicer 5.1.0-2022-06-01\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts ipython.exe and ipython3.exe are installed in 'C:\Users\murat\AppData\Local\NA-MIC\Slicer 5.1.0-2022-06-01\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script jupyter-execute.exe is installed in 'C:\Users\murat\AppData\Local\NA-MIC\Slicer 5.1.0-2022-06-01\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts jupyter-dejavu.exe and jupyter-nbconvert.exe are installed in 'C:\Users\murat\AppData\Local\NA-MIC\Slicer 5.1.0-2022-06-01\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts jupyter-bundlerextension.exe, jupyter-nbextension.exe, jupyter-notebook.exe and jupyter-serverextension.exe are installed in 'C:\Users\murat\AppData\Local\NA-MIC\Slicer 5.1.0-2022-06-01\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script jupyter-server.exe is installed in 'C:\Users\murat\AppData\Local\NA-MIC\Slicer 5.1.0-2022-06-01\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script jupyter-nbclassic.exe is installed in 'C:\Users\murat\AppData\Local\NA-MIC\Slicer 5.1.0-2022-06-01\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts jlpm.exe, jupyter-lab.exe, jupyter-labextension.exe and jupyter-labhub.exe are installed in 'C:\Users\murat\AppData\Local\NA-MIC\Slicer 5.1.0-2022-06-01\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script open3d.exe is installed in 'C:\Users\murat\AppData\Local\NA-MIC\Slicer 5.1.0-2022-06-01\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed MarkupSafe-2.1.1 Send2Trash-1.8.0 anyio-3.6.1 argon2-cffi-21.3.0 argon2-cffi-bindings-21.2.0 asttokens-2.0.5 attrs-21.4.0 babel-2.10.1 backcall-0.2.0 beautifulsoup4-4.11.1 bleach-5.0.0 colorama-0.4.4 debugpy-1.6.0 decorator-5.1.1 defusedxml-0.7.1 deprecation-2.1.0 entrypoints-0.4 executing-0.8.3 fastjsonschema-2.15.3 importlib-metadata-4.11.4 ipykernel-6.13.0 ipython-8.4.0 ipython-genutils-0.2.0 ipywidgets-7.7.0 jedi-0.18.1 jinja2-3.1.2 json5-0.9.8 jsonschema-4.6.0 jupyter-client-7.3.1 jupyter-core-4.10.0 jupyter-packaging-0.12.1 jupyter-server-1.17.0 jupyterlab-3.4.2 jupyterlab-pygments-0.2.2 jupyterlab-server-2.14.0 jupyterlab-widgets-1.1.0 matplotlib-inline-0.1.3 mistune-0.8.4 nbclassic-0.3.7 nbclient-0.6.4 nbconvert-6.5.0 nbformat-5.4.0 nest-asyncio-1.5.5 notebook-6.4.11 notebook-shim-0.1.0 open3d-0.14.1+816263b pandocfilters-1.5.0 parso-0.8.3 pickleshare-0.7.5 prometheus-client-0.14.1 prompt-toolkit-3.0.29 psutil-5.9.1 pure-eval-0.2.2 pygments-2.12.0 pyrsistent-0.18.1 pywin32-304 pywinpty-2.0.5 pyzmq-23.1.0 sniffio-1.2.0 soupsieve-2.3.2.post1 stack-data-0.2.0 terminado-0.15.0 tinycss2-1.1.1 tomlkit-0.11.0 tornado-6.1 traitlets-5.2.2.post1 wcwidth-0.2.5 webencodings-0.5.1 websocket-client-1.3.2 widgetsnbextension-3.6.0 zipp-3.8.0
WARNING: You are using pip version 22.0.3; however, version 22.1.2 is available.
You should consider upgrading via the 'C:\Users\murat\AppData\Local\NA-MIC\Slicer 5.1.0-2022-06-01\bin\python-real.exe -m pip install --upgrade pip' command.
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f7b7548a88674900a4fe395e3eaa38584aa3fb4.png" data-download-href="/uploads/short-url/2cXFx6jCVMGpHXXaIoD6Pi8UWLG.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f7b7548a88674900a4fe395e3eaa38584aa3fb4.png" alt="image" data-base62-sha1="2cXFx6jCVMGpHXXaIoD6Pi8UWLG" width="462" height="500" data-dominant-color="F4F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">590×638 19.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lili-yu22 (2022-06-03 05:40 UTC)

<p>thank you for your reply. i use windows system.<br>
python interactor show as picture<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba73c0f705f869a6d265d40aa35651165cd27f6a.jpeg" data-download-href="/uploads/short-url/qBqOgKPl1FaJLzGyEXi8XvbXXbs.jpeg?dl=1" title="IMG_20220603_133748_edit_71696661899476" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba73c0f705f869a6d265d40aa35651165cd27f6a_2_690x479.jpeg" alt="IMG_20220603_133748_edit_71696661899476" data-base62-sha1="qBqOgKPl1FaJLzGyEXi8XvbXXbs" width="690" height="479" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba73c0f705f869a6d265d40aa35651165cd27f6a_2_690x479.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba73c0f705f869a6d265d40aa35651165cd27f6a_2_1035x718.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba73c0f705f869a6d265d40aa35651165cd27f6a_2_1380x958.jpeg 2x" data-dominant-color="9FA1B4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20220603_133748_edit_71696661899476</span><span class="informations">3034×2110 1.47 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @muratmaga (2022-06-03 05:55 UTC)

<p>It appears that you cannot download the open3d wheel for some reason. Not clearly why.</p>
<p>What happens if you type this address to a web browser, can you download the file?<br>
<a href="https://app.box.com/shared/static/friq8fhfi8n4syklt1v47rmuf58zro75.whl" class="onebox" target="_blank" rel="noopener nofollow ugc">https://app.box.com/shared/static/friq8fhfi8n4syklt1v47rmuf58zro75.whl</a></p>
<p>If it does download, open Slicer, go to Python interactor and try:<br>
<code>pip_install("/your/download/path/to/open3d-0.14.1+816263b-cp39-cp39-win_amd64.whl")</code><br>
and replace <strong>/your/download/path/to/</strong> with the actual path of this wheel on your computer.</p>

---

## Post #11 by @lili-yu22 (2022-06-03 06:40 UTC)

<p>l can download，ihave try，python show as the picture<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45cd20fc2168e1902ea42d08649db19b1981be5a.jpeg" data-download-href="/uploads/short-url/9XuqMz84crnn2PjgSURxA6gUHjk.jpeg?dl=1" title="IMG_20220603_142236_edit_74387109378232" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45cd20fc2168e1902ea42d08649db19b1981be5a_2_690x212.jpeg" alt="IMG_20220603_142236_edit_74387109378232" data-base62-sha1="9XuqMz84crnn2PjgSURxA6gUHjk" width="690" height="212" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45cd20fc2168e1902ea42d08649db19b1981be5a_2_690x212.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45cd20fc2168e1902ea42d08649db19b1981be5a_2_1035x318.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45cd20fc2168e1902ea42d08649db19b1981be5a_2_1380x424.jpeg 2x" data-dominant-color="BDBAB5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20220603_142236_edit_74387109378232</span><span class="informations">3120×963 1.09 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @muratmaga (2022-06-03 14:32 UTC)

<p>You have typo in your path take out the first / before D and re-try</p>

---

## Post #13 by @lili-yu22 (2022-06-03 15:15 UTC)

<p>when l removed / the same result，but i noticed “requirement D：/anzhuang/open3d…amd64.whl looks like a filename,but the file does not exist”i wound whether the command malformed</p>

---

## Post #14 by @muratmaga (2022-06-03 16:06 UTC)

<p>Can you find the locate the wheel file in the windows explorer? It is not clear to me if the wheel is not correctly or it is being downloaded to path that pip cannot find…</p>
<p>M</p>

---

## Post #15 by @jcfr (2022-06-04 04:48 UTC)

<p>Consider executing the following snippet and updating the value associated the variable <code>wheel_filepath</code> until it does not fail with the  <code>Invalid path</code> assertion.</p>
<pre><code class="lang-python">import os

wheel_filepath = "D:/your/download/path/to/open3d-0.14.1+816263b-cp39-cp39-win_amd64.whl"
assert os.path.exists(wheel_filepath), "Invalid path"
</code></pre>
<p>once it succeeds, you should be able to run:</p>
<pre><code class="lang-python">pip_install(wheel_filepath)
</code></pre>

---

## Post #18 by @lili-yu22 (2022-06-04 08:43 UTC)

<p>i made it ，i am grateful for your help</p>

---

## Post #19 by @jcfr (2022-06-04 08:47 UTC)

<p>Glad you were able to sort out the problem <img src="https://emoji.discourse-cdn.com/twitter/100.png?v=12" title=":100:" class="emoji" alt=":100:" loading="lazy" width="20" height="20"></p>
<p>So that what you discovered is helpful to others, could you share your findings ? What was the root cause of the problems ?</p>

---

## Post #20 by @lili-yu22 (2022-06-04 09:12 UTC)

<p>i followed your process，i found it first removed the open3d-0. 15（i don’t know why and when it download）and then i close and reopen，i found success</p>

---
