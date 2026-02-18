# Help tab has a fixed size

**Topic ID**: 15972
**Date**: 2021-02-12
**URL**: https://discourse.slicer.org/t/help-tab-has-a-fixed-size/15972

---

## Post #1 by @muratmaga (2021-02-12 18:13 UTC)

<p>When expanded, Help tab takes too much space in the module view, pushing all module specific functions too far down (see example for Data module). Now that almost all the documentation is online, and modules provide hotlinks to the readthedocs or github repo as oppose to inline documentation, can we truncate this? I think 4-5 lines would suffice.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fece823448af235f276c666c42bcbc6d3a97a61.png" data-download-href="/uploads/short-url/6PY0IrYM3f3KNqK2DV13A9nYgBX.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fece823448af235f276c666c42bcbc6d3a97a61.png" alt="image" data-base62-sha1="6PY0IrYM3f3KNqK2DV13A9nYgBX" width="346" height="500" data-dominant-color="353535"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">553×798 15 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-02-12 20:15 UTC)

<p>In general, we cannot fully rely on online documentation (custom applications may not even have any publicly accessible documentation, network is not always available, etc.) but I agree that often the Help area takes more space than necessary from the very precious vertical space.</p>
<p>There is no fixed size set for the Help tab and the the text already displayed using a ctkFittedTextBrowser, but the problem may be that the Help&amp;acknowledegment section size is determined by size of both the Help and Acknowledgement tab content. Instead of trying to fix this problem in isolation, I think it would be better to address the problem of lack of vertical space in the module panel overall.</p>
<p>For example, we replace the current Slicer icon and Help&amp;acknowledgement section:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08fc69ef11046aa069e15236b5a701de6602bed8.png" data-download-href="/uploads/short-url/1huC3CoUEZdlFZRPIdBYqG5DBAQ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08fc69ef11046aa069e15236b5a701de6602bed8_2_300x70.png" alt="image" data-base62-sha1="1huC3CoUEZdlFZRPIdBYqG5DBAQ" width="300" height="70" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08fc69ef11046aa069e15236b5a701de6602bed8_2_300x70.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08fc69ef11046aa069e15236b5a701de6602bed8_2_450x105.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08fc69ef11046aa069e15236b5a701de6602bed8_2_600x140.png 2x" data-dominant-color="383838"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1088×274 10.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>With a more compact row consisting of Slicer icon, module title, and module actions (show help, show acknowledgment, add module to favorites, undock module panel, hide module panel, …):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0bdce1d139616e31c2ae525ab000e645e763acd7.png" alt="image" data-base62-sha1="1GWun8g8tZ7LtBMBs1DeIMIzmR1" width="300" height="35"></p>
<p>or</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c92c841ac2bf2e8317469a2d82d9d98a58a5b80.png" alt="image" data-base62-sha1="44LQCokrvKSnXhcm3DhErPqv5L2" width="300" height="60"></p>
<p>The Help and Acknowledgment buttons could show the text in a dockable widget, which could be moved out of the main window layout or docked to the side.</p>
<p>This new title widget could replace the module panel title bar, which is the empty row with the small undock and close buttons, saving one more line.</p>
<p>As a quick test, I would recommend trying to hide all the non-essential elements from the module panel - the result is breathtaking:</p>
<pre data-code-wrap="python"><code class="lang-python">slicer.util.setApplicationLogoVisible(False)
slicer.util.setModuleHelpSectionVisible(False)
slicer.util.setDataProbeVisible(False)
slicer.util.setModulePanelTitleVisible(False)
</code></pre>

---

## Post #3 by @muratmaga (2021-02-12 23:57 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="15972">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>As a quick test, I would recommend trying to hide all the non-essential elements from the module panel - the result is breathtaking:</p>
</blockquote>
</aside>
<p>We already do that in SlicerMorph, those are our defaults. However, I think there is some sort of a bug with the ctkFittedTextBrowser. When I first open the help, it has a huge blank space. But then when I click on the Acknowledgement it actually collapses that space, and when when I go back to Help, that blank space is removed.</p>
<p>This behavior reproduces for other modules too (e.g., segment editor)…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f165e5a3603491d8ffef36a68b97498bfc261422.png" data-download-href="/uploads/short-url/yrvnN7kE4UXs4cMQCv5D2540SDU.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f165e5a3603491d8ffef36a68b97498bfc261422.png" alt="image" data-base62-sha1="yrvnN7kE4UXs4cMQCv5D2540SDU" width="322" height="500" data-dominant-color="2E3030"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">554×859 13.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25f00d6413d48d64c927b66c0a1ae33ae7f6d894.png" alt="image" data-base62-sha1="5pBYw9cpld3SbOvkbgDBrh91qTO" width="421" height="344"></p>

