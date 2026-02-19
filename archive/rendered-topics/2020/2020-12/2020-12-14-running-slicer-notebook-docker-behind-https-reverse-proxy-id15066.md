---
topic_id: 15066
title: "Running Slicer Notebook Docker Behind Https Reverse Proxy"
date: 2020-12-14
url: https://discourse.slicer.org/t/15066
---

# Running slicer-notebook Docker behind HTTPS reverse proxy?

**Topic ID**: 15066
**Date**: 2020-12-14
**URL**: https://discourse.slicer.org/t/running-slicer-notebook-docker-behind-https-reverse-proxy/15066

---

## Post #1 by @Nadya_Shusharina (2020-12-14 23:59 UTC)

<p>Operating system: CentOS 7<br>
Slicer version: 4.11 ( <a href="https://github.com/Slicer/SlicerDocker" rel="noopener nofollow ugc">https://github.com/Slicer/SlicerDocker</a>  - lassoan/slicer-notebook:2020-05-15-89b6bb5 )<br>
I would like to run the container behind an Apache 2.4 as reverse proxy, so I could access the Slicer Jupyter notebook and in-browser Slicer GUI externally, at e.g. <a href="https://example.com/slicer" rel="noopener nofollow ugc">https://example.com/slicer</a> while all other URLs from <a href="http://example.com" rel="noopener nofollow ugc">example.com</a> are served by Apache directly.</p>

---

## Post #2 by @lassoan (2020-12-17 06:33 UTC)

<blockquote>
<p>I have tried the slicer-notebook docker container, and it is a really cool way of integrating both the Slicer GUI and its Jupyter notebook in the same web browser. It works great on my local computer, and I am trying to use on a web server as a prototype for interactive visualizations. To do that, I am running the docker container on the same machine as the web server, and I need to set up reverse proxy so that the container output at port 8888 is served externally at port 443 (https). My server is running Apache 2.4, fully configured, running a Joomla based website. Thus, I need to reverse-proxy the container to <a href="https://example.com/myslicer">https://example.com/myslicer</a></p>
<p>I am following <a href="https://can01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F23890386%2Fhow-to-run-ipython-behind-an-apache-proxy&amp;data=04%7C01%7Classo%40queensu.ca%7Cd966ce4dd78d41b7ea0708d8a2472612%7Cd61ecb3b38b142d582c4efb2838b925c%7C1%7C0%7C637437773763351373%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C2000&amp;sdata=SKYsXw7lSGYoqoGMLX%2BTdZNba%2FfCM2fOboRLEr8A6%2Bs%3D&amp;reserved=0">https://stackoverflow.com/questions/23890386/how-to-run-ipython-behind-an-apache-proxy</a><br>
and it appears that for reverse proxy to work, the container would have to expose the notebook not at 127.0.0.1:8888/ but 127.0.0.1:8888/myslicer</p>
<p>I was wondering if you could help me reconfigure the container to make this change?</p>
</blockquote>
<p>Sorry for the slow answer, we are all very busy at the Slicer Project Week. I would love to see this working.</p>
<p>Instead of trying to set all this up manually, have you considered to use <a href="https://jupyterhub.readthedocs.io/en/stable/reference/technical-overview.html">JupyterHub</a>? This is what binder uses and it supports multiple users, providing a dedicated server to each of them.</p>
<p>If you want to expose a single Jupyter server then it may be a matter of configuring the apache server to direct the <a href="http://example.com/slicer">example.com/slicer</a> traffic to the Jupyter server and set the Jupyter server base url in the Jupyter configuration file (as it is explained <a href="https://jupyter-notebook.readthedocs.io/en/stable/public_server.html#running-the-notebook-with-a-customized-url-prefix">here</a>). To set Jupyter configuration file in the image, you can upload it to the <a href="https://github.com/Slicer/SlicerDocker/tree/master/slicer-notebook">dockerfile folder</a> and add a copy command into the <a href="https://github.com/Slicer/SlicerDocker/blob/master/slicer-notebook/Dockerfile">Dockerfile</a> to put it to a place where Jupyter will find it (see info <a href="https://jupyter-notebook.readthedocs.io/en/stable/config.html">here</a> on how to generate a default configuration and where should it be).</p>

---

## Post #3 by @Nadya_Shusharina (2020-12-18 03:40 UTC)

<p>Thank you - I am building it for a single user. I have created  jupyter_notebook_config.py, added it to the Dockerfile and I rebuilt the container. The reverse proxy works as I can start a Python3 Jupyter notebook at <a href="https://example.com/myslicer" rel="noopener nofollow ugc">https://example.com/myslicer</a><br>
Here is my reverse proxy configuration for Apache 2.4 just in case:</p>
<pre><code class="lang-auto">&lt;Location /myslicer&gt;
ProxyPass  http://localhost:8888/myslicer
ProxyPassReverse http://localhost:8888/myslicer
ProxyPassReverseCookieDomain localhost example.com
RequestHeader set Origin "http://localhost:8888"
&lt;/Location&gt;
&lt;Location "/myslicer/api/kernels"&gt;
        ProxyPass ws://localhost:8888/myslicer/api/kernels
        ProxyPassReverse ws://localhost:8888/myslicer/api/kernels
&lt;/Location&gt;
</code></pre>
<p>However, the Slicer 4.11 notebook would not start:</p>
<pre><code class="lang-auto">error: [/home/sliceruser/Slicer-4.11.0-2020-05-14-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.
[I 03:20:11.378 NotebookApp] KernelRestarter: restarting kernel (1/5), keep random ports
</code></pre>
<p>Further, when building the container, the following errors occur:</p>
<pre><code class="lang-auto">Step 35/46 : RUN ./install.sh ${HOME}/$SLICER_ARCHIVE/Slicer
 ---&gt; Running in ac94ada5b72e
_XSERVTransmkdir: ERROR: euid != 0,directory /tmp/.X11-unix will not be created.
QIODevice::read (QFile, "/home/sliceruser/.config/NA-MIC/Extensions-29057/SlicerJupyter/share/Slicer-4.11/qt-loadable-modules/JupyterKernel/Slicer-4.11/kernel-template.json"): device not open
virtual bool qSlicerJupyterKernelModule::installSlicerKernel(QString) : launching  "/usr/local/bin//jupyter-kernelspec"   "install /home/sliceruser/.config/NA-MIC/Extensions-29057/SlicerJupyter/share/Slicer-4.11/qt-loadable-modules/JupyterKernel/Slicer-4.11 --replace --user"
Kernelspec install error output:  "[InstallKernelSpec] Installed kernelspec slicer-4.11 in /home/sliceruser/.local/share/jupyter/kernels/slicer-4.11\n"
</code></pre>
<p>I was wondering if something is no longer compatible. I had to comment out COPY etc/dpkg…01_nodoc in the Dockerfile to be able to build the container.</p>

---

## Post #4 by @lassoan (2020-12-18 03:52 UTC)

<p>Can you build the image using the original, unmodified dockerfile?</p>

---

## Post #5 by @Nadya_Shusharina (2020-12-18 14:28 UTC)

<p>No. Same errors _XSERVTransmkdir, QIODevice… Kernelspec as above when building using unmodified Dockerfile</p>

---

## Post #6 by @lassoan (2020-12-22 14:59 UTC)

<p>I’ve checked and both errors that you see are harmless: I have those as well and the image works fine.</p>
<p>You can open a new terminal with the New button and check if you can find any clue in the system logs about why Slicer startup fails.</p>
<p>What CPU and graphics do you have in your system?</p>

---

## Post #7 by @Nadya_Shusharina (2020-12-22 22:04 UTC)

<p>It is a CentOS7 headless VM sharing a Xeon E7-4830, with 4GB RAM, no GPU.</p>
<p>For a test, I have tried connecting the prebuilt container lassoan/slicer-notebook:2020-05-15-89b6bb5 to <a href="https://example.com/" rel="noopener nofollow ugc">https://example.com/</a> directly. Just as before, I can start python 3.8 notebooks but not slicer notebook, as before:</p>
<pre><code class="lang-auto">[I 21:34:48.458 NotebookApp] Kernel started: c58312d4-31a6-4a7b-90e3-695e37eb2cb8, name: slicer-4.11
Switch to module:  "Welcome"
Loading Slicer RC file [/home/sliceruser/.slicerrc.py]
Jupyter connection file: [/home/sliceruser/.local/share/jupyter/runtime/kernel-c58312d4-31a6-4a7b-90e3-695e37eb2cb8.json]
[W 21:35:48.846 NotebookApp] Timeout waiting for kernel_info reply from c58312d4-31a6-4a7b-90e3-695e37eb2cb8
error: [/home/sliceruser/Slicer-4.11.0-2020-05-14-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.
[I 21:35:54.450 NotebookApp] KernelRestarter: restarting kernel (1/5), keep random ports
</code></pre>
<p>Can this be a low RAM issue?</p>

---

## Post #8 by @lassoan (2020-12-23 01:23 UTC)

<p>4GB RAM is low and 4th generation Intel CPU is very old. You can open a new terminal using New button in the Jupyter GUI to inspect the system logs and see what fails. See for example <a href="https://discourse.slicer.org/t/slicer-and-jupyter-kernel-dies-repeatedly-problem-with-connection/14965/18">this similar topic</a> (failure to start Slicer on a 3rd generation Intel CPU).</p>
<p>You can also try to just simply install Slicer on that computer and see if it starts.</p>
<p>I’ve also updated and tested a <a href="https://github.com/Slicer/SlicerDocker/tree/master/slicer-notebook">notebook image</a> and tested that it works well.</p>
<p>Maybe you could make Slicer work by building it on your system instead of installing the pre-built package.</p>

---
