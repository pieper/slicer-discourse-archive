# Large discrepancy in logged output in Python vs. Bash Consoles

**Topic ID**: 43783
**Date**: 2025-07-20
**URL**: https://discourse.slicer.org/t/large-discrepancy-in-logged-output-in-python-vs-bash-consoles/43783

---

## Post #1 by @SomeoneInPart (2025-07-20 12:55 UTC)

<p>For ease of testing a WIP module, I will often start Slicer from a bash shell, so that I could save its output to a log programmatically. However, when I went to refactor my many <code>print</code> statements into <code>logging</code> calls, I noticed that they no longer appeared. Digging deeper, it seems that calling Slicer from the command line results in a pretty substantial de-sync.</p>
<p>For reference:</p>
<p>The bash console’s output:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad366a3681fff812d3bd98828dd5c31aec744d59.png" data-download-href="/uploads/short-url/oIjbw41dsUVyY4OLRp1YUB8tpkB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad366a3681fff812d3bd98828dd5c31aec744d59_2_517x372.png" alt="image" data-base62-sha1="oIjbw41dsUVyY4OLRp1YUB8tpkB" width="517" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad366a3681fff812d3bd98828dd5c31aec744d59_2_517x372.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad366a3681fff812d3bd98828dd5c31aec744d59_2_775x558.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad366a3681fff812d3bd98828dd5c31aec744d59.png 2x" data-dominant-color="310F27"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">812×585 15.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Slicer’s Python Console:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca449c2db5230aa61ed71f25d5b441890efa05cc.png" data-download-href="/uploads/short-url/sRlrCf9jy5YLNbQdgUl4fas3REw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca449c2db5230aa61ed71f25d5b441890efa05cc_2_517x177.png" alt="image" data-base62-sha1="sRlrCf9jy5YLNbQdgUl4fas3REw" width="517" height="177" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca449c2db5230aa61ed71f25d5b441890efa05cc_2_517x177.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca449c2db5230aa61ed71f25d5b441890efa05cc_2_775x265.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca449c2db5230aa61ed71f25d5b441890efa05cc.png 2x" data-dominant-color="1F231F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1031×353 55.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The code in question:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1efeefcc2a2bdfa71ac9f633705fb14d0465570.png" data-download-href="/uploads/short-url/rFEcPSw5t5QWVDeW26tqLcB2BdS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1efeefcc2a2bdfa71ac9f633705fb14d0465570.png" alt="image" data-base62-sha1="rFEcPSw5t5QWVDeW26tqLcB2BdS" width="326" height="120"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">326×120 6.79 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Far as I can tell, the following is happening:</p>
<ul>
<li><code>Qt</code> logs are properly displayed in both the Python and Bash console</li>
<li><code>print</code> statements are only shown in the Bash console</li>
<li><code>logging</code> statements are only shown in the Python console</li>
</ul>
<p>Is their something I’m missing? This is on Slicer 5.8.1, called within a <code>ScriptedLoadableModuleWidget</code> and <code>VTKObservationMixin</code> subclass, with <code>get_cart_logger</code> simply being a wrapper for a <code>logging.getLogger</code> call with some tracking strapped on. Any insight on this would be appreciated.</p>

---

## Post #2 by @SomeoneInPart (2025-07-21 01:42 UTC)

<p>Slight correction; only <em>some</em> of the <code>QT</code> logs are placed in the Bash console; the “green” logs are Python only, further confusing things.</p>

---

## Post #3 by @jamesobutler (2025-07-21 02:05 UTC)

<p>Have you tried adjusting the user setting for the logging level on the python console? See the following linked thread below:</p>
<aside class="quote" data-post="1" data-topic="26418">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/info-level-logging-messages-do-not-appear-in-python-console/26418">Info level logging messages do not appear in Python console</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #000000;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    I built the latest Slicer 5.3, and I now see the changes in the Python console. It’s great to see Qt and VTK errors there too. 
However, one thing that could make my day to day work very hard is that the output from logging.info calls in the executed code do not appear in the console. Is there any way to turn this back on? Thank you!
  </blockquote>
</aside>


---

## Post #4 by @SomeoneInPart (2025-07-21 02:12 UTC)

<p>Thank you for your response. I did check that; my “Log level” is currently set to Debug:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f0bc009cd8cb55b0086c4c54fd5232b5200848f.png" data-download-href="/uploads/short-url/bhgTtoKvEWqvIGDOvazV8tY3KhN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f0bc009cd8cb55b0086c4c54fd5232b5200848f_2_636x500.png" alt="image" data-base62-sha1="bhgTtoKvEWqvIGDOvazV8tY3KhN" width="636" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f0bc009cd8cb55b0086c4c54fd5232b5200848f_2_636x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f0bc009cd8cb55b0086c4c54fd5232b5200848f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f0bc009cd8cb55b0086c4c54fd5232b5200848f.png 2x" data-dominant-color="303131"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">795×625 39.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is also an <code>ERROR</code> level logging message, so it should appear for any logging whatsoever. And it does; but only in the Python console, not Bash.</p>

---

## Post #5 by @lassoan (2025-07-22 09:34 UTC)

<p>Console is only available in certain environments (e.g., no console on Windows GUI applications), so Slicer does not depend on it and I would not recommend for debugging.</p>
<p>You can access logs in the application log file (<code>slicer.app.errorLogModel().filePath</code>). You can also add a callback function to the error log model object to get notified when something is logged and can get any log messages like this:</p>
<pre data-code-wrap="python"><code class="lang-python">def onEntryAdded(datetime, threadId, logLevel, origin, context, text):
    slicer.util.messageBox(f"[{datetime.toString()}] [{origin}] ({logLevel}) {text}")

slicer.app.errorLogModel().connect('entryAdded(QDateTime,QString,ctkErrorLogLevel::LogLevel,QString,ctkErrorLogContext,QString)', onEntryAdded)
</code></pre>

---

## Post #6 by @SomeoneInPart (2025-07-22 18:31 UTC)

<p>Ah; I was wondering how to access that message box. Will start pivoting to that then; thank you!</p>

---
