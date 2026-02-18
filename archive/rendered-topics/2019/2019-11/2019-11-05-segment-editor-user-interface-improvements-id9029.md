# Segment Editor User Interface Improvements

**Topic ID**: 9029
**Date**: 2019-11-05
**URL**: https://discourse.slicer.org/t/segment-editor-user-interface-improvements/9029

---

## Post #1 by @Umesh_Persad (2019-11-05 14:14 UTC)

<p>I’ve been using 3DSlicer to segment and create 3d printable models mostly for Orthopaedic surgical planning. I have some background in HCI/Usability and I have a suggestion for user interface improvement in the segment editor. I created a rough mock-up below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/3971cb0f2ac52014e707fc38f5bcd9d66e029f10.png" data-download-href="/uploads/short-url/8cb11TCVxDz4TGvFpGjQPStjdHW.png?dl=1" title="Editor%201" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/3971cb0f2ac52014e707fc38f5bcd9d66e029f10_2_690x353.png" alt="Editor%201" data-base62-sha1="8cb11TCVxDz4TGvFpGjQPStjdHW" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/3971cb0f2ac52014e707fc38f5bcd9d66e029f10_2_690x353.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/3971cb0f2ac52014e707fc38f5bcd9d66e029f10_2_1035x529.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/3971cb0f2ac52014e707fc38f5bcd9d66e029f10_2_1380x706.png 2x" data-dominant-color="7A7C86"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Editor%201</span><span class="informations">1920×984 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol>
<li>I think having the 3DSlicer logo on the top left of every module (as it is now) is using up valuable space and it is not necessary. We all know what software we are using. Also the help and attribution at the top of every module is using up prime space. It may be better at the bottom of the module or as a pop-up when a help (?) icon is clicked.</li>
<li>Having a vertical list of tools (effects) in a tool panel or palette with a contextual inspector to the right is a better use of the space and makes using the segmentation tools more efficient. There may be some debate whether a vertical icon eye scan or a horizontal icon eye scan is better, but the vertical tool icon layout has the advantage that it does not change with resize of the panel.</li>
<li>To reduce clutter, the segments list could be placed separately to the right of the interface.</li>
<li>Finally, when using 3D slicer for long periods, the bright interface can cause eyestrain. It would be nice to have a dark mode theme to make it easier on the eyes.</li>
</ol>
<p>Just some thoughts for consideration.</p>

---

## Post #2 by @lassoan (2019-11-05 14:35 UTC)

<aside class="quote no-group" data-username="Umesh_Persad" data-post="1" data-topic="9029">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/umesh_persad/48/4719_2.png" class="avatar"> Umesh_Persad:</div>
<blockquote>
<p>having the 3DSlicer logo on the top left of every module (as it is now) is using up valuable space</p>
</blockquote>
</aside>
<p>Fully agree - see <a href="https://issues.slicer.org/view.php?id=3797" class="inline-onebox">Slicer logo steals considerable space from the module UIs · Issue #3797 · Slicer/Slicer · GitHub</a>.</p>
<aside class="quote no-group" data-username="Umesh_Persad" data-post="1" data-topic="9029">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/umesh_persad/48/4719_2.png" class="avatar"> Umesh_Persad:</div>
<blockquote>
<p>when using 3D slicer for long periods, the bright interface can cause eyestrain</p>
</blockquote>
</aside>
<p>You can enable dark mode in menu: Edit / Application settings / Appearance / Style / Dark Slicer.</p>
<aside class="quote no-group" data-username="Umesh_Persad" data-post="1" data-topic="9029">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/umesh_persad/48/4719_2.png" class="avatar"> Umesh_Persad:</div>
<blockquote>
<p>Having a vertical list of tools (effects) in a tool panel or palette</p>
</blockquote>
</aside>
<p>Vertical tool panel seems like a good idea to me (and it would be easy to implement).</p>
<p>Separating the segment list and effect options as you showed in the mockup above is something to consider, but might not be the optimal choice as is, becase it would:</p>
<ul>
<li>waste a lot of screen space (see all the unused areas in the image above)</li>
<li>make it necessary to cross the entire screen a few times each time you want to select a segment and an effect</li>
<li>would prevent/make it much harder to embed segment editor widget in other module’s GUI as it is not a single widget anymore but multiple widgets</li>
</ul>
<p>I agree that Segment Editor GUI should be improved and the proposal above is a good discussion starter. We would be happy to hear further suggestions.</p>

---

