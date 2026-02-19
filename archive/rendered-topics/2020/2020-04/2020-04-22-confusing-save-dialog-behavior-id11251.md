---
topic_id: 11251
title: "Confusing Save Dialog Behavior"
date: 2020-04-22
url: https://discourse.slicer.org/t/11251
---

# Confusing "save dialog" behavior

**Topic ID**: 11251
**Date**: 2020-04-22
**URL**: https://discourse.slicer.org/t/confusing-save-dialog-behavior/11251

---

## Post #1 by @muratmaga (2020-04-22 04:41 UTC)

<p>I am not sure when the 5.0 will bereleased but I would like to remind that the save dialog box still suffers from the confusing filename reversion behavior that was discussed previous (I cannot find the thread though).</p>
<p>If you want to try, download MRHead.nrrd, go to save dialog box, change folder, then the delete everything in the filename tab including the extension and rename something without the extension, and save and then try to find the saved file with that name… What will happen, slicer will quickly rename it to original name, and if the file is never saved before you will not get a warning message about file being overwritten. While the data is indeed saved, from a user point of view all is lost.</p>
<p>And we can’t really blame the users not including the extension when they rename, because the field says filename and then right next to it is a field that says format (which practicallly is the extension).</p>
<p>At the time of the thread my suggestion was disabling the ability of editing filenames as the dialog box, and forcing the user to change the node name at the subject hierarchy. Alternatively, if they don’t include an extension and we expect them they should, then make that expectation clear (error message perhaps, refuse to save). Or automatically add the suffix based on the selected format. Current behavior is not acceptable.</p>

---

## Post #2 by @lassoan (2020-04-22 15:19 UTC)

<p>I’ve moved the post here in its dedicated topic so that it can be discussed in detail.</p>
<p>The current behavior has been around for many years, so I would not say it is unacceptable, but it is certainly not ideal.</p>
<p>About the very specific issue: I think disabling “Save” button while a node name is being edited would resolve the confusion. However, the save dialog is quite complicated for new users overall - it is relatively easy to lose data (not actually lose, but make it hard to find).</p>
<p>What do you think about the followings making single-file MRB the default save format? It would solve many issues (all the information in the scene is saved, conflicting node names are automatically renamed, no need to make decisions about file names and formats, etc.).</p>
<p>Or, we can change this a bit even more: we could add separate menu items (and toolbar buttons) for:</p>
<ul>
<li>“Save” and “Save as…” would work the way as in most other software (single-click operation, it would just ask for a filename the first time)</li>
<li>“Export data” - the same as the current save data dialog (maybe the .mrb option would be removed to simplify it a bit)</li>
</ul>

---

## Post #3 by @muratmaga (2020-04-22 15:40 UTC)

<p>Behavior might be around for a while so that people experienced with Slicer developed their own way of dealing with it, but the entire save as dialog box throwing off first-timers quite a bit. With all these excellent improvement to 5.0, I think it would be the time to modify the save action.</p>
<p>Is MRB tested heavily enough to make it the default? I have seen at least two cases (one with me few years ago and one with student in a recent workshop) that we ended up with corrupted volumes (actual volume wasn’t written fully). I never replicated consistently, it might just be coincidence, but we have to test more extensively with the large volumes we work, some of which can be 5-6GB. And how does the compression work with it?</p>
<p>Perhaps rename the <strong>File-&gt;Save</strong> as <strong>File-&gt;Package Scene</strong> (with mrb as the default action) so it is clear what this menu item does, and may be put the add <strong>Save/Save As/Export</strong> to the Data module as right-click actions?</p>

---

## Post #4 by @hherhold (2020-04-22 16:18 UTC)

<p>I would not be in favor of making MRB the default save format - this would result in very large files for nearly all my datasets and load/save times would be excessive.</p>
<p>I’ve also run into corrupted MRB files, as Murat mentioned.</p>

---

