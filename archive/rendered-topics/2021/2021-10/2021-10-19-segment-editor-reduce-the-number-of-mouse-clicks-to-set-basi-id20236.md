---
topic_id: 20236
title: "Segment Editor Reduce The Number Of Mouse Clicks To Set Basi"
date: 2021-10-19
url: https://discourse.slicer.org/t/20236
---

# Segment Editor: reduce the number of mouse clicks to set basic colour for segment

**Topic ID**: 20236
**Date**: 2021-10-19
**URL**: https://discourse.slicer.org/t/segment-editor-reduce-the-number-of-mouse-clicks-to-set-basic-colour-for-segment/20236

---

## Post #1 by @DIV (2021-10-19 11:50 UTC)

<p>If I wish to set a Basic Color for a segment I need <em>seven</em> mouse clicks (or <em>six</em> operations):</p>
<ul>
<li>double-click the relevant swatch for <strong>Segment color</strong>;</li>
<li>click <strong>Color</strong> in the (badly named) <em>Slicer</em> dialogue box;</li>
<li>click <strong>Basic</strong> tab in the <em>Select Color</em> dialogue box;</li>
<li>click a swatch under <strong>Basic colors</strong>;</li>
<li>click <strong>OK</strong> in the <em>Select Color</em> dialogue box;</li>
<li>click <strong>Select</strong> in the <em>Slicer</em> dialogue box.<br>
That is too many mouse clicks for a basic operation that I regularly perform.</li>
</ul>
<p>I often have multiple segments representing the same category of anatomy (e.g. multiple bones; or multiple arteries).  I don’t want them all to be the same colour, because I want to able to distinguish them at a glance.</p>
<p>The best suggestion I have off the top of my head is to integrate the current <em>two</em> dialogue boxes identified above into a unified dialogue box with three tabs.  The first tab would contain the content of the current (badly named) <em>Slicer</em> dialogue box, and could perhaps be named <strong>Properties</strong>;  the remaining two tabs would be identical to the existing <strong>Basic</strong> and <strong>Labels</strong>  tabs in the <em>Select Color</em> dialogue box.</p>
<p>If I wish to set a Basic Color for a segment the new workflow would then be:</p>
<ul>
<li>double-click the relevant swatch for <strong>Segment color</strong>;</li>
<li>click <strong>Basic</strong> tab in the new (unified) dialogue box;</li>
<li>click a swatch under <strong>Basic colors</strong>;</li>
<li>click <strong>OK</strong> in the new (unified) dialogue box.<br>
I would thus need <em>five</em> mouse clicks (or <em>four</em> operations).</li>
</ul>
<p>It may be subtle, but I believe this would improve the user experience.</p>
<p>—DIV</p>

---

## Post #2 by @jamesobutler (2021-10-20 02:58 UTC)

<p>Here are images for reference for other readers</p>
<aside class="quote no-group" data-username="DIV" data-post="1" data-topic="20236">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>double-click the relevant swatch for <strong>Segment color</strong> ;</p>
</blockquote>
</aside>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2a0539ad9b429dd233291f457bb41ae6532ff2a.png" alt="image" data-base62-sha1="wkPpclDeS0kZCKp22Pc7H97ANgm" width="457" height="160"></p>
<aside class="quote no-group" data-username="DIV" data-post="1" data-topic="20236">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>click <strong>Color</strong> in the (badly named) <em>Slicer</em> dialogue box;</p>
</blockquote>
</aside>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/4026c683aebdbca272d7d8f944941a05f6602cf5.png" alt="image" data-base62-sha1="99vDjyE7y02UlsXDtmQ9WfIKdq5" width="306" height="404"></p>
<aside class="quote no-group" data-username="DIV" data-post="1" data-topic="20236">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<ul>
<li>click <strong>Basic</strong> tab in the <em>Select Color</em> dialogue box;</li>
<li>click a swatch under <strong>Basic colors</strong> ;</li>
</ul>
</blockquote>
</aside>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6db7602383a06d99f725cc01d5f47c0f75bee084.png" alt="image" data-base62-sha1="fEAVk1QVgiGnsw4uf6RKER4ByXW" width="581" height="453"></p>
<aside class="quote no-group" data-username="DIV" data-post="1" data-topic="20236">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>click <strong>Select</strong> in the <em>Slicer</em> dialogue box.</p>
</blockquote>
</aside>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d895f3215784109d869a95cd55db34f4b8902b65.png" alt="image" data-base62-sha1="uU0oLowp8LrZ4W1LcALOsvmQeyh" width="306" height="404"></p>

