---
topic_id: 29637
title: "Can Anyone Show Me How To Do Slicer Extension In C With An E"
date: 2023-05-25
url: https://discourse.slicer.org/t/29637
---

# Can anyone show me how to do slicer extension in c++ with an example?

**Topic ID**: 29637
**Date**: 2023-05-25
**URL**: https://discourse.slicer.org/t/can-anyone-show-me-how-to-do-slicer-extension-in-c-with-an-example/29637

---

## Post #1 by @dsa934 (2023-05-25 01:39 UTC)

<p>Operating system: 10<br>
Slicer version: 5.2.1</p>
<p>Hi, slicer users</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f18381df94d1d9cb75f4b12e034782982262a62.png" alt="image" data-base62-sha1="6ICkux1mkxkUPQM6gGIQIa7HIVc" width="383" height="169"></p>
<p>I am using several python modules in 3d slicer through extension wizard.<br>
However, I’ve read all the advice to use script repositories and loadable classes for C++ extensions, but I don’t know what the heck they are talking about.</p>
<p>A very simple example is good, so can anyone explain how to extend it with C++?</p>

---

## Post #2 by @jcfr (2023-05-25 01:48 UTC)

<p>Implementing a module in C++ is more involved than simply relying on python to implement a specific workflow and user interface.</p>
<p>Is there a specific task you are not able to achieve leveraging Python ?</p>
<p>By better understanding your goal, we may be able to more effectively guide you.</p>
<aside class="quote no-group" data-username="dsa934" data-post="1" data-topic="29637">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar"> dsa934:</div>
<blockquote>
<p>A very simple example is good, so can anyone explain how to extend it with C++?</p>
</blockquote>
</aside>
<p>All the modules available in the <a href="https://github.com/Slicer/Slicer/tree/main/Modules/Loadable">https://github.com/Slicer/Slicer/tree/main/Modules/Loadable</a> directory are examples you could look at.</p>

---

## Post #4 by @dsa934 (2023-05-27 11:54 UTC)

<p>I deleted the previous post because it was incorrect.</p>
<p>My current situation is that I can use the desired module as an extension with python, but I cannot use it with c++.</p>
<p>I have a module written in C++ that is already implemented and I want to use it in a slicer.</p>
<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="29637">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>All the modules available in the <a href="https://github.com/Slicer/Slicer/tree/main/Modules/Loadable" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/tree/main/Modules/Loadable </a> directory are examples you could look at.</p>
</blockquote>
</aside>
<p>I’ll try the link you linked above first.</p>

---
