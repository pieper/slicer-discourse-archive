---
topic_id: 31311
title: "Moving Dicom Database Between Versions"
date: 2023-08-23
url: https://discourse.slicer.org/t/31311
---

# Moving DICOM Database between Versions

**Topic ID**: 31311
**Date**: 2023-08-23
**URL**: https://discourse.slicer.org/t/moving-dicom-database-between-versions/31311

---

## Post #1 by @Markb (2023-08-23 09:03 UTC)

<p>Hi all.</p>
<p>I’ve been using an earlier version of Slicer (think it was 4.11) and I had a python script to run through segments and create new outputs based on masking each segment. I was doing this on a virtual machine running Ubuntu on my home laptop at the time and the script worked great.</p>
<p>I’ve recently moved to a different system through a networked server (still running the same version of Ubuntu on a virtual machine) and I took the opportunity to move to version 5.4. Unfortunately, it wouldn’t accept my dicom database as a transfer from my existing machine, and it took around 24 hours for it to build it’s own (based on my 100 patients with 5-20 datasets each). After all that, I found that my macro no longer works, so I thought about rolling back to v4.11 but now it isn’t recognising the database built by v5.4. I assume it would again take 24hrs+ to rebuild this so I was wondering if there was a way to get it to look at the existing database?</p>
<p>Thank you</p>

---

## Post #2 by @pieper (2023-08-23 11:44 UTC)

<p>Waiting the 24 hours to rebuild the 4.11 database sounds like the practical solution.  Older versions can’t read the databases from newer versions.  Going the other way from 4.11 to 5.4 should have worked, but I’m not sure people do that.very often.</p>
<p>Most sustainable would be to port your script to 5.4.  Probably only some small changes would be needed.</p>

---

## Post #3 by @Markb (2023-08-23 11:55 UTC)

<p>Cheers. I might get that to start and at least it will be done at some point.</p>
<p>I was surprised to find the macro no longer worked, it is just python commands. Is there any documentation anywhere which might help to point me towards which commands might have changed? As far as I can tell, the segment section has changed layout but all the names appear to be consistent, so not sure why it isn’t working.</p>
<p>Thank you</p>

---

## Post #4 by @jcfr (2023-08-23 12:40 UTC)

<blockquote>
<p>I found that my macro no longer works</p>
</blockquote>
<p>As hinted by <a class="mention" href="/u/pieper">@pieper</a> , it may indeed be straightforward to fix these.</p>
<blockquote>
<p>Is there any documentation anywhere which might help to point me towards which commands might have changed?</p>
</blockquote>
<p>If you share a reproducible example, we should be able to help.</p>

---

## Post #5 by @Markb (2023-08-24 08:28 UTC)

<p>Weirdly, it just seems to work now, I’ve made no changes. Maybe something just needed a reboot or similar. Thank you both!</p>

---
