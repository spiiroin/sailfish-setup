Name:       sailfish-setup
Summary:    Sailfish Setup
Version:    0.1.0
Release:    1
Group:      System/Base
License:    Public Domain
Url:        https://github.com/sailfishos/sailfish-setup
Source0:    %{name}-%{version}.tar.bz2

Requires: setup
Requires(pre): setup
Requires(pre): /usr/bin/getent
Requires(pre): /usr/sbin/groupadd
Requires(pre): /usr/sbin/useradd
Recommends: hardware-adaptation-setup

%description
%{summary}.

%pre
groupadd -rf privileged || :
groupadd -rf sailfish-mdm || :
if ! getent passwd sailfish-mdm >/dev/null ; then
    useradd -r -g sailfish-mdm -G privileged -d / -s /sbin/nologin sailfish-mdm || :
fi
groupadd -rf sailfish-radio || :
groupadd -rf sailfish-actdead || :
if ! getent passwd sailfish-actdead >/dev/null ; then
    useradd -r -g sailfish-actdead -d / -s /sbin/nologin sailfish-actdead || :
fi

groupadd -rf sailfish-system || :
usermod -a -G sailfish-system nemo || :
usermod -a -G sailfish-system sailfish-mdm || :

groupadd -rf ssu || :

%files
%defattr(-,root,root,-)
