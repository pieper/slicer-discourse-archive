# Linux freezes completely when using 3D slicer gui

**Topic ID**: 14237
**Date**: 2020-10-25
**URL**: https://discourse.slicer.org/t/linux-freezes-completely-when-using-3d-slicer-gui/14237

---

## Post #1 by @CST (2020-10-25 12:29 UTC)

<p>Operating system: Ubunutu 18.04<br>
Slicer version: 4.10.2-linux-amd64<br>
Expected behavior: run smoothly<br>
Actual behavior: Computer freezes completely and has to be forcefully rebooted</p>
<p>Dear community,</p>
<p>I use slicer for a couple of weeks now and I realized, that my Linux (Ubuntu 18.4) is freezing quite often when I try to use Slicer 4.10.2 GUI to draw masks or inspect my data. The computer otherwise never has this issue, which is why I believe, there is a problem with my slicer. Has anyone experienced the same issue and can offer advice on how to fix this issue?</p>
<p>kind regards</p>

---

## Post #2 by @lassoan (2020-10-25 12:37 UTC)

<p>It seems that you run out of physical memory. Since latest stable version (Slicer-4.11.20200930) contains lots of improvements, including memory optimization during segmentation, this newer version will most likely run smoother.</p>
<p>If you still have problems then please send application log (menu: Help / Report a bug) of a session where you encounter freezing. If the application froze then you can restart it and choose previous session in the listbox above the log messages.</p>

---

## Post #3 by @CST (2020-10-25 13:08 UTC)

<p>Thank you for your help. Unfortunately, the log from all the sessions before it froze and from when it froze are just empty… do you have any idea why this is the case?</p>

---

## Post #4 by @lassoan (2020-10-25 13:37 UTC)

<p>It seems that on your system, the log file content is not preserved if the application that has been writing in it is forcefully terminated. Not a big issue, we just need to collect information by other means.</p>
<p>Do you have any problems with latest stable version of Slicer? What is the size of the image volume that you work with? How much RAM do you have and how much swap space have you configured for your system?</p>

---

## Post #5 by @CST (2020-10-25 13:48 UTC)

<p>I can’t tell yet, whether the newest version is creating problems, as it only happens sporadically while working. The images I work with have 90 MB. I have 122 GB free memory and 1 GB swap space…</p>

---

## Post #6 by @lassoan (2020-10-25 14:28 UTC)

<p>How many segments do you have in your segmentation? Are you using Slicer-4.11.20200930?</p>

---

## Post #7 by @CST (2020-10-26 10:31 UTC)

<p>I draw 1 mask (1 segmentation) on 1 reference image and check whether the position aligns with other images (approx. 6 images open) I now updated slicer to 4.11.20200930 the freezing occured with the 4.10.2</p>

---

## Post #8 by @CST (2020-11-04 09:42 UTC)

<p>I would like to confirm that updating Slicer to Slicer-4.11.20200930 helped. However, I think the main cause of this issue was a graphics problem (<a href="https://askubuntu.com/questions/1287108/ubuntu-18-04-freezes-frequently-and-sudo-ubuntu-drivers-autoinstall-does-not-wor" rel="noopener nofollow ugc">https://askubuntu.com/questions/1287108/ubuntu-18-04-freezes-frequently-and-sudo-ubuntu-drivers-autoinstall-does-not-wor</a>). Thanks for your help!</p>

---
