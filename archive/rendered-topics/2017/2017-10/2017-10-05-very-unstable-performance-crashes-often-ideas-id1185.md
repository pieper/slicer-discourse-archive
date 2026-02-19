---
topic_id: 1185
title: "Very Unstable Performance Crashes Often Ideas"
date: 2017-10-05
url: https://discourse.slicer.org/t/1185
---

# Very unstable performance/crashes often, ideas?

**Topic ID**: 1185
**Date**: 2017-10-05
**URL**: https://discourse.slicer.org/t/very-unstable-performance-crashes-often-ideas/1185

---

## Post #1 by @Eduard_Pop (2017-10-05 16:04 UTC)

<p>I really love the program  (tried 4.6 and 4.7) but it runs very unstable on my system (i7 2700k, 16 GB ram, Geforce 550 ti 1GB). I use about a 1000 tiff files of 800 kb each.</p>
<p>Am I asking too much of my system, and therefore get the “not responding” message very often?<br>
Do you maybe have a solution? At the moment it is very difficult to work with.</p>
<p>Thanks in advance for any suggestions!</p>

---

## Post #2 by @lassoan (2017-10-05 17:50 UTC)

<p>Crashes and hangs are extremely rare in recent versions of Slicer and they are almost always due to running out of memory.</p>
<p>Probably your tiff files are compressed, so your raw data set size may be 2-8GB. Typically, you need 10x more memory space than your data set (as you need memory for intermediate processing results and temporary variables), so 16GB memory space will not be enough.</p>
<p>You have to increase your virtual memory size to about 60-80GB (backed up with as much physical memory, as possible, to get better speed) and/or reduce the size of your dataset (crop, resample, convert to grayscale, etc).</p>

---

## Post #3 by @pieper (2017-10-05 18:11 UTC)

<p>+1 to what Andras said.</p>
<p><a class="mention" href="/u/eduard_pop">@Eduard_Pop</a> you could try running the same steps with a subset of the data and if you don’t get a crash then you know the issue is memory related.</p>

---

## Post #4 by @hherhold (2017-10-05 22:18 UTC)

<p>This might seem like an obvious thing to check, but just in case - make sure other running programs aren’t chewing up memory or CPU time.</p>

---

## Post #5 by @Eduard_Pop (2017-10-06 07:35 UTC)

<p>I am monitoring RAM usage and it typically does not go above 10 GB. When it says “not responding” and I monitor cpu, crashes with 10-20% CPU usage resolve themselves (its just slow), crashes with 90-100% kill the program.</p>
<p>Nevertheless I will try the above suggestions and see if it works. In the near future I may also have the possibility to run it on a higher-end system (32 GB ram), maybe that resolve these issues too.</p>
<p>Would you say that the GPU plays a role as well? I had it enabled and set to use 1GB of the 1GB on the card. I also disabled it (i though that maybe there was a problem with drivers e.g.) but the problems persisted.</p>

---

## Post #6 by @lassoan (2017-10-06 11:30 UTC)

<p>Note that you don’t need more physical memory, just make sure you allocate enough virtual memory/swap space on your disk. Backing it up with as much physical memory is possible, because disk access is slower than RAM.</p>
<p>GPU is not likely to be a problem.</p>

---

## Post #7 by @lassoan (2017-10-06 11:32 UTC)

<p>By the way, what do you do with your data? What modules do you use, with what parameters?</p>

---
