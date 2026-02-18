# Slicer 4.6.2 and missing DCMQI

**Topic ID**: 209
**Date**: 2017-04-27
**URL**: https://discourse.slicer.org/t/slicer-4-6-2-and-missing-dcmqi/209

---

## Post #1 by @finetjul (2017-04-27 11:28 UTC)

<p>Hi,</p>
<p>With Slicer 4.6.2 (downloaded on Windows from <a href="http://download.slicer.org/" rel="nofollow noopener">http://download.slicer.org/</a>) the extension DCMQI is not available from the Extension Manager.<br>
Is it a known issue ?</p>
<p>Multiple extensions seem to depend from it and they don’t properly load at startup.</p>
<p>Thanks,<br>
Julien.</p>

---

## Post #2 by @lassoan (2017-04-27 12:19 UTC)

<p>Does it work in the latest nightly version? Can you use that? I’m not sure if the team has the bandwidth to investigate issues on 4.6.2 version.</p>

---

## Post #3 by @finetjul (2017-04-27 12:40 UTC)

<p>Yes, it does work in the latest nightly version, thanks. And I can use it, no worries. I just wanted to let you guys know <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>J.</p>

---

## Post #4 by @fedorov (2017-04-27 15:25 UTC)

<p><a class="mention" href="/u/finetjul">@finetjul</a> I am not sure it has ever been available in  “stable” 4.6. To confirm this, I searched the git logs for the 4.6 branch, and didn’t find any indication it has ever been there.</p>
<p>We added DCMQI and QuantitativeReporting right before RSNA to the nightly release at the time, and that was after the “stable” was cut.</p>

---

## Post #5 by @finetjul (2017-04-27 15:35 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> It would be ok if DCMQI is not a Slicer 4.6.2 extension. The problem is that some other extension (e.g. DICOM QR) are available as Slicer 4.6.2 extensions but they depend on DCMQI: they fail to be installed/loaded because they need DCMQI.<br>
But maybe those extensions (e.g. DICOM QR) shouldn’t also be part of 4.6.2</p>

---

## Post #6 by @fedorov (2017-04-27 15:52 UTC)

<p>Hmmm … QuantitativeReporting should not be in 4.6 either - see <a href="https://github.com/slicer/extensionsindex/tree/4.6">https://github.com/slicer/extensionsindex/tree/4.6</a>. I don’t know why it is showing up for you!</p>

---

## Post #7 by @finetjul (2017-04-27 16:19 UTC)

<p>But there is Reporting.s4ext which seem to be related.</p>
<p>You can find below the content of the file <em>C:\Users\Julien\AppData\Roaming\NA-MIC\Extensions-25516\QuantitativeReporting\share\Slicer-4.6\QuantitativeReporting.s4ext</em> downloaded by the 4.6.2 extension manager</p>
<pre><code>#
# First token of each non-comment line is the keyword and the rest of the line
# (including spaces) is the value.
# - the value can be blank
#

# This is source code manager (i.e. svn)
scm git
scmurl https://github.com/QIICR/Reporting.git
scmrevision 135a06e

# list dependencies
# - These should be names of other modules that have .s4ext files
# - The dependencies will be built first
depends SlicerProstate DCMQI

# Inner build directory (default is ".")
build_subdirectory .

# homepage
homepage http://wiki.slicer.org/slicerWiki/index.php/Documentation/Nightly/Modules/QuantitativeReporting

# Firstname1 Lastname1 ([SubOrg1, ]Org1), Firstname2 Lastname2 ([SubOrg2, ]Org2)
# For example: Jane Roe (Superware), John Doe (Lab1, Nowhere), Joe Bloggs (Noware)
contributors Andrey Fedorov (SPL), Christian Herz (SPL), Csaba Pinter (Queen's), Andras Lasso (Queen's), Steve Pieper (SPL)

# Match category in the xml description of the module (where it shows up in Modules menu)
category Informatics

# url to icon (png, size 128x128 pixels)
iconurl https://www.slicer.org/w/images/3/30/QuantitativeReportingLogo.png

# Give people an idea what to expect from this code
#  - Is it just a test or something you stand behind?
status Work in progress

# One line stating what the module does
description Support of quantitative image reporting with DICOM

# Space separated list of urls
screenshoturls https://www.slicer.org/w/images/f/fe/QuantitativeReporting-screenshot.jpg

# 0 or 1: Define if the extension should be enabled after its installation.
enabled 1</code></pre>

---

## Post #8 by @fedorov (2017-04-27 16:31 UTC)

<p>You are right, this is super confusing - I do see both in the Extension Manager:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c493a544c7f41fc64380e1bcd745cc04e828bae.png" alt="image" data-base62-sha1="hJu5Y5MuqDukKNBS0pwoId2Mav4" width="555" height="382"></p>
<p>I don’t know how this happened, but at least at the moment, only Reporting.s4ext is present in the 4.6 branch of ExtensionsIndex, and it points to <a href="https://github.com/QIICR/Reporting.git" class="inline-onebox">GitHub - QIICR/QuantitativeReporting: Segmentation-based measurements with DICOM import and export of the results.</a>, and it does not have a DCMQI dependency: <a href="https://github.com/Slicer/ExtensionsIndex/blob/4.6/Reporting.s4ext" class="inline-onebox">ExtensionsIndex/Reporting.s4ext at 4.6 · Slicer/ExtensionsIndex · GitHub</a>.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> or anyone else who has the expertise in the workings of the extensions - how can we fix this? Why is QuantitativeReporting showing up in 4.6 extensions list, and (more importantly!) how to remove it from there?</p>

---

## Post #9 by @jcfr (2017-04-27 16:42 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="8" data-topic="209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>how can we fix this? Why is QuantitativeReporting showing up in 4.6 extensions list, and (more importantly!) how to remove it from there?</p>
</blockquote>
</aside>
<p>Removing a description file from the index does NOT automatically remove associated extensions from the Slicer appstore. It needs to be explicitly removed.</p>
<p>Should I remove the following Reporting extension with Slicer r25516 (4.6.2):</p>
<ul>
<li>25516-linux-amd64-Reporting-git9bd1c06-2016-11-24.tar.gz: <a href="http://slicer.kitware.com/midas3/item/262943">http://slicer.kitware.com/midas3/item/262943</a></li>
<li>25516-win-amd64-Reporting-git4d45ea1-2016-11-25.zip: <a href="http://slicer.kitware.com/midas3/item/263006">http://slicer.kitware.com/midas3/item/263006</a></li>
<li>25516-macosx-amd64-Reporting-git9bd1c06-2016-11-24.tar.gz: <a href="http://slicer.kitware.com/midas3/item/262790">http://slicer.kitware.com/midas3/item/262790</a></li>
</ul>
<p>Before doing so, do you want to archive the extension packages or upload them as release into the QuantitativeReporting project ?</p>

---

## Post #10 by @fedorov (2017-04-27 16:45 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> what should be removed is all versions of QuantitativeReporting extension from Slicer 4.6 “stable”. It depends on dcmqi and a version of dcmtk that are NOT available in 4.6.</p>
<p>I am not sure how it ended up there - it must be my fault adding it by mistake (or lack of thought), although I can’t find adding QuantitativeReporting in git history.</p>

---

## Post #11 by @jcfr (2017-04-27 17:03 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="10" data-topic="209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I am not sure how it ended up there</p>
</blockquote>
</aside>
<p>I think that the nightly build following the release was probably still based on the same revision.</p>
<p><a class="mention" href="/u/fedorov">@fedorov</a> That said, as soon as you confirm, I will remove these packages:</p>
<ul>
<li>25516-win-amd64-QuantitativeReporting-git135a06e-2016-12-19.zip: <a href="http://slicer.kitware.com/midas3/item/266138">http://slicer.kitware.com/midas3/item/266138</a></li>
<li>25516-linux-amd64-QuantitativeReporting-git962c032-2017-04-25.tar.gz: <a href="http://slicer.kitware.com/midas3/item/266136">http://slicer.kitware.com/midas3/item/266136</a></li>
<li>25516-macosx-amd64-QuantitativeReporting-git962c032-2017-04-25.tar.gz: <a href="http://slicer.kitware.com/midas3/item/266132">http://slicer.kitware.com/midas3/item/266132</a></li>
</ul>

---

## Post #12 by @fedorov (2017-04-27 17:57 UTC)

<p>JC, it is still a mystery for me how it happened, but yes - confirmed - please remove those packages!</p>

---

## Post #13 by @fedorov (2017-04-28 20:11 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> I see you removed the packages in question - thanks! - but when I start ExtensionManager from Slicer “stable” 4.6, I still see QuantitativeReporting in the search results. What else needs to be done to make it go away?</p>

---

## Post #14 by @jcfr (2017-04-28 21:00 UTC)

<p>Look like their was issue with the removal of metadata associated with items. I will manually update the database.</p>

---

## Post #15 by @fedorov (2017-05-01 13:35 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> please let me know if you updated the database - the extension still shows up in the ExtensionManager.</p>

---

## Post #16 by @jcfr (2017-10-24 05:20 UTC)

<p><s>To conclude, following the Slicer 4.8 release, <code>QuantitativeReporting</code> does not show up.</s></p>

---

## Post #17 by @fedorov (2017-10-24 11:58 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> you mean in 4.6.2?</p>

---

## Post #18 by @jcfr (2017-10-24 13:15 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> You are right. Since 4.8 has been released, we should be all set.</p>

---
