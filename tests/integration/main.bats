#! /usr/bin/bats
#
# Requirements:
#   - ansible, apparently ;-)
#   - bats: https://github.com/sstephenson/bats
#
function setup () {
    cd $BATS_TEST_DIRNAME
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

@test "Run test playbooks" {
    run ansible-playbook -vv main.yml
    check_results
}

# vim:sw=4:ts=4:et:filetype=sh:
