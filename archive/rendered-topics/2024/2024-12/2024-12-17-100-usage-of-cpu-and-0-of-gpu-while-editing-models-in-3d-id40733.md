# 100% usage of CPU and 0% of GPU while editing models in 3D

**Topic ID**: 40733
**Date**: 2024-12-17
**URL**: https://discourse.slicer.org/t/100-usage-of-cpu-and-0-of-gpu-while-editing-models-in-3d/40733

---

## Post #1 by @MaxVs (2024-12-17 22:03 UTC)

<p>Hi!<br>
I have an issue.<br>
While editing my 3D models in 3D view (smoothing, holes filling or median) it takes so long to perform, whats more I can see 100% usage of my CPU and 0% of my GPU for the whole time.<br>
GPU Nvidia GeForce 4060 Ti.</p>
<p>I’ve already andjust settings of Nvidia Control Panel (3D settings) and nothing has changed.<br>
Could you give me any advise/idea how to make it right?</p>
<p>Best regards</p>

---

## Post #2 by @mau_igna_06 (2024-12-18 00:45 UTC)

<p>If this it’s not possible yet, could it be implemented with current itk/vtk? <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #3 by @Newbie101 (2024-12-18 12:02 UTC)

<p>Hi I can help here…First install the new AI drivers from Nvidia thats the easy bit. make sure its the new version. When you install this the new sets your programms and callobrates your GPU to that game or software. Once this is complete it does it auto. You need to ensure you have the correct drivers creater/gamer. You cannot have both…its 4070 ti and it will be heavy loaded unlike quadro,s …important part to take note many dont even bother.In order to use a 4070 you must set under the gpu setting in the nvida new apps panels the cuda settings on .not the old nvidia panel…scroll down for the app in the list and then find cuda cores. click and select all for that program. its a walk in the park. If you wish to use a faster process select the chip vs the GPU depends what kit you have. BIGGEST WINDOWS MESS EVER…to set the card the way you like you must change the windows device settings this is easier in the old panel but you need to set your gpu for gpu only graphics not allow windows to do what it wishes…BE carefull dont install create drivers if you game it will end in tears but you can flip but its long winded to game every time.! 2nd get a quadro 4k off intelegant servers for 100 quid and it will do ok for the $$$ and it wont mess up your kit setting.New AI may even combine the cudas we await to see that so much for many is trial atm.  1st. qtr or 2nd qtr next year we will soon know from Nvidia as this is hot topic…hope it helps.</p>

---

## Post #4 by @MaxVs (2024-12-18 13:15 UTC)

<p>What a time-consuming explanation by your side. Thank you so so much! I really appreciate it <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #5 by @lassoan (2024-12-19 00:34 UTC)

<aside class="quote no-group" data-username="MaxVs" data-post="1" data-topic="40733">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/maxvs/48/81480_2.png" class="avatar"> MaxVs:</div>
<blockquote>
<p>While editing my 3D models in 3D view (smoothing, holes filling or median) it takes so long to perform, whats more I can see 100% usage of my CPU and 0% of my GPU for the whole time.</p>
</blockquote>
</aside>
<p>Reimplementing algorithms to run on GPU would be prohibitively expensive, and would only work on data sets that can fully fit on your GPU (so the CPU implementations would still need to be all maintained, which would further increase software maintenance costs).</p>
<p>However, this is rarely an issue in practice, because you can make the updates 10-100x faster by two simple changes in your workflow:</p>
<ul>
<li>Use surface nets algorithm for 3D updates: in the “Show 3D” button’s dropdown menu, enable “Use surface nets” and “Use surface nets smoothing”.</li>
<li>After you use <code>Threshold</code> or <code>Grow from seeds</code> effect, before enabling <code>Show 3D</code>, use <code>Smoothing</code> effect (<code>Median</code> method should work well for most cases). These two effects can create noisy segmentation, which can result in millions of unnecessary triangles in the output mesh, that just clutter the view and slow down mesh generation.</li>
</ul>
<p>There are many more techniques, but since using these two will likely be sufficient, I would not go into more details now. If you still have performance issues that you cannot resolve then let us know.</p>

---

## Post #6 by @MaxVs (2024-12-19 06:13 UTC)

<p>I’m marking topic as solved.<br>
Thank you all for you time!</p>

---
