# How to stop a process without "Force Quit"

**Topic ID**: 8415
**Date**: 2019-09-13
**URL**: https://discourse.slicer.org/t/how-to-stop-a-process-without-force-quit/8415

---

## Post #1 by @dfafalis (2019-09-13 14:32 UTC)

<p>While using effects (any effects available) I very frequently encounter this problem:</p>
<p>a window pops up stating that the system is running out of memory and recommends to <strong>Force Quit</strong> Slicer</p>
<p>This happens a lot, either with small or large models.</p>
<p>I was wondering whether there is a way to stop the process of the effect without being forced to quit Slicer.</p>
<p>I am using MacOS, with a 16GB RAM and cache memory up to 200GB.</p>
<p>Please see attached screenshot.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45fc287aaad82f0f6dd1fb44d10eefe4dba6f765.jpeg" data-download-href="/uploads/short-url/9Z7bT4gkOd6E7o7xE7lcT5mUQAt.jpeg?dl=1" title="54" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45fc287aaad82f0f6dd1fb44d10eefe4dba6f765_2_690x431.jpeg" alt="54" data-base62-sha1="9Z7bT4gkOd6E7o7xE7lcT5mUQAt" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45fc287aaad82f0f6dd1fb44d10eefe4dba6f765_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45fc287aaad82f0f6dd1fb44d10eefe4dba6f765_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45fc287aaad82f0f6dd1fb44d10eefe4dba6f765_2_1380x862.jpeg 2x" data-dominant-color="9D9CB5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">54</span><span class="informations">3360×2100 1.03 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Thank you</p>

---

## Post #2 by @pieper (2019-09-14 15:01 UTC)

<p>What kind of images are you working with?  If they are large, you might want to crop them first (search discourse for CropVolume).</p>
<p>Also does this happen more if you have used Slicer for a while?  If so maybe there’s a memory leak we need to investigate.  If you can provide specific details to replicate the issue (what data, what effects, etc) it would really help.</p>
<p>Otherwise maybe the easiest is just to get an extra big disk.</p>

---

## Post #3 by @danpak94 (2023-04-12 21:58 UTC)

<p>Hello,</p>
<p>While the suggested answer may solve this particular case, I’m still interested about the general principle of stopping a process in 3D slicer.</p>
<p>If I have a custom pushbutton that calls a python function, is there proper way to stop that call mid-process, similar to a ctrl+c in a regular python interpreter?</p>
<p>Thank you</p>

---

## Post #4 by @hherhold (2023-04-12 22:08 UTC)

<p>To the best of my knowledge, there is no general purpose method of halting an in-progress operation in slicer. Some filters can be canceled and things like that, but there is no “global ctrl-C”, I think.</p>
<p>There are a number of tricks that can reduce your memory footprint, including cropping or resampling your dataset, and you can even set the number of undo states to zero with a little python.</p>
<p>But looking at the force quit dialog - Slicer is using 133GB? This is <em>massive</em>. I have to echo what <a class="mention" href="/u/pieper">@pieper</a> is saying - what type of data are you looking at, and do you need this resolution?</p>

---

## Post #5 by @hherhold (2023-04-12 22:09 UTC)

<p>You’re also using a pretty old version of Slicer - I’ve lost track of how many changes would help with memory footprint since 2019.</p>

---

## Post #6 by @hherhold (2023-04-12 22:11 UTC)

<p>Oh wait this is a really really old screenshot in the original post. My mistake. Please disregard nearly all of the above.</p>

---

## Post #7 by @pieper (2023-04-12 23:03 UTC)

<aside class="quote no-group" data-username="danpak94" data-post="3" data-topic="8415">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/danpak94/48/18310_2.png" class="avatar"> danpak94:</div>
<blockquote>
<p>If I have a custom pushbutton that calls a python function, is there proper way to stop that call mid-process, similar to a ctrl+c in a regular python interpreter?</p>
</blockquote>
</aside>
<p>To make this work you need to be able to integrate your custom code into the Slicer event loop.  You can put up a progress dialog and have the cancel signal set a variable that you check periodically during processing.   By calling <code>slicer.app.processEvents</code> periodically the variable will get set and you can break out of your processing.</p>
<p>There are several examples of this pattern in the source code, like this one:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/7cd9d41e60d4ebefd7a453d4bb24bfc87403bb3a/Modules/Scripted/DICOMLib/DICOMUtils.py#L822-L960">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/7cd9d41e60d4ebefd7a453d4bb24bfc87403bb3a/Modules/Scripted/DICOMLib/DICOMUtils.py#L822-L960" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/7cd9d41e60d4ebefd7a453d4bb24bfc87403bb3a/Modules/Scripted/DICOMLib/DICOMUtils.py#L822-L960" target="_blank" rel="noopener">Slicer/Slicer/blob/7cd9d41e60d4ebefd7a453d4bb24bfc87403bb3a/Modules/Scripted/DICOMLib/DICOMUtils.py#L822-L960</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="822" style="counter-reset: li-counter 821 ;">
          <li>def importFromDICOMWeb(dicomWebEndpoint, studyInstanceUID, seriesInstanceUID=None, accessToken=None, bulkRetrieve=True):</li>
          <li>    """</li>
          <li>    Downloads and imports DICOM series from a DICOMweb instance.</li>
          <li>    Progress is displayed and if errors occur then they are displayed in a popup window in the end.</li>
          <li>    If all the instances in a series are already imported then the series will not be retrieved and imported again.</li>
          <li></li>
          <li>    :param dicomWebEndpoint: Endpoint URL for retrieving the study/series from DICOMweb</li>
          <li>    :param studyInstanceUID: UID for the study to be downloaded</li>
          <li>    :param seriesInstanceUID: UID for the series to be downloaded. If not specified, all series will be downloaded from the study</li>
          <li>    :param accessToken: Optional access token for the query</li>
          <li>    :param bulkRetrieve: If enabled then all instances of a series is retrieved with one query. Some servers (including Slicer</li>
          <li>        DICOMweb server) may not support bulk retrieve and require query of each instance.</li>
          <li>    :return: List of imported study UIDs</li>
          <li></li>
          <li>    Example: calling from PythonSlicer console</li>
          <li></li>
          <li>    .. code-block:: python</li>
          <li></li>
          <li>      from DICOMLib import DICOMUtils</li>
          <li>      loadedUIDs = DICOMUtils.importFromDICOMWeb(dicomWebEndpoint="https://yourdicomweburl/dicomWebEndpoint",</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/7cd9d41e60d4ebefd7a453d4bb24bfc87403bb3a/Modules/Scripted/DICOMLib/DICOMUtils.py#L822-L960" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @pieper (2023-04-12 23:04 UTC)

<p>Or you can put the processing in a thread or separate process but those can be more complex.</p>

---
