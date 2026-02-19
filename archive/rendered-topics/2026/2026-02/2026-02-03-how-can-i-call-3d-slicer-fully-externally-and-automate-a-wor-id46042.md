---
topic_id: 46042
title: "How Can I Call 3D Slicer Fully Externally And Automate A Wor"
date: 2026-02-03
url: https://discourse.slicer.org/t/46042
---

# How can I call 3D Slicer fully externally and automate a workflow? 

**Topic ID**: 46042
**Date**: 2026-02-03
**URL**: https://discourse.slicer.org/t/how-can-i-call-3d-slicer-fully-externally-and-automate-a-workflow/46042

---

## Post #1 by @JoshMono (2026-02-03 04:04 UTC)

<p>Hey there folks.</p>
<p>I’m working on a software assignment where my goal is to help automate a couple of tasks for my employer. My employer uses 3D Slicer, Meshlab and eventually Blender to make a 3D model from Dicom files and then work on them in Blender. The final product should ideally be an all-emcompassing Blender add-on, so my employer can focus on working in Blender as much as possible. I’m still exploring the possibilities though.</p>
<p>The only thing I need Meshlab for is to do a quick cleanup of the model, and that can be done fully via Python without needing to run Meshlab. Ideally I’d like to do something like that with 3D Slicer. Is this possible? And how can I approach that?</p>
<p>On this same forum I found out about pyigtl, but from what I understand this requires that 3D Slicer is installed and currently running. Is there a way to call 3D Slicer fully externally, have it do some tasks on Dicom files, and export an STL model? That way I could then feed that into Meshlab, and then into Blender.</p>

---

## Post #2 by @muratmaga (2026-02-03 07:20 UTC)

<aside class="quote no-group" data-username="JoshMono" data-post="1" data-topic="46042">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/joshmono/48/81899_2.png" class="avatar"> JoshMono:</div>
<blockquote>
<p>pyigtl, but from what I understand this requires that 3D Slicer is installed</p>
</blockquote>
</aside>
<p>Yes, you will need to install Slicer one form or the other. Then you can drive it without invoking the UI either through directly interacting with SlicerPython, or using it through Jupyter notebook.</p>

---

## Post #3 by @pieper (2026-02-03 10:23 UTC)

<p>You can also set up the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html">Web Server</a> module in Slicer to accept commands (send it python scripts) to automate any process from the outside.</p>

---

## Post #4 by @ebrahim (2026-02-03 14:07 UTC)

<p>If you do have Slicer installed and you know what you want it to do in the form a python script (e.g. load DICOM, create model, export model), then a quick and easy approach is to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#run-a-python-script-file-in-the-slicer-environment">run the script in slicer headlessly</a>.</p>

---

## Post #5 by @JoshMono (2026-02-05 23:17 UTC)

<p>Ooh, awesome. Thank you for the replies, everybody. This gives me a few entry points that I can try out.</p>

---

## Post #6 by @JoshMono (2026-02-15 13:11 UTC)

<p>Excuse me, is what you’re referring to SlicerPython, or PythonSlicer? In the docs I did find the latter, which is an alternative Python environment essentially.</p>

---

## Post #7 by @cpinter (2026-02-18 16:33 UTC)

<p>The two are the same, it just has been renamed for clarity. Maybe the documentation is lagging behind. If you can suggest an edit we’d appreciate it, thanks!</p>

---
