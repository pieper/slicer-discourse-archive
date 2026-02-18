# Full screen issue with slicer on mac os 15.0.1

**Topic ID**: 39753
**Date**: 2024-10-18
**URL**: https://discourse.slicer.org/t/full-screen-issue-with-slicer-on-mac-os-15-0-1/39753

---

## Post #1 by @mohammed_alshakhas (2024-10-18 16:33 UTC)

<p>full screen issue with slicer on mac os 15.0.1. the right of screen is clipped in full screen . this is since i got new mac os 15</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/6936b2690bd10c79605579b28391bb5a573a0df8.jpeg" data-download-href="/uploads/short-url/f0LjXL6UcScvLVKmONIGUqBdFnq.jpeg?dl=1" title="Screenshot 2024-10-18 at 19.29.29" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/6936b2690bd10c79605579b28391bb5a573a0df8_2_690x448.jpeg" alt="Screenshot 2024-10-18 at 19.29.29" data-base62-sha1="f0LjXL6UcScvLVKmONIGUqBdFnq" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/6936b2690bd10c79605579b28391bb5a573a0df8_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/6936b2690bd10c79605579b28391bb5a573a0df8_2_1035x672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/6936b2690bd10c79605579b28391bb5a573a0df8_2_1380x896.jpeg 2x" data-dominant-color="353534"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-10-18 at 19.29.29</span><span class="informations">1920×1247 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-10-19 04:34 UTC)

<p>The content of the Slicer window juat does not fit on the screen. You can drag the vertical splitter between the module panel and the views to make a vit more space for the viewers. You can also try to force size constraints by exiting and entering maximized window state.</p>

---

## Post #3 by @mohammed_alshakhas (2024-10-19 05:47 UTC)

<p>this is new issue , never happened before  regardless of view im using . i think its related to new Mac Os. even in full screen it fits well then stretches out of screen which is very unusal behavior .</p>
<p>previosuly it fits ok then i drag vertical splitter ro make think even . now it is diffrent .<br>
just wanted to report it</p>

---

## Post #4 by @lassoan (2024-10-19 11:35 UTC)

<p>Could you take a screen capture video to illustrate what is happening exactly?</p>

---

## Post #5 by @mohammed_alshakhas (2024-10-20 09:35 UTC)

<p>i tried video but didn’t wok .  ill try taking another one</p>
<p>here is a screen shot in fullscreen mode , you can see cropped right side at the sagittal section</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4fbe56664fe70fc3bf07213b7993f7a980318f2.jpeg" data-download-href="/uploads/short-url/pP3D24KVUxftfO4h5K6lhTlv5f4.jpeg?dl=1" title="Screenshot 2024-10-20 at 12.30.23" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4fbe56664fe70fc3bf07213b7993f7a980318f2_2_690x448.jpeg" alt="Screenshot 2024-10-20 at 12.30.23" data-base62-sha1="pP3D24KVUxftfO4h5K6lhTlv5f4" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4fbe56664fe70fc3bf07213b7993f7a980318f2_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4fbe56664fe70fc3bf07213b7993f7a980318f2_2_1035x672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4fbe56664fe70fc3bf07213b7993f7a980318f2_2_1380x896.jpeg 2x" data-dominant-color="39393E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-10-20 at 12.30.23</span><span class="informations">1920×1247 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @mohammed_alshakhas (2024-10-20 09:40 UTC)

<p>i also noticed non reposviveness in many basic functions in fullscreen . like scrolling through slices or pressing any icon  . it stops responding until i exit fullscreen mode.</p>

---

## Post #7 by @lassoan (2024-10-20 12:53 UTC)

<p>These issues are probably due to bugs in macOS and/or Qt. They may be fixed in upcoming patches by Apple or maybe by Qt. Until then you may need to avoid using full-screen mode.</p>
<p>If you can send a screen capture video then it may help us identifying the underlying problem and figure out workarounds.</p>

