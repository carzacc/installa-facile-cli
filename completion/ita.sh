_ita()
{
	local corrente precedente
	COMPREPLY=()
	corrente="${COMP_WORDS[COMP_CWORD]}"
	precedente="${COMP_WORDS[COMP_CWORD-1]}"
	opzioni="-h --help --version"
	sottocomandi="--help --version installa cerca"
	if [[ ${cur} == -* ]] ; then
		COMPREPLY=( $(compgen -W "${opzioni}" -- ${corrente}) )
		return 0
	else
		case ${precedente} in
			-h|--help|--version)
				return 0
				;;
			installa|cerca)
				COMPREPLY=( $(compgen -W "$(dnf -q search ${corrente} | awk '{print($1)}')" -- ${corrente}) )
				return 0
				;;
		esac

		if [[ ${COMP_CWORD} -eq 1 ]]; then
			COMPREPLY=( $(compgen -W "${sottocomandi}" -- ${corrente}) )
			return 0
		fi
	fi
}
complete -F _ita ita