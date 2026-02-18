# Downloading extensions for older releases

**Topic ID**: 19256
**Date**: 2021-08-30
**URL**: https://discourse.slicer.org/t/downloading-extensions-for-older-releases/19256

---

## Post #1 by @Sam_Horvath (2021-08-30 12:58 UTC)

<p>Due to the recent transition to the updated Extension Manager and Data Store infrastructure, when using Slicer-4.11 (or older) version, users will need to manually download and install extensions from the new extension server, and download data sets from an alternative server instead of using the Data Store module. Rationale for the transition can be found <a href="https://discourse.slicer.org/t/upcoming-downtime-for-download-slicer-org-and-extension-manager-due-to-package-server-transition/17444">here</a>.  We anticipate that this will be a temporary measure will the transition is finalized.</p>
<p>Thank you for your patience!  Please do not hesitate to reach out here on Discourse if you have questions or need assistance with extension installation.</p>
<p>– Slicer Dev Team</p>
<h2><a name="p-64809-download-and-install-extensions-1" class="anchor" href="#p-64809-download-and-install-extensions-1" aria-label="Heading link"></a>Download and install extensions</h2>
<ol>
<li>Go to the <a href="https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/5f4474d0e1d8c75dfc705482">Slicer Packages server</a></li>
<li>Select your release version</li>
<li>Find the extension of interest in that releases extensions folder</li>
<li>Click the download icon to download the extension package</li>
<li>Follow the <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#install-downloaded-extension-packages">instructions</a> for manually installing the extension</li>
<li>The extension may have dependencies. Check the corresponding .s4ext file in <a href="https://github.com/Slicer/ExtensionsIndex">the extension index</a> to see what other extensions may need to be installed.</li>
</ol>
<h2><a name="p-64809-download-data-sets-that-were-previously-hosted-on-the-datastore-2" class="anchor" href="#p-64809-download-data-sets-that-were-previously-hosted-on-the-datastore-2" aria-label="Heading link"></a>Download data sets that were previously hosted on the DataStore</h2>
<p>If you are looking for data previously accessible via the Data Store module (hosted on the DataStore server), it can be found <strong><a href="https://github.com/Slicer/slicer.kitware.com-midas3-archive#readme">here</a></strong>.</p>

---

## Post #2 by @jamesobutler (2021-08-30 13:46 UTC)

<p>Does this work only for the already released “Stable” versions and any Slicer “Preview” releases prior to the transition to the updated Extension Manager infrastructure? Date?</p>
<p>I downloaded Slicer 2021-08-24 revision <a href="https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/6125c4e7342a877cb3b8be76" rel="noopener nofollow ugc">30133</a> from the Applications/packages/Slicer/draft/30133 directory and then download the <a href="https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/6125cd7c342a877cb3b8bede" rel="noopener nofollow ugc">SlicerDebuggingTools</a> extension in the  Applications/packages/Slicer/draft/30133/extensions directory. I then installed Slicer and then followed the instructions to manually install the extension. Upon doing so I get the same results as I posted about at <a href="https://discourse.slicer.org/t/unable-to-manually-install-extension-to-manual-slicer-build/19359" class="inline-onebox">Unable to manually install extension to manual Slicer build</a>.</p>

---

## Post #3 by @Sam_Horvath (2021-08-30 14:06 UTC)

<p>Yes, these instructions are intended for the older Releases / Previews that use the old extension manager infrastructure.  The bug you encountered affects the new versions, and will be fixed.</p>
<p>To give some context, this post was created as a landing page for anyone attempting to reach the old extension manager site.  It has been made public at this time because the old server is to be shut off today.</p>

---

## Post #4 by @muratmaga (2021-09-02 04:01 UTC)

<p>I am a little bit confused with this message. Does this mean that current stable will no longer receive updates from new extension server. Or once the new extension infrastructure is in place, everything will be the same as before (for stable and older versions)?</p>
<p>If this is indeed temporary, I would suggest adding the <strong>temporary</strong> to the section below.</p>
<aside class="quote no-group quote-modified" data-username="Sam_Horvath" data-post="1" data-topic="19256">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar"> Sam_Horvath:</div>
<blockquote>
<p>older Slicer releases will need to manually download and install extensions from the new extension server</p>
</blockquote>
</aside>

---

## Post #5 by @lassoan (2021-09-02 04:59 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="19256">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Does this mean that current stable will no longer receive updates from new extension server.</p>
</blockquote>
</aside>
<p>We still build and upload releases for the Slicer-4.11, but that cannot download it from the new extension server and you need to download and install the packages manually. Slicer-4.13 and above can download and install extensions from the Extensions manager as usual.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="19256">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>If this is indeed temporary,</p>
</blockquote>
</aside>
<p>Yes, it is temporary. We’ll create a new stable release within 1-2 weeks and then both the latest stable (Slicer-4.14) and latest preview (Slicer-4.15) will be use the Extensions manager as usual.</p>

---

## Post #6 by @jcfr (2021-09-10 07:53 UTC)

<h2><a name="p-66000-updates-1" class="anchor" href="#p-66000-updates-1" aria-label="Heading link"></a>Updates</h2>
<blockquote>
<p>Download and install extensions</p>
</blockquote>
<p>Older release of Slicer can now browse and install extensions directly from the application.</p>
<p>For more details, read about the <code>Slicer legacy extensions catalog</code> at <a href="https://github.com/KitwareMedical/slicer-extensions-legacy-webapp#readme">KitwareMedical/slicer-extensions-legacy-webapp</a></p>
<blockquote>
<p>Does this mean that current stable will no longer receive updates from new extension server.</p>
</blockquote>
<p>To clarify, updated extension associated with the current stable release are uploaded and available to the user.</p>

