---
topic_id: 26725
title: "Code Autocompletion On Vscode Fails"
date: 2022-12-14
url: https://discourse.slicer.org/t/26725
---

# Code autocompletion on VSCode fails

**Topic ID**: 26725
**Date**: 2022-12-14
**URL**: https://discourse.slicer.org/t/code-autocompletion-on-vscode-fails/26725

---

## Post #1 by @Alistair_McCutcheon (2022-12-14 13:14 UTC)

<p><strong>Problem:</strong><br>
I’m trying to use VSCode to develop a Slicer extension. This is my first time using Slicer. I am trying to set up my development environment such that the code has typical autocomplete functions. I am using Ubuntu 22.04.1 LTS and VSCode version 1.74.0 5235c6bb189b60b01b1f49062f4ffa42384f8c91 x64. My Slicer version is 5.2.1-linux-amd64</p>
<p><strong>Similar Topics:</strong><br>
Here are the other topics I’ve looked at, but neither solved my issue.</p><aside class="quote" data-post="1" data-topic="7390">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/autocomplete-code-lines-for-slicer-in-an-ide/7390">Autocomplete code lines for slicer in an IDE?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    new to slicer development, saw this tutorial and they seem to use an IDE that supports autocompleting statements unique to slicer as in the python interactor: 
            
 
what IDE could i use for that feature ( or how to add slicer API support to IDEs like pycharm?) 
Thanks for your help.
  </blockquote>
</aside>
<p><a href="https://discourse.slicer.org/t/developing-slicer-modules-in-visual-studio-visual-studio-code/9496" class="inline-onebox">Developing Slicer modules in Visual Studio / Visual Studio Code?</a> (slightly out of date as pythonPath is not part of the settings.json file anymore).</p>
<p><strong>What I’ve tried:</strong><br>
I’ve selected the Python contained in Slicer.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff52cf4b9db0fb9733056801030ef858716191c7.png" alt="image" data-base62-sha1="AqHaMYjJ4vlb1QQq9soYi1lYOBV" width="601" height="131"></p>
<p>I then went into the integrated python console of the slicer gui and ran:<br>
slicer.util.pip_install(‘pylint rope autopep8’)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e54fc096152df9b331efac14caeae177c1b0b87f.png" data-download-href="/uploads/short-url/wIAcYgu1lkoI0SK3bbhp6DCmRVd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e54fc096152df9b331efac14caeae177c1b0b87f_2_647x500.png" alt="image" data-base62-sha1="wIAcYgu1lkoI0SK3bbhp6DCmRVd" width="647" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e54fc096152df9b331efac14caeae177c1b0b87f_2_647x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e54fc096152df9b331efac14caeae177c1b0b87f_2_970x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e54fc096152df9b331efac14caeae177c1b0b87f.png 2x" data-dominant-color="E2E5E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1248×964 202 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My workspace settings.json file in .vscode is as follows. I have verified that this file is in the correct location.</p>
<pre><code class="lang-auto">{
    "python.autoComplete.extraPaths": [
        "/opt/Slicer-5.2.1-linux-amd64/",
        "/opt/Slicer-5.2.1-linux-amd64/lib/",
        "/opt/Slicer-5.2.1-linux-amd64/lib/Python",
        "/opt/Slicer-5.2.1-linux-amd64/lib/QtPlugins",
        "/opt/Slicer-5.2.1-linux-amd64/lib/Slicer-5.2",
        "/opt/Slicer-5.2.1-linux-amd64/bin",
    ],
    "python.linting.pylintPath": "/opt/Slicer-5.2.1-linux-amd64/lib/Python/bin/pylint",
    "python.analysis.extraPaths": [
        "/opt/Slicer-5.2.1-linux-amd64/",
        "/opt/Slicer-5.2.1-linux-amd64/lib/",
        "/opt/Slicer-5.2.1-linux-amd64/lib/Python",
        "/opt/Slicer-5.2.1-linux-amd64/lib/QtPlugins",
        "/opt/Slicer-5.2.1-linux-amd64/lib/Slicer-5.2",
        "/opt/Slicer-5.2.1-linux-amd64/bin"
    ],
    "python.linting.enabled": true,
    "python.formatting.autopep8Path": "/opt/Slicer-5.2.1-linux-amd64/lib/Python/bin/autopep8",
}
</code></pre>
<p>After doing this, I would expect to be able to have VSCode autocomplete/provide suggestions on modules etc. However:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6418f1e128f2abd938b5abb6f2d9ef904b2854ea.png" alt="image" data-base62-sha1="ehvbQFMlareKojFmJ7KxMBEkp3c" width="506" height="273"></p>
<p>I do have the suggestions when importing however, suggesting vscode is indeed pointing to the correct Python launcher:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f642416183f871640334479f7caf6affb514b8a6.png" alt="image" data-base62-sha1="z8vpnbClhEatO9eimj5ql719ocS" width="566" height="165"></p>
<p>I have also tried copying the above settings.json file to the user settings.json file, but to no avail.</p>

---

## Post #2 by @mikebind (2023-07-19 18:23 UTC)

<p>Has anyone gotten further than this?  I have followed the same path of trying to get this to work and gotten stuck at the same place…  <code>slicer.</code> lists a few things as autocomplete options, but not things like <code>slicer.util</code> .  However, I can do <code>from slicer import </code> and get <code>util</code> as a suggestion, and then I can get many <code>util.</code> method autocompletion settings. However, if I do <code>slicer.util.</code> I get no autocompletion options.  I don’t understand this… shouldn’t <code>slicer.util.</code> be the same as <code>util.</code> after <code>from slicer import util</code>? I’m not sure why one successfully autocompletes but the other doesn’t.</p>
<p>I understand from a previous thread that wrapped C++ code might be a problem as well as things which might be more dynamically constructed like <code>mrmlScene</code>, but I’d love to get autocompletion working at least for all the purely python and static components like <code>util</code>.  Any help out there? I did try adding <code>"C:\\Users\\mikeb\\AppData\\Local\\NA-MIC\\Slicer 5.2.1\\bin\\Python\\slicer"</code> (the home of <code>util.py</code>) to the VSCode <code>settings.json</code> list of extra <code>python.autoComplete.extraPaths</code>, but it didn’t seem to help.</p>

---

## Post #3 by @lassoan (2023-07-21 17:11 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> there are some Slicer pull requests with related changes. Could <a class="mention" href="/u/mikebind">@mikebind</a> test/work ok those?</p>

---

## Post #4 by @jcfr (2023-07-21 18:06 UTC)

<p>To get an idea of the remaining work, see <a href="https://github.com/Slicer/Slicer/issues/6690" class="inline-onebox">Improve auto-completion support · Issue #6690 · Slicer/Slicer · GitHub</a>.</p>

---

## Post #5 by @mikebind (2023-07-21 22:37 UTC)

<p>Thanks for the link <a class="mention" href="/u/jcfr">@jcfr</a>.  I would be happy to try to test things on my system.  Unfortunately, looking through the changes and remaining work, I doubt I would be capable of contributing in a meaningful way to helping move things forward.  While I would consider myself fairly comfortable developing scripted python modules in Slicer, at this point, the build system and even the C++ level of Slicer code are generally hard for me to follow. I can follow directions and be a naive user checking if PR’s work on my system though!</p>

---
