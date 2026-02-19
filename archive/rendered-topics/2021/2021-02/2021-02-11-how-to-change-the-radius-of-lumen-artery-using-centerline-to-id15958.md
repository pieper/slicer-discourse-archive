---
topic_id: 15958
title: "How To Change The Radius Of Lumen Artery Using Centerline To"
date: 2021-02-11
url: https://discourse.slicer.org/t/15958
---

# How to change the radius of lumen/artery using centerline tool

**Topic ID**: 15958
**Date**: 2021-02-11
**URL**: https://discourse.slicer.org/t/how-to-change-the-radius-of-lumen-artery-using-centerline-tool/15958

---

## Post #1 by @Jezza (2021-02-11 20:38 UTC)

<p>Operating system: macOS Catalina 10.15.7<br>
Slicer version: 4.11 20200930</p>
<p>I was able to learn how to change the length of my model using Centerline Extraction however I cannot find any information on how to change the sphere radius at each centerline point… I know it has something to do with the voronoi diagram but that’s all I could find on the subject…</p>
<p>Would anyone happen to know how I can modify the radius of my solid (blood pool) model using precise values? I assumed that there would be a practical way of doing this at each Center line point but maybe there is a better way of doing this that doesn’t involve Center line extraction? This is my first time using VMTK, I have no prior experience using it.</p>

---

## Post #2 by @Jezza (2021-02-11 20:44 UTC)

<p>EDIT: I also don’t know how to read the radius values at each center line point. I’m aware that the voronoi diagram indicates radius length based on the colour it displays, but I was wondering if there was a better way of displaying actual radius values at each centerline point</p>

---

## Post #3 by @lassoan (2021-02-11 21:00 UTC)

<aside class="quote no-group" data-username="Jezza" data-post="1" data-topic="15958">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/dfb087/48.png" class="avatar"> Jezza:</div>
<blockquote>
<p>I was able to learn how to change the length of my model using Centerline Extraction</p>
</blockquote>
</aside>
<p>What do you mean by this? What length were you able to change?</p>
<aside class="quote no-group" data-username="Jezza" data-post="1" data-topic="15958">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/dfb087/48.png" class="avatar"> Jezza:</div>
<blockquote>
<p>I cannot find any information on how to change the sphere radius at each centerline point</p>
</blockquote>
</aside>
<p>Do you use markups curves or models for representing the centerline tree?<br>
You can access (read/write) radius values in models as a numpy array by calling <code>slicer.util.arrayFromModelPoints</code> or <code>slicer.util.arrayFromMarkupsControlPointData</code> accordingly.</p>
<aside class="quote no-group" data-username="Jezza" data-post="1" data-topic="15958">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/dfb087/48.png" class="avatar"> Jezza:</div>
<blockquote>
<p>Would anyone happen to know how I can modify the radius of my solid (blood pool) model using precise values?</p>
</blockquote>
</aside>
<p>We currently do not have user interface for reconstructing a network of tubes from a centerline tree, but you should be able to do it using existing VMTK or VTK filters.</p>
<p>If you just want to modify a segmented blood pool then you can use Segment Editor (you can set a specific brush diameter in the Paint tool, you can increase/decrease diameter in an entire segment using Margin tool, etc.).</p>

---

## Post #4 by @Jezza (2021-02-11 21:37 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="15958">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What do you mean by this? What length were you able to change?</p>
</blockquote>
</aside>
<p>Sorry that was a mistake, this video -  <a href="https://www.youtube.com/watch?v=WJQexDTiRRc&amp;ab_channel=PerkLabResearch" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=WJQexDTiRRc&amp;ab_channel=PerkLabResearch</a>. -  explains how to change the center line curve length but I now realise that it doesn’t  actually change the length of the model (which is what I would like to do).</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="15958">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you use markups curves or models for representing the centerline tree?<br>
You can access (read/write) radius values in models as a numpy array by calling <code>slicer.util.arrayFromModelPoints</code> or <code>slicer.util.arrayFromMarkupsControlPointData</code> accordingly.</p>
</blockquote>
</aside>
<p>I have been making center line curves in "markups’. How do I change it to “model”? Is that the only way to change the radius at each center line point? I can have a go at reading/writing values in Python (I’m not an expert). If you could show me an example code to read a radius value from the array I would be very grateful! I’m assuming the array will have lots of different types of values and I don’t know how to specify the radius. More importantly, will this actually change the radius of my solid (blood pool)?</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="15958">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We currently do not have user interface for reconstructing a network of tubes from a centerline tree, but you should be able to do it using existing VMTK or VTK filters.</p>
</blockquote>
</aside>
<p>This is precisely what I want to do. Would you mind explaining to me which extensions and which options would help me achieve this?</p>
<p>I’m very grateful for your continued assistance lassoan. I am so close to finishing my project which involves creating an aorta phantom that can mimic real blood flow.</p>

