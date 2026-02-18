# Adjustable width for DICOM browser columns

**Topic ID**: 10862
**Date**: 2020-03-26
**URL**: https://discourse.slicer.org/t/adjustable-width-for-dicom-browser-columns/10862

---

## Post #1 by @fedorov (2020-03-26 19:54 UTC)

<p>It appears that only 1 column in the DICOM has resizable width. Can this be fixed? Is this in CTK?</p>
<p>            <video title="2020-03-26_15-44-52.mp4" width="695" height="533" style="max-width:100%" poster="https://thumb.screencast.com/3/dedcf330-5901-4d65-bb5d-9d8d97505ed8/thumb.gif" controls="">
              <source src="https://content.screencast.com/users/andrey.f/folders/Snagit/media/dedcf330-5901-4d65-bb5d-9d8d97505ed8/2020-03-26_15-44-52.mp4">
            </source></video>
</p>

---

## Post #2 by @lassoan (2020-03-26 20:18 UTC)

<p>Column width is either adjustable or auto-fit. Column settings (width, default sort option, order, visibility) are all stored in the database itself, so you can modify them with any sqlite editor.</p>
<p>On the video everything works beautifully - all data is visible, column widths are balanced. What would you like to change?</p>

---

## Post #3 by @fedorov (2020-03-26 21:39 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="10862">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Column width is either adjustable or auto-fit. Column settings (width, default sort option, order, visibility) are all stored in the database itself, so you can modify them with any sqlite editor.</p>
</blockquote>
</aside>
<p>Sorry, I don’t understand this. I just want to adjust the column width as a user, using sqlite editor is probably the last thing I want to do.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="10862">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>On the video everything works beautifully - all data is visible, column widths are balanced. What would you like to change?</p>
</blockquote>
</aside>
<p>“Date added” column is truncated.</p>

---

## Post #4 by @lassoan (2020-03-26 21:54 UTC)

<p>The date added column contains date&amp;time and therefore it is quite wide and most often it is only needed for sorting (e.g, most recently added appears at the top). Nevertheless, you can resize it the same way as all the other resizeable columns - by click-and-dragging the right side (see related discussion <a href="https://discourse.slicer.org/t/new-dicom-browser-is-ready/8819/7">here</a>).</p>
<p>Since this question has come up on this forum the second time, most likely there are 200 other people, who also had trouble with this, just did not report it, so it would be nice to find a solution that would make things more intuitive and not too hard to implement. Do you have any suggestions?</p>
<aside class="quote no-group" data-username="fedorov" data-post="3" data-topic="10862">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I just want to adjust the column width as a user, using sqlite editor is probably the last thing I want to do.</p>
</blockquote>
</aside>
<p>We could expose this feature to the users with a more convenient GUI, but for now you need to use an sqlite editor if you want to customize the database browser columns.</p>

---

## Post #5 by @fedorov (2020-03-26 21:58 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="10862">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Nevertheless, you can resize it the same way as all the other resizeable columns - by click-and-dragging the right side (see related discussion <a href="https://discourse.slicer.org/t/new-dicom-browser-is-ready/8819/7">here</a>).</p>
</blockquote>
</aside>
<p>Wow. I would never ever guess this. Thank you!</p>
<p><a href="https://www.screencast.com/t/kLEKCvxiIht" class="onebox" target="_blank" rel="noopener">https://www.screencast.com/t/kLEKCvxiIht</a></p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="10862">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>it would be nice to find a solution that would make things more intuitive and not too hard to implement. Do you have any suggestions?</p>
</blockquote>
</aside>
<p>I guess the obvious and intuitive way to do this by making it possible to drag the left edge of the column is not an option, and I can’t think of any other more intuitive way to do this.</p>

---
