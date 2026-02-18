# Slicer not starting at all on laptop

**Topic ID**: 26444
**Date**: 2022-11-25
**URL**: https://discourse.slicer.org/t/slicer-not-starting-at-all-on-laptop/26444

---

## Post #1 by @NotASlicerUser (2022-11-25 18:26 UTC)

<p>System is running a Ryzen 5 3500u with an integrated graphics card, 8gb of ram and windows 10 x64bit.<br>
Slicer will not even start an instance. We’ve tried clean new installs, running as admin but nothing seemingly works. System should meet minimal requirements but something else seems to be the problem. The version installed is 5.0.3.<br>
Any ideas as to what may be causing this problem ?</p>

---

## Post #2 by @lassoan (2022-11-25 18:36 UTC)

<p>Please try the followings:</p>
<ul>
<li>try if latest Slicer Preview Release works</li>
<li>is this a Dell computer? you may run into this recent <a href="https://github.com/Slicer/Slicer/issues/6568#issuecomment-1271932395">driver issue</a>
</li>
<li>try the instructions described <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#slicer-application-does-not-start">here</a> - they contain description of all the Windows startup issues that we have encountered in recent years and instruction for resolving them</li>
</ul>

---

## Post #3 by @NotASlicerUser (2022-11-26 10:20 UTC)

<p>It’s not a dell pc, it’s a huawei. I’ll try what you’ve listed and get back.</p>

---

## Post #4 by @NotASlicerUser (2022-11-27 15:19 UTC)

<p>So I’ve tried installing again with the latest versions of the cpu drivers, still not working.<br>
I can’t seem to find the settings for Slicer for the life of me withing the AppData foldier, can’t find the foldier itself too.<br>
I tried the event viewer thing, but can’t seem to find Slicer since it’s not even starting or creating a proccess to find its set path. Still pretty lost on how to run Slicer.</p>

---

## Post #5 by @lassoan (2022-11-27 16:04 UTC)

<aside class="quote no-group" data-username="NotASlicerUser" data-post="4" data-topic="26444">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/8edcca/48.png" class="avatar"> NotASlicerUser:</div>
<blockquote>
<p>I can’t seem to find the settings for Slicer for the life of me withing the AppData foldier, can’t find the foldier itself too.</p>
</blockquote>
</aside>
<p>On Windows, the AppData folder is hidden by default. You can enable showing hidden/system files or simply type <code>%appdata%</code> in the path selector in File Explorer:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88508a16cda449be897c2747192a0b9a677f47d5.jpeg" data-download-href="/uploads/short-url/jrTuqUzM5Hm9xlEcZc1r1OO1ILH.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88508a16cda449be897c2747192a0b9a677f47d5_2_690x307.jpeg" alt="image" data-base62-sha1="jrTuqUzM5Hm9xlEcZc1r1OO1ILH" width="690" height="307" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88508a16cda449be897c2747192a0b9a677f47d5_2_690x307.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88508a16cda449be897c2747192a0b9a677f47d5_2_1035x460.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88508a16cda449be897c2747192a0b9a677f47d5_2_1380x614.jpeg 2x" data-dominant-color="1E2020"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1691×754 90 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @NotASlicerUser (2022-11-27 19:00 UTC)

<p>I’ll try again tomorrow and if I can’t do it then we can try and schedule a teamviewer session.<br>
I’m in GMT +2 timezone so anywhere between 6pm to 10 pm would be a fine time, so around 11am to 3pm for you.</p>

---

## Post #7 by @NotASlicerUser (2022-11-28 15:49 UTC)

<p>So a little update, still couldn’t fix the issue myself so any help would be appreciated. As stated we live in GMT+2, I’ve listed the hours that are comfortable and I would be happy if we could fix the issue in the following days.</p>

---

## Post #8 by @jamesobutler (2022-11-28 16:33 UTC)

<p>From <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html:" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/get_help.html:</a></p>
<blockquote>
<ul>
<li>Your computer CPU or graphics capabilities may not meet <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#system-requirements" rel="noopener nofollow ugc">minimum system requirements</a>.</li>
<li>Slicer may not work if it is installed in a folder that has special characters in their name. Try installing Slicer in a path that only contains latin letters and numbers (a-z, 0-9).</li>
<li>Your Slicer settings might have become corrupted
<ul>
<li>Try launching Slicer using <code>Slicer.exe --disable-settings</code> (if it fixes the problem, delete Slicer.ini and Slicer-.ini files from your Slicer settings directory.</li>
<li>Rename or remove your Slicer settings directory (for example, <code>c:\Users\&lt;yourusername&gt;\AppData\Roaming\NA-MIC</code>). See instructions for getting the settings directory <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#settings-file-location" rel="noopener nofollow ugc">here</a>. Try to launch Slicer.</li>
</ul>
</li>
</ul>
</blockquote>
<aside class="quote no-group" data-username="NotASlicerUser" data-post="4" data-topic="26444">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/8edcca/48.png" class="avatar"> NotASlicerUser:</div>
<blockquote>
<p>I can’t seem to find the settings for Slicer for the life of me withing the AppData foldier, can’t find the foldier itself too.</p>
</blockquote>
</aside>
<p>Did you go to the location mentioned in the Get Help section? (for example, <code>c:\Users\&lt;yourusername&gt;\AppData\Roaming\NA-MIC</code>). You can go to this location directly by going to Window start → Run → then typing %AppData%/NA-MIC and pressing enter.</p>
<p>Can you also confirm, re the 2nd bullet point in the Get Help section, that Slicer is not installed in a folder path that contains special characters? Since Slicer is by default installed into the user space, does your username contain special characters? Your username is path of the folder path where Slicer is installed by default.</p>
<p>If you go to Windows Settings-&gt;System-&gt;About, what is the edition and version of Windows 10 that you are running? For example, Edition “Windows 10 Pro” and version “22H2”.</p>

---