---

## Post #8 by @mohammed_alshakhas (2024-10-21 12:31 UTC)

<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1DnKuqoNcopvXDQigqPl-FDkQMZos_Wp7/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1DnKuqoNcopvXDQigqPl-FDkQMZos_Wp7/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1DnKuqoNcopvXDQigqPl-FDkQMZos_Wp7/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1DnKuqoNcopvXDQigqPl-FDkQMZos_Wp7/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">Screen Recording 2024-10-21 at 15.16.19.mov</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>here is a video . this is similar but in this both sagittal and coronal is moving .<br>
the same issue but seems getting worse</p>
<p>hopefully im not wasting your time with these silliy issues</p>

---

## Post #9 by @lassoan (2024-10-21 13:23 UTC)

<p>Thanks for the video, it looks interesting. Can you check if it makes any difference if you deactivate the push-pin icon in the slice view controllers of the green and yellow slice views? Do you observe any issues if you are in different view layout, such as “3D Only”?</p>

---

## Post #10 by @jamesobutler (2024-10-21 15:42 UTC)

<p>I’ve tried running latest Slicer Preview on macOS 15.0.1 using a 14” MacBook Pro and did not see this issue when in full screen mode. This piece of hardware has a 3024x1964 display. I tried going into the same general registration module with three over three layout and everything was positioned appropriately.</p>
<p>I can observe a similar application cut off issue if I go into macOS Settings-&gt;Display and changed text size from “1512x982” aka Default on my system to a larger size that is “1352x878”.</p>
<p><a class="mention" href="/u/mohammed_alshakhas">@mohammed_alshakhas</a> what hardware are you using? And your display settings?</p>

---

## Post #11 by @mohammed_alshakhas (2024-10-26 04:19 UTC)

<p>sorry couldnt follow up the post got somehow busy</p>
<p>push pin on or off doesnt affect behavior . and i didnt notice the behavopr on single view like 3d or red only .</p>

---

## Post #12 by @mohammed_alshakhas (2024-10-26 04:21 UTC)

<p>im using mcbook pro M2pro 14 inch with default display setting  . the behavior is not only in 3 over 3 view . it happens with any multi view .</p>

---

## Post #13 by @muratmaga (2024-10-26 04:40 UTC)

<p>I am only seeing this issue in really low resolution on my M3 Pro 14". It starts to happen at the highlighted resolution and lower.</p>
<p>What is the resolution you are using? Did you try switching to a higher one?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/292563e9c35232679766e5b9b5f7608c6578b799.jpeg" data-download-href="/uploads/short-url/5RZGrCMXSMYv0zzqtXb616V6OVz.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/292563e9c35232679766e5b9b5f7608c6578b799_2_690x391.jpeg" alt="image" data-base62-sha1="5RZGrCMXSMYv0zzqtXb616V6OVz" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/292563e9c35232679766e5b9b5f7608c6578b799_2_690x391.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/292563e9c35232679766e5b9b5f7608c6578b799_2_1035x586.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/292563e9c35232679766e5b9b5f7608c6578b799_2_1380x782.jpeg 2x" data-dominant-color="9D9AA0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1089 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @mohammed_alshakhas (2024-10-26 04:46 UTC)

<p>im using this setting . i didnt change display setting , it started ti happen after latest update only</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92ef899f22f5c49a56e2119509d672c348683386.png" data-download-href="/uploads/short-url/kXQUTecNK6zbD7eQzgUyCYVZgUe.png?dl=1" title="Screenshot 2024-10-26 at 07.44.58" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92ef899f22f5c49a56e2119509d672c348683386_2_486x499.png" alt="Screenshot 2024-10-26 at 07.44.58" data-base62-sha1="kXQUTecNK6zbD7eQzgUyCYVZgUe" width="486" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92ef899f22f5c49a56e2119509d672c348683386_2_486x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92ef899f22f5c49a56e2119509d672c348683386_2_729x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92ef899f22f5c49a56e2119509d672c348683386.png 2x" data-dominant-color="323231"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-10-26 at 07.44.58</span><span class="informations">904×930 57 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @muratmaga (2024-10-26 04:46 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> we probably need to up the minimum required resolution:</p>
<p>Minimum required currently is 1024 by 768, which does not work on Mac properly.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#recommended-hardware-configuration" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#recommended-hardware-configuration</a></p>

