# Downloading older releases: need to update "Older releases" link?

**Topic ID**: 9015
**Date**: 2019-11-04
**URL**: https://discourse.slicer.org/t/downloading-older-releases-need-to-update-older-releases-link/9015

---

## Post #1 by @fedorov (2019-11-04 21:10 UTC)

<p>For the second time in the last few months I had a need to download an older nightly of Slicer (as a way to mitigate surprises for the users).</p>
<p>Today, as before, my first instinct was to go to the “Older releases” link on <a href="http://download.slicer.org">download.slicer.org</a>, only to be reminded that it is useless (points to a Midas instance, with no folder for 4.11.0).</p>
<p>I suggest “Older releases” link should be changed to point to this wiki page instead: <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/General#Where_can_I_download_Slicer.3F">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/General#Where_can_I_download_Slicer.3F</a>.</p>
<p>This entry should also be updated probably: <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/General#Where_can_I_download_older_release_of_Slicer_.3F">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/General#Where_can_I_download_older_release_of_Slicer_.3F</a>, but since I do not know how things are organized (it seems like new packages do not go to Midas, but it may also be that I just don’t know how to find them there), I don’t know what should be the actual instructions.</p>

---

## Post #2 by @Sam_Horvath (2019-11-04 21:21 UTC)

<p>So, nightly packages are still uploaded to Midas, but to <a href="http://slicer.kitware.com/midas3/folder/251">this</a> folder, which unfortunately holds ALL of the Slicer4 nightlies, and so it’s pretty much unbrowsable.</p>
<p>You will probably get the best result locating older packages by searching for the package name / date, ex something like</p>
<blockquote>
<p>Slicer-4.11.0-2019-11-04</p>
</blockquote>
<p>ex: <a href="http://slicer.kitware.com/midas3/search/index?q=Slicer-4.11.0-2019-11-04">http://slicer.kitware.com/midas3/search/index?q=Slicer-4.11.0-2019-11-04</a>, or by using the instructions in the first link FAQ link you posted</p>
<p>The “older release” current instructions (second FAQ link) are still correct, but only for actual releases, not nightly versions.</p>

---

## Post #3 by @fedorov (2019-11-04 21:34 UTC)

<p>Thanks. If we keep the current “Older releases” link at <a href="http://download.slicer.org">download.slicer.org</a>, I hope those who need this functionality are able to find this thread.</p>
<p>In my case, the most useful is the ability to use <code>release</code> URL attribute - this allows me to easily locate the same package I have on my system and share it with the users.</p>

---

## Post #4 by @Sam_Horvath (2019-11-04 21:38 UTC)

<p>I will look into adding a “older previews” link that will point to the FAQ</p>

---

## Post #5 by @mhalle (2019-11-05 00:44 UTC)

<p>Using the URL parameters for <a href="http://download.slicer.org" rel="nofollow noopener">download.slicer.org</a> as described in the FAQ, you can get nightly versions by setting stability=nightly or stability=any . I’ve confirmed it works.  The date parameters also work to get nightlies.</p>

---

## Post #6 by @mhalle (2019-11-05 00:52 UTC)

<p>I’ve made this change to the older releases link.</p>

---
