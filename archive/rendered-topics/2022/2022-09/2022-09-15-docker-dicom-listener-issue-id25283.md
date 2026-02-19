---
topic_id: 25283
title: "Docker Dicom Listener Issue"
date: 2022-09-15
url: https://discourse.slicer.org/t/25283
---

# Docker Dicom Listener issue

**Topic ID**: 25283
**Date**: 2022-09-15
**URL**: https://discourse.slicer.org/t/docker-dicom-listener-issue/25283

---

## Post #1 by @dSC (2022-09-15 19:38 UTC)

<p>Hello Guys,<br>
I’m trying to start storage listener in Slicer in the web (docker version)</p>
<p>this is the error.</p>
<p>Problem trying to start DICOM listener:<br>
[Errno 2] No such file or directory: ‘ps’</p>
<p>Any suggestion?</p>
<p>Best<br>
Daniele</p>

---

## Post #2 by @pieper (2022-09-15 20:48 UTC)

<p><code>ps</code> is the built in process list on linux that is used to tell if the listener is already running.  It should be available in the docker os layer.  You can investigate why it’s not available in your image or you can report back with more details about what image you are using and how you start it.</p>

---

## Post #3 by @dSC (2022-09-15 20:53 UTC)

<p>Thanks Steve for your reply.</p>
<p>I’m following repo instruction then:</p>
<pre><code>docker run -p 8888:8888 -p 49053:49053  -v "$PWD":/home/sliceruser/work  --rm -ti lassoan/slicer-notebook:latest
</code></pre>
<p>and this in jupyter</p>
<pre><code class="lang-python">import JupyterNotebooksLib as slicernb
import slicer
import ipywidgets
ipywidgets.HTML(f'&lt;h1&gt;&lt;center&gt;&lt;a href="{slicernb.AppWindow.defaultDesktopUrl()}" target="_blank"&gt;&lt;img src="https://www.slicer.org/assets/img/3D-Slicer-Mark.svg" width="100" height="100"/&gt;&lt;br&gt;Click here to open 3D Slicer in a new window&lt;/a&gt;&lt;/center&gt;&lt;/h1&gt;')
</code></pre>

---

## Post #4 by @pieper (2022-09-15 21:13 UTC)

<p>Ah, yes, the jupyter server may not be running on a normal OS and may not be able to run the dicom listener.</p>
<p>This is where it tries to run <code>ps</code>.  Maybe you need to find a different way to run external processes.</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/23744ee0e374928b76dc4c1209faa07377bee518/Modules/Scripted/DICOMLib/DICOMProcesses.py#L192-L200">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/23744ee0e374928b76dc4c1209faa07377bee518/Modules/Scripted/DICOMLib/DICOMProcesses.py#L192-L200" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/23744ee0e374928b76dc4c1209faa07377bee518/Modules/Scripted/DICOMLib/DICOMProcesses.py#L192-L200" target="_blank" rel="noopener">Slicer/Slicer/blob/23744ee0e374928b76dc4c1209faa07377bee518/Modules/Scripted/DICOMLib/DICOMProcesses.py#L192-L200</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="192" style="counter-reset: li-counter 191 ;">
          <li>def killStoreSCPProcessesPosix(self, uniqueListener):</li>
          <li>    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)</li>
          <li>    out, err = p.communicate()</li>
          <li>    for line in out.splitlines():</li>
          <li>        line = line.decode()</li>
          <li>        if self.STORESCP_PROCESS_FILE_NAME in line:</li>
          <li>            pid = int(line.split(None, 1)[0])</li>
          <li>            uniqueListener = self.notifyUserAboutRunningStoreSCP(pid)</li>
          <li>    return uniqueListener</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If you do get the listener running you will also need to map port 11112 if you want to communicate with it from your host machine.</p>

---

## Post #5 by @dSC (2022-09-15 21:44 UTC)

<p>Understood, thank you.</p>
<p>Do you have any web based alternative able to avoid this jupyter server issues?</p>

---

## Post #6 by @pieper (2022-09-16 14:34 UTC)

<p>The slicer-notebook is built on a regular linux as far as I can see.  I’m not sure why <code>ps</code> won’t run, maybe there’s some permission lockdown.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerDocker/blob/main/slicer-notebook/Dockerfile">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerDocker/blob/main/slicer-notebook/Dockerfile" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerDocker/blob/main/slicer-notebook/Dockerfile" target="_blank" rel="noopener">Slicer/SlicerDocker/blob/main/slicer-notebook/Dockerfile</a></h4>


      <pre><code class="lang-">FROM debian:bullseye-20200422-slim

################################################################################
# Prevent apt-get from prompting for keyboard choice
#  https://superuser.com/questions/1356914/how-to-install-xserver-xorg-in-unattended-mode
ENV DEBIAN_FRONTEND=noninteractive

################################################################################
# Remove documentation to save hard drive space
#  https://askubuntu.com/questions/129566/remove-documentation-to-save-hard-drive-space
COPY etc/dpkg/dpkg.cfg.d/01_nodoc /etc/dpkg/dpkg.cfg.d/01_nodoc

################################################################################
# - update apt, set up certs, run netselect to get fast mirror
# - reduce apt gravity
# - and disable caching
#   from https://blog.sleeplessbeastie.eu/2017/10/02/how-to-disable-the-apt-cache/
# Note: in each RUN command "apt-get update" must be called before apt-get is used.
RUN echo 'APT::Install-Recommends "0" ; APT::Install-Suggests "0" ;' &gt;&gt; /etc/apt/apt.conf &amp;&amp; \
    echo 'Dir::Cache::pkgcache "";\nDir::Cache::srcpkgcache "";' | tee /etc/apt/apt.conf.d/00_disable-cache-files
</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/SlicerDocker/blob/main/slicer-notebook/Dockerfile" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I have some other docker images that might work differently.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/pieper/SlicerDockers">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/pieper/SlicerDockers" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/23a9d1ef2057302379ea0c0d519a449ce8d7ef49dbe185be9b7119f376928be6/pieper/SlicerDockers" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/pieper/SlicerDockers" target="_blank" rel="noopener">GitHub - pieper/SlicerDockers: docker config files for slicer</a></h3>

  <p>docker config files for slicer. Contribute to pieper/SlicerDockers development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @lassoan (2022-09-16 18:21 UTC)

<p>The slice-notebook image uses a minimal linux installation. To get <code>ps</code>, we need to add <code>sudo  apt-get install procps</code> to the dockerfile. I’ve done this for 5.0.2, 5.0.3, and latest tags, and it seems to work well, the DICOM listener does complain.</p>

---

## Post #8 by @dSC (2022-09-17 15:27 UTC)

<p>This is great!<br>
Thanks a ton!</p>

---
