---
topic_id: 21594
title: "Slicer Qt Loadable Modules As Libraries To Support Other Mod"
date: 2022-01-24
url: https://discourse.slicer.org/t/21594
---

# Slicer qt-loadable-modules as libraries to support other modules

**Topic ID**: 21594
**Date**: 2022-01-24
**URL**: https://discourse.slicer.org/t/slicer-qt-loadable-modules-as-libraries-to-support-other-modules/21594

---

## Post #1 by @RafaelPalomar (2022-01-24 08:58 UTC)

<p>Hello,</p>
<p>for <strong>Slicer-Liver</strong>, we are thinking about the modularity of the extension. We have a set of components already developed in C++, but would like to have  a <code>qt-scripted-module</code>, featuring a single UI, be an entry point for our researchers to interact with and fast-prototype new ideas. We are currently thinking about two designs and would like to hear your opinion about their feasibility and your recommendation.</p>
<p><strong>Single hybrid module</strong></p>
<p>A single <code>qt-scripted-module</code> containing also C++ qtwidgets, logic, nodes, markups, etc., in the same module.</p>
<p><strong>A set of <code>qt-loadable-modules</code> providing the core components + a <code>qt-scripted-module</code> providing the module UI and connecting the components</strong></p>
<p>A set of <code>qt-loadable-modules</code> providing the core components (nodes, markups, qt-widgets, logics, etc.) and a <code>qt-scripted-module</code> that will feature a unified interface and connect the components. The <code>qt-loadable-modules</code> would be used as libraries for the <code>qt-scripted-module</code>, so they will be hidden and won’t have any module interface.</p>
<p>I thank you in advance for your feedback.</p>

---

## Post #2 by @pieper (2022-01-24 19:00 UTC)

<p>I’d say either of those could work fine.  I might favor keeping all the C++ code in loadable modules and have only python code in a scriptable module, which I guess is your second option.  I suppose it also depends on how many files you will end up with and whether a single module for all of it would get cluttered.  Keeping them separate might encourage modularity and reusability.</p>

---

## Post #3 by @RafaelPalomar (2022-01-27 14:39 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>. This is useful for us to decide.</p>

---

## Post #4 by @herryliq (2024-05-15 07:18 UTC)

<p>I currently have the same requirement, where there are many core modules written in C++ that need to be associated with a UI written in Python.<br>
Could you share your implementation ideas and some key issues you encountered?</p>

---

## Post #5 by @pieper (2024-05-15 11:58 UTC)

<p>This SlicerLiver code is here, so you can have a look: <a href="https://github.com/ALive-research/Slicer-Liver" class="inline-onebox">GitHub - ALive-research/Slicer-Liver: 3D Slicer extension for liver analysis and therapy planning</a></p>

---

## Post #6 by @herryliq (2024-05-18 00:37 UTC)

<p>Thank you very much, I will try to read  it. <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @RafaelPalomar (2024-06-10 12:26 UTC)

<p><a class="mention" href="/u/herryliq">@herryliq</a> Don’t hesitate to reach out if you have specific questions about how we implemented this in SlicerLiver <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
