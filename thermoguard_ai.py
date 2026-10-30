
# ThermoGuard AI
# Version 1: Core Temperature Monitoring Engine

from datetime import datetime


def get_temperature(reading_number):
    """Collect and validate one temperature reading."""

    while True:
        try:
            temperature = float(
                input(f"Enter temperature reading {reading_number} (°C): ")
            )

            if temperature < -273.15:
                print("Invalid temperature: below absolute zero.")
            else:
                return temperature

        except ValueError:
            print("Please enter a valid number, such as 45 or 45.5.")


def collect_readings():
    """Collect five temperature readings."""

    readings = []

    for number in range(1, 6):
        temperature = get_temperature(number)
        readings.append(temperature)

    return readings


def analyse_readings(readings, safe_limit):
    """Calculate statistics and identify high readings."""

    highest = max(readings)
    lowest = min(readings)
    average = sum(readings) / len(readings)

    high_readings = []

    for temperature in readings:
        if temperature > safe_limit:
            high_readings.append(temperature)

    return highest, lowest, average, high_readings


def detect_trend(readings):
    """Identify the pattern in temperature readings."""

    rising = True
    falling = True

    for i in range(1, len(readings)):
        if readings[i] <= readings[i - 1]:
            rising = False

        if readings[i] >= readings[i - 1]:
            falling = False

    if rising:
        return "RISING"
    elif falling:
        return "FALLING"
    elif all(value == readings[0] for value in readings):
        return "STABLE"
    else:
        return "FLUCTUATING"


def diagnose_temperature(readings, warning_limit, critical_limit):
    """Assign a diagnostic status based on temperature readings."""

    highest = max(readings)

    if highest >= critical_limit:
        status = "CRITICAL"
        recommendation = (
            "Investigate the high-temperature condition promptly."
        )

    elif highest > warning_limit:
        status = "WARNING"
        recommendation = (
            "Inspect operating conditions and monitor closely."
        )

    else:
        status = "NORMAL"
        recommendation = (
            "Continue routine monitoring."
        )

    return status, recommendation


def calculate_health_score(readings, warning_limit, critical_limit):
    """Calculate an illustrative temperature-based health score."""

    highest = max(readings)

    if highest >= critical_limit:
        score = 30
    elif highest > warning_limit:
        score = 70
    else:
        score = 100

    return score


def save_history(readings, highest, lowest, average,
                 trend, health_score, status, recommendation):
    """Save one monitoring report to a history file."""

    with open("thermoguard_history.txt", "a", encoding="utf-8") as file:
        file.write(
            f"Date and time: {datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S %Z')}\n"
        )
        file.write("\n" + "=" * 40 + "\n")
        file.write("THERMOGUARD AI - MONITORING HISTORY\n")
        file.write(f"Readings: {readings}\n")
        file.write(f"Highest temperature: {highest:.2f} °C\n")
        file.write(f"Lowest temperature: {lowest:.2f} °C\n")
        file.write(f"Average temperature: {average:.2f} °C\n")
        file.write(f"Temperature trend: {trend}\n")
        file.write(f"Health score: {health_score}/100\n")
        file.write(f"Status: {status}\n")
        file.write(f"Recommendation: {recommendation}\n")
        file.write("=" * 40 + "\n")

    print("Monitoring report saved to thermoguard_history.txt")


def display_report(readings, safe_limit, critical_limit):
    """Display the monitoring results."""

    highest, lowest, average, high_readings = analyse_readings(
        readings, safe_limit
    )

    print("\n" + "=" * 40)
    print("       THERMOGUARD AI REPORT")
    print("=" * 40)

    print(f"Readings: {readings}")
    print(f"Highest temperature: {highest:.2f} °C")
    print(f"Lowest temperature: {lowest:.2f} °C")
    print(f"Average temperature: {average:.2f} °C")

    trend = detect_trend(readings)
    print(f"Temperature trend: {trend}")

    status, recommendation = diagnose_temperature(
        readings, safe_limit, critical_limit
    )

    health_score = calculate_health_score(
        readings, safe_limit, critical_limit
    )

    print(f"Machine health score: {health_score}/100")

    print(f"\nSTATUS: {status}")
    print(f"Recommendation: {recommendation}")

    if high_readings:
        print(f"Readings above the limit: {high_readings}")

    print("=" * 40)

    save_history(
        readings, highest, lowest, average,
        trend, health_score, status, recommendation
    )


def main():
    """Start the ThermoGuard monitoring program."""

    safe_limit = 70.0
    critical_limit = 90.0

    print("Welcome to ThermoGuard AI")
    print("Machine Temperature Monitoring Simulator")
    print(f"Warning limit: {safe_limit:.1f} °C")
    print(f"Critical limit: {critical_limit:.1f} °C")

    readings = collect_readings()
    display_report(readings, safe_limit, critical_limit)


if __name__ == "__main__":
    main()