---

## Post #3 by @lassoan (2021-10-20 04:19 UTC)

<p>You actually don’t need to switch to Basic tab, so it “just” takes 5 clicks to change color. Of course 5 would be still more than the usual 3 clicks, but you can reduce the required number of clicks to 3 by creating a json file that contains all the segment names and colors that you use frequently, or further reduce it to 0 clicks by creating a segmentation node with empty segments that you can use as a template for each new segmentation.</p>
<p>If you just want to always use the “Basic” color picker then you can change that in Application settings → Application startup script → add <code>ctk.ctkColorDialog().setDefaultTab(0)</code> to the end of the displayed startup script file.</p>
<aside class="quote no-group" data-username="DIV" data-post="1" data-topic="20236">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>click <strong>Color</strong> in the (badly named) <em>Slicer</em> dialogue box;</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="DIV" data-post="1" data-topic="20236">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>content of the current (badly named) <em>Slicer</em> dialogue box</p>
</blockquote>
</aside>
<p>Windows uses the application name as title in all dialog boxes that have no specific title - not just in Slicer, but in all other applications, too.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/566a7e73a7b2961698721aa0a8f1e8b4f2198954.png" data-download-href="/uploads/short-url/cktdVK4JkJt6ZEjODXIolo4N25u.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/566a7e73a7b2961698721aa0a8f1e8b4f2198954_2_690x375.png" alt="image" data-base62-sha1="cktdVK4JkJt6ZEjODXIolo4N25u" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/566a7e73a7b2961698721aa0a8f1e8b4f2198954_2_690x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/566a7e73a7b2961698721aa0a8f1e8b4f2198954_2_1035x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/566a7e73a7b2961698721aa0a8f1e8b4f2198954.png 2x" data-dominant-color="F2F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1251×681 42.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Maybe adding a bit more specific title (“Terminology”?) could be useful, but the current behavior is not faulty. Therefore I don’t feel that it is justified bringing it up twice like it was some serious mistake and doing so somewhat dulls the edge of your other comments.</p>

---

## Post #4 by @DIV (2021-10-20 07:07 UTC)

<p>Hello, Andras.<br>
Thanks for your response.</p>
<p>I’m not sure why, but for me it <em>is</em> definitely necessary to click the <strong>Basic</strong> tab in the workflow I described, because when I click click <strong>Color</strong> in the (Windows-default-named) <em>Slicer</em> dialogue box (to be more precise, I’m clicking on the field next to that label, which contains a coloured square), the <strong>Labels</strong> tabs always comes up in the <em>Select Color</em> dialogue box.<br>
That is for the two most recent versions of Slicer on Windows (4.11.20210226 &amp; 4.11.20200930).</p>
<p>Or did you mean that it’s not necessary to select the Basic tab if I add the relevant line of code you described to the end of the displayed startup script file?<br>
I have tried to do this, by adding the command “ctk.ctkColorDialog().setDefaultTab(0)” on a new line in the file “C:/Users/[username]/.slicerrc.py”, but it seems to have no effect.  (Unless I have to restart the application or computer or something first?  I merely opened a new instance of Slicer, without closing all old instances.)</p>
<p>By the by, in the <em>Settings</em> dialogue box there’s a button with a folder icon beside the <strong>Application startup script</strong> text field.  I guess that clicking on this “opens” the file in whatever the default OS application is, because I was expecting the file to be opened for editing as a text file, but instead I think that Windows tried to run it as a Python file (because of the *.py extension), which wasn’t what I was expecting, and probably isn’t a very useful action for the button to invoke.  Not sure if it might be better for this button to get the OS to open this *.py file as if it were a text file?</p>
<p>OK, OK, it may have seemed unnecessary to repeat the point about the naming of the <em>Slicer</em> dialogue box twice.  I could say it was repeated for consistency, but you could also interpret the repetition as lazy copy-and-paste.<br>
Certainly I didn’t mean to imply that it was a major issue.  I was just feeling irritated that the dialogue box didn’t have a distinctive name that I could use to clearly refer to it.  In the meanwhile James has greatly helped out in that department by adding little screen captures of the relevant steps.</p>
<p>—DIV</p>

