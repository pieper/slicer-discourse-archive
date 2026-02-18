# Converting Slicer Python code to C++

**Topic ID**: 13762
**Date**: 2020-09-30
**URL**: https://discourse.slicer.org/t/converting-slicer-python-code-to-c/13762

---

## Post #1 by @nm19 (2020-09-30 01:05 UTC)

<p>Hello,</p>
<p>I was looking into converting some Slicer code from Python to C++, in particular from the slicer.util module the loadVolume method. Is there an already existing header file that does this for the util module? If not, any pointers on how to approach this task?</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2020-09-30 19:33 UTC)

<p>Converting Python code to C++ isn’t conceptually difficult, but there are a lot of steps involved and it’s typically not worth the effort, particularly for something like loading a volume, where the python code already calls down in to C++, so there’s no efficiency gained.</p>
<p>Of course you can load data using C++ but you will need to study a lot of the internal architecture to learn how.  I’d suggest reading the tests to get a sense of what’s required.</p>

---

## Post #3 by @nm19 (2020-09-30 22:58 UTC)

<p>Thanks for the advice.</p>
<p>The reason for doing so is more so for all of our code being in C++, rather than for efficiency. I’ve taken a closer look at the architecture of the existing code and I think I understand how it works. However, I’m at a loss as to what ‘from slicer import app’ is referring to in the util code.</p>

---

## Post #4 by @pieper (2020-10-01 12:44 UTC)

<aside class="quote no-group" data-username="nm19" data-post="3" data-topic="13762">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/6bbea6/48.png" class="avatar"> nm19:</div>
<blockquote>
<p>from slicer import app</p>
</blockquote>
</aside>
<p>You can find out the types by pasting this code in the python console and then typing <code>app</code> and you can see that it’s a <code>qSlicerApplication</code>.  So you need to include the appropriate headers and link the corresponding libraries to use that class in C++.</p>

---