## Post #5 by @lassoan (2020-04-22 17:28 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="11251">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p><strong>Export</strong> to the Data module as right-click actions</p>
</blockquote>
</aside>
<p>This is a good idea. Adding export option to data module for storable nodes would be very easy.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="11251">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Is MRB tested heavily enough to make it the default? I have seen at least two cases (one with me few years ago and one with student in a recent workshop) that we ended up with corrupted volumes (actual volume wasn’t written fully).</p>
</blockquote>
</aside>
<p>Yes, it is stable. Several groups always save everything in mrb files and they don’t report any issues. However, I can imagine that you may run out of disk space while creating many-GB archives: first we need to write out the files uncompressed then compress it, so temporarily we may need several times more disk space than the final result. With many laptops today having fast but small SSDs, not everyone always has tens of GBs of free disk space.</p>
<p><a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> has recently made impressive zipping performance optimizations, which may make file saving time more tolerable for large files.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/hherhold">@hherhold</a> Do you have a recipe for reproducing mrb corruption?</p>
<aside class="quote no-group" data-username="hherhold" data-post="4" data-topic="11251">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>I would not be in favor of making MRB the default save format</p>
</blockquote>
</aside>
<p>We can make the default save format configurable in the application settings so that advanced users and those who work with very large data sets can keep deciding manually which file to save.</p>
<p>There are many ways how people prefer to manage their files and changes in file contents and names. To make sure we rework data saving/export in a way that it makes things better for everyone, we need to collect these use cases.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/hherhold">@hherhold</a> and others: Could you describe how do you usually manage your data and how many and how big files you store in a scene and how would an ideal user interface work?</p>
<p>For example, my use cases:</p>
<ul>
<li>Most of the of my use cases are loading one or a few image files (each is not larger than a few hundred MB) and I usually save them as MRB. While I’m working on a complex task, I often save with new file name once in an hour, so that I can go back to an earlier version if needed.</li>
<li>I mostly use the save dialog GUI in non-MRB mode for exporting individual files.</li>
<li>In applications where we need fast saving of large files, I always override save dialog to create a new folder (the same way as it is done for mrb) but don’t zip it. It duplicates all the files, so consumes significant amount of storage, but it is very fast and each folder is fully self-contained.</li>
</ul>

---

## Post #6 by @muratmaga (2020-04-22 17:39 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="11251">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Yes, it is stable. Several groups always save everything in mrb files and they don’t report any issues. However, I can imagine that you may run out of disk space while creating many-GB archives: first we need to write out the files uncompressed then compress it, so temporarily we may need several times more disk space than the final result. With many laptops today having fast but small SSDs, not everyone always has tens of GBs of free disk space.</p>
</blockquote>
</aside>
<p>In my particular cases it is certainly not issue of the lack of space on drive I will comment on the others later…</p>

---

## Post #7 by @hherhold (2020-04-22 18:21 UTC)

<p>Apologies if I’m late in joining in on the discussion of save behavior.</p>
<p>So I do not do anything complicated like overriding save dialog behavior. I typically have a large volume file (single NRRD file, 0.5GB to 3GB, depending, and my average is probably around 1.5GB) that is unchanged, and associated segmentation files with it that change often (.seg.nrrd). Disk space is not so much a concern as we allow for that right now anyway - I usually have an 8TB disk hanging around with everything I’m working on, but I copy 4 or 5 datasets to a local SSD because it’s faster.</p>
<p>I tend to save early and often. I typically spend anywhere between a day and two weeks per file on manual segmentation, depending on quality of the CT scan and what I’m looking at. Re-writing of the gigabytes-large unchanged volume file for every MRB save would be very time consuming. (I actually did this early on when I was new to Slicer and moved away from it very quickly.)</p>

---

## Post #8 by @ezgimercan (2020-04-22 20:10 UTC)

<p>I am also very interested in changing the behavior of Save dialog - especially renaming without the extension.</p>
<p>My lab usually produces landmarks or segmentations for a large number of CT images - we only save the segmentation/label map and fidicual files. My team renames the segmentation and fcsv files in the save dialog using image identifier. For us, entering that additional “.fcsv” or “.nii.gz” (".nrrd", “.nii” etc) is not ideal especially when you forget or make a typo and not realize it until you close the workspace. I ask my team members to check the folder after every save operation to make sure the file is saved with the right name.</p>
<p>I would prefer automatic addition of appropriate file extension with the file format selection. As it was in earlier versions.</p>
<p>I really like the idea of having a right-click Export action in the Data Module. In terms of GUI, it is cleaner than checking/unchecking boxes in the Save menu, when you need to save only a Markups file but have a bunch of other data in the scene.</p>

