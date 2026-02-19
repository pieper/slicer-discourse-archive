---
topic_id: 13925
title: "Installing Extension Inside A Dockerfile"
date: 2020-10-07
url: https://discourse.slicer.org/t/13925
---

# Installing extension inside a Dockerfile

**Topic ID**: 13925
**Date**: 2020-10-07
**URL**: https://discourse.slicer.org/t/installing-extension-inside-a-dockerfile/13925

---

## Post #1 by @muratmaga (2020-10-07 17:17 UTC)

<p>I am trying to build a Dockerfile where I can install the extensions. I am following the instructions in <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#How_to_manually_install_an_extension_package.3F" rel="noopener nofollow ugc">here</a></p>
<p>As I understand, that requires knowing what folders exist in the lib/Slicer-4.11/ for every extension beforehand and adding those paths one by one to Slicer --additional-module-paths to enable them.</p>
<p>We have a number of extensions to install. Is there a more compact way doing this?</p>

---

## Post #2 by @pieper (2020-10-07 18:11 UTC)

<p>It’s possible to set up a custom .ini file with all the paths listed.  Or you can copy all the files into a common lib directory and specify that on the command line.</p>

---

## Post #3 by @lassoan (2020-10-07 18:16 UTC)

<p>Another option is to let the extension manager install the extension, as it is done in SlicerJupyter docker image:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/SlicerDocker/blob/c13632a1061371937f73acf9d42c605850f7b3bb/slicer-notebook/Dockerfile#L130-L140" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerDocker/blob/c13632a1061371937f73acf9d42c605850f7b3bb/slicer-notebook/Dockerfile#L130-L140" target="_blank" rel="noopener">Slicer/SlicerDocker/blob/c13632a1061371937f73acf9d42c605850f7b3bb/slicer-notebook/Dockerfile#L130-L140</a></h4>
<pre class="onebox"><code class="lang-"><ol class="start lines" start="130" style="counter-reset: li-counter 129 ;">
<li>ARG SLICER_JUPYTER_ARCHIVE=29057-linux-amd64-SlicerJupyter-git6993275-2020-05-14.tar.gz</li>
<li>ARG SLICER_JUPYTER_DOWNLOAD_URL=http://slicer.kitware.com/midas3/api/rest?method=midas.bitstream.download&amp;name=29057-linux-amd64-SlicerJupyter-git6993275-2020-05-14.tar.gz&amp;checksum=2e06dc51ecebd9345cea80953b5a9d5b</li>
<li>
</li><li>RUN curl -OJL "$SLICER_JUPYTER_DOWNLOAD_URL"</li>
<li>#COPY $SLICER_JUPYTER_ARCHIVE .</li>
<li>
</li><li>COPY start-xorg.sh .</li>
<li>COPY install.sh .</li>
<li>RUN ./install.sh ${HOME}/$SLICER_ARCHIVE/Slicer</li>
<li>
</li><li>RUN rm $SLICER_JUPYTER_ARCHIVE</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @pieper (2020-10-07 18:21 UTC)

<p>Yet another option would be to run slicer as part of the docker build step and have it programmatically access the needed extensions.  This has the advantage that you don’t need to hard code the package URLs, only the extension names.<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Download_and_install_extension">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Download_and_install_extension</a></p>

---

## Post #5 by @Alex_Vergara (2020-10-07 18:26 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="13925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Yet another option would be to run slicer as part of the docker build step and have it programmatically access the needed extensions.</p>
</blockquote>
</aside>
<p>I have tried this approach. BUT, slicer ask for restart and if you just call another slicer command it says the extension is not properly installed. See <a href="https://gitlab.com/opendose/opendose3d/-/issues/26" rel="noopener nofollow ugc">these errors</a>.</p>

---

## Post #6 by @pieper (2020-10-07 18:28 UTC)

<p>Hmm, I haven’t tried but that sounds fixable.</p>

---

## Post #7 by @lassoan (2020-10-07 18:41 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="5" data-topic="13925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>I have tried this approach. BUT, slicer ask for restart and if you just call another slicer command it says the extension is not properly installed. See <a href="https://gitlab.com/opendose/opendose3d/-/issues/26">these errors </a>.</p>
</blockquote>
</aside>
<p>I don’t see any errors related to extension install.</p>
<p>Once the extension is installed, you don’t need to restart Slicer, just exit Slicer and when you start it next time it works well. You can see how it works in SlicerJupyter docker image (see link above).</p>

---

## Post #8 by @muratmaga (2020-10-07 20:53 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="13925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Yet another option would be to run slicer as part of the docker build step and have it programmatically access the needed extensions. This has the advantage that you don</p>
</blockquote>
</aside>
<p>I think this will work for me the simplest. Thanks.</p>

---

## Post #9 by @muratmaga (2020-10-08 04:25 UTC)

<p>assuming the extensions to be installed in extensions.py</p>
<p>docker command<br>
<code>RUN /opt/slicer/bin/Slicer --no-main-window --python-script ./extensions.py</code><br>
fails due to lack of X environment. specific error:</p>
<p><code>qt.qpa.screen: QXcbConnection: could not connect to display Could not connect to any X display</code></p>

---

