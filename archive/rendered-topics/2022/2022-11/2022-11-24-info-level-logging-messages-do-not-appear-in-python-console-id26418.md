---
topic_id: 26418
title: "Info Level Logging Messages Do Not Appear In Python Console"
date: 2022-11-24
url: https://discourse.slicer.org/t/26418
---

# Info level logging messages do not appear in Python console

**Topic ID**: 26418
**Date**: 2022-11-24
**URL**: https://discourse.slicer.org/t/info-level-logging-messages-do-not-appear-in-python-console/26418

---

## Post #1 by @cpinter (2022-11-24 10:46 UTC)

<p>I built the latest Slicer 5.3, and I now see the changes in the Python console. It’s great to see Qt and VTK errors there too.</p>
<p>However, one thing that could make my day to day work very hard is that the output from <code>logging.info</code> calls in the executed code do not appear in the console. Is there any way to turn this back on? Thank you!</p>

---

## Post #2 by @jamesobutler (2022-11-24 12:35 UTC)

<p>Have you gone into application settings to change log level from the default Warning to Info?</p>
<aside class="quote quote-modified" data-post="1" data-topic="25739">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-feature-python-console-displays-more-log-messages/25739">New feature: Python console displays more log messages</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Until now, the Python console only displayed Python outputs and Python log messages. Therefore, if a Python command executed a VTK method and that VTK method logged an error or warning, it was not immediately visible for the developer (the developer had to notice the change in the log icon, click on it, and scroll down to see the new message). 
In latest Slicer Preview Release (Slicer 5.1.0-2022-10-15 and later), the Python console displays log messages from all sources - Python, Qt, VTK, ITK. 
F…
  </blockquote>
</aside>


---

## Post #3 by @cpinter (2022-11-24 13:19 UTC)

<p>That was easy then, thanks. I thought it would be a CMake option or something similar, that’s why I asked.</p>
<p>I’m wondering why warning is the default log level instead of info? The difference between debug and info is that although neither of them indicate errors, the debug messages don’t appear in the console but the info ones do. Now if you don’t change the setting, there is no difference between the two.</p>

---

## Post #4 by @lassoan (2022-11-24 14:21 UTC)

<p>Logging and process output in Python were previously somewhat intermixed, as it was not possible to print a message on the Python console without making that also show up in the process output and therefore in the application log. After the logging system rework, it has become possible to clearly separate logs, process output, and Python console output, which allowed to display log messages from any sources (Qt, VTK, ITK, CTK, …) in the Python console.</p>
<p>We just had to decide what log level to display in the Python console. Since debug and info messages usually not that important and anything that we want to appear in the process output can be displayed using <code>print</code>, we decided the default log level to be warning and make it easy to change it in application settings.</p>
<p>If you want to display messages in the Python console from Python code, then I would recommend following options (which are the standard way of doing this in Python):</p>
<ul>
<li>A. register an additional Python logger, which prints info-level messages to the process output/Python console (if this is information that user might be interested in), or</li>
<li>B. use <code>print</code> instead of <code>logging.info</code> (if users must see it, because for example that is the result of the command, not just some additional optional information).</li>
</ul>

---

## Post #5 by @cpinter (2022-11-24 14:45 UTC)

<p>Thanks for the answer! After setting the level (as you said, easily) to info, I can see what I want in the console - I usually info-log the main steps in my modules, and it’s easy to see where errors occured, if the values are still sensible etc.</p>
<p>By the way I expect way more work happening in the future about fixing errors, just so that they don’t clog up the console <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @lassoan (2023-11-15 05:10 UTC)

<p>A post was split to a new topic: <a href="/t/print-output-does-not-immediately-appear-in-python-console/32825">Print output does not immediately appear in Python console</a></p>

---
