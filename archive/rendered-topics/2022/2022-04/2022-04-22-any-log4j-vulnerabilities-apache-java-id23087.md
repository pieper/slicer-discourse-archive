---
topic_id: 23087
title: "Any Log4J Vulnerabilities Apache Java"
date: 2022-04-22
url: https://discourse.slicer.org/t/23087
---

# Any Log4J vulnerabilities (Apache Java)  

**Topic ID**: 23087
**Date**: 2022-04-22
**URL**: https://discourse.slicer.org/t/any-log4j-vulnerabilities-apache-java/23087

---

## Post #1 by @car (2022-04-22 13:40 UTC)

<p>Hi, apologies if this is a daft question, but I need to confirm that there are no Log4J vulnerabilities associated with 3D Slicer please.  I don’t use it personally, but it is used within our organisation and I am tasked with trying to find out for all our software if there are any Log4J vulnerabilities due to the use of Apache’s Java based Log4J code. I’m assuming it is not impacted as no mention on any of your sites/documentation, however I need confirmation, please could someone confirm if 3D slicer has any Log4J vulnerabilities.<br>
<a href="https://logging.apache.org/log4j/2.x/" rel="noopener nofollow ugc">Log4j – Apache Log4j 2</a></p>

---

## Post #2 by @pieper (2022-04-22 13:56 UTC)

<p>3D Slicer does not use Java, so this Log4J vulnerability would not be an issue as far as I know.</p>

---

## Post #3 by @jamesobutler (2022-04-22 14:05 UTC)

<p>I did a quick file search of “log4j” in a Slicer build tree and came across the following in the DCMTK build. I’m not familiar enough to know what these are for.</p>
<ul>
<li>log4judp.h, log4judp.cc and log4judp.obj</li>
</ul>
<p>Also, since 3D Slicer allows installing extensions through the “Extensions Manager” you would want to make sure any 3rd party extensions that you use in Slicer don’t also have any vulnerabilities.</p>

---

## Post #4 by @lassoan (2022-04-23 04:40 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="23087">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>came across the following in the DCMTK build. I’m not familiar enough to know what these are for.</p>
<ul>
<li>log4judp.h, log4judp.cc and log4judp.obj</li>
</ul>
</blockquote>
</aside>
<p>I’ve had a look at this and it comes from log4cpp library, which DCMTK uses for logging. This library can send log messages in a log4j compatible format and supports similar features as log4j, but it is a completely independent implementation (does not even use the same programming language) and it is not affected by log4j vulnerabilities. See this <a href="https://github.com/log4cplus/log4cplus/issues/542#issuecomment-992436513">discussion on the log4cpp issue tracker</a>:</p>
<blockquote>
<blockquote>
<p>as log4cplus is modelled after log4j, is log4cplus also affected by this vulnerability?</p>
</blockquote>
<p>No. log4cplus is C++ based library. It shares only name similary and concepts with log4j, not the implementation.</p>
</blockquote>
<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="23087">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Also, since 3D Slicer allows installing extensions through the “Extensions Manager” you would want to make sure any 3rd party extensions that you use in Slicer don’t also have any vulnerabilities.</p>
</blockquote>
</aside>
<p>I’ve checked the build tree of the extensions index and can confirm that log4j is not used by any of the extensions that are distributed via the Slicer Extensions Manager.</p>
<hr>
<p>Therefore, Slicer and its publicly available extensions are not impacted by log4j vulnerability. That said, neither Slicer core nor the libraries that Slicer uses are particularly hardened against potential security vulnerabilities. The application is expected to be used in a trusted environment - trusted users, data, network, etc.</p>

---
