---
topic_id: 22233
title: "Fast Share S4 Sources Between Two Development Computers On W"
date: 2022-03-01
url: https://discourse.slicer.org/t/22233
---

# Fast share S4 sources between two development computers on Windows

**Topic ID**: 22233
**Date**: 2022-03-01
**URL**: https://discourse.slicer.org/t/fast-share-s4-sources-between-two-development-computers-on-windows/22233

---

## Post #1 by @rbumm (2022-03-01 13:57 UTC)

<p>Maybe trivial, but I found it too time-consuming to use Github and daily commits to exchange recent source changes on two rapidly changing developing locations (windows). Can’t use RDP all the time.<br>
I created a folder “S4” on my dropbox.</p>
<p>After making source changes, I run</p>
<p>backup_to_dropbox.bat:</p>
<pre><code class="lang-auto">xcopy "C:\D\S4\*.cxx" "C:\Users\Yourname\Dropbox\S4\" /D /E /Y 
xcopy "C:\D\S4\*.cpp" "C:\Users\Yourname\Dropbox\S4\" /D /E /Y 
xcopy "C:\D\S4\*.h" "C:\Users\Yourname\Dropbox\S4\"  /D /E /Y 
xcopy "C:\D\S4\*.ui" "C:\Users\Yourname\Dropbox\S4\" /D /E /Y 
xcopy "C:\D\S4\*.py" "C:\Users\Yourname\Dropbox\S4\" /D /E /Y 
xcopy "C:\D\S4\*.txt" "C:\Users\Yourname\Dropbox\S4\" /D /E /Y 
pause
</code></pre>
<p>This will transfer the recently changed source files (and only them)  from my Slicer build directory to my Dropbox directory.<br>
On the other system, I run</p>
<p>import_from_dropbox.bat:</p>
<pre><code class="lang-auto">xcopy "C:\Users\Yourname\Dropbox\S4\*.cxx" "C:\D\S4\" /D /E /Y 
xcopy "C:\Users\Yourname\Dropbox\S4\*.cpp" "C:\D\S4\" /D /E /Y 
xcopy "C:\Users\Yourname\Dropbox\S4\*.h" "C:\D\S4\"  /D /E /Y 
xcopy "C:\Users\Yourname\Dropbox\S4\*.ui" "C:\D\S4\" /D /E /Y 
xcopy "C:\Users\Yourname\Dropbox\S4\*.py" "C:\D\S4\" /D /E /Y 
xcopy "C:\Users\Yourname\Dropbox\S4\*.txt" "C:\D\S4\" /D /E /Y 
pause
</code></pre>
<p>and transfer all recently changed source files to my other different computer.<br>
This minimizes Slicer compile times on both.<br>
Only when I am ready to commit to Github do I do this - preferably always from the same of the two development systems to avoid the Github vertigo.</p>

---

## Post #2 by @hherhold (2022-03-01 14:59 UTC)

<p>Not sure if this is useful or not, but I use an app called Beyond Compare from Scooter Software (<a href="https://www.scootersoftware.com" rel="noopener nofollow ugc">https://www.scootersoftware.com</a>) to sync all kinds of files between multiple computers (Mac, PC, etc). It’s cross-platform, and even has diff/merge capabilities, including for many image types. Works very well with large files and large numbers of files.</p>
<p>Disclaimer - I don’t work for them, I didn’t get the software for free, etc. I’m just a fan.</p>

---

## Post #3 by @lassoan (2022-03-01 18:04 UTC)

<p>Some people go to the extreme and say that if you cannot commit something that works at the end of the day then delete those changes and start again the next day from scratch. The rationale is that by not being able to wrap up your change in a day means that you were not focused enough and made too big of a change at once and there is a high chance that you have made mistakes. I would not recommend to follow this advice literally (maybe you don’t have a full day to work on something, and one day may be just too short for some things), but that’s a good target to shoot for.</p>
<p>Committing your changes at the end of the day (or a working session) is also useful as a checkpoint that you can go back to.</p>
<p>Frequent commits also an easy way to allow collaborators to see your progress. But you can use a private repository if you don’t want others to see what you are working on.</p>
<p>Git commit, push, pull take just a few clicks. If you find that how you use git is inconvenient then you can try different git clients. I use tortoisegit, as it exposes all git features and it is still reasonably convenient; but there is GitHub desktop and various Visual Studio Code plugins that make these operations even easier.</p>
<p>I would only recommend source code synchronization using dropbox for the special cases when you need continuous real-time mirroring of the source code, such as for an online pair programming session.</p>

---

## Post #4 by @rbumm (2022-03-01 18:07 UTC)

<p>Very good comments, thank you. I am using tortoisegit, still running into problems here and there with commits from two different systems in particular keeping the 1 commit rule as well as the cosmetic rules on Slicer pull requests, as soon as the PR is made.</p>

---