---

## Post #16 by @muratmaga (2024-10-26 04:47 UTC)

<p>If you scroll down on this setting, and choose advanced, you can enable show resolutions as list:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca2bf24504f6705dc03c0af160ce2f3ee0df40fc.jpeg" data-download-href="/uploads/short-url/sQuBqz0EAdX7cnkWKaw67dmXtww.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca2bf24504f6705dc03c0af160ce2f3ee0df40fc_2_451x500.jpeg" alt="image" data-base62-sha1="sQuBqz0EAdX7cnkWKaw67dmXtww" width="451" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca2bf24504f6705dc03c0af160ce2f3ee0df40fc_2_451x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca2bf24504f6705dc03c0af160ce2f3ee0df40fc.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca2bf24504f6705dc03c0af160ce2f3ee0df40fc.jpeg 2x" data-dominant-color="D6D5D7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">670×742 73.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #17 by @mohammed_alshakhas (2024-10-26 04:49 UTC)

<p>im using default</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd0bfeb5eca306b31c894f01b1d73422f6f30f1a.png" data-download-href="/uploads/short-url/tfVzZzcs6znsBLp3Uda3sOeE2G6.png?dl=1" title="Screenshot 2024-10-26 at 07.49.02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd0bfeb5eca306b31c894f01b1d73422f6f30f1a_2_427x500.png" alt="Screenshot 2024-10-26 at 07.49.02" data-base62-sha1="tfVzZzcs6znsBLp3Uda3sOeE2G6" width="427" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd0bfeb5eca306b31c894f01b1d73422f6f30f1a_2_427x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd0bfeb5eca306b31c894f01b1d73422f6f30f1a_2_640x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd0bfeb5eca306b31c894f01b1d73422f6f30f1a_2_854x1000.png 2x" data-dominant-color="333232"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-10-26 at 07.49.02</span><span class="informations">916×1072 56 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #18 by @lassoan (2024-10-26 13:31 UTC)

<p>Indeed 1024x768 resolution was the most common in early 2000s, in 2011 it was overtaken by 1366x768, in 2020 it was overtaken by 1920x1080.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/700804e081833d1daf78b47e4cd298d5b6dd4fd0.jpeg" data-download-href="/uploads/short-url/fZ4EL9iz5DlO1OIVIzqWBExDmi4.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/700804e081833d1daf78b47e4cd298d5b6dd4fd0_2_690x443.jpeg" alt="image" data-base62-sha1="fZ4EL9iz5DlO1OIVIzqWBExDmi4" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/700804e081833d1daf78b47e4cd298d5b6dd4fd0_2_690x443.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/700804e081833d1daf78b47e4cd298d5b6dd4fd0_2_1035x664.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/700804e081833d1daf78b47e4cd298d5b6dd4fd0_2_1380x886.jpeg 2x" data-dominant-color="CAD3DD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1822×1170 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<em>(source: <a href="https://gs.statcounter.com/screen-resolution-stats/desktop/worldwide" class="inline-onebox">Desktop Screen Resolution Stats Worldwide | Statcounter Global Stats</a>)</em></p>
<p>Ten years ago, 95% met the 1024 minimum width, 768 minimum height requirements. Unfortunately, nowadays there is a wider variety of image resolutions around, so all that we can say is that screens have become wider (from 1.33 to 1.78) and maximum resolution increased. We should change the recommended resolution based on a wide-screen aspect ratio, but I don’t think we can require higher resolution than 1366x768. I’ve <a href="https://github.com/Slicer/Slicer/pull/8010">submitted a pull request</a> to update the documentation to 1366x768 minimum, 1920x1080 recommended.</p>
<hr>
<p>However, in layout problems the most important factor is text size, because that determines the size of most Qt widgets. Text size depends on:</p>
<ul>
<li>size of the font chosen in the Slicer application settings</li>
<li>font scaling setting of the operating system</li>
<li>chosen application language (for example, German translation tends to be longer than the English original)</li>
</ul>
<p>Font scaling is much more complex, as it is operating system dependent, and acceptable range depends on the screen size and eyesight of the user.</p>
<p>We could describe in the documentation how the text scaling may need to be adjusted if there are layout problems. We could also add more tests for detecting too wide widgets (current tests only check the module widget size in pixels and they don’t detect any issues now). But probably this new layout issue on macOS requires an investigation that focuses on this specific problem. It very well may be a macOS bug and we can live with workarounds (e.g., adjust application font size in Slicer application settings or don’t use maximized mode) until it fixed. If Apple does not provide a fix then Qt probably will, but we would need to update to Qt6 for that, which will take at least a couple of months.</p>