---

## Post #4 by @lassoan (2021-02-13 00:06 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="15972">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>We already do that in SlicerMorph, those are our defaults.</p>
</blockquote>
</aside>
<p>Unfortunately, these <code>set...Visible</code> functions are only usable for custom applications and testing, because you would need convenient way to show these GUI elements (except the application logo, which I think we should just remove and show it in DataProbe when the mouse pointer is out of the view layout). The module panel title bar might not seem essential, but it is, because without that the module panel cannot be undocked or docked to another location.</p>
<p>The fitted text browser may not actually compute size hints until its first rendered, so maybe the size hint computation should be triggered somehow. Or merge help and acknowledgement into a single browser (how it is done in the module finder). Still it would not solve the main problem that there are just too many things in the module panel, and that if you show something in the Help section then you need to scroll a lot to see the module GUI. That’s why I think a better solution could be to show the help text in a docking widget, outside the module panel (this way the user could read the help text while manipulating the module widget).</p>
<p>There could be of course many other options - it would be great to get more feedback and suggestions.</p>

---

## Post #5 by @muratmaga (2021-02-13 05:35 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="15972">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>That’s why I think a better solution could be to show the help text in a docking widget, outside the module panel (this way the user could read the help text while manipulating the module widget).</p>
</blockquote>
</aside>
<p>I think how the documentation is going to be presented will determine how the Help tab should be reconfigured. As is, the sole function of Help is to provide a hotlink to online documentation. If this continues to be the case, I don’t think it will be helpful to have a another docking window as help, you may just as well use the external browser. Help tab might be collapsed into a something a lot more simple to provide the link functionality.</p>
<p>If somehow the online documentations can be rendered inside this Help window close to the fidelity of github, I think a dockable widget makes sense.</p>
<p>But as project we can’t maintain two different documentation sets to cover offline use cases.</p>

---

## Post #6 by @lassoan (2021-02-13 06:25 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="15972">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>As is, the sole function of Help is to provide a hotlink to online documentation.</p>
</blockquote>
</aside>
<p>A much more important role of module help is locating a module in the module finder. You just type a word and you get a list of modules that mention that word in their help text and you can very quickly browse through dozens of modules, have a quick glance at the few-sentence description of what the module does immediately (instead of waiting for several seconds for a webpage to open). We could make this even more powerful by somehow fetching module help text for all modules in all the extensions.</p>
<p>I agree that it is important not to duplicate module documentation and that hosting it in the same repository as the code makes the most sense (and you can set up readthedocs to handle versioning and offlne access). But keeping this short module description (Help &amp; Acknowledgemen) is not that much duplication and is quite useful.</p>
<p>We just need to figure out what are the best ways to make the information accessible.</p>

---

## Post #7 by @pieper (2021-02-13 14:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="15972">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We could make this even more powerful by somehow fetching module help text for all modules in all the extensions.</p>
</blockquote>
</aside>
<p>I like this idea - it could be the last step of the factory after building all the extensions to compile a file with all the help text fields.  Then in the module search we could propose extensions based on keywords.</p>

---

## Post #8 by @muratmaga (2021-02-13 17:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="15972">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>But keeping this short module description (Help &amp; Acknowledgemen) is not that much duplication and is quite useful.</p>
</blockquote>
</aside>
<p>No, that’s totally fine and that’s what we do that anyways. My point is, if all the information that the help and acknowledgement is going to convey continues to be a short summary of the module and a link to documentation, then I am not sure how valuable is to rethink the Help tab as a separate dockable widget.  We might perhaps keep as is, and just fix the erroneous auto-resizing issue. But you guys now this better of course.</p>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="15972">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We could make this even more powerful by somehow fetching module help text for all modules in all the extensions.</p>
</blockquote>
</aside>
<p>This sounds great actually…</p>

