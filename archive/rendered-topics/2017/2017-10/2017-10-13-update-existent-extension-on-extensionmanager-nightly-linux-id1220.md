---
topic_id: 1220
title: "Update Existent Extension On Extensionmanager Nightly Linux"
date: 2017-10-13
url: https://discourse.slicer.org/t/1220
---

# Update existent extension on ExtensionManager - Nightly - Linux

**Topic ID**: 1220
**Date**: 2017-10-13
**URL**: https://discourse.slicer.org/t/update-existent-extension-on-extensionmanager-nightly-linux/1220

---

## Post #1 by @acsenrafilho (2017-10-13 18:20 UTC)

<p>Hello, slicers!</p>
<p>I am sorry if this a naive question, but I’ve got stuck with my own<br>
extension updates inside ExtensionManager.</p>
<p>I have been developing new functionalities to my extension (AnomalousFilters<br>
<a href="https://github.com/Slicer/ExtensionsIndex/blob/master/AnomalousFiltersExtension.s4ext" rel="nofollow noopener">https://github.com/Slicer/ExtensionsIndex/blob/master/AnomalousFiltersExtension.s4ext</a>)<br>
and already pushed it to GitHub, in the extension repository (which has the<br>
newest git hag 7e30105<br>
<a href="https://github.com/CSIM-Toolkits/AnomalousFiltersExtension" rel="nofollow noopener">https://github.com/CSIM-Toolkits/AnomalousFiltersExtension</a>). As noticed,<br>
I have added the master branch as the target to the ExtensionIndex list, so<br>
I think that the new git hash will be used in the CDash building system.</p>
<p>In fact, the CDash informs the correct extension git hash (link<br>
<a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=Anom" rel="nofollow noopener">http://slicer.cdash.org/index.php?project=Slicer4&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=Anom</a>)<br>
and I’ve already tested the package generated there on Slicer (loading this<br>
compressed file in the Extension Manager “install from file” option). In<br>
this way, the extension works fine. However, when I look at the Extension<br>
Manager list, it continues showing a previous version of my extension (git<br>
hash b13577f).</p>
<p>What am I doing wrong here? How can I update my extension correctly to the<br>
Extension Index?</p>
<p>Best wishes<br>
Antonio</p>

---

## Post #2 by @jcfr (2017-10-13 19:17 UTC)

<p>Hi,</p>
<p>If you go to <code>Help -&gt; About</code>, which Slicer revision is shown ?</p>
<p>As illustrated <a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2017-10-13&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=Anom">here</a>, it should be <code>r26450</code>.</p>

---

## Post #3 by @jcfr (2017-10-13 19:40 UTC)

<p>After downloading the latest nightly build and installing the extension, it reports the expected information in the log:</p>
<pre><code class="lang-auto">"Retrieving extension metadata [ extensionId: 187822]" 
"Downloading extension [ itemId: 315191]" 
"Installed extension AnomalousFiltersExtension (187822) revision 7e30105" 
</code></pre>
<p>Git hash 7e30105 corresponds to the latest version of the extension packaged</p>

---

## Post #4 by @jcfr (2017-10-13 19:41 UTC)

<aside class="quote no-group" data-username="acsenrafilho" data-post="1" data-topic="1220">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/acsenrafilho/48/6217_2.png" class="avatar"> acsenrafilho:</div>
<blockquote>
<p>What am I doing wrong here?</p>
</blockquote>
</aside>
<p>May be you have additional path manually entered that are conflicting with the new extension ?</p>

---

## Post #5 by @acsenrafilho (2017-10-13 20:08 UTC)

<p>Hi jc,</p>
<p>Actually, my Slicer revision was r26398.<br>
Now, I have download the recent Slicer version that you commented and everything works fine.</p>
<p>But I still do not understand why this happened. Do I need to keep always the nightly version at the most recent revision?</p>

---

## Post #6 by @acsenrafilho (2017-10-13 20:12 UTC)

<p>In my machine, I have two version of Slicer. One to developing and another as a user (in order to have access to the extension manager).<br>
I only added a manual path to my extension to the developer version. I use the user-like Slicer just to check if the extension is normally available in the server.<br>
Do you think that it may cause a conflict?</p>

---

## Post #7 by @jcfr (2017-10-13 20:47 UTC)

<aside class="quote no-group" data-username="acsenrafilho" data-post="5" data-topic="1220">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/acsenrafilho/48/6217_2.png" class="avatar"> acsenrafilho:</div>
<blockquote>
<p>But I still do not understand why this happened. Do I need to keep always the nightly version at the most recent revision?</p>
</blockquote>
</aside>
<p>Since the API  and ABI of the nightly version of Slicer can change from one day to an other, we rebuild all extensions everyday. This effectively means that user using nightly build will have to download a recent nightly to get the latest version of the extension.</p>
<p>On the other hand, if the extension description file associated with release 4.6.2 is updated, user already having installed the stable version of slicer will be able to simply update the extension. This will work if the extension maintainer update the description file associated with that version.</p>
<p>For any given extension, being able to use the same code in both the last release and the nightly means that you consider API changes in the code … or maintain two version of the code.</p>
<p>Consider reading:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#What_is_the_Extensions_Index_.3F" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#What_is_the_Extensions_Index_.3F</a></p>
<p>and</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_often_extensions_are_uploaded_on_the_extensions_server_.3F" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_often_extensions_are_uploaded_on_the_extensions_server_.3F</a></p>
<aside class="quote no-group" data-username="acsenrafilho" data-post="6" data-topic="1220">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/acsenrafilho/48/6217_2.png" class="avatar"> acsenrafilho:</div>
<blockquote>
<p>I only added a manual path to my extension to the developer version. I use the user-like Slicer just to check if the extension is normally available in the server.</p>
<p>Do you think that it may cause a conflict?</p>
</blockquote>
</aside>
<p>No. Updating the module paths will only affect the revision and user specific settings.</p>
<p>I just updated the wiki to clarify: <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ApplicationSettings#Information_for_Advanced_Users" class="inline-onebox">Documentation/Nightly/SlicerApplication/ApplicationSettings - Slicer Wiki</a></p>

---
