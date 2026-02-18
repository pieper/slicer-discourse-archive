# Cancel CLI module running from a loadable scripted module through clicking the cancel button of qProgressDialog

**Topic ID**: 18330
**Date**: 2021-06-24
**URL**: https://discourse.slicer.org/t/cancel-cli-module-running-from-a-loadable-scripted-module-through-clicking-the-cancel-button-of-qprogressdialog/18330

---

## Post #1 by @bywbilly (2021-06-24 17:35 UTC)

<p>Hi,</p>
<p>I run a CLI module in the background in a customized loadable scripted module. And following here <a href="https://discourse.slicer.org/t/how-to-update-the-progress-bar-from-a-scripted-cli/3789/2" class="inline-onebox">How to update the progress bar from a scripted CLI - #2 by strider_hunter</a>, I create a progressDialog to show the progress.</p>
<p>Now I would like to know when the user clicks the cancel button of the progress bar so I can call cliNode.cancel() to kill the process of the CLI module. I checked the Status of clicking cancel but it is the same with interpreting the XML file (both are 2). So I am wondering how can I achieve this goal?</p>
<p>Thanks!</p>

---

## Post #2 by @rbumm (2021-06-24 18:52 UTC)

<p>Hi,</p>
<p>maybe this link helps:</p>
<aside class="quote quote-modified" data-post="2" data-topic="4343">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/use-progress-bar-from-python/4343/2">Use progress bar from python</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    You can use this convenience function for that 
 
 
See example of usage here
  </blockquote>
</aside>

<p>see the usage of <code>progress.wasCanceled</code></p>
<p>In my extension, I only use the naked progressbar without the Cancel button.</p>
<p>Best<br>
Rudolf</p>

---

## Post #3 by @bywbilly (2021-06-29 17:01 UTC)

<p>Hi Rudolf,</p>
<p>Thanks for the point. I didn’t make it work through wasCanceled. But I create another button for the GUI to cancel the process through cli_node.Cancel(), which works perfectly.</p>

---
