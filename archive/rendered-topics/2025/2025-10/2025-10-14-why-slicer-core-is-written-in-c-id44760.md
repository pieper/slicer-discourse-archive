---
topic_id: 44760
title: "Why Slicer Core Is Written In C"
date: 2025-10-14
url: https://discourse.slicer.org/t/44760
---

# Why Slicer core is written in C++?

**Topic ID**: 44760
**Date**: 2025-10-14
**URL**: https://discourse.slicer.org/t/why-slicer-core-is-written-in-c/44760

---

## Post #1 by @tas47 (2025-10-14 15:33 UTC)

<p>Since QT and VTK already have python equivalence binding Why did you guys chose to write Slicer core in C++? Would there have been a significance decrease in speed if it was written entirely in python?<br>
Are there other positives for writing this software in C++?</p>

---

## Post #2 by @pieper (2025-10-14 17:52 UTC)

<p>If we started over there’s a lot we probably would do differently using modern technologies, but having a core set of features in C++ for performance across platforms would probably still be a good idea.  We don’t encourage new developers to use C++ unless it’s strongly motivated.</p>

---

## Post #3 by @lassoan (2025-10-14 18:08 UTC)

<aside class="quote no-group" data-username="tas47" data-post="1" data-topic="44760">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/tas47/48/78529_2.png" class="avatar"> tas47:</div>
<blockquote>
<p>Since QT and VTK already have python equivalence binding Why did you guys chose to write Slicer core in C++?</p>
</blockquote>
</aside>
<p>Slicer development started about 10-15 years before Python became a useful and popular language, so choosing C++ for implementing most of Slicer core was very obvious.</p>
<aside class="quote no-group" data-username="tas47" data-post="1" data-topic="44760">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/tas47/48/78529_2.png" class="avatar"> tas47:</div>
<blockquote>
<p>Would there have been a significance decrease in speed if it was written entirely in python?</p>
</blockquote>
</aside>
<p>You cannot write a medical image computing application “entirely in Python”. You could not use essential packages, such as numpy, pandas, scipy, VTK, ITK, pytorch, etc. because none of these are written <em>entirely</em> in Python.</p>
<p>Probably what you meant to ask is if you can use Python as the application executable that uses pip-installed Python packages to build the Slicer application. The answer is: yes! The best example is the <a href="https://github.com/KitwareMedical/SlicerTrame">SlicerTrame project</a>, which is a Slicer application written entirely in Python.</p>

---

## Post #4 by @curtislisle (2025-10-14 18:10 UTC)

<p>Hi tas47,<br>
Your suggestion of asking about a scripting language (Python) for Slicer instead of C++ makes sense. Let me provide a bit of historical background: Having been a long-time user of Slicer, I can say that Slicer 1.x was actually written entirely in a scripting language (Tcl/Tk because Python bindings weren’t mature yet). Yes, C++ generally does have a noticeable speed advantage over Python. Only recently, several methods to compile or substantially speed up Python runtime performance have emerged, so Python hasn’t been performant enough historically, though that might be changing in the future. A bigger factor, though, is that Slicer is built on top of several mature, open-source C++ libraries that perform much of the computationally-intense work: The Insight Toolkit (ITK), written in C++, handles many medical imaging resampling, filtering, and analysis tasks. The Visualization Toolkit (VTK) is a mature C++ library for optimized rendering and 3D scene management. Custom Qt widgets were necessary, so a C++ library was built to simplify UI creation. So, it made sense to connect directly with processing done in these foundational libraries through their C++ bindings. In today’s Slicer, there is a lot of support for adding new functionality in python, while the core remains in C++ for the foreseeable future. Good question, though!</p>

---

## Post #5 by @tas47 (2025-10-14 18:31 UTC)

<p>Thank you for all the answers and replies! This was very informative.</p>
<p>Tas</p>

---
