# How to customize SubjectHierarchyTreeView?

**Topic ID**: 14358
**Date**: 2020-11-01
**URL**: https://discourse.slicer.org/t/how-to-customize-subjecthierarchytreeview/14358

---

## Post #1 by @apparrilla (2020-11-01 10:12 UTC)

<p>Hi!<br>
I want to customize a SubjectHierarchyTreeView Widget in a module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f012b3f94b4c8beb9ec14a38679adf2fda2fa921.png" data-download-href="/uploads/short-url/yfMFadEh4QgSPIXDpG2TY5vyhFL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f012b3f94b4c8beb9ec14a38679adf2fda2fa921_2_517x291.png" alt="image" data-base62-sha1="yfMFadEh4QgSPIXDpG2TY5vyhFL" width="517" height="291" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f012b3f94b4c8beb9ec14a38679adf2fda2fa921_2_517x291.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f012b3f94b4c8beb9ec14a38679adf2fda2fa921_2_775x436.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f012b3f94b4c8beb9ec14a38679adf2fda2fa921.png 2x" data-dominant-color="242424"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">992×558 5.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Things to change:</p>
<ul>
<li>Filter Model nodes:  made</li>
</ul>
<blockquote>
<p>self.uit.SubjectHierarchyTreeView.nodeTypes = [“vtkMRMLModelNode”]</p>
</blockquote>
<ul>
<li>Change header text: “Node” → “Model”</li>
<li>Hide columns: “ID”, “color”</li>
<li>Change colums order: Put View/Hide first one</li>
<li>Add new columns: should be lovely to add an “Opacity slider”, something like Segementations Module one.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a03cadac0726d9478ea8cfa07963b6021eb3c8d3.png" data-download-href="/uploads/short-url/mRwoGw5A7vJoiIDHrx8u8jh1r35.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a03cadac0726d9478ea8cfa07963b6021eb3c8d3.png" alt="image" data-base62-sha1="mRwoGw5A7vJoiIDHrx8u8jh1r35" width="517" height="48" data-dominant-color="2F2F2F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">919×87 2.16 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Slicer ver: 4.11.20200930 r29402 / 002be18<br>
OS: Win10</p>
<p>Thanks on advace!</p>

---

## Post #2 by @cpinter (2020-11-01 21:08 UTC)

<aside class="quote no-group" data-username="apparrilla" data-post="1" data-topic="14358">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<p>Hide columns: “ID”, “color”</p>
</blockquote>
</aside>
<pre><code class="lang-auto">subjectHierarchyTreeView.setColumnHidden(subjectHierarchyTreeView.model().idColumn, True)
subjectHierarchyTreeView.setColumnHidden(subjectHierarchyTreeView.model().colorColumn, True)
</code></pre>
<aside class="quote no-group" data-username="apparrilla" data-post="1" data-topic="14358">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<p>Change header text: “Node” → “Model”</p>
</blockquote>
</aside>
<p>Probably something like this:<br>
<code>subjectHierarchyTreeView.model().setHorizontalHeaderLabels(['Models', ...])</code></p>
<aside class="quote no-group" data-username="apparrilla" data-post="1" data-topic="14358">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<p>Change colums order</p>
</blockquote>
</aside>
<p>I believe you can do it by calling functions like <code>setNameColumn</code> with the desired column index.</p>
<aside class="quote no-group" data-username="apparrilla" data-post="1" data-topic="14358">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<p>Add new columns</p>
</blockquote>
</aside>
<p>I’m afraid for this you’ll need to extend or subclass the qMRMLSubjectHierarchyModel class.</p>

---

## Post #3 by @apparrilla (2020-11-03 23:44 UTC)

