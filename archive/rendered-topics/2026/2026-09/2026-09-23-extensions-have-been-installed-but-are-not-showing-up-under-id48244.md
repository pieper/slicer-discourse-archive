---
topic_id: 48244
title: "extensions have been installed but are not showing up under 'Welcome to Slicer' dropdown"
date: 2026-09-23
url: https://discourse.slicer.org/t/48244
last_bumped: 2026-09-23T15:34:04.593Z
---

# extensions have been installed but are not showing up under 'Welcome to Slicer' dropdown

**Topic ID**: 48244
**Date**: 2026-09-23
**URL**: https://discourse.slicer.org/t/extensions-have-been-installed-but-are-not-showing-up-under-welcome-to-slicer-dropdown/48244

---

## Post #1 by @julian.macdonald (2026-09-23 14:47 UTC)

<p>Hi. Hoping someone can help.  I’ve installed 3DSlicer onto work laptop and have added various extensions (OpenDose3D, SlicerElastix and SlicerRT as examples) manually.  They show up in ‘Manage Extensions’ (although they all have ‘Version:NA’ - but when I click on ‘more’ there are details of version numbers etc.) - however they are not showing in the list of modules and can’t find using search.  I’ve looked at previous similar posts and can confirm that various .dll files are present in the folder, e.g. for SlicerRT: C:\Users\<em>username</em>\AppData\Local\slicer.org\3D Slicer 5.10.0\slicer.org\Extensions-34045\SlicerRT\lib\Slicer-5.12\cli-modules.</p>
<p>As you can see I’m using v5.10.0 and my pc has Windows 11.</p>
<p>Could it be related to work IT restrictions ?</p>
<p>many thanks</p>

---

## Post #2 by @jamesobutler (2026-09-23 15:22 UTC)

<aside class="quote no-group" data-username="julian.macdonald" data-post="1" data-topic="48244">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/edb3f5/48.png" class="avatar"> julian.macdonald:</div>
<blockquote>
<p>C:\Users\<em>username</em>\AppData\Local\slicer.org\3D Slicer 5.10.0\slicer.org\Extensions-34045\SlicerRT\lib\Slicer-5.12\cli-modules.</p>
</blockquote>
</aside>
<p>You are intermixing Slicer 5.10.0 with extensions built for Slicer 5.12. If you are manually installing extensions from file those extensions need to match the version of the app you are installing them into.</p>
<p>So if you have extension files for Slicer 5.12, you should manually install those into a Slicer 5.12.x version of the application.</p>

---

## Post #3 by @julian.macdonald (2026-09-23 15:34 UTC)

<p>Ah - obvious now you’ve pointed it out!  Many thanks.</p>

---
