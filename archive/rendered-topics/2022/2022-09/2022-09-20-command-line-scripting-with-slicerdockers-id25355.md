---
topic_id: 25355
title: "Command Line Scripting With Slicerdockers"
date: 2022-09-20
url: https://discourse.slicer.org/t/25355
---

# Command line scripting with SlicerDockers

**Topic ID**: 25355
**Date**: 2022-09-20
**URL**: https://discourse.slicer.org/t/command-line-scripting-with-slicerdockers/25355

---

## Post #1 by @NaglisR (2022-09-20 11:54 UTC)

<p>Hi all,</p>
<p>A question regarding executing command line scripts while using SlicerDockers:</p>
<ul>
<li>I am using <a href="https://github.com/pieper/SlicerDockers" class="inline-onebox" rel="noopener nofollow ugc">GitHub - pieper/SlicerDockers: docker config files for slicer</a>, everything works succesfully, I am able to access Slicer interface via the hosted vnc client.</li>
<li>If possible I would like to send command line requests to the running slicer instance, similar to <code>Slicer.exe --python-code "slicer.util.loadScene('f:/2013-08-23-Scene.mrb')"</code> or <code>Slicer.exe --python-code "doSomething; doSomethingElse; etc." --testing --no-splash --no-main-window</code>
</li>
<li>Ultimately I am trying to figure out a way to create a way to open a slicer window from a custom web application, by creating a button which would execute a command, which opens a locally stored nifti file with the running slicer instance (and visible in the vnc window). I know that this exists - <a href="https://discourse.slicer.org/t/new-dicomweb-features-launch-slicer-from-web-browser-and-download-upload-data-sets-to-the-cloud-using-dicomweb/17811" class="inline-onebox">New DICOMweb features: launch Slicer from web browser and download/upload data sets to the cloud using DICOMweb</a> but in my case, all the files can be stored in the local storage, no communication with external DICOMWeb databases is necessary.</li>
</ul>
<p>Is it possible with SlicerDockers? Or is there a better way to achieve similar functionality?</p>
<p>Thank you in advance.</p>

---

## Post #2 by @pieper (2022-09-20 20:19 UTC)

<p>Yes, you can send commands to a running Slicer with the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html">WebServer</a> module and the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html#slicer-endpoints">slicer/exec</a> endpoint.  You can use the <code>--python-code</code> command line option to make sure the WebServer is running at startup.  The <code>exec</code> endpoint allows you to execute arbitrary python code and get the results via http (of course be careful who has access to this endpoint!).  You would also need to expose the port from your docker run command, 2016 by default.  If you have shared the volume with the files to the docker instance then you can load the files using the passed in commands and have them show up in your vnc window.</p>

---

## Post #3 by @NaglisR (2022-09-21 13:52 UTC)

<p>Thank you for your answer!<br>
I not yet sure how can I launch the WebServer using <a href="https://github.com/pieper/SlicerDockers" class="inline-onebox" rel="noopener nofollow ugc">GitHub - pieper/SlicerDockers: docker config files for slicer</a> .<br>
WebServer module does not seem to be available in the Slicer instance hosted in the vnc. Is there a way to enable it either after start or when starting the docker container/inside the docker container?</p>

---

## Post #4 by @NaglisR (2022-09-21 14:39 UTC)

<p>I managed to add the WebServer module using <a href="https://github.com/pieper/SlicerWeb" class="inline-onebox" rel="noopener nofollow ugc">GitHub - pieper/SlicerWeb: Slicer modules that support web services and web applications</a> and adding the <code>--env SLICER_ARGUMENTS="--additional-module-paths /home/researcher/Documents/SlicerWeb/WebServer"</code> argument to the docker run command. However this way does seem to be limited in functionality, as I can only open the <a href="http://localhost:2016/" rel="noopener nofollow ugc">http://localhost:2016/</a> (by exposing the port) but exec commands does not seem to be available (returns <code>unknown command "/exec"</code>) probably because I do not see the option to start server in the Web Server module started in this way.</p>

---

## Post #5 by @lassoan (2022-09-21 15:09 UTC)

<p>Slicer-5.0.3 has the Web Server module built in, so there is no need to set up anything else. You can start Slicer (with the exec interface enabled) from the command line like this:</p>
<pre><code>"%localappdata%\NA-MIC\Slicer 5.0.3\Slicer.exe" --python-code "wslogic=getModuleLogic('WebServer'); wslogic.addDefaultRequestHandlers(enableExec=True); wslogic.start()"
</code></pre>