<p>Hi <a class="mention" href="/u/cpinter">@cpinter</a>!<br>
Thanks to your answare, I´ve able to get this result:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5974ce141b1eb13023e43284ed87cc939af1ed34.png" alt="image" data-base62-sha1="cLmKoUvsMsJpyXKwnIGLIKlQ7Qg" width="451" height="78"></p>
<p>This is my code:</p>
<blockquote>
<p>self.ui.SubjectHierarchyTreeView.nodeTypes = [“vtkMRMLModelNode”]<br>
self.ui.SubjectHierarchyTreeView.setColumnHidden(self.uit.SubjectHierarchyTreeView.model().idColumn, True)<br>
self.ui.SubjectHierarchyTreeView.setColumnHidden(self.uit.SubjectHierarchyTreeView.model().colorColumn, True)<br>
self.ui.SubjectHierarchyTreeView.setColumnHidden(self.uit.SubjectHierarchyTreeView.model().transformColumn, True)<br>
self.ui.SubjectHierarchyTreeView.model().setHorizontalHeaderLabels([‘Models’, …])<br>
self.ui.SubjectHierarchyTreeView.setMRMLScene( slicer.mrmlScene )</p>
</blockquote>
<p>I havent been able to change columns order after many attempts with different methods from <a href="https://discourse.slicer.org/t/populating-qmrmlsubjecthierarchytreeview/10776">qMRMLSubjectHierarchyTreeView</a> Class and <a href="https://apidocs.slicer.org/v4.8/classqMRMLSubjectHierarchyModel.html" rel="noopener nofollow ugc">qMRMLSubjectHierarchyModel</a> documentation.</p>
<p>Thank you very much for your help!</p>

---

## Post #4 by @lassoan (2020-11-03 23:56 UTC)

<p>You can show/hide and change the order of columns by specifying colorColumn, descriptionColumn, etc. values. See <a href="http://apidocs.slicer.org/master/classqMRMLSubjectHierarchyModel.html">documentation</a>.</p>

---

## Post #5 by @apparrilla (2020-11-04 00:46 UTC)

<p>Sorry <a class="mention" href="/u/lassoan">@lassoan</a> . I don´t know how to do it…<br>
Error message:</p>
<blockquote>
<p>line 200, in setup self.ui.SubjectHierarchyTreeView.model().setVisibilityColumn(0)<br>
AttributeError: qMRMLSubjectHierarchyModel has no attribute named ‘setVisibilityColumn’</p>
</blockquote>

---

## Post #6 by @lassoan (2020-11-04 02:23 UTC)

<p><code>colorColumn</code> is a property. You can set it as:</p>
<pre><code>self.ui.SubjectHierarchyTreeView.model().visibilityColumn = 0
</code></pre>
<p>This documentation page can help in interpreting the API documentation: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#doxygen-style-documentation">https://slicer.readthedocs.io/en/latest/developer_guide/api.html#doxygen-style-documentation</a></p>

---

## Post #7 by @apparrilla (2020-11-04 14:49 UTC)

<p>I´ve triyed:</p>
<blockquote>
<p>self.uit.SubjectHierarchyTreeView.model().visibilityColumn = 0<br>
self.uit.SubjectHierarchyTreeView.model().nameColumn = 1<br>
self.uit.SubjectHierarchyTreeView.model().descriptionColumn = 2</p>
</blockquote>
<p>But result is the same:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3eace849337bd9633e3cbb7832b94a4949f250b.png" alt="image" data-base62-sha1="no4TIKWDw3wsIwQp9zceJ5NAysH" width="484" height="88"></p>
<p>Sorry to waste your precious time…!</p>

---

## Post #8 by @lassoan (2020-11-04 18:48 UTC)

<p>It works for me. Note that you need to change the headers label and icons with a separate call (it could be nice if that was updated automatically, if you have time to implement this then a pull request would be welcome):</p>
<pre><code class="lang-python">tv=slicer.qMRMLSubjectHierarchyTreeView()
tv.model().visibilityColumn=3
tv.model().colorColumn=2
tv.setMRMLScene(slicer.mrmlScene)
tv.model().setHorizontalHeaderLabels(['a','b','c','d','e','f'])
tv.show()
</code></pre>

---

## Post #9 by @apparrilla (2020-11-04 22:13 UTC)

<p>Ok. My problem was the headers order and columns width. Items reorder in new columns distribution but but headers stay in original order.</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="14358">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>it could be nice if that was updated automatically, if you have time to implement this then a pull request would be welcome</p>
</blockquote>
</aside>
<p>I´d like to help but it´s too much for my current poor code skills…</p>
<p>Thanks to all.</p>

---
