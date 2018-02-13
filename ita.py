#!/usr/bin/env python3
import argparse
import subprocess

parser = argparse.ArgumentParser(
	description="La nuova versione del programma che permette di installare programmi più facilmente"
	)
__version__ = "0.0.1"
subparsers = parser.add_subparsers()

def fun_installa(args):
	subprocess.run(["dnf", "install", args.pacchetto, "-y"], stderr=subprocess.STDOUT)
	print(subprocess.STDOUT)
def fun_cerca(args):
	subprocess.run(["dnf", "search", args.pacchetto, "-y"], stderr=subprocess.STDOUT)
	print(subprocess.STDOUT)

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
