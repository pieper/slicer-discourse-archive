# Is MonaiLabel functional?

**Topic ID**: 19376
**Date**: 2021-08-26
**URL**: https://discourse.slicer.org/t/is-monailabel-functional/19376

---

## Post #1 by @muratmaga (2021-08-26 18:13 UTC)

<p>I am trying to use MonaiLabel on windows build from 6/28 (4.13.0-2021-06-28 r30015 / 1807944). Extension is installed, but when Slicer starts there is this error in Python window:</p>
<blockquote>
<p>RuntimeError: qSlicerScriptedLoadableModule::setPythonSource - Failed to load scripted loadable module: class client was not found in file C:/Users/amaga/AppData/Local/NA-MIC/Slicer 4.13.0-2021-06-28/NA-MIC/Extensions-30015/MONAILabel/lib/Slicer-4.13/qt-scripted-modules/client.py</p>
</blockquote>
<p>When I switch to the Monai module and when I type in the Monai server address, I get this:</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “C:/Users/amaga/AppData/Local/NA-MIC/Slicer 4.13.0-2021-06-28/NA-MIC/Extensions-30015/MONAILabel/lib/Slicer-4.13/qt-scripted-modules/MONAILabel.py”, line 667, in fetchInfo<br>
info = self.logic.info()<br>
File “C:/Users/amaga/AppData/Local/NA-MIC/Slicer 4.13.0-2021-06-28/NA-MIC/Extensions-30015/MONAILabel/lib/Slicer-4.13/qt-scripted-modules/MONAILabel.py”, line 1225, in info<br>
return MONAILabelClient(self.server_url, self.tmpdir).info()<br>
File “C:\Users\amaga\AppData\Local\NA-MIC\Slicer 4.13.0-2021-06-28\NA-MIC\Extensions-30015\MONAILabel\lib\Slicer-4.13\qt-scripted-modules\client.py”, line 26, in info<br>
status, response, _ = MONAILabelUtils.http_method(“GET”, self._server_url, selector)<br>
File “C:/Users/amaga/AppData/Local/NA-MIC/Slicer 4.13.0-2021-06-28/NA-MIC/Extensions-30015/MONAILabel/lib/Slicer-4.13/qt-scripted-modules/client.py”, line 158, in http_method<br>
conn = http.client.HTTPConnection(parsed.hostname, parsed.port)<br>
File “C:\Users\amaga\AppData\Local\NA-MIC\Slicer 4.13.0-2021-06-28\lib\Python\Lib\http\client.py”, line 849, in <strong>init</strong><br>
(self.host, self.port) = self._get_hostport(host, port)<br>
File “C:\Users\amaga\AppData\Local\NA-MIC\Slicer 4.13.0-2021-06-28\lib\Python\Lib\http\client.py”, line 881, in _get_hostport<br>
i = host.rfind(‘:’)<br>
AttributeError: ‘NoneType’ object has no attribute ‘rfind’</p>
</blockquote>
<p>Server is accessible through the web browser installed on the machine that’s running slicer:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d1842d0d4b8f0db439332cc1aa26b1f13bf5b5c.png" data-download-href="/uploads/short-url/hQDF5DuSi5c9Qynwabo6eDuqiPa.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d1842d0d4b8f0db439332cc1aa26b1f13bf5b5c_2_261x250.png" alt="image" data-base62-sha1="hQDF5DuSi5c9Qynwabo6eDuqiPa" width="261" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d1842d0d4b8f0db439332cc1aa26b1f13bf5b5c_2_261x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d1842d0d4b8f0db439332cc1aa26b1f13bf5b5c_2_391x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d1842d0d4b8f0db439332cc1aa26b1f13bf5b5c_2_522x500.png 2x" data-dominant-color="D6DADD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">765×732 28.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-08-27 01:39 UTC)

<p>This is a very, very old build for MONAILabel. There are dozens of commits every week. The <a href="https://github.com/Project-MONAI/MONAILabel/issues/263">client.py warning</a> and many other issues were fixed long time ago. Please try the latest (maximum 1-2 days old) version and <a href="https://github.com/Project-MONAI/MONAILabel/issues/">submit a bug report</a> if something is broken.</p>

