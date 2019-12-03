#! /usr/bin/bats
#
# Requirements:
#   - bats: https://github.com/sstephenson/bats
#
export _SRCDIR=$(realpath $BATS_TEST_DIRNAME/../../)
export _NAME=$(sed -nr 's/^name.*: (.+)/\1/p' ${_SRCDIR:?}/galaxy.yml |
               sed 'N; s/\n/-/g')

function setup () {
    cd $BATS_TEST_DIRNAME
    export MY_COLLECTION_PATH=${MY_COLLECTION_PATH:-${BATS_TMPDIR:?}}
}

function check_results () {
    [[ ${status} -eq 0 ]] || {
        cat << EOM
output:
${output}
EOM
        exit ${status}
    }
}

@test "Build an Ansible collection artifact" {
    run ansible-galaxy collection build -v --force \
        --output-path ${MY_COLLECTION_PATH:?} ${_SRCDIR}
    check_results
}

@test "Install using ansible-galaxy" {
    run ansible-galaxy collection install -v \
        -p ${MY_COLLECTION_PATH} \
        $(ls -1t ${MY_COLLECTION_PATH}/${_NAME}*.tar.gz | head -n 1)
    check_results
}

# vim:sw=4:ts=4:et:filetype=sh:
