# Red window object - Script Dev

**Topic ID**: 27477
**Date**: 2023-01-26
**URL**: https://discourse.slicer.org/t/red-window-object-script-dev/27477

---

## Post #1 by @lucas_sd (2023-01-26 10:15 UTC)

<p>Hi everybody,</p>
<p>I would like to know if I can use/call the red window like an object to put it in a frame/container using it in another application.</p>
<p>If its possible, what would the command be? Maybe with slicer.app.layoutManager()?</p>
<p>Thankss, Lucas.</p>

---

## Post #2 by @lassoan (2023-01-26 23:32 UTC)

<p>Yes, sure, there are many ways to do this. What is your environment? Do you want to display the Slicer view in a web application or a local a desktop pplication? What interactivity is needed? What does the other application do and what framework it is inplemented in? What RPC mechanisms your application already uses to interact with other applications or devices? Have you considered embedding your application into Slicer instead?</p>

---

## Post #3 by @lucas_sd (2023-01-27 09:46 UTC)

<p>Hi Andras, like always thanks for your message.</p>
<p>Im working with pyqt making an external dev that interact and use some specific functions of 3ds (is required this way). At this moment I run my script with 3ds from the terminal.</p>
<p>I know its possible to do all of this using slicelets, other libraries, etc, etc. The idea, by now, is just call the red window like a object and put it over a frame in the pyqt script . Its that possible? There is a command of 3ds that evoque the red window? To represent it in another place.</p>
<p>Thanks,</p>

---

## Post #4 by @lassoan (2023-01-28 17:41 UTC)

<p>You can pass commands to Slicer when you start it (or later using Slicer’s REST API - either directly or via the <a href="https://pypi.org/project/slicerio">slicerio Python package</a>) to run commands to configure its viewer, put a view in a certain position on the desktop, etc.</p>
<p>However, based on what you describe it seems the right thing to do is to simply run your Python script in Slicer’s Python environment.</p>

---
