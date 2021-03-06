%global release_name juno

%global dist_eayunstack .eayunstack.dev

Name:		openstack-neutron
Version:	2014.2
Release:	28%{?dist_eayunstack}
Provides:	openstack-quantum = %{version}-%{release}
Obsoletes:	openstack-quantum < 2013.2-0.4.b3
Summary:	OpenStack Networking Service

Group:		Applications/System
License:	ASL 2.0
URL:		http://launchpad.net/neutron/

Source0:	http://launchpad.net/neutron/%{release_name}/%{version}/+download/neutron-%{version}.tar.gz
Source1:	neutron.logrotate
Source2:	neutron-sudoers
Source10:	neutron-server.service
Source11:	neutron-linuxbridge-agent.service
Source12:	neutron-openvswitch-agent.service
Source13:	neutron-ryu-agent.service
Source14:	neutron-nec-agent.service
Source15:	neutron-dhcp-agent.service
Source16:	neutron-l3-agent.service
Source17:	neutron-metadata-agent.service
Source18:	neutron-ovs-cleanup.service
Source19:	neutron-lbaas-agent.service
Source20:	neutron-mlnx-agent.service
Source21:	neutron-vpn-agent.service
Source22:	neutron-metering-agent.service
Source23:	neutron-sriov-nic-agent.service
Source24:	neutron-cisco-cfg-agent.service
Source25:	neutron-netns-cleanup.service
Source26:	neutron-netns-cleanup.init
Source27:	neutron-ovs-cleanup.init
Source28:	NetnsCleanup.ocf_ra
Source29:	OVSCleanup.ocf_ra
Source30:	NeutronScale.ocf_ra
Source31:	neutron-qos-agent.service

Source40:	neutron-dist.conf
#
# patches_base=+1
#
Patch0001: 0001-remove-runtime-dependency-on-pbr.patch
Patch0002: 0002-Drop-and-recreate-FK-if-adding-new-PK-to-routerl3bin.patch
Patch0003: 0003-Fix-hostname-regex-pattern.patch
Patch0004: 0004-Catch-exceptions-in-router-rescheduler.patch
Patch0005: 0005-Allow-to-specify-IP-address-of-floating-ip.patch
Patch0006: 0006-Allow-setting-a-tenant-router-s-external-IP.patch
Patch0007: 0007-Fix-Pluto-pidfile-deleting.patch
Patch0008: 0008-vpn-update-cmdline-options-and-config-for-ipsec.patch
Patch0009: 0009-vpn-do-preparing-work-before-running-ipsec.patch
Patch0010: 0010-vpnaas-add-ipsec-env-rootwrap-filter.patch
Patch0011: 0011-Use-stop-method-on-MessageHandlingServer.patch
Patch0012: 0012-merge-neutron-qos-feature.patch
Patch0013: 0013-different-qos-can-have-filters-with-the-same-prio.patch
Patch0014: 0014-fix-redmine-4163-queue-rate-error-in-qos_db.py.patch
Patch0015: 0015-Enable-to-specify-context-on-POST-requests-during-un.patch
Patch0016: 0016-Insert-validation-in-creating-updating-firewall.patch
Patch0017: 0017-Remove-port-from-ovsdb-after-its-deletion.patch
Patch0018: 0018-Don-t-delete-port-from-bridge-on-delete_port-event.patch
Patch0019: 0019-Check-for-removed-in-port_info-before-reference.patch
Patch0020: 0020-Refactor-retry-mechanism-used-in-some-DB-operations.patch
Patch0021: 0021-Randomize-tunnel-id-query-to-avoid-contention.patch
Patch0022: 0022-fix-redmine-4541.patch
Patch0023: 0023-Check-whether-target-s-tenant-is-the-same-with-qos.patch
Patch0024: 0024-Fix-wrong-class-inheritance.patch
Patch0025: 0025-Refine-database-relationships.patch
Patch0026: 0026-Implement-portmapping-feature.patch
Patch0027: 0027-Implement-firewall-target-routers.patch
Patch0028: 0028-Implement-PPTP-VPN-feature.patch
Patch0029: 0029-Catch-broad-exception-in-methods-used-in-FixedInterv.patch
Patch0030: 0030-Fix-redmine-issue-6277.patch
Patch0031: 0031-Allow-multiple-firewalls-for-a-tenant.patch
Patch0032: 0032-Fix-KeyError-when-updating-firewall.patch
Patch0033: 0033-Correctly-calculate-bandwidth-occupied-by-queues.patch
Patch0034: 0034-Metering-iptables-make-packets-travel-through-meteri.patch
Patch0035: 0035-Metering-iptables-fix-router-ext_dev-checker.patch
Patch0036: 0036-Qos-filter-s-prio-can-not-be-zero.patch
Patch0037: 0037-Give-a-default-selector-to-tc-filter.patch
Patch0038: 0038-qos_agent-don-t-add-tc-qdisc-when-device-is-not-read.patch
Patch0039: 0039-qos_agent-wrap-sfq-qdisc-under-the-htb-classes-16.patch
Patch0040: 0040-Pass-dhcp-authoritative-option-to-dnsmasq.patch
Patch0041: 0041-metering-fix-minor-error-in-agent.patch
Patch0042: 0042-Fix-metering-agent-failure-when-chain-missing.patch
Patch0043: 0043-Metering-filter-down-routers-when-syncing-data.patch
Patch0044: 0044-Metering-reconfigure-router-as-needed.patch
Patch0045: 0045-Check-whether-PPTP-VPN-service-already-exists-for-ro.patch
Patch0046: 0046-Lbaas-Enhancement-multi-VIP-bound-to-same-neutron-po.patch
Patch0047: 0047-Lbaas-Enhancement-Multi-VIP-bound-to-same-neutron-po.patch
Patch0048: 0048-Lbaas-Enable-create-and-remove-a-pool-to-from-lbaas-.patch
Patch0049: 0049-PPTP-VPN-set-provider-of-the-existing-vpnservices-40.patch
Patch0050: 0050-Enable-kill-pptpd-process-if-router-netns-does-not-e.patch
Patch0051: 0051-qos_agent-fix-pep8-warning.patch
Patch0052: 0052-db-move-target-checker-into-db.patch
Patch0053: 0053-qos_db-minor-style-fix.patch
Patch0054: 0054-Qos-queue-prio-could-not-be-null.patch
Patch0055: 0055-Correctly-set-queue-s-ceil-value.patch
Patch0056: 0056-Filters-give-default-value-to-src-and-dst-addr.patch
Patch0057: 0057-qos_agent-stateless-agent.patch
Patch0058: 0058-Fix-router-query-error-20.patch
Patch0059: 0059-Fix-cannot-delete-pptpd-process.patch
Patch0060: 0060-Fix-UnicodeEncodeError-generating-ipsec-configs-45.patch
Patch0061: 0061-Fix-error-when-using-fqdn-as-ipsec-peer-id-46.patch
Patch0062: 0062-VPNaaS-deprecate-two-dpd-actions-47.patch
Patch0063: 0063-Fix-error-when-checking-qos-target.patch
Patch0064: 0064-FWaaS-fix-port-range-validation-51.patch
Patch0065: 0065-Don-t-include-encryption-algorithm-in-phase2alg-for-.patch
Patch0066: 0066-Enable-usage-of-the-MTU-value-of-an-IPSec-connection.patch
Patch0067: 0067-Fix-ipsec-error-with-unsupport-provider-name.patch
Patch0068: 0068-VPNaaS-make-dpd_action-input-validation-work.patch
Patch0069: 0069-Fix-race-condition-when-auto-scheduling-routers.patch
Patch0070: 0070-Fix-error-when-invoke-firewall_deleted-rpc-function.patch
Patch0071: 0071-Enable-non-admin-user-to-operation-qos.patch
Patch0072: 0072-Only-send-effective-qos-configurations-to-agent.patch
Patch0073: 0073-Fix-process-logical-in-haproxy-get_stats.patch
Patch0074: 0074-Fix-ipset-can-t-be-destroyed-when-last-rule-is-delet.patch
Patch0075: 0075-Fix-the-last-qos-in-a-namespace-cannot-be-deleted.patch
Patch0076: 0076-metering-only-modify-related-iptables-parts.patch
Patch0077: 0077-Ovs-agent-adjust-internal-bridge-flow-priority.patch
Patch0078: 0078-openvswitch-agent-implement-EW-DVR-using-OpenFlow-ru.patch
Patch0079: 0079-Add-active-backup-model-for-lbaas.patch
Patch0080: 0080-iptables_firewall-add-firewall-rules-to-meter-instan.patch
Patch0081: 0081-Not-check-subnet-with-dhcp-disabled-when-get_isolate.patch
Patch0082: 0082-iptables_firewall-use-ipset-to-track-private-address.patch
Patch0083: 0083-Revert-metering-only-modify-related-iptables-parts.patch
Patch0084: 0084-Switches-metering-agent-to-stateless-iptables.patch
Patch0085: 0085-metering-extend-neutron-metering.patch
Patch0086: 0086-l3_agent-implement-EayunStack-floating-ip-mechanism.patch
Patch0087: 0087-Implement-lbaas-L7-policy-rule-model.patch
Patch0088: 0088-Implement-l7policy-for-lbaas-agent.patch


