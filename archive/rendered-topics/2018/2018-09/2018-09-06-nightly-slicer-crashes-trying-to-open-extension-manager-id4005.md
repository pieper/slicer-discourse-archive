---
topic_id: 4005
title: "Nightly Slicer Crashes Trying To Open Extension Manager"
date: 2018-09-06
url: https://discourse.slicer.org/t/4005
---

# Nightly Slicer crashes trying to open Extension Manager

**Topic ID**: 4005
**Date**: 2018-09-06
**URL**: https://discourse.slicer.org/t/nightly-slicer-crashes-trying-to-open-extension-manager/4005

---

## Post #1 by @fedorov (2018-09-06 16:00 UTC)

<p>I downloaded today’s nightly for Mac. Every time I click “Extension manager” button, I get a crash.</p>
<p>Crash stack is here: <a href="https://gist.github.com/fedorov/b539889d139d986410acc23370a5c0f2">https://gist.github.com/fedorov/b539889d139d986410acc23370a5c0f2</a> (unable to include in the message as it exceeds the maximum message size).</p>

---

## Post #2 by @pieper (2018-09-06 20:04 UTC)

<p>I don’t have that issue on my mac - this is a fresh download of the current nightly:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b37af45e06e87977009086124a6c9e7e30fb225a.png" data-download-href="/uploads/short-url/pBKTyLbhcsfhw00OsNxdro607Q6.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b37af45e06e87977009086124a6c9e7e30fb225a_2_690x389.png" alt="image" data-base62-sha1="pBKTyLbhcsfhw00OsNxdro607Q6" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b37af45e06e87977009086124a6c9e7e30fb225a_2_690x389.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b37af45e06e87977009086124a6c9e7e30fb225a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b37af45e06e87977009086124a6c9e7e30fb225a.png 2x" data-dominant-color="D3D4DB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">830×468 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2018-09-07 03:28 UTC)

<p>Does it still crash if you disconnect from internet?<br>
Does it crash if you remove Slicer.ini files?</p>
<p>Poor quality of QtWebEngine-based extension manager is quite annoying. In addition to crashes on Mac (see above and <a href="https://issues.slicer.org/view.php?id=4550">here</a>), the extension manager is extremely slow (takes 10-20 seconds to start or install an extension, without giving any feedback to the user about what’s happening). It would be great if somebody could check if there is something wrong with how we use QtWebEngine or it is that bad by itself.</p>

---

## Post #4 by @fedorov (2018-09-07 14:15 UTC)

<p>I don’t know how this works. It was crashing every single time when I tried yesterday on Partners network. I then tried on a different network later in the day, and it was working. Today it is working on the Partners network.</p>
<p>This is disturbing. Imagine this starts happening in a training session. I am assuming there is no reliable workaround for this, since sounds like no one exactly knows what causes this behavior. I guess at minimum it might be helpful to allow disabling auto-update of extensions via a command line switch.</p>

---

## Post #5 by @pieper (2018-09-07 14:56 UTC)

<p>We are still using Qt 5.10, but 5.11 is out and the webengine code has been updated.  It would be good to see if this addresses any of the reproducible issues (slowness) and maybe addresses the crash as well.</p>
<aside class="quote no-group" data-username="fedorov" data-post="4" data-topic="4005">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I guess at minimum it might be helpful to allow disabling auto-update of extensions via a command line switch.</p>
</blockquote>
</aside>
<p>Yes, good idea.</p>

---

## Post #6 by @ihnorton (2018-09-07 15:42 UTC)

<p>FWIW I used the extension manager with that build on two different macs yesterday, no problems.</p>

---

## Post #7 by @lassoan (2018-09-08 05:15 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="4" data-topic="4005">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I guess at minimum it might be helpful to allow disabling auto-update of extensions via a command line switch.</p>
</blockquote>
</aside>
<p>We could automatically turn off extension auto-update when there is a crash. We already have such a mechanism for Python debugger’s auto-connect feature. All we need to do is temporarily turn off extension auto-update in the application settings just before starting up the extension manager and restoring the previous state when the extension manager is successfully displayed. This way, if there is a crash when the extension manager is started, auto-update would remain turned off in the settings.</p>

---

## Post #8 by @jcfr (2018-10-16 07:15 UTC)

<h3>1) startup crash, and automatic install of extension at startup time (issue 4550)</h3>
<p>To follow up on this, while working on <a href="https://issues.slicer.org/view.php?id=4550">issue 4550</a>, I noticed that since commit r26960 (ENH: Speedup app startup time by lazily instantiating extension dialog), the extension dialog is lazily instantiated.</p>
<p>This means that that extension are <strong>NOT</strong> automatically updated at startup time (for details see this issue note <a href="https://issues.slicer.org/view.php?id=4550#c16124">4550#c16124</a>)</p>
<p>The crash reported at startup time does <strong>NOT</strong> make use of WebEngine, instead it is most likely an issue following the call to <code>qSlicerExtensionsManagerModelPrivate::retrieveExtensionMetadata</code>.</p>
<p>As outlined in the report, I tried few things on macOS, using different version of Qt, connecting/disconnecting internet … but as not able to reproduce it.</p>
<p>I am wondering if this could be related to some network specific settings (proxy, VPN, … ?)</p>
<h3>2) Crash when opening the extension manager (issue 4635)</h3>
<p>This is the issue reported by <a class="mention" href="/u/fedorov">@fedorov</a>, it basically crashes when opening the extensions manager . This is now tracked by <a href="https://issues.slicer.org/view.php?id=4635">issue 4635</a></p>
<p>While, I don’t know if it will alleviate this particular problem, we recently improved the <code>qSlicerWebWidget</code> so that it uses only one WebEngineProfile object and avoid race condition managing the webengine cache. see <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27480">r27480</a></p>

---

## Post #9 by @fedorov (2018-10-16 14:01 UTC)

<p>FWIW, I just tried today on Partners network, and it works. In the meantime, I also updated my OS to the latest Mojave. Slicer looks different (better!), but I don’t know if it had any other effects. Also seems to start slower, but I didn’t investigate.</p>

---

## Post #10 by @jcfr (2018-10-16 20:39 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> Thanks for the update.</p>
<p>Since the auto-update functionality was non-functional, it has been disabled in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27494">r27494</a>. We can revisit the current approach after the release (this is tracked by <a href="https://issues.slicer.org/view.php?id=4642">issue 4642</a>)</p>
<p>Also worth noting that Qt 5.13 will integrate a fix preventing error message like <code>ERROR:nss_ocsp.cc(614)] No URLRequestContext for NSS HTTP handler. host: ocsp.digicert.com</code>. See <a href="https://issues.slicer.org/view.php?id=4639">issue 4639</a> for more details.</p>

---

## Post #11 by @fedorov (2018-10-16 21:07 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="10" data-topic="4005">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Since the auto-update functionality was non-functional, it has been disabled in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27494">r27494</a></p>
</blockquote>
</aside>
<p>for the sake of completeness, the version that I tested today was r27399</p>

---
