#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : svg.path
Version  : 3.0
Release  : 3
URL      : https://files.pythonhosted.org/packages/5a/7f/7a601000fc400024f76e660569b0b97f98787279daff079f0dbfa89293ba/svg.path-3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/5a/7f/7a601000fc400024f76e660569b0b97f98787279daff079f0dbfa89293ba/svg.path-3.0.tar.gz
Summary  : SVG path objects and parser
Group    : Development/Tools
License  : MIT
Requires: svg.path-python = %{version}-%{release}
Requires: svg.path-python3 = %{version}-%{release}
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : setuptools

%description
========
        
        svg.path is a collection of objects that implement the different path
        commands in SVG, and a parser for SVG path definitions.
        
        
        Usage
        -----
        
        There are four path segment objects, ``Line``, ``Arc``, ``CubicBezier`` and
        ``QuadraticBezier``.`There is also a ``Path`` object that acts as a
        collection of the path segment objects.
        
        All coordinate values for these classes are given as ``complex`` values,
        where the ``.real`` part represents the X coordinate, and the ``.imag`` part
        representes the Y coordinate.
        
            >>> from svg.path import Path, Line, Arc, CubicBezier, QuadraticBezier
        
        All of these objects have a ``.point()`` function which will return the
        coordinates of a point on the path, where the point is given as a floating
        point value where ``0.0`` is the start of the path and ``1.0`` is end end.
        
        You can calculate the length of a Path or it's segments with the
        ``.length()`` function. For CubicBezier and Arc segments this is done by
        geometric approximation and for this reason **may be very slow**. You can
        make it faster by passing in an ``error`` option to the method. If you
        don't pass in error, it defaults to ``1e-12``.
        
            >>> CubicBezier(300+100j, 100+100j, 200+200j, 200+300j).length(error=1e-5)
            297.2208145656899
        
        CubicBezier and Arc also has a ``min_depth`` option that specifies the
        minimum recursion depth. This is set to 5 by default, resulting in using a
        minimum of 32 segments for the calculation. Setting it to 0 is a bad idea for
        CubicBeziers, as they may become approximated to a straight line.
        
        ``Line.length()`` and ``QuadraticBezier.length()`` also takes these
        parameters, but they are ignored.
        
        CubicBezier and QuadraticBezier also has ``is_smooth_from(previous)``
        methods, that check if the segment is a "smooth" segment compared to the
        given segment.
        
        There is also a ``parse_path()`` function that will take an SVG path definition
        and return a ``Path`` object.
        
            >>> from svg.path import parse_path
            >>> parse_path('M 100 100 L 300 100')
            Path(Move(to=(100+100j)), Line(start=(100+100j), end=(300+100j)), closed=False)
        
        
        Classes
        .......
        
        These are the SVG path segment classes. See the `SVG specifications

%package python
Summary: python components for the svg.path package.
Group: Default
Requires: svg.path-python3 = %{version}-%{release}

%description python
python components for the svg.path package.


%package python3
Summary: python3 components for the svg.path package.
Group: Default
Requires: python3-core

%description python3
python3 components for the svg.path package.


%prep
%setup -q -n svg.path-3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1543775381
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
