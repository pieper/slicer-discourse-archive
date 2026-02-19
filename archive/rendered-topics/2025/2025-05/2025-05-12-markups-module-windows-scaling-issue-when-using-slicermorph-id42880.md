---
topic_id: 42880
title: "Markups Module Windows Scaling Issue When Using Slicermorph"
date: 2025-05-12
url: https://discourse.slicer.org/t/42880
---

# Markups module windows scaling issue when using Slicermorph customizations

**Topic ID**: 42880
**Date**: 2025-05-12
**URL**: https://discourse.slicer.org/t/markups-module-windows-scaling-issue-when-using-slicermorph-customizations/42880

---

## Post #1 by @Logan_Moore (2025-05-12 01:09 UTC)

<p>Hi all,</p>
<p>My lab recently got a 4K monitor, and we are having issues placing landmarks. I found that <a class="mention" href="/u/muratmaga">@muratmaga</a> previously reported this as an issue on Github: <a href="https://github.com/SlicerMorph/SlicerMorph/issues/156" class="inline-onebox" rel="noopener nofollow ugc">Points placed incorrectly with the 'p' shortcut when display scaling is &gt;100 · Issue #156 · SlicerMorph/SlicerMorph · GitHub</a>. I noticed it was closed without follow-up, and I don’t see a similar report or further discussion.</p>
<p>Was the update solution submitted and perhaps broken in a later version? Switching to 100% scaling does resolve the issue for now.</p>
<p>I’m on Slicer 5.8 and Slicermorph 5e6ffae.</p>
<p>Thanks!<br>
Logan</p>

---

## Post #2 by @muratmaga (2025-05-12 01:27 UTC)

<p>That issue is 4 years old, and I think we closed because it no longer happens on windows (or at least we don’t encounter it in a reproducible way).</p>
<p>One thing to consider, in some windows applications (and I think Slicer is one of them), if you modified the scaling, you will need to log out of windows and and log back in for things to scale correctly in the application.</p>

---

## Post #3 by @Logan_Moore (2025-05-12 01:45 UTC)

<p>Yes, I bring it up again because I am actively experiencing it now.</p>
<p>Here is a short video showing the issue at 150% Windows scaling<br>
<iframe src="https://clips.twitch.tv/embed?clip=ColdKindSharkEagleEye-djrfXo8oj0SOk5hA&amp;parent=discourse.slicer.org&amp;autoplay=false" width="620" height="378" frameborder="0" style="overflow: hidden;" scrolling="no" allowfullscreen="allowfullscreen" seamless="seamless" sandbox="allow-same-origin allow-scripts allow-forms allow-popups allow-popups-to-escape-sandbox allow-presentation"></iframe>
</p>
<p>Here it is again with Slicer relaunched and Windows at 100% scaling<br>
<iframe src="https://clips.twitch.tv/embed?clip=SparklingEagerAlbatrossShadyLulu-dxgHdfqBiShQ0tn2&amp;parent=discourse.slicer.org&amp;autoplay=false" width="620" height="378" frameborder="0" style="overflow: hidden;" scrolling="no" allowfullscreen="allowfullscreen" seamless="seamless" sandbox="allow-same-origin allow-scripts allow-forms allow-popups allow-popups-to-escape-sandbox allow-presentation"></iframe>
</p>
<p>You can see that it goes away completely. I could not find a more recent thread with the issue. I didn’t modify the scaling just for the Slicer app; I could do that. But switching between 150% and 100% Windows scaling replicates this issue for me so far, 100% of the time.</p>

---

## Post #4 by @muratmaga (2025-05-12 01:45 UTC)

<p>Did you log out and login back between changing the scales?</p>

---

## Post #5 by @Logan_Moore (2025-05-12 01:46 UTC)

<p>I did close and reopen Slicer between changing the scales</p>

---

## Post #6 by @muratmaga (2025-05-12 01:47 UTC)

<p>No, I mean log out of windows and login back into Windows. Not just the application.</p>

---

## Post #7 by @Logan_Moore (2025-05-12 01:47 UTC)

<p>I did not, but I can do that and follow up with you</p>

---

## Post #8 by @muratmaga (2025-05-12 01:49 UTC)

<p>This is a very specific issue on windows and we don’t have much control over. usually login out (after changing the resolution) and login back in solves some of the issues (as per microsoft: <a href="https://support.microsoft.com/en-us/topic/windows-scaling-issues-for-high-dpi-devices-surface-pro-3-surface-pro-4-or-surface-book-508483cd-7c59-0d08-12b0-960b99aa347d" class="inline-onebox" rel="noopener nofollow ugc">Windows scaling issues for high-DPI devices (Surface Pro 3, Surface Pro 4, or Surface Book) - Microsoft Support</a>)</p>

---

## Post #9 by @Logan_Moore (2025-05-12 01:58 UTC)

<p>I see, thank you for the link.</p>
<p>To help anyone else who may run into this issue, I will highlight the two ways I have circumvented it.</p>
<ol>
<li>
<p>Change Windows scaling to 100%. This makes the text a little small on a 4K monitor, but the text size can be increased in Slicer.</p>
</li>
<li>
<p>Temporarily change your 4K monitor resolution to 2560x1440p or 1920x1080p while collecting data.</p>
</li>
</ol>

---

## Post #10 by @jamesobutler (2025-05-12 02:38 UTC)

<p><a class="mention" href="/u/logan_moore">@Logan_Moore</a> Did logging out of Windows after changing the scaling help you? Or did it not?</p>

---

## Post #11 by @Logan_Moore (2025-05-12 02:50 UTC)

<p>Sorry, James, I had to step out for a minute and forgot to test this.</p>
<p>I set scaling to 100% and 150% on two separate runs. So the order of operations was change scaling → sign out → sign in → open and test Slicer, and then repeat for the other option.</p>
<p>Both options, 100% and 150%, acted exactly as shown in the above videos.</p>

---