---

## Post #9 by @lassoan (2020-04-22 20:43 UTC)

<aside class="quote no-group" data-username="ezgimercan" data-post="8" data-topic="11251">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ezgimercan/48/4584_2.png" class="avatar"> ezgimercan:</div>
<blockquote>
<p>I would prefer automatic addition of appropriate file extension with the file format selection. As it was in earlier versions.</p>
</blockquote>
</aside>
<p>It is interesting. I don’t think the behavior has changed in the last 5 years.</p>
<p>Is there a reason why you don’t set the desired name as node name?</p>
<aside class="quote no-group" data-username="ezgimercan" data-post="8" data-topic="11251">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ezgimercan/48/4584_2.png" class="avatar"> ezgimercan:</div>
<blockquote>
<p>I really like the idea of having a right-click Export action in the Data Module. In terms of GUI, it is cleaner than checking/unchecking boxes in the Save menu, when you need to save only a Markups file but have a bunch of other data in the scene.</p>
</blockquote>
</aside>
<p>It is really easy to implement this and for a single node right-click to Export would definitely save 2-3 clicks, so it seems like a good idea to do this. However, if you want to save 2 or more nodes then Exporting them one-by-one using right-click and selecting output file folder and filename would be more clicks and more error-prone.</p>
<aside class="quote no-group" data-username="ezgimercan" data-post="8" data-topic="11251">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ezgimercan/48/4584_2.png" class="avatar"> ezgimercan:</div>
<blockquote>
<p>My lab usually produces landmarks or segmentations for a large number of CT images</p>
</blockquote>
</aside>
<p>You can make this fully automatic by a few lines of Python code, but if you have a particular workflow that you repeat more than 10-20 times then it is definitely worth spending a few hours (it really does not take more) with creating a custom scripted module. You can write it all in Python, edit the GUI in Qt Designer, so it is all very easy to create and optimize. The custom module can automate all the simple but tedious tasks, such as iterating through data sets in a folder, loading them, setting up the desired visualization, creating nodes with appropriate names, and offering one-click save.</p>

---

## Post #10 by @ezgimercan (2020-04-22 20:54 UTC)

<aside class="quote no-group" data-username="&quot;lassoan" data-post="9" data-topic="11251">
<div class="title">
<div class="quote-controls"></div>
 "lassoan:</div>
<blockquote>
<p>Is there a reason why you don’t set the desired name as node name?</p>
</blockquote>
</aside>
<p>No specific reason other than simplifying instructions. I have a team of doctors/students who are not very comfortable with computers and different software. I find it easier to tell them just click on Save, instead of changing modules. That way, when they close the scene and load the next scan, they are in the same module. They usually go between Volume Rendering and Markups.</p>
<aside class="quote no-group quote-modified" data-username="&quot;lassoan" data-post="9" data-topic="11251">
<div class="title">
<div class="quote-controls"></div>
 "lassoan:</div>
<blockquote>
<aside class="quote no-group" data-username="ezgimercan" data-post="8" data-topic="11251">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ezgimercan/48/4584_2.png" class="avatar"> ezgimercan:</div>
<blockquote>
<p>I really like the idea of having a right-click Export action in the Data Module. In terms of GUI, it is cleaner than checking/unchecking boxes in the Save menu, when you need to save only a Markups file but have a bunch of other data in the scene.</p>
</blockquote>
</aside>
<p>It is really easy to implement this and for a single node right-click to Export would definitely save 2-3 clicks, so it seems like a good idea to do this. However, if you want to save 2 or more nodes then Exporting them one-by-one using right-click and selecting output file folder and filename would be more clicks and more error-prone.</p>
</blockquote>
</aside>
<p>I completely agree but it could be nice to have the option.</p>
<aside class="quote no-group quote-modified" data-username="&quot;lassoan" data-post="9" data-topic="11251">
<div class="title">
<div class="quote-controls"></div>
 "lassoan:</div>
