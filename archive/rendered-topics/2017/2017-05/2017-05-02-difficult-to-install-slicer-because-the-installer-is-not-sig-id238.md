# DIfficult to install Slicer because the installer is not signed

**Topic ID**: 238
**Date**: 2017-05-02
**URL**: https://discourse.slicer.org/t/difficult-to-install-slicer-because-the-installer-is-not-signed/238

---

## Post #1 by @lassoan (2017-05-02 02:57 UTC)

<p>It is getting more and more difficult to install Slicer’s unsigned installation package.</p>
<p>On Windows, the user has to click through a series of dialog boxes explaining how unsafe this downloaded application is and recently SmartFilter scans started to take several minutes (the user just waiting for the SmartFilter dialog to go away, it’s not clear what’s happening).</p>
<p>The situation is getting worse on Mac, too, as reported by <a class="mention" href="/u/fedorov">@Fedorov</a> here: <a href="https://discourse.slicer.org/t/multiple-startup-errors-and-no-simpleitk-in-may-1-nightly-on-mac/231/8">Multiple startup errors and no SimpleITK in May 1 nightly on mac</a>.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> you worked on this in the past, can you summarize how far you got and what would need to be done to get the installation packages signed?</p>

---

## Post #2 by @jcfr (2017-05-02 03:05 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="238">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>you worked on this in the past, can you summarize how far you got and what would need to be done to get the installation packages signed?</p>
</blockquote>
</aside>
<h3><a name="p-689-windows-1" class="anchor" href="#p-689-windows-1" aria-label="Heading link"></a>windows</h3>
<p>it is quite “straight forward” to sign the installer at least, see <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Windows_Code_Signing" class="inline-onebox">Documentation/Nightly/Developers/Windows Code Signing - Slicer Wiki</a></p>
<p>We have available certificate(s) (we already use them for signing the stable release). I will check internally how we can automate signing of the nightly installers.</p>
<h3><a name="p-689-macosx-2" class="anchor" href="#p-689-macosx-2" aria-label="Heading link"></a>MacOSX,</h3>
<p>We also have the process documented here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Mac_OS_X_Code_Signing" class="inline-onebox">Documentation/Nightly/Developers/Mac OS X Code Signing - Slicer Wiki</a></p>
<p>For this one, we need to update the packaging system to be more closely integrated with the signing process.</p>
<p>Also, we have certificate available (we are member of the developer program). I will check internally and report back with a timeline.</p>

---

## Post #3 by @lassoan (2017-05-02 16:13 UTC)

<p>Thanks for the information, it sounds very promising!</p>

---

## Post #4 by @jcfr (2017-05-08 16:04 UTC)

<p>To follow up on this, internally at Kitware we are currently discussing how to solve the issue across our platforms. While I don’t yet have a timeline, I can tell that we are making progress.</p>
<p>The idea will be to have decoupled components including “signing systems” (e.g windows system for installer signing, MacOSX system for dmg signing, Linux based GPG signing for source distribution, …) and a “distributions depot” system (probably an internal SFTP server).</p>

---
