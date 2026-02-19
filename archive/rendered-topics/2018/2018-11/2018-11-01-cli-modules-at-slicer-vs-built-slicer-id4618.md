---
topic_id: 4618
title: "Cli Modules At Slicer Vs Built Slicer"
date: 2018-11-01
url: https://discourse.slicer.org/t/4618
---

# Cli modules at Slicer vs built Slicer

**Topic ID**: 4618
**Date**: 2018-11-01
**URL**: https://discourse.slicer.org/t/cli-modules-at-slicer-vs-built-slicer/4618

---

## Post #1 by @siaeleni (2018-11-01 19:20 UTC)

<p>Hi All,</p>
<p>I am trying to run a CLI module from python:</p>
<p>cliNode = slicer.cli.run( slicer.modules.linemarkerregistration, None, parameters, True)</p>
<p>When I am running that on Slicer that I build, seems that I get the desired OutputText.<br>
But If I run it at a client Slicer(one that you can download and run it) seems that I get an empty OutputText.</p>
<p>Why did that happen? Should I always call cli modules from Slicer that I built?</p>
<p>Thanks,<br>
Eleni</p>

---

## Post #2 by @Sam_Horvath (2018-11-05 15:48 UTC)

<p>Hi:</p>
<p>Is this a custom C++ CLI that you have written and built against Slicer?  In order to ensure that a CLI runs with a certain version of Slicer, they need to be built with the same build environment, and the CLI needs to be built against the same(ish) version of Slicer you are trying to use it in.  So if you are doing a custom module, it will likely only work in the Slicer you have built yourself.  Did you get any error output (modules not found, etc?)</p>
<p>Python modules would be more flexible if you want to test with downloaded binaries, since they just need to match the Slicer API of the binary.</p>
<p>Sam</p>

---

## Post #3 by @siaeleni (2018-11-05 17:03 UTC)

<p>Hi Sam,</p>
<p>It is a C++ CLI custom module that I want to use but seems that is a three-year code. Both cliNode.GetErrorText() and cliNode.GetOutputText() returns me an empty string. I was wondering why that module works on Slicer that I have built (4.9.0 version) and not at binary one(4.8.1 version).<br>
Note: In both environments works fine if I manually insert the module and run it.</p>
<p>So, maybe should be built again with a new environment in order to work?</p>
<p>Thanks a lot,<br>
Eleni</p>

---

## Post #4 by @pieper (2018-11-06 17:26 UTC)

<p>Hi <a class="mention" href="/u/siaeleni">@siaeleni</a> -</p>
<p>Yes, it can be problematic to mix different builds of C++ libraries - the compilers and build settings need to match exactly.  Building the CLI from source to match your build should work.</p>
<p>HTH,<br>
Steve</p>

---