## Post #3 by @Umesh_Persad (2019-11-05 15:23 UTC)

<p>Thanks, I enabled the dark mode and it works fine.</p>
<p>I understand the issue with the segment list … I suppose the general principle is to have an interface that minimizes scrolling and expanding/contracting interface items.</p>
<p>Maybe the solution is a two panel sort of layout across the board. The interface of COMSOL multiphysics comes to mind (screenshot below):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8690064facd6bbbd0810b4338a65cf7a6768056.png" data-download-href="/uploads/short-url/x9ZJKw6JJcbkaD5qBwHBoCNHO4u.png?dl=1" title="Structural_Mechanics_Example_in_COMSOL_Multiphysics" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8690064facd6bbbd0810b4338a65cf7a6768056_2_690x388.png" alt="Structural_Mechanics_Example_in_COMSOL_Multiphysics" data-base62-sha1="x9ZJKw6JJcbkaD5qBwHBoCNHO4u" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8690064facd6bbbd0810b4338a65cf7a6768056_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8690064facd6bbbd0810b4338a65cf7a6768056_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8690064facd6bbbd0810b4338a65cf7a6768056_2_1380x776.png 2x" data-dominant-color="CFD3E9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Structural_Mechanics_Example_in_COMSOL_Multiphysics</span><span class="informations">1920×1080 365 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>A “ribbon” type interface for main functions across the top might be another solution to consider.</p>

---

## Post #4 by @lassoan (2019-11-05 15:54 UTC)

<p>Ribbon interface has come up today on another discussion, too (<a href="https://discourse.slicer.org/t/markups-node-creation-icon-is-confusing-users/9016/3" class="inline-onebox">Markups node creation icon is confusing users</a>). Would you be interested in a mockup of a possible ribbon interface (just using a Tab Widget and dropping other controls into it)?</p>
<p>You can use Qt designer to create GUI - see tutorial <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx?raw=true">here</a>. You don’t need to write any code, just draw using the designer.</p>

---

## Post #5 by @chir.set (2019-11-05 16:04 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="9029">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Vertical tool panel seems like a good idea to me</p>
</blockquote>
</aside>
<p>As a user, that sounds like a good idea to me also.</p>
<aside class="quote no-group" data-username="Umesh_Persad" data-post="3" data-topic="9029">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/umesh_persad/48/4719_2.png" class="avatar"> Umesh_Persad:</div>
<blockquote>
<p>A “ribbon” type interface</p>
</blockquote>
</aside>
<p>That one is quite far from ‘improvement’, being more a profound remake of the UI. It’s already an excellent UI design.</p>

---

## Post #6 by @Umesh_Persad (2019-11-05 19:02 UTC)

<p>I am happy to look at it. Is it QT Design Studio that I need? <a href="https://www.qt.io/ui-design-tools" rel="nofollow noopener">https://www.qt.io/ui-design-tools</a></p>

---

## Post #7 by @lassoan (2019-11-05 19:49 UTC)

<p>For now, you can use any software as a drawing tool.</p>
<p>Qt Designer (which is completely different from Qt Design Studio) is special because .ui files that it generates can be loaded directly into Slicer. Qt Designer is bundled with Slicer (run SlicerDesigner.exe or follow steps described in the tutorial linked above).</p>

---

## Post #8 by @Umesh_Persad (2019-11-05 20:39 UTC)

<p>Ahh, I found it, thanks.</p>
<p>As a prelude to interface design, normally functions are grouped together. So a ribbon is really an organised toolbar with tabs. What comes to mind is the trade-off between modules which is useful from a user contributed perspective versus program functions given the workflow tasks that users have to perform. So is it then that each module category below (including segmentation) could become a tab, and there would be one side panel on the left side of the screen to set options?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af4a59d17cd41f5dd842beb590f291a737cff82d.png" alt="modules" data-base62-sha1="p0GQU4kjVMUYKk6inIPPNF16ERT" width="200" height="315"></p>
<p>The top menu would be:</p>
<p><strong>File Edit View Segmentation Registration Informatics … Utilities Developer Tools Help</strong></p>
<p>where each category is a ribbon toolbar?</p>

---

## Post #9 by @lassoan (2019-11-05 20:49 UTC)

<p>I haven’t thought about putting all the module GUIs in the toolbar, but it’s an interesting idea. Maybe it could be tried on a few modules as an experiment.</p>
<p>What I’ve thought that the ribbon would contain selected commonly used functions, such as features already in the toolbar and menu, but better arranged, and with some more functions and options added.</p>

