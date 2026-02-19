---
topic_id: 13868
title: "Vtkmrmlcommandlinemodulenode Addobserver Missing Documentati"
date: 2020-10-05
url: https://discourse.slicer.org/t/13868
---

# [vtkMRMLCommandLineModuleNode.AddObserver()] Missing Documentation

**Topic ID**: 13868
**Date**: 2020-10-05
**URL**: https://discourse.slicer.org/t/vtkmrmlcommandlinemodulenode-addobserver-missing-documentation/13868

---

## Post #1 by @strider_hunter (2020-10-05 16:10 UTC)

<p>Using <code>cliNode = slicer.cli.run()</code> returns a <a href="http://apidocs.slicer.org/master/classvtkMRMLCommandLineModuleNode.html" rel="noopener nofollow ugc">vtkMRMLCommandLineModuleNode</a> that can asynchronously call a CLI module.</p>
<p>It is shown <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python" rel="noopener nofollow ugc">here</a> that one can use the <code>cliNode.AddObserver()</code> callback for when the “<strong>cliNode is modified</strong>”.</p>
<p>I was unable to find any documentation on what this means exactly?  When I print the output of the callback I get a lot of events. But the only unique <code>caller.GetStatus():caller.GetStatusString()</code> values are “2:Running” or “32:Completed”. So why is the callback called so many times if the modification of the CLI module takes place only twice.</p>
<p>This is not a blocker to my work and I was just curious since I was unable to find documentation around it.</p>

---

## Post #2 by @lassoan (2020-10-06 20:21 UTC)

<aside class="quote no-group" data-username="strider_hunter" data-post="1" data-topic="13868">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/strider_hunter/48/8253_2.png" class="avatar"> strider_hunter:</div>
<blockquote>
<p>So why is the callback called so many times if the modification of the CLI module takes place only twice.</p>
</blockquote>
</aside>
<p>The callback is called many times because progress is updated more often than the status (percentage complete, name of current phase and operation, etc.).</p>

---
