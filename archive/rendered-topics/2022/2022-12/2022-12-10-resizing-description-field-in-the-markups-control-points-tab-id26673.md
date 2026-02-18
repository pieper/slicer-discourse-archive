# Resizing description field in the markups control points table

**Topic ID**: 26673
**Date**: 2022-12-10
**URL**: https://discourse.slicer.org/t/resizing-description-field-in-the-markups-control-points-table/26673

---

## Post #1 by @muratmaga (2022-12-10 07:35 UTC)

<p>I cannot seem to adjust the width of the description field. Name field can be modified but not the description.<br>
I would be good to bring back the old behavior<br>
This is on windows 11 with 5.2.1</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52cd3d1c3cbe503116fe76aebf776a93fd741641.png" alt="image" data-base62-sha1="bOuSdxlw4mnnMR14qLOUcB79Cpj" width="674" height="226"></p>

---

## Post #2 by @muratmaga (2022-12-10 07:38 UTC)

<p>Actually I take it back. It is modifiable. But I have to grab from the right side, which wasn’t intuitive. Is there reason why the left one cannot be moved (as I hover over, cursor icon doesn’t change to indicate that width can be changed</p>

---

## Post #3 by @lassoan (2022-12-10 15:25 UTC)

<p>In all software that I know of, you can adjust column width in a spreadsheet by drag-and-dropping the right side of the column. We cannot and should not change this.</p>
<p>I can see that there is a certain <em>description</em> column width range when the column sizes may change unexpectedly, but this is just due to that the <em>name</em> column is set to use all the available space and if you make <em>description</em> column narrower then it makes the <em>name</em> column wider.</p>
<p>We could turn off automatic expansion of <em>description</em> column, but then the table columns would not automatically use all available space.</p>
<p>The main issue that I see is that making <em>description</em> column very wide compresses the name column. I don’t know what a good solution for this would be. Resizing a column based on content would be extremely slow on large tables. Adding a button for “fit to contents” would further complicate the GUI.</p>

---

## Post #4 by @muratmaga (2022-12-10 19:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="26673">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>In all software that I know of, you can adjust column width in a spreadsheet by drag-and-dropping the right side of the column. We cannot and should not change this.</p>
</blockquote>
</aside>
<p>I am not sure I described it correctly. The highlighted section is not movable. According to your description is the right correct place to resize the name column. The width of the name column can be adjust only by grabbing the handle on its left side (in other words the right hand of the visibility column). It just creates a weird dynamic. Try you will see…</p>

---

## Post #5 by @lassoan (2022-12-10 19:51 UTC)

<p>Could you capture a video of your screen?</p>

---

## Post #6 by @muratmaga (2022-12-10 20:21 UTC)

<p>I never properly managed to use OSB, so apologies for the crappy video. But it shows the awkward adjustment behavior.<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b087ef7e56bdd5cab2813afc1c1b85826ddbd2cf.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b087ef7e56bdd5cab2813afc1c1b85826ddbd2cf.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b087ef7e56bdd5cab2813afc1c1b85826ddbd2cf.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #7 by @lassoan (2022-12-10 21:08 UTC)

<p>The ability to adjust the visibility column is a bug (easy to fix). Otherwise everything works normally. As I described above, the name column is configured to use up all unused space (and if you take space away then it is taken away from the name column). I agree that the end result can be somewhat unexpected (especially when you take away space from the name column), but it is all correct, consistent behavior, and I don’t see how we could change it without impacting appearance (having a blank space if columns don’t use all available space is ugly), performance (automatic fitting of size to content is extremely slow and does not solve all problems), usability (adding one more button to fit name column width to content would make the GUI even more cluttered). Often the issue is sidestepped by making the last column claim the remaining space, but we have the status column in the rightmost position and we also have two wide columns (name and description), so we cannot follow this pattern.</p>

---

## Post #8 by @muratmaga (2022-12-10 22:17 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="26673">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Otherwise everything works normally</p>
</blockquote>
</aside>
<p>I respectfully disagree. Treating the total length of the name + description field is a fixed width and them adjusting their proportions is an awkward behavior, is completely different than what I am used to seeing before (in Markups) as well as any table oriented program like a spreadsheet. For me, for the behavior to be “normal”, name and description fields needs to be adjusted independently of each other as the user chooses. As a users that’s what I would expect when there is a visual vertical divider separating these columns.</p>

---

## Post #9 by @lassoan (2022-12-11 04:51 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="8" data-topic="26673">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Treating the total length of the name + description field is a fixed width and them adjusting their proportions</p>
</blockquote>
</aside>
<p>The sizing rule is much simpler: the name columns takes up any unused space. Apparently, it is hard to figure this rule by using the system (even when explained), so probably it should be changed. However, I don’t see any simple solution, because the space is narrow, there are <em>two</em> potentially wide fields, and we always want to make the status column visible on the right.</p>
<p>You can experiment with the various options yourself:</p>
<pre data-code-wrap="python"><code class="lang-python">tableWidget = findChild(None,name="activeMarkupTableWidget")
columnIndex = 3  # name column
sizeMode = qt.QHeaderView.Interactive  # see options at https://doc.qt.io/qt-5/qheaderview.html#ResizeMode-enum
tableWidget.horizontalHeader().setSectionResizeMode(columnIndex, sizeMode)
</code></pre>
<p>Disabling stretching of name column makes sizing behavior easier to understand for users, but makes the status column disappear, as there is no column that would absorb various column width changes.</p>

---

## Post #10 by @muratmaga (2022-12-11 05:10 UTC)

<p>If the goal is to maximize space for name column, wouldn’t be easier to implement an option to hide the description field like RAS fields? So people who need to have long markup names can hide description and . maximize the width for name column?</p>

---

## Post #11 by @lassoan (2022-12-11 05:17 UTC)

<p>You can already hide coordinates column (Coordinates → Hide), but it does not make a difference (space is still constrained).</p>
<p>Please experiment with column sizing options and see if you can find any combination that looks good to you.</p>
<p>For example, try this:</p>
<pre><code class="lang-python">tableWidget = findChild(None,name="activeMarkupTableWidget")
tableWidget.horizontalHeader().setSectionResizeMode(3, qt.QHeaderView.Interactive)
tableWidget.horizontalHeader().setSectionResizeMode(4, qt.QHeaderView.Stretch)
</code></pre>

---

## Post #12 by @jamesobutler (2022-12-11 16:11 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="8" data-topic="26673">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>as well as any table oriented program like a spreadsheet.</p>
</blockquote>
</aside>
<p>For it to be like excel you would have an infinite number of columns and the width of the table would be infinitely sized. For filled columns to have any size width would mean likely supporting a horizontal scroll bar so not to increase the size of the widget container such as the module panel area.</p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="26673">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The sizing rule is much simpler: the name columns takes up any unused space.</p>
</blockquote>
</aside>
<p>The name column being given the unused space seems to be tied to the assumption that name will support longer text entries than the description field. The description is not pre-filled like the name field so by default it always has less text at 0 characters, but when description is actually used I think it would easily be longer than a given name. In my group’s work we have an instance of a cell defining Animal ID (like name) and then a button next to it to bring up a widget for all the extra details including a description/comment field which is a plain text field that can have the infinite space. This widget is ultimately closed but tied and saved with the data.</p>
<p>Based on <a class="mention" href="/u/muratmaga">@muratmaga</a>’s usage in the original post, it doesn’t look like he’s using the name field as a real meaningful name. One of the names is “mca” which is actually an abbreviation of a name. My guess is the content in the “description” field is closer to a meaningful name, but it is not put in the “name” field because showing the name in the 3D slice views would clutter the visibility. However it would help if there was a way to abbreviate the name in the viewers or some other method to resolve the issue of meaningful names that are long but are not actually a full description of the name.</p>

---

## Post #13 by @muratmaga (2022-12-11 18:53 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="12" data-topic="26673">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Based on <a class="mention" href="/u/muratmaga">@muratmaga</a>’s usage in the original post, it doesn’t look like he’s using the name field as a real meaningful name.</p>
</blockquote>
</aside>
<p>I am also not sure what <strong>“name”</strong> implies in this context. I always interpreted that field to be a <strong>“label”</strong>, as its contents is what’s shown in viewers. A label can be a fully qualified name, or an abbreviation, or databaseID. So perhaps <strong>name</strong> is not really the right term to use. Regardless, description is usually a lot more verbose than what name field can convey. Here is a typical craniometric landmak names and their description, as an example.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/740b2d4a076797bcd8498cc09c8317b12bd6e83c.png" data-download-href="/uploads/short-url/gyzkE1AmaVja5HGnUsKJPVbnxHS.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/740b2d4a076797bcd8498cc09c8317b12bd6e83c.png" alt="image" data-base62-sha1="gyzkE1AmaVja5HGnUsKJPVbnxHS" width="577" height="499" data-dominant-color="EEEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1353×1171 64.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I may not want to use a label like Opistocranion because of its length and possibility of occluding things around it in 3D. Also a landmark/point may not have a name, but simply an anatomical description (e.g., the anteriormost point on the nasal bone in the dorsal view). So it is very common practice to have a few letter (3-5) abbreviations, if not simply using numbers…</p>
<p>going back to the original post:</p>
<p>This is what I see when I load my landmark template.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef1c877762934f2c0ac52e1c2995177174cb09e3.png" data-download-href="/uploads/short-url/y7heOiJuFvwdSTf5mlg7v8pzKPp.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef1c877762934f2c0ac52e1c2995177174cb09e3_2_689x395.png" alt="image" data-base62-sha1="y7heOiJuFvwdSTf5mlg7v8pzKPp" width="689" height="395" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef1c877762934f2c0ac52e1c2995177174cb09e3_2_689x395.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef1c877762934f2c0ac52e1c2995177174cb09e3_2_1033x592.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef1c877762934f2c0ac52e1c2995177174cb09e3.png 2x" data-dominant-color="EAEAF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1181×677 60.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is what happens when I choose to hide coordinates<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/255d005bca8e7c07750a608f75844e9d7c7eeb67.png" data-download-href="/uploads/short-url/5kwV6hluEpzqGtZKf0ntTwImesn.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/255d005bca8e7c07750a608f75844e9d7c7eeb67_2_690x332.png" alt="image" data-base62-sha1="5kwV6hluEpzqGtZKf0ntTwImesn" width="690" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/255d005bca8e7c07750a608f75844e9d7c7eeb67_2_690x332.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/255d005bca8e7c07750a608f75844e9d7c7eeb67_2_1035x498.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/255d005bca8e7c07750a608f75844e9d7c7eeb67.png 2x" data-dominant-color="E9E9F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1154×556 44.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As a user my expectation at this point is to use the divider at the right hand side of the Name column to adjust the spacing, which i don’t think anyone can argue that is a unreasonable expectation. And I can’t do it. Because it is not grabbable (if that’s a word).</p>
<p>I can eventually get it to look like what I expect by dragging the right hand divider of Description field to the <strong>right</strong>. That’s a completely weird and unexpected behavior that I never saw in any program before. This is what I am trying to get fixed.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d4d9f68e7e847017e63350475bee52035c638c2.png" data-download-href="/uploads/short-url/8KjqKTf5JvoJu8Wtiqj0M38YIIG.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d4d9f68e7e847017e63350475bee52035c638c2_2_690x330.png" alt="image" data-base62-sha1="8KjqKTf5JvoJu8Wtiqj0M38YIIG" width="690" height="330" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d4d9f68e7e847017e63350475bee52035c638c2_2_690x330.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d4d9f68e7e847017e63350475bee52035c638c2_2_1035x495.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d4d9f68e7e847017e63350475bee52035c638c2.png 2x" data-dominant-color="E5E5ED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1178×564 50.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I understand the concerns about the space, and I don’t want to make an already very busy with more scrollbars etc. So here are my suggestions:</p>
<ol>
<li>Leave everything as is, but implement the Name/Description divider to be adjustable. (this what I would prefer)</li>
<li>I am not sure what the original justification was to maximize viewable space of Name field at the expense of Descrption. if the assumption is that description is not often use, whereas Name is always used, then I would suggest implementing on option to hide it (right click on the column name and choose hide) to maximize. That behavior can be applied to R/A/S fields as well (as opposed to hiding it from coordinates dropdown).</li>
</ol>

---

## Post #14 by @lassoan (2022-12-11 21:36 UTC)

<p>I would not like to defend our even discuss the current behavior, because a simple operation such as resizing a column must be obvious and should not raise any questions.</p>
<p>Let’s move on and try to find a behavior that is obvious for everyone.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Have you tried the code snippet that I provided above? It configures the behavior that you expect but have other issues (unused space looks ugly and status column may be not be visible without scrolling). Maybe you can tune the behavior that it makes sense for you but does not have these other problems.</p>

---

## Post #15 by @muratmaga (2022-12-11 23:29 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="26673">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Have you tried the code snippet that I provided above?</p>
</blockquote>
</aside>
<p>Sorry, i didn’t see your response. I am away now, but i will try later tonight.</p>

---

## Post #16 by @jamesobutler (2022-12-12 00:50 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="13" data-topic="26673">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I may not want to use a label like Opistocranion because of its length and possibility of occluding things around it in 3D.</p>
</blockquote>
</aside>
<p>If the length results in it occluding the 3D view, I was suggesting that maybe this is the problem that can be addressed for this workflow. A good name should be used.</p>
<p>If there are times that there is no such name and only a description, then leaving name completely empty and hiding the name column would seem valid. It would be a list of descriptions where each description has no name, otherwise there would be a general accepted name for its meaning recognized around the world.</p>

---

## Post #17 by @muratmaga (2022-12-12 02:36 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="26673">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Have you tried the code snippet that I provided above?</p>
</blockquote>
</aside>
<p>In a new Slicer session, this is what I get without the snippet (I hid R/A/S)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e0f22a1d0271343e6f4488dae33b97b2d99757d.png" data-download-href="/uploads/short-url/20n6VFHVpgCnHqv3AvjvxDZZsdv.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e0f22a1d0271343e6f4488dae33b97b2d99757d_2_689x333.png" alt="image" data-base62-sha1="20n6VFHVpgCnHqv3AvjvxDZZsdv" width="689" height="333" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e0f22a1d0271343e6f4488dae33b97b2d99757d_2_689x333.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e0f22a1d0271343e6f4488dae33b97b2d99757d_2_1033x499.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e0f22a1d0271343e6f4488dae33b97b2d99757d.png 2x" data-dominant-color="E9E9F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1148×555 43.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>With the snippet, I can now slide the Description column towards name to benefit from extra space. This is the behavior I want to see implemented.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/038200e0927952abbbd9dc37d19eddf18a873fa2.png" data-download-href="/uploads/short-url/v1XJzvY7GVHVq8mqOrledvcZfs.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/038200e0927952abbbd9dc37d19eddf18a873fa2_2_690x328.png" alt="image" data-base62-sha1="v1XJzvY7GVHVq8mqOrledvcZfs" width="690" height="328" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/038200e0927952abbbd9dc37d19eddf18a873fa2_2_690x328.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/038200e0927952abbbd9dc37d19eddf18a873fa2_2_1035x492.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/038200e0927952abbbd9dc37d19eddf18a873fa2.png 2x" data-dominant-color="E3E3E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1157×551 52.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Re-enabling the R/A/S fields slightly alter the space arrangement, but can easily be modified by rearranging the column width. I did not notice any strange or invisible columns.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0f37581fac9c12f738b601af19d62ac5c1b9393.png" data-download-href="/uploads/short-url/tOsVbEx1sRKYMjKpRJgadPldz11.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0f37581fac9c12f738b601af19d62ac5c1b9393_2_690x340.png" alt="image" data-base62-sha1="tOsVbEx1sRKYMjKpRJgadPldz11" width="690" height="340" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0f37581fac9c12f738b601af19d62ac5c1b9393_2_690x340.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0f37581fac9c12f738b601af19d62ac5c1b9393_2_1035x510.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0f37581fac9c12f738b601af19d62ac5c1b9393.png 2x" data-dominant-color="E7E7EE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1138×561 48.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, I did notice that the divider between Description and R columns exhibit the same symptom (not grabbable). So I still would have expected that it should be movable.</p>
<p>On a different note, the information that pops up when the user hovers over the table is somewhat useless (or rather very limited use to an early user ). It’s exactly the same information for every row. instead, for overflowing text  like these (indicated by …) it might be more meaningful to display the full text of the description field (if the user’s mouse is on description column) or the name (if they are on the name column).</p>
<p>Finally, if you are going to implement hide/unhide columns (in general not just for R/A/S), the right click context menu of the table would be more natural place than the coordinates dropbox.</p>

---

## Post #18 by @lassoan (2022-12-12 06:31 UTC)

<p>Let’s go back and keep experimenting with the column sizing options using the code snippet.</p>
<p>If you don’t want to make the description column take up all the unused space (but manually=interactively adjust its size), you can do this:</p>
<pre><code class="lang-python">tableWidget = findChild(None,name="activeMarkupTableWidget")
tableWidget.horizontalHeader().setSectionResizeMode(3, qt.QHeaderView.Interactive)
tableWidget.horizontalHeader().setSectionResizeMode(4, qt.QHeaderView.Interactive)
</code></pre>
<p>This makes the column sizing behavior simpler, but also much worse, as the status column immediately becomes visible (you need to scroll to make it visible) when you make either name or description column wider. When description column is set to be <code>Stretch</code> (take up unused space) then you only lost the status column when you made the name column very wide.</p>
<p>Overall, I think disabling manual sizing of the description column is a very small price to pay and if it is the last variable-size column then it does not surprise users. If we make R, A, S columns interactively resizable then users again may be surprised to see the description column losing width when R, A, S columns are widened.</p>
<p>Please check these sizing modes to see if it fulfills all your needs and feels intuitive. You can try if setting R, A, S columns to <code>Fixed</code> improves things (but then of course we may need to accept truncation of coordinate values).</p>
<pre><code class="lang-python">tableWidget = findChild(None,name="activeMarkupTableWidget")
tableWidget.horizontalHeader().setSectionResizeMode(0, qt.QHeaderView.Fixed)  # selected
tableWidget.horizontalHeader().setSectionResizeMode(1, qt.QHeaderView.Fixed)  # locked
tableWidget.horizontalHeader().setSectionResizeMode(2, qt.QHeaderView.Fixed)  # visible
tableWidget.horizontalHeader().setSectionResizeMode(3, qt.QHeaderView.Interactive)  # name
tableWidget.horizontalHeader().setSectionResizeMode(4, qt.QHeaderView.Stretch)  # description
tableWidget.horizontalHeader().setSectionResizeMode(5, qt.QHeaderView.Interactive)  # R
tableWidget.horizontalHeader().setSectionResizeMode(6, qt.QHeaderView.Interactive)  # A
tableWidget.horizontalHeader().setSectionResizeMode(7, qt.QHeaderView.Interactive)  # S
tableWidget.horizontalHeader().setSectionResizeMode(8, qt.QHeaderView.Fixed)  # status
</code></pre>
<p>Moving the status column before the variable-sized columns (right before name column?) might help, too, as it is not a big issue if description or coordinate value columns gets hidden (require scrolling to become fully visible). Unfortunately, there is no way to change the column order using Python scripting, so you cannot try it easily.</p>

---

## Post #19 by @muratmaga (2022-12-12 17:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="18" data-topic="26673">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you don’t want to make the description column take up all the unused space (but manually=interactively adjust its size), you can do this:</p>
</blockquote>
</aside>
<p>I still like the first snippet behavior above. These options here either change the overall width of the table (I end up with blank space on right hand side of status columns, or columns go beyond displayed are), or create very awkward behaviors (like multiple column widths changing at simultaeously to adjust proportions).</p>
<p>I think word table behavior is what I am expecting for name/description columns. Everything else can be fixed width as far as I am concerned. So it will be this:</p>
<pre><code class="lang-auto">
tableWidget = findChild(None,name="activeMarkupTableWidget")
tableWidget.horizontalHeader().setSectionResizeMode(0, qt.QHeaderView.Fixed)  # selected
tableWidget.horizontalHeader().setSectionResizeMode(1, qt.QHeaderView.Fixed)  # locked
tableWidget.horizontalHeader().setSectionResizeMode(2, qt.QHeaderView.Fixed)  # visible
tableWidget.horizontalHeader().setSectionResizeMode(3, qt.QHeaderView.Interactive)  # name
tableWidget.horizontalHeader().setSectionResizeMode(4, qt.QHeaderView.Stretch)  # description
tableWidget.horizontalHeader().setSectionResizeMode(5, qt.QHeaderView.Fixed)  # R
tableWidget.horizontalHeader().setSectionResizeMode(6, qt.QHeaderView.Fixed)  # A
tableWidget.horizontalHeader().setSectionResizeMode(7, qt.QHeaderView.Fixed)  # S
tableWidget.horizontalHeader().setSectionResizeMode(8, qt.QHeaderView.Fixed)  # status
</code></pre>
<p>What I don’t understand and don’t like that QT allows being able to accidentally push things beyond visible area, even with this settings. Can that be fixed? I.e the rightmost column never moves out of sight and the whole width of the table is fixed (to the size of the module panel)</p>

---

## Post #20 by @lassoan (2022-12-12 18:26 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="19" data-topic="26673">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>What I don’t understand and don’t like that QT allows being able to accidentally push things beyond visible area, even with this settings.</p>
</blockquote>
</aside>
<p>There are conflicting requirements (we want to allow users to resize columns, some columns to take up space, but also make sure columns can show some information without truncation, etc.). Qt has tons of sizing policies at many levels to resolve these conflicts, but in the end it is not possible to make every automatic conflict resolution work that fulfills everybody’s needs.</p>
<p>We can always implement custom mechanisms (e.g., inject additional constraints or make automatic adjustments when a user finished some manual adjustment) but these take a lot of time to develop and maintain and usually leads to bugs in some environments and unusual, unexpected behavior.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="19" data-topic="26673">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Everything else can be fixed width as far as I am concerned</p>
</blockquote>
</aside>
<p>Maybe you are not concerned about the coordinates display right now, but you may need to be able to see accurate coordinate values (5-6 digits) when you work on something else in the future and then you would be bothered by the fixed RAS column widths.</p>
<p>Maybe moving the position status column to the left side and freeze the first few columns (selected, locked, visible, position status) would help?</p>
<p>We need to make the control point list widget reusable (now it is hardwired into the Markups module widget) for many reasons. If we do that then the widget could be shown in the view layout (similarly to the table view) with much more space. That could also help with reducing the irresolvable size constraints.</p>

---

## Post #21 by @muratmaga (2022-12-12 18:32 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="20" data-topic="26673">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Maybe you are not concerned about the coordinates display right now, but you may need to be able to see accurate coordinate values (5-6 digits) when you work on something else in the future and then you would be bothered by the fixed RAS column widths.</p>
</blockquote>
</aside>
<p>True. I guess there is no auto-resize without user modifying it? (Like expand to fit the coordinates automatically).</p>
<aside class="quote no-group" data-username="lassoan" data-post="20" data-topic="26673">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Maybe moving the position status column to the left side and freeze the first few columns (selected, locked, visible, position status) would help?</p>
</blockquote>
</aside>
<p>Makes sense. There is no reason for them to be adjustable.</p>
<aside class="quote no-group" data-username="lassoan" data-post="20" data-topic="26673">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We need to make the control point list widget reusable (now it is hardwired into the Markups module widget) for many reasons. If we do that then the widget could be shown in the view layout (similarly to the table view) with much more space. That could also help with reducing the irresolvable size constraints.</p>
</blockquote>
</aside>
<p>I like that idea.</p>

---
