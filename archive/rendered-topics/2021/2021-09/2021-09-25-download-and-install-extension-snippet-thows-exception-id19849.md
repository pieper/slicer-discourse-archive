# "Download and install extension" snippet thows exception

**Topic ID**: 19849
**Date**: 2021-09-25
**URL**: https://discourse.slicer.org/t/download-and-install-extension-snippet-thows-exception/19849

---

## Post #1 by @rbumm (2021-09-25 10:26 UTC)

<p>Windows<br>
Slicer 4.13</p>
<p>The script repository snippet “<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#download-and-install-extension" rel="noopener nofollow ugc">Download and install an extension</a>”<br>
throws a “Key error: ‘item_id’” exception when used in Slicer 4.13</p>
<p>Has anything changed ?<br>
Thank you.</p>

---

## Post #3 by @jcfr (2021-09-25 16:33 UTC)

<p>Thanks for the report <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="rbumm" data-post="1" data-topic="19849">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Has anything changed ?</p>
</blockquote>
</aside>
<p>Indeed, we updated the infrastructure and some the API details changed.</p>
<p>For reference, see <a href="https://discourse.slicer.org/t/downloading-extensions-for-older-releases/19256" class="inline-onebox">Downloading extensions for older releases</a></p>
<p>Waiting we update the documentation and fix the legacy server to support this snippet, when using Slicer 4.13, you could do this:</p>
<pre data-code-wrap="diff"><code class="lang-diff">extensionName = 'SlicerIGT'
em = slicer.app.extensionsManagerModel()
if not em.isExtensionInstalled(extensionName):
  extensionMetaData = em.retrieveExtensionMetadataByName(extensionName)
-   url = em.serverUrl().toString()+'/download/item/'+extensionMetaData['item_id']
-   extensionPackageFilename = slicer.app.temporaryPath+'/'+extensionMetaData['_id']
+   url = em.serverUrl().toString() + '/download?items='+extensionMetaData['_id']
+   extensionPackageFilename = slicer.app.temporaryPath+'/'+extensionMetaData['_id']
  slicer.util.downloadFile(url, extensionPackageFilename)
  em.installExtension(extensionPackageFilename)
  slicer.util.restart()
</code></pre>
<p>For convenience, here is the full snippet for easy copy-paste:</p>
<pre data-code-wrap="python"><code class="lang-python">extensionName = 'SlicerIGT'
em = slicer.app.extensionsManagerModel()
if not em.isExtensionInstalled(extensionName):
  extensionMetaData = em.retrieveExtensionMetadataByName(extensionName)
  url = em.serverUrl().toString() + '/download?items='+extensionMetaData['_id']
  extensionPackageFilename = slicer.app.temporaryPath+'/'+extensionMetaData['_id']
  slicer.util.downloadFile(url, extensionPackageFilename)
  em.installExtension(extensionPackageFilename)
  slicer.util.restart()
</code></pre>

---

## Post #4 by @jcfr (2021-09-25 16:39 UTC)

<blockquote>
<p>Waiting we […] fix the legacy server</p>
</blockquote>
<p>Issue is now tracked in</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/KitwareMedical/slicer-extensions-legacy-webapp/issues/2">
  <header class="source">

      <a href="https://github.com/KitwareMedical/slicer-extensions-legacy-webapp/issues/2" target="_blank" rel="noopener">github.com/KitwareMedical/slicer-extensions-legacy-webapp</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/KitwareMedical/slicer-extensions-legacy-webapp/issues/2" target="_blank" rel="noopener">Add legacy route to support download python snippet</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-09-25" data-time="16:38:53" data-timezone="UTC">04:38PM - 25 Sep 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When using Slicer  4.13, the following snippet is expected to work:


```pyth<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">on
extensionName = 'SlicerIGT'
em = slicer.app.extensionsManagerModel()
if not em.isExtensionInstalled(extensionName):
  extensionMetaData = em.retrieveExtensionMetadataByName(extensionName)
  url = em.serverUrl().toString()+'/download/item/'+extensionMetaData['item_id']
  extensionPackageFilename = slicer.app.temporaryPath+'/'+extensionMetaData['md5']
  slicer.util.downloadFile(url, extensionPackageFilename)
  em.installExtension(extensionPackageFilename)
  slicer.util.restart()
```

For reference, see https://discourse.slicer.org/t/download-and-install-extension-snippet-thows-exception/19849

Changes to implement:
* Add route `/download/item/&lt;id&gt;`
* In  addition of `_id`, add `item_id` to the payload
* Fill  `md5` field .... this should probably be done only if this legacy route is used as it is "compute intense", or we could simply compute the hash of `&lt;package name&gt;`</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @rbumm (2021-09-25 18:44 UTC)

<blockquote>
<p>Waiting we update the documentation and fix the legacy server to support this snippet, when using Slicer 4.13, you could do this:</p>
</blockquote>
<p>Thank you <a class="mention" href="/u/jcfr">@jcfr</a> .</p>
<p>I tested the new snippet in 4.13.0-2021-09-11 r30174 / 0db2e6e but got:</p>
<p>urllib.error.HTTPError: HTTP Error 404: Not Found</p>
<p>Failed to download file from <a href="https://slicer-packages.kitware.com/download?items=613dbbc4342a877cb3bf8bd4">https://slicer-packages.kitware.com/download?items=613dbbc4342a877cb3bf8bd4</a></p>
<p>Any ideas ?</p>

