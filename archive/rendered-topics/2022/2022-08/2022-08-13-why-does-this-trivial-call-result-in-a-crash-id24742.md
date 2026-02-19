---
topic_id: 24742
title: "Why Does This Trivial Call Result In A Crash"
date: 2022-08-13
url: https://discourse.slicer.org/t/24742
---

# Why does this trivial call result in a crash?

**Topic ID**: 24742
**Date**: 2022-08-13
**URL**: https://discourse.slicer.org/t/why-does-this-trivial-call-result-in-a-crash/24742

---

## Post #1 by @chir.set (2022-08-13 20:24 UTC)

<p>I am trying to create a module in C++ and am stumbling on a crash on line 4 below :</p>
<pre><code class="lang-auto">vtkMRMLNode * fiducialNode = d-&gt;inputFiducialSelector-&gt;currentNode();
vtkMRMLMarkupsFiducialNode * fiducialNodeReal = vtkMRMLMarkupsFiducialNode::SafeDownCast(fiducialNode);
std::cout &lt;&lt; fiducialNodeReal-&gt;GetClassName() &lt;&lt; std::endl; // OK
std::cout &lt;&lt; fiducialNodeReal-&gt;GetNumberOfControlPoints() &lt;&lt; std::endl; // Crash
</code></pre>
<p>The module is created using the extension wizard. The code is executed when a button is clicked. Debugging does not help, no thread is available on crash (Slicer and the module are compiled with RelWithDebInfo).</p>
<p>This very primitive <a href="https://github.com/chir-set/Tinkering/blob/9cf3c92bd44405272753796bd63c25dae0a17ee0/Test0/qSlicerTest0ModuleWidget.cxx#L77" rel="noopener nofollow ugc">sample</a> illustrates the issue.</p>
<p>I wish to avoid a fallback on Python, and would appreciate any comment to help resolve this.</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2022-08-13 21:01 UTC)

<p>It seems that <code>fiducialNodeReal</code> is a null pointer. You can confirm this by adding a null-pointer check or building Slicer in debug mode.</p>
<p>In <code>RelWithDebInfo</code> mode, unnecessary temporary variables are optimized out, so you won’t be able to step through the source code lines that create them.</p>

---

## Post #3 by @chir.set (2022-08-14 08:39 UTC)

<p>Thanks for replying.</p>
<p>While comparing with other C++ modules, I ended up with <a href="https://github.com/chir-set/Tinkering/commit/cb9867a47f40c857b53facf4fc79f72103cce872" rel="noopener nofollow ugc">this</a> efficient patch.</p>
<p>Should the extension wizard template for a loadable module be updated?</p>

---
