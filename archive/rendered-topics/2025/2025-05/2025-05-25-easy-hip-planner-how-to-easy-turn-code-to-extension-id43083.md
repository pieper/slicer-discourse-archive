# Easy Hip Planner - how to -easy- turn code to extension?

**Topic ID**: 43083
**Date**: 2025-05-25
**URL**: https://discourse.slicer.org/t/easy-hip-planner-how-to-easy-turn-code-to-extension/43083

---

## Post #1 by @Przemek_Czuma (2025-05-25 04:33 UTC)

<p>Here’s the situation: I built an application (a Python script) for simple total hip arthroplasty planning. I can’t code at all – I used a few LLMs to get it done. I was testing how far I could go with programming without knowing how to code… and I may have gone a bit overboard.</p>
<p>But the app works (see pic) and does what it’s supposed to do, so I’d like to share it publicly for possible testing, feedback, comments – or maybe, most importantly, because someone might find it useful.</p>
<p>The approach is a bit unusual – it mainly uses X-rays (2D), but there’s also a 3D planning option. That probably makes it one of the most versatile orthopedic scripts out there <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=14" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>
<p>I understand I should probably turn it into an extension probably with extension manager?<br>
The only issue is that the code is already 4500 lines long, which is more than even the best LLMs (like Gemini 2.5 or Sonnet 4) can reasonably handle. So if anyone’s willing to help – with advice or hands-on – I’d be grateful <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/763c3275ab6d0a39df147157460c6882934d67ac.jpeg" data-download-href="/uploads/short-url/gRXjq1AnIZFa4kXvUFC6fHlZ6MI.jpeg?dl=1" title="Zrzut ekranu 2025-05-24 214349" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/763c3275ab6d0a39df147157460c6882934d67ac_2_690x362.jpeg" alt="Zrzut ekranu 2025-05-24 214349" data-base62-sha1="gRXjq1AnIZFa4kXvUFC6fHlZ6MI" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/763c3275ab6d0a39df147157460c6882934d67ac_2_690x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/763c3275ab6d0a39df147157460c6882934d67ac_2_1035x543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/763c3275ab6d0a39df147157460c6882934d67ac_2_1380x724.jpeg 2x" data-dominant-color="737371"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Zrzut ekranu 2025-05-24 214349</span><span class="informations">1683×884 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @ungi (2025-05-25 13:34 UTC)

<p>Hi, sounds like you’ve had a lot of fun with this!<br>
I’ve been trying vibe coding Slicer modules in the past months, but none of the LLMs seem to have enough knowledge to completely develop and maintain a full working module. You need to keep correcting its mistakes and show good relevant examples for some steps.</p>
<p>I’d recommend that you make your code open source on GitHub now. If you add clear instructions and maybe a couple of test input too, somebody may get excited enough to help you add the Slicer extension.<br>
There is a Slicer project week in a month when a lot of the community members dedicate some time to helping others: <a href="https://projectweek.na-mic.org/PW43_2025_Montreal/" rel="noopener nofollow ugc">Welcome to the web page for the 43rd Project Week! | NA-MIC Project Weeks</a><br>
Even if you cannot attend in person, it may be a good idea to attend the preparation meetings to find somebody who could guide you a little bit. But I think eventually you will need to learn some programming skills.</p>
<p>About long files: If you break down your code into a few logical modules as separate python files, then none of them will be too long for LLM agents to edit. And use the LLMs built into Visual Studio Code. That’s more effective than the web browser-based interfaces of the LLMs. You can specify the context so it reads all open code files before starting to edit one.</p>
<p>Please keep us updated!</p>

---

## Post #3 by @Przemek_Czuma (2025-05-26 11:41 UTC)

<p>Honestly, realizing that segmentation can be used in an unconventional way – and that I could build something like this myself without actually knowing how to code – was a bit of a joyful moment. On the other hand, I’ve also learned how slow and detail-oriented coding can be… much respect.</p>
<p>I’ll definitely check out Project Week.</p>
<p>I’ve been using VS Code for some time already – it really makes things easier. Without it, I probably would’ve gotten stuck much earlier.</p>
<p>Following your advice, I published the code on GitHub (which wasn’t that straightforward either <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=14" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20">):<br>
<a href="https://github.com/P-Czum/EasyHipPlanner" rel="noopener nofollow ugc">https://github.com/P-Czum/EasyHipPlanner</a></p>
<p>All the best!</p>

---
