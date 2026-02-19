---
topic_id: 10272
title: "How To Close The Widget"
date: 2020-02-15
url: https://discourse.slicer.org/t/10272
---

# How to close the Widget

**Topic ID**: 10272
**Date**: 2020-02-15
**URL**: https://discourse.slicer.org/t/how-to-close-the-widget/10272

---

## Post #1 by @timeanddoctor (2020-02-15 03:33 UTC)

<p>I called the endoscopy with python script such as:<br>
<code> import Endoscopy</code></p>
<pre><code>endo=Endoscopy.EndoscopyWidget()
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/934099457bb371b356f8b89774c50418c97cf551.png" data-download-href="/uploads/short-url/l0EAAZkOPTnv06LT44e0Dio6c1j.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/934099457bb371b356f8b89774c50418c97cf551.png" alt="image" data-base62-sha1="l0EAAZkOPTnv06LT44e0Dio6c1j" width="430" height="500" data-dominant-color="D6D6D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">469×545 9.09 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But I cannot close it.</p>
<p><code>endo.close()</code></p>
<p>and I get some erro:<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
AttributeError: EndoscopyWidget instance has no attribute ‘close’</p>
<p>Can I close this window by python code and change the mainTitle from ‘slicer’ to ‘endoscopy’. What can I do for that proplems?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2020-02-15 19:00 UTC)

<p>We cannot prevent you to instantiate module widgets but you should not do that, as they are not designed to work well when you create multiple instances. Also, a module widget has node selectors for all its inputs/outputs, so there would be always several node redundant node selectors when you integrate a module widget in your own module’s GUI.</p>
<p>If you want to reuse widgets from a module then use the same high-level widgets that are in the other module and use the other module’s logic. If you find that there is logic (algorithm, complex scene manipulations, etc.) in the other module’s <em>widget</em> that you would like to use then that other module has to be refactored so that all reusable logic is in its module <em>logic</em> class (which is designed to be reusable from other modules).</p>
<p>Also note that many features of Endoscopy module is already available in curve markups and soon Endoscopy module will be fully written to take advantage of that and remove duplication between these modules.</p>

---

## Post #3 by @timeanddoctor (2020-02-16 00:32 UTC)

<p>Thank you very much. Pros. Lassoan</p>
<p>What I am going to do is open the endoscopy and markups in one time by slicer’s python interactor. But when I click the mani windows of slicer, the window of endoscopy will run in background(hidden by slicer main window). Slicer seems to not detect the ‘widget’ of endoscopy was open as will as me?  So,some times,too many windows(all endoscopy windows) were open for me.</p>

---

## Post #4 by @lassoan (2020-02-16 04:45 UTC)

<p>I don’t understand what you are planning to do exactly but it seems quite complex and not how the modules are supposed to be used. Your module should have its own GUI (do not try to hijack other module’s GUI) and use other module’s logic. To implement GUI of your module, you can of course have a look at other module’s GUIs and use similar widgets but then copy only those widgets that are relevant for your workflow and with a layout that is optimal for your workflow.</p>

---
