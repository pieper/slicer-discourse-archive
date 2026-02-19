---
topic_id: 25307
title: "Cant Upgrade Open3D"
date: 2022-09-16
url: https://discourse.slicer.org/t/25307
---

# Can't upgrade open3d

**Topic ID**: 25307
**Date**: 2022-09-16
**URL**: https://discourse.slicer.org/t/cant-upgrade-open3d/25307

---

## Post #1 by @b_pei (2022-09-16 13:44 UTC)

<p>Hi,<br>
When I first load ALPACA, it failed to upgrade and it hit “Error: please check the url of the open3d wheel in the script” .<br>
I have tried the version 5.0.3 and 5.1.0.  My computer system is windows 11.<br>
I have searched in the forum and find a similar situation(<a href="https://discourse.slicer.org/t/cant-load-open3d/12950" class="inline-onebox">Can't load open3d</a>) and tried<br>
type <code>pip_install("open3d")</code> into your python console and paste log.<br>
After the pip install, type<code> import open3d</code> into your console, and paste the error message (if there is one).<br>
it showed<br>
Python 3.9.10 (main, Jul 8 2022, 02:32:50) [MSC v.1930 64 bit (AMD64)] on win32</p>
<blockquote>
<blockquote>
<blockquote>
<p>pip_install(“open3d”)</p>
</blockquote>
</blockquote>
</blockquote>
<p>Collecting open3d</p>
<p>Using cached open3d-0.15.1-cp39-cp39-win_amd64.whl (117.0 MB)</p>
<p>Requirement already satisfied: jupyter-packaging~=0.10 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from open3d) (0.12.3)</p>
<p>Requirement already satisfied: wheel&gt;=0.36.0 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from open3d) (0.37.1)</p>
<p>Requirement already satisfied: setuptools&gt;=40.8.0 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from open3d) (60.9.3)</p>
<p>Requirement already satisfied: ipywidgets&gt;=7.6.0 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from open3d) (8.0.2)</p>
<p>Requirement already satisfied: numpy&gt;=1.18.0 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from open3d) (1.22.1)</p>
<p>Requirement already satisfied: jupyterlab==3.*,&gt;=3.0.0 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from open3d) (3.4.7)</p>
<p>Requirement already satisfied: pygments&gt;=2.7.4 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from open3d) (2.13.0)</p>
<p>Requirement already satisfied: notebook&lt;7 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (6.4.12)</p>
<p>Requirement already satisfied: tornado&gt;=6.1.0 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (6.2)</p>
<p>Requirement already satisfied: jupyter-core in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (4.11.1)</p>
<p>Requirement already satisfied: ipython in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (8.5.0)</p>
<p>Requirement already satisfied: packaging in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (21.3)</p>
<p>Requirement already satisfied: jupyterlab-server~=2.10 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (2.15.1)</p>
<p>Requirement already satisfied: nbclassic in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (0.4.3)</p>
<p>Requirement already satisfied: tomli in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (2.0.1)</p>
<p>Requirement already satisfied: jupyter-server~=1.16 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (1.18.1)</p>
<p>Requirement already satisfied: jinja2&gt;=2.1 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (3.1.2)</p>
<p>Requirement already satisfied: jupyterlab-widgets~=3.0 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from ipywidgets&gt;=7.6.0-&gt;open3d) (3.0.3)</p>
<p>Requirement already satisfied: ipykernel&gt;=4.5.1 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from ipywidgets&gt;=7.6.0-&gt;open3d) (6.15.3)</p>
<p>Requirement already satisfied: widgetsnbextension~=4.0 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from ipywidgets&gt;=7.6.0-&gt;open3d) (4.0.3)</p>
<p>Requirement already satisfied: traitlets&gt;=4.3.1 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from ipywidgets&gt;=7.6.0-&gt;open3d) (5.4.0)</p>
<p>Requirement already satisfied: tomlkit in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyter-packaging~=0.10-&gt;open3d) (0.11.4)</p>
<p>Requirement already satisfied: deprecation in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyter-packaging~=0.10-&gt;open3d) (2.1.0)</p>
<p>Requirement already satisfied: jupyter-client&gt;=6.1.12 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from ipykernel&gt;=4.5.1-&gt;ipywidgets&gt;=7.6.0-&gt;open3d) (7.3.5)</p>
<p>Requirement already satisfied: debugpy&gt;=1.0 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from ipykernel&gt;=4.5.1-&gt;ipywidgets&gt;=7.6.0-&gt;open3d) (1.6.3)</p>
<p>Requirement already satisfied: matplotlib-inline&gt;=0.1 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from ipykernel&gt;=4.5.1-&gt;ipywidgets&gt;=7.6.0-&gt;open3d) (0.1.6)</p>
<p>Requirement already satisfied: nest-asyncio in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from ipykernel&gt;=4.5.1-&gt;ipywidgets&gt;=7.6.0-&gt;open3d) (1.5.5)</p>
<p>Requirement already satisfied: psutil in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from ipykernel&gt;=4.5.1-&gt;ipywidgets&gt;=7.6.0-&gt;open3d) (5.9.2)</p>
<p>Requirement already satisfied: pyzmq&gt;=17 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from ipykernel&gt;=4.5.1-&gt;ipywidgets&gt;=7.6.0-&gt;open3d) (24.0.0)</p>
<p>Requirement already satisfied: jedi&gt;=0.16 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from ipython-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (0.18.1)</p>
<p>Requirement already satisfied: stack-data in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from ipython-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (0.5.0)</p>
<p>Requirement already satisfied: prompt-toolkit&lt;3.1.0,&gt;3.0.1 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from ipython-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (3.0.31)</p>
<p>Requirement already satisfied: pickleshare in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from ipython-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (0.7.5)</p>
<p>Requirement already satisfied: backcall in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from ipython-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (0.2.0)</p>
<p>Requirement already satisfied: colorama in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from ipython-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (0.4.5)</p>
<p>Requirement already satisfied: decorator in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from ipython-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (5.1.1)</p>
<p>Requirement already satisfied: MarkupSafe&gt;=2.0 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jinja2&gt;=2.1-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (2.1.1)</p>
<p>Requirement already satisfied: anyio&lt;4,&gt;=3.1.0 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (3.6.1)</p>
<p>Requirement already satisfied: websocket-client in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (1.4.1)</p>
<p>Requirement already satisfied: Send2Trash in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (1.8.0)</p>
<p>Requirement already satisfied: nbformat&gt;=5.2.0 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (5.5.0)</p>
<p>Requirement already satisfied: argon2-cffi in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (21.3.0)</p>
<p>Requirement already satisfied: terminado&gt;=0.8.3 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (0.15.0)</p>
<p>Requirement already satisfied: nbconvert&gt;=6.4.4 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (7.0.0)</p>
<p>Requirement already satisfied: prometheus-client in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (0.14.1)</p>
<p>Requirement already satisfied: pywinpty in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (2.0.8)</p>
<p>Requirement already satisfied: pywin32&gt;=1.0 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyter-core-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (304)</p>
<p>Requirement already satisfied: requests in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyterlab-server~=2.10-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (2.27.1)</p>
<p>Requirement already satisfied: babel in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyterlab-server~=2.10-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (2.10.3)</p>
<p>Requirement already satisfied: json5 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyterlab-server~=2.10-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (0.9.10)</p>
<p>Requirement already satisfied: importlib-metadata&gt;=3.6 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyterlab-server~=2.10-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (4.12.0)</p>
<p>Requirement already satisfied: jsonschema&gt;=3.0.1 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyterlab-server~=2.10-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (4.16.0)</p>
<p>Requirement already satisfied: ipython-genutils in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from notebook&lt;7-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (0.2.0)</p>
<p>Requirement already satisfied: notebook-shim&gt;=0.1.0 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from nbclassic-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (0.1.0)</p>
<p>Requirement already satisfied: pyparsing!=3.0.5,&gt;=2.0.2 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from packaging-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (3.0.7)</p>
<p>Requirement already satisfied: sniffio&gt;=1.1 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from anyio&lt;4,&gt;=3.1.0-&gt;jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (1.3.0)</p>
<p>Requirement already satisfied: idna&gt;=2.8 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from anyio&lt;4,&gt;=3.1.0-&gt;jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (3.3)</p>
<p>Requirement already satisfied: zipp&gt;=0.5 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from importlib-metadata&gt;=3.6-&gt;jupyterlab-server~=2.10-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (3.8.1)</p>
<p>Requirement already satisfied: parso&lt;0.9.0,&gt;=0.8.0 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jedi&gt;=0.16-&gt;ipython-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (0.8.3)</p>
<p>Requirement already satisfied: attrs&gt;=17.4.0 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jsonschema&gt;=3.0.1-&gt;jupyterlab-server~=2.10-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (22.1.0)</p>
<p>Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,&gt;=0.14.0 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jsonschema&gt;=3.0.1-&gt;jupyterlab-server~=2.10-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (0.18.1)</p>
<p>Requirement already satisfied: entrypoints in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyter-client&gt;=6.1.12-&gt;ipykernel&gt;=4.5.1-&gt;ipywidgets&gt;=7.6.0-&gt;open3d) (0.4)</p>
<p>Requirement already satisfied: python-dateutil&gt;=2.8.2 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from jupyter-client&gt;=6.1.12-&gt;ipykernel&gt;=4.5.1-&gt;ipywidgets&gt;=7.6.0-&gt;open3d) (2.8.2)</p>
<p>Requirement already satisfied: nbclient&gt;=0.5.0 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from nbconvert&gt;=6.4.4-&gt;jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (0.6.8)</p>
<p>Requirement already satisfied: pandocfilters&gt;=1.4.1 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from nbconvert&gt;=6.4.4-&gt;jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (1.5.0)</p>
<p>Requirement already satisfied: mistune&lt;3,&gt;=2.0.3 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from nbconvert&gt;=6.4.4-&gt;jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (2.0.4)</p>
<p>Requirement already satisfied: bleach in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from nbconvert&gt;=6.4.4-&gt;jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (5.0.1)</p>
<p>Requirement already satisfied: tinycss2 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from nbconvert&gt;=6.4.4-&gt;jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (1.1.1)</p>
<p>Requirement already satisfied: defusedxml in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from nbconvert&gt;=6.4.4-&gt;jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (0.7.1)</p>
<p>Requirement already satisfied: jupyterlab-pygments in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from nbconvert&gt;=6.4.4-&gt;jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (0.2.2)</p>
<p>Requirement already satisfied: lxml in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from nbconvert&gt;=6.4.4-&gt;jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (4.9.1)</p>
<p>Requirement already satisfied: beautifulsoup4 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from nbconvert&gt;=6.4.4-&gt;jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (4.11.1)</p>
<p>Requirement already satisfied: fastjsonschema in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from nbformat&gt;=5.2.0-&gt;jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (2.16.1)</p>
<p>Requirement already satisfied: wcwidth in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from prompt-toolkit&lt;3.1.0,&gt;3.0.1-&gt;ipython-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (0.2.5)</p>
<p>Requirement already satisfied: argon2-cffi-bindings in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from argon2-cffi-&gt;jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (21.2.0)</p>
<p>Requirement already satisfied: pytz&gt;=2015.7 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from babel-&gt;jupyterlab-server~=2.10-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (2022.2.1)</p>
<p>Requirement already satisfied: charset-normalizer~=2.0.0 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from requests-&gt;jupyterlab-server~=2.10-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (2.0.12)</p>
<p>Requirement already satisfied: certifi&gt;=2017.4.17 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from requests-&gt;jupyterlab-server~=2.10-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (2021.10.8)</p>
<p>Requirement already satisfied: urllib3&lt;1.27,&gt;=1.21.1 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from requests-&gt;jupyterlab-server~=2.10-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (1.26.8)</p>
<p>Requirement already satisfied: asttokens in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from stack-data-&gt;ipython-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (2.0.8)</p>
<p>Requirement already satisfied: executing in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from stack-data-&gt;ipython-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (1.0.0)</p>
<p>Requirement already satisfied: pure-eval in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from stack-data-&gt;ipython-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (0.2.2)</p>
<p>Requirement already satisfied: six&gt;=1.5 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from python-dateutil&gt;=2.8.2-&gt;jupyter-client&gt;=6.1.12-&gt;ipykernel&gt;=4.5.1-&gt;ipywidgets&gt;=7.6.0-&gt;open3d) (1.16.0)</p>
<p>Requirement already satisfied: cffi&gt;=1.0.1 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from argon2-cffi-bindings-&gt;argon2-cffi-&gt;jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (1.15.0)</p>
<p>Requirement already satisfied: soupsieve&gt;1.2 in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from beautifulsoup4-&gt;nbconvert&gt;=6.4.4-&gt;jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (2.3.2.post1)</p>
<p>Requirement already satisfied: webencodings in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from bleach-&gt;nbconvert&gt;=6.4.4-&gt;jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (0.5.1)</p>
<p>Requirement already satisfied: pycparser in d:\3d\slicer 5.0.3\lib\python\lib\site-packages (from cffi&gt;=1.0.1-&gt;argon2-cffi-bindings-&gt;argon2-cffi-&gt;jupyter-server~=1.16-&gt;jupyterlab==3.*,&gt;=3.0.0-&gt;open3d) (2.21)</p>
<p>Installing collected packages: open3d</p>
<p>WARNING: The script open3d.exe is installed in ‘D:\3D\Slicer 5.0.3\lib\Python\Scripts’ which is not on PATH.</p>
<p>Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.</p>
<p>Successfully installed open3d-0.15.1</p>
<p>WARNING: You are using pip version 22.0.3; however, version 22.2.2 is available.</p>
<p>You should consider upgrading via the ‘D:\3D\Slicer 5.0.3\bin\python-real.exe -m pip install --upgrade pip’ command.</p>
<blockquote>
<blockquote>
<blockquote>
<p>import open3d<br>
I was wondering what would I do next.</p>
</blockquote>
</blockquote>
</blockquote>
<p>Thanks.</p>