<blockquote>
<aside class="quote no-group" data-username="ezgimercan" data-post="8" data-topic="11251">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ezgimercan/48/4584_2.png" class="avatar"> ezgimercan:</div>
<blockquote>
<p>My lab usually produces landmarks or segmentations for a large number of CT images</p>
</blockquote>
</aside>
<p>You can make this fully automatic by a few lines of Python code, but if you have a particular workflow that you repeat more than 10-20 times then it is definitely worth spending a few hours (it really does not take more) with creating a custom scripted module. You can write it all in Python, edit the GUI in Qt Designer, so it is all very easy to create and optimize. The custom module can automate all the simple but tedious tasks, such as iterating through data sets in a folder, loading them, setting up the desired visualization, creating nodes with appropriate names, and offering one-click save.</p>
</blockquote>
</aside>
<p>Oh, yes. It is on my to-do list. One of these days. What I would really like to have is a mechanism for loading landmark template list with empty landmarks and go through the list to annotate each one. That’s the most common task we do in Slicer.</p>

---

## Post #11 by @lassoan (2020-04-22 21:01 UTC)

<aside class="quote no-group" data-username="ezgimercan" data-post="10" data-topic="11251">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ezgimercan/48/4584_2.png" class="avatar"> ezgimercan:</div>
<blockquote>
<p>What I would really like to have is a mechanism for loading landmark template list with empty landmarks and go through the list to annotate each one. That’s the most common task we do in Slicer.</p>
</blockquote>
</aside>
<p>We already have all the underlying infrastructure to support this, it just has not been exposed on the GUI yet. You might want to create a new topic here to discuss it, as there are others who would be interested in having this and could contribute to the implementation (for example, <a class="mention" href="/u/muratmaga">@muratmaga</a>’s team).</p>

---

## Post #12 by @jamesobutler (2020-04-22 21:34 UTC)

<p>I have to agree that requiring the user to include the extension in the “Filename” field of the Save dialog can result in errors and isn’t super user friendly.</p>
<p>As I previously mentioned in a past thread (quoted at the end of this post), it seems like a waste of time to specify the extension in the filename and then specify it again in the “File Format” column. These fields have to be matched correctly and it only validates the new field text after I’ve finished editing the file name field, so when I mess up, I have to rewrite the new file name all over again. I think most Windows users are most familiar with the native file dialog which looks like the following below which allows you to write either “MyNewFile” or “MyNewFile.txt” in the filename field and the result is a file in “some-location/MyNewFile.txt”.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61ae61289045e0b19077ec42aca440712fe1a964.png" alt="filename-ext-image" data-base62-sha1="dW7V6uou4BbpeOE9Ws5zEJ0SmIQ" width="304" height="96"></p>
<aside class="quote no-group" data-username="jamesobutler" data-post="37" data-topic="4488">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"><a href="https://discourse.slicer.org/t/how-to-unset-default-compress-option-during-save/4488/37">How to unset default 'compress' option during save</a></div>
<blockquote>
<p>Is there a reason for the redundancy of showing the extension in the file name and having it shown in the column directly to the right of it? When the file format is changed it automatically changes the extension in the file name cell, but if you change the extension in the file name it doesn’t choose the correct file format even if it is a valid file format. Reading left to right I change the file name first and then choose the file format second.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64b97b9a3705e786625cb9036eea5d5cdab581b5.png" alt="extension_duplication" data-base62-sha1="en38OseIvtjr91UjzLwuJ75FTyR" width="336" height="165"></p>
</blockquote>
</aside>

---

## Post #13 by @mbutler808 (2020-04-22 22:55 UTC)

<p>As a new user, I would have never guessed that the file extension would have to be included when the file format and extension is right there next to it. Itʻs not the expected behavior for a software interface, so I can understand why people would not notice that the save had reverted to the original filename. In fact in many software packages, you get a warning that changes have been made to the original file, do you want to replace or rename, etc.  Basically an “are you sure” message.<br>
Instead, what I would expect is that my manually entered name would be used with the extension in the file format box appended. I would expect that either I could add .mha  or if nothing was added, .mha would be added (according to what is indicated).</p>
<p>I also hope that the default file format is not changed to MRB. We work on microCT scans that are 2-4GB each, and we try to do this on laptops. We would quickly run out of space! Itʻs a challenge already but it would then add to additional file management overhead.  I would prefer that it save in the original format, assuming that people are working in the formats best suited to their workflow.</p>
<p>Thanks for all your work! Itʻs an incredible software suite.</p>
<p>Marguerite Butler</p>

