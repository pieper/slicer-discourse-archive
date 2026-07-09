---
topic_id: 47568
title: "Slicer oneline installer script"
date: 2026-07-07
url: https://discourse.slicer.org/t/47568
last_bumped: 2026-07-08T17:11:21.160Z
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
