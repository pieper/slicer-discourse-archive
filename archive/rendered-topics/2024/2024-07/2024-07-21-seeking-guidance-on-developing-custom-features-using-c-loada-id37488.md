---
topic_id: 37488
title: "Seeking Guidance On Developing Custom Features Using C Loada"
date: 2024-07-21
url: https://discourse.slicer.org/t/37488
---

# Seeking Guidance on Developing Custom Features using C++ (loadable module / core)

**Topic ID**: 37488
**Date**: 2024-07-21
**URL**: https://discourse.slicer.org/t/seeking-guidance-on-developing-custom-features-using-c-loadable-module-core/37488

---

## Post #1 by @park (2024-07-21 14:31 UTC)

<p>Hello,</p>
<p>I am currently developing a custom app using Slicer. So far, I have been using Python and Scripted Modules for my development. However, I now need to accomplish the following tasks:</p>
<ul>
<li>Develop Custom Markups</li>
<li>Create new MRML modules</li>
<li>Modify the pipeline</li>
<li>Create Custom Transform Handles</li>
</ul>
<p>I understand that these tasks typically require modifying Slicer’s source code or developing Loadable Modules. <strong>I attempted to look into the C++ code to implement these features but am unsure where to start.</strong></p>
<p>I am proficient in Python and can handle Scripted Modules effectively. While I have a basic understanding of C++ and can use the basic API of VTK, I am not very skilled in C++.</p>
<p><strong>Given this situation, what should I prioritize to achieve my goals?</strong></p>
<ul>
<li>Become highly proficient in C++ programming</li>
<li>Study VTK more in-depth</li>
<li>Learn the Qt Framework</li>
<li>Study CMake to understand the structure</li>
<li>Take the Slicer Advanced Course</li>
</ul>
<p>I would appreciate any advice. Thank you.</p>

---

## Post #2 by @mau_igna_06 (2024-07-21 19:11 UTC)

<p>I’m not an expert but I would start in this extension <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"></p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/chir-set/SlicerExtraMarkups/">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/chir-set/SlicerExtraMarkups/" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/9822ba01b507755187b8b35fb71b653abaf8dcceb8deea25540e72f9303c876d/chir-set/SlicerExtraMarkups" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/chir-set/SlicerExtraMarkups/" target="_blank" rel="noopener nofollow ugc">GitHub - chir-set/SlicerExtraMarkups: Custom markups for Slicer</a></h3>

  <p>Custom markups for Slicer. Contribute to chir-set/SlicerExtraMarkups development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>HIH</p>

---

## Post #3 by @ebrahim (2024-07-29 14:35 UTC)

<blockquote>
<ul>
<li>Create new MRML modules</li>
</ul>
</blockquote>
<p>I think this advanced topic in the developer’s guide can be helpful: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/mrml_overview.html#creating-custom-mrml-node-classes" rel="noopener nofollow ugc">Creating Custom MRML Node Classes</a></p>
<blockquote>
<p><strong>Given this situation, what should I prioritize to achieve my goals?</strong></p>
</blockquote>
<p>From the things that you listed, here are my views:</p>
<ul>
<li>learning the Qt framework at a basic level will help make the code more readable, and it will be needed for customizing UI</li>
<li>becoming proficient in C++ will help, but if you already know the basics then the you can learn via your work on Slicer itself. It is a slow and steady process. Lately while getting familiar with a new language I have found it useful to paste code into chatgpt and ask it to explain things</li>
</ul>
<p>I think that VTK and CMake are less critical for figuring out where to start and how to get moving, and they can be filled in as you need them.</p>
<p>(we offer the 3D slicer advanced course at Kitware so of course I would recommend it <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20">)</p>

---

## Post #4 by @pieper (2024-07-30 11:52 UTC)

<p>In general my suggestion for new Slicer C++ developers is to study and follow existing patterns - a lot of complex design decisions have been made in the division of code between GUI (Qt) vs Logic/MRML/displayable managers (VTK) vs support libraries in vanilla C++, including how they are exposed in Python.  Plus for maintainability you will find it easier if you closely follow conventions so you can more easily adapt as compilers, OSes, dependencies, and build systems inevitably evolve.</p>
<aside class="quote no-group" data-username="ebrahim" data-post="3" data-topic="37488">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ebrahim/48/13403_2.png" class="avatar"> ebrahim:</div>
<blockquote>
<p>we offer the 3D slicer advanced course</p>
</blockquote>
</aside>
<p>This sounds like good advice!</p>

---

## Post #5 by @park (2024-07-31 19:16 UTC)

<p>Thank you all for the advice!!</p>
<p>I will take it step by step and leave feedback afterward. Hopefully, one day I can write advice like this myself.</p>
<p>Thank you.</p>

---
