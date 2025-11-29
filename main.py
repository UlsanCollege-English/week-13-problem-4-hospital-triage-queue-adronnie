def select_patients(patients, k):
    """
    Select up to k patient names in the order they should be called.

    Patients are dictionaries with:
      - "name": string
      - "severity": integer 1 (most urgent) to 5 (least urgent)
      - "arrival_order": integer, smaller means arrived earlier
    """

    # If no patients or k is 0 → return empty
    if not patients or k == 0:
        return []

    # Sort by (severity, arrival_order)
    ordered = sorted(patients, key=lambda p: (p["severity"], p["arrival_order"]))

    # Take first k and return only names
    return [p["name"] for p in ordered[:k]]


if __name__ == "__main__":
    # Optional manual test
    sample_patients = [
        {"name": "Alex", "severity": 3, "arrival_order": 5},
        {"name": "Bella", "severity": 1, "arrival_order": 6},
        {"name": "Chris", "severity": 1, "arrival_order": 2},
    ]
    print(select_patients(sample_patients, 2))
