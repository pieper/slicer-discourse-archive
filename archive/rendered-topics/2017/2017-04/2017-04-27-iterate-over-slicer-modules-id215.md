---
topic_id: 215
title: "Iterate Over Slicer Modules"
date: 2017-04-27
url: https://discourse.slicer.org/t/215
---

# Iterate over slicer modules

**Topic ID**: 215
**Date**: 2017-04-27
**URL**: https://discourse.slicer.org/t/iterate-over-slicer-modules/215

---

## Post #1 by @mirclem (2017-04-27 18:15 UTC)

<p>Hello,</p>
<p>I am working on creating a program to get all the modules loaded in Slicer. I know I can access the list with all the module names, I also know that I can access a module by hard typing the module name like “slicer.modules.modelmaker”. But is there a way to access a module with a variable or a string?</p>
<p>The first command I tried was slicer.modules[variable] but it can’t work because modules is a namespace.</p>
<p>Thanks,<br>
Clément</p>

---

## Post #2 by @ihnorton (2017-04-27 18:18 UTC)

<aside class="quote no-group" data-username="mirclem" data-post="1" data-topic="215">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mirclem/48/3356_2.png" class="avatar"> mirclem:</div>
<blockquote>
<p>But is there a way to access a module with a variable or a string?</p>
</blockquote>
</aside>
<p><code>getattr(slicer.modules,'units')</code></p>

---

## Post #3 by @mirclem (2017-04-27 18:23 UTC)

<p>Hum, sometimes when you don’t find what you want, it’s nice to get back to python basics.</p>
<p>Thanks a lot.</p>

---

## Post #4 by @Johan_Andruejol (2017-04-27 18:29 UTC)

<p>Clement,</p>
<p>You could also use the slicer util method <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L467" rel="nofollow noopener">getModule()</a>.</p>
<p>Johan</p>

---

## Post #5 by @mirclem (2017-05-01 20:46 UTC)

<p>Based on the work done before, I was able to access the module, then the widget and the currentCLInode. So, I can get the parameters names, flags, types. But, I can’t find the way to access the current value corresponding to a parameter.<br>
I saw there is a function ‘WriteParameterFile’ which is able to access the value and match it with the key but the <a href="https://github.com/Slicer/Slicer/blob/9e7de7256691782a2650a312313d47aafa31c4a2/Libs/MRML/CLI/vtkMRMLCommandLineModuleNode.cxx#L1001-L1013" rel="nofollow noopener">source code</a> can’t help me.</p>

---

## Post #6 by @Johan_Andruejol (2017-05-01 21:04 UTC)

<p>Hey Clement,</p>
<p>Did you look at <a href="https://github.com/Slicer/Slicer/blob/9e7de7256691782a2650a312313d47aafa31c4a2/Libs/MRML/CLI/vtkMRMLCommandLineModuleNode.h#L250" rel="nofollow noopener">GetParameterAsString()</a> ?</p>
<p>Johan</p>

---

## Post #7 by @mirclem (2017-05-01 21:08 UTC)

<p>Thank you so much Johan!</p>

---

## Post #8 by @lassoan (2017-05-15 23:52 UTC)

<p>A post was split to a new topic: <a href="/t/access-color-table-in-cli-module/318">Access color table in CLI module</a></p>

---
