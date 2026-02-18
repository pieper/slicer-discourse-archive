# Build error caused by qSlicerSubjectHierarchyPlotsPlugin

**Topic ID**: 2060
**Date**: 2018-02-10
**URL**: https://discourse.slicer.org/t/build-error-caused-by-qslicersubjecthierarchyplotsplugin/2060

---

## Post #1 by @chir.set (2018-02-10 17:52 UTC)

<p>I’m having this error while building Slicer on Linux (Qt5/VTK9, gcc 7.3.0) :</p>
<pre><code> /home/arc/src/Slicer/Modules/Loadable/Plots/SubjectHierarchyPlugins/qSlicerSubjectHierarchyPlotsPlugin.cxx:306:10: error: cannot convert 'bool' to 'vtkMRMLPlotViewNode*' in return
   return false;
</code></pre>
<p>This trivial patch allows the build to complete :</p>
<pre><code>diff --git a/Modules/Loadable/Plots/SubjectHierarchyPlugins/qSlicerSubjectHierarchyPlotsPlugin.cxx b/Modules/Loadable/Plots/SubjectHierarchyPlugins/qSlicerSubjectHierarchyPlotsPlugin.cxx
index 9f9545f0a..559875adb 100644
--- a/Modules/Loadable/Plots/SubjectHierarchyPlugins/qSlicerSubjectHierarchyPlotsPlugin.cxx
+++ b/Modules/Loadable/Plots/SubjectHierarchyPlugins/qSlicerSubjectHierarchyPlotsPlugin.cxx
@@ -303,5 +303,5 @@ vtkMRMLPlotViewNode* qSlicerSubjectHierarchyPlotsPlugin::getPlotViewNode()const
     }
 
   // no valid plot view in current layout
-  return false;
+  return NULL;
 } 
</code></pre>
<p>I guess it’s how the compiler equates false and NULL.</p>
<p>[Sorry for the title, the web app wants a complete sentence !. It doesn’t accept : Build error with qSlicerSubjectHierarchyPlotsPlugin , for example]</p>

---

## Post #2 by @chir.set (2018-02-10 18:05 UTC)

<p>And when Slicer is launched or the Python interactor is shown, this message is shown :</p>
<p>Failed to import PythonQt.qSlicerPlotsSubjectHierarchyPlugins</p>
<p>I can’t know how does it impact anything.</p>

---

## Post #3 by @lassoan (2018-02-10 18:23 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="1" data-topic="2060">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Sorry for the title, the web app wants a complete sentence !. It doesn’t accept : Build error with qSlicerSubjectHierarchyPlotsPlugin , for example</p>
</blockquote>
</aside>
<p>This is a feature developed with a good intention (make it harder to submit low-quality posts) but it clearly did not work well in this case. The problem was that qSlicerSubjectHierarchyPlotsPlugin word was too long. I have now increased “title max word length” from 30 to 50 and it solved the problem. As it turns out, Discourse is intentionally giving vague error message for titles that it does not like, to force you to think about how to improve the title in general, instead of just making some minimal formal change to make the title acceptable. The mechanism works well in general but in cases like this it is really frustrating. We’ll keep tuning settings based on forum users feedback.</p>

---

## Post #4 by @lassoan (2018-02-10 18:26 UTC)

<p>Thanks for reporting this, the build error is fixed now.</p>
<aside class="quote no-group" data-username="chir.set" data-post="2" data-topic="2060">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>I can’t know how does it impact anything.</p>
</blockquote>
</aside>
<p>The subject hierarchy plugin makes plot charts show up in the subject hierarchy tree in Data module.</p>

---
