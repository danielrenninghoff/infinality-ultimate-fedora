BASE = fedora-24
DIRS = $(wildcard */)

define makerpm =
$(eval names := $(shell rpmspec --target $(ARCH) -q --qf "%{name}-%{version}-%{release}.%{arch}.rpm " $1*.spec))
spectool -C $1 -g $1*.spec
for f in $(names); do\
	if [ ! -f $1$$f ]; then \
		rpmbuild --define "_tmppath /tmp" --define "_sourcedir $1" --define "_srcrpmdir $1" --nodeps -bs $1*.spec; \
		mock -r $(BASE)-$(ARCH) --resultdir=$1 $1*.src.rpm; \
		break; \
	fi; \
done
endef

all:
	$(foreach dir, $(DIRS), $(call makerpm,$(dir)))

pkg:
	$(call makerpm,$(PKG))

repo:
	mkdir -p repo/$(BASE)/$(ARCH)
	cp */*.$(ARCH).rpm /repo/$(BASE)/$(ARCH)/
