---
topic_id: 10782
title: "Basic Questions On Cli Modules Vs Scripted Modules"
date: 2020-03-22
url: https://discourse.slicer.org/t/10782
---

# Basic questions on CLI modules vs Scripted Modules

**Topic ID**: 10782
**Date**: 2020-03-22
**URL**: https://discourse.slicer.org/t/basic-questions-on-cli-modules-vs-scripted-modules/10782

---

## Post #1 by @Prashant_Pandey (2020-03-22 21:31 UTC)

<p>I’m writing a basic ‘programming in Slicer’ tutorial for my lab (which borrows heavily from existing documentation and the Perk Lab bootcamp slides).</p>
<p>Something that wasn’t been clear to me: When would you write a CLI module vs. a scritped module? I’ve only written scripted modules, and from what I understand on <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Modules#Command_Line_Interface_.28CLI.29" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Modules#Command_Line_Interface_.28CLI.29</a> it’s always better to write a scripted module for increased flexibility? If this is true, when would you write a CLI module?</p>

---

## Post #2 by @lassoan (2020-03-22 21:57 UTC)

<p>CLI module has a number of restrictions, such as:</p>
<ul>
<li>GUI is static, with a limited set of widgets, generated from the XML descriptor file</li>
<li>the module does not have access to the full scene (only to the selected input nodes)</li>
<li>only runs when the user clicks apply (or an input node is changed and auto-update is enabled)</li>
<li>always performs all computations from scratch</li>
</ul>
<p>However, these limitations allow faster, simpler development and asynchronous execution (application GUI is not blocked).</p>
<p>CLI modules can be also created from any existing command-line applications or Python scripts - by simply creating an XML file that describes command-line arguments.</p>

---

## Post #3 by @pieper (2020-03-22 22:04 UTC)

<p>The original motivation for CLI modules (which is still valid) was to allow people to write or adapt traditional C or C++ programs so that they would have a GUI.  So they only rely on having a <code>main(argc,argv)</code> entry point with data access via files and progress reporting to <code>stdout</code> and errors reported via <code>stderr</code> and return codes.  A lot of algorithms, like in ITK, are not interactive anyway and by writing them as CLI modules you can reuse the executable in batch jobs or other environments without having Slicer as a dependency.</p>

---

## Post #4 by @Prashant_Pandey (2020-03-22 22:23 UTC)

<p>Thanks, this is very helpful!</p>
<p>I’ll be sure to tell my lab how to use this forum as a key Slicer resource <img src="https://emoji.discourse-cdn.com/twitter/stuck_out_tongue.png?v=9" title=":stuck_out_tongue:" class="emoji" alt=":stuck_out_tongue:"></p>

---