---

## Post #7 by @muratmaga (2021-09-10 16:25 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>I just tried this with the stable on windows and while I can indeed install the extensions, it throws this error</p>
<pre><code class="lang-auto">
"Downloading extension [ itemId: 60ae2680ae4540bf6a89dc81]"

"Error retrieving extension metadata: amd64, win, MONAILabel, 29738 ({2d46a981-d88e-45d3-bbc0-004d69568701}: 401: Error transferring http://slicer.kitware.com/midas3/api/json?arch=amd64&amp;os=win&amp;productname=MONAILabel&amp;slicer_revision=29738&amp;method=midas.slicerpackages.extension.list - server replied: INTERNAL SERVER ERROR)"

"Installed extension IntensitySegmenter (60ae2680ae4540bf6a89dc81) revision ace1890"
</code></pre>
<p>But more concerning is the update extension behavior. When I click on update button, it showed updates for all installed extensions (which is not true, but I suppose it is an artifact of architecture change), and when I tried to update SlicerMorph, it actually disabled the extension (after the restart) with the error that the installed version is not compatible. The only solution I found was to uninstall and reinstall it. SlicerMorph was the only extension that the update partially work. For everything else I am getting this:</p>
<pre><code class="lang-auto">
"update check for SurfaceWrapSolidify complete: 'f70c039' available, 'a9512a0' installed"

Uncaught SyntaxError: missing ) after argument list

"Retrieving extension metadata [ extensionId: 613b6f1d342a877cb3bf031f]"

"Downloading extension [ itemId: 613b6f1d342a877cb3bf031f]"
</code></pre>

---

## Post #8 by @jcfr (2021-09-10 20:06 UTC)

<p>Thanks for reporting the issue.</p>
<p>As you noticed, the Slicer legacy extensions catalog still  have some rough edges and we plan on addressing these.</p>
<h2><a name="p-66052-updates-1" class="anchor" href="#p-66052-updates-1" aria-label="Heading link"></a>Updates</h2>
<aside class="quote no-group" data-username="muratmaga" data-post="7" data-topic="19256">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p><code>"Error retrieving extension metadata: amd64, win, MONAILabel, 29738 ({2d46a981-d88e-45d3-bbc0-004d69568701}: 401: Error transferring http://slicer.kitware.com/midas3/api/json?arch=amd64&amp;os=win&amp;productname=MONAILabel&amp;slicer_revision=29738&amp;method=midas.slicerpackages.extension.list - server replied: INTERNAL SERVER ERROR)"</code></p>
</blockquote>
</aside>
<p>Thanks for the report.</p>
<p>This particular issue has been fixed in <a href="https://github.com/KitwareMedical/slicer-extensions-legacy-webapp/commit/90ad5a22bfa314dd69b82ce74224313035874a96">KitwareMedical/slicer-extensions-legacy-webapp@90ad5a22b</a> and corresponding change have just been deployed.</p>
<p>Background: <code>MONAILabel</code> is not available in the latest stable release and the api call should not fail.</p>

---

## Post #9 by @muratmaga (2021-09-10 20:14 UTC)

<p>Thanks JC. What worried me is not the MonaiLabel, but the error I got when I tried to update WarpSolidfy extension. Glad to hear that it will be fixed.</p>

---

## Post #10 by @jcfr (2021-09-14 04:15 UTC)

<h3><a name="p-66226-updates-1" class="anchor" href="#p-66226-updates-1" aria-label="Heading link"></a>Updates</h3>
<aside class="quote no-group" data-username="muratmaga" data-post="7" data-topic="19256">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<pre><code class="lang-auto">"update check for SurfaceWrapSolidify complete: 'f70c039' available, 'a9512a0' installed"

Uncaught SyntaxError: missing ) after argument list
</code></pre>
</blockquote>
</aside>
<p>This particular issue has been fixed in <a href="https://github.com/Slicer/Slicer/pull/5846" class="inline-onebox">Fix extensions manager integration by jcfr · Pull Request #5846 · Slicer/Slicer · GitHub</a> and corresponding changes have been integrated.</p>

---

## Post #11 by @jcfr (2022-07-13 21:39 UTC)

<aside class="quote no-group quote-modified" data-username="Sam_Horvath" data-post="1" data-topic="19256">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar"> Sam_Horvath:</div>
<blockquote>
<h2>Download data sets that were previously hosted on the DataStore</h2>
<p>If you are looking for data previously accessible via the Data Store module (hosted on the DataStore server), it can be found here: <code>https://slicer-packages.kitware.com/#collection/6124ffb8342a877cb3b8afdd/folder/6125487e342a877cb3b8b6ed</code></p>
</blockquote>
</aside>
<p>As of July 13th 2022, the collection <code>6124ffb8342a877cb3b8afdd</code> has been removed and datasets are now available in the GitHub project <a href="https://github.com/Slicer/slicer.kitware.com-midas3-archive#readme">Slicer/slicer.kitware.com-midas3-archive</a>.</p>
<p>Original post has been updated accordingly.</p>

---
