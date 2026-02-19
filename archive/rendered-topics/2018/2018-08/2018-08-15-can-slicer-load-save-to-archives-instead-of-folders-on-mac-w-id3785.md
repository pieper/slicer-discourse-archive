---
topic_id: 3785
title: "Can Slicer Load Save To Archives Instead Of Folders On Mac W"
date: 2018-08-15
url: https://discourse.slicer.org/t/3785
---

# Can Slicer load/save to archives instead of folders, on Mac/Windows?

**Topic ID**: 3785
**Date**: 2018-08-15
**URL**: https://discourse.slicer.org/t/can-slicer-load-save-to-archives-instead-of-folders-on-mac-windows/3785

---

## Post #1 by @jdx-john (2018-08-15 12:44 UTC)

<p>I think this is a dev rather than support question - we have a custom Slicer application which saves a plan/project to a single user-specified directory so plans are portable. We also use a traditional “load/save file” approach instead of having a database of plans managed by Slicer.</p>
<p>However because it’s a regular directory users can see inside, and it could be slicker if the directory was actually a file. Or <em>looked</em> like a file. I’m aware on Mac that application packages .app are an archive you can look inside with Finder, and on Windows you can look inside a .ZIP in Explorer.</p>
<p>Is there a good way we can make our Slicer saved projects look like a single file without impacting load/save performance (folders typically end up 2-3Gb)? Even to let you double-click so they launch our application? But we still would need ability to inspect the contents.</p>
<p>Maybe you can flag a directory to appear as a file? Maybe you can use a non-compressed ZIP/archive or other file-system trick?</p>

---

## Post #2 by @ihnorton (2018-08-15 14:19 UTC)

<aside class="quote no-group" data-username="jdx-john" data-post="1" data-topic="3785">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a6a055/48.png" class="avatar"> jdx-john:</div>
<blockquote>
<p>Is there a good way we can make our Slicer saved projects look like a single file</p>
</blockquote>
</aside>
<p>The save interface should offer an option for MRB for the .mrml file, which will bundle everything in to a zip archive. See: <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/SupportedDataFormat" class="inline-onebox">Documentation/Nightly/SlicerApplication/SupportedDataFormat - Slicer Wiki</a></p>
<aside class="quote no-group" data-username="jdx-john" data-post="1" data-topic="3785">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a6a055/48.png" class="avatar"> jdx-john:</div>
<blockquote>
<p>without impacting load/save performance (folders typically end up 2-3Gb)</p>
</blockquote>
</aside>
<p>The archive MRB is (de)compressed from(to) a temp folder, so there will be <em>some</em> performance hit, possibly a noticeable one for that amount of data. It will depend in part on the CPU, hard disk, and virtual memory configuration (if the temp dir goes to SSD or to RAM without a sync to a spinning disk, then it should be quite fast). I would suggest to try it and see if it meets your performance needs as-is. If not, for starters, a simple change to the code in <code>Libs/MRML/vtkArchive.h</code> to disable compression should help (use <code>compression_type = "store"</code> only).</p>

---

## Post #3 by @jdx-john (2018-08-15 16:17 UTC)

<p>Thanks for that. Yes I can see now MRB is available as a built-in option for Slicer. Aside from performance considerations, I’m curious how that works if you work on a plan and then re-save it. Since it sounds like you’re saying Slicer actually works on a temp-folder which gets (de)compressed to file as needed.</p>
<p>Another route I’d wondered about is if there’s a way for Slicer to <em>think</em> it’s working on a regular folder, which the OS presents to the user as a file. A little searching suggested that Qt has some built-in archive functionality and I wonder if this would make the whole process transparent to Slicer.</p>

---

## Post #4 by @pieper (2018-08-15 17:40 UTC)

<p>Hi <a class="mention" href="/u/jdx-john">@jdx-john</a> -</p>
<p>Yes, with the .mrb option the file is saved in a temp directory and then zipped (if you change a .mrb extension to .zip you can look inside).  The opposite happens on load of an mrb.  If you make incremental changes and then re-save you end up with the potential of a lot of duplicated source data compared to the .mrml approach.</p>
<p>Also note that volumes get compressed on save by default and for large volumes that can be big.  Then the zip (mrb) process re-runs compression of those which is also wasteful.   If performance is a big issue for you it’s possible to bypass that.</p>
<p>You could also look at <a href="https://en.wikipedia.org/wiki/Filesystem_in_Userspace">FUSE</a> with either a tarfs backend to keep things organized an hopefully efficient without needing to change Slicer.</p>

---
