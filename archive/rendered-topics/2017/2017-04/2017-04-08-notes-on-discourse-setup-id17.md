---
topic_id: 17
title: "Notes On Discourse Setup"
date: 2017-04-08
url: https://discourse.slicer.org/t/17
---

# Notes on Discourse setup

**Topic ID**: 17
**Date**: 2017-04-08
**URL**: https://discourse.slicer.org/t/notes-on-discourse-setup/17

---

## Post #1 by @ihnorton (2017-04-08 03:06 UTC)

<p>TODO:</p>
<ul>
<li>
<s>decide on/configure contact email (rarely needed but good to have)</s> (posted in Staff)</li>
<li>
<s>research Google OAuth endpoint that can be controlled by group?</s>(posted details in Staff)</li>
<li><s>move GitHub OAuth endpoint to Slicer org</s></li>
<li><s>find/make a better horizontal logo, “3DSlicer” is too small in the current one.</s></li>
<li>
<s>consider/test whether we can use <a href="https://meta.discourse.org/t/setup-incoming-emails-e-mail/42026">inbound email</a> support with <a href="mailto:slicer-users@bwh.harvard.edu">slicer-users@bwh.harvard.edu</a> – for muscle memory posting seamlessly. Responses would pass through discoursemail domain, and users could eventually log in and fully configure the automatic shadow account.</s> (I think this would be too complicated. Let’s try without first)</li>
</ul>
<hr>
<p>Points of contact:</p>
<ul>
<li>
<a href="mailto:team@discourse.org">team@discourse.org</a><br>
or</li>
<li>simply <code>@discourse</code> (note that @-name will ping user, just like GitHub. Use backticks to avoid ping!).</li>
</ul>
<hr>
<p>OAuth config is very simple:</p>
<ul>
<li>Google: <a href="https://meta.discourse.org/t/configuring-google-login-for-discourse/15858">https://meta.discourse.org/t/configuring-google-login-for-discourse/15858</a>
</li>
<li>GitHub: <a href="https://meta.discourse.org/t/configuring-github-login-for-discourse/13745">https://meta.discourse.org/t/configuring-github-login-for-discourse/13745</a>
</li>
</ul>
<hr>

---

## Post #2 by @jcfr (2017-04-08 04:52 UTC)

<p>Well done <a class="mention" href="/u/ihnorton">@ihnorton</a> <img src="https://emoji.discourse-cdn.com/twitter/thumbsup.png?v=12" title=":thumbsup:" class="emoji" alt=":thumbsup:" loading="lazy" width="20" height="20"></p>
<p>I didn’t have issue to sign up using GitHub. That said, when I first tried using google email, it failed. The screenshot below illustrate the issue.</p>
<p>Additionally, the authorization for GitHub is not associated with a Slicer logo but with <a class="mention" href="/u/ihnorton">@ihnorton</a> handle. Is there a way to change it to <code>@slicer</code> (<code>@slicerbot</code>) or something like this ?</p>
<p>Here the failed one from Google:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/496abcf9797db16e2da8b0fb5c098cf8c8af12d4.png" data-download-href="/uploads/short-url/attxwZSc8ksjLee7ayhniRfCoT2.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/496abcf9797db16e2da8b0fb5c098cf8c8af12d4_2_690x405.png" alt="image" data-base62-sha1="attxwZSc8ksjLee7ayhniRfCoT2" width="690" height="405" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/496abcf9797db16e2da8b0fb5c098cf8c8af12d4_2_690x405.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/496abcf9797db16e2da8b0fb5c098cf8c8af12d4.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/496abcf9797db16e2da8b0fb5c098cf8c8af12d4.png 2x" data-dominant-color="FCFAF9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">829×487 11.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @jcfr (2017-04-08 04:53 UTC)