---

## Post #5 by @DIV (2021-10-20 07:44 UTC)

<p>Further on the topic of modifying the start-up script file, I clicked the toolbar button to show the Python Interactor window just after launching a new instance of Slicer, and it shows the following error message.</p>
<pre><code class="lang-auto">Python 3.6.7 (default, Feb 27 2021, 00:03:56) [MSC v.1924 64 bit (AMD64)] on win32
&gt;&gt;&gt; 
Loading Slicer RC file [C:/Users/[username]/.slicerrc.py]
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "&lt;string&gt;", line 131, in loadSlicerRCFile
  File "E:/Program Files/Slicer 4.11.20210226/bin/../lib/Python/Lib\encodings\cp1252.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 370: character maps to &lt;undefined&gt;
</code></pre>
<p>I’m not too sure what’s producing the error.  Maybe it’s been there all along, as it came up again even when I removed (commented out) the newly added command from the start-up script file.<br>
Before now I haven’t generally opened the Python Interactor window.</p>
<p>—DIV</p>
<p>P.S.  One recent thing I tried quickly was running the code at <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#register-custom-volume-rendering-presets" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a> , but without creating the *.mrml file first.  Funnily enough, Python didn’t show any error when I ran that.</p>

---

## Post #6 by @jamesobutler (2021-10-20 19:51 UTC)

<aside class="quote no-group" data-username="DIV" data-post="5" data-topic="20236">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p><code>Loading Slicer RC file [C:/Users/[username]/.slicerrc.py]</code></p>
</blockquote>
</aside>
<p>What is the actual location of your .slicerrc.py file? Do you have special characters in your username?</p>
<p>This is what it displays for me in the python interactor window.</p>
<blockquote>
<p>Loading Slicer RC file [C:/Users/james/.slicerrc.py]</p>
</blockquote>

---

## Post #7 by @DIV (2021-10-22 05:01 UTC)

<p>Hello, James.<br>
My username is purely alphanumeric;  besides that, the file is exactly where I said:   <code>C:/Users/[username]/.slicerrc.py</code>.<br>
<em>thinking</em>…<br>
<em>working</em>…<br>
OK, I have found the cause of the error message.<br>
I had inserted the following into the start-up script file (on the last three lines):</p>
<pre><code class="lang-auto"># Always use the “Basic” color picker
# https://discourse.slicer.org/t/segment-editor-reduce-the-number-of-mouse-clicks-to-set-basic-colour-for-segment/20236/3
ctk.ctkColorDialog().setDefaultTab(0)
</code></pre>
<p>If you inspect the comment “<code>Always use the </code><strong>“</strong><code>Basic</code><strong>”</strong><code> color picker</code>” [<em>copied from this thread</em>] carefully you’ll see that proper quotation marks are used.  This is causing the error.<br>
When I change the comment to “<code>Always use the "Basic" color picker</code>” the error goes away.</p>
<p>I don’t think the curved quotation marks are especially exotic symbols, and most of all I didn’t expect any issue to be caused because they are in a comment, not a command.<br>
Nevertheless I leave it to your judgement as to whether this is a bug or whether it is expected/intended behaviour.</p>
<p>I can also confirm that the command is run at start-up, as the <strong>Basic</strong> tab is indeed now shown as the default tab in the <em>Select Color</em> dialogue box.<br>
Every little bit helps.  <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p><code>***</code></p>
<p>Personally I would prefer that after clicking <strong>OK</strong> in the <em>Select Color</em> dialogue box I didn’t have to then also click <strong>Select</strong> in the <em>Slicer</em> dialogue box, but I think that the current structure of having two dialogue boxes makes the twofold confirmation unavoidable.  That was part of the rationale behind my proposal to unify the current two dialogue boxes (with 1 + 2 tabs) into a single dialogue box (with 3 tabs):  just a single “OK” would be needed.<br>
I realise that may not be a huge priority, but the idea is there to be considered anyway.</p>
<p>—DIV</p>

---