---

## Post #6 by @Jezza (2021-02-11 23:41 UTC)

<p>To summarize:</p>
<ul>
<li>
<p>I want to change the radius and length of my solid (blood pool) in a precise and controlled way. I thought centerline extraction was the answer but maybe I was wrong. I have learned Python, numpy, arrays, data-sets etc… But only 1 year of experience.</p>
</li>
<li>
<p>The margin tool is great for radius changes, but it does not show me the radius values my model has at any given instance (which is not ideal for controlled changes). Will the centerline points update their radius values after I’ve used the margin tool?</p>
</li>
<li>
<p>To extend or shorten the length of my model remains a mystery. Again I assumed this could be done using Centerline extraction but maybe I was wrong.</p>
</li>
</ul>

---

## Post #7 by @lassoan (2021-02-12 00:10 UTC)

<p>What is your overall goal?</p>

---

## Post #8 by @Jezza (2021-02-12 04:15 UTC)

<p>My overall goal is to 3D print a realistic aorta phantom that can reproduce the same flow rate as blood flow. To do this, I have segmented a real aorta from MRI images. Now, I need to modify the radius, or the length (or a combination of both) of <strong>each branch</strong> of the aorta to very specific values (which I have calculated using a biomedical engineering model). If I don’t do that, the model will look like a real aorta but it won’t reproduce the same flow rate as blood flow.</p>
<p>Therefore, I need to:</p>
<ol>
<li>
<p>Know how long each branch is  (I was able to find the length of each branch using the centerline extraction so this has been solved already) <strong>and</strong> to Shorten or extend each branch to a specific length ( while retaining the morphology of my model as much as possible).</p>
</li>
<li>
<p>Know what the radius (or diameter) of each branch is <strong>and</strong> find a way to modify it (in a way that retains the morphology of my model as much as possible).</p>
</li>
</ol>
<ul>
<li>
<p>The margin tool looks like it will do the trick to change the radius of each branch, but I still need to find out what the numbers are (maybe using the python code you told me about).</p>
</li>
<li>
<p>I still don’t know how I can extend or shorten the branches of my model… I thought it would be possible to link the center lines to my blood pool (solid) model, such that the length of each branch of my blood pool model could be changed by extending or shortening the center line branches. I also thought that the radius of my blood pool branches could be changed in a similar way.</p>
</li>
</ul>

---

## Post #9 by @lassoan (2021-02-13 13:31 UTC)

<aside class="quote no-group" data-username="Jezza" data-post="8" data-topic="15958">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/dfb087/48.png" class="avatar"> Jezza:</div>
<blockquote>
<p>If I don’t do that, the model will look like a real aorta but it won’t reproduce the same flow rate as blood flow.</p>
</blockquote>
</aside>
<p>Why a realistic vessel lumen geometry will not produce realistic flow? Do you plan to create a rigid-walled phantom? How do you know what is the “correct” flow rate? Do you know how much parameters vary between patients? (I would assume that variation is quite high, so the unmodified geometry is similar to what you find in some patients)</p>
<p>If you have a specific geometry in mind, specified by vessel lengths and diameters then you can generate each branch by a vtkTubeFilter (or there may be filters or script in VMTK that you can use), and import each tube model into a segmentation to add them together.</p>

---

## Post #10 by @Jezza (2021-02-16 00:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="15958">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>slicer.util.arrayFromMarkupsControlPointData</p>
</blockquote>
</aside>
<p>Hi Iassoan,</p>
<p>My apologies there has been a mix-up with my project. I do not need to modify the actual phantom geometry as much as I thought I did, since we will be using various “tube connectors” to control the flow rates and pressure in each branch of the phantom. Thank you for being patient with me and continuing to respond as best you can, I appreciate it very very much.</p>
<p>I think that being able to read the varying radius of a segmentation would be very useful for people that need precise dimensions or people that want to make calculations. I would highly recommend that you implement this feature in the extract centerline module in the same way that we are given the length of each curved centerline in the markups section. (for example, you could display the radius at each centerline point)</p>
<p>Kind Regards,</p>

---

## Post #11 by @Jezza (2021-02-16 01:00 UTC)

<p>I am aware that a lot of these things can be done using Python code. However for novice/medium programmers such as me, it is hard to understand the code that allows us to communicate with 3DSlicer. I think that a tutorial explaining how to make use of the information on github would be helpful with some examples! Just a suggestion I thought could be helpful.</p>

---