---

## Post #3 by @muratmaga (2021-08-27 01:47 UTC)

<p>Good to know. At this point I can’t try a recent build due to these two issues;</p>
<aside class="quote quote-modified" data-post="5" data-topic="19359">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/unable-to-manually-install-extension-to-manual-slicer-build/19359/5">Unable to manually install extension to manual Slicer build</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Commits in question include: 

<a href="https://github.com/Slicer/Slicer/commit/109e79ce24a24fae7d053696b5eb46ebe193e1cf#diff-28a05eaf07fcf6d76c0acf5469b48e5c86f2c0f169d995f027e1f6be14debce0" class="inline-onebox" rel="noopener nofollow ugc">ENH: Update extensions manager to support Girder · Slicer/Slicer@109e79c · GitHub</a>
<a href="https://github.com/Slicer/Slicer/commit/489a919a321c7911dc49183745375269a5b99e9b#diff-28a05eaf07fcf6d76c0acf5469b48e5c86f2c0f169d995f027e1f6be14debce0" class="inline-onebox" rel="noopener nofollow ugc">ENH: Set default extensions manager ServerAPI to "Girder_v1" · Slicer/Slicer@489a919 · GitHub</a>
<a href="https://github.com/Slicer/Slicer/commit/5c7c2e4c1614167fbe96a23bd889897ad57066a1#diff-28a05eaf07fcf6d76c0acf5469b48e5c86f2c0f169d995f027e1f6be14debce0" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix loading of extension installed using "Girder_v1" serverAPI · Slicer/Slicer@5c7c2e4 · GitHub</a>
<a href="https://github.com/Slicer/Slicer/commit/57ce038ac3dc761d19906af5045ec18c953fd673#diff-28a05eaf07fcf6d76c0acf5469b48e5c86f2c0f169d995f027e1f6be14debce0" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix retrieval of extension metadata by name using "Girder_v1" se… · Slicer/Slicer@57ce038 · GitHub</a>
<a href="https://github.com/Slicer/Slicer/commit/1c71a320711e4a88fa7a443037e8cc4cd301aa69#diff-28a05eaf07fcf6d76c0acf5469b48e5c86f2c0f169d995f027e1f6be14debce0" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix extension compatibility check if installed using "Girder_v1"… · Slicer/Slicer@1…</a>
  </blockquote>
</aside>

<aside class="quote quote-modified" data-post="1" data-topic="19361">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-extension-manager-and-issues-with-corporate-certificates/19361">New extension manager and issues with corporate certificates</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Today I downloaded a new preview version, and tried to install MoniaLabel and SlicerMorph on my work computers, and encountered this error: 

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.example.com/Slicer/Extensions/BreastImplantAnalyzer.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over H…
  </blockquote>
</aside>


---

## Post #4 by @lassoan (2021-08-27 01:50 UTC)

<p>You can simply unzip the content of the extension package and add the loadable, scripted, and CLI module folders to additional module paths.</p>
<p>You can also use the extension manager from a mobile network or at home to download Slicer and install extensions, then copy it to a USB stick. Slicer Preview Releases are fully portable applications, so they run without any installation.</p>

---

## Post #5 by @muratmaga (2021-08-27 01:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="19376">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>nd CLI module folders to additional module paths.</p>
</blockquote>
</aside>
<p>OK. I forgot about that method of manually installing. Will try. Hopefully those extension manager issues will get fixed soon though…</p>

---

## Post #6 by @lassoan (2021-08-27 02:01 UTC)

<p>I think <a class="mention" href="/u/jcfr">@jcfr</a> will return next week and this will be probably quite high on his priority list.</p>

---

## Post #7 by @Fernando (2021-09-01 18:26 UTC)

<p>Pinging <a class="mention" href="/u/diazandr3s">@diazandr3s</a> so he’s aware of this thread.</p>

---

## Post #8 by @diazandr3s (2021-09-02 09:36 UTC)

<p><a class="mention" href="/u/fernando">@Fernando</a> many thanks for the ping! As Andras commented, MONAI Label is under continuous development. Three days is almost history for this project <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=10" title=":smiley:" class="emoji" alt=":smiley:"></p>

---
