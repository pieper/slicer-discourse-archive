---
topic_id: 11921
title: "Configure Slicer Settings To Be Persistent"
date: 2020-06-08
url: https://discourse.slicer.org/t/11921
---

# Configure Slicer settings to be persistent

**Topic ID**: 11921
**Date**: 2020-06-08
**URL**: https://discourse.slicer.org/t/configure-slicer-settings-to-be-persistent/11921

---

## Post #1 by @adminst (2020-06-08 06:03 UTC)

<p>Hi All<br>
On the default configuration slicer saves all settings to the user profile. Our slicer workstation is shared with many user. We do not want to configure for every user the pacs settings and others directly to the userprofile. How could we configure slicer to pe persistent to every user?</p>
<p>Thx<br>
Stefan</p>

---

## Post #2 by @pieper (2020-06-08 15:11 UTC)

<p>Hi - Probably it’s easiest just to copy the settings file to each user’s directory.  Use the <code>--settings-path</code> command line argument to find the file for a user where it’s set up as you want and then copy that to the corresponding location for the other users.</p>

---

## Post #3 by @lassoan (2020-06-08 16:13 UTC)

<p>I agree that creating a default .ini file in a login script would be probably the best option for now.</p>
<p>We are moving towards having completely localized installations (all code and .ini files stored in a single folder) because Python packages need to be installed for each user (since each user may want to use different combination of python packages, there may not be a single combination of all packages that works for all users). This would also make the application completely portable (Slicer could be added as a viewer on a DICOM CD) and allow shared configuration in a shared workstation installation, so it would provide what you need.</p>
<p>I’ve added this issue to track this request: <a href="https://github.com/Slicer/Slicer/issues/4966">https://github.com/Slicer/Slicer/issues/4966</a></p>

---

## Post #4 by @muratmaga (2020-06-08 16:32 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="11921">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We are moving towards having completely localized installations (all code and .ini files stored in a single folder)</p>
</blockquote>
</aside>
<p>Will this be targeted for 5.0 release or will be done on a rolling basis after the release of 5.0?</p>

---

## Post #5 by @lassoan (2020-06-08 17:06 UTC)

<p>This has not been decided yet. It would certainly make sense to change this in Slicer-5.0, but at the same time we don’t want to push out the release date indefinitely because we keep adding more to its scope.</p>
<p>Nevertheless, I could implement this for Windows, but others would need to test it on Linux and Mac.</p>

---
