---
topic_id: 22766
title: "Slicer Ini File Locations"
date: 2022-03-30
url: https://discourse.slicer.org/t/22766
---

# Slicer ini file locations

**Topic ID**: 22766
**Date**: 2022-03-30
**URL**: https://discourse.slicer.org/t/slicer-ini-file-locations/22766

---

## Post #1 by @muratmaga (2022-03-30 15:49 UTC)

<p>As I understand Slicer has two ini files.<br>
<strong>Slicer.ini,</strong> which is sort of global and is read by all Slicer versions installed and then there is <strong>Slicer-XXXXX.ini</strong> which is version specific.</p>
<p>For our docker instance we bake the Slicer application and Slicer.ini into the container, but we need to have Slicer-XXXX.ini on a persistent storage so that last loaded files, additional modules and user specific customizations are saved and retained in between sessions.</p>
<p>Is there an option that I set in global Slicer.ini to look for a specific folder for version specific Slicer-XXXXX.ini? I can of course do a volume mapping between host and docker for Slicer-XXXXX.ini file, but that means it needs to be modified everytime Slicer version is changed.</p>
<p>I am also open to other suggestions as well.</p>

---

## Post #2 by @pieper (2022-03-30 15:57 UTC)

<p>I don’t think we have anything like that now, but it might be a place where an environment variable could be added to handle this use case.  Like a <code>SLICER_VERSIONED_INI_PATH</code> or similar.</p>

---

## Post #3 by @muratmaga (2022-03-30 19:10 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="22766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>environment variable could be added to handle this use case.</p>
</blockquote>
</aside>
<p>So should I add this as a feature request to GH issues?</p>

---

## Post #4 by @pieper (2022-03-30 22:37 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="22766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>So should I add this as a feature request to GH issues?</p>
</blockquote>
</aside>
<p>Yes, sure.  Then if anyone has other ideas we can discuss it there.</p>

---

## Post #5 by @lassoan (2022-03-30 23:35 UTC)

<p>The global <code>Slicer.ini</code> is only used if you haven’t created a Slicer.ini file in the <code>&lt;application home&gt;/&lt;organization&gt;</code> directory (next to your <code>Slicer-NNN.ini</code> file). See details <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html?highlight=slicer.ini#settings-file-location">here</a>.</p>
<p>I see two options:</p>
<ul>
<li>If you do not let users install new extensions: keep Slicer.ini in the default user profile folder location and preserve the content of that folder.</li>
<li>If you let users install new extensions: Create a <code>Slicer.ini</code> file in your <code>&lt;application home&gt;/&lt;organization&gt;</code> directory and make the entire <code>&lt;application home&gt;</code> folder persistent. If you want to minimize storage requirements then it will be a bit more complicated, as you need to persist a couple of folders, such as:
<ul>
<li>
<code>&lt;application home&gt;/&lt;organization&gt;</code> (settings and extensions)</li>
<li>
<code>&lt;application home&gt;/lib/Python/Lib/site-packages</code> (Python packages installed by extensions)</li>
<li>
<code>&lt;application home&gt;/lib/Python/Scripts</code> (script for Python packages installed by extensions)</li>
<li>
<code>&lt;application home&gt;/DICOMDatabase</code> (whereever you configure it, but it is more consistent if you keep all files at one location)</li>
<li>you may consider persisting the cache folder, too</li>
</ul>
</li>
</ul>

---

## Post #6 by @muratmaga (2022-03-31 03:29 UTC)

<p>Thanks Andras.</p>
<p>I may consider going back to putting whole Slicer folder in a persistent volume, which we used to do. It will definitely simplify the number of exported volumes. I think that might be the easiest and most flexible option.</p>

---