---

## Post #6 by @jcfr (2021-09-25 19:04 UTC)

<p>I initially thought this was for the latest stable release, for the preview build, you could do that:</p>
<p>Replace <code>em.serverUrl().toString()</code> with `“<a href="https://slicer.kitware.com/midas3/">https://slicer.kitware.com/midas3/</a>”’</p>

---

## Post #7 by @rbumm (2021-09-25 19:46 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="6" data-topic="19849">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>“<a href="https://slicer.kitware.com/midas3/%E2%80%9D">https://slicer.kitware.com/midas3/”</a></p>
</blockquote>
</aside>
<p>This seems to work. Thank you</p>

---

## Post #8 by @rbumm (2021-09-26 07:14 UTC)

<p>Unfortunately, it is not quite working yet.</p>
<p>If I use this code in 4.13:</p>
<pre><code class="lang-auto">        extensionName = 'SlicerIGT'
        em = slicer.app.extensionsManagerModel()
        if not em.isExtensionInstalled(extensionName):
          extensionMetaData = em.retrieveExtensionMetadataByName(extensionName)
          url = "https://slicer.kitware.com/midas3" + '/download?items='+extensionMetaData['_id']
          extensionPackageFilename = slicer.app.temporaryPath+'/'+extensionMetaData['_id']
          slicer.util.downloadFile(url, extensionPackageFilename)
          em.installExtension(extensionPackageFilename)
          slicer.util.restart()

</code></pre>
<p>there is no error message or exception, but the extension that is installed seems not to be the right version:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c82b967599184b14f2f7b333d83d64855c17a89.png" alt="image" data-base62-sha1="ftVDOz1VBomSGMN28vc3IYt4EOt" width="360" height="98"></p>
<p>If I install SlicerIGT from the extension manager I seem to get the correct version:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c507b64c0b529a14764ea839e6c5ed12ec917360.png" alt="image" data-base62-sha1="s70AfRvTRhKXvE7c5MMNLhKvhNS" width="378" height="77"></p>

---

## Post #9 by @rbumm (2021-09-30 15:10 UTC)

<p>Obviously, this URL<br>
<a href="https://slicer.kitware.com/midas3/download?items=613dbbc4342a877cb3bf8bd4">https://slicer.kitware.com/midas3/download?items=613dbbc4342a877cb3bf8bd4</a><br>
downloads SlicerIGT from the extension server which is no longer active in 4.13.<br>
That is why the extension is older and shows outdated in 4.13.</p>
<p>But what would be the download URL to be used from 4.13 and to get the latest extension version?</p>

---

## Post #10 by @lassoan (2021-09-30 16:40 UTC)

<p>To simplify things, here is a script that works without any changes in both Slicer-4.11 and Slicer-4.13:</p>
<pre><code class="lang-python">extensionName = 'SlicerIGT'
em = slicer.app.extensionsManagerModel()
if not em.isExtensionInstalled(extensionName):
    extensionMetaData = em.retrieveExtensionMetadataByName(extensionName)
    if slicer.app.majorVersion*100+slicer.app.minorVersion &lt; 413:
        # Slicer-4.11
        itemId = extensionMetaData['item_id']
        url = f"{em.serverUrl().toString()}/download?items={itemId}"
    else:
        # Slicer-4.13
        itemId = extensionMetaData['_id']
        url = f"{em.serverUrl().toString()}/api/v1/item/{itemId}/download"
    extensionPackageFilename = slicer.app.temporaryPath+'/'+itemId
    slicer.util.downloadFile(url, extensionPackageFilename)
    em.installExtension(extensionPackageFilename)
    slicer.util.restart()
</code></pre>

---

## Post #11 by @rbumm (2021-09-30 17:37 UTC)

<p>Thanks, but unfortunately this still loads an outdated version of the extension into 4.13:</p>
<pre><code class="lang-auto">Downloading from
  https://slicer-packages.kitware.com/api/v1/item/613dbbc4342a877cb3bf8bd4/download
as file
  C:/Users/Rudolf/AppData/Local/Temp/Slicer/613dbbc4342a877cb3bf8bd4
It may take a few minutes...
</code></pre>
<p>but result is:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6eb63afb0f927ed3e51ba5e649187c8d8931d579.png" alt="image" data-base62-sha1="fNoWOhYGC77kQzVMyFoIWFIndod" width="372" height="94"></p>

---

## Post #12 by @lassoan (2021-09-30 17:43 UTC)

<p>30174 was some random nightly build some time ago. Please use latest Slicer Stable Release or latest Slicer Preview Release and let us know if you have problems with any of those.</p>

---

## Post #13 by @jamesobutler (2021-09-30 17:43 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> You’re likely not going to be able to stay on an older version of Slicer 4.13 from the early period of the extension manager transition where some fixes were still being worked out on the Slicer side. Including <a href="https://github.com/Slicer/Slicer/issues/5840" class="inline-onebox" rel="noopener nofollow ugc">Unable to manually install extension with ExtensionsManager · Issue #5840 · Slicer/Slicer · GitHub</a>.</p>

---

## Post #14 by @rbumm (2021-09-30 18:05 UTC)

<p>Thank you.<br>
The script now works with r30272 (preview) as well as the latest stable release.</p>

---
