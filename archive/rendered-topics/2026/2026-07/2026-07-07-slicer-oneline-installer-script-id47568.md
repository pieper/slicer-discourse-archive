---
topic_id: 47568
title: "Slicer oneline installer script"
date: 2026-07-07
url: https://discourse.slicer.org/t/47568
last_bumped: 2026-07-12T10:48:01.659Z
---

# Slicer oneline installer script

**Topic ID**: 47568
**Date**: 2026-07-07
**URL**: https://discourse.slicer.org/t/slicer-oneline-installer-script/47568

---

## Post #1 by @mau_igna_06 (2026-07-07 23:31 UTC)

<p>Hi all,</p>
<p>I have created this one-line installer script for Slicer and I’d like to receive feedback from the community.</p>
<p>It has been tested on Ubuntu 22 and Windows 10</p>
<p>Linux &amp; macOS version:</p>
<pre data-code-wrap="bash"><code class="lang-bash">curl -fsSL https://raw.githubusercontent.com/mauigna06/slicer-installer/main/install.sh | sh
</code></pre>
<p>Windows version:</p>
<pre data-code-wrap="powershell"><code class="lang-powershell">irm https://raw.githubusercontent.com/mauigna06/slicer-installer/main/install.ps1 | iex
</code></pre>

---

## Post #2 by @ebrahim (2026-07-08 11:05 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="1" data-topic="47568">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<pre><code class="lang-auto">curl -fsSL https://raw.githubusercontent.com/mauigna06/slicer-installer/main/install.sh | sh

</code></pre>
</blockquote>
</aside>
<p>The ascii logo is beautiful</p>
<p>I tried the linux one, but I stopped when it asked for sudo.</p>
<p>I think people are put off when an install script they run with curl asks for sudo. It’s already a lot of trust required to run it in the first place. I understand it’s to install runtime dependencies, but I also don’t necessarily want a script messing around with my system package manager on its own – that is for me to do. Maybe linux users would often feel the same.</p>
<p>Instead of automatically installing runtime dependencies, the script could just download and install Slicer to a local directory like you are doing, and then at the end it can print a command for the user to use to install runtime dependencies. Then sudo should not be needed and the experience would be smoother</p>

---

## Post #3 by @mau_igna_06 (2026-07-08 12:17 UTC)

<p>Ok. Updated according to your feedback. Now it does not install dependencies by default so it does not ask for sudo, it just prints a comment to the user with the command he needs to execute for the dependencies install instead</p>
<p>Could you please try again?</p>

---

## Post #4 by @ebrahim (2026-07-08 17:11 UTC)

<p>It worked well! I am on ubuntu 22.04</p>
<p>Some feedback:</p>
<ul>
<li>the “Downloading 3D Slicer…” display during download could display the version also</li>
<li>the icon it chose is completely wrong! it chose the splash screen as the icon!</li>
<li>when I ran it a second time, it tried to start the download all over again. it would be extra nice if the script checked whether you already have slicer in the same install location and did something differently. But I am not sure what is the best design: should it abort? offer to clean-reinstall? offer to install multiple versions side by side each with their own version-specific launcher?</li>
</ul>

---

## Post #5 by @mau_igna_06 (2026-07-10 14:06 UTC)

