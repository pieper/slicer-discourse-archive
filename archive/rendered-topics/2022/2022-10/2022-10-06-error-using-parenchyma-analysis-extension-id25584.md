# Error Using Parenchyma Analysis Extension

**Topic ID**: 25584
**Date**: 2022-10-06
**URL**: https://discourse.slicer.org/t/error-using-parenchyma-analysis-extension/25584

---

## Post #1 by @yonnif (2022-10-06 19:04 UTC)

<p>Very new to 3dslicer (and the forum) so please forgive any naive misunderstandings here. I’ve looked and didn’t find an answer in the forums.</p>
<p>I’m using the parenchyma analysis extension to analyze a whole bunch of datasets. I’m able to make it work wonderfully for any of them (whichever I open first). However, when I try open a second acquistion to analyze, the “analysing…” button doesn’t change back to “analyse”. When I click on “analysing…” an error message says “Input Volumes do not have the same geometry.”</p>
<p>I’ve tried deleting all of the scenes and clearing the cache in the extension but I cannot get it to work without closing the program and then starting it back up every time I want to anlyze a different case.</p>
<p>Any suggestions?</p>
<p>Thanks,<br>
Yonni</p>

---

## Post #2 by @yonnif (2022-10-07 11:50 UTC)

<p>For anyone stumbling here at a later date, I’ve figured out the issue.</p>
<p>After analyzing, the “lung mask” drop down automatically toggles to “none”  but, in fact, it’s still selecting the last mask you made. You need to toggle the “lung mask” to a mask (any one will do) and then toggle it back to none before removing data from your workspace.</p>

---

## Post #3 by @rbumm (2022-10-07 14:27 UTC)

<p>Thank you for the report. <a class="mention" href="/u/paolozaffino">@PaoloZaffino</a> maybe you can look at this and push an update?</p>

---

## Post #4 by @PaoloZaffino (2022-10-07 14:34 UTC)

<p>Which extension are you using?</p>

---

## Post #5 by @yonnif (2022-10-07 14:47 UTC)

<p>The parenchyma analysis module of the Chest Imaging Platform extension</p>

---

## Post #6 by @PaoloZaffino (2022-10-07 14:54 UTC)

<p>Ah, ok, so it’s not the module I wrote.<br>
I think <a class="mention" href="/u/pnardelli">@PNardelli</a> can help.</p>
<p>Sorry, but I’m not familiar with this tool <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Paolo</p>

---

## Post #7 by @rbumm (2022-10-09 19:38 UTC)

<p><a class="mention" href="/u/yonnif">@yonnif</a> Most of the errors should now be resolved. Please update CIP within the next few days and test.</p>

---
