# Clipping volume

**Topic ID**: 23925
**Date**: 2022-06-18
**URL**: https://discourse.slicer.org/t/clipping-volume/23925

---

## Post #1 by @mohammed_alshakhas (2022-06-18 11:39 UTC)

<p>i wish to have a scissor/eraser tool for volume.</p>
<p>that will allow free hand clipping of volume.</p>
<p>I’m aware of other methods like splitting volume but those are more involved.</p>
<p>i rather have a simple scissor / eraser of volume</p>

---

## Post #2 by @lassoan (2022-06-18 13:52 UTC)

<p>This feature is available in Segment Editor in two steps: use <code>Scissors</code> effect to specify a region to remove and then use <code>Mask volume</code> effect to blank out that part of the volume.</p>

---

## Post #3 by @mohammed_alshakhas (2022-06-19 11:41 UTC)

<p>eraser would be a fantastic addition, scissor is not applicable in all situations where surrounding structures nearby.</p>
<p>I used this with many viewers and I love it</p>

---

## Post #4 by @pieper (2022-06-19 13:28 UTC)

<p>You can already erase with the paint or draw effects on the slices, and you can already use the scissors tool to erase in 3D.  Practice a bit with the Mask Volume effect - it’s very powerful for this operation.  If you have a specific tool in another software package that you think has useful features please point to it.</p>

---

## Post #5 by @mohammed_alshakhas (2022-06-20 12:56 UTC)

<p>other viewers have a 3d volume eraser, without the need to segment a part and then mask it.</p>
<p>masking is very useful when I want to create a new volume for a specific part, but for me as a user id rather be able to delete/erase part of the volume directly.</p>
<p>another disadvantage with masking is that some volumes are noisy, like if I have a CBCT and I was to remove some of the artifacts. then creating a mask for that part is not easy and time-consuming</p>

---

## Post #6 by @lassoan (2022-06-21 05:24 UTC)

<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="5" data-topic="23925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>for me as a user id rather be able to delete/erase part of the volume directly</p>
</blockquote>
</aside>
<p>Indeed, it takes about 6 extra clicks to set up masking:</p>
<ol>
<li>Go to Segment Editor</li>
<li>Click Scissors effect</li>
<li>Click “Fill inside” mode</li>
<li>Draw in the view</li>
<li>Click Mask volume effect</li>
<li>Click Apply</li>
</ol>
<p>After this, it just requires 3 clicks to update after drawing with scissors:</p>
<ol>
<li>Hit space key to switch to Mask volume</li>
<li>Click Apply</li>
<li>Hit space key to switch back to Scissors</li>
</ol>
<p>For an experienced Slicer user these take about 10 seconds extra one-time setup time and 2 seconds extra for each additional cut, which should be tolerable.</p>
<p>For new users I agree that this can be hard to figure this out. They don’t even realize that the feature exist and cannot easily discover that it just takes a few clicks. So, why don’t we make it simpler?</p>
<p>Anyone could add a a small scripted module that would automate those 6+3 clicks. However, newcomers would still need to discover that module and switch to that module, select input volume, activate the scissor, etc. so overall this would be not be a game changer for most use cases.</p>
<p>To achieve more substantial improvements, we usually need to go beyond the immediate request and look at the final user need. Often the user does not really need a manual clipping tool but wants to solve a more complex task and there may be better solutions for that.</p>
<ul>
<li>For example, if the user wants to use volume clipping to remove the patient table then instead of improving usability of a manual clipping tool, it can be much better to use a single-click solution, such as the <a href="https://github.com/PerkLab/SlicerSandbox#remove-ct-table">Remove CT table module</a> (in Sandbox extension).</li>
<li>If users really need manual volume clipping then usually it is just one step of a longer workflow. Then much more automation and user convenience can be achieved by implementing a scripted module that guides the user through the <em>entire</em> workflow, which eliminates the need to switch between modules and set inputs/outputs of modules - not just for the volume clipping but for all workflow steps.</li>
</ul>
<p>So, we don’t have a simpler, dedicated manual volume clipping tool because advanced users do not really need it, and most new users and clinical users need something better, so it has not been a high priority.</p>
<p>If this is high priority for you then you can implement that small Python scripted module that automates those 6+3 clicks. We would be happy to help you getting started. You can even bring it as a project to the <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/">upcoming Slicer Project Week</a>, starting next Monday.</p>
<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="5" data-topic="23925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>another disadvantage with masking is that some volumes are noisy, like if I have a CBCT and I was to remove some of the artifacts. then creating a mask for that part is not easy and time-consuming</p>
</blockquote>
</aside>
<p>Image noise should not be a concern if you use “Fill inside” mode, but if you run into issues then describe in a bit more detail what causes the issue.</p>

