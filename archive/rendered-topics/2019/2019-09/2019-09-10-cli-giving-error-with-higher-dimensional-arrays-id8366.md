---
topic_id: 8366
title: "Cli Giving Error With Higher Dimensional Arrays"
date: 2019-09-10
url: https://discourse.slicer.org/t/8366
---

# CLI giving error with higher dimensional arrays

**Topic ID**: 8366
**Date**: 2019-09-10
**URL**: https://discourse.slicer.org/t/cli-giving-error-with-higher-dimensional-arrays/8366

---

## Post #1 by @fpsiddiqui91 (2019-09-10 14:40 UTC)

<p>Hello Developers,</p>
<p>I am creating a CLI module for performing computationally expensive tasks. <a class="mention" href="/u/lassoan">@lassoan</a> already helped me with parsing an arguments and all.</p>
<p>There is some weird problem. If I initiate 2 or more high dimensional array like (128x128x49) in my CLI module, it is ending with a fault.</p>
<pre><code>const int slices= 96;
const int x=127;
const int y=127;

float array1[slices][x][y]={};
float array2[slices][x][y]={};  
</code></pre>
<p>The error message I am getting is<br>
CLI_test terminated with a fault</p>
<p>However, if I use low dimensional array. My module runs perfectly. Is there any memory issue or something else?</p>

---

## Post #2 by @lassoan (2019-09-10 15:17 UTC)

<p>These arrays are way too big to be stored on the stack, but allocating them on the heap should be no problem. The easiest way is to let STL containers or VTK or ITK objects manage the memory for you. Most CLI modules use ITK, so you can find lots of examples how to do it.</p>

---

## Post #3 by @fpsiddiqui91 (2019-09-10 16:25 UTC)

<p>Thank you for your response <a class="mention" href="/u/lassoan">@lassoan</a>. I have seen several examples but most of the examples are manipulating image. Like taking input as an image , apply itk filter and return an image.</p>
<p>I need to work on these 3 dimensional large arrays. Is there any basic example in in ITK to work on these  which can return a 3 dimensional array as well.</p>
<p>Maybe a simple example to parse these higher dimensional arrays from scripting module and return as well.</p>
<p>Thank you so much for all your guidance throughout this development process</p>

---

## Post #4 by @lassoan (2019-09-10 17:19 UTC)

<p>Images are 3D arrays. VTK supports up to 4-dimensional images, ITK can handle arbitrary number of dimensions.</p>
<p>What would you like to achieve? What programming language do you prefer: C++ or Python?</p>

---

## Post #5 by @fpsiddiqui91 (2019-09-10 17:33 UTC)

<p>Thank you for your response. I have some higher dimensional arrays and I want to perform some numerical manipulation on them.  Doing this in python is  very time consuming, so I am planning to parse my arrays to CLI module in  C++ and perform these computationally expensive tasks in CLI module thn return the output array.</p>
<p>I mostly have to use simple operations like dot product and vector additions …</p>
<p>Thank you</p>

---

## Post #6 by @lassoan (2019-09-11 01:05 UTC)

<aside class="quote no-group" data-username="fpsiddiqui91" data-post="5" data-topic="8366">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/53a042/48.png" class="avatar"> fpsiddiqui91:</div>
<blockquote>
<p>I have some higher dimensional arrays and I want to perform some numerical manipulation on them. Doing this in python is very time consuming</p>
</blockquote>
</aside>
<p>You cannot iterate through each voxel of an image in Python, but there are hundreds of Python packages that implement efficient processing operations on higher-dimensional arrays. See numpy, scipy, SimpleITK, VTK, scikitimage, OpenCV, etc.</p>
<p>In C++ you <em>can</em> implement pixel-by-pixel processing, but nowadays this is rarely needed, since most common low-level operations are already have nice, robust, performance-optimized implementations.</p>
<aside class="quote no-group" data-username="fpsiddiqui91" data-post="5" data-topic="8366">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/53a042/48.png" class="avatar"> fpsiddiqui91:</div>
<blockquote>
<p>I mostly have to use simple operations like dot product and vector additions …</p>
</blockquote>
</aside>
<p>You certainly don’t need to implement such basic operations from scratch, in C++. You can add two n-dimensional numpy arrays like this: <code>c = a + b</code>.</p>

---