---

## Post #9 by @lassoan (2021-02-13 18:20 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> how do you use the help section now? Is the blank area below the text a cosmetic issue only or it affects functionality as well? Showing the help and acknowledgment text in one widget would probably solve the blank space is but it would make the area bigger. Would this work for you?</p>

---

## Post #10 by @muratmaga (2021-02-13 18:47 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="15972">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>how do you use the help section now?</p>
</blockquote>
</aside>
<p>We use it very similar to other modules. Provide a short description of what the module does, and provide a link to the documents on GH page.</p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="15972">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Is the blank area below the text a cosmetic issue only or it affects functionality as well?</p>
</blockquote>
</aside>
<p>I wouldn’t say a cosmetic issue. because the extra space in the help tab takes so much of the vertical space (unless one goes back and forth between acknowledgement and help section), we decided to start out views with Help compressed (see below). We tell that Help is there, but it is easy to overlook, if you are not a regular slicer user. Even the reviewers of the SlicerMorph paper missed that.</p>
<p>This is how modules initiate:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f03b589b903d25df172bddc04b76c0df21f815c1.png" data-download-href="/uploads/short-url/yhbJXUkHp8Ex8sWcAPUDBmcmTQZ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f03b589b903d25df172bddc04b76c0df21f815c1.png" alt="image" data-base62-sha1="yhbJXUkHp8Ex8sWcAPUDBmcmTQZ" width="430" height="500" data-dominant-color="404343"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">558×648 18.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
versus the same module Help section expanded:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8b2debf9d0d8761224139a24b65292dc5f41214.png" data-download-href="/uploads/short-url/sDsIJAbKQWjJVPBNarizRBrjAOM.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8b2debf9d0d8761224139a24b65292dc5f41214.png" alt="image" data-base62-sha1="sDsIJAbKQWjJVPBNarizRBrjAOM" width="433" height="500" data-dominant-color="333636"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">559×645 14.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
versus auto-resize kicks in<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7dd23cac2b0e4cc19acc6b4159384f3d40fca8e.png" data-download-href="/uploads/short-url/x5a5iNUkZAPRZxkjDV4XiXeKmlg.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7dd23cac2b0e4cc19acc6b4159384f3d40fca8e.png" alt="image" data-base62-sha1="x5a5iNUkZAPRZxkjDV4XiXeKmlg" width="426" height="500" data-dominant-color="3E4041"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">554×649 18.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The last would be a good solution. That way parts of the actual module is still visible. And the help tab is expanded.</p>
<p>(As a side note, older modules have large logos and text in acknowledgement section, which end up taking a lot of space, and it is one of the reasons that help section having so much white space. Those logos do not render particularly well, and their layout leaves much to be desired. See Volumes module below:)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1fe36cbbeeabc802ab2e5bd05274fed428d7433e.png" alt="image" data-base62-sha1="4y63wwpYS4JdaxIbwNZ5SMzoMBo" width="447" height="449"></p>

---

## Post #11 by @lassoan (2021-02-13 20:36 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="15972">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I wouldn’t say a cosmetic issue. because the extra space in the help tab takes so much of the vertical space</p>
</blockquote>
</aside>
<p>Help &amp; Acknowledgement section is collapsed by default. Users can open it, read it, maybe click the link to the online documentation, and then close it if they want to use the module. For the rare case when the help text contain step-by-step instructions then it could be useful to keep it open, but then the user needs to scroll between the instructions and the module GUI anyway (somewhat less if the minimum amount of space is used), but for that a better solution could be a separate docking widget. But from all the discussion above, it seems that keeping the help text as a short summary and link to online documentation (no step-by-step instructions) seems to be a more reasonable option.</p>

---

## Post #12 by @muratmaga (2021-02-13 20:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="15972">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Help &amp; Acknowledgement section is collapsed by default.</p>
</blockquote>
</aside>
<p>Oh, I didn’t know that became default in overall Slicer. Anyways, but that’s really not a good thing to do. Help do contain useful information and starting collapsed make so inconspicuous in the module view that it is over looked.</p>

---
