#!/usr/bin/env bash

PACKAGE_VERSION=${PACKAGE_VERSION:-2.5.1-SNAPSHOT}
PACKAGE_ITERATION=${PACKAGE_ITERATION:-1}
PACKAGE_FORMATS=${PACKAGE_FORMATS:-deb rpm}

LICENSE="Copyright © 2018 Splice Machine Inc. Licensed under the Apache License, Version 2.0."
RPM_FPM_ARGS="-t rpm --rpm-os linux"
DEB_FPM_ARGS="-t deb"

if [[ ${PACKAGE_VERSION} =~ "-SNAPSHOT" ]] ; then
  PACKAGE_VERSION=${PACKAGE_VERSION/-SNAPSHOT/.$(date +%s)}
fi

clean() { rm -rf build target; };
setup() { mkdir -p build/var/lib/ambari-server/resources target; };

install() {
  cp -a src/main/resources/* build/var/lib/ambari-server/resources
}

clean && setup && install

__failed=0
cd target
for p in ${PACKAGE_FORMATS} ; do
  case ${p} in
    deb)
      fpm \
        --name splicemachine-ambari-service \
        --license "${LICENSE}" \
        --vendor "Splice Machine Inc." \
        --maintainer support@splicemachine.com \
        --description "Splice Machine Install for HDP" \
        -s dir \
        -a all \
        --url "http://www.splicemachine.com" \
        --category misc \
        --depends "python > 2.6" \
        --depends "ambari-server > 2.2" \
        --version ${PACKAGE_VERSION} \
        --iteration ${PACKAGE_ITERATION} \
        ${DEB_FPM_ARGS} \
        -C ../build \
        var
      __ret=$?
      ;;
    rpm)
      fpm \
        --name splicemachine-ambari-service \
        --license "${LICENSE}" \
        --vendor "Splice Machine Inc." \
        --maintainer support@splicemachine.com \
        --description "Splice Machine Install for HDP" \
        -s dir \
        -a all \
        --url "http://cask.co" \
        --category misc \
        --depends "python > 2.6" \
        --depends "ambari-server > 2.2" \
        --version ${PACKAGE_VERSION} \
        --iteration ${PACKAGE_ITERATION} \
        ${RPM_FPM_ARGS} \
        -C ../build \
        var
      __ret=$?
     ;;
    *)
      echo "Unsupported format! ${p}"
      exit 1
      ;;
  esac
  [[ ${__ret} -ne 0 ]] && __failed=1
done

exit ${__failed} # It's okay if this is empty