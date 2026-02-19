---
topic_id: 21713
title: "Is It Possible To Split A Python Extension Into Multiple Fil"
date: 2022-01-31
url: https://discourse.slicer.org/t/21713
---

# Is it possible to split a python extension into multiple Files?

**Topic ID**: 21713
**Date**: 2022-01-31
**URL**: https://discourse.slicer.org/t/is-it-possible-to-split-a-python-extension-into-multiple-files/21713

---

## Post #1 by @tsims (2022-01-31 15:15 UTC)

<p>Hi everyone,</p>
<p>I have been working on a python extension for slicer, but the .py file has started getting rather large, and I wanted to break it into more digestible chunks.</p>
<p>Is it possible to move the Widget and Logic classes to different files and import them from the main file?</p>
<p>Ideally my project structure would look something like this:</p>
<p>/Extension<br>
|-- Extension.py<br>
|-- ExtensionWidget.py<br>
|-- ExtensionLogic.py</p>
<p>Where I import ExtensionWidget and Extension logic into the main Extension file.</p>
<p>I tried setting this up, but Slicer doesn’t seem to be detecting the UI or the Logic as a part of the main extension. And help is appreciated, thanks!</p>

---

## Post #2 by @pieper (2022-01-31 15:24 UTC)

<p>Yes, you can make a lib folder and put your extra py files in that.  There are lots of examples in the extension index, but <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Animator">here a simple one</a>.  Slicer looks at all the .py files in the top level and tries to interpret them as modules.</p>

---

## Post #3 by @pieper (2022-01-31 15:26 UTC)

<p>Looking at it now the link I sent is maybe not the best example but lots of modules in that repo follow the same pattern.</p>

---

## Post #4 by @lassoan (2022-02-01 04:39 UTC)

<p>Here is another example: <a href="https://github.com/SlicerHeart/SlicerHeart/tree/master/ValveAnnulusAnalysis" class="inline-onebox">SlicerHeart/ValveAnnulusAnalysis at master · SlicerHeart/SlicerHeart · GitHub</a></p>

---

## Post #5 by @tsims (2022-02-01 14:04 UTC)

<p>Thank you both so much for the help, I was able to figure everything out with this advice!</p>
<p>For splitting the Widget and Logic classes to different files, I just had to make sure that I pointed to the right locations from the main plugin file as well!</p>
<p>e.g.<br>
Module.py</p>
<pre><code class="lang-auto">import ModuleLib.Widget as mw

class Module(ScriptedLoadableModule):
    ...

ModuleWidget = mw
</code></pre>

---

## Post #6 by @tsims (2022-02-04 21:05 UTC)

<p>Just noticed something that doing this actually caused, and was wondering if there was a way to fix/work around it…</p>
<p>Now when I reload my module using the developer tools, it doesn’t seem to update the files that are imported from other locations, just the main module file. Is there a way to tell slicer it needs to reload these files too when it updates?</p>
<p>Thanks!</p>

---

## Post #7 by @lassoan (2022-02-08 20:38 UTC)

<p>Yes, if you split up your module into multiple files then reloading becomes more complex. In the example module that I linked above you can also find how additional .py files can be reloaded dynamically:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerHeart/SlicerHeart/blob/9dc27d8fb8b19e59bef78be76b977064776bbedd/ValveAnnulusAnalysis/ValveAnnulusAnalysis.py#L785-L798">
  <header class="source">

      <a href="https://github.com/SlicerHeart/SlicerHeart/blob/9dc27d8fb8b19e59bef78be76b977064776bbedd/ValveAnnulusAnalysis/ValveAnnulusAnalysis.py#L785-L798" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerHeart/SlicerHeart/blob/9dc27d8fb8b19e59bef78be76b977064776bbedd/ValveAnnulusAnalysis/ValveAnnulusAnalysis.py#L785-L798" target="_blank" rel="noopener">SlicerHeart/SlicerHeart/blob/9dc27d8fb8b19e59bef78be76b977064776bbedd/ValveAnnulusAnalysis/ValveAnnulusAnalysis.py#L785-L798</a></h4>



    <pre class="onebox">      <code class="lang-py">
        <ol class="start lines" start="785" style="counter-reset: li-counter 784 ;">
            <li>def onReload(self):</li>
            <li>  logging.debug("Reloading ValveAnnulusAnalysis")</li>
            <li>
            </li>
<li>  packageName='HeartValveLib'</li>
            <li>  submoduleNames=['util', 'LeafletModel', 'SmoothCurve', 'ValveRoi', 'PapillaryModel', 'ValveModel', 'HeartValves']</li>
            <li>  import imp</li>
            <li>  f, filename, description = imp.find_module(packageName)</li>
            <li>  package = imp.load_module(packageName, f, filename, description)</li>
            <li>  for submoduleName in submoduleNames:</li>
            <li>    f, filename, description = imp.find_module(submoduleName, package.__path__)</li>
            <li>    try:</li>
            <li>        imp.load_module(packageName+'.'+submoduleName, f, filename, description)</li>
            <li>    finally:</li>
            <li>        f.close()</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Note, that reloading can be tricky. For example, if you reload the .py files in incorrect order (<code>a.py</code> uses <code>b.py</code>; but you reload <code>a.py</code> before <code>b.py</code>) then you may find that you need to reload multiple times to get everything updated.</p>

---
