---
topic_id: 29112
title: "About Fmri Unity"
date: 2023-04-25
url: https://discourse.slicer.org/t/29112
---

# About fMRI & Unity

**Topic ID**: 29112
**Date**: 2023-04-25
**URL**: https://discourse.slicer.org/t/about-fmri-unity/29112

---

## Post #1 by @Shaban (2023-04-25 11:11 UTC)

<p>Hello, I’m new here.<br>
I have a question regarding fMRI visualization in VR &amp; unity. right now I’m planning to import .nii format file into unity to view it in PCVR, and also add a lot of other different features as a game object in unity.</p>
<p>I have used a volume renderer to show the anatomy file which works fine, but I’m not quiet sure what is the best solution to add the BOLD signals into it. I have 2 .nii format files one for the anatomy, and the other is the BOLD signal. what is the best way to implement something like this? also is it possible to view the changes with a time slider in unity?</p>
<p>I’m still in the researching phase of creating something like this, and I really wish that someone guide me I’m open to all different ways to solve this problem.</p>

---

## Post #2 by @lassoan (2023-04-25 11:13 UTC)

<p>Why are you considering using unity for this? Have you tried to use Slicer’s VirtualReality extension that can show everything in the 3D view by a single button click?</p>

---

## Post #3 by @Shaban (2023-04-25 16:11 UTC)

<p>First Thanks for quick reply.<br>
Yes I’m aware of slicer Virtual Reality. I tried it, and it is good. FYI I’m a unity developer, and I want to create it in OpenVR. so I can add a lot of other unity stuff in it. so why I’m considering unity? many reasons actually.</p>
<p>I would really appreciate it if you guide on a path to achieve something like this. and the question now is something like this doable in unity or not? should I create 4D volume rendering shader? I’m really lost at this point.</p>

---

## Post #4 by @lassoan (2023-05-06 18:37 UTC)

<p>Of course everything is doable in all computing environments, the question is really just the amount of effort needed to develop and maintain it. Creating a decent 4D volume rendering shader alone may probably take several months (maybe much more, if you want to have similar quality and performance as the one in Slicer, with corrent interaction with non-volume-rendered elements, interaction with the volume, etc.). Implementing slice views that you can conveniently browse, basic annotations (points, lines, curves), segmentation tools, adjust visualization options in immersive view, … each may take several months to develop and much more to refine and continuous effort to maintain (user support, bugfixes, platform updates, etc.).</p>
<p>So, while everything is doable, it is probably not a good candidate for a successful one-man-project, because by the time you finish, you already run out of time/funding and/or others have implemented something that is much better than what you have.</p>
<p>I can see a few approaches that could make sense:</p>
<ul>
<li>Implement a minimal viewer in Unity (reimplementing as few features as possible) and leverage as much as possible what Slicer provides. You can do all your data import and pre-processing in Slicer, have all the easy-to-use desktop widgets (buttons, sliders, etc.) for going through complex workflows and setting advanced options. We currently use this approach for some of our HoloLens projects, for example this <a href="https://github.com/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning">pedicle screw planner prototype</a>. This project is very simple, very small amount of code, no volume rendering,  just a single slice for reformatting, rendered and sent in real-time to Unity by Slicer. Transforms are also synchronized between Unity and Slicer.</li>
<li>Join one of the large projects that reimplement medical applications in Unity. I don’t know about open-source projects but there are a number for companies in this space. They work mostly with HoloLens, but some of them also use virtual reality. Unity is not a good platform for medical application development, as lots of things are missing and needs and priorities of game developers are very different from medical device developers, but if enough resources are poured into a project like this then eventually something usable gets out from it.</li>
</ul>

---

## Post #5 by @chrisvasquezfuentes (2025-02-15 18:30 UTC)

<p>hola que tal, me podrías guiar para poder obtener el valor bold de la señal adquirida. muchas gracias</p>

---
