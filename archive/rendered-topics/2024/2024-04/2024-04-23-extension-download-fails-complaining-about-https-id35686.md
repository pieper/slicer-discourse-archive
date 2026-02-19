---
topic_id: 35686
title: "Extension Download Fails Complaining About Https"
date: 2024-04-23
url: https://discourse.slicer.org/t/35686
---

# Extension download fails complaining about HTTPS

**Topic ID**: 35686
**Date**: 2024-04-23
**URL**: https://discourse.slicer.org/t/extension-download-fails-complaining-about-https/35686

---

## Post #1 by @Juergen (2024-04-23 16:59 UTC)

<p>Hello,</p>
<p>I keep having this problem with downloading extensions from the Slicer app. This is the message I get for any extension:</p>
<p>[FD] DevTools listening on ws://127.0.0.1:1337/devtools/browser/d41c38da-7491-4300-893a-064b31096b02</p>
<p>[Qt] Remote debugging server started successfully. Try pointing a Chromium-based browser to <a href="http://127.0.0.1:1337" rel="noopener nofollow ugc">http://127.0.0.1:1337</a></p>
<p>[Qt] “<a href="https://extensions.slicer.org/catalog/All/32818/win" rel="noopener nofollow ugc">https://extensions.slicer.org/catalog/All/32818/win</a>” 0 “Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32818/win" rel="noopener nofollow ugc">https://extensions.slicer.org/catalog/All/32818/win</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/b/bc/BaselineFollowupSCANRegisteredCMFreg2.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/b/bc/BaselineFollowupSCANRegisteredCMFreg2.png</a>’. This content should also be served over HTTPS.”</p>
<p>[Qt] Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32818/win" rel="noopener nofollow ugc">https://extensions.slicer.org/catalog/All/32818/win</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/b/bc/BaselineFollowupSCANRegisteredCMFreg2.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/b/bc/BaselineFollowupSCANRegisteredCMFreg2.png</a>’. This content should also be served over HTTPS.</p>
<p>Unfortunately, the automatic download and installation of bookmarked extensions also fails which is a big headache.</p>
<p>Any ideas what can be done?</p>
<p>Thanks, Juergen</p>

---

## Post #2 by @lassoan (2024-04-24 01:32 UTC)

<p>Those are just warnings that some icons or screenshots are downloaded using http protocol.  You can safely ignore these messages.</p>

---

## Post #3 by @Juergen (2024-04-24 15:41 UTC)

<p>Thanks for the quick response, Andras.</p>
<p>Unfortunately, the download also failed:</p>
<p>[Qt] Retrieving extension metadata for MarkupsToModel extension</p>
<p>[Qt] Retrieving MarkupsToModel extension files (extensionId: 662768b26a328ae4b089b69d)</p>
<p>[Qt] Downloading MarkupsToModel extension (item_id: 662768b26a328ae4b089b69d, file_id: 662768b26a328ae4b089b6a4)</p>
<p>[Qt] Failed downloading: <a href="https://slicer-packages.kitware.com/api/v1/file/662768b26a328ae4b089b6a4/download" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/file/662768b26a328ae4b089b6a4/download</a></p>
<p>[Qt] Retrieving extension metadata for AnglePlanesExtension extension</p>
<p>[Qt] Retrieving AnglePlanesExtension extension files (extensionId: 6627674d6a328ae4b089b57c)</p>
<p>[Qt] Downloading AnglePlanesExtension extension (item_id: 6627674d6a328ae4b089b57c, file_id: 6627674e6a328ae4b089b58d)</p>
<p>[Qt] Failed downloading: <a href="https://slicer-packages.kitware.com/api/v1/file/6627674e6a328ae4b089b58d/download" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/file/6627674e6a328ae4b089b58d/download</a></p>
<p>Something else showed up in the error logs:</p>
<p>“” 1 “JQuery not loaded - Failed to trigger webkitvisibilitychange”</p>
<p>Thanks for any help.</p>

---

## Post #4 by @lassoan (2024-04-24 20:15 UTC)

<p>The URLs are valid, which means that most likely you are behind some institutional firewall or proxy server, which restricts Slicer in accessing the internet. You can either report the problem to your IT administrators (they can add exceptions to their firewall) or download the extension packages using an application that your institution’s IT infrastructure approve (such as your web browser). See instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#extensions-manager-does-not-show-any-extensions">here</a>.</p>
<p>There also have been discussions about issues with specific network security systems on this forum. If your IT administrators are not sure what to change then these topics may help.</p>

---
