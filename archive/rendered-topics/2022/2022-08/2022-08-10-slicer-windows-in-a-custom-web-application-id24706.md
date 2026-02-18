# Slicer windows in a custom web application

**Topic ID**: 24706
**Date**: 2022-08-10
**URL**: https://discourse.slicer.org/t/slicer-windows-in-a-custom-web-application/24706

---

## Post #1 by @NaglisR (2022-08-10 08:35 UTC)

<p>Hi all, I have a somewhat abstract question regarding integrating slicer windows in a custom web application window. Generally I suppose it should work something like this <a href="https://youtu.be/vTGQMDIqL9k" rel="noopener nofollow ugc">https://youtu.be/vTGQMDIqL9k</a> meaning that the Slicer instance would be running in a docker instance (deployed in bundle with other docker containers) which would be able to receive requests and open a selected study in a slicer window on command. However, optimally I would be looking for a way to do an even deeper integration, which would allow to display a custom slicer window as an iframe or similar in an interactive custom html page.<br>
Optimally it should look like something like SlicerJupyter UI, only integrated in a custom UI and without the code.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac467091257e3c32a4b76b4219b6b59433a9f40f.png" alt="Screenshot from 2022-08-10 11-29-02" data-base62-sha1="oA12yNlLsFPnMJbXJPaI1nPwzAX" width="318" height="330"><br>
Is there a way to do this with Slicer, if so what could be the best way to do it (using SlicerDocker/JupyterSlicer/SlicerWeb?).</p>
<p>I am not sure if there are existing examples of a similar type of integration. Thanks to anyone in advance :).</p>

---

## Post #2 by @pieper (2022-08-10 14:07 UTC)

<p>It sounds like you have a use case that would be a good fit for the WebServer module now in Slicer 5.0.3 (the module used to be in the SlicerWeb extension prototype).  The WebServer exposes a rest api that can be used to control Slicer and get rendered images.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html?highlight=webserver" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html?highlight=webserver</a></p>

---

## Post #3 by @NaglisR (2022-08-10 15:00 UTC)

<p>This looks very promising, thank you! Is it possible to set it up to support multiple concurrent users?<br>
Will investigate and try it out.</p>

---

## Post #4 by @pieper (2022-08-10 18:00 UTC)

<aside class="quote no-group" data-username="NaglisR" data-post="3" data-topic="24706">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/naglisr/48/16280_2.png" class="avatar"> NaglisR:</div>
<blockquote>
<p>Is it possible to set it up to support multiple concurrent users?</p>
</blockquote>
</aside>
<p>Yes, if the concurrent users need to access the same data and other state they can access the same Slicer instance.  If they need a private session then the server can be run from different instances of Slicer using distinct ports (e.g. in different docker containers or just running in different processes).  Let us know how it goes!</p>

---

## Post #5 by @NaglisR (2022-08-11 07:49 UTC)

<p>Understood, thank you.<br>
I am stuggling a bit to find these endpoints described in the Remote Rendering:<br>
“There are several endpoints to get png images from slice views and 3D views. These endpoints allow control of slice offset or 3D camera view (see method doc strings in the source code for options since there is currently no auto-generated api documentation)”<br>
Also, are these enpoints designed to return static png images, or is there a posibility to return a dynamic endpoint, which return a red slice window for example, with the scolling controls, similarly like a JupyterSlicer function?</p>
<pre><code class="lang-auto">from ipywidgets import interact
@interact(position=(0,100))
def update(position=50):
    return slicernb.ViewSliceDisplay('Red', positionPercent=position)
</code></pre>

---

## Post #6 by @pieper (2022-08-11 14:20 UTC)

<p>The assumption is that the client (javascript) would implement all the control like sliders to touch interactions and just use the WebServer api to set rendering parameters and retrieve rendered data.  So you would build the <code>scrollTo</code> parameter value based on the state of the slider and get back the png of the current slice.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/WebServer/Resources/docroot/index.html#L51-L55">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/WebServer/Resources/docroot/index.html#L51-L55" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/WebServer/Resources/docroot/index.html#L51-L55" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Modules/Scripted/WebServer/Resources/docroot/index.html#L51-L55</a></h4>



    <pre class="onebox"><code class="lang-html">
      <ol class="start lines" start="51" style="counter-reset: li-counter 50 ;">
          <li>&lt;p&gt;Displays the current contents of a Slicer slice view window.&lt;/p&gt;
</li>
          <li>&lt;a href='./slicer/slice'&gt;slicer/slice&lt;/a&gt;&lt;br&gt;
</li>
          <li>&lt;a href='./slicer/slice?orientation=sagittal'&gt;slicer/slice?orientation=sagittal&lt;/a&gt;&lt;br&gt;
</li>
          <li>&lt;a href='./slicer/slice?orientation=axial&amp;scrollTo=.3'&gt;slicer/slice?orientation=axial&amp;scrollTo=.3&lt;/a&gt;&lt;br&gt;
</li>
          <li>&lt;a href='./slicer/slice?orientation=axial&amp;scrollTo=.6'&gt;slicer/slice?orientation=axial&amp;scrollTo=.6&lt;/a&gt;&lt;br&gt;
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
