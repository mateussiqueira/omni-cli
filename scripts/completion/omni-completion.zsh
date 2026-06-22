#compdef omni
# Omni CLI Zsh completion
# Place this file in a directory in $fpath, e.g.:
#   sudo cp omni-completion.zsh /usr/local/share/zsh/site-functions/_omni

_omni() {
    local curcontext="$curcontext" state line
    typeset -A opt_args

    _arguments -C \
        '(-h --help)'{-h,--help}'[Show help]' \
        '(-v --version)'{-v,--version}'[Show version]' \
        '*:: :->subcmd'

    case "$state" in
        subcmd)
            case "$line[1]" in
                memory)
                    _values 'memory command' \
                        'status[Show memory status]' \
                        'setup[Setup Thunderbolt SSD]' \
                        'monitor[Start memory monitor]' \
                        'cache-move[Move app cache]'
                    ;;
                mcp)
                    _values 'mcp command' \
                        'list[List MCP servers]' \
                        'add[Add MCP server]' \
                        'remove[Remove MCP server]' \
                        'test[Test MCP server]'
                    ;;
                hostinger)
                    _values 'hostinger command' \
                        'domains[List domains]' \
                        'vps[List VPS instances]' \
                        'dns[Show DNS records]'
                    ;;
                github)
                    _values 'github command' \
                        'repos[List repositories]' \
                        'trending[Show trending repos]' \
                        'clone[Clone repository]'
                    ;;
                unleash)
                    _values 'unleash command' \
                        'flags[List feature flags]' \
                        'create[Create feature flag]' \
                        'toggle[Toggle feature flag]'
                    ;;
                config)
                    _values 'config command' \
                        'show[Show configuration]' \
                        'set[Set configuration value]' \
                        'env[Show environment variables]' \
                        'init[Interactive setup]'
                    ;;
                *)
                    _values 'omni command' \
                        'version[Show version]' \
                        'status[Show status]' \
                        'memory[Memory optimization]' \
                        'mcp[MCP server management]' \
                        'hostinger[Hostinger management]' \
                        'github[GitHub operations]' \
                        'unleash[Unleash feature flags]' \
                        'config[Configuration]'
                    ;;
            esac
            ;;
    esac
}

_omni "$@"