## Post #10 by @lassoan (2020-10-08 04:52 UTC)

<p>You can use the <a href="https://github.com/Slicer/SlicerDocker/blob/c13632a1061371937f73acf9d42c605850f7b3bb/slicer-notebook/Dockerfile">SlicerJupyter docker image</a> as an example of setting up display properly and use Slicer’s extension manager to install the extension. By following <a class="mention" href="/u/pieper">@pieper</a>’s suggestion you can make installation even simpler (by making extension manager download the extension, too, instead of manually downloading it from a URL).</p>

---

## Post #11 by @ROSENty (2021-12-30 09:36 UTC)

<p>dear Andras, my question is how to Slicer’s extension manager to install the extension. Cause docker container is non-GUI. Please help me. Thanks a lot .<br>
Btw, my question is report here. <a href="https://discourse.slicer.org/t/how-to-install-slicerrt-extension-in-docker-slicerdocker-container/21270">https://discourse.slicer.org/t/how-to-install-slicerrt-extension-in-docker-slicerdocker-container/21270?u=rosenty</a></p>

---

## Post #12 by @lassoan (2021-12-30 17:58 UTC)

<aside class="quote no-group" data-username="ROSENty" data-post="11" data-topic="13925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rosenty/48/13334_2.png" class="avatar"> ROSENty:</div>
<blockquote>
<p>Cause docker container is non-GUI</p>
</blockquote>
</aside>
<p>Showing GUI or not is your choice, but you need to set up a display server to run the full application. It does not mean that you need to display a GUI at the host.</p>
<p>The slicer-notebook docker image that I linked above installs SlicerJupyter. Replace that by SlicerElastix and you are good.</p>

---

## Post #13 by @pieper (2021-12-30 19:52 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="9" data-topic="13925" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>assuming the extensions to be installed in extensions.py</p>
<p>docker command<br>
<code>RUN /opt/slicer/bin/Slicer --no-main-window --python-script ./extensions.py</code><br>
fails due to lack of X environment. specific error:</p>
<p><code>qt.qpa.screen: QXcbConnection: could not connect to display Could not connect to any X display</code></p>
</blockquote>
</aside>
<p>Another option for this is to use <code>xvfb-run</code> in your <code>Dockerfile</code> like <a href="https://github.com/pieper/SlicerDockers/blob/master/slicer-plus/Dockerfile#L8-L21">this example</a>.</p>

---

## Post #14 by @muratmaga (2021-12-31 00:08 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="13925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can use the <a href="https://github.com/Slicer/SlicerDocker/blob/c13632a1061371937f73acf9d42c605850f7b3bb/slicer-notebook/Dockerfile">SlicerJupyter docker image </a> as a</p>
</blockquote>
</aside>
<p>FYI, I don’t think the download/wget links in that image is valid anymore. I think they refer to old midas server that doesn’t exist, I think…</p>

---

## Post #15 by @ROSENty (2021-12-31 07:48 UTC)

<p>I mean I don’t want to use slicer-Jupyter-notebook, I just want to use slicer with SlicerRT extension in the docker container, and execute python script like this <a href="https://discourse.slicer.org/t/installing-extension-inside-a-dockerfile/13925/9">https://discourse.slicer.org/t/installing-extension-inside-a-dockerfile/13925/9?u=rosenty</a></p>
<pre><code class="lang-auto">/xxx/Slicer-X-Y-linux-amd64/Slicer --no-main-window --python-script ./myTest.py
</code></pre>

---

## Post #16 by @lassoan (2021-12-31 15:11 UTC)

<p>You can jusr just the relevant parts of the image: setting up the display server and installing an extension. There are many other Slicer docker images for various purposes. You can find references to them in posts in this forum.</p>
<p>Unfortunately, we don’t have a single location where all the images are listed at, but we could create it now. <a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/muratmaga">@muratmaga</a>, <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> what do you think about adding links to all known Slicer docker (and singularity, etc.) images at <a href="https://github.com/Slicer/SlicerDocker/blob/master/README.rst" class="inline-onebox">SlicerDocker/README.rst at master · Slicer/SlicerDocker · GitHub</a>? The earlier idea of having a single hierarchy of images may be unrealistic, but at least collecting links (with a 1-2 sentence description of each) at a single location should be feasible.</p>

---

## Post #17 by @pieper (2021-12-31 19:02 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="16" data-topic="13925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>what do you think about adding links to all known Slicer docker (and singularity, etc.) images at <a href="https://github.com/Slicer/SlicerDocker/blob/master/README.rst">SlicerDocker/README.rst at master · Slicer/SlicerDocker · GitHub</a>?</p>
</blockquote>
</aside>
<p>This makes sense.  And since it’s still an active topic we could add links to the discourse threads as well.</p>

---

## Post #18 by @mau_igna_06 (2022-01-01 00:56 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="16" data-topic="13925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>what do you think about adding links to all known Slicer docker (and singularity, etc.) images at <a href="https://github.com/Slicer/SlicerDocker/blob/master/README.rst" rel="noopener nofollow ugc">SlicerDocker/README.rst at master · Slicer/SlicerDocker · GitHub</a>?</p>
</blockquote>
</aside>
<p>Yes. No problem Andras</p>

---
