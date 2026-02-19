---
topic_id: 35023
title: "Change Letter Size In Interface Messages"
date: 2024-03-22
url: https://discourse.slicer.org/t/35023
---

# Change letter size in interface messages

**Topic ID**: 35023
**Date**: 2024-03-22
**URL**: https://discourse.slicer.org/t/change-letter-size-in-interface-messages/35023

---

## Post #1 by @SANTIAGO_PENDON_MING (2024-03-22 14:17 UTC)

<p>Hi to everyone. Today I’m interested in interface configuration.</p>
<p>At this moment, the way I use to communicate info to the users is displaying text in the lower left corner using:</p>
<pre><code class="lang-auto">slicer.util.showStatusMessage("Editing completed")
</code></pre>
<p>And the result is:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29047df77c637fdb0d2dd2b91a7bdc306a989ce3.png" data-download-href="/uploads/short-url/5QRcqDnqYE5x1NHB6LEHo9SnNxp.png?dl=1" title="Captura de pantalla 2024-03-22 151448" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29047df77c637fdb0d2dd2b91a7bdc306a989ce3_2_690x373.png" alt="Captura de pantalla 2024-03-22 151448" data-base62-sha1="5QRcqDnqYE5x1NHB6LEHo9SnNxp" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29047df77c637fdb0d2dd2b91a7bdc306a989ce3_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29047df77c637fdb0d2dd2b91a7bdc306a989ce3_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29047df77c637fdb0d2dd2b91a7bdc306a989ce3_2_1380x746.png 2x" data-dominant-color="313957"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-03-22 151448</span><span class="informations">1404×759 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My goal is make this text bigger, or display it in other stage with a bigger letter size.</p>
<p>Any suggestion or way to display text info? (I want to avoid using Python terminal and also I prefer not to use pop-up windows for that.</p>
<p>Thanks a lot once again <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @pieper (2024-03-22 14:33 UTC)

<p>That’s a standard Qt element, so I’m sure you can configure it, but maybe not in Python.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://doc.qt.io/qt-5/qstatusbar.html#reformat">
  <header class="source">
      <img src="https://d33sqmjvzgs8hq.cloudfront.net/wp-content/themes/oneqt/assets/images/favicon.ico.gzip" class="site-icon" width="32" height="32">

      <a href="https://doc.qt.io/qt-5/qstatusbar.html#reformat" target="_blank" rel="noopener">doc.qt.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://doc.qt.io/qt-5/qstatusbar.html#reformat" target="_blank" rel="noopener">QStatusBar Class | Qt Widgets 6.6.3</a></h3>

  <p>The QStatusBar class provides a horizontal bar suitable for presenting status information.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>But you can also add widgets to the status bar, so adding a label with a bigger font should be easy.</p>

---

## Post #3 by @SANTIAGO_PENDON_MING (2024-03-25 09:36 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>. With your answer and some tries I finally achieve my goal. I will add to the post my code solution:</p>
<pre><code class="lang-auto"># Import modules
from __main__ import qt, slicer

# Create the message
message= "¡Hola desde Slicer 3D!"
label= qt.QLabel(message)

# Change the Font and Size:
etiqueta.setFont(qt.QFont('Times', 15))

# Use the Object statusBar()
barra_estado = slicer.util.mainWindow().statusBar()

# Add to the StatusBar the Label
status.addWidget(label)

# Reformat the StatusBar
status.reformat()
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6ad1952287b241883e3f34e189adbdeeb5428a93.png" data-download-href="/uploads/short-url/feXDHNO4Vk4EOpA7eitMTeBqdIT.png?dl=1" title="Captura de pantalla 2024-03-25 103550" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6ad1952287b241883e3f34e189adbdeeb5428a93_2_690x412.png" alt="Captura de pantalla 2024-03-25 103550" data-base62-sha1="feXDHNO4Vk4EOpA7eitMTeBqdIT" width="690" height="412" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6ad1952287b241883e3f34e189adbdeeb5428a93_2_690x412.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6ad1952287b241883e3f34e189adbdeeb5428a93_2_1035x618.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6ad1952287b241883e3f34e189adbdeeb5428a93_2_1380x824.png 2x" data-dominant-color="222226"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-03-25 103550</span><span class="informations">1916×1146 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks so much once again.</p>

---
