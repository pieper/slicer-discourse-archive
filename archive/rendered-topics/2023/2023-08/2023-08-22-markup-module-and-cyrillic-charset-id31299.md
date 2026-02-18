# Markup module and Cyrillic charset

**Topic ID**: 31299
**Date**: 2023-08-22
**URL**: https://discourse.slicer.org/t/markup-module-and-cyrillic-charset/31299

---

## Post #1 by @Grigoriy_Postolskiy (2023-08-22 18:37 UTC)

<p>Hello! I tried to set a Cyrillic text as control point name in Markups module but this text didn’t visualize on the slice.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0dab053ff343b2ed9b4adb89172c7107f46db29c.png" data-download-href="/uploads/short-url/1WUCfdz8ORDHtnQQClqsrIwcBpq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0dab053ff343b2ed9b4adb89172c7107f46db29c_2_690x375.png" alt="image" data-base62-sha1="1WUCfdz8ORDHtnQQClqsrIwcBpq" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0dab053ff343b2ed9b4adb89172c7107f46db29c_2_690x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0dab053ff343b2ed9b4adb89172c7107f46db29c_2_1035x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0dab053ff343b2ed9b4adb89172c7107f46db29c_2_1380x750.png 2x" data-dominant-color="A3A4AE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1910×1039 81.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is it possible to visualize Cyrillic symbols on slices in 3D Slicer?</p>
<p>Regards, Grigoriy Postolskiy, software developer.</p>

---

## Post #2 by @muratmaga (2023-08-22 21:20 UTC)

<p>There has been a lot of improvement for localization since 5.0.3. Can you try with the latest stable (5.4.0) and report back.</p>

---

## Post #3 by @Grigoriy_Postolskiy (2023-08-23 08:57 UTC)

<p>The same situation with Slicer 5.4.0:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/778999914babf784dffc8347bac4f0f05aaf4e2c.png" data-download-href="/uploads/short-url/h3tCLQXXIr7k4hdxkh1BAUlC7ik.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/778999914babf784dffc8347bac4f0f05aaf4e2c_2_690x374.png" alt="image" data-base62-sha1="h3tCLQXXIr7k4hdxkh1BAUlC7ik" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/778999914babf784dffc8347bac4f0f05aaf4e2c_2_690x374.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/778999914babf784dffc8347bac4f0f05aaf4e2c_2_1035x561.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/778999914babf784dffc8347bac4f0f05aaf4e2c_2_1380x748.png 2x" data-dominant-color="7B7C83"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×1041 76.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2023-08-23 11:46 UTC)

<p>Slicer uses Qt for the UI, which is more internationalized.  The 3D and Slice views use VTK.  Perhaps you can investigate if VTK’s font rendering supports Cyrillic.  It’s possible we haven’t enabled it.</p>

---

## Post #5 by @lassoan (2023-08-24 08:10 UTC)

<p>The font file included with Slicer by default only supports a limited set of unicode characters. If you install <code>LanguagePacks</code> extension and you update any translations using <code>Language Tools</code> module then the module also installs the “Noto” font, which should display all Cyrillic characters correctly.</p>
<p>For example, with default font:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f6764585f9dca216153d8b4e113974876cb54ea.png" data-download-href="/uploads/short-url/bkreETWAkZcV0l29j2CJC54HYfg.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f6764585f9dca216153d8b4e113974876cb54ea_2_690x241.png" alt="image" data-base62-sha1="bkreETWAkZcV0l29j2CJC54HYfg" width="690" height="241" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f6764585f9dca216153d8b4e113974876cb54ea_2_690x241.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f6764585f9dca216153d8b4e113974876cb54ea_2_1035x361.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f6764585f9dca216153d8b4e113974876cb54ea_2_1380x482.png 2x" data-dominant-color="4E5160"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1977×691 56.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After Languate Tools module installed Noto font:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/decc365e1597f8c460b1ce4d197046fd658a0ef8.png" data-download-href="/uploads/short-url/vMXwknFmd7v2nfsR1WvEnrSI5PG.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/decc365e1597f8c460b1ce4d197046fd658a0ef8_2_690x203.png" alt="image" data-base62-sha1="vMXwknFmd7v2nfsR1WvEnrSI5PG" width="690" height="203" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/decc365e1597f8c460b1ce4d197046fd658a0ef8_2_690x203.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/decc365e1597f8c460b1ce4d197046fd658a0ef8_2_1035x304.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/decc365e1597f8c460b1ce4d197046fd658a0ef8_2_1380x406.png 2x" data-dominant-color="494850"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2056×607 62.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