---

## Post #7 by @mohammed_alshakhas (2022-06-24 19:20 UTC)

<p>thank you for the thorough response,</p>
<p>I was not aware of the " removing CT table effect",I have to try it soon.</p>
<p>creating a mask with scissors is tricky and would be too much when the part you want to erase has multiple contacts think of ( teeth, neck collar, face mask, etc). you just end up including too much of what you want to keep.</p>
<p>a 3d sphere eraser that I can alter in size would be sufficient for most medical users like me. and it is already there in softwares like Romexis and Nemofab.</p>
<p>the advantage of 3d  editing/ erasing the volume is incredible for complex cases. it is already the with the scissor, <em>I just wish to have a sphere eraser in addition to the scissor</em>. exactly like the eraser effect in segmentation being possible to use it in 3D.</p>
<p>the issue with noisy volumes is that it is quite challenging to distinguish the artifacts in individual slices  ( the beginning of the artifact and the true image ), on contrary, erasing those artifacts in 3D is much simpler.  at least you can do most of the work in 3d then shift to individual slices for fine-tuning.</p>

---

## Post #8 by @lassoan (2022-06-24 20:03 UTC)

<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="7" data-topic="23925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p><em>I just wish to have a sphere eraser in addition to the scissor</em>. exactly like the eraser effect in segmentation being possible to use it in 3D.</p>
</blockquote>
</aside>
<p>This is already available, just check the “Edit in 3D views” checkbox in the Paint or Erase effect. You can adjust the size using Shift+MouseWheel.</p>
<p>But that’s not all. You can also do local smoothing in 3D, which can also removes small bridges and noise.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="rjNcvefBaNU" data-video-title="Segmentation smoothing brush - new segmentation tool in 3D Slicer" data-video-start-time="27" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=rjNcvefBaNU&amp;t=27" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/rjNcvefBaNU/maxresdefault.jpg" title="Segmentation smoothing brush - new segmentation tool in 3D Slicer" width="" height="">
  </a>
</div>


---

## Post #9 by @mohammed_alshakhas (2022-06-24 20:51 UTC)

<p>I meant for volume clipping , not for segmentation.</p>

---

## Post #10 by @lassoan (2022-06-25 04:37 UTC)

<p>Editing the segmentation is the same as blanking clipping the volume (you just need to set it up with a few clicks; and then do two clicks to make the segmentation clip the volume). If the couple of clicks to set up the clipping by segmentation and the two clicks after segments are modified is a problem then you can automate them using Python scripting, but it is only worth the time if you need to clip hundreds of cases.</p>

---

## Post #11 by @mohammed_alshakhas (2022-06-25 08:30 UTC)

<p>I’m totally aware about the how of clipping volume based on segmentation or masks . And actually, that’s my work flow .</p>
<p>Believe  me it is quite  time consuming and not  always easy for reasons I mentioned before .</p>
<p>I’m not sure I’m getting my idea through ,  it’s just a spherical volume eraser .</p>
<p>I’m aware about others ways to do it , but they all time consuming and difficult to apply in many situation for my cases .</p>
<p>And yes , I’m using volume clipping for almost all my cases nowadays since I need to look at some structure isolated</p>
<p>And I can’t script <img src="https://emoji.discourse-cdn.com/twitter/face_holding_back_tears.png?v=12" title=":face_holding_back_tears:" class="emoji" alt=":face_holding_back_tears:" loading="lazy" width="20" height="20"> at all</p>

---

## Post #12 by @mohammed_alshakhas (2022-06-25 10:07 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p>this video illustrate the idea I’m talking about</p>
<p>          <iframe width="640" height="360" src="https://player.vimeo.com/video/392156458?h=930ed7f095&amp;app_id=122963" data-original-href="https://vimeo.com/392156458" frameborder="0" allowfullscreen="" seamless="seamless" sandbox="allow-same-origin allow-scripts allow-forms allow-popups allow-popups-to-escape-sandbox allow-presentation"></iframe>
</p>

---

## Post #13 by @pieper (2022-06-25 12:33 UTC)

<p>Thank you for taking the time to explain <a class="mention" href="/u/mohammed_alshakhas">@mohammed_alshakhas</a>.  Yes, there are more clicks involved in Slicer to accomplish that.  I agree with <a class="mention" href="/u/lassoan">@lassoan</a> that something very similar to the video could be accomplished with some programming.  Maybe you can enlist someone to help you implement a custom module for your workflow.</p>

---
