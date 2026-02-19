---
topic_id: 31924
title: "3D Slicer Not Responding But Still Using Maximum Cpu"
date: 2023-09-27
url: https://discourse.slicer.org/t/31924
---

# 3D Slicer not responding but still using maximum CPU

**Topic ID**: 31924
**Date**: 2023-09-27
**URL**: https://discourse.slicer.org/t/3d-slicer-not-responding-but-still-using-maximum-cpu/31924

---

## Post #1 by @b_gop (2023-09-27 02:54 UTC)

<p>I am trying to use vmtk centerline extraction on a model of approximately ~250mb size. [Even though the file size is not too big, the model is definitely intricate with a lot of branches and would understandably require time for computation]</p>
<p>Often the application will freeze and become unresponsive but according to the Task Manager, it is still maxing out the CPU and also steadily increasing the used disk space.<br>
Does this mean that the computation is ongoing even though the application is not responding?</p>
<p>System:<br>
Windows 10<br>
128GB RAM<br>
Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz Processor</p>

---

## Post #2 by @cpinter (2023-09-27 10:51 UTC)

<p>It is expected that when the application uses maximum CPU it becomes unresponsive. It means it is still working on the task. It may mean that the application hangs, but then it would stay the same way indefinitely. On a crash the application closes. Since you posted this 8 hours ago, probably you can tell if it finished successfully or not. Can you please let us know?</p>

---

## Post #3 by @b_gop (2023-09-27 10:58 UTC)

<p>The computation ended successfully after I left it running overnight! [This is when the application was maxing out the CPU]</p>
<p>Side question: if the application goes into the Not Responding state and is also NOT using maximum CPU, that should probably be a sign to restart it, right? Or can it still be running the computation?</p>
<p>Thanks!</p>

---

## Post #4 by @cpinter (2023-09-27 11:03 UTC)

<p>There is no easy way you can tell what is happening in that case. Hangs are much more rare than crashes, so if it uses maximum CPU, and thus does not respond, you can almost safely assume it is doing the computation.</p>

---

## Post #5 by @lassoan (2023-09-27 15:01 UTC)

<aside class="quote no-group" data-username="b_gop" data-post="3" data-topic="31924">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/b_gop/48/67116_2.png" class="avatar"> b_gop:</div>
<blockquote>
<p>Side question: if the application goes into the Not Responding state and is also NOT using maximum CPU, that should probably be a sign to restart it, right? Or can it still be running the computation?</p>
</blockquote>
</aside>
<p>Usually a processing algorithm only uses one CPU core (unless it is designed to be an algorithm that can be distributed to run on multiple threads in parallel). Therefore if the algorithm runs at full speed your total CPU usage does not go above 1 / <code>number of CPU cores</code>, which is usually about 10-20%.</p>
<p>Note that most often centerline extraction only takes a couple of seconds. Have you used “Extract centerline” module in 3D Slicer or you just ran VMTK filters in Python? If you just run the filter manually make sure you preprocess the model properly (e.g., smooth and decimate - it does not make sense to run centerline extraction on the raw model extracted from images, because they have unnecessarily large number of points).</p>

---

## Post #6 by @zariliusra (2023-09-28 15:17 UTC)

<p>Hi, I always get “not responding” while doing “growing from seed”, the CPU usage is only 10–18%. Is there anyway to optimize the CPU usage and not get the app into “not responding”?</p>
<p>I use intel i7 13th gen with 32 gb of ram.</p>

---

## Post #7 by @lassoan (2023-09-28 15:30 UTC)

<p>“Not responding” when you are trying to operate the software while it is busy is normal. It means that you have to wait before you can do something.</p>
<p>“CPU usage is only 10–18%” is normal, too. As I explained above, most algorithms cannot be run on multiple CPU cores in parallel, because you need to perform steps of the algorithm in order (you can only start the next step if the previous is finished). This means that if you look at the overall CPU usage of your computer, you’ll see about 10% usage, because most of your CPU cores are idle.</p>
<p>While “Grow from seeds” algorithm cannot run on multiple threads in parallel, and initialization may take 10-20 seconds, the algorithm is very efficient when you are adding more seeds. Then update should take just a seconds. If you enable 3D preview and you have a large, complex segmentation then the 3D surface generation may take significant amount of time, so if you need faster updates then you may disable that.</p>

---
