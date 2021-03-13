#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json

if len(sys.argv) > 1:
    field = str(sys.argv[1])

    # verify that a json-type file has been passed
    if len(sys.argv) > 2:
        json_object = json.loads(open(str(sys.argv[2])).read())
    else:
        json_object = None

else:
    field = None

# if not exists json type file return a error
if json_object is not None:

    # Return all data for default
    results = json_object

    if field is not None and field != "":
        # it searches in the first level and if it finds the field, it returns the data
        results = json_object.get(field, None)

        if results is None:

            for object_1 in json_object.keys():

                # it searches in the second level and if it finds the field, it returns the data
                try:
                    results = json_object.get(object_1, None).get(field, None)
                    if results is not None:
                        break
                    else:
                        sub_object = json_object.get(object_1, None)
                        for object2 in sub_object.keys():

                            # it searches in the third level and if it finds the field, it returns the data
                            try:
                                results = sub_object.get(object2, None).get(field, None)
                                if results is not None:
                                    break
                            except:
                                continue
                except:
                    continue
    if results is None:
        results = "El campo buscado no existe o no fue encontrado"
    
    print(results)
else:
    print("Debe de pasar un archivo para realizar la busqueda")
