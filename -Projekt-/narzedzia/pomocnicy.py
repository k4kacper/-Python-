def znajdz_element_po_id(lista, id_elementu):
    return next((element for element in lista if element.id == id_elementu), None)