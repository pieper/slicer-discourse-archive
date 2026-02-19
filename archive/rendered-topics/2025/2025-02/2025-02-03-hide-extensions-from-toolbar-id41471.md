---
topic_id: 41471
title: "Hide Extensions From Toolbar"
date: 2025-02-03
url: https://discourse.slicer.org/t/41471
---

# Hide Extensions from toolbar

**Topic ID**: 41471
**Date**: 2025-02-03
**URL**: https://discourse.slicer.org/t/hide-extensions-from-toolbar/41471

---

## Post #1 by @Djonathan_Souza (2025-02-03 20:51 UTC)

<p>Hi,</p>
<p>How can I hide toolbar extensions? Or just remove it. I need to remove the python icon from there</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/742b41ee8b18a4bda64c6b299de94f49607c4ad5.png" alt="image" data-base62-sha1="gzG43xwM6q07cy3vvMpp17nReoB" width="444" height="70"></p>

---

## Post #2 by @lassoan (2025-02-03 21:04 UTC)

<p>You can use (or write a similar function to) the <a href="https://github.com/Slicer/Slicer/blob/71394e2955e040f3b7ffcb36538b1cb751a77f17/Base/Python/slicer/util.py#L587-L609"><code>slicer.util.setToolbarsVisible</code> function</a> to show/hide toolbars.</p>
<p>You can customize everything about how the application looks or behaves. Check out the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">Slicer Script Repository</a> for more examples and the <a href="https://github.com/KitwareMedical/SlicerCAT">Slicer Custom Application Template</a> if you want to create a proper custom application.  If you have any specific question that is not answered in the script repository, here on the forum, and you have trouble getting useful answers from AI copilots then feel free to keep asking here (each independent question in a new topic, so that others can easily find the questions/answers later).</p>
<p>I am just curious - why do you want to hide the Python icon? You don’t want the user to be able to show the Python console? Or you don’t want the user to be able to hide the Python console? Even if you hide the icon, there are still ways for users to make Slicer display a Python console (e.g., a developer who knows Slicer could specify a command that makes the application display the Python console, could add a Slicer module that registers a new keyboard shortcut for this or adds a button to the module’s GUI, …), so depending on what exactly you want to achieve, there may be better way to do that than hiding a toolbar button.</p>

---

## Post #4 by @Djonathan_Souza (2025-02-04 13:59 UTC)

<p>Hi Lessoan, actually I need remove the python console from appplication, but idk how i do that</p>

---

## Post #5 by @lassoan (2025-02-04 16:28 UTC)

<p>The console can be hidden at several levels, many different ways. If there is something that you want to prevent (e.g., prevent the user seeing some messages, running Python commands) then describe that and we can give advice on how to achieve that.</p>

---

## Post #6 by @Djonathan_Souza (2025-02-04 16:45 UTC)

<p>Hello Lassoan, thanks for answering me again!</p>
<p>so, I need to completely remove the python console from the application, I don’t need it to exist in my context.  How can I achieve this result?</p>

---

## Post #7 by @jamesobutler (2025-02-04 17:04 UTC)

<p>Are you looking to remove the python console and all Python capabilities completely from the application? In this case no Python Slicer modules would be present.</p>

---

## Post #8 by @Djonathan_Souza (2025-02-04 17:29 UTC)

<p>Hi James,</p>
<p>I´d like to explicitly disable access to the Python console in Slicer while keeping the rest of the Python modules available. Would that be possible?</p>

---

## Post #9 by @jamesobutler (2025-02-04 20:18 UTC)

<p>Yes you can use the method described in <a href="https://discourse.slicer.org/t/hide-extensions-from-toolbar/41471/2" class="inline-onebox">Hide Extensions from toolbar - #2 by lassoan</a>, however as mentioned it is not completely unavailable to users. Developers are knowledgeable to add code to the slicer rc startup file or to another module that can show it again. It is similar to a user simply commenting out the Python code that you might have to hide it so that it can be shown again.</p>

---
