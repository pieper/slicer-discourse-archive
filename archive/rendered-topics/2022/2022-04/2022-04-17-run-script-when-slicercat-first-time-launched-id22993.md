---
topic_id: 22993
title: "Run Script When Slicercat First Time Launched"
date: 2022-04-17
url: https://discourse.slicer.org/t/22993
---

# Run script when SlicerCAT first time launched

**Topic ID**: 22993
**Date**: 2022-04-17
**URL**: https://discourse.slicer.org/t/run-script-when-slicercat-first-time-launched/22993

---

## Post #1 by @keri (2022-04-17 18:02 UTC)

<p>Hi,</p>
<p>I need to do some customizations when user first time launches SlicerCAT.<br>
Is there a way to achieve that?</p>
<p>More detailly:<br>
I bundle julia with SlicerCAT.<br>
I install some packages to julia during buildtime but these packages hardly transportable. Julia is organized differently than python.</p>
<p>And the main reason is that during buildtime I install <code>pyjulia</code> to python and I set the path to the julia during that action.<br>
After packaging SlicerCAT the path to julia changes so I need to reinstall/update pyjulia.</p>

---

## Post #2 by @lassoan (2022-04-17 19:23 UTC)

<p>You can do anything anytime, not just at the first launch. If you want to do something only once then you can detect if you have already performed the action that you want to do only once and don’t do it again.</p>
<p>I’m just curious. What do you intend to do with Julia that Python and C++ does not cover well enough already?</p>

---

## Post #3 by @keri (2022-04-17 19:40 UTC)

<p>Thank you,</p>
<p>I think I will try to use some environment variable in SlicerCAT’s setting.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="22993">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’m just curious. What do you intend to do with Julia that Python and C++ does not cover well enough already?</p>
</blockquote>
</aside>
<p>For now I find <a href="https://github.com/slimgroup/JUDI.jl" rel="noopener nofollow ugc">JUDI</a> library very attractive.<br>
Though it uses python’s <a href="https://github.com/devitocodes/devito" rel="noopener nofollow ugc">Devito</a> under the hood for solving wave equation.<br>
It is all about wavefield modeling and wavefield inversion (restore velocity model from wavefield).<br>
It is tested on big data (I don’t remember 1.6 TB or 16 TB) and that is very important.<br>
And it is open source under MIT license.</p>
<p>By the way there is some <a href="https://github.com/slimgroup/JUDI.jl/blob/master/examples/scripts/modeling_medical_2D.jl" rel="noopener nofollow ugc">medical example</a> maybe you will find it useful.</p>
<p>I very like julia as it has pretty simple syntax similar to Matlab and it is all about math. It has great interability with python. I can write python module in SlicerCAT and use easilly call julia code. I even can do some GUI staff by calling python from julia (and python calls PythonQt).</p>
<p>I believe in the future its popularity will grow.</p>

---

## Post #4 by @lassoan (2022-04-18 03:23 UTC)

<aside class="quote no-group" data-username="keri" data-post="3" data-topic="22993">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>I very like julia as it has pretty simple syntax similar to Matlab and it is all about math.</p>
</blockquote>
</aside>
<p>This is what I (and most other software developers) dislike about it.</p>
<p>Just one example. For me, choice of 1-based indexing disqualifies the language from any further consideration. It means that its developers don’t think like programmers, so I would need to throw away lots of my prior experience and intuition in software development and would need to relearn whatever julia developers thought could be good ideas.</p>
<aside class="quote no-group" data-username="keri" data-post="3" data-topic="22993">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>I believe in the future its popularity will grow.</p>
</blockquote>
</aside>
<p>It seems that its popularity has plateaued about 4 years ago (<a href="https://www.tiobe.com/tiobe-index/julia/" class="inline-onebox">TIOBE Index - TIOBE</a>). I don’t see the language has space to grow when we have Python for flexible high-level glue code and C++ for developing low-level high-performance algorithm code.</p>

---

