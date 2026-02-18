# Unable to manually install extension to manual Slicer build

**Topic ID**: 19359
**Date**: 2021-08-25
**URL**: https://discourse.slicer.org/t/unable-to-manually-install-extension-to-manual-slicer-build/19359

---

## Post #1 by @jamesobutler (2021-08-25 15:42 UTC)

<p>I have built latest Slicer manually and have also built some Slicer extensions manually to install into the extension manager by ZIP.  I’m running into an issue where they are being detected as incorrect matching revision. Have I done something wrong?</p>
<p>I get the following message upon trying to install by ZIP<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ea1588fa6bccf13cbb86b37e86f44bd98fda04f.png" alt="image" data-base62-sha1="fMGcDxLs1iuIER7ucE0Ojm3Lamr" width="502" height="120"><br>
followed by<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/adf04ae26adba74fc3d7ecfefe712518fa1beef2.png" alt="image" data-base62-sha1="oOJqsm86us1MbVfAYrVqbAkzids" width="282" height="120"><br>
and then when observing the installed extensions tab<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/8141202c53bab56f7155f0292d543abc967bfae9.png" alt="image" data-base62-sha1="irr7JKMdi6h7I11cPETc1YOyojv" width="422" height="125"></p>
<p>When I query <code>slicer.app.revision</code> I get it appropriately as version 30133<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c04014da57a78ef97d928d5ed6ca4df712c7e152.png" alt="image" data-base62-sha1="rqIY1OtA7bCFQcboM8uph4NM9KW" width="299" height="87"></p>

---

## Post #2 by @jamesobutler (2021-08-25 18:25 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> This would seem related to some of your recent work with extensions.</p>

---

## Post #3 by @muratmaga (2021-08-25 18:46 UTC)

<p>I encountered the same using the official preview version from today, but manual extension installation method (due to this issue <a href="https://discourse.slicer.org/t/new-extension-manager-and-issues-with-corporate-certificates/19361" class="inline-onebox">New extension manager and issues with corporate certificates</a>)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae6cc31092a0824d2b0df74d6a652ad96bfa4cc2.png" data-download-href="/uploads/short-url/oT26hqsajEP24OiVhEeMk6v0PrY.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae6cc31092a0824d2b0df74d6a652ad96bfa4cc2_2_690x288.png" alt="image" data-base62-sha1="oT26hqsajEP24OiVhEeMk6v0PrY" width="690" height="288" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae6cc31092a0824d2b0df74d6a652ad96bfa4cc2_2_690x288.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae6cc31092a0824d2b0df74d6a652ad96bfa4cc2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae6cc31092a0824d2b0df74d6a652ad96bfa4cc2.png 2x" data-dominant-color="2A2A2A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">873×365 17.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @jamesobutler (2021-08-25 23:26 UTC)

<p>The error retrieving extension metadata is due to receiving 50 results (all the extensions) instead of just 1 for the extension of interest. Trying to figure out what is wrong with the query.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/5af0a09a8aa00640c196f82d8e88eb7b6a16ff9e/Base/QTCore/qSlicerExtensionsManagerModel.cxx#L1112-L1113">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/5af0a09a8aa00640c196f82d8e88eb7b6a16ff9e/Base/QTCore/qSlicerExtensionsManagerModel.cxx#L1112-L1113" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/5af0a09a8aa00640c196f82d8e88eb7b6a16ff9e/Base/QTCore/qSlicerExtensionsManagerModel.cxx#L1112-L1113" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/5af0a09a8aa00640c196f82d8e88eb7b6a16ff9e/Base/QTCore/qSlicerExtensionsManagerModel.cxx#L1112-L1113</a></h4>



  <pre class="onebox">    <code class="lang-cxx">
      <ol class="start lines" start="1112" style="counter-reset: li-counter 1111 ;">
          <li>// extension manager returned multiple results, this is not expected, do not use the results</li>
          <li>errorText = QString("expected 0 or 1 result, received %1").arg(results.count());</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @jamesobutler (2021-08-26 01:16 UTC)