---

## Post #10 by @Umesh_Persad (2019-11-06 01:25 UTC)

<p>How would you put the following effects into logical groupings based on usage?</p>
<p>None<br>
Paint<br>
Draw<br>
Erase<br>
Level Tracing<br>
Grow from seeds<br>
Fill between slices<br>
Threshold<br>
Margin<br>
Smoothing<br>
Scissors<br>
Logical operators<br>
Draw Tube<br>
Fast Marching<br>
Flood Filling<br>
Mask Volume<br>
Split Volume<br>
Surface Cut<br>
Watershed</p>

---

## Post #11 by @Umesh_Persad (2019-11-06 01:50 UTC)

<p>Another easy change with a drastic increase in usability (in my mind) would be to have the headers of subsections clearly delineated with a higher contrast background as the following example shows:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d19c4f55a81944de17c15b6840155e6cdbc13c1.png" data-download-href="/uploads/short-url/k8ex6vymOYFC3Gotm0babSXtxyV.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d19c4f55a81944de17c15b6840155e6cdbc13c1_2_540x500.png" alt="Untitled" data-base62-sha1="k8ex6vymOYFC3Gotm0babSXtxyV" width="540" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d19c4f55a81944de17c15b6840155e6cdbc13c1_2_540x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d19c4f55a81944de17c15b6840155e6cdbc13c1_2_810x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d19c4f55a81944de17c15b6840155e6cdbc13c1_2_1080x1000.png 2x" data-dominant-color="6D6E6E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1227×1136 45.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It makes it easier to visually scan all the properties or settings on the panel pages.</p>

---

## Post #12 by @lassoan (2019-11-06 04:36 UTC)

<aside class="quote no-group" data-username="Umesh_Persad" data-post="10" data-topic="9029">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/umesh_persad/48/4719_2.png" class="avatar"> Umesh_Persad:</div>
<blockquote>
<p>How would you put the following effects into logical groupings based on usage?</p>
</blockquote>
</aside>
<p>Maybe something like this could work as a categorization:</p>
<p>Manual editing:</p>
<ul>
<li>Paint</li>
<li>Draw</li>
<li>Erase</li>
<li>Level Tracing</li>
<li>Scissors</li>
</ul>
<p>Semi-automatic editing:</p>
<ul>
<li>Threshold</li>
<li>Grow from seeds</li>
<li>Fill between slices</li>
<li>Watershed</li>
<li>Fast Marching</li>
<li>Flood Filling</li>
</ul>
<p>Global editing:</p>
<ul>
<li>Margin</li>
<li>Smoothing</li>
<li>Logical operators</li>
</ul>
<p>Modeling:</p>
<ul>
<li>Draw Tube</li>
<li>Surface Cut</li>
</ul>
<p>Volumes:</p>
<ul>
<li>Mask Volume</li>
<li>Split Volume</li>
</ul>
<p>How would you use these categories?</p>
<aside class="quote no-group" data-username="Umesh_Persad" data-post="11" data-topic="9029">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/umesh_persad/48/4719_2.png" class="avatar"> Umesh_Persad:</div>
<blockquote>
<p>Another easy change with a drastic increase in usability (in my mind) would be to have the headers of subsections clearly delineated with a higher contrast background as the following example shows</p>
</blockquote>
</aside>
<p>That’s interesting and indeed it would be quite easy to implement (by adjusting the style sheet). Let’s see what other users/developers think.</p>

---

## Post #13 by @muratmaga (2019-11-06 05:22 UTC)

<p>Personally, the biggest UI improvements to segment editor would come from making some of the buttons smaller, and saving some real-estate. Currently I have four rows segment effects. Some of the icons are fairly large, and because number of rows change by the width of the module panel, it gets confusing since sometimes I cannot find the tool in the place that I remember it being. (if you want to see what I am talking about in action, make sure to module panel is the smallest width possible in segment editor, then click Scissors effect, which in my case increases the panel width, and reduces the number of rows to three.).</p>
<p>Since we are brain storming session, I wonder if it is possible to create special right-click function for the segment editor where all effects are listed, and I choose what to work on with a single click without having to leave the slice or 3D views, where I am already doing the work?</p>
<p>While we are at it, would it be possible to considering merging Segment Editor and Segmentation modules in a single module panel with two tabs at the top that one can switch between (i.e., right at where Slicer icon is right now). From a workflow and conceptual point of view these two modules are so closely coupled that I am not sure if it makes sense to split them into different modules. One tab can be called ‘Editor’ and the other can be ‘Segment Operations’ or something, and the whole thing can be ‘Segmentation’ or whatever.</p>
<p>+1 for the dark header subsection, better contrast will help to find the subsection boundaries more clearly. <a class="mention" href="/u/smrolfe">@smrolfe</a> this will be definitely useful for the GPA module of SlicerMorph</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb4ca0947b29e37c3ea5c854c697def1685da22f.png" alt="image" data-base62-sha1="zR6187CKCr25bfls3ermoJsVlv1" width="577" height="223"></p>