BuildArch:	noarch

BuildRequires:	python2-devel
BuildRequires:	python-d2to1
BuildRequires:	python-pbr
BuildRequires:	python-setuptools
BuildRequires:	systemd

Requires:	python-neutron = %{version}-%{release}
Requires:	openstack-utils

# dnsmasq is not a hard requirement, but is currently the only option
# when neutron-dhcp-agent is deployed.
Requires:	dnsmasq
Requires:	dnsmasq-utils

# radvd is not a hard requirement, but is currently the only option
# for IPv6 deployments.
Requires:	radvd

# conntrack is not a hard requirement, but is currently used by L3 agent
# to immediately drop connections after a floating IP is disassociated
Requires:	conntrack-tools

# keepalived is not a hard requirement, but is currently used by DVR L3
# agent
Requires:	keepalived

# those are not hard requirements, but are used to implement firewall
# drivers.
Requires:	ipset
Requires:	iptables

Requires(pre): shadow-utils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


%description
Neutron is a virtual network service for Openstack. Just like
OpenStack Nova provides an API to dynamically request and configure
virtual servers, Neutron provides an API to dynamically request and
configure virtual networks. These networks connect "interfaces" from
other OpenStack services (e.g., virtual NICs from Nova VMs). The
Neutron API supports extensions to provide advanced network
capabilities (e.g., QoS, ACLs, network monitoring, etc.)


%package -n python-neutron
Summary:	Neutron Python libraries
Group:		Applications/System

Provides:	python-quantum = %{version}-%{release}
Obsoletes:	python-quantum < 2013.2-0.4.b3

Requires:	MySQL-python
Requires:	python-alembic >= 0.6.4
Requires:	python-anyjson >= 0.3.3
Requires:	python-babel >= 1.3
Requires:	python-eventlet >= 0.15.1
Requires:	python-greenlet >= 0.3.2
Requires:	python-httplib2 >= 0.7.5
Requires:	python-iso8601 >= 0.1.9
Requires:	python-jinja2
Requires:	python-jsonrpclib
Requires:	python-keystoneclient >= 0.10.0
Requires:	python-keystonemiddleware >= 1.0.0
Requires:	python-netaddr >= 0.7.12
Requires:	python-neutronclient >= 2.3.6
Conflicts:	python-neutronclient >= 3
Requires:	python-novaclient >= 2.18.0
Requires:	python-oslo-config >= 2:1.4.0
Requires:	python-oslo-db >= 1.0.0
Requires:	python-oslo-messaging >= 1.4.0.0
Requires:	python-oslo-rootwrap >= 1.3.0.0
Requires:	python-paste
Requires:	python-paste-deploy >= 1.5.0
Requires:	python-qpid
Requires:	python-requests >= 1.2.1
Requires:	python-routes >= 1.12.3
Conflicts:	python-routes = 2.0
Requires:	python-sqlalchemy >= 0.9.7
Conflicts:	python-sqlalchemy >= 1.0
Requires:	python-stevedore >= 1.0.0
Requires:	python-six >= 1.7.0
Requires:	python-webob >= 1.2.3
Requires:	sudo
Requires:	libreswan



%description -n python-neutron
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the Neutron Python library.


%package bigswitch
Summary:	Neutron Big Switch plugin
Group:		Applications/System

Provides:	openstack-quantum-bigswitch = %{version}-%{release}
Obsoletes:	openstack-quantum-bigswitch < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description bigswitch
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the Neutron plugin that implements virtual
networks using the FloodLight Openflow Controller or the Big Switch
Networks Controller.


%package brocade
Summary:	Neutron Brocade plugin
Group:		Applications/System

Provides:	openstack-quantum-brocade = %{version}-%{release}
Obsoletes:	openstack-quantum-brocade < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description brocade
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the Neutron plugin that implements virtual
networks using Brocade VCS switches running NOS.


%package cisco
Summary:	Neutron Cisco plugin
Group:		Applications/System

Provides:	openstack-quantum-cisco = %{version}-%{release}
Obsoletes:	openstack-quantum-cisco < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description cisco
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the Neutron plugin that implements virtual
networks using Cisco UCS and Nexus.


%package embrane
Summary:	Neutron Embrane plugin
Group:		Applications/System

Requires:	openstack-neutron = %{version}-%{release}


%description embrane
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the Neutron plugin that implements virtual
L3-L7 network services using Embrane's heleos platform.


%package hyperv
Summary:	Neutron Hyper-V plugin
Group:		Applications/System

Provides:	openstack-quantum-hyperv = %{version}-%{release}
Obsoletes:	openstack-quantum-hyperv < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description hyperv
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the Neutron plugin that implements virtual
networks using Microsoft Hyper-V.


%package ibm
Summary:	Neutron IBM plugin
Group:		Applications/System

Requires:	openstack-neutron = %{version}-%{release}


%description ibm
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the Neutron plugin that implements virtual
networks from IBM.


%package linuxbridge
Summary:	Neutron linuxbridge plugin
Group:		Applications/System

Provides:	openstack-quantum-linuxbridge = %{version}-%{release}
Obsoletes:	openstack-quantum-linuxbridge < 2013.2-0.4.b3

Requires:	bridge-utils
Requires:	openstack-neutron = %{version}-%{release}


%description linuxbridge
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the Neutron plugin that implements virtual
networks as VLANs using Linux bridging.


%package mellanox
Summary:	Neutron Mellanox plugin
Group:		Applications/System

Provides:	openstack-quantum-mellanox = %{version}-%{release}
Obsoletes:	openstack-quantum-mellanox < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description mellanox
This plugin implements Neutron v2 APIs with support for Mellanox embedded
switch functionality as part of the VPI (Ethernet/InfiniBand) HCA.


%package metaplugin
Summary:	Neutron meta plugin
Group:		Applications/System

Provides:	openstack-quantum-metaplugin = %{version}-%{release}
Obsoletes:	openstack-quantum-metaplugin < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description metaplugin
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the Neutron plugin that implements virtual
networks using multiple other Neutron plugins.


%package midonet
Summary:	Neutron MidoNet plugin
Group:		Applications/System

Provides:	openstack-quantum-midonet = %{version}-%{release}
Obsoletes:	openstack-quantum-midonet < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description midonet
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the Neutron plugin that implements virtual
networks using MidoNet from Midokura.


%package ml2
Summary:	Neutron ML2 plugin
Group:		Applications/System

Provides:	openstack-quantum-ml2 = %{version}-%{release}
Obsoletes:	openstack-quantum-ml2 < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description ml2
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains a Neutron plugin that allows the use of drivers
to support separately extensible sets of network types and the mechanisms
for accessing those types.


%package nec
Summary:	Neutron NEC plugin
Group:		Applications/System

Provides:	openstack-quantum-nec = %{version}-%{release}
Obsoletes:	openstack-quantum-nec < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description nec
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the Neutron plugin that implements virtual
networks using the NEC OpenFlow controller.


%package nuage
Summary:	Neutron Nuage plugin
Group:		Applications/System

Requires:	openstack-neutron = %{version}-%{release}


%description nuage
This plugin implements Neutron v2 APIs with support for Nuage Networks
Virtual Service Platform (VSP).


%package ofagent
Summary:	Neutron ofagent plugin from ryu project
Group:		Applications/system

Requires:	openstack-neutron = %{version}-%{release}


%description ofagent
This plugin implements Neutron v2 APIs with support for the ryu ofagent
plugin.