---

## Post #6 by @NaglisR (2022-09-21 15:16 UTC)

<p>Right, but for my usecase, I need the Slicer to be running in a docker container and accessible via vnc client, so I am using <a href="https://github.com/pieper/SlicerDockers" class="inline-onebox" rel="noopener nofollow ugc">GitHub - pieper/SlicerDockers: docker config files for slicer</a> . However, SlicerDockers seems to run the Slicer version 5.0.2 version, so thats probably why the Web Server module in not available in the launched Slicer instance. Maybe I can try to manually rebuild the docker with Slicer version 5.0.3 or are there are better alternatives?</p>

---

## Post #7 by @lassoan (2022-09-21 15:20 UTC)

<p>The web server in 5.0.3 is refactored and improved, so I would recommend it over the experimental version that was developed in a separate extension.</p>
<p>All you need to do is to <a href="https://github.com/pieper/SlicerDockers/blob/master/build.sh#L4">change the version to 5.0.3</a> and rebuild the image. Maybe <a class="mention" href="/u/pieper">@pieper</a> could do it and upload the new image to dockerhub.</p>

---

## Post #8 by @NaglisR (2022-09-21 15:23 UTC)

<p>That would certainly be excellent <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"> Otherwise, I will try to rebuild the image on my end, thanks</p>

---

## Post #9 by @pieper (2022-09-21 15:42 UTC)

<p><a class="mention" href="/u/naglisr">@NaglisR</a> did you run <code>stevepieper/slicer:5.0.2</code> ?  that should have the WebServer option built in.  I haven’t had a chance to update to 5.0.3 yet but 5.0.2 should work the same mostly.  Let us know how it goes.</p>

---

## Post #10 by @NaglisR (2022-09-21 17:22 UTC)

<p>It seems to me that 5.0.2 does not yet have the inbuilt Web Server module, checked that by downloading <a href="https://download.slicer.org/bitstream/6286ce04e8408647b39f803a" rel="noopener nofollow ugc">https://download.slicer.org/bitstream/6286ce04e8408647b39f803a</a> .<br>
I am trying to rebuild the SlicerDockers image after changing the version <a href="https://github.com/pieper/SlicerDockers/blob/master/build.sh#L4" class="inline-onebox" rel="noopener nofollow ugc">SlicerDockers/build.sh at master · pieper/SlicerDockers · GitHub</a> and the download link <a href="https://github.com/pieper/SlicerDockers/blob/5949f71fab141740ba0da7c03af3825cc9b91798/slicer/Dockerfile#L22" class="inline-onebox" rel="noopener nofollow ugc">SlicerDockers/Dockerfile at 5949f71fab141740ba0da7c03af3825cc9b91798 · pieper/SlicerDockers · GitHub</a><br>
However, I am not yet able to rebuilt the image, as it seems some minor adjustments have to be made elsewhere (probably names of some atributes have to be updated?).</p>
<pre><code class="lang-auto">Step 7/7 : RUN for ext in ${SLICER_EXTS} ; do echo "Installing ${ext}" ;   EXTENSION_TO_INSTALL=${ext}     su researcher -c "xvfb-run --auto-servernum       /opt/slicer/Slicer --python-script /tmp/install-slicer-extension.py" ; done
 ---&gt; Running in 975b22429285
Installing MarkupsToModel
QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-researcher'
Switch to module:  "Welcome"
installing MarkupsToModel
Traceback (most recent call last):
  File "&lt;string&gt;", line 5, in &lt;module&gt;
  File "&lt;string&gt;", line 7, in &lt;module&gt;
AttributeError: qSlicerExtensionsManagerModel has no attribute named 'retrieveExtensionMetadataByName'
</code></pre>

---

## Post #11 by @pieper (2022-09-21 20:59 UTC)

<p>Thanks testing this - I was mistaken, the 5.0.2 version didn’t have the WebServer module as you discovered.  I’m looking into updating the images to include a 5.0.3 version.  I’ll report back if I get one uploaded.  We should be able to fix the extensions (slicer-plus image) but the base slicer image wouldn’t need the extension manager so you can probably run that even if the build script doesn’t complete.</p>
<p>If you want to experiment without fixing the docker, you can also just copy the WebServer code directly from the Slicer source code into the module path of the 5.0.2 instance.  There’s no compilation needed and I don’t think there’s even any configuration done during the cmake process, just copying the files.</p>

