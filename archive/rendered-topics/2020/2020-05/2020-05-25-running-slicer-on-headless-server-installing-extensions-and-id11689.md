# Running Slicer on headless server (Installing Extensions and more...)

**Topic ID**: 11689
**Date**: 2020-05-25
**URL**: https://discourse.slicer.org/t/running-slicer-on-headless-server-installing-extensions-and-more/11689

---

## Post #1 by @Davide_Cester (2020-05-25 09:42 UTC)

<p>Dear all,</p>
<p>I am setting up a shared server for the research in our group, it’s a headless Ubuntu 20.04. People are supposed to log in to web services and share the computing power. JupyterHub is already up &amp; running, with Python and R kernels available. Now I would like to add Slicer support, which I already did on a standalone machine with Ubuntu 18.04.</p>
<p>The documentation (<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_run_Slicer_on_a_headless_compute_node.3F" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/Python scripting - Slicer Wiki</a>) refers to a discussion that is not reachable (<a href="http://massmail.spl.harvard.edu/public-archives/slicer-devel/2015/017317.html" class="inline-onebox" rel="noopener nofollow ugc">[slicer-devel] Slicer batch mode</a>), that’s why I am opening a new one here.</p>
<p>I have installed Slicer in /opt/slicer-4.10.2 and I am trying to adapt the installation instructions in step 2 from here: <a href="https://github.com/Slicer/SlicerJupyter" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/SlicerJupyter: Extension for 3D Slicer that allows the application to be used from Jupyter notebook</a></p>
<p>My questions are:</p>
<ul>
<li>I tried to run the Slicer GUI from remote with “ssh -X” but it loops erroring “composeAndFlush: makeCurrent() failed” after the initial medical disclaimer. Is that supposed to work?</li>
<li>how do I install the SlicerJupyter extension without the GUI?</li>
<li>how can I access the command to be copied in the SlicerJupyter Extension tab?</li>
</ul>
<p>Thanks in advance <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @Davide_Cester (2020-05-25 12:29 UTC)

<p>Here some of the solutions I found so far:</p>
<aside class="quote no-group" data-username="Davide_Cester" data-post="1" data-topic="11689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_cester/48/6564_2.png" class="avatar"> Davide_Cester:</div>
<blockquote>
<p>how do I install the SlicerJupyter extension without the GUI?</p>
</blockquote>
</aside>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Extensions#How_to_manually_download_an_extension_package.3F" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Extensions#How_to_manually_download_an_extension_package.3F</a><br>
However the site won’t load normally, see <a href="https://discourse.slicer.org/t/extension-app-store-not-accessible-http-slicer-kitware-com-midas3-slicerappstore/7550" class="inline-onebox">Extension app store not accessible (http://slicer.kitware.com/midas3/slicerappstore)</a> for a workaround. Even in this case no extension is found, for any combination of OS and version…?<br>
That site seems fundamentally broken, everything I clic just generates an endless loading in the browser.</p>
<aside class="quote no-group" data-username="Davide_Cester" data-post="1" data-topic="11689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_cester/48/6564_2.png" class="avatar"> Davide_Cester:</div>
<blockquote>
<p>how can I access the command to be copied in the SlicerJupyter Extension tab?</p>
</blockquote>
</aside>
<p>From <a href="https://github.com/Slicer/SlicerJupyter:" rel="noopener nofollow ugc">https://github.com/Slicer/SlicerJupyter:</a><br>
jupyter-kernelspec install /tmp/SlicerJupyter-build/inner-build/share/Slicer-4.11/qt-loadable-modules/JupyterKernel/Slicer-4.9/ --replace --user<br>
Of course the paths will have to be updated but that depends on the extension installation, which I’m not yet able to do…</p>

---

## Post #3 by @lassoan (2020-05-25 13:28 UTC)

<aside class="quote no-group quote-modified" data-username="Davide_Cester" data-post="2" data-topic="11689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_cester/48/6564_2.png" class="avatar"> Davide_Cester:</div>
<blockquote>
<p>However the site won’t load normally, see <a href="https://discourse.slicer.org/t/extension-app-store-not-accessible-http-slicer-kitware-com-midas3-slicerappstore/7550">Extension app store not accessible</a></p>
</blockquote>
</aside>
<p>I confirm that the extension server takes really long time to respond (it took me now about 5-10 minutes to load the page). Unfortunately, the server is temporarily overloaded from time to time. It usually returns to normal in an hour or so. <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> when you have a chance, could you check if anything can be done?</p>
<p>In the meantime, you can try specifying a Slicer revision - then the server can skip the automatic revision detection step and there is a higher chance your request gets served. For example: <a href="http://slicer.kitware.com/midas3/slicerappstore/?os=win&amp;arch=amd64&amp;revision=29074&amp;category=Developer%20Tools&amp;search=&amp;layout=layout" class="inline-onebox">@KitwareMedical/slicer-extensions-webapp</a></p>
<p>If that does not work then you can download extensions directly from the dashboard: <a href="http://slicer.cdash.org/index.php?project=SlicerPreview" class="inline-onebox">CDash</a></p>
<aside class="quote no-group quote-modified" data-username="Davide_Cester" data-post="1" data-topic="11689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_cester/48/6564_2.png" class="avatar"> Davide_Cester:</div>
<blockquote>
<p>I have installed Slicer in /opt/slicer-4.10.2 and I am trying to adapt the installation instructions in step 2 from here: <a href="https://github.com/Slicer/SlicerJupyter">https://github.com/Slicer/SlicerJupyter </a></p>
</blockquote>
</aside>
<p>This docker image describes a complete Slicer Jupyter kernel installation:</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/Slicer/SlicerDocker/tree/main/slicer-notebook">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerDocker/tree/main/slicer-notebook" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/Slicer/SlicerDocker/tree/main/slicer-notebook" target="_blank" rel="noopener"></a></h3>

  <p><a href="https://github.com/Slicer/SlicerDocker/tree/main/slicer-notebook" target="_blank" rel="noopener">//github.com/Slicer/SlicerDocker/tree/main/slicer-notebook</a></p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>We use this image with binder’s dockerhub and it works well.</p>

---

## Post #4 by @Davide_Cester (2020-05-25 15:48 UTC)

<p>Hi,</p>
<p>thanks for the reply! It now works and I’m writing a few lines as reference for the others.</p>
<p>After some minutes I managed to get the archive for the extension, and I figured it out where to manually copy the files. In the install.sh in the Docker repo there is a nice command-line alternative which I didn’t fully test: one command to get the current version, another to download the extension, the third one to install it. However with my slicer the first one fails with something like ‘revision’ property missing, so I did it manually.</p>
<p>To run headless I installed the Ubuntu package xvfb. In the docker repo a custom Xorg is launched instead, with xorg.conf and all, but I am confortable with xvfb from previous experiencese. I located the kernel-template.json, copied into kernel.json in the same folder and replaced the version and executable parameters:</p>
<pre><code>{
"display_name": "Slicer 4.10",
"language" : "python",
"argv": [
    "xvfb-run",
    "-a",
    "/opt/slicer-4.10.2/Slicer",
    "--no-splash",
    "--python-code",
    "connection_file=r'{connection_file}'; print('Jupyter connection file: ['+connection_file+']'); slicer.modules.jupyterkernel.startKernel(connection_file);slicer.util.mainWindow().showMinimized()"
]
</code></pre>
<p>}</p>
<p>and finally I installed the kernel in Jupyter with</p>
<p><code>sudo jupyter-kernelspec install /path-to-slicer/share/Slicer-4.10/qt-loadable-modules/JupyterKernel/Slicer-4.10/ --replace</code></p>
<p>Didn’t add the documented option --user to enable the kernel for the entire system.</p>
<p>I have now a nice server where user can use Slicer via JupyterHub <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #5 by @lassoan (2020-05-25 15:53 UTC)

<p>I’m happy that it works for you now.</p>
<p>I would strongly recommend to use Slicer-4.11:</p>
<ul>
<li>it uses Python 3</li>
<li>you can install any python packages into Slicer’s Python environment</li>
<li>its kernel is based on xeus-python which is essentially a full IPython implementation (while our custom kernel that we implemented in Slicer-4.10 had a number of limitations), including widgets and interactive 3D viewer in notebook cells. See some more information here:</li>
</ul>
<aside class="quote quote-modified" data-post="1" data-topic="11569">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/run-slicer-in-your-web-browser-as-a-jupyter-notebook-or-as-a-full-application/11569">Run Slicer in your web browser - as a Jupyter notebook or as a full application</a> <a class="badge-category__wrapper " href="/c/announcements/7"><span data-category-id="7" style="--category-badge-color: #ED207B; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="Low-traffic category for 3D Slicer, extension, and community news and announcements."><span class="badge-category__name">Announcements</span></span></a>
  </div>
  <blockquote>
    It has been possible to use Slicer from Jupyter notebooks but the most recent Slicer Preview Release takes this to a whole new level. 
<a href="https://mybinder.org/v2/gh/slicer/SlicerNotebooks/master">Click here to try a few example interactive notebooks now</a> - or see a short video demonstrating the new features: 

  <a href="https://www.youtube.com/watch?v=oZ3_cRXX2QM" target="_blank" rel="noopener">
    [Medical image processing in your web browser using Jupyter notebooks and 3D Slicer]
  </a>


Highlights: 

Improved interactive use

You can now use IPython widgets (sliders, buttons, etc.) to control Slicer or adjust processing and visualization…
  </blockquote>
</aside>


---

## Post #6 by @Davide_Cester (2020-05-25 15:59 UTC)

<p>I was about to ask, why I was not seeing the JupyterNotebooksLib module. And now I wonder why I installed 4.10…??? <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=9" title=":smiley:" class="emoji" alt=":smiley:"> I’ll install 4.11 while I’m “hot”…<br>
I got the Preview announcement via mail a few days ago, that’s what motivated me to integrate Slicer in the server I’m building. Very nice tool!</p>
<p>Thanks again! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #7 by @lassoan (2020-05-25 16:03 UTC)

<p>Is your Slicer/Python/R JupyterHub docker image publicly available? It would help people who wants to set up Slicer server on their computers.</p>

---

## Post #8 by @Davide_Cester (2020-05-25 16:14 UTC)

<p>Unfortunately it’s not an image, I’m not that much into Docker yet. It’s an “old style” server with several services.<br>
I’m planning to write an article as soon as my first two users provide positive feedback, which I hope will be soon. Later I could maybe do an image myself, or someone could use my notes to build it. It would definitely be a good idea.</p>

---

## Post #9 by @Davide_Cester (2020-05-25 17:19 UTC)

<p>Ok, I moved to Slicer 4.11. Same procedure as before: installed slicer, installed extension, installed kernel. Kernel is available in Jupyter, but hangs in the connection and never becomes operational.</p>
<p>Usually when a kernel is hanging in the init / conn stage it’s a websocket issue, I had it before. But here the Python kernels are working, and Slicer 4.10 was working with the same webserver configuration. If I manually run the headless slicer it doesn’t crash, so it looks really like a communication problem.</p>
<p>Is there anything different between the two versions of Slicer and the extension?</p>
<p>Something I’ve noticed is that v. 4.11 has a kernel-configure.py script. Is that important? How do I run it?<br>
Here’s my kernel.json:</p>
<pre><code>{
    "display_name": "Slicer 4.11",
    "language" : "python",
    "argv": [
        "xvfb-run",
        "-a",
        "/opt/slicer/Slicer",
        "--no-splash",
        "--python-code",
        "connection_file=r'{connection_file}'; print('Jupyter connection file: ['+connection_file+']'); slicer.modules.jupyterkernel.startKernel(connection_file);slicer.util.mainWindow().showMinimized()"
    ]
}
</code></pre>
<p>My revision number is now 29074.</p>
<p>EDIT: it’s definitely a websocket problem, I get Javascript errors on the browser’s console.</p>
<p>EDIT <span class="hashtag">#2:</span> I have re-installed Slicer 4.10 in parallel, now I see both kernels. 4.10 works, 4.11 has WS issues.</p>

---

## Post #10 by @lassoan (2020-05-25 19:09 UTC)

<aside class="quote no-group" data-username="Davide_Cester" data-post="9" data-topic="11689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_cester/48/6564_2.png" class="avatar"> Davide_Cester:</div>
<blockquote>
<p>Something I’ve noticed is that v. 4.11 has a kernel-configure.py script</p>
</blockquote>
</aside>
<p>Where have you found that script? Can you send a link to the repository/file?</p>
<aside class="quote no-group" data-username="Davide_Cester" data-post="9" data-topic="11689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_cester/48/6564_2.png" class="avatar"> Davide_Cester:</div>
<blockquote>
<p>I have re-installed Slicer 4.10 in parallel, now I see both kernels. 4.10 works, 4.11 has WS issues.</p>
</blockquote>
</aside>
<p>Check <em>all</em> configuration steps that are performed in the slicer-notebook image - in the <a href="https://github.com/Slicer/SlicerDocker/blob/master/slicer-notebook/Dockerfile">dockerfile</a> and in <a href="https://github.com/Slicer/SlicerDocker/blob/master/slicer-notebook/install.sh">install.sh</a>.</p>
<p>Also double-check your zeromq version in Slicer and in the Jupyter client (if they are matching or compatible; maybe try upgrading/downgrading to a few different versions).</p>

---

## Post #11 by @Davide_Cester (2020-05-25 21:34 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="11689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Where have you found that script? Can you send a link to the repository/file?</p>
</blockquote>
</aside>
<p>It’s inside 29074-linux-amd64-SlicerJupyter-git4c5fa4d-2020-05-23.tar.gz downloaded from midas, in the folder 29074-linux-amd64-SlicerJupyter-git4c5fa4d-2020-05-23/share/Slicer-4.11/qt-loadable-modules/JupyterKernel/Slicer-4.11</p>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="11689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Check <em>all</em> configuration steps that are performed</p>
</blockquote>
</aside>
<p>You are right… I think what I was missing was:</p>
<p><code>sudo /opt/jupyterhub/bin/python3 -m pip install ipywidgets ipyevents ipycanvas</code><br>
<code>sudo /opt/jupyterhub/bin/python3 -m pip install websockify --upgrade</code><br>
<code>sudo /opt/jupyterhub/bin/jupyter-labextension install @jupyter-widgets/jupyterlab-manager</code><br>
<code>sudo /opt/jupyterhub/bin/jupyter-labextension install @jupyter-widgets/jupyterlab-manager ipycanvas</code><br>
<code>sudo /opt/jupyterhub/bin/jupyter-labextension install @jupyter-widgets/jupyterlab-manager ipyevents</code></p>
<p>commands to be run in the environment of jupyterhub.</p>
<p>Thanks!!!</p>

---

## Post #12 by @jcfr (2020-05-26 13:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="11689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Unfortunately, the server is temporarily overloaded from time to time</p>
</blockquote>
</aside>
<p>Indeed, the server is currently on <a href="https://www.slicer.org/wiki/Documentation/Labs/ExtensionsServer">“life support”</a> (we need to allocate resources to transition it), in the meantime I will make sure it is restarted on daily basis (9pm EST)</p>

---
