# Superfluous suffix for reloads causes issues with save

**Topic ID**: 13216
**Date**: 2020-08-28
**URL**: https://discourse.slicer.org/t/superfluous-suffix-for-reloads-causes-issues-with-save/13216

---

## Post #1 by @muratmaga (2020-08-28 16:52 UTC)

<p>This is a minor issue, but annoys me particularly when the scene is empty (but not reset).</p>
<p>Load MRHead.nrrd, rename the node to something else, and the ]note that the second time it is loaded name becomes MRHead_1, even though there is no other MRHead. If you delete everything, and reload MRHead (without resetting the scene), you get MRHead_2</p>
<p>While mild, this behavior becomes more concerning at the save time. Contiuing from the previous step, if you go to the volumes module and check the file name it points out to a non-existent, never saved before MRHEad_2.nrrd. If you try to save this file, you got a duplication of data. This should not be the case, it should point out the file I loaded, which is MRHead.nrrd.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf250ca58657f9b8cc2c9474907419d998499fa0.jpeg" data-download-href="/uploads/short-url/tyudhZu6k0A6BZOokhUKIt6hCwg.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf250ca58657f9b8cc2c9474907419d998499fa0_2_690x498.jpeg" alt="image" data-base62-sha1="tyudhZu6k0A6BZOokhUKIt6hCwg" width="690" height="498" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf250ca58657f9b8cc2c9474907419d998499fa0_2_690x498.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf250ca58657f9b8cc2c9474907419d998499fa0_2_1035x747.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf250ca58657f9b8cc2c9474907419d998499fa0.jpeg 2x" data-dominant-color="F3F3F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1058×765 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2020-09-10 00:06 UTC)

<p>any forum opinion on this issue?</p>

---

## Post #3 by @hherhold (2020-09-10 00:25 UTC)

<p>I find the occasional number suffix “mystery increment” to be somewhere between annoying and troubling, where annoying = “I don’t like it but I can deal” and troubling is “am I going to lose data along the way?”</p>
<p>If that makes sense.</p>

---

## Post #4 by @mangotee (2020-09-10 00:54 UTC)

<p>Same here. I often code up workflows and sometimes I load same-named volumes or transforms for different subjects, where the suffix can break the workflow. I’ve gotten used to it and work around it if necessary, but it’s sth that I wouldn’t miss if it was gone.</p>

---

## Post #5 by @lassoan (2020-09-10 01:17 UTC)

<p>We are open to any suggestions. These problems seem simple, but actually it is really hard to come up with good solutions.</p>
<p>There are a couple of somewhat independent questions/issues.</p>
<ol>
<li>Node name suffices are always incremented until the scene is closed</li>
</ol>
<p>Current behavior: If you load nodes from the same filename then numerical suffices are added to guarantee unique name in the session. Higher suffix always mean that the node was loaded later. Counters are reset when the scene is closed.</p>
<p>What behavior would you prefer instead?</p>
<p>Option A. We could reuse old node names every time. For example, if you have CT, CT_1 CT_3, CT_4 and load a file CT then the node could be named as CT_2. I don’t think it would be any better than CT_5. Actually, CT_5 name would more clearly reflect that this image was loaded later. Not reusing names immediately is also safer, because there is a lower change that the file already exists.</p>
<p>Option B. We could check if there is any node by a similar name (<em>nodename</em>_<em>someinteger</em>) and if none found then restart the counter. This would not be as risky as Option A, but this kind of complex heuristics could be quite hard for users to understand. For example, how long it would take for a user to figure out that if you have still have “CT_3” node in your scene (after loading “CT” file 8 times, but deleting all of them except one) then your “CT” file is named “CT_8”; but if you removed “CT_3” node and then then load “CT” file then it is named simply as “CT”?</p>
<p>Any other options?</p>
<ol start="2">
<li>Output file name is automatically updated to match node name</li>
</ol>
<p>This mechanism was implemented because lots of users complained and they mixed up and/or lost data because fixing node names in the scene did not fix file names. You can easily imagine how bad it is if you rename your nodes in the scene but file names still remain the same.</p>
<p>The solution to this issue was to update filename automatically from node name, which created unwanted, but less sever side effects than the original problem. For example, users that realized that they didn’t like the file name changed it in the save dialog but next time they saved the scene it got reverted to the node name.</p>
<p>Any suggestions are welcome for softening this side effect (without introducing other issues).</p>
<ol start="3">
<li>Scene saving and export is not separated clearly enough</li>
</ol>
<p>Saving: save everything in the scene so that the current state can be restored without any change or loss of information.</p>
<p>Exporting: save a few nodes to a certain folder in some chosen file format, potentially in a lossy format.</p>
<p>Currently, the save dialog serves both purpose. Saving in mrb format saves the scene, but it is slow and takes lots of space for large data sets. Saving to individual files can be messy due to automatic filename changes (see issue 2), choice of various file formats, folders.</p>
<p>Suggestions are welcome how to make things simple things simple to do, but still allow to do complex things.</p>
<ol start="4">
<li>If multiple nodes have the same name then it is hard to know which one is which</li>
</ol>
<p>Before we had subject hierarchy, we could only rely on a node’s name to identify it. At many places we still use a simple node name combo box for selecting inputs/outputs.</p>
<p>The automatic node suffix mechanism reduces the chance of having many nodes with the same name, but it is still possible.</p>
<p>A potential solution instead or in addition to automatix suffices could be to change the node selector to always show a subject hierarchy tree. Then node names could be the same and they could be distinguished by their parent folder. There could be name clashes when the scene is saved (unless subject hierarchy folder name is used as subfolder name by default).</p>
<hr>
<p>Maybe instead of brainstorming about all kinds of possible solutions, we could converge to meaningful improvements faster if you could describe your typical workflows: what data sets you load, how you process them, what do you want to export/save. We could then focus on finding solutions that make all the described workflows as effortless to do as possible.</p>

---

## Post #6 by @muratmaga (2020-09-10 03:10 UTC)

<p>I understand the necessity, and I don’t want to alter things drastically. I think it makes complete sense when you keep reloading the same volume (without removing the first iteration from the scene) subsequent ones get the suffix.</p>
<p>For the particular case I present (i.e., a node is loaded, then deleted, and reloaded) would it be possible the not to add the suffix? Can there be a logical check for this case? This is only behavior I would like to see changed.</p>

---

## Post #7 by @hherhold (2020-09-10 12:54 UTC)

<p>Agreed with Murat on this one.</p>
<p>And I totally get Andras’ point that these simple problems often have very complex solutions. Minimal impact on current implementation is important, and I also feel much better that the current implementation seeks to be as conservative as possible (i.e., far better to have multiples of something than to delete something that the user really didn’t want deleted).</p>
<p>My biggest with node number suffix increases has been with the proliferation of camera nodes, but this is much more of an annoyance than an issue. It’s easy enough to cycle through them to find the one you’re looking for.</p>

---

## Post #8 by @lassoan (2020-09-10 12:56 UTC)

<p>Proliferation of camera nodes is an independent bug. Could you file a bug report at <a href="http://issues.slicer.org">issues.slicer.org</a>?</p>

---

## Post #9 by @hherhold (2020-09-10 13:05 UTC)

<p>Oh! Sure.</p>
<p>Wasn’t sure if it fell under the same umbrella as the suffix issue.</p>

---
