# Bad allocation exception

**Topic ID**: 12172
**Date**: 2020-06-23
**URL**: https://discourse.slicer.org/t/bad-allocation-exception/12172

---

## Post #1 by @SummerZ2020 (2020-06-23 08:05 UTC)

<p>Operating system:windows<br>
Slicer version:4.11 2020-6-15<br>
Expected behavior:The segment operation can be done successfully.<br>
Actual behavior: bad allocation exception popped up.<br>
I add a CT image volume which contains 2748 images. and then i use “Threshold” to segment first, and then I clicked “Islands” and choose “Remove small islands” to remove the islands which voxel number is smaller than 500. And then the exception popped up. The cpu memory occupied by Slicer app is up to almost 8 GB. see the screenshot below.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e316357b65d16242bdd8e3eedaf000dbf9045045.png" data-download-href="/uploads/short-url/woTY1EgN81PSegqMifw8YjiA8TP.png?dl=1" title="bad allocation exception" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e316357b65d16242bdd8e3eedaf000dbf9045045_2_690x371.png" alt="bad allocation exception" data-base62-sha1="woTY1EgN81PSegqMifw8YjiA8TP" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e316357b65d16242bdd8e3eedaf000dbf9045045_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e316357b65d16242bdd8e3eedaf000dbf9045045_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e316357b65d16242bdd8e3eedaf000dbf9045045_2_1380x742.png 2x" data-dominant-color="AFAEB4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">bad allocation exception</span><span class="informations">2560×1380 276 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2020-06-23 13:08 UTC)

<p>That’s not really a bug, you just ran out of memory.  Options are to get more memory, allocate more virtual memory, crop the volume, or choose different segmentation methods.  For example, you might try a denoising filter on the images first, so you have fewer islands.</p>

---

## Post #3 by @SummerZ2020 (2020-06-24 01:37 UTC)

<p>I see, thanks a lot.</p>

---

## Post #4 by @muratmaga (2020-06-24 03:02 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="12172">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>That’s not really a bug, you just ran out of memory</p>
</blockquote>
</aside>
<p>Is it possible to catch these bad allocation errors and display a proper out of memory error with out standard suggestion of either increasing the physical memory, virtual memory or downsample the image.<br>
<a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #5 by @pieper (2020-06-24 12:22 UTC)

<p>I was thinking the same thing - <code>bad allocation</code> may not be clear to non-programmers, and it is misleading in this case, since it says it’s a Slicer error, which implies bug.  <code>bad allocation</code> is still a pretty non-specific error because it could be models or algorithms throwing the error so users will still need to come up with their own strategy to fix it.  Most of the message is correct though, since we don’t know where the error occurred it’s not recoverable in general and the user should save and restart the application.</p>
<p>I added [an issue].  Here’s the code in case anyone wants to take a shot at it.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/dfef9574096a10c4f02337b59c5edfd6810b55db/Base/QTGUI/qSlicerApplication.cxx#L390-L417" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/dfef9574096a10c4f02337b59c5edfd6810b55db/Base/QTGUI/qSlicerApplication.cxx#L390-L417" target="_blank">Slicer/Slicer/blob/dfef9574096a10c4f02337b59c5edfd6810b55db/Base/QTGUI/qSlicerApplication.cxx#L390-L417</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="390" style="counter-reset: li-counter 389 ;">
<li>bool qSlicerApplication::notify(QObject *receiver, QEvent *event)</li>
<li>{</li>
<li>  try</li>
<li>    {</li>
<li>    return QApplication::notify(receiver, event);</li>
<li>    }</li>
<li>  catch( std::exception&amp; exception )</li>
<li>    {</li>
<li>    QString errorMessage;</li>
<li>    errorMessage = tr("%1 has caught an internal error.\n\n").arg(this-&gt;applicationName());</li>
<li>    errorMessage += tr("You may be able to continue from this point, but results are undefined.\n\n");</li>
<li>    errorMessage += tr("Suggested action is to save your work and restart.");</li>
<li>    errorMessage += tr("\n\nIf you have a repeatable sequence of steps that causes this message, ");</li>
<li>    errorMessage += tr("please report the issue following instructions available at http://slicer.org\n\n\n");</li>
<li>    errorMessage += tr("The message detail is:\n\n");</li>
<li>    errorMessage += tr("Exception thrown in event: ") + exception.what();</li>
<li>    qCritical() &lt;&lt; errorMessage;</li>
<li>    if (this-&gt;commandOptions()-&gt;isTestingEnabled())</li>
<li>      {</li>
<li>      this-&gt;exit(EXIT_FAILURE);</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/dfef9574096a10c4f02337b59c5edfd6810b55db/Base/QTGUI/qSlicerApplication.cxx#L390-L417" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @lassoan (2020-06-24 16:33 UTC)

<p>Good idea, I’ve added an issue to not forget about it: <a href="https://github.com/Slicer/Slicer/issues/5011">https://github.com/Slicer/Slicer/issues/5011</a></p>

---