---

## Post #14 by @muratmaga (2020-04-22 23:39 UTC)

<p>The topic is getting longer. I made a google doc with a suggestion of changes I deem important and useful. Should be editable to all.</p>
<aside class="onebox googledocs">
  <header class="source">
      <a href="https://docs.google.com/document/d/12yYl0gLBf4RQxQI_JhCq5QLEdrkr0w_1VzfkTcJ8C1A/edit?skip_itp2_check=true" target="_blank" rel="nofollow noopener">docs.google.com</a>
  </header>
  <article class="onebox-body">
    <a href="https://docs.google.com/document/d/12yYl0gLBf4RQxQI_JhCq5QLEdrkr0w_1VzfkTcJ8C1A/edit?skip_itp2_check=true" target="_blank" rel="nofollow noopener"><span class="googledocs-onebox-logo g-docs-logo"></span></a>

<h3><a href="https://docs.google.com/document/d/12yYl0gLBf4RQxQI_JhCq5QLEdrkr0w_1VzfkTcJ8C1A/edit?skip_itp2_check=true" target="_blank" rel="nofollow noopener">Slicer5.0 Save</a></h3>

<p>Keep the Save As Dialog behavior box more or less the same with these changes:  Move MRB Icon into its own File-&gt;Package Scene. (Right now it is mostly unclear how to disable the packaging, if you end up clicking on it. Clicking the buttons left to...</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #15 by @lassoan (2020-04-23 01:31 UTC)

<p>Thanks for all the feedback, they are very useful. I’ve compared behavior of file saving of a couple of software on Windows. The conclusion is that while there is variety in how different software work with filename extensions during saving, a “mainstream” behavior can be clearly identified and we can update Slicer to match that:</p>
<ul>
<li>Show file extension in filename in addition to showing file extension in format selector (keep current Slicer behavior)</li>
<li>If a different file extension is entered than the current one:
<ul>
<li>If the extension is supported for the data node then switch to the entered file extension (as opposed to current Slicer behavior of reverting the filename and extension)</li>
<li>If the extension is not supported for the data node then the current extension is appended to the entered filename (as opposed to current Slicer behavior of reverting the filename and extension)</li>
</ul>
</li>
</ul>
<details>
<summary>
Details</summary>
<p>Assuming selected file type is .doc and other supported file types are .txt, .doc, .pdf:.</p>
<p>File extension in displayed in save dialog (in addition to showing extension in file format listbox):</p>
<ul>
<li>Yes: Notepad, Camtasia, Snagit, Visual Studio Code, Gimp, <strong>Slicer</strong>
</li>
<li>Yes, but not everywhere: Word, Blender</li>
</ul>
<p>If a known file extension is entered but not the one that is selected in the listbox (e.g., something.txt):</p>
<ul>
<li>Entered file name is used as is (something.txt): Notepad, Camtasia, Snagit, Word, Snagit, Visual Studio Code, Gimp</li>
<li>File extension selected in the listbox is appended (something.txt.doc): Word, Blender</li>
<li>Filename is reverted to last one: <strong>Slicer</strong>
</li>
</ul>
<p>If an unknown file extension is entered (something.qqq):</p>
<ul>
<li>File extension selected in the listbox is appended (something.qqq.doc): Notepad, Word, Snagit, Visual Studio Code, Blender</li>
<li>Entered file name is used as is (something.qqq): Camtasia</li>
<li>Error popup is displayed: Gimp</li>
<li>Filename is reverted to last one: <strong>Slicer</strong>
</li>
</ul>
</details>
<p>We need to continue the discussion about:</p>
<ul>
<li>Saving in-place, saving in dedicated folder without packaging, saving in dedicated folder with packaging into single file (mrb). There seems to be a conflict of interest between power users, people who work with large data sets, and novice users.</li>
<li>Automatic synchronization of node and file names. There is no obviously correct behavior. We may need to make the behavior semi-automatic and/or more configurable.</li>
</ul>

---

## Post #16 by @lassoan (2020-04-25 22:00 UTC)

<p>FYI, <a href="https://github.com/Slicer/Slicer/pull/4890">pull request has been submitted</a> that makes file name setting consistent with other software.</p>

---