---

## Post #2 by @muratmaga (2022-09-16 17:29 UTC)

<aside class="quote no-group" data-username="b_pei" data-post="1" data-topic="25307">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/b_pei/48/16682_2.png" class="avatar"> b_pei:</div>
<blockquote>
<p>When I first load ALPACA, it failed to upgrade and it hit “Error: please check the url of the open3d wheel in the script” .</p>
</blockquote>
</aside>
<p>We are now using a specific version of open3d that’s compatible with ALPACA and Slicer, and manually doing pip_install(“open3d”) will not help you.</p>
<p>The error suggests there was a problem reaching out to the URL link to download the wheel. Are you behind a firewall? What operating system are you trying this one? Can you get to these URL on that computer?</p>
<p>windows: <a href="https://app.box.com/shared/static/friq8fhfi8n4syklt1v47rmuf58zro75.whl">https://app.box.com/shared/static/friq8fhfi8n4syklt1v47rmuf58zro75.whl</a><br>
Mac: <a href="https://app.box.com/shared/static/ixhac95jrx7xdxtlagwgns7vt9b3mbqu.whl">https://app.box.com/shared/static/ixhac95jrx7xdxtlagwgns7vt9b3mbqu.whl</a><br>
Linux <a href="https://app.box.com/shared/static/wyzk0f9jhefrbm4uukzym0sow5bf26yi.whl">https://app.box.com/shared/static/wyzk0f9jhefrbm4uukzym0sow5bf26yi.whl</a></p>

