---
topic_id: 45252
title: "Writing A Scripted Subject Hierarchy Plugin Documentation La"
date: 2025-11-27
url: https://discourse.slicer.org/t/45252
---

# Writing a Scripted Subject Hierarchy Plugin -- documentation lacking

**Topic ID**: 45252
**Date**: 2025-11-27
**URL**: https://discourse.slicer.org/t/writing-a-scripted-subject-hierarchy-plugin-documentation-lacking/45252

---

## Post #1 by @shai-ikko (2025-11-27 13:33 UTC)

<p>Hi,</p>
<p>Recently I’ve been writing an internal-use Subject Hierarchy plugin. I ran into some difficulties that stem, IMO, from lacking documentation, so I want to share what I’ve learned with a view to getting some comments and eventually improving the docs.</p>
<p>The first, and most important issue, is the context. For a class to serve as a Subject Hierarchy Plugin, it needs to</p>
<ul>
<li>Be written in the main file of an Extension Module</li>
<li>Be named exactly as the module, with the suffix <code>SubjectHierarchyPlugin</code></li>
</ul>
<p>That is, if your module is named <code>Kawabanga</code>, the plugin class must reside in <code>Kawabanga.py</code> and be named <code>KawabangaSubjectHiearachyPlugin</code>.</p>
<p>This is followed, but not explicitly declared, in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#subject-hierarchy-plugin-offering-view-context-menu-action" rel="noopener nofollow ugc">the example plugin</a> in the script repository; that example is also a bit misleading, because it is (correctly) described as an example for a special plugin (one that operates in views, rather than in the subject hierarchy).</p>
<p>Other plugins which claim to serve as examples – e.g. <code>SegmentEditorSubjectHierarchyPlugin</code> in the sources – don’t actually follow these rules, and so they are misleading.</p>
<p>When fixing the documentation, we should also modernize the examples – currently, the way to iterate over children is presented in the script repository as</p>
<pre><code class="lang-auto">children = vtk.vtkIdList()
shNode.GetItemChildren(parent, children)
for i in range(children.GetNumberOfIds()):
  child = children.GetId(i)
  ...
</code></pre>
<p>but with modern Python and Slicer, this can be done with</p>
<pre><code class="lang-auto">shNode.GetItemChildren(parent, children:=[])
for child in children:
  ...
</code></pre>
<p>I will come back to this later, but wanted to raise this while fresh in mind and maybe get some feedback.</p>
<p>Thanks!</p>

---

## Post #2 by @cpinter (2025-11-27 14:19 UTC)

<p>Just very quickly due to not having any time today.</p>
<blockquote>
<p>No documentation</p>
</blockquote>
<p>You’re right, this could be improved.</p>
<blockquote>
<p>That is, if your module is named <code>Kawabanga</code>, the plugin class must reside in <code>Kawabanga.py</code> and be named <code>KawabangaSubjectHiearachyPlugin</code>.</p>
</blockquote>
<p>I’m pretty sure that this is not correct. Please look at for example <code>SlicerHeart\ValveAnnulusAnalysis\HeartValveLib\HeartValvesSubjectHierarchyPlugin.py</code></p>
<blockquote>
<p>but with modern Python and Slicer</p>
</blockquote>
<p>Actually, I think what we’d suggest would be <code>slicer.util.getSubjectHierarchyItemChildren</code>, but what you’re suggesting is great too. Honestly I’d need to look at how it works exactly.</p>

---

## Post #3 by @shai-ikko (2025-12-03 16:18 UTC)

<aside class="quote no-group quote-modified" data-username="cpinter" data-post="2" data-topic="45252">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<blockquote>
<p>That is, if your module is named <code>Kawabanga</code>, the plugin class must reside in <code>Kawabanga.py</code> and be named <code>KawabangaSubjectHiearachyPlugin</code>.</p>
</blockquote>
<p>I’m pretty sure that this is not correct. Please look at for example <code>SlicerHeart\ValveAnnulusAnalysis\HeartValveLib\HeartValvesSubjectHierarchyPlugin.py</code></p>
</blockquote>
</aside>
<p>So, yes, my claim was inaccurate. The plugin class doesn’t really need to be in the same file as the main module. Its name only has to match the name of the module it is actually in, that is:</p>
<ul>
<li>If the module name ends with <code>SubjectHierarchyPlugin</code>, the plugin class must have the same name;</li>
<li>Otherwise, the plugin class must be named as the module with the suffix <code>SubjectHierarchyPlugin</code>.</li>
</ul>
<p>That is, even if your main module is <code>Kawabanga.py</code>, you plugin class may be named <code>YipeeSubjectHierachyPlugin</code>. And then the file it is defined in can be either <code>YipeeSubjectHierachyPlugin.py</code> or <code>Yipee.py</code>, but it <em>must</em> be one of these two.</p>
<p>This is enforced in <code>qSlicerSubjectHierarchyScriptedPlugin::setPythonSource(const QString filePath)</code></p>
<p>More of this later.</p>

---