%package oneconvergence-nvsd
Summary:	Neutron One Convergence NVSD plugin
Group:		Applications/System

Requires:	openstack-neutron = %{version}-%{release}


%description oneconvergence-nvsd
Neutron provides an API to dynamnically request and configure virtual
networks.

This package contains the Neutron plugin that implements virtual
networks using One Convergence NVSD


%package opencontrail
Summary:	Neutron OpenContrail plugin
Group:		Applications/system

Requires:	openstack-neutron = %{version}-%{release}


%description opencontrail
This plugin implements Neutron v2 APIs with support for the OpenContrail
plugin.


%package openvswitch
Summary:	Neutron openvswitch plugin
Group:		Applications/System

Provides:	openstack-quantum-openvswitch = %{version}-%{release}
Obsoletes:	openstack-quantum-openvswitch < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}
Requires:	openvswitch


%description openvswitch
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the Neutron plugin that implements virtual
networks using Open vSwitch.


%package plumgrid
Summary:	Neutron PLUMgrid plugin
Group:		Applications/System

Provides:	openstack-quantum-plumgrid = %{version}-%{release}
Obsoletes:	openstack-quantum-plumgrid < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description plumgrid
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the Neutron plugin that implements virtual
networks using the PLUMgrid platform.


%package ryu
Summary:	Neutron Ryu plugin
Group:		Applications/System

Provides:	openstack-quantum-ryu = %{version}-%{release}
Obsoletes:	openstack-quantum-ryu < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description ryu
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the Neutron plugin that implements virtual
networks using the Ryu Network Operating System.


%package vmware
Summary:	Neutron Nicira plugin
Group:		Applications/System

Provides:	openstack-neutron-nicira = %{version}-%{release}
Obsoletes:	openstack-neutron-nicira < 2014.1-0.5.b2

Requires:	openstack-neutron = %{version}-%{release}


%description vmware
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the Neutron plugin that implements virtual
networks using VMware NSX.


%package metering-agent
Summary:	Neutron bandwidth metering agent
Group:		Applications/System

Requires:	openstack-neutron = %{version}-%{release}

%description metering-agent
Neutron provides an API to measure bandwidth utilization

This package contains the Neutron agent responsible for generating bandwidth
utilization notifications.


%package sriov-nic-agent
Summary:	Neutron SR-IOV NIC agent
Group:		Applications/system

Requires:	openstack-neutron = %{version}-%{release}


%description sriov-nic-agent
Neutron allows to run virtual instances using SR-IOV NIC hardware

This package contains the Neutron agent to support advanced features of
SR-IOV network cards.


%package vpn-agent
Summary:	Neutron VPNaaS agent
Group:		Applications/System

Requires:	openstack-neutron = %{version}-%{release}

%description vpn-agent
Neutron provides an API to implement VPN as a service

This package contains the Neutron agent responsible for implementing VPNaaS with
IPSec.


%prep
%setup -q -n neutron-%{version}

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1
%patch0009 -p1
%patch0010 -p1
%patch0011 -p1
%patch0012 -p1
%patch0013 -p1
%patch0014 -p1
%patch0015 -p1
%patch0016 -p1
%patch0017 -p1
%patch0018 -p1
%patch0019 -p1
%patch0020 -p1
%patch0021 -p1
%patch0022 -p1
%patch0023 -p1
%patch0024 -p1
%patch0025 -p1
%patch0026 -p1
%patch0027 -p1
%patch0028 -p1
%patch0029 -p1
%patch0030 -p1
%patch0031 -p1
%patch0032 -p1
%patch0033 -p1
%patch0034 -p1
%patch0035 -p1
%patch0036 -p1
%patch0037 -p1
%patch0038 -p1
%patch0039 -p1
%patch0040 -p1
%patch0041 -p1
%patch0042 -p1
%patch0043 -p1
%patch0044 -p1
%patch0045 -p1
%patch0046 -p1
%patch0047 -p1
%patch0048 -p1
%patch0049 -p1
%patch0050 -p1
%patch0051 -p1
%patch0052 -p1
%patch0053 -p1
%patch0054 -p1
%patch0055 -p1
%patch0056 -p1
%patch0057 -p1
%patch0058 -p1
%patch0059 -p1
%patch0060 -p1
%patch0061 -p1
%patch0062 -p1
%patch0063 -p1
%patch0064 -p1
%patch0065 -p1
%patch0066 -p1
%patch0067 -p1
%patch0068 -p1
%patch0069 -p1
%patch0070 -p1
%patch0071 -p1
%patch0072 -p1
%patch0073 -p1
%patch0074 -p1
%patch0075 -p1
%patch0076 -p1
%patch0077 -p1
%patch0078 -p1
%patch0079 -p1
%patch0080 -p1
%patch0081 -p1
%patch0082 -p1
%patch0083 -p1
%patch0084 -p1
%patch0085 -p1
%patch0086 -p1
%patch0087 -p1
%patch0088 -p1

find neutron -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

sed -i 's/RPMVERSION/%{version}/; s/RPMRELEASE/%{release}/' neutron/version.py

# Ensure SOURCES.txt ends in a newline and if any patches have added files, append them to SOURCES.txt
[ -n "$(tail -c 1 < neutron.egg-info/SOURCES.txt)" ] && echo >> neutron.egg-info/SOURCES.txt
if ls %{_sourcedir}/*.patch >/dev/null 2>&1; then
  awk '/^new file/ {split(a,files," ");print substr(files[3],3)} {a = $0}' %{_sourcedir}/*.patch >> neutron.egg-info/SOURCES.txt
fi

# Let's handle dependencies ourseleves
rm -f requirements.txt

%build
%{__python} setup.py build

# Loop through values in neutron-dist.conf and make sure that the values
# are substituted into the neutron.conf as comments. Some of these values
# will have been uncommented as a way of upstream setting defaults outside
# of the code. For notification_driver, there are commented examples
# above uncommented settings, so this specifically skips those comments
# and instead comments out the actual settings and substitutes the
# correct default values.
while read name eq value; do
  test "$name" && test "$value" || continue
  if [ "$name" = "notification_driver" ]; then
    sed -ri "0,/^$name *=/{s!^$name *=.*!# $name = $value!}" etc/neutron.conf
  else
    sed -ri "0,/^(#)? *$name *=/{s!^(#)? *$name *=.*!# $name = $value!}" etc/neutron.conf
  fi
done < %{SOURCE40}

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Remove unused files
rm -rf %{buildroot}%{python_sitelib}/bin
rm -rf %{buildroot}%{python_sitelib}/doc
rm -rf %{buildroot}%{python_sitelib}/tools
rm -rf %{buildroot}%{python_sitelib}/neutron/tests
rm -rf %{buildroot}%{python_sitelib}/neutron/plugins/*/tests
rm -f %{buildroot}%{python_sitelib}/neutron/plugins/*/run_tests.*
rm %{buildroot}/usr/etc/init.d/neutron-server

# Move rootwrap files to proper location
install -d -m 755 %{buildroot}%{_datarootdir}/neutron/rootwrap
mv %{buildroot}/usr/etc/neutron/rootwrap.d/*.filters %{buildroot}%{_datarootdir}/neutron/rootwrap

# Move config files to proper location
install -d -m 755 %{buildroot}%{_sysconfdir}/neutron
mv %{buildroot}/usr/etc/neutron/* %{buildroot}%{_sysconfdir}/neutron
mv %{buildroot}%{_sysconfdir}/neutron/api-paste.ini %{buildroot}%{_datadir}/neutron/api-paste.ini
chmod 640  %{buildroot}%{_sysconfdir}/neutron/plugins/*/*.ini

# Install logrotate
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/openstack-neutron

# Install sudoers
install -p -D -m 440 %{SOURCE2} %{buildroot}%{_sysconfdir}/sudoers.d/neutron

