---
topic_id: 346
title: "Mantis Issue Tracker Access Issue"
date: 2017-05-19
url: https://discourse.slicer.org/t/346
---

# Mantis issue tracker access issue:

**Topic ID**: 346
**Date**: 2017-05-19
**URL**: https://discourse.slicer.org/t/mantis-issue-tracker-access-issue/346

---

## Post #1 by @jcfr (2017-05-19 17:36 UTC)

<p>As of 2017-05-19, 1.30pm EST, trying to access the bug tracker report the following:</p>
<p>see <a href="http://www.na-mic.org/Bug/">http://www.na-mic.org/Bug/</a><br>
or <a href="http://www.na-mic.org/Mantis/">http://www.na-mic.org/Mantis/</a></p>
<pre><code class="lang-auto">Forbidden

You don't have permission to access /Mantis/view.php on this server.
</code></pre>
<p>Cc: <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/mhalle">@mhalle</a> <a class="mention" href="/u/freephile">@freephile</a></p>

---

## Post #2 by @freephile (2017-05-19 18:32 UTC)

<p>Still hosted on Partners infra. Should come back with NFS restore?</p>

---

## Post #3 by @mhalle (2017-05-19 19:06 UTC)

<p>I’ve reported this problem as well.  This may be a permissions issue – Partners is migrating us away from our legacy NIS/LDAP machine to a modern LDAP instance as a stepping stone for adopting Partners active directory.</p>
<p>It’s quite possible something got bashed in the process.  Kevin’s checking, if he fails I will look into it.</p>
<p>–Mike</p>

---

## Post #4 by @jcfr (2017-05-22 13:39 UTC)

<p>Thanks Mike.</p>
<p>As of 2017-05-22, the problem is addressed.</p>

---
