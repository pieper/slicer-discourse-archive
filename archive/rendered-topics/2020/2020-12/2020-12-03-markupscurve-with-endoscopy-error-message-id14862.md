---
topic_id: 14862
title: "Markupscurve With Endoscopy Error Message"
date: 2020-12-03
url: https://discourse.slicer.org/t/14862
---

# MarkupsCurve with Endoscopy error message

**Topic ID**: 14862
**Date**: 2020-12-03
**URL**: https://discourse.slicer.org/t/markupscurve-with-endoscopy-error-message/14862

---

## Post #1 by @torquil (2020-12-03 13:07 UTC)

<p>In the Endoscopy module it is possible to choose a MarkupsCurve as the “Input Fiducials”. However, nothing happens when clicking on “Create path”. In addition, I have seven cameras with the same name, so I’m not really sure which one to use. Anyway, when I click on “Create path”, the Python console shows the following:</p>
<pre><code>Traceback (most recent call last):
  File "/home/torquil/usr/slicer/lib/Slicer-4.13/qt-scripted-modules/Endoscopy.py", line 222, in onCreatePathButtonClicked
    result = EndoscopyComputePath(fiducialsNode)
  File "/home/torquil/usr/slicer/lib/Slicer-4.13/qt-scripted-modules/Endoscopy.py", line 394, in __init__
    self.calculatePath()
  File "/home/torquil/usr/slicer/lib/Slicer-4.13/qt-scripted-modules/Endoscopy.py", line 414, in calculatePath
    t, p, remainder = self.step(segment, t, remainder)
TypeError: 'NoneType' object is not iterable
</code></pre>
<p>Btw, I’m using 3D Slicer 4.13.0-2020-11-24 r29485 / 5a52b58 on Linux.</p>

---

## Post #2 by @lassoan (2020-12-03 20:13 UTC)

<p>I’ve pushed a <a href="https://github.com/Slicer/Slicer/commit/8bf393e4fee2f8aa3748f73279848d98637ded13">fix</a> please try again with the Slicer Preview Release tomorrow.</p>

---

## Post #3 by @torquil (2020-12-03 23:31 UTC)

<p>Hi!</p>
<p>That’s great! I tried it by copying Endoscopy.py to my existing installation. Slicer now generates an endoscopy flight from a markups curve. However, would it be possible to set the “dl”-parameter manually? I found that by reducing it from dl = 0.5 to dl = 0.1 (on line 354 in Endoscopy.py after your modifications) I could achieve the smoothness of the endoscopy flight that I wanted. Could the “dl”-parameter be user adjustable in the Endoscopy module?</p>
<p>Best regards,<br>
Torquil Sørensen</p>

---

## Post #4 by @lassoan (2020-12-04 00:40 UTC)

<p>Endoscopy is a very simple Python scripted module and so you can a <code>slicer.qMRMLSliderWidget()</code> to control the sampling distance very easily. If it works well then send us a pull request so that we can add it to Slicer core. Thank you!</p>

---

## Post #6 by @yee (2020-12-06 02:05 UTC)

<p>Hello, I also have this problem, but I can’t download  Slicer Preview Release , which display the " 0 kb" in the download directory.</p>

---

## Post #7 by @lassoan (2020-12-06 04:18 UTC)

<p>I can confirm that Windows and MacOS packages have 0 length. <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> could you have a look?</p>
<p>Until it is fixed, you can download preview release from a few days ago from this link:</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://download.slicer.org/static/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://download.slicer.org/?date=2020-12-03" target="_blank" rel="noopener">download.slicer.org</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://download.slicer.org/?date=2020-12-03" target="_blank" rel="noopener">3D Slicer Download</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #8 by @yee (2020-12-06 05:42 UTC)

<p>Can I use Endoscopy to generate open markup curve from markup nodes? But the Endoscopy report this error: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c5da14fd1badec97c87b7af9f401356feb92d1d.png" data-download-href="/uploads/short-url/mjh5orXwZ4lztViC9WbGJ1y5lMh.png?dl=1" title="{E54W@1HD5FZ~OJ6$KX74P7" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c5da14fd1badec97c87b7af9f401356feb92d1d_2_690x359.png" alt="{E54W@1HD5FZ~OJ6$KX74P7" data-base62-sha1="mjh5orXwZ4lztViC9WbGJ1y5lMh" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c5da14fd1badec97c87b7af9f401356feb92d1d_2_690x359.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c5da14fd1badec97c87b7af9f401356feb92d1d_2_1035x538.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c5da14fd1badec97c87b7af9f401356feb92d1d_2_1380x718.png 2x" data-dominant-color="BAB7BB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">{E54W@1HD5FZ~OJ6$KX74P7</span><span class="informations">1909×995 254 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you !</p>

---

## Post #9 by @lassoan (2020-12-06 05:51 UTC)

<p>The error is fixed in latest Slicer Preview Release but packaging seems to be broken right now, so you can download a preview release from a few days ago and overwrite Endoscopy.py with the <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/Endoscopy/Endoscopy.py">latest version</a>.</p>

---

## Post #10 by @Sam_Horvath (2020-12-07 16:14 UTC)

<p>Looking into issues with the server:</p>
<aside class="quote" data-post="1" data-topic="14914">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/extension-service-is-down/14914">Extension service is down</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    It looks like midas is half-broken.  The metadata can be retrieved but the downloaded files are empty. 
Can someone reboot it? 
"Retrieving extension metadata [ extensionId: 405842]"
"Downloading extension [ itemId: 548410]"
"Archive /tmp/29402-linux-amd64-WindowLevelEffect-git39baeae-2016-07-22.tar.gz.mFmokN doesn't contain any files !"
Uncaught SyntaxError: missing ) after argument list
  </blockquote>
</aside>


---

## Post #11 by @lassoan (2020-12-07 16:16 UTC)

<p>Can we switch to the new server? It would be a better investment of your time to get the new server up and running instead of trying to prop up the old one.</p>

---
