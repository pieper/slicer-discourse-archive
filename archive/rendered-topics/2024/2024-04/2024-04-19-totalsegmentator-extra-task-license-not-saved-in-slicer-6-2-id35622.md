---
topic_id: 35622
title: "Totalsegmentator Extra Task License Not Saved In Slicer 6 2"
date: 2024-04-19
url: https://discourse.slicer.org/t/35622
---

# TotalSegmentator Extra Task License Not Saved in Slicer 6.2

**Topic ID**: 35622
**Date**: 2024-04-19
**URL**: https://discourse.slicer.org/t/totalsegmentator-extra-task-license-not-saved-in-slicer-6-2/35622

---

## Post #1 by @evaherbst (2024-04-19 14:24 UTC)

<p>Hi all,</p>
<p>I added the license for the extra tasks for TotalSegmentator as I did in previous versions.<br>
The license is added but I get prompted to restart slicer, and after restarting, the license is gone again (whereas previous versions saved the license)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5085b6e90f3b47e879c557f558ea2f6ec98dfea.png" alt="image" data-base62-sha1="uozBAJik07cvdHgd1wGRTJGrucy" width="221" height="38"></p>
<p>Thank you,<br>
Eva</p>

---

## Post #2 by @evaherbst (2024-04-22 12:59 UTC)

<p>I just double checked, in Slicer 6.1 I have the same issue. The license is accepted as in the screenshot above, but when I restart as requested, the license disappears again and the field is empty.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> should I add an issue directly in the github for TotalSegmentator Slicer extension?</p>

---

## Post #3 by @lassoan (2024-04-22 18:17 UTC)

<aside class="quote no-group" data-username="evaherbst" data-post="2" data-topic="35622">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evaherbst/48/65595_2.png" class="avatar"> evaherbst:</div>
<blockquote>
<p>The license is accepted as in the screenshot above, but when I restart as requested, the license disappears again and the field is empty.</p>
</blockquote>
</aside>
<p>You only need to set the license once (not at each startup). If the license has been successfully set then you are done, it should all work.</p>

---

## Post #5 by @evaherbst (2024-04-23 08:23 UTC)

<p>Hi Andras,</p>
<p>It says the license is accepted (see screenshot in initial post) but it is not saved.</p>
<p>I tried with the new license and it still does not work.<br>
I also tried reinstalling Slicer 5.6.2 and it also does not fix the issue.</p>
<p>It always says the license is accepted and set but it is never saved, and every time I enter it, it requires a restart, and then it isn’t saved again.</p>
<p>I see there is a totalseg_set_license.exe, I tried running just this part of the TotalSegmentator code in a separate python file and I get no issues<br>
but it does not solve my problem of the license not being saved</p>
<p>cmd = [<br>
pythonSlicerExecutablePath,<br>
totalSegmentatorLicenseToolExecutablePath,<br>
“-l”,<br>
licenseStr<br>
]</p>
<p>Do you have any ideas on how to fix this, or any other workaround? We have a project using totalSegmentator tisse_types extra weights and I am under some time pressure, so any solution would be greatly appreciated</p>

---

## Post #7 by @evaherbst (2024-04-23 10:56 UTC)

<p>I also tried uninstalling all Slicer versions, removing pip cache, removing .totalsegmentator folder in my user data, and re-installing from scratch. I am still running into the same issue</p>
<p>UPDATE:<br>
I see in the .totalsegmentator folder in Users/myusername/.totalsegmentator, the .config file has been created by the Slicer TotalSegmentator installation and my license is listed in this .config file.</p>
<p>So, the license setting seems to work, Slicer is just not accessing it whenever it gets reopened.</p>

---

## Post #8 by @lassoan (2024-04-23 12:47 UTC)

