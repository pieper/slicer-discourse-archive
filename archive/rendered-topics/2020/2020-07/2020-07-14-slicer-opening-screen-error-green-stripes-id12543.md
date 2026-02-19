---
topic_id: 12543
title: "Slicer Opening Screen Error Green Stripes"
date: 2020-07-14
url: https://discourse.slicer.org/t/12543
---

# Slicer opening screen error - Green Stripes

**Topic ID**: 12543
**Date**: 2020-07-14
**URL**: https://discourse.slicer.org/t/slicer-opening-screen-error-green-stripes/12543

---

## Post #1 by @Nicholas.jacobson (2020-07-14 23:08 UTC)

<p>Hey. Today, upon opening slicer my program is showing striped green lines across the entire program. Yesterday the program worked and nothing has changed overnight. I uninstalled and reinstalled, restarted, and did everything I know to do. Any advice?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13923882185ecbd1b187f9ac232a8eaa747d2053.png" data-download-href="/uploads/short-url/2N8lBjV9EY6udbiz6nXphdtEYfh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13923882185ecbd1b187f9ac232a8eaa747d2053_2_690x370.png" alt="image" data-base62-sha1="2N8lBjV9EY6udbiz6nXphdtEYfh" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13923882185ecbd1b187f9ac232a8eaa747d2053_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13923882185ecbd1b187f9ac232a8eaa747d2053_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13923882185ecbd1b187f9ac232a8eaa747d2053_2_1380x740.png 2x" data-dominant-color="8FBC97"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1032 73 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jamesobutler (2020-07-14 23:41 UTC)

<p>This other thread looks familiar.  Read and see if the solution there will help you as well.</p><aside class="quote quote-modified" data-post="1" data-topic="12090">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/4bbf92/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/bug-with-slicer/12090">Green horizontal lines appear in Slicer-4.10.2 at startup</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Operating system: Windows 10 i7 
Slicer version: 4.10.2 
Hi all 
I have been using slicer with my pc for quite sometime. However, out of the blue, the following happen to my slicer as shown in the image  below. I had tried reinstalling it but it does not work. Do you have any idea what is happening? 
Thank you 
[image]
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2020-07-15 04:19 UTC)

<p>Most likely application window position saved your application settings has become invalid either because you had Slicer displayed on an external monitor that you since have disconnected; or the entire Slicer*.ini file became corrupted due to an application crash. Deleting you Slicer*.ini files will fix the issue.</p>
<p>However, before you delete those files, it would be great if you could share them with us (upload to dropbox/onedrive/gdrive and post the link) so that we can investigate and prevent such errors in the future.</p>

---

## Post #4 by @Nicholas.jacobson (2020-07-15 18:14 UTC)

<p>Thanks but can you tell me where I can find the .ini files? I seem to be struggle to locate them on my CPU. The issue must be from this because I did not connect to any other devices.</p>

---

## Post #5 by @pieper (2020-07-15 18:27 UTC)

<p><code>Slicer --settings-path</code></p>

---

## Post #6 by @lassoan (2020-07-16 03:58 UTC)

<p>On Windows, Slicer does not write on the console by default, so you need to run the output through some other software that does. For example, <code>more</code> works:</p>
<pre><code>Slicer --settings-path | more
</code></pre>
<p>What Windows version are you using? What hardware? A laptop with a discrete NVidia graphics card?</p>
<p>Does the latest Slicer Preview Release work?</p>
<p>Does Slicer work correctly after you rename/remove Slicer.ini?</p>

---

## Post #7 by @AT3432984 (2020-07-17 04:09 UTC)

<p>Hi,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f23d5ed1345aaaae697340721c94409df0c9ab9.png" data-download-href="/uploads/short-url/29VWfKevvzEej9OUC1PdOyXvBjj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0f23d5ed1345aaaae697340721c94409df0c9ab9_2_690x388.png" alt="image" data-base62-sha1="29VWfKevvzEej9OUC1PdOyXvBjj" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0f23d5ed1345aaaae697340721c94409df0c9ab9_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0f23d5ed1345aaaae697340721c94409df0c9ab9_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0f23d5ed1345aaaae697340721c94409df0c9ab9_2_1380x776.png 2x" data-dominant-color="74A876"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3840×2160 856 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am having trouble when opening 3D Slicer. I have had this program for a while and it always works fine, but now when I open it I get a bunch of green lines across the screen. I have looked at the following 2 pages but I still can’t seem to fix it.</p>
<aside class="quote quote-modified" data-post="1" data-topic="12543">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/ba8739/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-opening-screen-error-green-stripes/12543">Slicer opening screen error - Green Stripes</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hey. Today, upon opening slicer my program is showing striped green lines across the entire program. Yesterday the program worked and nothing has changed overnight. I uninstalled and reinstalled, restarted, and did everything I know to do. Any advice? 
[image]
  </blockquote>