# Install systemd units
install -p -D -m 644 %{SOURCE10} %{buildroot}%{_unitdir}/neutron-server.service
install -p -D -m 644 %{SOURCE11} %{buildroot}%{_unitdir}/neutron-linuxbridge-agent.service
install -p -D -m 644 %{SOURCE12} %{buildroot}%{_unitdir}/neutron-openvswitch-agent.service
install -p -D -m 644 %{SOURCE13} %{buildroot}%{_unitdir}/neutron-ryu-agent.service
install -p -D -m 644 %{SOURCE14} %{buildroot}%{_unitdir}/neutron-nec-agent.service
install -p -D -m 644 %{SOURCE15} %{buildroot}%{_unitdir}/neutron-dhcp-agent.service
install -p -D -m 644 %{SOURCE16} %{buildroot}%{_unitdir}/neutron-l3-agent.service
install -p -D -m 644 %{SOURCE17} %{buildroot}%{_unitdir}/neutron-metadata-agent.service
install -p -D -m 644 %{SOURCE18} %{buildroot}%{_unitdir}/neutron-ovs-cleanup.service
install -p -D -m 644 %{SOURCE19} %{buildroot}%{_unitdir}/neutron-lbaas-agent.service
install -p -D -m 644 %{SOURCE20} %{buildroot}%{_unitdir}/neutron-mlnx-agent.service
install -p -D -m 644 %{SOURCE21} %{buildroot}%{_unitdir}/neutron-vpn-agent.service
install -p -D -m 644 %{SOURCE22} %{buildroot}%{_unitdir}/neutron-metering-agent.service
install -p -D -m 644 %{SOURCE23} %{buildroot}%{_unitdir}/neutron-sriov-nic-agent.service
install -p -D -m 644 %{SOURCE24} %{buildroot}%{_unitdir}/neutron-cisco-cfg-agent.service
install -p -D -m 644 %{SOURCE25} %{buildroot}%{_unitdir}/neutron-netns-cleanup.service
install -p -D -m 644 %{SOURCE31} %{buildroot}%{_unitdir}/neutron-qos-agent.service

# Install scripts for pacemaker support
install -p -D -m 755 %{SOURCE26} %{buildroot}%{_prefix}/lib/ocf/lib/neutron/neutron-netns-cleanup
install -p -D -m 755 %{SOURCE27} %{buildroot}%{_prefix}/lib/ocf/lib/neutron/neutron-ovs-cleanup
install -p -D -m 755 %{SOURCE28} %{buildroot}%{_prefix}/lib/ocf/resource.d/neutron/NetnsCleanup
install -p -D -m 755 %{SOURCE29} %{buildroot}%{_prefix}/lib/ocf/resource.d/neutron/OVSCleanup
install -p -D -m 755 %{SOURCE30} %{buildroot}%{_prefix}/lib/ocf/resource.d/neutron/NeutronScale

# Setup directories
install -d -m 755 %{buildroot}%{_datadir}/neutron
install -d -m 755 %{buildroot}%{_sharedstatedir}/neutron
install -d -m 755 %{buildroot}%{_localstatedir}/log/neutron
install -d -m 755 %{buildroot}%{_localstatedir}/run/neutron

# Install dist conf
install -p -D -m 640 %{SOURCE40} %{buildroot}%{_datadir}/neutron/neutron-dist.conf

# Install version info file
cat > %{buildroot}%{_sysconfdir}/neutron/release <<EOF
[Neutron]
vendor = Fedora Project
product = OpenStack Neutron
package = %{release}
EOF

%pre
getent group neutron >/dev/null || groupadd -r neutron
getent passwd neutron >/dev/null || \
    useradd -r -g neutron -d %{_sharedstatedir}/neutron -s /sbin/nologin \
    -c "OpenStack Neutron Daemons" neutron
exit 0


%post
%systemd_post neutron-dhcp-agent.service
%systemd_post neutron-l3-agent.service
%systemd_post neutron-lbaas-agent.service
%systemd_post neutron-metadata-agent.service
%systemd_post neutron-server.service


%preun
%systemd_preun neutron-dhcp-agent.service
%systemd_preun neutron-l3-agent.service
%systemd_preun neutron-lbaas-agent.service
%systemd_preun neutron-metadata-agent.service
%systemd_preun neutron-server.service


%postun
%systemd_postun_with_restart neutron-dhcp-agent.service
%systemd_postun_with_restart neutron-l3-agent.service
%systemd_postun_with_restart neutron-lbaas-agent.service
%systemd_postun_with_restart neutron-metadata-agent.service
%systemd_postun_with_restart neutron-server.service


%preun cisco
%systemd_preun neutron-cisco-cfg-agent.service


%postun cisco
%systemd_postun_with_restart neutron-cisco-cfg-agent.service


%preun linuxbridge
%systemd_preun neutron-linuxbridge-agent.service


%postun linuxbridge
%systemd_postun_with_restart neutron-linuxbridge-agent.service


%preun mellanox
%systemd_preun neutron-mlnx-agent.service


%postun mellanox
%systemd_postun_with_restart neutron-mlnx-agent.service


%preun nec
%systemd_preun neutron-nec-agent.service


%postun nec
%systemd_postun_with_restart neutron-nec-agent.service


%preun openvswitch
%systemd_preun neutron-openvswitch-agent.service


%postun openvswitch
%systemd_postun_with_restart neutron-openvswitch-agent.service


%preun ryu
%systemd_preun neutron-ryu-agent.service


%postun ryu
%systemd_postun_with_restart neutron-ryu-agent.service


%preun metering-agent
%systemd_preun neutron-metering-agent.service


%postun metering-agent
%systemd_postun_with_restart neutron-metering-agent.service


%preun sriov-nic-agent
%systemd_preun neutron-sriov-nic-agent.service


%postun sriov-nic-agent
%systemd_postun_with_restart neutron-sriov-nic-agent.service


%preun vpn-agent
%systemd_preun neutron-vpn-agent.service


%postun vpn-agent
%systemd_postun_with_restart neutron-vpn-agent.service


%files
%doc LICENSE
%doc README.rst

%{_bindir}/neutron-db-manage
%{_bindir}/neutron-debug
%{_bindir}/neutron-dhcp-agent
%{_bindir}/neutron-get-htb-conf
%{_bindir}/neutron-l3-agent
%{_bindir}/neutron-lbaas-agent
%{_bindir}/neutron-metadata-agent
%{_bindir}/neutron-netns-cleanup
%{_bindir}/neutron-ns-metadata-proxy
%{_bindir}/neutron-ovs-cleanup
%{_bindir}/neutron-qos-agent
%{_bindir}/neutron-rootwrap
%{_bindir}/neutron-rootwrap-xen-dom0
%{_bindir}/neutron-sanity-check
%{_bindir}/neutron-server
%{_bindir}/neutron-usage-audit

%{_prefix}/lib/ocf/lib/neutron/neutron-netns-cleanup
%{_prefix}/lib/ocf/lib/neutron/neutron-ovs-cleanup
%{_prefix}/lib/ocf/resource.d/neutron/NetnsCleanup
%{_prefix}/lib/ocf/resource.d/neutron/OVSCleanup
%{_prefix}/lib/ocf/resource.d/neutron/NeutronScale

