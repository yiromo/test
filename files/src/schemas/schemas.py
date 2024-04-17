def individual_disease(disease) -> dict:
    return {
        "id": str(disease["_id"]),
        "name": disease["name"],
        "description": disease["description"]
    }

def list_diseases(diseases) -> list:
    return[individual_disease(disease) for disease in diseases]