---

## Post #4 by @b_pei (2022-09-17 02:20 UTC)

<p>Thanks for your reply！<br>
There might be a firewall, and I usually use Virtual Private Network to browse the web. I have tried Windos 11 and mac os(12.5.1) . I can get the URL both on windos and mac. Whether the downloaded .whl file should be put in a specific folder?</p>
<p>Thanks</p>

---

## Post #5 by @muratmaga (2022-09-17 04:39 UTC)

<p>So you can download wheels from the URL, but the ALPACA open3d install fails? Or did you download the wheels from a computer other than the one that open3d install fail?</p>
<p>Anyways, if you rename the wheels appropriately you can do<br>
<code>pip_install("path_to_correct_wheel")</code></p>
<p>For windows rename the wheel to <strong>open3d-0.14.1+816263b-cp39-cp39-win_amd64.whl</strong><br>
For mac rename it to <strong>open3d-0.14.1+816263b-cp39-cp39-macosx_10_15_x86_64.whl</strong></p>

---

## Post #6 by @chschaefe (2023-03-06 22:38 UTC)

<p>Hi everyone,</p>
<p>I have a student working with me who is getting this error when attempting this solution. He is on Mac and has Slicer 5.2.2.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6bca7a488a8647fc8c6f61a7eac4b8e4b63f304.png" data-download-href="/uploads/short-url/q4z5CY8CEQRCgCo92pbHsE2kifq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6bca7a488a8647fc8c6f61a7eac4b8e4b63f304_2_690x373.png" alt="image" data-base62-sha1="q4z5CY8CEQRCgCo92pbHsE2kifq" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6bca7a488a8647fc8c6f61a7eac4b8e4b63f304_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6bca7a488a8647fc8c6f61a7eac4b8e4b63f304_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6bca7a488a8647fc8c6f61a7eac4b8e4b63f304.png 2x" data-dominant-color="3B3636"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1280×692 364 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @muratmaga (2023-03-06 23:58 UTC)

<p>Is this generated by the ALPACA module of the SlicerMorph extension when installing, or are you trying to install open3d on your own? it is not clear where the error is generated from. Normally you would use the extension manager to install SlicerMorph, and when you switch to ALPACA the first time, it should download and install packages for you automatically (barring any network issues).</p>
<p>In any event, I think they key is the “Certificate Verify Failed” message. Are you behind a firewall or a corporate network? They can interfere with package installs. Is it possible for you to try this on a more open network and see if it resolves?</p>

---