<p>Commits in question include:</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/commit/109e79ce24a24fae7d053696b5eb46ebe193e1cf#diff-28a05eaf07fcf6d76c0acf5469b48e5c86f2c0f169d995f027e1f6be14debce0" class="inline-onebox" rel="noopener nofollow ugc">ENH: Update extensions manager to support Girder · Slicer/Slicer@109e79c · GitHub</a></li>
<li><a href="https://github.com/Slicer/Slicer/commit/489a919a321c7911dc49183745375269a5b99e9b#diff-28a05eaf07fcf6d76c0acf5469b48e5c86f2c0f169d995f027e1f6be14debce0" class="inline-onebox" rel="noopener nofollow ugc">ENH: Set default extensions manager ServerAPI to "Girder_v1" · Slicer/Slicer@489a919 · GitHub</a></li>
<li><a href="https://github.com/Slicer/Slicer/commit/5c7c2e4c1614167fbe96a23bd889897ad57066a1#diff-28a05eaf07fcf6d76c0acf5469b48e5c86f2c0f169d995f027e1f6be14debce0" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix loading of extension installed using "Girder_v1" serverAPI · Slicer/Slicer@5c7c2e4 · GitHub</a></li>
<li><a href="https://github.com/Slicer/Slicer/commit/57ce038ac3dc761d19906af5045ec18c953fd673#diff-28a05eaf07fcf6d76c0acf5469b48e5c86f2c0f169d995f027e1f6be14debce0" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix retrieval of extension metadata by name using "Girder_v1" se… · Slicer/Slicer@57ce038 · GitHub</a></li>
<li><a href="https://github.com/Slicer/Slicer/commit/1c71a320711e4a88fa7a443037e8cc4cd301aa69#diff-28a05eaf07fcf6d76c0acf5469b48e5c86f2c0f169d995f027e1f6be14debce0" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix extension compatibility check if installed using "Girder_v1"… · Slicer/Slicer@1c71a32 · GitHub</a></li>
<li><a href="https://github.com/Slicer/Slicer/commit/e074b36cd66aa986bc2974e69799b3a5cb38bb6c#diff-28a05eaf07fcf6d76c0acf5469b48e5c86f2c0f169d995f027e1f6be14debce0" class="inline-onebox" rel="noopener nofollow ugc">BUG: Ensure all Girder_v1 extension metadata are added to the model · Slicer/Slicer@e074b36 · GitHub</a></li>
<li><a href="https://github.com/Slicer/Slicer/commit/e2ea8afa61a4d4b0372f3650c7843c56b757a20c#diff-28a05eaf07fcf6d76c0acf5469b48e5c86f2c0f169d995f027e1f6be14debce0" class="inline-onebox" rel="noopener nofollow ugc">BUG: Ensure extensions installed using "Girder_v1" serverAPI are enabled · Slicer/Slicer@e2ea8af · GitHub</a></li>
</ul>

---

## Post #6 by @jamesobutler (2021-09-08 15:08 UTC)

<p>Any updates on this? I downloaded latest Slicer Preview and downloaded a corresponding extension from <a href="https://slicer-packages.kitware.com/" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/</a> and I’m still unable to manually install it using the extension manager.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b47cac2cdf358fcbf175eb0b0d9a352c8896ecf.png" alt="image" data-base62-sha1="d1vgl26OI81CypMgbINSf7bgNVJ" width="502" height="119"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d721add1c10ed3780ea241d8bf2d43e8ac5e99f.png" alt="image" data-base62-sha1="fCcvNSVQypvBGXkOG3gkUvfyuK3" width="268" height="119"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e889f2aac5f9b4a3170fb122e052aa69e924df6.png" alt="image" data-base62-sha1="8VcjsEF4SK0YBcwJigihdWzhPoO" width="397" height="195"></p>

---

## Post #7 by @lassoan (2021-09-08 15:16 UTC)

<p>We talked about this with <a class="mention" href="/u/jcfr">@jcfr</a> yesterday and he is expected to work on it this week. This is clearly a bug, so it may be useful to <a href="https://issues.slicer.org/">file a bug report</a> to ensure that it gets sufficient visibility.</p>

---

## Post #8 by @jamesobutler (2021-09-08 15:20 UTC)

<p>Should I file it under the Slicer repo or at <a href="https://github.com/KitwareMedical/slicer-extensions-webapp" rel="noopener nofollow ugc">https://github.com/KitwareMedical/slicer-extensions-webapp</a>? I’m not specifically sure if Slicer repo issue or the extensions server side.</p>

---

## Post #9 by @lassoan (2021-09-08 15:27 UTC)

<p>It is an issue in Slicer core.</p>

---

## Post #10 by @jamesobutler (2021-09-08 16:35 UTC)

<p>Now tracked at <a href="https://github.com/Slicer/Slicer/issues/5840" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/issues/5840</a></p>

---
