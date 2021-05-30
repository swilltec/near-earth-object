"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neo_collection = []
    with open(neo_csv_path, 'r') as infile:
        reader = csv.DictReader(infile)


        for elem in reader:
            params = {
                 'designation': elem["pdes"],
                 'name': elem["name"],
                 'hazardous': elem["pha"],
                 'diameter':elem["diameter"] if elem["diameter"] \
                     else "nan"

            }
            neo_collection.append(
                NearEarthObject(**params)
            )

    return neo_collection


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    ca_collection = list()
    with open(cad_json_path, 'r') as infile:
        contents = json.load(infile)

        for key in contents["data"]:
            params = {
            'designation': key[0],
            'time': key[3],
            'distance': key[4],
            'velocity': key[7]

            }

            ca_collection.append(CloseApproach(**params))

    return ca_collection
