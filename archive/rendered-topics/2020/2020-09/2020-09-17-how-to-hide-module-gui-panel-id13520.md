---
topic_id: 13520
title: "How To Hide Module Gui Panel"
date: 2020-09-17
url: https://discourse.slicer.org/t/13520
---

# How to hide module GUI Panel?

**Topic ID**: 13520
**Date**: 2020-09-17
**URL**: https://discourse.slicer.org/t/how-to-hide-module-gui-panel/13520

---

## Post #1 by @Chintha_Siva_Prasad (2020-09-17 10:06 UTC)

<p>How can I hide the module GUI panel?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53317775f9d60037f7a011a01597f99127b80d2d.png" data-download-href="/uploads/short-url/bRXBVVl1CHx4ng5l8D4KKcmkrFj.png?dl=1" title="Screenshot from 2020-09-17 15-35-31" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53317775f9d60037f7a011a01597f99127b80d2d_2_690x387.png" alt="Screenshot from 2020-09-17 15-35-31" data-base62-sha1="bRXBVVl1CHx4ng5l8D4KKcmkrFj" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53317775f9d60037f7a011a01597f99127b80d2d_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53317775f9d60037f7a011a01597f99127b80d2d_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53317775f9d60037f7a011a01597f99127b80d2d.png 2x" data-dominant-color="8C8C9A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-09-17 15-35-31</span><span class="informations">1366×768 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I was able to hide all the bars but can’t hide the GUI with this welcome label on the left.</p>

---

## Post #2 by @lassoan (2020-09-17 11:35 UTC)

<p>Usually we keep the module panel displayed, showing a custom module GUI, but you can hide it entirely very easily:</p>
<pre><code class="lang-python">mainWindow().findChild('QDockWidget','PanelDockWidget').hide()
</code></pre>

---