---

## Post #19 by @jamesobutler (2024-10-26 13:57 UTC)

<p>Yes so <a class="mention" href="/u/mohammed_alshakhas">@mohammed_alshakhas</a> ’s setting of Default at 1512x982 matches what was displayed on my 14” M1 MacBook Pro running macOS 15.0.1 where I did not observe the issues. So I’m not sure why that clipping is being observed. I only observed the issue when I set it to a lower resolution than that default.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://9to5mac.com/2021/10/19/new-macbook-pro-screen-resolution-options/">
  <header class="source">
      <img src="https://9to5mac.com/wp-content/uploads/sites/6/2019/10/cropped-cropped-mac1-1.png?w=32" class="site-icon" width="32" height="32">

      <a href="https://9to5mac.com/2021/10/19/new-macbook-pro-screen-resolution-options/" target="_blank" rel="noopener nofollow ugc" title="03:50PM - 19 October 2021">9to5Mac – 19 Oct 21</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://i0.wp.com/9to5mac.com/wp-content/uploads/sites/6/2021/10/macbook-pro-display.jpg?resize=1200%2C628&amp;quality=82&amp;strip=all&amp;ssl=1" class="thumbnail" width="690" height="361"></div>

<h3><a href="https://9to5mac.com/2021/10/19/new-macbook-pro-screen-resolution-options/" target="_blank" rel="noopener nofollow ugc">Here are the new MacBook Pro screen resolution options, native 2x Retina by...</a></h3>

  <p>The 14-inch and 16-inch MacBook Pro were announced to much fanfare yesterday, with one of the hero features being the...</p>

  <p>
    <span class="label1">Est. reading time: 3 minutes</span>
  </p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<blockquote>
<p>The higher-density panel on the new 14-inch MacBook Pro features a 3024 x 1964 native resolution, which will be presented to users as 1512 x 982@2x</p>
</blockquote>

---

## Post #20 by @mohammed_alshakhas (2024-10-30 19:20 UTC)

<p>the issue now is apparent  in all view not only in full screen.</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1mzI-Fh5ZXutC6uvDzUBO8ORmGNMPcpL5/view?usp=drive_link">
  <header class="source">

      <a href="https://drive.google.com/file/d/1mzI-Fh5ZXutC6uvDzUBO8ORmGNMPcpL5/view?usp=drive_link" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1mzI-Fh5ZXutC6uvDzUBO8ORmGNMPcpL5/view?usp=drive_link" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1mzI-Fh5ZXutC6uvDzUBO8ORmGNMPcpL5/view?usp=drive_link" target="_blank" rel="noopener nofollow ugc">Untitled.mov</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #21 by @jamesobutler (2024-10-30 19:33 UTC)

