def convert_length(value, from_unit, to_unit):
    base_factors = {
        'millimeter': 0.001,
        'centimeter': 0.01,
        'meter': 1,
        'kilometer': 1000,
        'inch': 0.0254,
        'foot': 0.3048,
        'yard': 0.9144,
        'mile': 1609.34
    }

    if isinstance(value, (int, float)):
        if from_unit not in base_factors or to_unit not in base_factors:
            raise ValueError(f"Unsupported units: {from_unit} or {to_unit}")
        elif value < 0:
            raise ValueError(f"Value must be positive: {value}")


        value_in_meters = value * base_factors[from_unit]
        result = value_in_meters / base_factors[to_unit]

        return result
    else:
        raise TypeError(f"Unsupported type must be numeric")

def convert_weight(value, from_unit, to_unit):
    base_factors = {
        'miligram': 0.000001,
        'grams': 0.001,
        'kilogram': 1,
        'ounces': 0.028,
        'pound': 0.45,
    }

    if isinstance(value, (int, float)):
        if from_unit not in base_factors or to_unit not in base_factors:
            raise ValueError(f"Unsupported units: {from_unit} or {to_unit}")
        elif value < 0:
            raise ValueError(f"Value must be positive: {value}")


        value_in_kilograms = value * base_factors[to_unit]
        result = value_in_kilograms / base_factors[from_unit]

        return result
    else:
        raise TypeError(f"Unsupported type must be numeric")

def convert_temperature(value, from_unit, to_unit):
    base_factors = {
        'celsius': 1,
        'fahrenheit': lambda c: c * 9/5 + 32,
        'kelvin': lambda c: c + 273.15,
    }

    if from_unit not in base_factors or to_unit not in base_factors:
        raise ValueError(f"Unsupported units: {from_unit} or {to_unit}")

    if isinstance(value, (int, float)):
        if from_unit == 'fahrenheit':
            value_in_celsius = (value - 32) * 5/9
        elif from_unit == 'kelvin':
            value_in_celsius = value - 273.15
        else:
            value_in_celsius = value


        if to_unit == 'fahrenheit':
            result = base_factors['fahrenheit'](value_in_celsius)
        elif to_unit == 'kelvin':
            result = base_factors['kelvin'](value_in_celsius)
        else:
            result = value_in_celsius

        return result
    else:
        raise TypeError(f"Unsupported type must be numeric")