## Post #5 by @keri (2022-04-18 11:59 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="4" data-topic="22993">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<aside class="quote no-group" data-username="keri" data-post="3" data-topic="22993">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>I very like julia as it has pretty simple syntax similar to Matlab and it is all about math.</p>
</blockquote>
</aside>
<p>This is what I (and most other software developers) dislike about it.</p>
</blockquote>
</aside>
<p>I started “programming” with Matlab. Probably that why I like julia.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="22993">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Just one example.</p>
</blockquote>
</aside>
<p>If you mean the only example of a library (JUDI), then I can say there is no alternatives in open source software. There are libraries for wave modeling and inversion but they hardly work with big data.<br>
Writing something similar by myself would take half of my life at least. And even then I won’t do that.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="22993">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>For me, choice of 1-based indexing disqualifies the language from any further consideration.</p>
</blockquote>
</aside>
<p>Don’t understand why so critical to 1 based indexing.</p>
<p>Alright it is inconvenient to code in julia and C/C++/python at the same time. But after a while you get used to that.<br>
Also sometimes you have an array of indexes generated in julia (starts with 1) and you need to pass it to python (start with 0) to retrieve for example columns from array. In that case you also need to keep in mind that most likely you would like to subtract 1 before passing it to python.<br>
But to run julia code from python application you usually need to get some parameters (from GUI for example) and pass it to julia for heavy weight computations. That is it. After that julia algorithm starts to work and you get only the result of computations. Save it to file or plot it.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="22993">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It seems that its popularity has plateaued about 4 years ago</p>
</blockquote>
</aside>
<p>I have not seen the statistics.<br>
But as for me as I started with Matlab what I didn’t like the most is that it is very heavy and standalone. There is no cooperation with python. Julia solves this. I think julia is some kind of a pythonical version of Matlab.</p>
<p>Some little thing that I also don’t like in python is that numpy arrays are row-oriented by default (i’m talking about memory layout). In Matlab and julia and C++ Eigen arrays are column oriented by default. For me it is sligtly better to work with column oriented arrays.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="22993">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I don’t see the language has space to grow when we have Python for flexible high-level glue code and C++ for developing low-level high-performance algorithm code.</p>
</blockquote>
</aside>
<p>I disagree.<br>
Let’s imagine an engineer who has some math knowledge and have a task to write high perfomance algorithm.</p>
<p>For me it was very difficult to get started with C++. I didn’t know anything about compilation, ABI, the errors that I get, how to link libs etc… Don’t know why I didn’t throw this idea away.<br>
It is very likely that the engineer doesn’t know C/C++. And if he needs parallelization (MPI?), would he choose to write an algorithm in C++? I don’t think so.</p>
<p>Most likely he will choose either python or julia.<br>
And there the chances for choosing python/julia are somehow equal I think. Python is fullly functional but avoid loops and julia is narrowly focused math language.</p>
<p>And one more thing that I lately got known with. It is about interfaces and types.<br>
If you use some external library and it has some function:</p>
<pre><code class="lang-auto">export foo

function foo(Int x, Int y)
  x + y
end
</code></pre>
<p>Then you usually can overload (or override) it:</p>
<pre><code class="lang-auto">import foo

function foo(Float x, Float y)
  x + y
end
</code></pre>
<p>It is the simplest example but if <code>foo</code> works with custom <code>struct</code> then it make more sense as you can make the external library work with your <code>struct</code> type.</p>
<p>I don’t know if this is possible in python but this may greately help when adjusting external library for your custom data.</p>

---

## Post #6 by @lassoan (2022-04-18 12:44 UTC)

<aside class="quote no-group" data-username="keri" data-post="5" data-topic="22993">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>you mean the only example of a library (JUDI), then</p>
</blockquote>
</aside>
<p>I meant one-based indexing is just one example of why I don’t consider getting to know Julia better.</p>
<p>Indexing is important because developers of the language decided to break with a well-established norm of today’s programming languages.</p>
<aside class="quote no-group" data-username="keri" data-post="5" data-topic="22993">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>I think julia is some kind of a pythonical version of Matlab.</p>
</blockquote>
</aside>
<p>I agree. Octave a Julia are strong Matlab competitors. Julia has a more friendly license, which is good; but does not exactly follow Matlab syntax and API, which might make switch from Matlab a bit harder.</p>
<p>However, Matlab+Octave+Julia combined represent only a very small fraction of programming languages and their share may continue to shrink, as engineering schools may slowly move to Python from Matlab as scope and quality of engineering modules in Python improve.</p>

---

## Post #7 by @keri (2022-04-18 12:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="22993">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I meant one-based indexing is just one example of why I don’t consider getting to know Julia better.</p>
</blockquote>
</aside>
<p>I see now.</p>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="22993">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>However, Matlab+Octave+Julia combined represent only a very small fraction of programming languages and their share may continue to shrink, as engineering schools may slowly move to Python from Matlab as scope and quality of engineering modules in Python improve.</p>
</blockquote>
</aside>
<p>And if some of these three will survive then I would bet that it most likely will be julia <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #8 by @lassoan (2022-04-18 13:30 UTC)

<aside class="quote no-group" data-username="keri" data-post="7" data-topic="22993">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>And if some of these three will survive then I would bet that it most likely will be julia</p>
</blockquote>
</aside>
<p>It very well may be.</p>
<p>By the way, I am the author of MatlabBridge extension (wrote it before Python was a thing and I still used Matlab occasionally). Similarly, you could write a JuliaBridge extension that makes it easier to use Julia from Slicer. Even just minor configuration things, installing required Python packages, updating paths, etc. could help. I would be happy to suggest users to try JupyterBridge instead of MatlabBridge when they come to me with questions.</p>

---

## Post #9 by @keri (2022-04-18 13:40 UTC)

<p>I remember <a href="https://discourse.slicer.org/t/use-julia-with-slicer/16765/4">we had some conversation on that</a> I keep that in mind.</p>
<p>My project is enthusiastic and soon (probably a 1-2 months) the future of my project will be decided.<br>
For now I’m trying to some kind of a finilize my work to present it and if everything is ok I hope I get sponsorship.</p>

---