<p>Do you work with multiple monitors that are of different resolution than your laptop screen? Does it continue to happen if you close Slicer and reopen it?</p>

---

## Post #22 by @jamesobutler (2024-10-30 19:37 UTC)

<p><a class="mention" href="/u/mohammed_alshakhas">@mohammed_alshakhas</a> You also have a volume node with a long name as being displayed in the slice view controller pop-up widget. If you start Slicer fresh and then go to the Sample Data module and load MRHead does the issue happen?</p>

---

## Post #23 by @mohammed_alshakhas (2024-11-08 18:27 UTC)

<p>this is only on my laptop,  this is only happening recenly . my workflow has not changed in long time . the name is the name of the study , MRI tend to have long names</p>

---

## Post #24 by @Keegan_Paetzel (2024-11-08 19:14 UTC)

<p>hay i need to now about</p>

---

## Post #25 by @mohammed_alshakhas (2025-01-24 13:06 UTC)

<p>the problem is till ongoing . UI functionality is not working . many icons are not working in either small or full window . i need to toggle full and small window to get icon working fine</p>

---

## Post #26 by @jamesobutler (2025-01-24 19:22 UTC)

<p>Which icon buttons are not working? In the last video you linked it showed you pressing the Data module button in the top toolbar area but you did not have the module panel shown so there was no change.</p>
<p>To show/hide the module panel go to “View-&gt;Appearance-&gt;Show Module Panel”.</p>
<p>Slicer may have other issues with using the application and lower resolutions. I would suggest trying a higher resolution selection such as 1800x1169. Most users are probably using standard 1920x1080 displays at 100% scaling (no scale).</p>

---

## Post #27 by @mohammed_alshakhas (2025-01-27 15:08 UTC)

<p>Random icons each times . Not particularly a certain icon . But they all start to respond once I maximize or minimize screen .</p>

---

## Post #28 by @jamesobutler (2025-01-27 15:24 UTC)

<p>Can you provide a video of the icons not working? Last video you provided you clicked on a module icon but the module panel was not shown so it was expected for the button click to result in no change on screen.</p>

---

## Post #29 by @mohammed_alshakhas (2025-10-14 04:54 UTC)

<p>this issue continues till today and its reallt frustrating .</p>
<p>any change in focus now crops the application view . a double click on top bar fixed it but it needs to be done so frequently that i cant complete my work .</p>
<p>please give this issue some attention</p>
<p>thanks</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a961650e1eb5b91e37f70730f15faa64db47805.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21fb3dbbb38a4001a852ab1d4afaee9c07c8614a.png" data-video-base62-sha1="hurOk5n2kf33HDyiWiwvDKpERKZ.mp4">
  </div><p></p>

---

## Post #30 by @lassoan (2025-10-14 18:23 UTC)

<p>We expect that this Qt bug will disappear when we switch to Qt6. This should happen in the next few months.</p>
<p>Until then I would recommend to resize the application to fill your display instead of using the maximize button; and/or use larger or higher resolution screen or adjust font size or <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#runtime-environment-variables">Qt scale factor</a> to avoid the application running out of screen space.</p>

---

## Post #31 by @mohammed_alshakhas (2025-10-15 04:46 UTC)

<p>It’s happening now without full screen . In this video I’m not using full screen . I’m using double tab to fill maximize the app view .</p>
<p>But as you can see it’s impossible to work with this way</p>

---

## Post #32 by @lassoan (2025-10-15 04:52 UTC)

<p>The problem is that what you choose to see on screen physically cannot fit there with the current display size and settings. Qt tries to resolve the conflicting requirements, but on this macOS version it has some problems.</p>
<p>You can avoid the problem by adjusting your display or font settings so that everything fits on the screen. Alternatively, you can also undock the module panel so that it can overlap with the views. Then both the module panel and the views will have plenty of space - at the cost of a slight inconvenience that the module panel and the views may partially overlap.</p>

---
