---
topic_id: 43670
title: "Getting The Preview Working On Newer Macos"
date: 2025-07-09
url: https://discourse.slicer.org/t/43670
---

# Getting the preview working on newer MacOS

**Topic ID**: 43670
**Date**: 2025-07-09
**URL**: https://discourse.slicer.org/t/getting-the-preview-working-on-newer-macos/43670

---

## Post #1 by @muratmaga (2025-07-09 18:55 UTC)

<p>On Mac when I download a preview version and copy the package contents to my Desktop, I usually have to command+Click and then choose Open Anyways to disregard the warning message about Slicer being potentially a dangerous application, downloaded off the web (if you don’t do this, the only option is “Move to Trash”).  Once you do this sequence, you can launch the Slicer normally.</p>
<p>I recently upgraded to MacOs 15 and looks like Open Anyways behavior has been significantly altered. You can no longer do the CMD+click, and choose Open. You need to launch slicer at least once, see the warning, then go to Security, and find the Slicer in the list of blocked applications, click the “Launch Anyways” icon next to it, and then enter your admin password to verify.</p>
<p>This is a company managed device, so I do not know whether my security policies just got tighther with the upgrade, or Apple indeed changed this behavior. I appreciate if someone can confirm this.</p>
<p>If this is indeed the default behavior for everyone, we might have to put a some explanation on the docs.</p>

---

## Post #2 by @pieper (2025-07-09 19:00 UTC)

<p>Yes, I think Apple has gotten stricter.</p>
<p>I always use the following:</p>
<pre><code class="lang-auto">xattr -rd com.apple.quarantine Slicer.app
</code></pre>
<p>and then it opens as expected.</p>
<p>I thinking we should add a README document into the .dmg with this information in preview downoads and also describe it in our readthedocs.</p>

---

## Post #3 by @ctrueden (2025-07-12 17:28 UTC)

<p>Yep, it is very strict now. I wrote about it <a href="https://github.com/apposed/jaunch/blob/1.0.4/doc/MACOS.md#code-signing" rel="noopener nofollow ugc">here</a>, as part of my work developing a new native launcher for Fiji/ImageJ.</p>
<p>For Fiji/ImageJ, we are now code-signing the native launcher so that the software runs in the <a href="https://developer.apple.com/documentation/security/hardened-runtime" rel="noopener nofollow ugc">hardened runtime</a>. A downside of this is that it is impossible to load unsigned native libraries within the hardened runtime—it will crash the program, and there is no entitlement to prevent it. For Slicer, it might be easier to make a PKG installer that not only copies over the Slicer.app but also does the <code>xattr</code> command(s) needed to unquarantine it, so that Slicer can continue to run outside the hardened runtime, and therefore still utilize extensions without needing to code-sign them all.</p>

---

## Post #4 by @pieper (2025-07-12 17:44 UTC)

<p>Thanks for providing the background info <a class="mention" href="/u/ctrueden">@ctrueden</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=14" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>I think it’s okay to make people explicitly un-quarantine the preview builds.  It is experimental software after all.  But I do think we should make it easier to discover how to make it work, and yes maybe provide a script, ideally with a message that informs them what what’s going on and a chance to opt out before proceeding.</p>

---