---

## Post #12 by @pieper (2022-09-21 21:04 UTC)

<p>It turned out to be <a href="https://github.com/pieper/SlicerDockers/commit/d0facca5d43d5ce7c9a5e77babf61a9f9e2cb8ce">easy enough</a> to update the base image, so now this should work to run 5.0.3 with the WebServer pre-installed.</p>
<p><code>docker run -d -p 8080:8080 --name slicer stevepieper/slicer:5.0.3</code></p>

---

## Post #13 by @NaglisR (2022-09-22 05:09 UTC)

<p>Yes, pulled the stevepieper/slicer:5.0.3, everything seems to be working now, thank you!</p>

---

## Post #14 by @pieper (2022-09-22 11:29 UTC)

<p>Great!  Your use case with a custom web app and containerized Slicer access sounds pretty interesting.  If you can share your app source code, or just a small demo script, that would be good for others to learn from.</p>

---

## Post #15 by @lassoan (2022-09-22 16:56 UTC)

<aside class="quote no-group" data-username="pieper" data-post="11" data-topic="25355">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>We should be able to fix the extensions (slicer-plus image) but the base slicer image wouldn’t need the extension manager so you can probably run that even if the build script doesn’t complete</p>
</blockquote>
</aside>
<p>FYI, here is an extension install code snippet that is compatible with all Slicer versions (including the latest Slicer-5.0.3):</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerDocker/blob/10a8f38f6086f8d97a2a9cf81446974da2053001/slicer-notebook/install.sh#L41-L76">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerDocker/blob/10a8f38f6086f8d97a2a9cf81446974da2053001/slicer-notebook/install.sh#L41-L76" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerDocker/blob/10a8f38f6086f8d97a2a9cf81446974da2053001/slicer-notebook/install.sh#L41-L76" target="_blank" rel="noopener">Slicer/SlicerDocker/blob/10a8f38f6086f8d97a2a9cf81446974da2053001/slicer-notebook/install.sh#L41-L76</a></h4>



    <pre class="onebox"><code class="lang-sh">
      <ol class="start lines" start="41" style="counter-reset: li-counter 40 ;">
          <li>$slicer_executable -c '</li>
          <li>em = slicer.app.extensionsManagerModel()</li>
          <li>extensionName = "SlicerJupyter"</li>
          <li>if int(slicer.app.revision) &gt;= 30893:</li>
          <li>    # Slicer-5.0.3 or later</li>
          <li>    em.updateExtensionsMetadataFromServer(True, True)</li>
          <li>    if not em.downloadAndInstallExtensionByName(extensionName, True):</li>
          <li>        raise ValueError(f"Failed to install {extensionName} extension")</li>
          <li>    # Wait for installation to complete</li>
          <li>    # (in Slicer-5.4 downloadAndInstallExtensionByName has a waitForComplete flag</li>
          <li>    # so that could be enabled instead of running this wait loop)</li>
          <li>    import time</li>
          <li>    while not em.isExtensionInstalled(extensionName):</li>
          <li>        slicer.app.processEvents()</li>
          <li>        time.sleep(0.1)</li>
          <li>else:</li>
          <li>    # Older than Slicer-5.0.3</li>
          <li>    extensionMetaData = em.retrieveExtensionMetadataByName(extensionName)</li>
          <li>    # Prevent showing popups for installing dependencies</li>
          <li>    # (this is not needed right now for SlicerJupyter, but we still add this line here</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/SlicerDocker/blob/10a8f38f6086f8d97a2a9cf81446974da2053001/slicer-notebook/install.sh#L41-L76" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>In Slicer-5.1 and later the installation got simpler, see in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#download-and-install-extension">script repository</a>.</p>

---

## Post #16 by @NaglisR (2023-08-16 08:34 UTC)

<p>Dear <a class="mention" href="/u/pieper">@pieper</a> would it be possible to ask you to do the same (rebuild the SlicerDockers image in dockerhub) to the newest stable release 5.2.2?</p>

---

## Post #17 by @pieper (2023-08-16 15:14 UTC)

<p>I haven’t had a chance to work on those in a while.  If you could make a PR with the update I could have a look.</p>

---
