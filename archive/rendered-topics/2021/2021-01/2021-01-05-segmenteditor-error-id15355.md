---
topic_id: 15355
title: "Segmenteditor Error"
date: 2021-01-05
url: https://discourse.slicer.org/t/15355
---

# SegmentEditor error

**Topic ID**: 15355
**Date**: 2021-01-05
**URL**: https://discourse.slicer.org/t/segmenteditor-error/15355

---

## Post #1 by @mohsenp (2021-01-05 19:38 UTC)

<p>Operating system:<br>
Slicer version:Slicer 4.11.20200930<br>
Expected behavior:<br>
Actual behavior:</p>
<p>hi , I have a problem with segment editor module in 3d slicer .</p>
<p>Warning, the module  “SegmentEditor” has no widget representation<br>
Warning, there is no UI for the module “SegmentEditor”</p>
<p>can anybody help me ?</p>

---

## Post #2 by @lassoan (2021-01-05 21:47 UTC)

<p>Can you post the application log (menu: Help/Report a bug)?</p>

---

## Post #3 by @mohsenp (2021-01-06 18:21 UTC)

<p>Thank you for your prompt reply.</p>
<p>it’s too long and I don’t have permission to upload log file.</p>
<p>can i post it as text ?</p>

---

## Post #4 by @lassoan (2021-01-06 18:57 UTC)

<p>You can upload it anywhere (dropbox/onedrive/google drive) and post the link here.</p>

---

## Post #5 by @mohsenp (2021-01-06 19:27 UTC)

<aside class="onebox googledocs">
  <header class="source">
      <a href="https://docs.google.com/document/d/1dLYYDwA_gzqKSzIC41l4O_unY2EEMRJ5AjH2wuIgLTw/edit?usp=sharing" target="_blank" rel="noopener nofollow ugc">docs.google.com</a>
  </header>
  <article class="onebox-body">
    <a href="https://docs.google.com/document/d/1dLYYDwA_gzqKSzIC41l4O_unY2EEMRJ5AjH2wuIgLTw/edit?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-docs-logo"></span></a>

<h3><a href="https://docs.google.com/document/d/1dLYYDwA_gzqKSzIC41l4O_unY2EEMRJ5AjH2wuIgLTw/edit?usp=sharing" target="_blank" rel="noopener nofollow ugc">Untitled document</a></h3>

<p>[DEBUG][Qt] 06.01.2021 20:12:57 [] (unknown:0) - Session start time .......: 2021-01-06 20:12:57 [DEBUG][Qt] 06.01.2021 2[DEBUG][Qt] 06.01.2021 20:12:57 [] (unknown:0) - Session start time .......: 2021-01-06 20:12:57 [DEBUG][Qt] 06.01.2021 20:12:57...</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @lassoan (2021-01-06 19:30 UTC)

<p>Most likely the issue is that your username (<code>mohsen's PC</code>) contains a special character. Could you try to create a new user, install Slicer for that user, and see if it solves the problem?</p>

---

## Post #7 by @lassoan (2021-01-07 00:51 UTC)

<p>I can confirm that Slicer did not work if installed in a folder with <code>'</code> character in the name. The issue is fixed now, so Slicer Preview Release that you download tomorrow or later will work in your user folder. Until then, you can install Slicer into another folder that does not contain special characters in its path.</p>
<p>Nevertheless, for compatibility with various software in general, I would not recommend to avoid special characters (space, apostrophe, non-ascii characters) in your username.</p>

---

## Post #8 by @jamesobutler (2021-01-07 03:18 UTC)

<p>I remember I issued the bug report that resulted in <a href="https://github.com/Slicer/Slicer/commit/23ed57dacf4a5139f7fe2966009e0b89c054e42f" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix passing module paths containing single quote · Slicer/Slicer@23ed57d · GitHub</a> to solve the same type issue with a python extension not importing correctly since it was in a path where the username contained an apostrophe.</p>
<p>Would you be able to make sure there is a test case to maintain this fix as it relates to the Slicer install as well?</p>
<p>Considering Windows is heavily moving to user accounts that sign in using Microsoft Account credentials which sets their regular “First Name Last Name” as the username path, it will be likely that more users will have apostrophes in their username especially due to their last name. This being for many of Irish decent (eg O’Sullivan, O’Brien,  O’Conner,  O’Neill,  O’Reilly etc)</p>

---

## Post #9 by @mohsenp (2021-01-07 14:05 UTC)

<p>I installed Slicer into another folder and it works.</p>
<p>I am so very grateful for your time.</p>

---