---

## Post #14 by @Umesh_Persad (2019-11-06 10:17 UTC)

<p>The categories would be used to order the tools on the panels/ribbon. We discussed two alternative designs. Here are wireframes showing rough positioning of items.</p>
<p><strong>Alternative 1</strong> - Reorganized side panel layout. Click on a tool and the options panel contextually changes to the options for the tool.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4db7232e6052b371544e140e4f4b523c3c7f15e5.png" data-download-href="/uploads/short-url/b5v8ohWpMZ4cfS4056Y7kipAc8l.png?dl=1" title="Alternative%201" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4db7232e6052b371544e140e4f4b523c3c7f15e5_2_618x500.png" alt="Alternative%201" data-base62-sha1="b5v8ohWpMZ4cfS4056Y7kipAc8l" width="618" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4db7232e6052b371544e140e4f4b523c3c7f15e5_2_618x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4db7232e6052b371544e140e4f4b523c3c7f15e5_2_927x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4db7232e6052b371544e140e4f4b523c3c7f15e5.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Alternative%201</span><span class="informations">1157×935 27 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Alternative 2</strong> - Ribbon Layout. The tools are organised on the ribbon in categories, and options for the the selected tool will appear in the options panel to the left.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac96e672d5657f188ef5a2adaa01ab133b321966.png" data-download-href="/uploads/short-url/oCNqtHKUdTQoEHR9xDUSwUkL16C.png?dl=1" title="alternative%202" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac96e672d5657f188ef5a2adaa01ab133b321966_2_666x500.png" alt="alternative%202" data-base62-sha1="oCNqtHKUdTQoEHR9xDUSwUkL16C" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac96e672d5657f188ef5a2adaa01ab133b321966_2_666x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac96e672d5657f188ef5a2adaa01ab133b321966_2_999x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac96e672d5657f188ef5a2adaa01ab133b321966.png 2x" data-dominant-color="F9F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">alternative%202</span><span class="informations">1265×949 21.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>NOTE: I am using the free <strong>Pencil</strong> software to do the mockups: <a href="https://pencil.evolus.vn/" rel="noopener nofollow ugc">https://pencil.evolus.vn/</a></p>

---

## Post #15 by @pieper (2019-11-06 14:18 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="13" data-topic="9029">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>+1 for the dark header subsection, better contrast will help to find the subsection boundaries more clearly</p>
</blockquote>
</aside>
<p>I’d also like this - it doesn’t have to be dramatic, just easier to see (and if possible it could be smaller).</p>
<p>Similarly, I find the scrollbar to be very subtle too.  The track color could be darker.</p>
<p><a class="mention" href="/u/umesh_persad">@Umesh_Persad</a> thanks for your work on this <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20">  Did you try the Qt Designer for tweaking the styles?  It might help us close the gap between ideas and implementation.</p>
<p>Another tool people might find helpful for this and other tasks is <a href="https://www.kdab.com/development-resources/qt-tools/gammaray/">GammaRay</a> which connects to the app and exposes just about everything Qt-related including styles (powerful, but also somewhat difficult to use).</p>

---

## Post #16 by @muratmaga (2019-11-06 16:30 UTC)

<p>While these designs look elegant, I would discourage any changes to UI that will result in less viewer area than what we currently have. I often work with the four up view (if not more), and even on 4K screen, I find myself that I need to undock the panel and menus to 2nd screen to increase the viewable areas of slice views (since those are affected by the expansion of slice controllers and other viewer specific menus).  That actually works fairly well, but then the mouse travel time increases and your eyes have to unfocus from what you are doing to another part of the screen to select menus and/or change options.</p>
<p>While going through this exercise, may I also suggest increasing the usability through more context specific menu and interactions (e.g., like right click, drop down menu of effect selection in segment editor).</p>

---

## Post #17 by @pieper (2019-11-06 16:50 UTC)

