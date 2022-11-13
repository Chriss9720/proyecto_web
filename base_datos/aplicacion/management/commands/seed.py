import os
import json
from django.core.management.base import BaseCommand

from aplicacion.models import Pais, Ciudad

# from catalogos_modular.models import User, TipoUsuario
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class Command(BaseCommand):
    help = "Seed the database's catalogues"

    def add_arguments(self, parser):
        parser.add_argument("--mode", type=str, help="Mode")

    def handle(self, *args, **options):
        run_seed()
        self.stdout.write("Finished data seeding.")

def PaisesEstados():
    f = open(f"{BASE_DIR}/commands/json/countries+states+cities.json", "r", encoding="utf-8")

    print("Insertando paises y estados...")
    json_array = json.load(f)
    total = len(json_array) - 1
    for cont, value in enumerate(json_array):
        print(f"{cont} de {total}")
        pais = Pais.objects.get_or_create(
            clave = value['iso3'],
            pais = value['name']
        )
        for index, state in enumerate(value['states']):
            Ciudad.objects.get_or_create(
                clave = state['state_code'],
                ciudad = state['name'],
                pais = pais[0]
            )
            if (index > 5):
                break

def run_seed():
    PaisesEstados()