<aside class="quote no-group" data-username="evaherbst" data-post="7" data-topic="35622">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evaherbst/48/65595_2.png" class="avatar"> evaherbst:</div>
<blockquote>
<p>So, the license setting seems to work, Slicer is just not accessing it whenever it gets reopened.</p>
</blockquote>
</aside>
<p>The module works the same way as most other software that requires a registration key: you need to provide a license key file to register the software once, then you never need to enter that key again. Do you find it confusing that the license key selector is not hidden after entering the license? Or it would be more intuitive if the license number was entered in a popup window?</p>

---

## Post #9 by @evaherbst (2024-04-23 13:09 UTC)

<p>Hi Andras,</p>
<p>Apologies for my confusion.<br>
In a previous version, the license number was saved in the TotalSegmentator license number box.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb4f97d6ad39a4e5ecc46fd002823cd45c565893.png" alt="image" data-base62-sha1="t0zs94vt8hlhZkIpLUpgOz4dSUP" width="426" height="213"></p>
<p>The fact that this was now empty made me think the license was not saved when indeed it was.</p>
<p>But you are right, internally the key was saved, I just tried running it and it works.<br>
I was just confused that the box remained empty.</p>
<p>Thanks,<br>
Eva</p>

---

## Post #10 by @lassoan (2024-04-23 13:42 UTC)

<p>OK. To make the behavior more clear, I’ve now moved the license key inputbox into a popup window that is displayed when the button is clicked.</p>

---

## Post #11 by @evaherbst (2024-04-24 09:08 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I tested this and the popup works.<br>
However, it was not the location of entering the license that was confusing, but the fact that even when the license was saved internally, when you reopen Slicer, the license field is empty.<br>
So it looks like it has not been saved (even though for the purposes for running the application it has). You can see below what it looks like (even when the license is saved and the extra tasks run)&gt;</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb4f97d6ad39a4e5ecc46fd002823cd45c565893.png" alt="image" data-base62-sha1="t0zs94vt8hlhZkIpLUpgOz4dSUP" width="426" height="213"></p>
<p>It is not a big issue but it did make me think the license wasn’t being saved.</p>
<p>Thanks,<br>
Eva</p>

---

## Post #12 by @lassoan (2024-04-24 12:42 UTC)

<p>It seems that you have not updated to the latest TotalSegmentator extension version yet. There is no longer a license number field that is always displayed.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fcff9d24423decc166a0d0dc8b8fac07e7d9b0f.png" data-download-href="/uploads/short-url/fX8AiuhAPBud3JdbPGEDtDUZJN5.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fcff9d24423decc166a0d0dc8b8fac07e7d9b0f_2_690x252.png" alt="image" data-base62-sha1="fX8AiuhAPBud3JdbPGEDtDUZJN5" width="690" height="252" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fcff9d24423decc166a0d0dc8b8fac07e7d9b0f_2_690x252.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fcff9d24423decc166a0d0dc8b8fac07e7d9b0f_2_1035x378.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fcff9d24423decc166a0d0dc8b8fac07e7d9b0f_2_1380x504.png 2x" data-dominant-color="453F42"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1563×573 32.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To get the latest version, install the latest Slicer Preview Release or latest Slicer Stable Release and install/update TotalSegmentator extension.</p>

---

## Post #13 by @evaherbst (2024-05-02 08:07 UTC)

<p>Ok, thank you Andres!</p>

---

## Post #14 by @bulala (2025-09-29 09:30 UTC)

<p>When I use the license, an error occurs. Could you please tell me how to solve it? Also, if the license is successfully activated, will the license option still show as empty, or will it display the license information?</p>
<p><em>(image removed, as it might have contained license number)</em></p>

---

## Post #15 by @lassoan (2025-09-29 17:41 UTC)

<p>Thanks for reporting. I’ve fixed the issue (it was introduced by a recent change that made the module translatable to different languages). If you update the extension tomorrow then it should not throw any errors when you are setting the license key.</p>

---

## Post #16 by @bulala (2025-09-30 01:16 UTC)

<p>ok, thank you a lot, I will update the extension.</p>

---
