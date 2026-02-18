# What's the best approach to saving additional data associated with a module?

**Topic ID**: 9018
**Date**: 2019-11-04
**URL**: https://discourse.slicer.org/t/whats-the-best-approach-to-saving-additional-data-associated-with-a-module/9018

---

## Post #1 by @mikebind (2019-11-04 22:12 UTC)

<p>I would like to be able to save/restore data from one usage session to another for my scripted python module.  I understand that there is the ability to use a <code>vtkMRMLScriptedModuleParameterNode()</code> like <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting" rel="nofollow noopener">shown here</a>. However, as far as I can tell, all this allows saving is strings as parameters, and I have moderately complex derived data that I would like to save/restore.  This data is currently represented in python in nested dictionaries with entries which are objects that are custom classes (which are defined within my module file).  Would the recommended approach be to just serialize these objects into strings and put them into the parameter node?  If so, are there limits to how big the parameter node values could be (e.g. number of characters or number of bytes)?   Alternatively, am I better off saving the data in some custom format to a file and then having a button to load from that file?  I appreciate any recommendations people have, thanks!</p>

---

## Post #2 by @pieper (2019-11-04 22:44 UTC)

<p>It really depends on exactly how heavyweight your data ends up being and how granular you need to be in responding to events.  For even medium complexity you can often get by with just json strings stored in a node attribute, like <a href="https://github.com/pieper/SlicerAnimator/blob/master/Animator/Animator.py#L722-L729">here</a>.  You are unlikely to hit a limit on the size of these (they are <code>std::string</code> under the hood).  It’s more performance that you would be concerned with.  I suppose you can also pickle your custom python objects into these node attributes too.</p>

---

## Post #3 by @lassoan (2019-11-05 01:33 UTC)

<p>If your json is more than a few hundred characters then it may be more appropriate to store it in a <a href="http://apidocs.slicer.org/master/classvtkMRMLTextNode.html"><code>slicer.vtkMRMLTextNode</code></a>:</p>
<ul>
<li>You have the option to save the text in a separate file (so that you can view/edit more easily in external software).</li>
<li>There is a separate <code>TextModifiedEvent</code> for indicating text content modifications</li>
<li>“Texts” module has a small text editor</li>
<li>You can show/edit the content of the text node in your module using <code>slicer.qMRMLTextWidget</code>
</li>
</ul>
<p>You can keep using the scripted module node for other parameters and add a node reference to the text node to store the json text.</p>

---

## Post #4 by @mikebind (2019-11-05 19:51 UTC)

<p>Thanks for this suggestion and information <a class="mention" href="/u/pieper">@pieper</a>.  My data is more than short strings, but less than extremely huge  (currently ~ 10K characters serialized into json), so probably either of these approaches would work.  I am going to try the TextNode approach suggested by <a class="mention" href="/u/lassoan">@lassoan</a> because the ability to inspect/modify the contents easily within Slicer’s GUI may be handy during development.</p>

---
