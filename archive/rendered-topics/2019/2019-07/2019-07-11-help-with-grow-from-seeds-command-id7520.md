---
topic_id: 7520
title: "Help With Grow From Seeds Command"
date: 2019-07-11
url: https://discourse.slicer.org/t/7520
---

# Help with "Grow From Seeds" command

**Topic ID**: 7520
**Date**: 2019-07-11
**URL**: https://discourse.slicer.org/t/help-with-grow-from-seeds-command/7520

---

## Post #1 by @Ricardo (2019-07-11 03:39 UTC)

<p>Hi all.</p>
<p>Recently started to work with 3DSlicer and would like to know if it’s possibly for the community to help with some issue I’m having with the “Grow From Seeds” command.</p>
<p>I’m trying the a human heart segmentation using this command, but the end result is merely some small volumes for the different created segments. End result:</p>
<p>                        <a href="https://imgur.com/4FXPlQO" target="_blank" class="onebox" rel="nofollow noopener">
              <img src="https://i.imgur.com/4FXPlQO.jpg?fb" title="Imgur" alt="Imgur" height="315" width="600">
            </a>

</p>
<p>I’ve created 8 different segments, marked all of them, but when I initialize the “Grow From Seeds” command, all I get is what you see in the upper image.</p>
<p>What can be the cause for this and what other options do I have to do a heart segmentation?</p>
<p>Thank you in advance,<br>
Ricardo</p>

---

## Post #2 by @lassoan (2019-07-11 03:41 UTC)

<p>Click “Apply” in “Grow from seeds” effect once you are happy with the preview results.</p>

---

## Post #3 by @Ricardo (2019-07-15 10:18 UTC)

<p>Thank you so much, will try it out.</p>

---

## Post #4 by @Ricardo (2019-08-01 11:07 UTC)

<p>Hi again.</p>
<p>Despite Iassoan tip, I couldn’t make it work. The end result is always the one showed in the first message.</p>
<p>I’ve been thinking and looking answers for this, but with no luck. I wonder if the cause can be one of the following:</p>
<ol>
<li>Poor image quality from the TAC scan, making so it’s hard for the software to find boundaries for each region;</li>
<li>Badly defined regions, with some seeds overlapping more than one region?</li>
</ol>
<p>Thank you,<br>
Ricardo</p>

---

## Post #5 by @lassoan (2019-08-01 12:45 UTC)

<p>Which Slicer version do you use?<br>
Do you see any warnings or errors in the application log?<br>
Does the same procedure works if you segment one of the sample data sets?</p>

---

## Post #6 by @Ricardo (2019-08-09 13:45 UTC)

<p>Hi Iassoan.</p>
<p>First of all, my apologies on taking so long to answer you and thanks again for your quick response.</p>
<ol>
<li>
<p>Im using 4.10.1 build;</p>
</li>
<li>
<p>No errors in the log;</p>
</li>
<li>
<p>I’ve made this one tutorial (<a href="https://www.youtube.com/watch?v=BJoIexIvtGo" rel="nofollow noopener">Whole heart segmentation from cardiac CT in 10 minutes</a>) from start to end and everything went really smooth.</p>
</li>
</ol>
<p>Regards,<br>
Ricardo</p>

---

## Post #7 by @lassoan (2019-08-09 13:57 UTC)

<p>Thanks for the update so you still have problems segmenting your data set?</p>

---

## Post #8 by @Ricardo (2019-08-09 14:09 UTC)

<p>I do. It’s really weird, cause I followed every single step on the tutorial I posted and while working perfectly with the tutorial case, it just doesn’t with mine.</p>
<p>Of course I’m doing something wrong, but can’t figure out what.</p>
<p>Regards,<br>
Ricardo</p>

---

## Post #9 by @lassoan (2019-08-09 17:38 UTC)

<p>What is the scalar type and dimensions of your volume? (you can find it in Volumes module / information section)</p>

---

## Post #10 by @Ricardo (2019-08-13 08:52 UTC)

<p>Hello Iassoan,</p>
<p>I’m gonna redo this case from zero with all the caution and see if I get a different outcome this time. I’ll let you know how it went.</p>
<p>Thank you for the help.</p>

---
