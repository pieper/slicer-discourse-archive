---
topic_id: 8322
title: "Settings And Extension Install Location"
date: 2019-09-06
url: https://discourse.slicer.org/t/8322
---

# Settings and extension install location

**Topic ID**: 8322
**Date**: 2019-09-06
**URL**: https://discourse.slicer.org/t/settings-and-extension-install-location/8322

---

## Post #1 by @lassoan (2019-09-06 14:14 UTC)

<p>Since Slicer is now installed in writable folder on all platforms by default and Python packages are installed into this folder, it would make sense to install extensions and version-specific (Slicer-NNN.ini) setting file into this folder, too. It would bring all Slicer files together in one folder and make Slicer installations fully isolated and portable. It would also make it easier to cleanly uninstall the application.</p>
<p>What do you think?<br>
I’m not sure how exactly this works on Mac. Would it make sense there, too?</p>

---

## Post #2 by @jcfr (2019-09-06 14:30 UTC)

<blockquote>
<p>What do you think?</p>
</blockquote>
<p>In the context of commercial application, user install extension while having the main application installed in a readonly location.</p>
<p>To support installing extension and for sake of simplification, it may be worth requiring Slicer to be installed in a writable location. I will check with some of our customers.</p>
<p>This means that to be fully relocatable, we would have to have an extension settings file (or some sort of manifest) existing within the Slicer install tree. That way it would be fully relocatable.</p>
<blockquote>
<p>I’m not sure how exactly this works on Mac. Would it make sense there, too?</p>
</blockquote>
<p>On macOS, we already install extension within the install tree.</p>

---

## Post #3 by @lassoan (2019-09-06 15:08 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="8322">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>To support installing extension and for sake of simplification, it may be worth requiring Slicer to be installed in a writable location. I will check with some of our customers.</p>
</blockquote>
</aside>
<p>Nowadays it is becoming quite common to install applications in user folder (Google Chrome, Microsoft OneDrive, VS Code, etc.).</p>
<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="8322">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>This means that to be fully relocatable, we would have to have an extension settings file (or some sort of manifest) existing within the Slicer install tree. That way it would be fully relocatable.</p>
</blockquote>
</aside>
<p>Could we use relative path? For example, extensions could be installed in an “extensions” subfolder in the install tree.</p>

---
