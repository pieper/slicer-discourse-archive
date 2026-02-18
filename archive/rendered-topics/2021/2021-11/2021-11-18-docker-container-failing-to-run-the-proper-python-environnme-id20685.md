# Docker Container - failing to run the proper Python Environnment

**Topic ID**: 20685
**Date**: 2021-11-18
**URL**: https://discourse.slicer.org/t/docker-container-failing-to-run-the-proper-python-environnment/20685

---

## Post #1 by @sebastien_goffart (2021-11-18 13:42 UTC)

<p>Good Morning,</p>
<p>I’m quite new to 3Dslicer and I’m trying to set up 3D slicer in a container so I can use python scripts in the Python environment of 3D Slicer. I follow then several guidelines and based myself on the <code>slicer/slicer-notebook</code> container.</p>
<p>Correct me if I’m wrong but the executable python version needed is <code>PythonSlicer</code> (link<a href="https://discourse.slicer.org/t/using-slicer-and-slicer-modules-from-command-line/8162">here</a> and from the documentation, python scripts can be run from the terminal CLI.</p>
<p>Here is the dockerfile used to build my image:</p>
<pre><code class="lang-auto"># Linux env
FROM debian:buster

RUN apt update -y &amp;&amp; apt upgrade -y
# RUN apt install -y \
#         libpulse-dev \
#         libglu1-mesa \
#         libxi-dev \
#         libxmu-dev \
#         libglu1-mesa-dev \
#         libnss3 \
#         libglu1-mesa \
#         libxcb-xinerama0 \
#         libxkbcommon0

# Download 3DSlicer build 
RUN apt install -y curl
# Current preview release (2021-10-15, rev30315)
ARG SLICER_DOWNLOAD_URL=https://download.slicer.org/bitstream/61690039342a877cb3d01245
RUN curl -JL "$SLICER_DOWNLOAD_URL" | tar xz -C /tmp &amp;&amp; mv /tmp/Slicer* Slicer

# latest version
# https://download.slicer.org/bitstream/60add706ae4540bf6a89bf98

# Installing dependancies required by 3DSlicer runtime
RUN apt install -y \
    libgl1-mesa-glx \
    libxrender1 \
    libpulse0 \
    libpulse-mainloop-glib0  \
    libnss3  \
    libxcomposite1 \
    libxcursor1 \
    libfontconfig1 \
    libxrandr2 \
    libasound2 \
    libglu1 \
    libxi-dev \
    libxcb-xinerama0 \
    libxmu-dev \
    libxkbcommon0

WORKDIR ${PWD}/Slicer

# copy utils files
COPY utils.py .
COPY tmp/masks.nii .

# RUN apt install -y libxrender1 libxcomposite-dev
CMD ["./Slicer","--launcher-verbose","--launcher-no-splash","--launch", "PythonSlicer", "utils.py"]

</code></pre>
<p>and here is the content of the utils.py file where I only try to load a segmentation:</p>
<pre><code class="lang-auto">import os
import sys

import slicer
import slicer.util

print("----Python version----")
print(sys.executable)

print("-----test library slicer----")
#Load a 3D image as segmentation
slicer.util.loadSegmentation("masks.nii")

</code></pre>
<p>Howerver, when I try to run the container I have several issue mainly due to the wrong python environnment:</p>
<ul>
<li>first the lunch python version is not <code>PythonSlicer</code> but <code>python-real</code>.</li>
<li>the <code>slicer.util</code> loading has a warning “No module named 'logic”.</li>
<li>the <code>slicer.util</code> library is loaded but impossible to access to the <code>app</code> file necessary for the <code>slicer.util.loadSegmentation()</code>
</li>
</ul>
<p>Here is the output:</p>
<pre><code class="lang-auto">No module named 'logic'
----Python version----
/Slicer/bin/./python-real
-----test library slicer----
Traceback (most recent call last):
  File "utils.py", line 13, in &lt;module&gt;
    slicer.util.loadSegmentation("masks.nii")
  File "/Slicer/bin/Python/slicer/util.py", line 798, in loadSegmentation
    return loadNodeFromFile(filename, 'SegmentationFile', {}, returnNode)
  File "/Slicer/bin/Python/slicer/util.py", line 631, in loadNodeFromFile
    from slicer import app
ImportError: cannot import name 'app'
</code></pre>
<p>I’m pretty sure it’s not a big issue? maybe some expert of the tool have some clues to help me to solve the problem. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Cheers,<br>
Sébastien</p>

---

## Post #2 by @lassoan (2021-11-18 13:55 UTC)

<aside class="quote no-group" data-username="sebastien_goffart" data-post="1" data-topic="20685">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sebastien_goffart/48/9722_2.png" class="avatar"> sebastien_goffart:</div>
<blockquote>
<p>first the lunch python version is not <code>PythonSlicer</code> but <code>python-real</code> .</p>
</blockquote>
</aside>
<p>This is correct. The executable is <code>python-real</code>. The <code>Slicer</code> or <code>PythonSlicer</code> launcher sets up the virtual Python environment and executes <code>python-real</code>.</p>
<aside class="quote no-group" data-username="sebastien_goffart" data-post="1" data-topic="20685">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sebastien_goffart/48/9722_2.png" class="avatar"> sebastien_goffart:</div>
<blockquote>
<ul>
<li>the <code>slicer.util</code> loading has a warning “No module named 'logic”.</li>
<li>the <code>slicer.util</code> library is loaded but impossible to access to the <code>app</code> file necessary for the <code>slicer.util.loadSegmentation()</code></li>
</ul>
</blockquote>
</aside>
<p><code>PythonSlicer</code> is a Python interpreter, which you can use to have access to basic Python features without installing a Python distribution. You can use this to install packages, use standard Python packages, and even some Slicer features that does not require a running Slicer <em>application</em>.</p>
<p>For most actual data processing you need Slicer modules, which are instantiated by the Slicer application. You can start the Slicer application, by specifying <code>SlicerApp-real</code> instead of <code>PythonSlicer</code> as <code>--launch</code> argument. Or you can simply remove <code>"--launch", "PythonSlicer", </code> to run the default executable, which is the Slicer application.</p>

---

## Post #3 by @sebastien_goffart (2021-11-19 07:42 UTC)

<p>Alright thanks for this precious information, it makes then perfectly sense to have <code>python-real</code> running.<br>
Since I need slicer features requiring the application to run, I will select the second option.<br>
Cheers,<br>
Sébastien</p>

---
