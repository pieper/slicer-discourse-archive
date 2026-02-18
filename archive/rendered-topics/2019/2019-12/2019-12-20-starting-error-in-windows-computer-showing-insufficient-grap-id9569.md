# Starting Error in Windows computer showing Insufficient Graphics capability

**Topic ID**: 9569
**Date**: 2019-12-20
**URL**: https://discourse.slicer.org/t/starting-error-in-windows-computer-showing-insufficient-graphics-capability/9569

---

## Post #1 by @muntahi398 (2019-12-20 10:11 UTC)

<p>Operating system: WIndows 10<br>
Slicer version: 4.11<br>
Expected behavior: Starting normally, as RTX2080 card is there<br>
Actual behavior: Shows error in starting saying Graphics capabilities of this computer:</p>
<p>Renderer does not support required OpenGL capabilities.</p>
<p>HI I am sometimes having problem  to run slicer, It says <strong>Graphics capability of this computer is not sufficient to run this application. The application most likely will not function properly.</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf569565651fd90d3bf1e843bb0b2f6ad45407dd.png" data-download-href="/uploads/short-url/riEHtRtqIDd0ZdEwRO2UE1aKxKB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf569565651fd90d3bf1e843bb0b2f6ad45407dd_2_517x500.png" alt="image" data-base62-sha1="riEHtRtqIDd0ZdEwRO2UE1aKxKB" width="517" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf569565651fd90d3bf1e843bb0b2f6ad45407dd_2_517x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf569565651fd90d3bf1e843bb0b2f6ad45407dd_2_775x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf569565651fd90d3bf1e843bb0b2f6ad45407dd.png 2x" data-dominant-color="DCEDF5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">789×763 50.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But this computer has a fairly strong GPU installed. I have checked and latest nvidia driver " NVIDIA game ready VErsion 441.66" is iinstalled in the computer.  But slicer sometimes runs without any problem, but sometimes it is showing this error. What might be the reason?</p>

---

## Post #2 by @pieper (2019-12-20 12:30 UTC)

<p>I get that message when using microsoft remote desktop, but not when I access the machine directly or use other remote desktop options.</p>

---

## Post #3 by @muntahi398 (2019-12-20 15:37 UTC)

<p>Wow, thanks a lot.<br>
Although it is strange, I find that is  the case for me too.<br>
Is there a  way to overcome this? except for using alternative software?</p>

---

## Post #4 by @lassoan (2019-12-20 15:44 UTC)

<p>On recent Windows 10 computers I find that remote desktop works well (does not have this OpenGL limitation as before). However, it may depend on your video card drivers, operating system edition and version and device management settings. If you have a monitor attached to the remote computer then you don’t need to use Windows Remote Desktop but you can use any third-party remote control applications (RealVNC, AnyDesk, Google Remote desktop are completely free or free for personal use; TeamViewer and LogMeIn might be somewhat more polished, but they are ridiculously expensive).</p>

---

## Post #5 by @pieper (2019-12-20 16:28 UTC)

<p>I use google remote desktop via chrome.  It’s free and works well for my (limited) purposes.</p>

---

## Post #6 by @muratmaga (2019-12-20 16:37 UTC)

<p>If remote desktop is a must and you use windows 10 both ends, you can use Quadro cards. Quadro’s new drivers seem to support H/W opengl through windows RDC (can’t speak for other clients though). It actually work quite well even with my 6 year old laptop that has a  K4100M (and couple other desktops that has more recent Quadro’s in them).</p>

---

## Post #7 by @lassoan (2019-12-20 16:48 UTC)

<p>Remote desktop GPU acceleration also works with recent (few-year-old) Intel graphics cards.</p>

---

## Post #8 by @muratmaga (2019-12-20 17:58 UTC)

<p>That interesting. For laptops both intel and geforce GPUs, then do you set the opengl GPU to integrated to work through RDP?</p>

---

## Post #9 by @lassoan (2019-12-20 18:32 UTC)

<p>I just know that between two Windows 10 computers that only have Intel integrated graphics, Slicer can be started via Windows RDP. It started to work a few years ago.</p>
<p>OpenGL3 support via RDP seems to be a Windows core feature, as it works on computers with Intel HD graphics and others reported that it works with AMD Radeon, too. I suspect that Nvidia intentionally downgrades OpenGL support for GeForce cards to encourage “professionals” to buy Quadro. Hopefully Nvidia will eventually give in.</p>

---

## Post #10 by @muratmaga (2019-12-20 20:41 UTC)

<p>I can confirm that in dual GPU laptop, the openGL warning disappears if the preferred GPU engine is set to integrated GPU in Nvidia control panel prior to the remote connection.</p>

---

## Post #11 by @muntahi398 (2019-12-23 09:32 UTC)

<p>Thanks everyone for their nice suggestions.<br>
Both my computers are  having windows 10. One AMD build with Radeon  8 in localwhereas Remote is having RTX2080 card. Drivers are updated. Unfortunately I cant change the hardwares for now.</p>
<p>As windows remote desktop is making issue, I have tried Google chrome Remote desktop and it seems to be  working for  now.</p>

---

## Post #12 by @lassoan (2021-10-12 01:52 UTC)

<p>Just in case you need to use a Windows computer via Remote Desktop - there is one more option: use a software renderer. It is easy to set up (copy Mesa OpenGL dlls into the bin folder of Slicer and set a few environment variables - see details <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#slicer-application-does-not-start">here</a>). It may not take advantage of the GPU for rendering, though, so it may not be an ideal solution.</p>

---
