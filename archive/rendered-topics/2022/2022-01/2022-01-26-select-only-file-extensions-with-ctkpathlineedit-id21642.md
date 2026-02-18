# Select only file extensions with ctkPathLineEdit

**Topic ID**: 21642
**Date**: 2022-01-26
**URL**: https://discourse.slicer.org/t/select-only-file-extensions-with-ctkpathlineedit/21642

---

## Post #1 by @kleingeo (2022-01-26 19:34 UTC)

<p>I’m writing a module where I need to load a csv file. I am currently using <code>ctkPathLineEdit</code> to open a file selection dialog box. Is there a way to modify <code>ctkPathLineEdit</code> to only accept files with specific file extensions?</p>

---

## Post #2 by @lassoan (2022-01-27 03:08 UTC)

<p>You can specify name filters in the <code>nameFilters</code> property of the <code>ctkPathLineEdit</code> widget:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee329e8b94deb50fec328a62f1ba2fc4c2ef1a20.png" data-download-href="/uploads/short-url/xZc5xtApnqWgsdfriM9rHB2VMGY.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee329e8b94deb50fec328a62f1ba2fc4c2ef1a20_2_690x440.png" alt="image" data-base62-sha1="xZc5xtApnqWgsdfriM9rHB2VMGY" width="690" height="440" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee329e8b94deb50fec328a62f1ba2fc4c2ef1a20_2_690x440.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee329e8b94deb50fec328a62f1ba2fc4c2ef1a20_2_1035x660.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee329e8b94deb50fec328a62f1ba2fc4c2ef1a20_2_1380x880.png 2x" data-dominant-color="DCDEDB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1441 263 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @kleingeo (2022-01-27 03:25 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="21642">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code>ctkPathLineEdit</code></p>
</blockquote>
</aside>
<p>Thannks, this was all I needed.</p>
<pre data-code-wrap="python"><code class="lang-python">self.dataframePath = ctk.ctkPathLineEdit()
self.dataframePath.settingKey = 'measurementFile'
self.dataframePath.filters = ctk.ctkPathLineEdit.Files
self.dataframePath.nameFilters = ['*.csv']
</code></pre>

---
