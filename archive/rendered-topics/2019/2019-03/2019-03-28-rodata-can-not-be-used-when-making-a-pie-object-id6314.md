# rodata can not be used when making a PIE object

**Topic ID**: 6314
**Date**: 2019-03-28
**URL**: https://discourse.slicer.org/t/rodata-can-not-be-used-when-making-a-pie-object/6314

---

## Post #1 by @Zhiy (2019-03-28 02:59 UTC)

<p>Dear all,<br>
Any one built Slicer with gcc/g++ 7.3 before. I am hitting errors like<br>
/usr/bin/ld: CMakeFiles/vtkParseJava.dir/vtkParseJava.c.o: relocation R_X86_64_32 against <code>.rodata' can not be used when making a PIE object; recompile with -fPIC /usr/bin/ld: ../../lib/libvtkWrappingTools-8.2.a(vtkParseMain.c.o): relocation R_X86_64_32 against</code>.rodata’ can not be used when making a PIE object; recompile with -fPIC<br>
/usr/bin/ld: …/…/lib/libvtkWrappingTools-8.2.a(vtkParseString.c.o): relocation R_X86_64_32S against symbol <code>parse_charbits' can not be used when making a PIE object; recompile with -fPIC /usr/bin/ld: ../../lib/libvtkWrappingTools-8.2.a(vtkParseHierarchy.c.o): relocation R_X86_64_32 against</code>.text’ can not be used when making a PIE object; recompile with -fPIC<br>
/usr/bin/ld: …/…/lib/libvtkWrappingTools-8.2.a(vtkParsePreprocess.c.o): relocation R_X86_64_32S against symbol <code>parse_charbits' can not be used when making a PIE object; recompile with -fPIC /usr/bin/ld: ../../lib/libvtkWrappingTools-8.2.a(vtkWrap.c.o): relocation R_X86_64_32 against</code>.rodata’ can not be used when making a PIE object; recompile with -fPIC<br>
/usr/bin/ld: …/…/lib/libvtkWrappingTools-8.2.a(vtkParseMerge.c.o): relocation R_X86_64_32 against `.rodata’ can not be used when making a PIE object; recompile with -fPIC</p>
<p>I am suspecting it’s caused by compilers version.</p>

---
