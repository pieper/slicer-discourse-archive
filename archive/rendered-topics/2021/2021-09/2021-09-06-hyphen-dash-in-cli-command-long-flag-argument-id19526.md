---
topic_id: 19526
title: "Hyphen Dash In Cli Command Long Flag Argument"
date: 2021-09-06
url: https://discourse.slicer.org/t/19526
---

# Hyphen/dash in CLI command long flag argument

**Topic ID**: 19526
**Date**: 2021-09-06
**URL**: https://discourse.slicer.org/t/hyphen-dash-in-cli-command-long-flag-argument/19526

---

## Post #1 by @benzwick (2021-09-06 05:00 UTC)

<p>I am developing a Python CLI module for some software that uses hyphens in command line arguments. I created the XML file and loaded everything into 3D Slicer but I get the following error due to the hyphen/dash in the long flags:</p>
<pre><code class="lang-auto">ModuleDescriptionParser Error: &lt;longflag&gt; can only contain letters, numbers and underscores and must start with a _ or letter. The offending name is "input-file"
</code></pre>
<p>Is there any way to use flags with hyphens, e.g. <code>--input-file</code>, in a CLI extension?</p>

---

## Post #2 by @pieper (2021-09-07 17:41 UTC)

<p>At least for C++ cli modules the <code>--</code> is added automatically if you just specify <code>input-file</code>.  Is this not the case for python cli?</p>

---

## Post #3 by @benzwick (2021-09-08 01:56 UTC)

<p>Yes, the <code>--</code> at the start is added automatically (in the XML file I use <code>&lt;longflag&gt;input-file&lt;/longflag&gt;</code>) but the hyphen in the middle in e.g. <code>input-file</code> is not allowed.</p>

---

## Post #4 by @lassoan (2021-09-08 02:47 UTC)

<p>If you cannot change the command-line argument names to be compatible with the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/SlicerExecutionModel#XML_Schema">Slicer Execution Model</a>, then you can create a Python scripted CLI module that runs the executable. See for example <a href="https://github.com/simonoxen/SlicerANTs/tree/master/antsCommand">this module</a>.</p>

---

## Post #5 by @benzwick (2021-09-08 03:35 UTC)

<p>I’ve changed the arguments in my program to remove the hyphens. However, there are many programs that use this style. Is there any change planned for Slicer Execution Model to support these argument names in the future? The Python argparse module simply replaces the hyphen <code>-</code> with underscore <code>_</code> so something similar could be done in Slicer XML as well.</p>
<p>As an aside, I am also working on creating an extension for a standalone C++ CLI program that has similar argument names. Do you recommend to use the same approach as the antsCommand module in the link you mentioned (i.e. create a Python CLI module that provides an interface to the external C++ program)?</p>

---

## Post #6 by @lassoan (2021-09-08 03:50 UTC)

<aside class="quote no-group" data-username="benzwick" data-post="5" data-topic="19526">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/benzwick/48/80521_2.png" class="avatar"> benzwick:</div>
<blockquote>
<p>I’ve changed the arguments in my program to remove the hyphens. However, there are many programs that use this style. Is there any change planned for Slicer Execution Model to support these argument names in the future?</p>
</blockquote>
</aside>
<p>Yes, indeed many programs allow using long arguments but usually short form of the arguments are available, too. For example, if a program accepts <code>--input-file</code> and <code>-i</code> to specify an input file then we simply use the short form.</p>
<p>I agree that it would be nice to have a way to specify arguments that contain <code>-</code> in the name. However, since you can usually use the short form of the arguments, change the argument names, or if all else fail then use an adaptor script, this enhancement has never made it to the top of anyone’s priority list. If you decide to implement it then we’ll be happy to review and merge this improvement.</p>

---

## Post #7 by @lassoan (2021-09-08 03:57 UTC)

<p>By the way, this is a known limitation - see <a href="https://github.com/Slicer/SlicerExecutionModel/issues/17">https://github.com/Slicer/SlicerExecutionModel/issues/17</a></p>

---
