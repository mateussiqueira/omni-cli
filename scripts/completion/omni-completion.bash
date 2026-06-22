#!/bin/bash
# Omni CLI Bash completion
# Source this file in your ~/.bashrc:
#   source /path/to/omni-completion.bash

_omni_completion() {
    local cur prev opts
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    opts="version status memory mcp hostinger github unleash config --help --version"

    case "$prev" in
        memory)
            opts="status setup monitor cache-move --help"
            ;;
        mcp)
            opts="list add remove test --help"
            ;;
        hostinger)
            opts="domains vps dns --help"
            ;;
        github)
            opts="repos trending clone --help"
            ;;
        unleash)
            opts="flags toggle create --help"
            ;;
        config)
            opts="show set env init --help"
            ;;
    esac

    COMPREPLY=( $(compgen -W "$opts" -- "$cur") )
}

complete -F _omni_completion omni