</aside>
<aside class="quote quote-modified" data-post="1" data-topic="12090">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/4bbf92/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/bug-with-slicer/12090">Green horizontal lines appear in Slicer-4.10.2 at startup</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Operating system: Windows 10 i7 
Slicer version: 4.10.2 
Hi all 
I have been using slicer with my pc for quite sometime. However, out of the blue, the following happen to my slicer as shown in the image  below. I had tried reinstalling it but it does not work. Do you have any idea what is happening? 
Thank you 
[image]
  </blockquote>
</aside>

<p>I have uninstalled and re-installed the program several times. I can’t seem to find where the .ini files are to delete them.</p>
<p>I have also tried this but I nothing shows up and I cant find the path</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70bd966710f0c191450fad51ca8d0e901a0a35ad.png" data-download-href="/uploads/short-url/g5lFik9nar1juwFWNAeOauAXC7X.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70bd966710f0c191450fad51ca8d0e901a0a35ad_2_689x59.png" alt="image" data-base62-sha1="g5lFik9nar1juwFWNAeOauAXC7X" width="689" height="59" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70bd966710f0c191450fad51ca8d0e901a0a35ad_2_689x59.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70bd966710f0c191450fad51ca8d0e901a0a35ad_2_1033x88.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70bd966710f0c191450fad51ca8d0e901a0a35ad_2_1378x118.png 2x" data-dominant-color="000E00"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2388×207 9.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2020-07-17 04:38 UTC)

<p><a class="mention" href="/u/at3432984">@AT3432984</a></p>
<p>Since nothing has changed in Slicer-4.10.2 on your computer, it might be a configuration issue, but since multiple people encountered this in the last few days, it is getting more likely the problem is caused by an operating system or graphics card driver update. As a first step, it would be very useful if we could confirm this and find out exactly what change caused the issue.</p>
<p>What Windows version are you using? What hardware? A laptop with a discrete NVidia graphics card?</p>
<p>Does the latest Slicer Preview Release work?</p>
<p>Does Slicer work correctly after you rename/remove Slicer.ini? (to get your settings path, copy-paste this into a command prompt: <code>"c:\Program Files\Slicer 4.10.2\Slicer.exe" --settings-path | more</code>)</p>

---

## Post #9 by @lassoan (2020-07-17 04:49 UTC)