<p>I agree about keeping the focus on the images as much as possible.</p>
<p>Another kind of system we might learn from is computer modeling / animation systems.  For example Maya has a “<a href="https://www.google.com/search?q=hotbox+maya&amp;tbm=isch&amp;ved=2ahUKEwjrvcvnhNblAhXRn-AKHWCSCU4Q2-cCegQIABAA&amp;oq=hotbox+maya&amp;gs_l=img.3..0i24.4819.5200..5438...0.0..0.72.285.4......0....1..gws-wiz-img.......0j0i5i30j0i8i30.V2mGsFUFfVQ&amp;ei=EPnCXev1OdG_ggfgpKbwBA&amp;bih=1456&amp;biw=1369">hotbox</a>” that you access with the space bar and it’s pretty productive for people who spend all day in the app.</p>

---

## Post #18 by @lassoan (2019-11-06 17:03 UTC)

<p>To minimize need for mouse movement, you can use keyboard shortcuts. Many of them are predefined (see <a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">Segment editor documentation</a>) and you can define custom shortcut for almost anything.</p>
<p>Role of GUI is mainly to make features discoverable and easy to find. It is also very important to make the GUI look nice, because aesthetically not pleasing user interface gives the impression of bad-quality software.</p>
<p>It could be useful to collect the list of most important requirements and prioritize them before trying to find specific solutions. <a class="mention" href="/u/umesh_persad">@Umesh_Persad</a> would you be interested in looking into potential GUI design process approaches and try to apply them for this case? We can certainly use this discourse forum to continue the discussion but we could also talk about this topic during our <a href="https://discourse.slicer.org/c/community/hangout">weekly meetings</a> or set up dedicated meetings about it; and talk in person at upcoming events (RSNA, Slicer project weeks, etc.).</p>

---

## Post #19 by @ezgimercan (2019-11-06 17:34 UTC)

<p>I think darker section headings and moving help are simple ideas that will improve the experience a lot.<br>
Also +1 for the confusion that resizing creates with the layout of Segmentation Effects. Any new layout that changes the location of buttons less than the current layout would be a huge improvement. Even stacking them vertically instead of horizontally in the current layout would change the order less (since some modules change the width of the left panel as Murat described).</p>

---

## Post #20 by @Umesh_Persad (2019-11-06 22:00 UTC)

<p>I can assist time permitting. What my experience has shown me over the years is that it would be difficult to come up with a solution that everyone is happy with for a piece of software that is used for so many tasks. The best designs usually have a very clear vision for what is to be achieved, and there is a core design team that drives it all (with feedback from users of course). Minor changes could be implemented easily without a loss of familiarity for users.</p>
<p>Three key principles of usability are familiarity, consistency and feedback. In other words, if the interface is similar to what people already know and use (standards), it will be easier to use. Menu names, structures and layouts are what users are familiar with using other software. For example, why “Segmentation Effects” versus “Segmentation Tools”. This was why Blender was so hard to use until the Blender 2.8 update. Experts could use it but the majority of people could not.</p>
<p>Secondly, some of the problems mentioned above are due to consistency i.e. panels should have a maximum fixed width so that they don’t allow the layout to stretch out, flow and change. It may seem that this provides more flexibility, but what ends up happening is that it trades off with usability. This is what is happening with the button layout in the segmentation effects panel. Buttons should not also stretch across a full panel and expand with panel expansion. Also for modules, maybe a style guide has to be given to developers to enforce good practice together with vetting to make sure the interface adheres.</p>
<p>Thirdly, on feedback, I also noticed that at times processing is taking place but there is no “being processed” feedback given leaving the impression that the program has frozen, when actually it is just taking a while to process the data. There needs to be some sort of progress bar/indicator to show this.</p>
<p>For the user interface to make sense, the first step is always information architecture. This is what we did by grouping segmentation effects. It must be decided very clearly what the core functionality of 3D Slicer would be and the list of functions of the core. This is the time to combine “modules” by functional area. Programmers care about modules, users care about functions (what can I do and how can tasks flow).</p>
<p>I can’t see any other standard layout aside from Alternatives 1 and 2 above. The left panels may look wide in the mockup, but they are intended to be narrower and take up less space with a more compact design. Menu on top and tools/options panels on the left or right or both. That is what everyone understands.</p>
<p>I am looking at Slicer (Qt) Designer, but it seems to be a bit dated and limited. For example, there are no modern controls like a ribbon menu. I will have to spend some time with it.</p>

---

## Post #21 by @Umesh_Persad (2019-11-07 11:23 UTC)

<p>Is there a way I can get the .ui file(s) for the existing interface so that I can experiment with changes on it?</p>

---

## Post #22 by @Umesh_Persad (2019-11-07 12:15 UTC)

<p>Here is the ribbon simulation with Slicer Designer and buttons. I would need to get the icons.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29dd9ca970b80b7e7ec8454bb147078bd27ed8d4.png" data-download-href="/uploads/short-url/5YmnpYbBgNyFDyTCzqkmFOkrU6o.png?dl=1" title="Ribbon%20light%20mode" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29dd9ca970b80b7e7ec8454bb147078bd27ed8d4.png" alt="Ribbon%20light%20mode" data-base62-sha1="5YmnpYbBgNyFDyTCzqkmFOkrU6o" width="690" height="156" data-dominant-color="E4EEF6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ribbon%20light%20mode</span><span class="informations">1203×273 9.45 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65a0f23fc0e13b03995fc267a092468b5f1a0c76.png" data-download-href="/uploads/short-url/ev337vJP0b2aaPq44s8TDK5BVVs.png?dl=1" title="ribbon%20dark%20mode" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65a0f23fc0e13b03995fc267a092468b5f1a0c76.png" alt="ribbon%20dark%20mode" data-base62-sha1="ev337vJP0b2aaPq44s8TDK5BVVs" width="690" height="149" data-dominant-color="5B656F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ribbon%20dark%20mode</span><span class="informations">1211×262 11.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #23 by @Umesh_Persad (2019-11-07 13:06 UTC)

<p>ITK snap has a good segmentation interface:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c0ad71c92cb68d5cef7aec169a290263462f760.png" data-download-href="/uploads/short-url/404AQJMdsncFNFKkipk3wRPoPCg.png?dl=1" title="itksnap" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c0ad71c92cb68d5cef7aec169a290263462f760_2_122x500.png" alt="itksnap" data-base62-sha1="404AQJMdsncFNFKkipk3wRPoPCg" width="122" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c0ad71c92cb68d5cef7aec169a290263462f760_2_122x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c0ad71c92cb68d5cef7aec169a290263462f760_2_183x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c0ad71c92cb68d5cef7aec169a290263462f760.png 2x" data-dominant-color="DDDDDF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">itksnap</span><span class="informations">187×766 19.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Based on this, here is another layout design that is a small modification of the existing design:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21fe6eb25af606051fa7eddeb894eb90052e8ffa.png" data-download-href="/uploads/short-url/4QIShdxaCk7AHePAgrnqUS1ddIS.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21fe6eb25af606051fa7eddeb894eb90052e8ffa_2_245x500.png" alt="Untitled" data-base62-sha1="4QIShdxaCk7AHePAgrnqUS1ddIS" width="245" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21fe6eb25af606051fa7eddeb894eb90052e8ffa_2_245x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21fe6eb25af606051fa7eddeb894eb90052e8ffa_2_367x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21fe6eb25af606051fa7eddeb894eb90052e8ffa_2_490x1000.png 2x" data-dominant-color="EEF0F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">534×1089 56.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #24 by @jcfr (2019-11-07 14:20 UTC)

<p>Thanks everyone for their input, I am really excited to see where the discussion leads us <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=9" title=":pray:" class="emoji" alt=":pray:"></p>

---

## Post #25 by @lassoan (2021-06-25 21:44 UTC)

<p>2 posts were split to a new topic: <a href="/t/change-segment-editor-button-layout/18343">Change segment editor button layout</a></p>

---

## Post #26 by @lassoan (2021-09-13 19:55 UTC)

<p>Thanks to all the efforts of <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, the new Segment Editor layout is now ready - see more information (and provide any feedback and suggestions) in this topic:</p>
<aside class="quote quote-modified" data-post="1" data-topic="19649">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-segment-editor-layout-vertical-effect-toolbar/19649">New Segment Editor layout - vertical effect toolbar</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Thanks to all the development efforts of <a class="mention" href="/u/jamesobutler">@jamesobutler</a> and feedback from the community, the new, more space-efficient Segment Editor user interface is now ready (available in latest Slicer Preview Release). The main difference is that the effect toolbar is vertical, with fixed number of columns and without icon labels. This layout makes it easier to remember where to find an effect (because the same effect always appears at the same place), and the space is used more efficiently (there is less n…
  </blockquote>
</aside>


---
