# Change site icon to easily distinguish Slicer wiki and Slicer discourse

**Topic ID**: 315
**Date**: 2017-05-15
**URL**: https://discourse.slicer.org/t/change-site-icon-to-easily-distinguish-slicer-wiki-and-slicer-discourse/315

---

## Post #1 by @lassoan (2017-05-15 20:28 UTC)

<p>When I have many tabs open in my browser then I cannot easily distinguish Slicer wiki and Slicer discourse tabs:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/dd1a3f983d7c1508d86928b67c80cf0fc99cf2f0.png" width="442" height="42"><br>
(the last two are Slicer discourse and Slicer wiki - they look the same)</p>
<p>Could we slightly change the site icon so that they show up a bit differently?</p>
<p>For example, add a small discourse icon in the corner: <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/6703bd5a3018f88af6947586d20ea19c03451881.png" width="24" height="22"></p>

---

## Post #2 by @lassoan (2017-05-16 14:46 UTC)

<p>I’ve made the small adjustment by modifying settings <a href="https://discourse.slicer.org/admin/site_settings/category/all_results?filter=favicon">here</a>. The old and new favicons are available on the <a href="https://discourse.slicer.org/t/assets-for-the-site-design/7/2">site assets page</a>.</p>

---

## Post #3 by @jcfr (2017-05-17 03:35 UTC)

<p>Checking using either chrome or firefox, the new favicon is not displayed. I think it is because an <code>.ico</code> file need to be uploaded instead of <code>.png</code></p>

---

## Post #4 by @jcfr (2017-05-17 03:44 UTC)

<p>I tried using an <code>*.ico</code> file without success. Also after reading the hint in the setting, I found <em>A favicon for your site, see <a href="http://en.wikipedia.org/wiki/Favicon">http://en.wikipedia.org/wiki/Favicon</a>, to work correctly over a CDN it must be a png</em></p>

---

## Post #5 by @jcfr (2017-05-17 03:45 UTC)

<p>Worth noting that Wikipedia indicates <em>such icon files can be 16×16, 32×32, 48×48, or 64×64 pixels in size</em></p>

---

## Post #6 by @lassoan (2017-05-17 03:48 UTC)

<p>In the settings page it is written:</p>
<blockquote>
<p>A favicon for your site, see <a href="http://en.wikipedia.org/wiki/Favicon" class="inline-onebox">Favicon - Wikipedia</a>, to work correctly over a CDN it must be a png</p>
</blockquote>
<p>Some browsers cache the favicon for a while. I would give it a few days/try clearing all browser caches to see if the icon gets updated then.</p>

---

## Post #7 by @jcfr (2017-05-17 03:54 UTC)

<p>After uploading a <code>64x64 / *.png</code> version of the icon, it now shows as expected.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/631fd47648004f8cc48d5cfdf946eee40fe84247.png" alt="image" data-base62-sha1="e8TsP113WmbOXIE25MpZ5SH43Ur" width="372" height="156"></p>

---