<p>And here is the one from GitHub where we can see the missing Slicer logo:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29d3a873943a1bc193a80278264b636819c695b4.png" data-download-href="/uploads/short-url/5Y13bVMjegHfwTHNO0vA8IpMhk8.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29d3a873943a1bc193a80278264b636819c695b4_2_690x337.png" alt="image" data-base62-sha1="5Y13bVMjegHfwTHNO0vA8IpMhk8" width="690" height="337" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29d3a873943a1bc193a80278264b636819c695b4_2_690x337.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29d3a873943a1bc193a80278264b636819c695b4.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29d3a873943a1bc193a80278264b636819c695b4.png 2x" data-dominant-color="EEF4F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">909×444 48.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2017-04-08 12:22 UTC)

<p>I’ve signed up using github and indeed it is very confusing that I have to give permission to my github account personally to Isaiah. Slicerbot or similar would be good.</p>

---

## Post #5 by @ihnorton (2017-04-08 12:22 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> I requested to transfer the github oauth application to the Slicer org. Google is fixed, though I’m not sure yet if we can move it to a group-control (it’s on the list).</p>

---

## Post #6 by @lassoan (2017-04-08 12:27 UTC)

<p>Great, thank you.</p>
<p>I like the current logo, but maybe we can switch to the horizontal logo, available at:<br>
<a href="https://www.slicer.org/wiki/Slicer3:Slicer3Brand#Full_color.2C_horizontal_format" class="onebox" target="_blank">https://www.slicer.org/wiki/Slicer3:Slicer3Brand#Full_color.2C_horizontal_format</a></p>

---

## Post #7 by @lassoan (2017-04-08 14:39 UTC)

<p>By default there is a large pinned message (Questions and comments are welcome here! (about usage, coding – or bugs)<br>
PLEASE NOTE: any data shared/linked on this site must be anonymized…).<br>
I find it too big (and took some time to realize I can remove it with the X button) and not all information is relevant here.<br>
Could you move the note about not include any patient data to the text that is displayed when you first post a message? Also, this note on patient data should go to a some permanent page that explains rule of what/how to post.</p>

---

## Post #8 by @ihnorton (2017-04-08 16:05 UTC)

<p>I added you Jc Steve to admin group, feel free to make changes (just don’t break login <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=5" title=":grinning:" class="emoji" alt=":grinning:">). I’ll be out until tonight and can make these changes later otherwise.</p>

---

## Post #9 by @fedorov (2017-04-08 19:08 UTC)

<p>Great job <a class="mention" href="/u/ihnorton">@ihnorton</a>!</p>
<p>Can we configure the colors for the topics? I would choose something more lively than black, brown and light brown!</p>

---

## Post #10 by @lassoan (2017-04-08 19:10 UTC)

<p>I can change the colors. Do you have any specific suggestion for colors?</p>

---

## Post #11 by @fedorov (2017-04-08 19:18 UTC)

<p>I don’t. R-G-B? I don’t know if we need a deep thought into it, just a bit more lively.</p>

---

## Post #12 by @fedorov (2017-04-08 19:34 UTC)

<p>Integration with github issues works!</p>
<p>Just a test:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/698" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/698" target="_blank">getbuildtest fails to configure/build kwwidgets</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:30:21" data-timezone="UTC">10:30PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:30:22" data-timezone="UTC">10:30PM - 12 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank">
          <img alt="slicerbot" src="https://avatars3.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">This issue was created automatically from an original Mantis Issue. Further discussion may take place here.</p>
</div>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #13 by @lassoan (2017-04-08 19:35 UTC)

<p>I’ve changed the colors to more lively ones.</p>

---

## Post #14 by @pieper (2017-04-08 20:24 UTC)

<p>For that “Slicer look” we could use the generic anatomy colors.</p>
<p><a href="https://www.slicer.org/wiki/Slicer3:2010_GenericAnatomyColors" class="onebox" target="_blank">https://www.slicer.org/wiki/Slicer3:2010_GenericAnatomyColors</a></p>
<p><a href="https://www.slicer.org/wiki/Slicer3:2010_Label_Colors" class="onebox" target="_blank">https://www.slicer.org/wiki/Slicer3:2010_Label_Colors</a></p>

---
