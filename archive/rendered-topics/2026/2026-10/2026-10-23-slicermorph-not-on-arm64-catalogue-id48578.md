---
topic_id: 48578
title: "Slicermorph not on arm64 catalogue"
date: 2026-10-23
url: https://discourse.slicer.org/t/48578
last_bumped: 2026-10-23T19:04:19.173Z
---

# Slicermorph not on arm64 catalogue

**Topic ID**: 48578
**Date**: 2026-10-23
**URL**: https://discourse.slicer.org/t/slicermorph-not-on-arm64-catalogue/48578

---

## Post #1 by @muratmaga (2026-10-23 02:51 UTC)

<p><a class="mention" href="/u/ebrahim">@ebrahim</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a></p>
<p>looks like MacOS arm64 build is now integrated to the downloads site. Congrats on the milestone.</p>
<p>I noticed SlicerMorph is not available for arm64. Any idea why?</p>

---

## Post #2 by @Thibault_Pelletier (2026-10-23 07:52 UTC)

<p>For information, other extensions seem to be missing such as the Dental Segmentator.</p>
<p>On a related note, the MacOS arm64 is currently the only platform in the previews using Qt6.<br>
To bump the extensions, it would probably be a good idea to make the switch for the other platforms as well to avoid a Qt5 / Qt6 dual compat.</p>

---

## Post #3 by @Sam_Horvath (2026-10-23 14:02 UTC)

<p>Hi Murat,</p>
<p>So there are a number of issues occurring here.</p>
<ul>
<li>There is a bug that is redirecting the extension page back to the intel version</li>
<li>The intel version is the one that is missing</li>
</ul>
<p>We will have this fixed soon</p>

---

## Post #4 by @Sam_Horvath (2026-10-23 14:07 UTC)

<p>And the Intel is missing because I cut off the intel extension build yesterday to fix some things on that system. Intel macOS extensions are always lagging behind everything else due to the long build times on that machine, I have been working on speeding that up</p>

---

## Post #5 by @Sam_Horvath (2026-10-23 14:17 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Try launching your arm64 download again and checking for SlicerMorph, it should be there now</p>

---

## Post #6 by @Sam_Horvath (2026-10-23 14:47 UTC)

<p>The full Qt6 switchover is next on my list</p>

---

## Post #7 by @muratmaga (2026-10-23 17:08 UTC)

<p>When I tried to run the extension manager and install slicermorph, I got these errors (and nothing was installed)<img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<pre><code class="lang-auto">Added {--remote-allow-origins=*} to command-line arguments to avoid web socket connection errors during remote debugging.



DevTools listening on ws://127.0.0.1:1337/devtools/browser/4b3064fa-2a78-4d6a-8013-599816100856

Remote debugging server started successfully. Try pointing a Chromium-based browser to http://127.0.0.1:1337

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Extension metadata response missed required 'extensionname' field

Download of extension failed, could not find an extension with id = 6adb253632e5d6bfbf6eb47f

2026-10-23 10:06:46.307 SlicerApp-real[70747:23511547] TSMSendMessageToUIServer: CFMessagePortSendRequest FAILED(-1) to send to port com.apple.tsm.uiserver
</code></pre>

---

## Post #8 by @muratmaga (2026-10-23 17:26 UTC)

<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> From claude it if it useful:</p>
<hr>
<p>Found the cause. The server side is fine: the <code>/api/v1/app/.../extension?app_revision=35403&amp;os=macosx&amp;arch=arm64</code> query returns all 230 extensions, each with <code>meta.baseName</code>. The problem is in qRestAPI under Qt6.</p>
<p><code>qRestAPI::qVariantMapFlattened()</code> (commontk/qRestAPI@5c4a76e, the commit Slicer currently pins) uses <code>QVariant::canConvert&lt;QVariantMap&gt;()</code> / <code>canConvert&lt;QVariantList&gt;()</code> to decide whether to recurse. In Qt6, <code>QVariant(QString).canConvert&lt;QVariantList&gt;()</code> returns <code>true</code>. So every string field gets treated as a list, converted with <code>toMap()</code> into an empty map, and dropped. After flattening, each record has only <code>size</code> and <code>meta.tier</code>. With no <code>extensionname</code>, <code>onExtensionsMetadataFromServerQueryFinished</code> skips all of them (one warning per extension). Install then can’t find the extension id. The catalog still displays because the web frontend queries the server directly.</p>
<p>I reproduced this with a small test against Qt 6.11.2 using the same parse/flatten code on the live server response:</p>
<pre><code class="lang-auto">name type QString  canConvert&lt;QVariantMap&gt; false  canConvert&lt;QVariantList&gt; true
flattened keys: ("meta.tier", "size")
</code></pre>
<p>Checking the actual type fixes it, and it works for both Qt5 and Qt6:</p>
<pre data-code-wrap="cpp"><code class="lang-cpp">if (value.userType() == QMetaType::QVariantMap)    // was canConvert&lt;QVariantMap&gt;()
...
if (value.userType() == QMetaType::QVariantList)   // was canConvert&lt;QVariantList&gt;()
</code></pre>
<p>With that change all fields come through, including <code>meta.baseName</code>. This will hit every Qt6 build, so it should be fixed in qRestAPI and the pin bumped before the full Qt6 switchover.</p>

---

## Post #9 by @Sam_Horvath (2026-10-23 18:28 UTC)

<p>Awesome, thanks Murat.  I am getting a fix ready for this now</p>

---

## Post #10 by @Sam_Horvath (2026-10-23 19:04 UTC)

<p>Fix has been merged: <a href="https://github.com/Slicer/Slicer/pull/9498" class="inline-onebox">BUG: Fix Extensions Manager failing to install extensions with Qt 6 by sjh26 · Pull Request #9498 · Slicer/Slicer · GitHub</a></p>
<p>This will be available after tonight’s build is done, so tomorrow after 10 AM ET</p>

---