%{_unitdir}/neutron-dhcp-agent.service
%{_unitdir}/neutron-l3-agent.service
%{_unitdir}/neutron-lbaas-agent.service
%{_unitdir}/neutron-metadata-agent.service
%{_unitdir}/neutron-server.service
%{_unitdir}/neutron-netns-cleanup.service
%{_unitdir}/neutron-ovs-cleanup.service
%{_unitdir}/neutron-qos-agent.service
%dir %{_sysconfdir}/neutron
%{_sysconfdir}/neutron/release
%attr(-, root, neutron) %{_datadir}/neutron/neutron-dist.conf
%attr(-, root, neutron) %{_datadir}/neutron/api-paste.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/dhcp_agent.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/fwaas_driver.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/l3_agent.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/metadata_agent.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/lbaas_agent.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/policy.json
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/neutron.conf
%config(noreplace) %{_sysconfdir}/neutron/rootwrap.conf
%dir %{_sysconfdir}/neutron/plugins
%config(noreplace) %{_sysconfdir}/logrotate.d/*
%config %{_sysconfdir}/sudoers.d/neutron
%dir %attr(0755, neutron, neutron) %{_sharedstatedir}/neutron
%dir %attr(0750, neutron, neutron) %{_localstatedir}/log/neutron
%dir %{_datarootdir}/neutron
%dir %{_datarootdir}/neutron/rootwrap
%{_datarootdir}/neutron/rootwrap/debug.filters
%{_datarootdir}/neutron/rootwrap/dhcp.filters
%{_datarootdir}/neutron/rootwrap/ipset-firewall.filters
%{_datarootdir}/neutron/rootwrap/iptables-firewall.filters
%{_datarootdir}/neutron/rootwrap/l3.filters
%{_datarootdir}/neutron/rootwrap/lbaas-haproxy.filters
%{_datarootdir}/neutron/rootwrap/qos.filters


%files -n python-neutron
%doc LICENSE
%doc README.rst
%{python_sitelib}/neutron
%{python_sitelib}/neutron-%%{version}*.egg-info


%files bigswitch
%doc LICENSE
%doc neutron/plugins/bigswitch/README
%{_bindir}/neutron-restproxy-agent
%dir %{_sysconfdir}/neutron/plugins/bigswitch
%{_sysconfdir}/neutron/plugins/bigswitch/ssl
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/bigswitch/*.ini


%files brocade
%doc LICENSE
%doc neutron/plugins/brocade/README.md
%dir %{_sysconfdir}/neutron/plugins/brocade
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/brocade/*.ini


%files cisco
%doc LICENSE
%doc neutron/plugins/cisco/README
%{_bindir}/neutron-cisco-cfg-agent
%{_unitdir}/neutron-cisco-cfg-agent.service
%dir %{_sysconfdir}/neutron/plugins/cisco
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/cisco/*.ini


%files embrane
%doc LICENSE
%doc neutron/plugins/embrane/README
%dir %{_sysconfdir}/neutron/plugins/embrane
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/embrane/*.ini


%files hyperv
%doc LICENSE
#%doc neutron/plugins/hyperv/README
%{_bindir}/neutron-hyperv-agent
%dir %{_sysconfdir}/neutron/plugins/hyperv
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/hyperv/*.ini


%files ibm
%doc LICENSE
%{_bindir}/neutron-ibm-agent
%doc neutron/plugins/ibm/README
%dir %{_sysconfdir}/neutron/plugins/ibm
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/ibm/*.ini


%files linuxbridge
%doc LICENSE
%doc neutron/plugins/linuxbridge/README
%{_bindir}/neutron-linuxbridge-agent
%{_unitdir}/neutron-linuxbridge-agent.service
%{_datarootdir}/neutron/rootwrap/linuxbridge-plugin.filters
%dir %{_sysconfdir}/neutron/plugins/linuxbridge
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/linuxbridge/*.ini


%files mellanox
%doc LICENSE
%doc neutron/plugins/mlnx/README
%{_bindir}/neutron-mlnx-agent
%{_unitdir}/neutron-mlnx-agent.service
%dir %{_sysconfdir}/neutron/plugins/mlnx
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/mlnx/*.ini


%files metaplugin
%doc LICENSE
%doc neutron/plugins/metaplugin/README
%dir %{_sysconfdir}/neutron/plugins/metaplugin
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/metaplugin/*.ini


%files midonet
%doc LICENSE
#%doc neutron/plugins/midonet/README
%dir %{_sysconfdir}/neutron/plugins/midonet
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/midonet/*.ini


%files ml2
%doc LICENSE
%doc neutron/plugins/ml2/README
%dir %{_sysconfdir}/neutron/plugins/ml2
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/ml2/*.ini


%files nec
%doc LICENSE
%doc neutron/plugins/nec/README
%{_bindir}/neutron-nec-agent
%{_unitdir}/neutron-nec-agent.service
%{_datarootdir}/neutron/rootwrap/nec-plugin.filters
%dir %{_sysconfdir}/neutron/plugins/nec
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/nec/*.ini


%files nuage
%doc LICENSE
%{python_sitelib}/neutron/plugins/nuage
%dir %{_sysconfdir}/neutron/plugins/nuage
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/nuage/*.ini


%files ofagent
%doc LICENSE
%doc neutron/plugins/ofagent/README
%{_bindir}/neutron-ofagent-agent


%files oneconvergence-nvsd
%doc LICENSE
%doc neutron/plugins/oneconvergence/README
%dir %{_sysconfdir}/neutron/plugins/oneconvergence
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/oneconvergence/*.ini
%{_bindir}/neutron-nvsd-agent


%files opencontrail
%doc LICENSE
#%doc neutron/plugins/opencontrail/README
%dir %{_sysconfdir}/neutron/plugins/opencontrail
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/opencontrail/*.ini


%files openvswitch
%doc LICENSE
%doc neutron/plugins/openvswitch/README
%{_bindir}/neutron-openvswitch-agent
%{_unitdir}/neutron-openvswitch-agent.service
%{_datarootdir}/neutron/rootwrap/openvswitch-plugin.filters
%dir %{_sysconfdir}/neutron/plugins/openvswitch
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/openvswitch/*.ini


%files plumgrid
%doc LICENSE
%doc neutron/plugins/plumgrid/README
%dir %{_sysconfdir}/neutron/plugins/plumgrid
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/plumgrid/*.ini


%files ryu
%doc LICENSE
%doc neutron/plugins/ryu/README
%{_bindir}/neutron-ryu-agent
%{_unitdir}/neutron-ryu-agent.service
%{_datarootdir}/neutron/rootwrap/ryu-plugin.filters
%dir %{_sysconfdir}/neutron/plugins/ryu
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/ryu/*.ini


%files vmware
%doc LICENSE
%{_bindir}/neutron-check-nsx-config
%{_bindir}/neutron-nsx-manage
%dir %{_sysconfdir}/neutron/plugins/vmware
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/vmware/*.ini


%files metering-agent
%doc LICENSE
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/metering_agent.ini
%{_unitdir}/neutron-metering-agent.service
%{_bindir}/neutron-metering-agent


%files sriov-nic-agent
%doc LICENSE
%{_unitdir}/neutron-sriov-nic-agent.service
%{_bindir}/neutron-sriov-nic-agent


%files vpn-agent
%doc LICENSE
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/vpn_agent.ini
%{_unitdir}/neutron-vpn-agent.service
%{_bindir}/neutron-vpn-agent
%{_datarootdir}/neutron/rootwrap/vpnaas.filters


%changelog
* Mon Mar 06 2017 Xu Meihong <meihong.xu@eayun.com> 2014.2-28.eayunstack.1.1
- add patch 0077-0078 from github pull request #65 (redmine#9118)
- add patch 0079 from github pull request #69 (redmine#9249)
- add patch 0080 from github pull request #66 (redmine#9154)
- add patch 0081 from github pull request #71 (redmine#9433)
- add patch 0082 from github pull request #70 (redmine#9400)
- add patch 0083-0085 from github pull request #72 (redmine#9467)
- add patch 0086 from github pull request #74 (redmine#9517)
- add patch 0087 from github pull request #73 (redmine#9404)
- add patch 0088 from github pull request #73 (redmine#9518)

* Mon Nov 28 2016 Xu Meihong <meihong.xu@eayun.com> 2014.2-27.eayunstack.1.1
- add patch 0076 from github pull request #64 (redmine#8984)

* Fri Nov 11 2016 Xu Meihong <meihong.xu@eayun.com> 2014.2-26.eayunstack.1.1
- add patch 0074 from github pull request #61 (redmine#8916)
- add patch 0075 from neutron-qos github pull request #23 (redmine#8954)

* Wed Nov 02 2016 Xu Meihong <meihong.xu@eayun.com> 2014.2-25.eayunstack.1.1
- add patch 0065 from github pull request #52 (redmine#8761)
- add patch 0066 from github pull request #53 (redmine#8765)
- add patch 0067 from github pull request #54 (redmine#7730)
- add patch 0068 from github pull request #55 (redmine#8878)
- add patch 0069 from github pull request #56 (redmine#8685)
- add patch 0070 from github pull request #57 (redmine#8884)
- add patch 0071 from github pull request #58 (redmine#8823)
- add patch 0072 from neutron-qos github pull request #22 (redmine#8886)
- add patch 0073 from github pull request #59 (redmine#7735)

* Mon Oct 17 2016 Xu Meihong <meihong.xu@eayun.com> 2014.2-24.eayunstack.1.1
- add patch 0063 from neutron-qos github pull request #21 (redmine#8579)
- add patch 0064 from github pull request #51 (redmine#8601)

* Fri Sep 30 2016 Xu Meihong <meihong.xu@eayun.com> 2014.2-23.eayunstack.1.1
- add patch 0058 from neutron-qos github pull request #20
- add patch 0059 from github pull request #44 (redmine#7991)
- add patch 0060 from github pull request #45 (redmine#8078)
- add patch 0061 from github pull request #46 (redmine#8135)
- add patch 0062 from github pull request #47 (redmine#8272)

* Thu Aug 25 2016 Xu Meihong <meihong.xu@eayun.com> 2014.2-22.eayunstack.1.1
- add patch 0049 from github pull request #40 (redmine#7693)
- add patch 0050 from github pull request #41 (redmine#7694)
- add patch 0051-0057 from neutron-qos github pull request #19 (redmine#7659)

* Tue Jul 26 2016 Xu Meihong <meihong.xu@eayun.com> 2014.2-21.eayunstack.1.1
- add patch 0034 from github pull request #26 (redmine#6468)
- add patch 0035 from github pull request #27 (redmine#6469)
- add patch 0036 from neutron-qos github pull request #13 (redmine#6407)
- add patch 0037 from neutron-qos github pull request #14 (redmine#6406)
- add patch 0038 from neutron-qos github pull request #15 (redmine#6163)
- add patch 0039 from neutron-qos github pull request #16 (redmine#7265)
- add patch 0040 from github pull request #30 (redmine#7371)
- add patch 0041 from github pull request #32 (redmine#7375)
- add patch 0042-0044 from github pull request #31 (redmine#7372)
- add patch 0045 from github pull request #33 (redmine#7450)
- add patch 0046 from github pull request #38 (partial, redmine#7412)
- add patch 0047 from github pull request #36 (redmine#7412)
- add patch 0048 from github pull request #39 (redmine#7543)

* Mon Mar 14 2016 Xu Meihong <meihong.xu@eayun.com> 2014.2-20.eayunstack.1.1
- add patch 0030 from github pull request #22 (redmine#6277)
- add patch 0031 from github pull request #23 (redmine#6329)
- add patch 0032 from github pull request #24 (redmine#6332)
- add patch 0033 from github pull request #25 (redmine#5965)

* Mon Dec 14 2015 Xu Meihong <meihong.xu@eayun.com> 2014.2-19.eayunstack.1.1
- add patch 0026 from github pull request #10, #16 (redemine#4543)
- add patch 0027 from github pull request #11, #19 (redemine#4674)
- add patch 0028 from github pull request #15, #18, #20
- add patch 0029 from github pull request #21

* Fri Dec 11 2015 Xu Meihong <meihong.xu@eayun.com> 2014.2-18.eayunstack.1.0.1
- add patch 0015 and 0016 from github pull request #12 (redemine#5360)
- add patch 0017-0019 from github pull request #13 (redmine#5500)
- add patch 0020-0021 from github pull request #14 (redmine#5504)
- add patch 0022 from neutron-qos github pull request #7 (redmine#4541)
- add patch 0023 from neutron-qos github pull request #8 (redmine#4542)
- add patch 0024 from neutron-qos github pull request #9
- add patch 0025 from neutron-qos github pull request #11

* Tue Jun 30 2015 Xu Meihong <meihong.xu@eayun.com> 2014.2-17.eayunstack.1.0
- remove Revert-Fix-direction-problem-when-target_type-is-por.patch

* Mon Jun 29 2015 Xu Meihong <meihong.xu@eayun.com> 2014.2-16.eayunstack.1.0
- add 0013-different-qos-can-have-filters-with-the-same-prio.patch (redmine#4003)
- add 0014-Revert-Fix-direction-problem-when-target_type-is-por.patch (redmine#4205)
- add 0015-fix-redmine-4163-queue-rate-error-in-qos_db.py.patch (redmine#4163)

* Mon Jun 01 2015 Xu Meihong <meihong.xu@eayun.com> 2014.2-15.eayunstack.1.0
- merge neutron-qos feature (redmine#3678)

* Mon May 25 2015 Zhao Chao <chao.zhao@eayun.com> 2014.2-14.eayunstack.1.0
- add 0011-Use-stop-method-on-MessageHandlingServer.patch
- add out-of-tree-patches/neutron-server.service-workaournd-for-service-stop-r.patch

* Thu May 21 2015 Xu Meihong <meihong.xu@eayun.com> 2014.2-13.eayunstack.1.0
- add 0010-vpnaas-add-ipsec-env-rootwrap-filter.patch (redmine#3721)

* Mon May 11 2015 Xu Meihong <meihong.xu@eayun.com> 2014.2-12.eayunstack.1.0
- Add libreswan dependency
- Fix redmine #3556
- Fix redmine #3651
- Fix redmine #3659

* Tue Nov 25 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.2-11
- CVE-2014-7821: Fix hostname regex pattern, rhbz#1165886, rhbz#1165887

* Tue Nov 25 2014 Alan Pevec <apevec@redhat.com> 2014.2-10
- Drop and recreate FK to support MariaDB 10, rhbz#1157599
- Drop "Create DHCP port for IPv6 subnet" due to regression:
  https://bugs.launchpad.net/neutron/+bug/1392564

* Thu Nov 13 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.2-9
- Revert to 755 permissions for /var/lib/neutron since dnsmasq drops
  'neutron' user and runs as 'nobody' by default, rhbz#1163759

* Tue Nov 11 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.2-8
- Added pacemaker OCF resources

* Tue Nov 11 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.2-7
- don't kill children of agents, rhbz#1063427

* Fri Oct 31 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.2-6
- added keepalived as runtime dependency for L3 agent

* Fri Oct 31 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.2-5
- added conntrack-tools as runtime dependency for L3 agent, rhbz#1158871

* Wed Oct 29 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.2-4
- Made /var/log/neutron and /var/lib/neutron permissions more strict
  (0755 -> 0750) since those directories may contain sensitive data,
  rhbz#1149688

* Wed Oct 29 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.2-3
- Create DHCP port for IPv6 subnet, bz#1158507

* Fri Oct 17 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.2-2
- Moved neutron-ovs-cleanup systemd service file into base package too.

* Fri Oct 17 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.2-1
- Update to upstream 2014.2

* Thu Oct 16 2014 Miguel Ángel Ajo <majopela@redhat.com> 2014.2-0.15.rc3
- neutron-netns-cleanup (network namespaces cleanup) service definition added.
- Enables RemainAfterExit for the oneshot neutron-ovs-cleanup script,
  to make it compatible with manual pacemaker deployments as an agents
  pre/post.

* Wed Oct 15 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.2-0.14.rc3
- Update to upstream 2014.2.rc3

* Fri Oct 10 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.2-0.13.rc2
- Updated some of dependencies to reflect epoches and version numbers in Fedora

* Fri Oct 10 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.2-0.12.rc2
- Updated dependencies to reflect upstream requirements.txt

* Fri Oct 10 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.2-0.11.rc2
- Update to upstream 2014.2.rc2

* Tue Oct 07 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.2-0.10.rc1
- use macroized systemd scriptlets, rhbz#850253

* Fri Oct 03 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.2-0.9.rc1
- Update to upstream 2014.2.rc1

* Tue Sep 30 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.2-0.8.b3
- Removed service_providers from neutron-dist.conf, rhbz#1022725

* Thu Sep 25 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.2-0.7.b3
- Forbid regular users to reset admin-only attrs to default values, rhbz#1142012

* Mon Sep 15 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.2-0.6.b3
- python-jsonrpclib is now available in Fedora.
- python-oslo-rootwrap >= 1.3.0.0.a1 is now available in Fedora.

* Mon Sep 15 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.2-0.5.b3
- Split embrane pieces into separate plugin package.

* Fri Sep 12 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.2-0.4.b3
- Added radvd as a dependency for IPv6 address management.

* Fri Sep 12 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.2-0.3.b3
- Update to upstream 2014.2.b3

* Mon Aug 18 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.2-0.2.b2
- Moved neutron-ovs-cleanup from openvswitch plugin package into base
  package, for it may be used by other plugins (f.e. ofagent).

* Thu Jul 31 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.2-0.1.b2
- Update to upstream 2014.2.b2
- Moved python dependencies from plugin and agent and server packages to
  python-neutron
- Synchronized dependencies with u/s, made all version requirements
  explicit
- Removed python-configobj dependency (seems to be obsolete)

* Wed Jul 23 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1.1-8
- no quota for allowed address pair, rhbz#1121941

* Wed Jul 16 2014 Miguel Ángel Ajo <majopela@redhat.com> 2014.1.1-7
- Moved all plugin sources to python-neutron to avoid breaking
  hidden upstream dependencies from agents to plugins, etc.
  fixes rhbz#1119619
- Removed the hyper-v agent exclude.
- Added a few LICENSE files to packages that missed it.

* Thu Jul 10 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1.1-6
- removed 'noreplace' tag from sudoers file to reflect change in RHEL-OSP

* Wed Jul 02 2014 Jakub Libosvar <jlibosva@redhat.com> 2014.1.1-5
- Disable nova notifications by default, bz#1093879

* Wed Jun 25 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1.1-4
- remove token from notifier middleware, bz#1112948

* Tue Jun 24 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1.1-3
- Send SIGTERM signal only to parent process when stopping neutron
  service, bz#1110642

* Tue Jun 24 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1.1-2
- Notify systemd when starting Neutron server, bz#1063427

* Fri Jun 13 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1.1-1
- Update to upstream 2014.1.1
- Added previously missing ml2_conf_mlnx.ini, bz#1100136

* Wed Jun 11 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-22
- Ensure routing key is specified in the address for a direct producer, bz#1108025

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Miguel Ángel Ajo <majopela@redhat.com> 2014.1-20
- Add nuage plugin packaging as openstack-neutron-nuage

* Wed May 28 2014 Miguel Angel Ajo <majopela@redhat.com> 2014.1-19
- Remove kernel version check for OVS VXLAN, not revelant for RDO
  bz#1081011

* Mon May 19 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-18
- netaddr<=0.7.10 raises ValueError instead of AddrFormatError, bz#1090137

* Mon May 19 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-17
- Validate CIDR given as ip-prefix in security-group-rule-create, bz#1090137

* Fri May 16 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-16
- Fixed neutron-server startup due to duplicate options

* Thu May 15 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-15
- Make neutron-vpn-agent read fwaas_driver.ini, bz#1098121

* Tue Apr 29 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-14
- Removed signing_dir from neutron-dist.conf, again (bz#1050842)

* Mon Apr 28 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-13
- Removed signing_dir from neutron.conf (bz#1050842)

* Wed Apr 23 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-12
- Removed obsolete setup scripts

* Tue Apr 22 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-11
- Pin python-novaclient dependency to >= 2.17.0

* Fri Apr 18 2014 Pádraig Brady <pbrady@redhat.com> - 2014.1-10
- Remove uneeded dep on python-keystone

* Fri Apr 18 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-9
- Require python-novaclient (used for Nova notifications)

* Fri Apr 18 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-8
- We no longer specify notification_driver in neutron-dist.conf

* Fri Apr 18 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-7
- Move api-paste.ini to /usr to make sure new values are applied on upgrade

* Fri Apr 18 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-6
- Add more build directories

* Fri Apr 18 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-5
- Require python-keystoneclient >= 0.7.0 to reflect upstream requirement

* Fri Apr 18 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-4
- Require python-keystone package

* Fri Apr 18 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-3
- Clean up neutron-dist.conf to reflect identical upstream defaults

* Fri Apr 18 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-2
- Set use_stderr = False to avoid duplicate logging for stderr

* Fri Apr 18 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-1
- Update to upstream 2014.1

* Tue Apr 15 2014 Miguel Ángel Ajo <majopela@redhat.com> -2014.1-0.19.rc2
- Include the systemd readiness notification patch

* Tue Apr 15 2014 Pádraig Brady <pbrady@redhat.com> - 2014.1-0.18.rc2
- Add missing dependency on python-oslo-rootwrap

* Fri Apr 11 2014 Miguel Angel Ajo <mangelajo@redhat.com> 2014.1-0.17.rc2
- Update to upstream 2014.1.rc2

* Fri Apr 11 2014 Miguel Ángel Ajo <majopela@redhat.com> 2014.1-0.16.rc1
- Use rabbitmq by default

* Thu Apr 10 2014 Miguel Ángel Ajo <majopela@redhat.com> 2014.1-0.15.rc1
- Removes the python-pyudev dependency, bz#1053001

* Thu Apr 10 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-0.14.rc1
- Remove signing_dir from neutron-dist.conf, bz#1050842

* Fri Apr 04 2014 Pádraig Brady <pbrady@redhat.com> - 2014.1-0.13.rc1
- Fix startup issue due to invalid group permissions, bz#1080560

* Wed Apr 02 2014 Terry Wilson <twilson@redhat.com> 2014.1-0.12.rc1
- Update to upstream 2014.1.rc1
- Remove python-psutil requirement

* Mon Mar 24 2014 Pádraig Brady <pbrady@redhat.com> - 2014.1-0.11.b3
- Remove runtime dependency on python-pbr

* Wed Mar 19 2014 Miguel Ángel ajo <majopela@redhat.com> - 2013.1-0.10.b3
- Create agents table when ML2 core_plugin is used

* Tue Mar 11 2014 Miguel Ángel Ajo <majopela@redhat.com> - 2013.1-0.9.b3
- Forcing python-six version to be at least >= 1.4.1

* Tue Mar 11 2014 Miguel Ángel Ajo <majopela@redhat.com> - 2014.1-0.8.b3
- Updated to Icehouse milestone 3 
- Added neutron-dhcp-agent dependency bz#1019487
- Add openstack-neutron-ibm plugin
- Add openstack-neutron-ofagent plugin from ryu project

* Wed Feb 19 2014 Pádraig Brady <pbrady@redhat.com> - 2014.1-0.7.b2
- Sync up Quantum renaming changes

* Thu Feb 13 2014 Terry Wilson <twilson@redhat.com> - 2014.1-0.6.b2
- Rename nicira plugin to vmware

* Tue Feb 04 2014 Pádraig Brady <pbrady@redhat.com> - 2014.1-0.5.b2
- Fix missing dependency on python-stevedore

* Mon Jan 27 2014 Terry Wilson <twilson@redhat.com> - 2014.1-0.4.b2
- Update to icehouse milestone 2

* Fri Jan 24 2014 Terry Wilson <twilson@redhat.com> - 2014.1-0.3.b1
- Remove requirements.txt, bz#1057615

* Tue Jan 07 2014 Terry Wilson <twilson@redhat.com> - 2014.1-0.2.b1
- Add python-psutil requirement for openvswitch agent, bz#1049235

* Mon Dec 23 2013 Pádraig Brady <pbrady@redhat.com> - 2014.1-0.1.b1
- Update to icehouse milestone 1

* Wed Dec 18 2013 Pádraig Brady <pbrady@redhat.com> - 2013.2.1-1
- Update to havana stable release 2013.2.1

* Tue Dec 10 2013 Terry Wilson <twilson@redhat.com> - 2013.2-6
- Add rootwrap.conf limitation to sudoers.d/neutron, bz#984097
- neutron-server-setup: support mariadb

* Wed Dec 04 2013 Terry Wilson <twilson@redhat.com> - 2013.2-5
- Add missing debug and vpnaas rootwrap filters, bz#1034207

* Mon Dec 02 2013 Terry Wilson <twilson@redhat.com> - 2013.2-4
- Replace quantum references in neutron-dist.conf

* Wed Nov 13 2013 Terry Wilson <twilson@redhat.com> - 2013.2-3
- Add dnsmasq-utils dependency

* Wed Oct 30 2013 Terry Wilson <twilson@redaht.com> - 2013.2-2
- Better support for upgrading from grizzly to havana
- Update dependencies on python-{babel,keystoneclient,oslo-config}

* Fri Oct 18 2013 Pádraig Brady <pbrady@redhat.com> - 2013.2-1
- Update to havana GA

* Thu Oct 10 2013 Terry Wilson <twilson@redhat.com> - 2013.2-0.12.rc1
- Update to havana rc1

* Wed Oct  2 2013 Terry Wilson <twilson@redhat.com> - 2013.2-0.11.b3
- Add python-jinja2 requires to VPN agent
- Add missing services and pre/postuns for VPN and metering agents

* Thu Sep 26 2013 Terry Wilson <twilson@redhat.com> - 2013.2-0.10.b3
- Add support for neutron-dist.conf

* Tue Sep 17 2013 Pádraig Brady <pbrady@redhat.com> - 2013.2-0.9.b3
- Fix typo in openstack-neutron-meetering-agent package name

* Tue Sep 10 2013 Terry Wilson <twilson@redhat.com> - 2013.2-0.8.b3
- Add python-pbr dependency (for now)

* Mon Sep 09 2013 Terry Wilson <twilson@redhat.com> - 2013.2-0.6.b3
- Update to havana milestone 3 release

* Mon Aug 26 2013 Terry Wilson <twilson@redhat.com> - 2013.2-0.5.b2
- Add provides/obsoletes for subpackages

* Mon Aug 19 2013 Terry Wilson <twilson@redhat.com> - 2013.2-0.4.b2
- Updated to havana milestone 2 release
- Renamed quantum to neutron

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.2-0.3.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Terry Wilson <twilson@redhat.com> - 2013.2-0.2.b1
- Update to havana milestone 1 release

* Fri Jun 07 2013 Terry Wilson <twilson@redhat.com> - 2013.1.2-1
- Update to grizzly 2013.1.2 release

* Fri May 24 2013 Pádraig Brady <P@draigBrady.com> - 2013.1.1-5
- Fix inclusion of db migrations

* Thu May 23 2013 Gary Kotton <gkotton@redhat.com> - 2013.1.1-4
- Fix rootwrap (bug 947793)

* Mon May 20 2013 Terry Wilson <twilson@redhat.com> - 2013.1.1-3
- Fix swapped l3-agent and lbaas-agent service definitions

* Mon May 13 2013 Gary Kotton <gkotton@redhat.com> - 2013.1.1-2
- Update to grizzly release
- Update install scripts to configure security groups
- Update install scripts to remove virtual interface configurations

* Wed Apr  3 2013 Gary Kotton <gkotton@redhat.com> - 2013.1-1
- Update to grizzly release

* Wed Apr  3 2013 Gary Kotton <gkotton@redhat.com> - 2013.1-0.7.rc3
- Update to grizzly rc3
- Update rootwrap (bug 947793)
- Update l3-agent-setup to support qpid (bug 947532)
- Update l3-agent-setup to support metadata-agent credentials
- Update keystone authentication details (bug 947776)

* Tue Mar 26 2013 Terry Wilson <twilson@redhat.com> - 2013.1-0.6.rc2
- Update to grizzly rc2

* Tue Mar 12 2013 Pádraig Brady <P@draigBrady.Com> - 2013.1-0.5.g3
- Relax the dependency requirements on sqlalchemy

* Mon Feb 25 2013 Robert Kukura <rkukura@redhat.com> - 2013.1-0.4.g3
- Update to grizzly milestone 3
- Add brocade, hyperv, midonet, and plumgrid plugins as sub-packages
- Remove cisco files that were eliminated
- Add quantum-check-nvp-config
- Include patch for https://code.launchpad.net/bugs/1132889
- Require python-oslo-config
- Require compatible version of python-sqlalchemy
- Various spec file improvements

* Thu Feb 14 2013 Robert Kukura <rkukura@redhat.com> - 2013.1-0.3.g2
- Update to grizzly milestone 2
- Add quantum-db-manage, quantum-metadata-agent,
  quantum-ns-metadata-proxy, quantum-ovs-cleanup, and
  quantum-usage-audit executables
- Add systemd units for quantum-metadata-agent and quantum-ovs-cleanup
- Fix /etc/quantum/policy.json permissions (bug 877600)
- Require dnsmasq (bug 890041)
- Add the version info file
- Remove python-lxml dependency
- Add python-alembic dependency

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.1-0.2.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec  5 2012 Robert Kukura <rkukura@redhat.com> - 2013.1-0.1.g1
- Update to grizzly milestone 1
- Require python-quantumclient >= 1:2.1.10
- Remove unneeded rpc control_exchange patch
- Add bigswitch plugin as sub-package
- Work around bigswitch conf file missing from setup.py

* Mon Dec  3 2012 Robert Kukura <rkukura@redhat.com> - 2012.2.1-1
- Update to folsom stable 2012.2.1
- Turn off PrivateTmp for dhcp_agent and l3_agent (bug 872689)
- Add upstream patch: Fix rpc control_exchange regression.
- Remove workaround for missing l3_agent.ini

* Fri Sep 28 2012 Robert Kukura <rkukura@redhat.com> - 2012.2-1
- Update to folsom final
- Require python-quantumclient >= 1:2.1.1

* Sun Sep 23 2012 Gary Kotton <gkotton@redhat.com> - 2012.2-0.9.rc2
- Update to folsom rc2

* Sun Sep 16 2012 Robert Kukura <rkukura@redhat.com> - 2012.2-0.9.rc1
- Fix setting admin_user in quantum_l3_setup

* Fri Sep 14 2012 Robert Kukura <rkukura@redhat.com> - 2012.2-0.8.rc1
- Setup script fixes from garyk
- Fix openvswitch service config file path
- Make log file names consistent with service names

* Thu Sep 13 2012 Robert Kukura <rkukura@redhat.com> - 2012.2-0.7.rc1
- Fix various issues in setup scripts
- Configure quantum-dhcp-agent to store files under /var/lib/quantum
- Make config files with passwords world-unreadable
- Replace bug workarounds with upstream patches

* Wed Sep 12 2012 Robert Kukura <rkukura@redhat.com> - 2012.2-0.6.rc1
- Require python-quantumclient >= 2.0.22
- Add bug references for work-arounds
- Use /usr/share/quantum/rootwrap instead of /usr/share/quantum/filters

* Wed Sep 12 2012 Robert Kukura <rkukura@redhat.com> - 2012.2-0.5.rc1
- Update to folsom rc1
- Fix command lines in agent systemd units
- Fix setup scripts
- Fix configuration of agents to use quantum-rootwrap
- Set "debug = False" and "auth_strategy = noauth" in quantum.conf
- Symlink /etc/quantum/plugin.ini to plugin's config file
- Add "--config-file /etc/quantum/plugin.ini" to ExecStart in quantum-server.service

* Tue Sep 11 2012 Robert Kukura <rkukura@redhat.com> - 2012.2-0.4.rc1.20120911.1224
- Update to folsom rc1 snapshot
- Add support for new agents, plugins and rootwrap

* Wed Aug 22 2012 Pádraig Brady <P@draigBrady.com> - 2012.2-0.3.f2
- Fix helper scripts to setup the database config correctly (#847785)

* Tue Aug  7 2012 Robert Kukura <rkukura@redhat.com> - 2012.2-0.2.f2
- Include quantum module no longer provided by python-quantumclient
- Update description text
- Disable setuptools_git dependency

* Tue Aug  7 2012 Robert Kukura <rkukura@redhat.com> - 2012.2-0.1.f2
- Update to folsom milestone 2

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 28 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-2
- Fix helper scripts to use the always available openstack-config util

* Mon Apr  9 2012 Robert Kukura <rkukura@redhat.com> - 2012.1-1
- Update to essex release

* Thu Apr  5 2012 Robert Kukura <rkukura@redhat.com> - 2012.1-0.7.rc2
- Update to essex rc2 milestone
- Use PrivateTmp for services

* Wed Mar 21 2012 Robert Kukura <rkukura@redhat.com> - 2012.1-0.6.rc1
- Update to official essex rc1 milestone
- Add quantum-server-setup and quantum-node-setup scripts
- Use hand-coded agent executables rather than easy-install scripts
- Make plugin config files mode 640 and group quantum to protect passwords

* Mon Mar 19 2012 Robert Kukura <rkukura@redhat.com> - 2012.1-0.5.e4
- Update to essex possible RC1 tarball
- Remove patches incorporated upstream
- Don't package test code
- Remove dependencies only needed by test code

* Wed Mar 14 2012 Robert Kukura <rkukura@redhat.com> - 2012.1-0.4.e4
- Upstream patch: add root_helper to quantum agents
- Add sudoers file enabling quantum-rootwrap for quantum user
- Configure plugin agents to use quantum-rootwrap
- Run plugin agents as quantum user

* Fri Mar  9 2012 Robert Kukura <rkukura@redhat.com> - 2012.1-0.3.e4
- Add upstream patch: remove pep8 and strict lxml version from setup.py
- Remove old fix for pep8 dependency
- Add upstream patch: Bug #949261 Removing nova drivers for Linux Bridge Plugin
- Add openvswitch dependency

* Mon Mar  5 2012 Robert Kukura <rkukura@redhat.com> - 2012.1-0.2.e4
- Update to essex milestone 4
- Move plugins to sub-packages
- Systemd units for agents

* Mon Jan 30 2012 Robert Kukura <rkukura@redhat.com> - 2012.1-0.1.e3
- Update to essex milestone 3 for F17

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov  17 2011 Robert Kukura <rkukura@redhat.com> - 2011.3-1
- Initial package for Fedora
