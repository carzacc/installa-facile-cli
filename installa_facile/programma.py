# Copyright 2018 Carmine Zaccagnino
#  
# Concesso in licenza a norma dell'EUPL, esclusivamente
# versione 1.2 (la "Licenza");
# Non è possibile utilizzare l'opera salvo nel rispetto
# della Licenza.
# È possibile ottenere una copia della Licenza al seguente
# indirizzo: 
#  
# https://joinup.ec.europa.eu/software/page/eupl
#
#  
# Salvo diversamente indicato dalla legge applicabile o
# concordato per iscritto, il software distribuito secondo
# i termini della Licenza è distribuito "TAL QUALE",
# SENZA GARANZIE O CONDIZIONI DI ALCUN TIPO,
# esplicite o implicite.
# Si veda la Licenza per la lingua specifica che disciplina
# le autorizzazioni e le limitazioni secondo i termini della
# Licenza.
import argparse
import subprocess

def fun_installa(args):
    subprocess.run(["dnf", "install", args.pacchetto, "-y"], stderr=subprocess.STDOUT)
    print(subprocess.STDOUT)

def fun_cerca(args):
    subprocess.run(["dnf", "search", args.pacchetto, "-y"], stderr=subprocess.STDOUT)
    print(subprocess.STDOUT)

def main():
    parser = argparse.ArgumentParser(
        description="La nuova versione del programma che permette di installare programmi più facilmente"
    )
    __version__ = "0.0.1"
    subparsers = parser.add_subparsers()
    
    installa = subparsers.add_parser("installa", help="installa un pacchetto")
    installa.add_argument('pacchetto', type=str, help='Nome del programma da installare')

    cerca = subparsers.add_parser("cerca", help="cerca un pacchetto")
    cerca.add_argument('pacchetto', type=str, help='Nome del programma da cercare')

    installa.set_defaults(func=fun_installa)
    cerca.set_defaults(func=fun_cerca)

    parser.add_argument(
        '--version',
       action='version',
       version=__version__
    )
    args = parser.parse_args()
    args.func(args)
