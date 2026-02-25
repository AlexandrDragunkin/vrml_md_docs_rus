# ![](../../pix/vrml97.gif)

# The Virtual Reality Modeling Language

# 1\. Scope

### ISO/IEC DIS 14772-1

#### 4 April 1997

### ![](../../pix/vrmlbar.gif)

## 1.0 Scope

The VRML specification defines a file format that integrates 3D
graphics and multimedia. Conceptually, each VRML file is a 3D
time-based space that contains graphic and aural objects that can be
dynamically modified through a variety of mechanisms. VRML defines a
primary set of objects and mechanisms that encourage composition,
encapsulation, and extension.

The semantics of VRML describe an abstract functional behaviour of
time-based, interactive 3D, multimedia worlds. VRML does not define
physical devices or any other implementation-dependent concepts (e.g.,
screen resolution and input devices). VRML is intended for a wide
variety of devices and applications, and provides wide latitude in
interpretation and implementation of the functionality. For example,
VRML does not assume the existence of a mouse or 2D display device.

Each VRML file:

1. implicitly establishes a world coordinate space for all objects defined
    in the file, as well as all objects recursively included by the file;

2. explicitly defines and composes a set of 3D and multimedia objects;

3. can specify hyperlinks to other files and applications;

4. can define object behaviours.


An important characteristic of VRML files is the ability to compose
files together through inclusion and to relate files together through
hyperlinking. For example, consider the file _earth.wrl_ which
specifies a world that contains a sphere representing the earth. This
file may also contain references to a variety of other VRML files
representing cities on the earth (e.g., file _paris.wrl)_. The
enclosing file, _earth.wrl_, defines the coordinate system that
all the cities reside in. Each city file defines the world coordinate
system that the city resides in but that becomes a local coordinate
system when contained by the earth file.

Hierarchical file inclusion enables the creation of arbitrarily large,
dynamic worlds. Therefore, VRML ensures that each file is completely
described by the objects and files contained within it and that the
effects of each file are strictly scoped by the file and the spatial
limits of the objects defined in the file. Otherwise, the accumulation
of files into larger worlds would produce unscalable results (as each
added world produces global effects on all other worlds). For example,
light sources have the potential of global effect since light energy
theoretically does not dissipate to zero. And, if the earth file
contains 100 city files each containing 100 lights each affecting all
objects in the world, the lighting calculations would quickly become
intractable. Therefore, in order to prevent global effects, light
source objects are scoped by either a maximum radius or by location
within the file.

Another essential characteristic of VRML is that it is intended to be
used in a distributed environment such as the World Wide Web. There are
various objects and mechanisms built into the language that support
multiple distributed files, including:

5. in-lining of other VRML files

6. hyperlinking to other files

7. using established Internet standards for other file formats

8. defining a compact syntax.


![](../../pix/vrmlbar.gif)

```
http://www.vrml.org/Specifications/VRML97/DIS/part1/scope.html

```

