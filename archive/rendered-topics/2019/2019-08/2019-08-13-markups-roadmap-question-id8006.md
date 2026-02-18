# Markups roadmap question

**Topic ID**: 8006
**Date**: 2019-08-13
**URL**: https://discourse.slicer.org/t/markups-roadmap-question/8006

---

## Post #1 by @muratmaga (2019-08-13 17:04 UTC)

<p>On the Slicer5 roadmap link, I saw proposed changes to coordinate system for markups and models to be LPS.<br>
<a href="https://www.slicer.org/wiki/Documentation/Labs/Slicer5-roadmap#Coordinate_system_in_files" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Labs/Slicer5-roadmap#Coordinate_system_in_files</a></p>
<p>I am curious how this will impact the existing data being loaded in the Slicer5. We have thousands of landmark files from published datasets (and associated models/volumes), and I would like to know the impact.</p>

---

## Post #2 by @lassoan (2019-08-15 15:40 UTC)

<p>All medical imaging software I know (except Slicer) uses LPS coordinate system in files. So, we don’t really have a choice and follow this convention to avoid errors and frustration of users.</p>
<p>To make the transition smooth, since 2017 Slicer writes it in the header of all saved model and markup files what coordinate system is used (LPS or RAS). When we change Slicer to start writing LPS files as default, all the new and old files can still be read correctly.</p>
<p>The final step is to change how files without coordinate system definition are interpreted by default. Old scenes will still be loaded correctly (because from the scene file version we know that the default was RAS back then). For standalone model files that were created by Slicer before 2017 the user will have to choose the correct coordinate system in Add data dialog manually. We can delay this final step for a couple of more years to give users more time to update their model files.</p>

---

## Post #3 by @muratmaga (2019-08-15 16:52 UTC)

<p>We don’t keep the scene files unfortunately, only the models/volumes and associated fcsv file.</p>
<p>But it is good to know that at least files since 2017 will be automatically converted. For older files, we can programmatically add those headers. This is a fairly significant change for us.</p>
<p>What is the plan to save for re-saving on old fcsv file imported to the new version? Will it remain intact (unless a property modified), or as the user saving the scene will automatically get overwritten with new coordinates and coordinate system.<br>
I am asking this more from a data preservation/integrity perspective</p>

---

## Post #4 by @lassoan (2019-08-15 17:18 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="8006">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>What is the plan to save for re-saving on old fcsv file imported to the new version?</p>
</blockquote>
</aside>
<p>Coordinate system storage in fcsv files was added many years ago, so most likely all your fcsv files already have <code># CoordinateSystem</code> in their header.</p>
<p>If you need to update any file then you can load it and re-save it. You can do it in the GUI by making sure the checkbox in save data dialog is checked. You can also write a python script to update all the files in a folder hierarchy (it should be really simple, about 10-15 lines of code).</p>

---
