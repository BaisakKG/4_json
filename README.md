# Prettify JSON

Average monthly nominal accrued wages by occupation in Moscow.

# Quickstart

Example use how module

```python
from pprint_json from load_data, pretty_print_json

f_json = r'd:\PythonScript\Devman\4_json\data-6784-2017-11-21.json'
p_json = load_data(f_json)
pretty_print_json(p_json)
```

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>
# Output example
[
    {
        "AdministrationAndServices": 55560.2,
        "AgricultureHuntingAndFishing": 44261.2,
        "AverageSalaryTotal": 73826.0,
        "Building": 43218.9,
        "CommunicationAndInformation": 87421.8,
        "CultureSportsAndEntertainment": 90357.0,
        "Education": 61270.9,
        "EnergyGasSteamDistribution": 81198.9,
        "ExterritorialOrg": 73438.8,
        "FinancialAndInsurance": 120083.6,
        "HealthcareAndSocialServices": 64161.7,
        "HotelsAndCatering": 35941.7,
        "Manufacturing": 75781.9,
        "Mining": 120491.5,
        "Month": "\u042f\u043d\u0432\u0430\u0440\u044c",
        "OtherServices": 89174.6,
        "ProfessionalScienceAndTech": 107262.0,
        "PublicMilitarySocialAdministration": 53730.9,
        "RealtyOperations": 47935.8,
        "TradingAndAutomotiveRepairs": 68697.5,
        "TransportationAndStorage": 68270.2,
        "WaterSupplyAndWaste": 67688.2,
        "Year": 2017,
        "global_id": 64592464
    },

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
