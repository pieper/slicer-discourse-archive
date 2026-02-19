---
topic_id: 19485
title: "Create Slicer With Customized User Interface"
date: 2021-09-02
url: https://discourse.slicer.org/t/19485
---

# Create Slicer with customized user interface

**Topic ID**: 19485
**Date**: 2021-09-02
**URL**: https://discourse.slicer.org/t/create-slicer-with-customized-user-interface/19485

---

## Post #1 by @S_Arbabi (2021-09-02 07:48 UTC)

<p>This is great, how Slicer Custom App allows to create a customized slicer app based on the needs.<br>
I was wondering how much is it adjustable, for example I want to show the user a few drop-downs with patient name, and by just choosing one of the patients, image for that patient load and shows up. then by choosing another dropdown, different segmentations can be overlayed.<br>
Is that possible or the user should always browse files one by one?</p>
<p>Best</p>

---

## Post #2 by @lassoan (2021-09-02 15:27 UTC)

<p>Absolutely. You have full control over what you want to display and how.</p>
<aside class="quote no-group" data-username="S_Arbabi" data-post="1" data-topic="19485">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/dfb087/48.png" class="avatar"> S_Arbabi:</div>
<blockquote>
<p>I was wondering how much is it adjustable, for example I want to show the user a few drop-downs with patient name, and by just choosing one of the patients, image for that patient load and shows up. then by choosing another dropdown, different segmentations can be overlayed.<br>
Is that possible or the user should always browse files one by one?</p>
</blockquote>
</aside>
<p>This sounds all very easily doable. You can create a simple Python scripted module and set that as startup module in the Slicer.ini file. In your module you add those few comboboxes, tree views, etc. and hide all other standard user interface elements that you don’t need. Whenever the user makes a selection your module can load the corresponding data.</p>

---