<aside class="quote no-group" data-username="ebrahim" data-post="4" data-topic="47568">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/ebrahim/48/13403_2.png" class="avatar"> ebrahim:</div>
<blockquote>
<ul>
<li>the “Downloading 3D Slicer…” display during download could display the version also</li>
</ul>
</blockquote>
</aside>
<p>Done</p>
<aside class="quote no-group" data-username="ebrahim" data-post="4" data-topic="47568">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/ebrahim/48/13403_2.png" class="avatar"> ebrahim:</div>
<blockquote>
<ul>
<li>the icon it chose is completely wrong! it chose the splash screen as the icon!</li>
</ul>
</blockquote>
</aside>
<p>Corrected</p>
<aside class="quote no-group" data-username="ebrahim" data-post="4" data-topic="47568">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/ebrahim/48/13403_2.png" class="avatar"> ebrahim:</div>
<blockquote>
<ul>
<li>But I am not sure what is the best design: should it abort? offer to clean-reinstall? offer to install multiple versions side by side each with their own version-specific launcher?</li>
</ul>
</blockquote>
</aside>
<p>Improved, let the user select (see picture below)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a9d756e48658944d2ed0c2c159e63562f76fe10.png" data-download-href="/uploads/short-url/64Zpgq8DgrL3SNTghb9FKlJC0cE.png?dl=1" title="Screenshot from 2026-07-10 11-00-04_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a9d756e48658944d2ed0c2c159e63562f76fe10_2_561x500.png" alt="Screenshot from 2026-07-10 11-00-04_2" data-base62-sha1="64Zpgq8DgrL3SNTghb9FKlJC0cE" width="561" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a9d756e48658944d2ed0c2c159e63562f76fe10_2_561x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a9d756e48658944d2ed0c2c159e63562f76fe10_2_841x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a9d756e48658944d2ed0c2c159e63562f76fe10_2_1122x1000.png 2x" data-dominant-color="262728"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2026-07-10 11-00-04_2</span><span class="informations">1345×1198 294 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you</p>

---

## Post #6 by @ebrahim (2026-07-10 16:33 UTC)

<p>Nice! What does it do when a different version is already installed? Side by side? Do the launchers then have versions in their name to distinguish them?</p>

---

## Post #7 by @mau_igna_06 (2026-07-10 18:29 UTC)

<blockquote>
<p><img src="https://emoji.discourse-cdn.com/twitter/robot.png?v=15" title=":robot:" class="emoji" alt=":robot:" loading="lazy" width="20" height="20"> This post was written with AI assistance.</p>
</blockquote>
<p>Sorry, I had forgotten to push the last 2 commits for the feature I showed above</p>
<blockquote>
<p>What does it do when a different version is already installed? Side by side? Do the launchers then have versions in their name to distinguish them?</p>
</blockquote>
<p><strong>On Linux</strong>:<br>
The prompt about the 3 options only fires when that <em>same</em> version+arch directory already exists.<br>
A <em>different</em> version has a different directory name, so no collision is detected.</p>
<p><strong>On macOS</strong>:<br>
Every version installs as <code>Slicer.app</code> at the same path so <em>any</em> different version <em>does</em> trigger the prompt</p>
<p><strong>On Windows</strong>:<br>
Every version has its own installer and they use a different directory and provide a different desktop shortcut</p>
<h3><a name="p-134821-do-the-launchers-get-versioned-names-1" class="anchor" href="#p-134821-do-the-launchers-get-versioned-names-1" aria-label="Heading link"></a>Do the launchers get versioned names?</h3>
<p><strong>On Linux</strong>: Last version overwrites the link to <code>Slicer</code></p>
<p><strong>On macOS</strong>:  there’s no PATH launcher at all; <code>open -a Slicer</code> resolves by bundle id through LaunchServices, and the script even warns that with multiple copies it may launch an unexpected one</p>
<p><strong>On Windows</strong>: the launcher name is always <code>Slicer.exe</code> (different version live on different directories)</p>
<p><strong>Bottom line:</strong> versions coexist on disk (on Linux and Windows), but the launchers are single, unversioned names that always track the most recent install — there’s no <code>Slicer-5.12</code> vs <code>Slicer-5.10</code> launcher to pick between.</p>

---

## Post #8 by @mau_igna_06 (2026-07-12 10:48 UTC)

<p>Windows version of the command was failing if not executing from powershell, now that’s solved. New calling (from powershell or cmd):</p>
<pre data-code-wrap="bash"><code class="lang-bash">powershell -c "irm https://raw.githubusercontent.com/mauigna06/slicer-installer/main/install.ps1 | iex"
</code></pre>

---