<p>Note that seems to happen with other software, too, such as Adobe After Effects:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://community.adobe.com/t5/image/serverpage/image-id/109601i940D191F3057EA10/image-size/large?v=1.0&amp;px=999" title=""><img src="https://community.adobe.com/t5/image/serverpage/image-id/109601i940D191F3057EA10/image-size/large?v=1.0&amp;px=999" alt="" width="690" height="392"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use xlink:href="#far-image"></use></svg><span class="filename"></span><span class="informations">999×568</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use xlink:href="#discourse-expand"></use></svg></div></a></div><br>
(source: <a href="https://community.adobe.com/t5/after-effects/a-bunch-of-horizontal-green-lines-won-t-go-away-on-my-composition-screen-when-i-open-up-any-video/td-p/11223965?page=1">https://community.adobe.com/t5/after-effects/a-bunch-of-horizontal-green-lines-won-t-go-away-on-my-composition-screen-when-i-open-up-any-video/td-p/11223965?page=1</a>)</p>
<p>There are lots of complaints for this latest Intel graphics driver causing these green horizontal lines appear in various software  - see these: <a href="https://www.reddit.com/r/premiere/comments/gzk1r8/how_can_i_solve_this_problem_black_and_green/">1</a>, <a href="https://adobe-video.uservoice.com/forums/911311-after-effects/suggestions/40712056-green-horizontal-lines-in-preview-of-ae-and-premie">2</a>, <a href="https://community.adobe.com/t5/premiere-pro/green-horizontal-lines-amp-distorted-colors/td-p/11188074?page=1">3</a>, <a href="https://community.adobe.com/t5/premiere-pro/green-horizontal-lines-in-my-source-monitor-please-help/td-p/11214905?page=1">4</a>, <a href="https://community.adobe.com/t5/after-effects/a-bunch-of-horizontal-green-lines-won-t-go-away-on-my-composition-screen-when-i-open-up-any-video/td-p/11223965?page=1">5</a>.</p>
<p>Recommended solution there is to either upgrade or downgrade your graphics driver to a different version that does not have this bug (but before that, trying to delete Slicer application settings .ini files would worth a shot, too).</p>

---

## Post #10 by @AT3432984 (2020-07-17 05:07 UTC)

<p>I have a Dell laptop running Windows 10 with Intel® UHD Graphics 620 (don’t have a NVidia graphics card). I am having the same issues with the latest Slicer preview release (4.11.0)</p>
<p>I deleted Slicer.ini, but as soon as I try and re-open Slicer, the Slicer.ini file comes back.</p>
<p>I have also tried re-naming NA-MIC to NA-MIC-backup and that didn’t work either</p>

---

## Post #11 by @lassoan (2020-07-17 05:50 UTC)

<aside class="quote no-group" data-username="AT3432984" data-post="10" data-topic="12543">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f04885/48.png" class="avatar"> AT3432984:</div>
<blockquote>
<p>I deleted Slicer.ini, but as soon as I try and re-open Slicer, the Slicer.ini file comes back.</p>
</blockquote>
</aside>
<p>That’s normal, by deleting Slicer.ini you have reset your settings to defaults.</p>
<aside class="quote no-group" data-username="AT3432984" data-post="10" data-topic="12543">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f04885/48.png" class="avatar"> AT3432984:</div>
<blockquote>
<p>I have a Dell laptop running Windows 10 with Intel® UHD Graphics 620 (don’t have a NVidia graphics card). I am having the same issues with the latest Slicer preview release (4.11.0)</p>
</blockquote>
</aside>
<p>This makes it highly probable that Slicer has run into the same driver issue as Adobe and other software. What is your graphics driver version?</p>

---

## Post #12 by @AT3432984 (2020-07-17 06:08 UTC)

<p>Graphic driver version is 27.20.100.8280</p>

---

## Post #13 by @lassoan (2020-07-17 16:37 UTC)

<p>This is the exact driver version that caused this problem in other software, too (see <a href="https://adobe-video.uservoice.com/forums/911311-after-effects/suggestions/40712056-green-horizontal-lines-in-preview-of-ae-and-premie">here</a>).</p>
<p>It seems that your only option is to get rid of this driver and replace it with an older version or a newer beta version.</p>

---

## Post #14 by @Nicholas.jacobson (2020-07-17 17:13 UTC)

<p>Great. Thank you andras. Sorry for the delay. I will try this today! Thank you so much.</p>

---

## Post #15 by @AT3432984 (2020-07-19 09:12 UTC)

<p>Thank you, this worked</p>

---

## Post #16 by @mattmi (2020-08-14 16:02 UTC)

<p>Hi,<br>
This happened to me today after a Windows 10 update I received.  I understand I will need to investigate up/downgraded drivers but in case it is interesting to the dev team, I found this:<br>
Faulting application name: SlicerApp-real.exe, version: 0.0.0.0, time stamp: 0x5cddc587<br>
Faulting module name: ig9icd64.dll, version: 26.20.100.7812, time stamp: 0x5e280fb1<br>
Exception code: 0xc0000005<br>
Fault offset: 0x0000000000040003<br>
Faulting process id: 0x14ec<br>
Faulting application start time: 0x01d6716dc1779a63<br>
Faulting application path: C:\Program Files\Slicer 4.10.2\bin\SlicerApp-real.exe<br>
Faulting module path: C:\WINDOWS\System32\DriverStore\FileRepository\igdlh64.inf_amd64_915651e73d639c22\ig9icd64.dll<br>
Report Id: 762b8418-9e5c-45d5-bfa7-9263f491ceeb</p>
<p>Best…</p>

---

## Post #17 by @lassoan (2020-08-14 18:34 UTC)

<p>Thank you for reporting this. This confirms that the bug is in Intel graphics driver. To fix this, I don’t see any other option than upgrading/downgrading the Intel graphics driver to a different version.</p>

---

## Post #18 by @dayanjan (2020-10-05 20:14 UTC)

<p>I hope this helps the community. I just used this to fix the problem on my computer</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <a href="https://community.intel.com/t5/Graphics/Request-for-details-on-Intel-HD-630-green-lines-in-OpenGL-apps/td-p/1202179" target="_blank" rel="noopener nofollow ugc" title="06:02PM - 20 August 2020">community.intel.com – 20 Aug 20</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="" height="">

<h3><a href="https://community.intel.com/t5/Graphics/Request-for-details-on-Intel-HD-630-green-lines-in-OpenGL-apps/td-p/1202179" target="_blank" rel="noopener nofollow ugc">Request for details on Intel HD 630 green lines in OpenGL apps</a></h3>

<p>Dear Intel, I'm a game developer and I'd like to have a few more details about the "Green Lines" issue that recently surfaced across the globe with one of your latest drivers release (one report of the issue is...</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
